#!/usr/bin/env python3
"""Run one board-quality scenario on one Devin model the way the playbook's operator does.

The comparison asks which model drives the skill to the best board, so every model is
driven by the same operator through the same runner, and only the model differs. The
sandbox, the isolation proof, the turn runner and the redaction are the Devin runner's
own, imported unchanged.

The operator sends the scenario's scripted turns in order. After a reply that is an
intake round it first sends the recommended answers, at most twice, as the playbook
tells it to. When the script runs out with no board written, it sends "Yes, go ahead."
at most three times, so a model that stops once more than the script still reaches a
board a grader can score. Each turn is labelled scripted, adaptive or supplementary in
meta.json, and a small classifier's label for each reply's stop is kept as `kind`.

Usage: adaptive_compare.py <system dir> <run folder> <label> <devin model> <scenario id> <file key>
"""
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import devin_playbook_runner as dv  # noqa: E402

INTAKE_ANSWER = "Use your recommended answers."
MAX_INTAKE = 2
MAX_FOLLOW = 3
CLAUDE_BIN = os.path.expanduser("~/.local/bin/claude")
# An empty folder, so the classifier loads no project instructions
CLASSIFY_DIR = os.path.join(os.environ.get("TMPDIR", "/tmp"), "claude-reply-classifier")
BOARD_ID = re.compile(r'boardId\\*"?\s*:\s*\\*"(\d+:\d+)')

CLASSIFY = """Classify one reply from a FigJam drawing assistant that works in stops: intake rounds of
questions about the brief, then a playback of its reading that asks whether the reading is right, then
a write gate that asks permission to write the board, then a delivery that reports the written board.
Answer with one word: INTAKE when the reply asks intake questions about the brief and is not yet the
playback, PLAYBACK, GATE, DELIVERY or OTHER.

Reply:
"""


def kind(reply):
    """The stop one reply ends on, as a one-word label from a small model."""
    os.makedirs(CLASSIFY_DIR, exist_ok=True)
    p = subprocess.run([CLAUDE_BIN, "-p", CLASSIFY + reply[:6000], "--model", "claude-haiku-5-5",
                        "--output-format", "json", "--setting-sources", "project", "--tools", "",
                        "--strict-mcp-config", "--no-session-persistence"],
                       cwd=CLASSIFY_DIR, stdin=subprocess.DEVNULL, capture_output=True, text=True)
    try:
        word = json.loads(p.stdout).get("result", "").strip().upper()
    except ValueError:
        return "OTHER"
    return next((k for k in ("INTAKE", "PLAYBACK", "GATE", "DELIVERY") if k in word), "OTHER")


def boards(session_dir, n):
    """The board ids one turn's `use_figma` calls returned, read from its raw export.

    Any call whose result carries a `boardId` counts, because a model can run the composer from client
    storage, so the code it sends need not hold `const MODEL`.
    """
    path = os.path.join(session_dir, f"export-turn-{n}.json")
    if not os.path.isfile(path):
        return []
    steps = json.load(open(path, encoding="utf-8")).get("steps") or []
    start = max((i for i, s in enumerate(steps) if s.get("source") == "user"), default=-1)
    found = []
    for s in steps[start + 1:]:
        results = {x.get("source_call_id"): x.get("content")
                   for x in ((s.get("observation") or {}).get("results") or [])}
        for tc in s.get("tool_calls") or []:
            args = tc.get("arguments") or {}
            if args.get("tool_name") == "use_figma":
                found += BOARD_ID.findall(str(results.get(tc.get("tool_call_id")) or ""))
    return list(dict.fromkeys(found))


def main():
    system_dir, out, label, model, sid, key = (os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3],
                                               sys.argv[4], sys.argv[5], sys.argv[6])
    dv.MODEL = model
    sk = next(r for r in dv.load_playbook(system_dir, "product-owner") if r["id"] == sid and r["side"] == "skill")
    harness_root = os.path.join(os.environ.get("TMPDIR", "/tmp"), "devin-compare-bench")
    scratch = os.path.join(harness_root, sid)
    sessions = os.path.join(harness_root, ".sessions", sid)
    dest = os.path.join(out, "skill", label, f"{sid} - {sk['slug']}")
    replies = os.path.join(out, "replies", label)
    pin = dv.FILE_PIN.format(key=key)
    failures = []
    for attempt in range(1, dv.ATTEMPTS + 1):
        dv.build(system_dir, "skill", scratch, sk["seed_export"])
        problems = dv.prove_isolation("skill", scratch)
        if problems:
            print(json.dumps({"id": sid, "label": label, "status": "isolation-failed", "problems": problems}))
            return 2
        for d in (sessions, dest):
            shutil.rmtree(d, ignore_errors=True)
            os.makedirs(d)
        queue = [(t, "scripted") for t in sk["turns"]]
        queue[0] = (f"{queue[0][0]}\n\n{pin}", "scripted")
        turns, intake, follow, n, ok, session_id = [], 0, 0, 0, True, None
        before0 = before = dv.snapshot(scratch)
        while queue:
            prompt, role = queue.pop(0)
            n += 1
            r = dv.run_turn(scratch, sessions, session_id, prompt, n, dest, dv.deny_roots(system_dir, harness_root))
            session_id = session_id or r["session_id"]
            after = dv.snapshot(scratch)
            r["ledger"], before = dv.diff(before, after), after
            r["turn"], r["input"], r["role"] = n, prompt, role
            r["boards"] = boards(sessions, n)
            turns.append(r)
            with open(os.path.join(out, "run-log.jsonl"), "a", encoding="utf-8") as fh:
                fh.write(json.dumps({k: v for k, v in r.items() if k not in ("reply", "transcript")}
                                    | {"id": sid, "label": label, "attempt": attempt}) + "\n")
            if r["status"] != "ok":
                ok = False
                failures.append({"attempt": attempt, "turn": n, "status": r["status"], "rc": r["rc"]})
                break
            r["kind"] = kind(r["reply"])
            if r["kind"] == "INTAKE" and intake < MAX_INTAKE:
                intake += 1
                queue.insert(0, (INTAKE_ANSWER, "adaptive"))
            elif (not queue and not any(t.get("composed") for t in turns)
                  and r["kind"] != "DELIVERY" and follow < MAX_FOLLOW):
                follow += 1
                queue.append((INTAKE_ANSWER if r["kind"] == "INTAKE" else dv.FOLLOW_UP, "supplementary"))
            print(json.dumps({"id": sid, "label": label, "turn": n, "role": role, "kind": r["kind"],
                              "figma": r["inner_calls"], "boards": r["boards"]}), flush=True)
        if ok:
            break
        # A failed attempt keeps its evidence beside the retry, never silently replaced
        keep = os.path.join(out, "failed-attempts", label, f"{sid}-attempt-{attempt}")
        shutil.rmtree(keep, ignore_errors=True)
        shutil.copytree(dest, keep)
    changed = dv.diff(before0, dv.snapshot(scratch))
    for rel in changed["created"] + changed["modified"]:
        tgt = os.path.join(dest, "exports", rel)
        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        shutil.copy2(os.path.join(scratch, rel), tgt)
    os.makedirs(replies, exist_ok=True)
    for r in turns:
        open(os.path.join(dest, f"turn-{r['turn']}.md"), "w", encoding="utf-8").write(dv.redact(r["reply"]))
        open(os.path.join(replies, f"{sid}-turn{r['turn']}.txt"), "w", encoding="utf-8").write(dv.redact(r["reply"]))
        dv.write_transcript(os.path.join(dest, f"transcript-turn-{r['turn']}.md"), sk, r["turn"], r["input"], r)
    meta = {"id": sid, "label": label, "model": model, "permission": dv.PERMISSION, "runtime": "devin-adaptive",
            "scenario_file": sk["file"], "file_pin": pin, "scripted_turns": sk["turns"],
            "intake_answers_sent": intake, "follow_ups_sent": follow, "session_id": session_id,
            "attempts": attempt, "failures": failures, "completed": ok,
            "boards": [b for r in turns for b in r["boards"]], "net_file_changes": changed,
            "turns": [{k: v for k, v in r.items() if k not in ("reply", "transcript")} for r in turns]}
    json.dump(meta, open(os.path.join(dest, "meta.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps({"id": sid, "label": label, "status": "ok" if ok else "failed", "attempts": attempt,
                      "turns": len(turns), "boards": meta["boards"]}), flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

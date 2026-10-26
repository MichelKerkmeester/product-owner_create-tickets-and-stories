#!/usr/bin/env python3
"""Run one board-quality scenario on one Devin model the way the playbook's operator does.

The comparison asks which model drives the skill to the best board, so every model is
driven by the same operator through the same runner, and only the model differs. The
sandbox, the isolation proof, the turn runner and the redaction are the Devin runner's
own, imported unchanged.

The operator sends the scenario's scripted turns in order. An intake round takes the
script's own answer while the script still holds one before its "Yes, that reading is
right." turn. Only once those are used up does the operator send the recommended answers,
at most twice, as the playbook tells it to, and never past the script's end in a scenario
that expects no board. When the script runs out with no board written, it sends "Yes, go
ahead." at most three times, so a model that stops once more than the script still reaches
a board a grader can score. Each turn is labelled scripted, adaptive or supplementary in
meta.json, and a small classifier's label for each reply's stop is kept as `kind`.

A scenario's `driver:` frontmatter key changes how it runs. `operator-only` is skipped with
its reason, because it needs a setup step the driver does not run. `new-file` drops the pin
to the test file and keeps only where a new file may go. After the run the scenario's
read-only shell steps run in its sandbox through `scenario_commands.py` into commands.json.

A model id of the form `codex:<model>:<effort>` or `claude:<model>:<effort>` runs on that CLI
through `runtimes.py` instead of Devin, with the same sandbox, operator and record.

Usage: adaptive_compare.py <system dir> <run folder> <label> <model> <scenario id> <file key>
"""
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import devin_playbook_runner as dv  # noqa: E402
import runtimes  # noqa: E402
import scenario_commands  # noqa: E402

INTAKE_ANSWER = "Use your recommended answers."
# The scripted answer to the playback. A scripted turn before it answers an intake round.
READING_YES = "yes, that reading is right"
# Why an operator-only scenario is skipped when its frontmatter gives no reason of its own
OPERATOR_ONLY = "the playbook marks this scenario operator-only, because it needs a setup step the driver does not run"
MAX_INTAKE = 2
MAX_FOLLOW = 3
# Opus 5.5 low would not draw on the pinned file and stopped to ask for a plan, so the
# operator allowed it one new file, in drafts of the Barter team plan and never in a project
# The scripted answer to the write gate, and the phrase a scenario uses for a runtime with no Figma server
WRITE_YES = "yes, go ahead"
NO_FIGMA = "no hosted Figma MCP"
DRAFTS_PIN = ("If you need a new file instead, create it in the Barter team plan and leave it "
              "in drafts, with no project.")
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


def kind(reply, tmp):
    """The stop one reply ends on, as a one-word label from a small model, with the run's own TMPDIR."""
    os.makedirs(CLASSIFY_DIR, exist_ok=True)
    os.makedirs(tmp, exist_ok=True)
    p = subprocess.run([CLAUDE_BIN, "-p", CLASSIFY + reply[:6000], "--model", "claude-haiku-5-5",
                        "--output-format", "json", "--setting-sources", "project", "--tools", "",
                        "--strict-mcp-config", "--no-session-persistence"],
                       cwd=CLASSIFY_DIR, stdin=subprocess.DEVNULL, capture_output=True, text=True,
                       env=dict(os.environ, TMPDIR=tmp))
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


def plan(sk):
    """How the driver runs one scenario, read from its file.

    `driver` is the frontmatter's `driver:` value, `model` when the key is absent. A reason may
    follow the value on the same line or sit in `driver_reason:`. A scenario expects a board only
    when its script answers the write gate itself and a Figma server is there to draw it. Otherwise
    it grades an earlier stop, so the driver adds no follow-up yes."""
    text = open(sk["file"], encoding="utf-8").read()
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = fm.group(1) if fm else ""
    m = re.search(r"^driver:\s*(.+)$", fm, re.M)
    value = m.group(1).strip().strip("\"'") if m else "model"
    mode, _, rest = value.partition(" ")
    why = re.search(r"^driver_reason:\s*(.+)$", fm, re.M)
    reason = rest.strip(" :,()-") or (why.group(1).strip().strip("\"'") if why else "")
    no_figma = NO_FIGMA in text
    return {"driver": mode.rstrip(":,"), "reason": reason or (OPERATOR_ONLY if mode.startswith("operator-only") else ""),
            "no_figma": no_figma,
            "expects_board": not no_figma and any(t.strip().lower().startswith(WRITE_YES) for t in sk["turns"])}


def scripted_answer(queue, sk):
    """Whether the next queued turn is the scenario's own answer to an intake round.

    That is a scripted turn that comes before the script's playback answer, is not itself a gate
    answer and is not the request that opens a chained scenario's own part."""
    if not queue or queue[0][1] != "scripted":
        return False
    i = queue[0][2]
    said = [t.strip().lower() for t in sk["turns"]]
    return (i != sk.get("setup_turns") and not said[i].startswith((READING_YES, WRITE_YES))
            and any(t.startswith(READING_YES) for t in said[i + 1:]))


def main():
    system_dir, out, label, model, sid, key = (os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3],
                                               sys.argv[4], sys.argv[5], sys.argv[6])
    dv.MODEL = model
    spec = runtimes.runtime(model)
    sk = next(r for r in dv.load_playbook(system_dir, "product-owner") if r["id"] == sid and r["side"] == "skill")
    harness_root = os.path.join(os.environ.get("TMPDIR", "/tmp"), "devin-compare-bench")
    scratch = os.path.join(harness_root, sid)
    sessions = os.path.join(harness_root, ".sessions", sid)
    dest = os.path.join(out, "skill", label, f"{sid} - {sk['slug']}")
    replies = os.path.join(out, "replies", label)
    how = plan(sk)
    if how["driver"] == "operator-only":
        print(json.dumps({"id": sid, "label": label, "status": "skipped", "reason": how["reason"]}))
        return 0
    if how["driver"] not in ("model", "new-file"):
        print(json.dumps({"id": sid, "label": label, "status": "bad-driver",
                          "reason": f"unknown driver value {how['driver']}"}))
        return 2
    # A new-file scenario tests making a file, so it keeps only where the new file may go
    if how["driver"] == "new-file":
        pin = DRAFTS_PIN
    else:
        pin = dv.FILE_PIN.format(key=key)
        if spec and spec[0] == "claude":
            pin += " " + DRAFTS_PIN
    # A scenario written for a runtime with no hosted Figma server runs only where one can be left out.
    no_figma, expects_board = how["no_figma"], how["expects_board"]
    if no_figma and not (spec and spec[0] == "claude"):
        print(json.dumps({"id": sid, "label": label, "status": "skipped",
                          "reason": "the scenario needs a runtime without the hosted Figma server"}))
        return 0
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
        queue = [(t, "scripted", i) for i, t in enumerate(sk["turns"])]
        queue[0] = (f"{queue[0][0]}\n\n{pin}", "scripted", 0)
        turns, intake, follow, n, ok, session_id = [], 0, 0, 0, True, None
        before0 = before = dv.snapshot(scratch)
        while queue:
            prompt, role, _ = queue.pop(0)
            n += 1
            if spec:
                r = runtimes.run_turn(spec, scratch, sessions, session_id, prompt, n, dest,
                                      dv.deny_roots(system_dir, harness_root), figma=not no_figma)
            else:
                r = dv.run_turn(scratch, sessions, session_id, prompt, n, dest, dv.deny_roots(system_dir, harness_root))
            session_id = session_id or r["session_id"]
            after = dv.snapshot(scratch)
            r["ledger"], before = dv.diff(before, after), after
            r["turn"], r["input"], r["role"] = n, prompt, role
            r["boards"] = r["boards"] if spec else boards(sessions, n)
            turns.append(r)
            with open(os.path.join(out, "run-log.jsonl"), "a", encoding="utf-8") as fh:
                fh.write(json.dumps({k: v for k, v in r.items() if k not in ("reply", "transcript")}
                                    | {"id": sid, "label": label, "attempt": attempt}) + "\n")
            if r["status"] != "ok":
                ok = False
                failures.append({"attempt": attempt, "turn": n, "status": r["status"], "rc": r["rc"]})
                break
            r["kind"] = kind(r["reply"], os.path.join(sessions, "tmp"))
            # The script's own answer to an intake round goes next unchanged. The recommended answers
            # go only once the script has none left before its playback answer, and never past the
            # script's end in a scenario that expects no board.
            if r["kind"] == "INTAKE" and scripted_answer(queue, sk):
                pass
            elif r["kind"] == "INTAKE" and intake < MAX_INTAKE and (queue or expects_board):
                intake += 1
                queue.insert(0, (INTAKE_ANSWER, "adaptive", None))
            elif (expects_board and not queue and not any(t.get("composed") for t in turns)
                  and r["kind"] != "DELIVERY" and follow < MAX_FOLLOW):
                follow += 1
                queue.append((INTAKE_ANSWER if r["kind"] == "INTAKE" else dv.FOLLOW_UP, "supplementary", None))
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
    # The model is done, so the scenario's read-only shell steps run in its sandbox for the grader
    steps = scenario_commands.run(system_dir, sk["file"], scratch, os.path.join(sessions, "tmp"),
                                  os.path.join(dest, "commands.json"))
    meta = {"id": sid, "label": label, "model": model, "permission": dv.PERMISSION, "runtime": f"{spec[0]}-adaptive" if spec else "devin-adaptive",
            "scenario_file": sk["file"], "file_pin": pin, "driver": how["driver"], "expects_board": expects_board, "no_figma": no_figma, "scripted_turns": sk["turns"],
            "commands_run": sum(s["status"] != "skipped" for s in steps),
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

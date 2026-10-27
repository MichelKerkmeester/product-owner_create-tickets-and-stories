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
meta.json, and a small classifier's label for each reply's stop is kept as `kind`. A reply with
a counted `Read-back:` line, or a turn whose `use_figma` call returned a board, is a DELIVERY without asking the classifier.
The run log is tracked, so with `RUN_REDACT_FILE` or `RUN_FILE_KEY` set each row is redacted the way
`redact_run.py` redacts a file before it is written.

A scenario's `driver:` frontmatter key changes how it runs. `operator-only` is skipped with
its reason, because it needs a setup step the driver does not run. `new-file` drops the pin
to the test file and names the plan the new file goes in, which `NEW_FILE_PLAN` sets at launch. `OPERATOR_PAUSE_BEFORE`, a scripted
turn index or `part` for a chained scenario's own first turn, holds the run before that turn
until the operator marks their own step done, and `FILE_START_SECTIONS` records how many
sections the file held before turn 1. `OPERATOR_DONE` set to a scenario id runs that operator-only
scenario once the operator has done the setup the driver cannot, and a prompt that names its
prepared board by a `<fileKey ...>` placeholder gets the file key in its place and no pin. After the run the scenario's
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
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import devin_playbook_runner as dv  # noqa: E402
import redact_run  # noqa: E402
import runtimes  # noqa: E402
import scenario_commands  # noqa: E402

INTAKE_ANSWER = "Use your recommended answers."
# The scripted answer to the playback. A scripted turn before it answers an intake round.
READING_YES = "yes, that reading is right"
# Why an operator-only scenario is skipped when its frontmatter gives no reason of its own
OPERATOR_ONLY = "the playbook marks this scenario operator-only, because it needs a setup step the driver does not run"
MAX_INTAKE = 2
MAX_FOLLOW = 3
# The scripted answer to the write gate, and the phrase a scenario uses for a runtime with no Figma server
WRITE_YES = "yes, go ahead"
NO_FIGMA = "no hosted Figma MCP"
# A prompt that names a fictional plan tells a pinned run the test file is in it and a run that makes a file
# which real plan that is. A pin naming a second plan made runs ask the plan question. The real plan's name
# comes from NEW_FILE_PLAN at launch, so this public file names none.
IN_PLAN = "That file is in the plan named above."
NAMES_PLAN = re.compile(r"\bplan\b", re.I)
# Where a paused run waits for the operator's own step, such as a sticky added by hand
PAUSE_DIR = ".pause"
CLAUDE_BIN = os.path.expanduser("~/.local/bin/claude")
# An empty folder, so the classifier loads no project instructions
CLASSIFY_DIR = os.path.join(os.environ.get("TMPDIR", "/tmp"), "claude-reply-classifier")
PREPARED = re.compile(r"<fileKey[^>]*>")
# The line a delivery reply carries, whether or not the model bolds or bullets it. It counts what the board
# holds, so a read-back line that says nothing was written is no delivery.
READ_BACK = re.compile(r"^[\s>*_-]*Read-back:[\s*_]*\d+ of \d+", re.I | re.M)
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


def classify(r, tmp):
    """The stop one turn ends on.

    A delivery restates the brief, so the small model can read it as a playback. A counted read-back line or
    a `use_figma` call that returned a board settles it first, since a call that failed may end on a retry
    question. Devin reports the call in `inner_calls`, and Codex and Claude Code
    report it in `tools_used` under their own prefixes."""
    wrote = r.get("boards") and any(str(t).endswith("use_figma") for t in r["tools_used"] + r["inner_calls"])
    if READ_BACK.search(r["reply"]) or wrote:
        return "DELIVERY"
    return kind(r["reply"], tmp)


def log_line(r, sid, label, attempt):
    """One turn's run-log row, redacted when the run names a key or a plan name to hide."""
    hide = bool(os.environ.get("RUN_REDACT_FILE") or os.environ.get("RUN_FILE_KEY"))
    # Unescaped when redacting, so a name with accented letters still matches
    line = json.dumps({k: v for k, v in r.items() if k not in ("reply", "transcript")}
                      | {"id": sid, "label": label, "attempt": attempt}, ensure_ascii=not hide)
    return (redact_run.redact_text(line, redact_run.settings()) if hide else line) + "\n"


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
    answer and is not the request that opens a chained scenario's own part. A script with no playback
    answer, such as a conflict that never reaches a board, answers each round with its own next turn."""
    if not queue or queue[0][1] != "scripted":
        return False
    i = queue[0][2]
    said = [t.strip().lower() for t in sk["turns"]]
    playback = [t.startswith(READING_YES) for t in said]
    return (i != sk.get("setup_turns") and not said[i].startswith((READING_YES, WRITE_YES))
            and (any(playback[i + 1:]) or not any(playback)))


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
    operator_done = os.environ.get("OPERATOR_DONE") == sid
    if how["driver"] == "operator-only" and not operator_done:
        print(json.dumps({"id": sid, "label": label, "status": "skipped", "reason": how["reason"]}))
        return 0
    if how["driver"] == "operator-only":
        # The operator has done the setup the driver cannot, so the scenario's own turns run as usual
        how["driver"] = "model"
    if how["driver"] not in ("model", "new-file"):
        print(json.dumps({"id": sid, "label": label, "status": "bad-driver",
                          "reason": f"unknown driver value {how['driver']}"}))
        return 2
    # A new-file scenario tests making a file, so it is told only which plan the new file goes in
    names_plan = bool(NAMES_PLAN.search(sk["turns"][0]))
    new_plan = os.environ.get("NEW_FILE_PLAN", "").strip()
    if how["driver"] == "new-file":
        pin = (f"The plan named above is the {new_plan} plan on this account." if names_plan
               else f"Use the {new_plan} plan on this account.") + " Create the new file there, in drafts, with no project."
    else:
        pin = dv.FILE_PIN.format(key=key) + (f" {IN_PLAN}" if names_plan else "")
    # A prompt that names its prepared board by placeholder gets the file key there, so it needs no pin on top
    if how["driver"] == "model" and PREPARED.search(sk["turns"][0]):
        pin = None
    pause_env = os.environ.get("OPERATOR_PAUSE_BEFORE", "")
    pause_at = sk.get("setup_turns") if pause_env == "part" else int(pause_env) if pause_env.isdigit() else None
    start_sections = os.environ.get("FILE_START_SECTIONS", "")
    # A bad value would only show once every turn had run, so it stops the run before the first
    bad = []
    if how["driver"] == "new-file" and not new_plan:
        bad.append("NEW_FILE_PLAN names no plan for a new-file scenario")
    if pause_env and not (pause_at is not None and 0 < pause_at < len(sk["turns"])):
        bad.append(f"OPERATOR_PAUSE_BEFORE={pause_env} names no scripted turn of {sid}")
    if start_sections and not start_sections.isdigit():
        bad.append(f"FILE_START_SECTIONS={start_sections} is not a count")
    if bad:
        print(json.dumps({"id": sid, "label": label, "status": "bad-env", "reason": " and ".join(bad)}))
        return 2
    hold = os.path.join(harness_root, PAUSE_DIR, sid)
    # A scenario written for a runtime with no hosted Figma server runs only where one can be left out.
    no_figma, expects_board = how["no_figma"], how["expects_board"]
    if no_figma and not (spec and spec[0] == "claude"):
        print(json.dumps({"id": sid, "label": label, "status": "skipped",
                          "reason": "the scenario needs a runtime without the hosted Figma server"}))
        return 0
    failures, paused = [], None
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
        queue[0] = (f"{queue[0][0]}\n\n{pin}" if pin else PREPARED.sub(key, queue[0][0]), "scripted", 0)
        turns, intake, follow, n, ok, session_id = [], 0, 0, 0, True, None
        # A retry does not ask again, so the operator's own step lands in the file once
        pause = pause_at if attempt == 1 else None
        before0 = before = dv.snapshot(scratch)
        while queue:
            if pause is not None and queue[0][1] == "scripted" and queue[0][2] == pause:
                # The operator's own step runs here, and the run waits until they mark it done
                pause, paused = None, attempt
                shutil.rmtree(hold, ignore_errors=True)
                os.makedirs(hold)
                open(os.path.join(hold, "paused"), "w", encoding="utf-8").write(f"{sid} waits before scripted turn {pause_at}\n")
                print(json.dumps({"id": sid, "label": label, "status": "paused",
                                  "resume": os.path.join(hold, "resume")}), flush=True)
                while not os.path.exists(os.path.join(hold, "resume")):
                    time.sleep(5)
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
                fh.write(log_line(r, sid, label, attempt))
            if r["status"] != "ok":
                ok = False
                failures.append({"attempt": attempt, "turn": n, "status": r["status"], "rc": r["rc"]})
                break
            r["kind"] = classify(r, os.path.join(sessions, "tmp"))
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
            "scenario_file": sk["file"], "file_pin": pin, "operator_setup_done": operator_done, "operator_pause_before": pause_at, "operator_paused": paused is not None,
            "file_start_sections": int(start_sections) if start_sections else None, "driver": how["driver"], "expects_board": expects_board, "no_figma": no_figma, "scripted_turns": sk["turns"],
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

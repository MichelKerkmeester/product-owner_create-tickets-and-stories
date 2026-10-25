#!/usr/bin/env python3
"""Run one scenario on Claude Code the way the playbook's operator does, answering intake rounds.

The scenario files tell the operator that when the run opens an intake round first, they
answer it with the recommended answers and confirm the playback follows. The fixed turn
list cannot do that, so a run that opens with intake reaches each later yes one stop early.
This driver sends the scripted turns in order, and after any reply that is an intake round
it first sends the recommended-answers turn, at most twice per scenario.

Usage: adaptive_scenario.py <system dir> <run folder> <scenario id> <file key>
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import claude_playbook_runner as c  # noqa: E402

base = c.base
INTAKE_ANSWER = "Use your recommended answers."
MAX_INTAKE = 2
# An empty folder, so the classifier loads no project instructions
CLASSIFY_DIR = os.path.join(os.environ.get("TMPDIR", "/tmp"), "claude-reply-classifier")


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
    p = subprocess.run([c.CLAUDE_BIN, "-p", CLASSIFY + reply[:6000], "--model", "claude-haiku-5-5",
                        "--output-format", "json", "--setting-sources", "project", "--tools", "",
                        "--strict-mcp-config", "--no-session-persistence"],
                       cwd=CLASSIFY_DIR, stdin=subprocess.DEVNULL, capture_output=True, text=True)
    try:
        word = json.loads(p.stdout).get("result", "").strip().upper()
    except ValueError:
        return "OTHER"
    return next((k for k in ("INTAKE", "PLAYBACK", "GATE", "DELIVERY") if k in word), "OTHER")


def main():
    system_dir, out, sid, key = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
    sk = next(r for r in base.load_playbook(system_dir, "product-owner") if r["id"] == sid and r["side"] == "skill")
    harness_root = os.path.join(os.environ.get("TMPDIR", "/tmp"), "claude-sonnet-playbook-adaptive")
    scratch = os.path.join(harness_root, sid)
    sessions = os.path.join(harness_root, ".sessions", sid)
    dest = os.path.join(out, "skill", f"{sid} - {sk['slug']}")
    base.build(system_dir, "skill", scratch, sk["seed_export"])
    problems = base.prove_isolation("skill", scratch)
    if problems:
        print(json.dumps({"id": sid, "status": "isolation-failed", "problems": problems}))
        return 2
    for d in (sessions, dest):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
    os.makedirs(os.path.join(out, "replies"), exist_ok=True)
    session_id, turns, intake_sent, n = None, [], 0, 0
    sk = dict(sk, turns=list(sk["turns"]))
    pin = base.pin_for(sk, argparse.Namespace(file_key=key, new_file_ids=""))
    queue = list(sk["turns"])
    if pin:
        queue[0] = f"{queue[0]}\n\n{pin}"
    while queue:
        prompt = queue.pop(0)
        n += 1
        ev = os.path.join(dest, f"events-turn-{n}.jsonl")
        r = c.run_turn(scratch, sessions, session_id, c.SKILL_TOOLS, prompt, ev, c.deny_roots(system_dir, harness_root))
        session_id = session_id or r["session_id"]
        r["turn"], r["input"], r["adaptive"] = n, prompt, prompt == INTAKE_ANSWER
        turns.append(r)
        open(os.path.join(dest, f"turn-{n}.md"), "w", encoding="utf-8").write(base.redact(r["reply"]))
        open(os.path.join(out, "replies", f"{sid}-turn{n}.txt"), "w", encoding="utf-8").write(base.redact(r["reply"]))
        base.write_transcript(os.path.join(dest, f"transcript-turn-{n}.md"), sk, n, prompt, r)
        if r["status"] != "ok":
            print(json.dumps({"id": sid, "turn": n, "status": r["status"]}), flush=True)
            break
        r["kind"] = kind(r["reply"])
        if r["kind"] == "INTAKE" and intake_sent < MAX_INTAKE:
            intake_sent += 1
            queue.insert(0, INTAKE_ANSWER)
        print(json.dumps({"id": sid, "turn": n, "input": prompt[:60], "kind": r["kind"],
                          "figma": r["inner_calls"]}), flush=True)
    meta = {"id": sid, "model": c.MODEL, "thinking": c.THINKING, "runtime": "claude-code-adaptive",
            "scenario_file": sk["file"], "scripted_turns": sk["turns"], "intake_answers_sent": intake_sent,
            "session_id": session_id,
            "turns": [{k: v for k, v in r.items() if k not in ("reply", "transcript")} for r in turns]}
    json.dump(meta, open(os.path.join(dest, "meta.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return 0 if all(r["status"] == "ok" for r in turns) else 1


if __name__ == "__main__":
    sys.exit(main())

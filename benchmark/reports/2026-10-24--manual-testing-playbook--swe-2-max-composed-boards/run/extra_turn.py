#!/usr/bin/env python3
"""Run one supplementary turn on a finished Claude Code scenario's own session and sandbox.

A scenario whose declared turns end at the write gate leaves no board to grade. The
extra turn answers the gate, and its files are named supplementary so a grader keeps
the declared turns and this one apart.

Usage: extra_turn.py <system dir> <run folder> <scenario id> <prompt> [label]
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import claude_playbook_runner as c  # noqa: E402

system_dir, out, sid, prompt = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
label = sys.argv[5] if len(sys.argv) > 5 else "supplementary"
dest = glob.glob(os.path.join(out, "skill", f"{sid} - *"))[0]
meta = json.load(open(os.path.join(dest, "meta.json")))
harness_root = os.path.join(os.environ.get("TMPDIR", "/tmp"), "claude-sonnet-playbook-bench")
scratch = os.path.join(harness_root, "product-owner", "skill", sid)
sessions = os.path.join(harness_root, "product-owner", "skill", ".sessions", sid)
ev = os.path.join(dest, f"events-turn-{label}.jsonl")
r = c.run_turn(scratch, sessions, meta["session_id"], c.SKILL_TOOLS, prompt, ev,
               c.deny_roots(system_dir, harness_root))
open(os.path.join(dest, f"turn-{label}.md"), "w", encoding="utf-8").write(c.base.redact(r["reply"]))
open(os.path.join(out, "replies", f"{sid}-turn-{label}.txt"), "w", encoding="utf-8").write(c.base.redact(r["reply"]))
meta.setdefault("supplementary_turns", {})[label] = {"input": prompt, **{k: v for k, v in r.items() if k not in ("reply", "transcript")}}
json.dump(meta, open(os.path.join(dest, "meta.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps({"id": sid, "status": r["status"], "figma_calls": r["inner_calls"]}))

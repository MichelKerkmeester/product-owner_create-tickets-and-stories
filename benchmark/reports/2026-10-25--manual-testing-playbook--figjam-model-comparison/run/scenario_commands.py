#!/usr/bin/env python3
"""The read-only shell steps of one scenario's Commands block, run after the model's last turn.

A grader marks a signal harness when the operator step behind it never ran. Many of those steps
only read the packet, such as the hub check, a grep of SKILL.md or flow_check.py on a shipped
example, so the driver runs them itself and keeps each command, its output and its exit status
beside the run in commands.json. A step runs only when it is one plain `bash:` command that calls
no Figma tool, names no path the operator fills in and writes no file. Every other step is listed
as skipped with its reason.

The sandbox leaves out benchmark/ and every playbook folder, so the model cannot read its own
grading. The model is done when these steps run, so those read-only inputs are copied back first.

Usage: scenario_commands.py <system dir> [ID ...] prints each FigJam scenario's plan and runs nothing.
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

STEP = re.compile(r"^\d+\.\s+`(.*)`\s*$")
TIMEOUT_S = 300
MAX_OUTPUT = 20000
# The commands a read-only step may start with. A step that starts with any other word is an
# instruction to the operator, such as "write a flowchart to <scratch>/rank.md".
HEADS = {"python3", "python", "node", "grep", "rg", "for", "test", "cat", "head", "tail", "ls", "wc",
         "git", "diff", "jq", "find", "echo"}
FIGMA = re.compile(r"use_figma|get_figjam|get_screenshot|get_metadata|generate_diagram|create_new_file"
                   r"|figma-ds-cli|\bfj\s|figma\.com", re.I)
# Read once quoted text is taken out, so a grep pattern such as "-> er" is not a redirect
WRITE = re.compile(r"(?<![-=])>(?!&)|\btee\b|\bcp\b|\bmv\b|\brm\b|\btouch\b|\bmkdir\b|\bsed\s+-i"
                   r"|--write\b|--out\b|-delete\b|-exec\b|\bgit\s+(?:add|commit|checkout|reset|apply|stash|push)\b")
QUOTED = re.compile(r"\"(?:\\.|[^\"\\])*\"|'[^']*'")
PLACEHOLDER = re.compile(r"<[a-z][^>]*>")


def steps(scenario_file):
    """Each numbered step of the scenario's Commands block, in order."""
    text = open(scenario_file, encoding="utf-8").read()
    m = re.search(r"^### Commands\s*\n(.*?)(?=^#{2,3} |\Z)", text, re.M | re.S)
    if not m:
        return []
    return [s.group(1) for s in map(STEP.match, m.group(1).splitlines()) if s]


def classify(step):
    """The command one step runs, or None and the reason the driver leaves it to the operator."""
    kind, _, body = step.partition(":")
    if kind.strip() != "bash":
        return None, f"{kind.strip()} step, not a shell command"
    cmd = body.strip()
    bare = QUOTED.sub('""', cmd)
    if " -> " in bare:
        return None, "chains more than one action"
    if PLACEHOLDER.search(bare):
        return None, "names a path the operator fills in"
    if FIGMA.search(cmd):
        return None, "calls Figma"
    if WRITE.search(bare):
        return None, "writes a file"
    if cmd.split()[0] not in HEADS:
        return None, "an instruction to the operator, not a command"
    return cmd, None


def stage_inputs(system_dir, scratch):
    """Copy back the read-only inputs the sandbox leaves out: benchmark/ without its reports, and
    every playbook folder."""
    src = os.path.join(system_dir, "benchmark")
    shutil.copytree(src, os.path.join(scratch, "benchmark"), dirs_exist_ok=True,
                    ignore=lambda d, names: [n for n in names if n == "__pycache__" or (d == src and n == "reports")])
    for top in [""] + sorted(os.listdir(system_dir)):
        play = os.path.join(system_dir, top, dv.TEST_DIR_EXACT)
        if os.path.isdir(play):
            shutil.copytree(play, os.path.join(scratch, top, dv.TEST_DIR_EXACT), dirs_exist_ok=True)


def run(system_dir, scenario_file, scratch, tmp, out_path):
    """Run the scenario's read-only steps inside its sandbox and write commands.json."""
    planned = [(n, s, *classify(s)) for n, s in enumerate(steps(scenario_file), 1)]
    if any(cmd for _, _, cmd, _ in planned):
        stage_inputs(system_dir, scratch)
    os.makedirs(tmp, exist_ok=True)
    env = dict(os.environ, TMPDIR=tmp, PWD=scratch)
    skilled = os.path.join(system_dir, ".skilled")
    if os.path.isdir(skilled):
        env.setdefault("SKILLED", os.path.realpath(skilled))
    records = []
    for n, step, cmd, reason in planned:
        if cmd is None:
            records.append({"step": n, "text": step, "status": "skipped", "reason": reason})
            continue
        t0 = time.time()
        try:
            p = subprocess.run(["bash", "-c", cmd], cwd=scratch, env=env, stdin=subprocess.DEVNULL,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=TIMEOUT_S)
            status, rc, output = "ran", p.returncode, p.stdout
        except subprocess.TimeoutExpired as e:
            out = e.output or ""
            status, rc, output = "timeout", None, out.decode(errors="ignore") if isinstance(out, bytes) else out
        records.append({"step": n, "command": cmd, "status": status, "exit": rc,
                        "wall_s": round(time.time() - t0, 2), "output": dv.redact(output)[:MAX_OUTPUT]})
    json.dump(records, open(out_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return records


def main():
    system_dir, ids = os.path.abspath(sys.argv[1]), set(sys.argv[2:])
    for sk in dv.load_playbook(system_dir, "product-owner"):
        if sk["side"] != "skill" or "sk-create-figjam" not in sk["file"] or (ids and sk["id"] not in ids):
            continue
        for n, step in enumerate(steps(sk["file"]), 1):
            cmd, reason = classify(step)
            print(json.dumps({"id": sk["id"], "step": n, "run": cmd is not None, "why": reason or cmd}))
    return 0


if __name__ == "__main__":
    sys.exit(main())

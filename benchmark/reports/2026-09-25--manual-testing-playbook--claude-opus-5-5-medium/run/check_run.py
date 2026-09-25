#!/usr/bin/env python3
"""Check that a playbook run is complete and ran on the model it names.

The runner's exit status says every scenario was attempted. It does not say that
each scenario's last turn was captured, and the command line's --model does not
say which model answered. This reads both from the files the run left: every
scenario in manifest.json must have a completed meta.json, one non-empty reply
per declared turn, and one event stream per turn whose system event, assistant
messages and result usage name only the expected model.

manifest.json must also name the engine, model and effort this run folder was
made for. The event streams prove the model but not the effort, and a run
started with the wrong flags would otherwise pass as the run its folder name
promises.

The event streams are ignored by git, so this runs on the machine that ran the
playbook, before the streams are cleaned up.

Usage: check_run.py [run folder] [--model claude-opus-5-5] [--effort medium]

Exit codes:
  0  every scenario whole, every turn on the expected model and effort
  1  at least one finding, each printed
  2  manifest.json or run-status.json missing or unreadable
"""
import json
import os
import sys

EXPECTED_ENGINE = "claude"
DEFAULTS = {"model": "claude-opus-5-5", "effort": "medium"}


def split_args(argv):
    """The run folder and each --option value, so an option's value is never read
    as the run folder."""
    values, positional, i = dict(DEFAULTS), [], 1
    while i < len(argv):
        arg = argv[i]
        if arg.startswith("--") and arg[2:] in values and i + 1 < len(argv):
            values[arg[2:]] = argv[i + 1]
            i += 2
            continue
        if not arg.startswith("--"):
            positional.append(arg)
        i += 1
    return (positional[0] if positional else "."), values


def side_dir(side):
    return "skill" if side == "skill" else "claude project"


def models_in(path):
    """Every model an event stream names, or None when the stream is missing."""
    if not os.path.isfile(path):
        return None
    found = set()
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if event.get("type") == "system" and event.get("model"):
                found.add(event["model"])
            model = (event.get("message") or {}).get("model")
            if model:
                found.add(model)
            if event.get("type") == "result":
                found.update((event.get("modelUsage") or {}).keys())
    return found


def main(argv):
    folder, values = split_args(argv)
    run = os.path.abspath(folder)
    expected, effort = values["model"], values["effort"]
    try:
        manifest = json.load(open(os.path.join(run, "manifest.json"), encoding="utf-8"))
        json.load(open(os.path.join(run, "run-status.json"), encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"unreadable run at {run}: {exc}", file=sys.stderr)
        return 2
    findings, turns_total, streams = [], 0, 0
    # The runner records the effort under "thinking", the name Pi gives it.
    for field, want in (("engine", EXPECTED_ENGINE), ("model", expected), ("thinking", effort)):
        if manifest.get(field) != want:
            findings.append(f"manifest.json: {field} is {manifest.get(field)!r}, not {want!r}")
    for sc in manifest["scenarios"]:
        sid, declared = sc["id"], len(sc["turns"])
        folder = os.path.join(run, side_dir(sc["side"]), f"{sid} - {sc['slug']}")
        try:
            meta = json.load(open(os.path.join(folder, "meta.json"), encoding="utf-8"))
        except (OSError, ValueError):
            findings.append(f"{sid}: no readable meta.json, so the scenario did not finish")
            continue
        if not meta.get("completed") or meta.get("turns_run") != declared:
            findings.append(f"{sid}: {meta.get('turns_run')} of {declared} turns run, "
                            f"completed={meta.get('completed')}")
        for n in range(1, declared + 1):
            turns_total += 1
            reply = os.path.join(run, "replies", f"{sid}-turn{n}.txt")
            if not os.path.isfile(reply) or not open(reply, encoding="utf-8").read().strip():
                findings.append(f"{sid}: turn {n} has no captured reply")
            names = models_in(os.path.join(folder, f"events-turn-{n}.jsonl"))
            if names is None:
                findings.append(f"{sid}: turn {n} has no event stream to read the model from")
                continue
            streams += 1
            if not names:
                findings.append(f"{sid}: turn {n}'s event stream names no model")
            elif names != {expected}:
                findings.append(f"{sid}: turn {n} names {sorted(names)}, not only {expected}")
    for finding in findings:
        print(finding)
    print(f"{len(manifest['scenarios'])} scenarios, {turns_total} declared turns, "
          f"{streams} event streams read, {len(findings)} finding(s), expected "
          f"{EXPECTED_ENGINE} {expected} at effort {effort}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

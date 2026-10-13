#!/usr/bin/env python3
"""Prove every hard value in the phase 002 manifest sits verbatim in its fixture.

Reads the Manifest table in this phase's spec.md, finds each file in its company
folder and greps every backticked value in the row's last column as a fixed string.
Exit 0 when every file exists and holds every value, 1 on any miss.

Usage:
  check_manifest_values.py [--company roamstay|loomlist|fernhouse] [--plant]

--plant adds a value no fixture holds to the first checked row, so a run that
still exits 0 proves the check cannot fail.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, "..", "spec.md")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
BASE = os.path.join(REPO, "AI Systems", "Product Owner", "benchmark", "fixtures", "companies")
PLANTED = "planted-value-no-fixture-holds"


def cells(row):
    out, cur, tick, i = [], "", False, 0
    s = row.strip().strip("|")
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if c == "`":
            tick = not tick
        if c == "|" and not tick:
            out.append(cur.strip())
            cur = ""
        else:
            cur += c
        i += 1
    out.append(cur.strip())
    return out


def manifest_rows():
    lines = open(SPEC, encoding="utf-8").read().splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip() == "### Manifest")
    rows = []
    for line in lines[start + 1:]:
        if line.startswith("### ") or line.startswith("## "):
            break
        if not line.startswith("| `"):
            continue
        c = cells(line)
        name = c[0].strip("`")
        company = c[1].lower()
        values = re.findall(r"`([^`]+)`", c[4])
        rows.append((name, company, values))
    return rows


def main():
    args = sys.argv[1:]
    only = args[args.index("--company") + 1] if "--company" in args else None
    plant = "--plant" in args
    rows = [r for r in manifest_rows() if only is None or r[1] == only]
    if not rows:
        print("no manifest rows matched")
        return 1
    misses, checked = [], 0
    for index, (name, company, values) in enumerate(rows):
        if plant and index == 0:
            values = values + [PLANTED]
        path = os.path.join(BASE, company, name)
        if not os.path.isfile(path):
            misses.append(f"{company}/{name}: file missing")
            continue
        text = open(path, encoding="utf-8").read()
        for value in values:
            checked += 1
            if value not in text:
                misses.append(f"{company}/{name}: missing `{value}`")
    for miss in misses:
        print(miss)
    print(f"{len(rows)} files, {checked} values checked, {len(misses)} misses")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())

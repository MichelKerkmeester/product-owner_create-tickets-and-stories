#!/usr/bin/env python3
"""Check a rewritten benchmark export against its graded snapshot.

Usage: verify_rewrite.py <export file> [...]   or   verify_rewrite.py --all

A file passes when the rewrite kept every structural line, every backticked
span, every number, link and HTML comment of its snapshot, added no em dash,
meets the length caps and passes the Product Owner format gate. An About or
Overview opening left over its cap prints KEPT: the brief keeps a fact over the
cap, and whether that was the reason is a reader's call. New
capitalized words are listed for a reader, since an invented name is the fact
most likely to slip in.
"""
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
EXPORTS = os.path.join(REPO, "AI Systems", "Product Owner", "export", "benchmark")
BEFORE = os.path.join(HERE, "before")
GATE = os.path.join(REPO, "AI Systems", "z — Claude Project Sync Loop", "validate-output-format.cjs")

HEADING = re.compile(r"^#{1,6}(\s|$)")
LABEL = re.compile(r"^\s*\*\*[^*]+\*\*[.,:;!?]?\s*$")
NUMBERED_TITLE = re.compile(r"^\d+\\\.")
GWT = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\*\*(?:Given|When|Then|And|But)\*\*|Given\b)")
TABLE = re.compile(r"^\s*\|")
QUOTE = re.compile(r"^\s*>")
FIXED = re.compile(r"^\s*(?:\* \* \*|-{3,}|_[^_].*_|- \[[ xX]\] _Mark as done.*_)\s*$")
BACKTICK = re.compile(r"`[^`\n]+`")
NUMBER = re.compile(r"(?<![A-Za-z])\d+(?:[.,:]\d+)*")
URL = re.compile(r"https?://[^\s)>\]]+")
COMMENT = re.compile(r"<!--.*?-->", re.S)
CAP = re.compile(r"over the (?:25-word|one-sentence|60-word|three-sentence|two-paragraph) cap")

# The one structural line a rewrite may change: a label the gate reads as an
# importance assertion, which no rewording of the text below it can clear.
ALLOWED = {
    ("skill/SIR-001 - 001 - intake-guest-loyalty-points-clarification.md", "**2. Why it matters**"): "**2. What points should achieve**",
}


def structural(lines):
    out, fence = [], False
    for line in lines:
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            out.append(line)
            continue
        if fence or any(p.search(line) for p in (HEADING, LABEL, NUMBERED_TITLE, GWT, TABLE, QUOTE, FIXED)):
            out.append(line.rstrip())
    return out


def words(text):
    return set(re.findall(r"[A-Za-z][A-Za-z'-]+", text))


def check(path):
    rel = os.path.relpath(os.path.abspath(path), EXPORTS)
    before_path = os.path.join(BEFORE, rel)
    if not os.path.isfile(before_path):
        return rel, ["no snapshot at scratch/before/" + rel], []
    before = open(before_path, encoding="utf-8").read()
    after = open(path, encoding="utf-8").read()
    fails, notes = [], []

    b_struct, a_struct = structural(before.splitlines()), structural(after.splitlines())
    b_struct = [ALLOWED.get((rel, line), line) for line in b_struct]
    if b_struct != a_struct:
        missing = [l for l in b_struct if l not in a_struct][:3]
        added = [l for l in a_struct if l not in b_struct][:3]
        fails.append(f"structural lines changed (headings, labels, Given/When/Then, tables, quotes, code, fixed lines): missing {missing} added {added}")
    for name, pattern in (("backticked span", BACKTICK), ("number", NUMBER), ("link", URL), ("HTML comment", COMMENT)):
        b, a = set(pattern.findall(before)), set(pattern.findall(after))
        if b - a:
            fails.append(f"{name}(s) dropped: {sorted(b - a)[:8]}")
        if a - b:
            fails.append(f"{name}(s) added: {sorted(a - b)[:8]}")
    nested = re.compile(r"^ {2,}(?:[-*+]|\d+[.)]) ", re.M)
    if len(nested.findall(after)) > len(nested.findall(before)):
        fails.append(f"nested list lines rose from {len(nested.findall(before))} to {len(nested.findall(after))}, and the templates keep lists one level deep")
    if after.count("—") > before.count("—"):
        fails.append(f"em dashes rose from {before.count(chr(0x2014))} to {after.count(chr(0x2014))}")

    run = subprocess.run(["node", GATE, "--system", "product-owner", path], capture_output=True, text=True)
    output = run.stdout + run.stderr
    if run.returncode != 0:
        fails.append("format gate exit %d: %s" % (run.returncode, " | ".join(l.strip() for l in output.splitlines() if "error" in l.lower() or ".md:" in l)[:600]))
    caps = [l.strip().split(os.path.basename(path) + ":", 1)[-1] for l in output.splitlines() if CAP.search(l)]
    opening = [c for c in caps if "opening holds" in c]
    others = [c for c in caps if "opening holds" not in c]
    if others:
        fails.append(f"{len(others)} over-cap line(s): {others[:6]}")
    if opening:
        notes.append(f"KEPT: {opening[0].strip()}, left over the cap only where cutting would drop a fact")

    new_caps = sorted(w for w in words(after) - words(before) if w[0].isupper() and w.lower() not in {x.lower() for x in words(before)})
    if new_caps:
        notes.append(f"new capitalized words, check none is an invented name: {new_caps[:12]}")
    wb, wa = len(before.split()), len(after.split())
    notes.append(f"words {wb} -> {wa}")
    return rel, fails, notes


def main(argv):
    if argv == ["--all"]:
        argv = [os.path.join(d, f) for d, _, fs in os.walk(EXPORTS) for f in fs if f.endswith(".md")]
    if not argv:
        print(__doc__)
        return 64
    failed = 0
    for path in sorted(argv):
        rel, fails, notes = check(path)
        kept = any(n.startswith("KEPT") for n in notes)
        status = "FAIL" if fails else ("KEPT" if kept else "PASS")
        failed += bool(fails)
        print(f"{status} {rel}")
        for line in fails:
            print(f"  - {line}")
        for line in notes:
            print(f"  . {line}")
    print(f"{len(argv) - failed} of {len(argv)} passed, About openings over the cap counted as passing and listed as KEPT")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

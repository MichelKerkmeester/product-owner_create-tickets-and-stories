#!/usr/bin/env python3
"""Check a cut benchmark export against its snapshot from before the cut.

Usage: verify_cut.py <export file> [...]   or   verify_cut.py --all

A file passes when the cut kept every heading, bold label, numbered criterion
title, table header, code line and fixed template line, kept as many
Given/When/Then lines, table rows and blockquote blocks as before, kept every backticked
span, number, link and HTML comment, added no em dash or nested list, meets the
length caps and passes the Product Owner format gate. The word change is
reported against the snapshot, and a file cut by less than 20% prints LIGHT so
the writer says why. Proper names that no longer appear are listed for the fact
reviewers, since a dropped owner or team is the loss most likely to slip by.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
EXPORTS = os.path.join(REPO, "AI Systems", "Product Owner", "export", "benchmark")
BEFORE = os.path.join(HERE, "before-cut")
GATE = os.path.join(REPO, "AI Systems", "z — Claude Project Sync Loop", "validate-output-format.cjs")

HEADING = re.compile(r"^#{1,6}(\s|$)")
LABEL = re.compile(r"^\s*\*\*[^*]+\*\*[.,:;!?]?\s*$")
NUMBERED_TITLE = re.compile(r"^\s*\d+(?:\\\.|\.)\s+\*\*")
TABLE = re.compile(r"^\s*\|")
FIXED = re.compile(r"^\s*(?:\* \* \*|-{3,}|_[^_].*_|- \[[ xX]\] _Mark as done.*_|#+\s*)\s*$")
GWT = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\*\*(?:Given|When|Then|And|But)\*\*|Given\b)")
BACKTICK = re.compile(r"`[^`\n]+`")
NUMBER = re.compile(r"(?<![A-Za-z])\d+(?:[.,:]\d+)*")
URL = re.compile(r"https?://[^\s)>\]]+")
MDLINK = re.compile(r"\]\(([^)\s]+)\)")
COMMENT = re.compile(r"<!--.*?-->", re.S)
CAP = re.compile(r"over the (?:25-word|one-sentence|60-word|three-sentence|two-paragraph) cap")
LIGHT = 0.20


def fixed_lines(lines):
    """Lines a cut keeps byte for byte, including the header row of each table."""
    out, fence, prev = [], False, None
    for line in lines:
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            out.append(line.rstrip())
            continue
        if fence or any(p.search(line) for p in (HEADING, LABEL, NUMBERED_TITLE, FIXED)):
            out.append(line.rstrip())
        elif TABLE.search(line) and not (prev and TABLE.search(prev)):
            out.append(line.rstrip())
        prev = line
    return out


def quote_blocks(lines):
    blocks, inside = 0, False
    for line in lines:
        quoted = line.lstrip().startswith(">")
        blocks += quoted and not inside
        inside = quoted
    return blocks


def prose_words(text):
    """Words outside code fences, the measure the cut and the budget both use."""
    out, fence = [], False
    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            continue
        if not fence:
            out.append(line)
    return len("\n".join(out).split())


def names(text):
    """Capitalized words that do not open a sentence, a line or a list item."""
    found = set()
    for match in re.finditer(r"(?<=[a-z0-9,;)] )([A-Z][A-Za-z'-]+)", text):
        found.add(match.group(1))
    return found


def check(path):
    rel = os.path.relpath(os.path.abspath(path), EXPORTS)
    before_path = os.path.join(BEFORE, rel)
    if not os.path.isfile(before_path):
        return rel, ["no snapshot at scratch/before-cut/" + rel], [], 0, 0
    before = open(before_path, encoding="utf-8").read()
    after = open(path, encoding="utf-8").read()
    bl, al = before.splitlines(), after.splitlines()
    fails, notes = [], []

    if fixed_lines(bl) != fixed_lines(al):
        b, a = fixed_lines(bl), fixed_lines(al)
        fails.append(f"fixed lines changed (headings, labels, criterion titles, tables, code, template lines): "
                     f"missing {[l for l in b if l not in a][:3]} added {[l for l in a if l not in b][:3]}")
    gb, ga = sum(bool(GWT.search(l)) for l in bl), sum(bool(GWT.search(l)) for l in al)
    if gb != ga:
        fails.append(f"Given/When/Then lines went from {gb} to {ga}; tighten them, never drop or merge one")
    tb_, ta_ = sum(bool(TABLE.search(l)) for l in bl), sum(bool(TABLE.search(l)) for l in al)
    if tb_ != ta_:
        fails.append(f"table rows went from {tb_} to {ta_}; tighten a row, never drop or merge one")
    qb, qa = quote_blocks(bl), quote_blocks(al)
    if qa < qb:
        fails.append(f"blockquote blocks fell from {qb} to {qa}")
    for label, pattern in (("backticked span", BACKTICK), ("number", NUMBER), ("URL", URL),
                           ("link target", MDLINK), ("HTML comment", COMMENT)):
        b, a = set(pattern.findall(before)), set(pattern.findall(after))
        if b - a:
            fails.append(f"{label}(s) dropped: {sorted(b - a)[:8]}")
        if a - b:
            fails.append(f"{label}(s) added: {sorted(a - b)[:8]}")
    nested = re.compile(r"^ {2,}(?:[-*+]|\d+[.)]) ", re.M)
    if len(nested.findall(after)) > len(nested.findall(before)):
        fails.append("nested list lines rose, and the templates keep lists one level deep")
    if after.count("—") > before.count("—"):
        fails.append("em dashes rose")

    run = subprocess.run(["node", GATE, "--system", "product-owner", path], capture_output=True, text=True)
    output = run.stdout + run.stderr
    if run.returncode != 0:
        fails.append("format gate exit %d: %s" % (run.returncode, " | ".join(
            l.strip() for l in output.splitlines() if "error" in l.lower() or ".md:" in l)[:600]))
    caps = [l.strip().split(os.path.basename(path) + ":", 1)[-1] for l in output.splitlines() if CAP.search(l)]
    opening = [c for c in caps if "opening holds" in c]
    others = [c for c in caps if "opening holds" not in c]
    if others:
        fails.append(f"{len(others)} over-cap line(s): {others[:6]}")
    if opening:
        notes.append(f"KEPT: {opening[0].strip()}")

    lost = sorted(names(before) - set(re.findall(r"[A-Za-z][A-Za-z'-]+", after)))
    if lost:
        notes.append(f"names no longer present, confirm each was a restatement: {lost[:12]}")
    wb, wa = prose_words(before), prose_words(after)
    cut = (wb - wa) / wb if wb else 0
    notes.append(f"words {wb} -> {wa}, cut {cut:.0%}")
    if cut < LIGHT:
        notes.append("LIGHT: cut under 20%, say why in the report")
    return rel, fails, notes, wb, wa


def main(argv):
    if argv == ["--all"]:
        argv = [os.path.join(d, f) for d, _, fs in os.walk(EXPORTS) for f in fs if f.endswith(".md")]
    if not argv:
        print(__doc__)
        return 64
    failed = tb = ta = 0
    for path in sorted(argv):
        rel, fails, notes, wb, wa = check(path)
        tb, ta = tb + wb, ta + wa
        status = "FAIL" if fails else ("KEPT" if any(n.startswith("KEPT") for n in notes) else "PASS")
        failed += bool(fails)
        print(f"{status} {rel}")
        for line in fails:
            print(f"  - {line}")
        for line in notes:
            print(f"  . {line}")
    print(f"{len(argv) - failed} of {len(argv)} passed; words {tb} -> {ta}, cut {(tb - ta) / tb if tb else 0:.1%}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Move a Product Owner artifact to the new house forms, in place.

Story and Epic: Problem, Solution and Goal go to H4, the Expected outcomes and User Story
headings become bold labels, spacers inside About follow the H4 level, and every plain
bullet under `## Requirements` becomes a `- []` item. Task and Bug: `### About` becomes
`## About`. Everywhere: a `[ ]` checkbox becomes `[]`.

--check compares each file with its snapshot and fails any changed line that is not one
of those transforms, so a stray edit cannot hide inside the conversion.
"""
import os, re, sys

OPENING = re.compile(r"^### (Problem|Solution|Goal)$")
BOLD_HEAD = re.compile(r"^#### \*\*(Expected outcomes|User Story)\*\*$")
H3_SPACER = re.compile(r"^###\s+$")
BOX = re.compile(r"^(\s*)(- |\*   )\[ \] ")
PLAIN = re.compile(r"^\*   (?!\[)(.*)$")


def kind(lines):
    text = "\n".join(lines)
    if re.search(r"(?m)^### (Problem|Goal)$", text) or re.search(r"(?m)^#### (Problem|Goal)$", text):
        return "story"
    if re.search(r"(?m)^#{2,3} About$", text):
        return "task"
    return "doc"


def convert(lines):
    k = kind(lines)
    out, section = [], None
    for line in lines:
        if re.match(r"^## \S", line):
            section = line[3:].strip()
        new = BOX.sub(r"\1\2[] ", line)
        if k == "story":
            if OPENING.match(new):
                new = "#" + new
            elif BOLD_HEAD.match(new):
                new = new[5:]
            elif section == "About" and H3_SPACER.match(new):
                new = "####   "
            elif section == "Requirements":
                m = PLAIN.match(new)
                if m:
                    new = "- [] " + m.group(1)
        elif k == "task" and new == "### About":
            new = "## About"
        out.append(new)
    return k, out


def check(before, after):
    """Return the changed lines that no transform explains."""
    k, expect = convert(before)
    bad = []
    if len(before) != len(after):
        return k, [("line count", len(before), len(after))]
    for i, (e, a) in enumerate(zip(expect, after)):
        if e != a:
            bad.append((i + 1, e, a))
    return k, bad


def main():
    args = sys.argv[1:]
    if args and args[0] == "--check":
        snap_root, live_root = args[1], args[2]
        fails = 0
        counts = {}
        for dp, _, fs in os.walk(snap_root):
            for f in fs:
                if not f.endswith(".md"):
                    continue
                sp = os.path.join(dp, f)
                lp = os.path.join(live_root, os.path.relpath(sp, snap_root))
                before = open(sp, encoding="utf-8").read().split("\n")
                after = open(lp, encoding="utf-8").read().split("\n")
                k, bad = check(before, after)
                counts[k] = counts.get(k, 0) + 1
                if bad:
                    fails += 1
                    print("FAIL", lp)
                    for b in bad[:5]:
                        print("   ", b)
        print("checked", sum(counts.values()), counts, "fails", fails)
        return 1 if fails else 0
    for p in args:
        lines = open(p, encoding="utf-8").read().split("\n")
        k, out = convert(lines)
        if out != lines:
            open(p, "w", encoding="utf-8").write("\n".join(out))
        print(k, sum(1 for a, b in zip(lines, out) if a != b), p)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Run the HVR hard-blocker linter over every reply a playbook run captured.

The manual testing playbook (`sk-product-owner/manual-testing-playbook/`)
persists a run's `PASS`/`FAIL`/`SKIP` verdicts, but nothing in this system
previously read the captured reply text itself against the hard blockers its
own kernel states on every turn. A scenario can pass on behavior (the right
mode, the right artifact shape, the right delivery lines) while the prose
still carries an em dash or a hard-blocker word the self-scan line should
have caught and did not. `hvr_lint.py` reads one file, and this walks a run's
`replies/` directory, lints each through the same `lint()` that tool calls,
writes `hvr-lint.csv` beside it, and returns an exit code that means
something.

Zero only when everything is clean. Another system's benchmark tooling in
this same fleet shipped a linter that exited 0 whether a file was spotless or
carried four hard violations, and that zero was read once as a pass. This
does not repeat that shape.

A dirty reply is a finding about the runtime that produced it, a fact about
one playbook run, not a defect in this repository, so it belongs in a run
record rather than in a standing gate. It reports what a session wrote. It
never edits a reply.

Accepts a single file too, with `--brief` printing one line rather than a
table, so a per-scenario capture step can report what it just saved without
embedding a JSON reader in shell.

Usage:
  lint_replies.py <run report dir or replies dir>
  lint_replies.py <file> --brief
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hvr_lint import extract_deliverable, lint  # noqa: E402  path set above

TEXT_SUFFIXES = {".txt", ".md"}


def replies_dir(target: Path) -> Path:
    """The directory holding reply files, given either it or the run root."""
    if (target / "replies").is_dir():
        return target / "replies"
    return target


def lint_file(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text, confidence = extract_deliverable(raw)
    violations = lint(text, confidence)
    hard = [v for v in violations if v["severity"] == "hard"]
    return {
        "file": path.name,
        "clean": not hard,
        "hard_violations": len(hard),
        "violations": ", ".join(f"{v['type']}x{v['count']}" for v in violations) or "none",
        "extraction_confidence": confidence,
    }


def main(argv) -> int:
    if len(argv) < 2:
        print("usage: lint_replies.py <run report dir or replies dir>", file=sys.stderr)
        return 64
    brief = "--brief" in argv[1:]
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: lint_replies.py <run report dir or replies dir>", file=sys.stderr)
        return 64
    target = Path(args[0]).resolve()

    if target.is_file():
        row = lint_file(target)
        if brief:
            print("clean" if row["clean"] else f"HVR {row['violations']}")
        else:
            print(f"  {row['file']}  {'clean' if row['clean'] else 'DIRTY'}  {row['violations']}")
        return 0 if row["clean"] else 1

    if not target.is_dir():
        print(f"{target} is not a directory, so no reply was read", file=sys.stderr)
        return 2
    directory = replies_dir(target)
    rows = [lint_file(p) for p in sorted(directory.iterdir())
            if p.is_file() and p.suffix in TEXT_SUFFIXES]
    if not rows:
        print(f"no reply files under {directory}, so nothing was linted", file=sys.stderr)
        return 2

    out = directory.parent / "hvr-lint.csv"
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    width = max(len(r["file"]) for r in rows)
    for r in rows:
        print(f"  {r['file'].ljust(width)}  {'clean' if r['clean'] else 'DIRTY'}  {r['violations']}")
    dirty = [r for r in rows if not r["clean"]]
    print(f"  {len(rows) - len(dirty)} clean of {len(rows)}, written to {out.name}")
    if dirty:
        print(f"FAILED {len(dirty)} reply/replies carry an HVR hard blocker")
        return 1
    print("PASSED every reply clean of HVR hard blockers")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

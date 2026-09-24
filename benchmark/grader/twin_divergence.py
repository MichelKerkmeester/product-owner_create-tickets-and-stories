#!/usr/bin/env python3
"""Report scenario twins whose two runtimes disagreed in a playbook run.

`sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` runs
every scenario twice: once as the skill, `S`-prefixed, from `AGENTS.md` with
`sk-product-owner/` loaded, and once as the Project, `P`-prefixed, from
`claude project/Custom Instructions.md` with the knowledge set attached. Both
sides are declared as one contract over the same prompt (Section 4's "Prompt
synchronization gate" requires the two runtimes' Turn 1 text to match
character for character), and the playbook's own coverage map pairs seven
categories across the two runtimes: identity (`ID`), backlog task (`TK`),
backlog bug (`BG`), document (`DK`, twice), story (`ST`) and interactive
routing (`IR`). No script previously read a finished run's results across
that pairing, so a divergence between the two runtimes was only as visible as
whichever reader happened to compare two rows by hand.

Rule parity (`benchmark/gates/rule_parity.py`) can hold a rule's wording
identical on both sides of every declared pair and still miss this, because a
kernel that states a rule correctly and a skill file that states the same
rule correctly can still be *routed* or *applied* differently by the runtime
that reads them. Comparing the two packagings' actual verdicts, scenario by
scenario, is the only check aimed at that gap.

Twins are paired by id: an `S`-prefixed row and a `P`-prefixed row that share
the same category letters and number are one twin, read from a `results.csv`
this system's run records supply (`id,result` at minimum). A pair is the
unit: a scenario run on only one runtime is unpaired and named as such, never
counted as agreement, because a comparison that quietly drops half its input
proves nothing about the half it dropped.

Rows whose id carries a suffix after the number are excluded from pairing and
listed as variants, since a re-run or a diagnostic capture is a version of a
scenario rather than a runtime's answer to one.

`PARTIAL` is not a verdict and is never compared. Most scenarios in this
playbook are two-turn conversations (see, for example, `SID-001`'s Turn 1 and
Turn 2), and a captured run that only reached Turn 1 is evidence about Turn 1
alone. Two such partial runs matching would report agreement about an outcome
neither runtime actually reached, so a pair with a `PARTIAL` side is counted
and named apart from the pairs that agreed.

Exit codes:
  0  every paired twin agreed
  1  at least one pair disagreed
  2  no results file, or nothing in it that could be paired

Usage:
  twin_divergence.py <run report dir, or a results.csv>
"""
import csv
import re
import sys
from pathlib import Path

# S|P + two letters (ID, TK, BG, DK, ST, IR today) + "-" + digits, confirmed
# against this playbook's own coverage map rather than assumed from another
# system's scheme.
ID = re.compile(r"^([SP])([A-Z]{2})-(\d+)$")


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main(argv) -> int:
    if len(argv) < 2:
        print("usage: twin_divergence.py <run report dir, or a results.csv>", file=sys.stderr)
        return 64
    target = Path(argv[1]).resolve()
    results = target / "results.csv" if target.is_dir() else target
    if not results.is_file():
        print(f"no results file at {results}, so no twin was compared", file=sys.stderr)
        return 2

    paired, variants = {}, []
    for row in rows(results):
        match = ID.match((row.get("id") or "").strip())
        if not match:
            variants.append(row.get("id", "?"))
            continue
        side, group, number = match.groups()
        paired.setdefault(f"{group}-{number}", {})[side] = row

    if not paired:
        print(f"no rows in {results.name} carry a twin id, so nothing was compared", file=sys.stderr)
        return 2

    disagreed, agreed, unpaired, partial = [], [], [], []
    for key, sides in sorted(paired.items()):
        if len(sides) < 2:
            unpaired.append((key, next(iter(sides))))
            continue
        skill, project = sides["S"]["result"].strip(), sides["P"]["result"].strip()
        if "PARTIAL" in (skill, project):
            partial.append((key, skill, project))
            continue
        (agreed if skill == project else disagreed).append((key, skill, project))

    for key, skill, project in disagreed:
        print(f"  {key}: skill {skill}, Project {project}")
    print(f"  {len(agreed)} twin(s) agreed, {len(disagreed)} disagreed, "
          f"{len(partial)} not settled, {len(unpaired)} run on one runtime only")
    if partial:
        print("  not settled: " + ", ".join(f"{k} (skill {s}, Project {p})" for k, s, p in partial))
    if unpaired:
        print("  unpaired: " + ", ".join(f"{k} ({s})" for k, s in unpaired))
    if variants:
        print("  variants not paired: " + ", ".join(variants))

    if disagreed:
        print(f"FAILED {len(disagreed)} twin(s) disagreed across runtimes")
        return 1
    print("PASSED every paired twin agreed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

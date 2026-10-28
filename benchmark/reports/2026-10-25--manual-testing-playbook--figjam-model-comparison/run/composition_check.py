#!/usr/bin/env python3
"""Score a board's Composition from the plan's Glance line and the readers' orders, so no grader reads it by eye.

usage: composition_check.py --plan "Glance: A (accent) > B > C (goal)" reader-a.md reader-b.md
       composition_check.py --self-test

The plan is the `Glance:` line the check printed for the board the run wrote. The accent is the part it marks
`(accent)`. Each reader note ends on one `Order: A > B > C` line that names only the board's nodes, as the reader
brief asks, and that line is what this script reads. A note with no such line stops the run, naming the note, and
so does an Order line that leaves out a node the plan names, since a reworded label would otherwise read as a
part in place.

A part is out of place for one reader when it falls outside a longest common subsequence of the plan and that
reader's order, and a tie goes to the part read earlier than its planned place, as the playbook's Composition row
says. A part costs a point only when it is out of place for every reader. The level is 2 when no part costs,
1 when one does and 0 when two or more do or the accent is not first on every reader's list.

`--legacy-list` reads notes written before the Order line existed. It takes the numbered `## Reading order` list,
skips title and subtitle items and puts each item's node labels in the order they appear. It is the fragile
reading the Order line replaces, kept so the stored runs can still be rescored.
"""
from __future__ import annotations

import argparse
import re
import sys

ACCENT_MARK = re.compile(r"\s*\((?:accent|goal|accent, goal)\)\s*$")


def norm(text: str) -> str:
    """A label with curly quotes straightened, runs of space folded and the case dropped, for matching."""
    straight = text.replace("“", '"').replace("”", '"').replace("’", "'")
    return re.sub(r"\s+", " ", straight).strip().lower()


def plan_parts(line: str) -> tuple[list[str], str | None]:
    """The plan's labels in order and the one marked as the accent."""
    body = line.split(":", 1)[1]
    raw = [p.strip() for p in body.split(" > ")]
    accent = next((ACCENT_MARK.sub("", p) for p in raw if re.search(r"\((?:accent|accent, goal)\)\s*$", p)), None)
    return [ACCENT_MARK.sub("", p).strip() for p in raw], accent


def order_line(text: str) -> list[str] | None:
    """The labels on a note's Order line, or None when the note has none."""
    found = re.findall(r"^\W*Order:\**\s*(.+)$", text, re.M)
    return [p.strip() for p in found[-1].split(" > ")] if found else None


def listed_order(text: str, labels: list[str]) -> list[str]:
    """The labels of a pre-Order note, from its numbered reading order list."""
    block = re.search(r"^## Reading order[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    items = re.findall(r"^\s*\d+\.\s+(.*)$", block.group(1) if block else text, re.M)
    items = [i for i in items if not re.match(r"(the )?(title|subtitle)\b", i.strip(), re.I)]
    order: list[str] = []
    for item in items:
        t = norm(item)
        hits = sorted((t.find(norm(label)), label) for label in labels if norm(label) in t)
        # A label that sits inside a longer label of the same item names the longer node, not itself.
        hits = [h for h in hits if not any(h[1] != o[1] and norm(h[1]) in norm(o[1]) for o in hits)]
        order += [label for _, label in hits if label not in order]
    return order


def match(order: list[str], plan: list[str]) -> list[str]:
    """The reader's order in the plan's own spelling, dropping any item the plan does not name."""
    spelled = {norm(p): p for p in plan}
    return [spelled[norm(o)] for o in order if norm(o) in spelled]


def out_of_place(plan: list[str], seen: list[str]) -> set[str]:
    """The plan parts this order reads outside a longest common subsequence, ties to the part read early."""
    parts = [p for p in plan if p in seen]
    rank = {p: i for i, p in enumerate(parts)}
    seen = [p for p in seen if p in rank]
    pos = {p: i for i, p in enumerate(seen)}
    best = None
    for mask in range(1 << len(parts)):
        keep = [parts[i] for i in range(len(parts)) if mask >> i & 1]
        if [p for p in seen if p in keep] != keep:
            continue
        out = [p for p in parts if p not in keep]
        key = (len(keep), sum(rank[p] - pos[p] for p in out))
        if best is None or key > best[0]:
            best = (key, out)
    return set(best[1])


def score(plan: list[str], accent: str, orders: list[list[str]]) -> tuple[int, list[str], list[set[str]]]:
    """The level, the parts that cost it and each reader's out of place parts."""
    costs = [out_of_place(plan, o) | ({accent} if o and o[0] != accent else set()) for o in orders]
    shared = set.intersection(*costs)
    accent_late = all(o and o[0] != accent for o in orders)
    level = 0 if accent_late or len(shared) >= 2 else 1 if shared else 2
    return level, [p for p in plan if p in shared], costs


def read_note(path: str, plan: list[str], legacy: bool) -> list[str]:
    """One note's order in the plan's spelling, or a SystemExit that names the note and what it lacks."""
    text = open(path, encoding="utf-8").read()
    if legacy:
        return match(listed_order(text, plan), plan)
    given = order_line(text)
    if given is None:
        raise SystemExit(f"{path}: no Order line, so the note cannot be scored")
    order = match(given, plan)
    missing = [p for p in plan if p not in order]
    if missing:
        raise SystemExit(f"{path}: the Order line leaves out {', '.join(missing)}, so it cannot be scored")
    return order


def self_test() -> int:
    """Score fixed orders against one plan, so a change to the rule shows as a failed case."""
    plan, accent = plan_parts("Glance: A (accent) > B > C")
    cases = [
        ("the accent read last by both readers", [["B", "C", "A"], ["B", "C", "A"]], 0, ["A"]),
        ("one part read early by both readers", [["A", "C", "B"], ["A", "C", "B"]], 1, ["C"]),
        ("a part out of place for one reader only", [["A", "B", "C"], ["B", "A", "C"]], 2, []),
        ("two parts out of place for both readers", [["B", "A", "C"], ["B", "A", "C"]], 0, ["A", "B"]),
    ]
    failed = 0
    for name, orders, want, want_cost in cases:
        level, cost, _ = score(plan, accent, orders)
        ok = level == want and cost == want_cost
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {name}: Composition {level}, costing {cost or 'nothing'}")
    import os, tempfile
    with tempfile.TemporaryDirectory() as tmp:
        note = os.path.join(tmp, "note.md")
        open(note, "w", encoding="utf-8").write("## Reading order\n1. A\n")
        try:
            read_note(note, plan, legacy=False)
            ok = False
        except SystemExit as stop:
            ok = "no Order line" in str(stop)
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'} a note with no Order line stops the run")
    print(f"{5 - failed} of 5 self-test checks passed")
    return 1 if failed else 0


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--plan", required=True, help="the board's Glance line")
    ap.add_argument("--legacy-list", action="store_true", help="read the numbered reading order of a pre-Order note")
    ap.add_argument("notes", nargs="+")
    args = ap.parse_args()
    plan, accent = plan_parts(args.plan)
    if accent is None:
        raise SystemExit("the plan marks no accent, so Composition cannot be scored")
    orders = [read_note(n, plan, args.legacy_list) for n in args.notes]
    for note, order in zip(args.notes, orders):
        absent = [p for p in plan if p not in order]
        print(f"{note}: {' > '.join(order)}" + (f"  [not found in the note: {', '.join(absent)}]" if absent else ""))
    level, shared, _ = score(plan, accent, orders)
    print(f"Composition {level}" + (f", costing: {', '.join(shared)}" if shared else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

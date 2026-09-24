#!/usr/bin/env python3
"""Hold each named Product Owner rule on both sides of its declared pair.

`benchmark/parity/` already checks that every declared mirror exists and that
the kernel statements stay where `systems.py` says they live. `benchmark/format/`
already checks that a delivered artifact has the right shape. Neither reads
whether a rule stated in a skill document is the same rule stated in its Project
mirror, so a mirror can go stale in wording while every existing check stays
green: the mirror still exists (parity), the artifact it describes still
validates (format), and the rule itself has quietly drifted.

This gate names the verbatim phrases that carry a rule and requires the same
count on both sides of every declared pair that teaches it. Asymmetry is the
finding. A pair where neither side carries a phrase does not teach that rule
and is not a gap, because most pairs are not about that rule at all.

Counting rather than testing presence is the point: a phrase taught at three
sites in a source and two in its mirror is exactly the drift a presence test
calls agreement.

Phrases are chosen to carry rule meaning and nothing else, verbatim spans a
reader could grep for. Where the exact statement is the contract rather than
merely its presence, the phrase is the whole sentence including its full
stop, so a mirror cannot append a qualifier and reverse the rule while the
count holds.

The declaration lives in `z — Claude Project Sync Loop/systems.py`, a file another process
owns and this gate never writes. It is read as source text with bytecode
caching disabled and executed into a private namespace rather than imported,
so a normal import cannot leave a compiled cache behind in a directory this
system does not own.

What this gate does not catch, stated so nobody reads its green as more than
it is: prose that quotes a rule's phrase while discussing it counts as an
instance, so a mirror could reach the same count with a sentence that mentions
the rule rather than states it. Whole-sentence phrases close that for the
rules whose exact statement is the contract, and the rest rely on a reader.
This gate holds that a rule reached both sides, not that both sides mean it.

Usage:
  rule_parity.py            -> check every declared pair, exit 1 on any finding

Environment:
  CW_ROOT   overrides the system root that `sk-product-owner/` and
            `claude project/knowledge/` are resolved under. The shared
            declaration itself is always read from its one real location,
            never from this override, so a sandboxed run still checks the
            genuine 38 pairs against substitute file content.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Always the real system root, regardless of CW_ROOT, so the declaration this
# gate reads is never itself redirected by the same knob that redirects the
# files it checks.
REAL_CW = os.path.dirname(os.path.dirname(HERE))
CW = os.environ.get("CW_ROOT") or REAL_CW
GATE_DIR = os.path.join(os.path.dirname(REAL_CW), "z — Claude Project Sync Loop")
SYSTEMS_PY = os.path.join(GATE_DIR, "systems.py")
SKILL = os.path.join(CW, "sk-product-owner")
KNOWLEDGE = os.path.join(CW, "claude project", "knowledge")
SYSTEM_ID = "product-owner"

# Each rule names what carries it and how many declared pairs teach it today.
#
# `phrases` are verbatim spans, never patterns, so a reader can grep for one
# and land on the same lines this gate reads.
#
# `min_pairs` is how many declared pairs teach the rule today, measured by
# running this gate's own counting logic over the current tree. A rule moved
# from one declared pair to another leaves every per-pair count equal, 0
# against 0 here and 1 against 1 there, so counting alone reports a rule that
# left its owning pair as agreement. The floor catches the departure, and it
# also stops a declaration that resolves to no rule-bearing document at all
# from printing a pass it did not earn. A rise is not a failure, it means the
# number was updated deliberately after adding a pair that teaches the rule.
RULES = {
    # Task Mode and Bug Mode both use the bold sub-label to open the checklist
    # block inside Requirements, so this one span reaches across two mode
    # families plus every worked example that shows a filled-in checklist.
    "requirement items close under the bold Checklist sub-label": {
        "phrases": ("**Checklist**",),
        "min_pairs": 9,
    },
    # Task Mode's own rule states it as a whole sentence with the trailing
    # backtick-quoted period, which is the shape a reader would grep for
    # rather than a paraphrase of it.
    "checklist and bullet items are never closed with a period": {
        "phrases": ("Checklist and bullet items must not end with `.`",),
        "min_pairs": 1,
    },
    # Every Story and Epic acceptance criterion closes on this exact
    # checkbox line. Story Mode states it once as the rule, and the templates
    # and every worked Story/Epic example show it repeated per criterion, so the
    # count on a multi-criterion example is greater than one and still has
    # to match between the two sides.
    "acceptance criteria close with the mark-as-done checkbox": {
        "phrases": ("_Mark as done, if the criteria are met_",),
        "min_pairs": 8,
    },
    # The Barter bug corpus writes these two labels verbatim and in order.
    # Bug Mode states the rule, the Bug Report Template scaffolds it, the
    # Human Voice card carries the one named exemption that lets a title-case
    # label stand, and every worked bug example instantiates both labels.
    "bug reports carry the two fixed corpus labels in order": {
        "phrases": ("1. Observed Behavior", "2. Expected Behavior"),
        "min_pairs": 7,
    },
    # Doc Mode's ClickUp definition delimiter is the one span both the Human
    # Voice card and Doc Mode itself state as the named exception to the
    # general em-dash ban, so the exemption has to read the same on both
    # sides of both pairs that grant it.
    "the ClickUp definition delimiter is the named exception to the em-dash ban": {
        "phrases": ("*   **Term** — definition",),
        "min_pairs": 2,
    },
    # A whole sentence, not a fragment, because a mirror could otherwise keep
    # the word "full stop" while quietly narrowing when the ban applies.
    "bullet items never end with a full stop": {
        "phrases": ("Bullet items never end with a full stop.",),
        "min_pairs": 1,
    },
}


def load_systems():
    """The shared SYSTEMS declaration, read as source text, never imported.

    `z — Claude Project Sync Loop/systems.py` is large and owned by a different,
    concurrently running process. A normal `import systems` can leave a
    compiled `.pyc` behind under that directory's own `__pycache__`, which is
    a write this gate has no standing to make into a file it was told to
    only ever read. Reading the bytes and executing them into a throwaway
    namespace produces the same `SYSTEMS` dict without that side effect.
    """
    sys.dont_write_bytecode = True
    try:
        with open(SYSTEMS_PY, encoding="utf-8") as handle:
            source = handle.read()
    except OSError as exc:
        return None, f"{SYSTEMS_PY}: cannot be read ({exc})"
    namespace = {"__file__": SYSTEMS_PY, "__name__": "systems"}
    try:
        exec(compile(source, SYSTEMS_PY, "exec"), namespace)
    except Exception as exc:  # reported as a refusal, never a traceback
        return None, f"{SYSTEMS_PY}: could not be executed ({exc!r})"
    systems = namespace.get("SYSTEMS")
    if not isinstance(systems, dict):
        return None, f"{SYSTEMS_PY}: does not define a SYSTEMS dict"
    return systems, None


def body(path, drop_frontmatter=True):
    """The document's text, or None when it cannot be read.

    Frontmatter is stripped on both sides here. Most Product Owner mirrors
    open straight on a heading, but a few (the Human Voice Core mirror, the
    Router Contract mirror) carry the same YAML block their source does, so
    stripping only the source would report drift in packaging that is
    actually symmetric. The strip only fires when the very first line is the
    opening `---`, so a later `---` used as an in-body section rule is left
    alone on both sides.
    """
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError:
        return None
    if drop_frontmatter and text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    return text


def inside(root, path):
    """Whether a resolved path stays under root, checked lexically.

    Four of this system's declared sources are shared rule files
    (`hvr-core.md`, `human-voice-rules.md`, `conciseness.md`,
    `conciseness-rationale.md`), carried here as regular-file copies of cards
    in the shared knowledge tree. A system that carries them as symlinks
    instead would have every one resolve outside the skill root and be
    rejected as an escape, taking every rule they teach out of the count along
    with them. `abspath` normalises `..` segments and relative components
    without following a symlink, so a row that climbs out or names an
    absolute path is caught while a symlinked row is read through the link and
    reported under the name the declaration gives it.
    """
    root = os.path.abspath(root)
    target = os.path.abspath(path)
    return target == root or target.startswith(root + os.sep)


def main() -> int:
    systems, problem = load_systems()
    if problem is not None:
        print(problem, file=sys.stderr)
        return 2
    declared = systems.get(SYSTEM_ID)
    if not declared:
        print(f"'{SYSTEM_ID}' is not declared in systems.py, so nothing was compared", file=sys.stderr)
        return 2
    # Keyed by the mirror filename already, the way systems.py declares it,
    # so no basename re-keying happens here that could collapse two
    # differently-pathed sources that happen to share a name.
    pairs = declared.get("pairs") or {}
    if not pairs:
        print("no declared pairs, so no rule could be compared", file=sys.stderr)
        return 2

    findings, taught, compared = [], {name: 0 for name in RULES}, 0
    for mirror, source in pairs.items():
        source_path = os.path.join(SKILL, source)
        mirror_path = os.path.join(KNOWLEDGE, mirror)
        if not inside(SKILL, source_path):
            findings.append(
                f"{source}: the declaration points outside the skill root, so this "
                f"pair was not compared"
            )
            continue
        if not inside(KNOWLEDGE, mirror_path):
            findings.append(
                f"{mirror}: the declaration points outside the knowledge root, so this "
                f"pair was not compared"
            )
            continue
        left = body(source_path)
        right = body(mirror_path)
        if left is None or right is None:
            missing = source if left is None else mirror
            findings.append(f"{missing}: cannot be read, so this pair was not compared")
            continue
        compared += 1
        for name, rule in RULES.items():
            pair_teaches = False
            for phrase in rule["phrases"]:
                here, there = left.count(phrase), right.count(phrase)
                if here or there:
                    pair_teaches = True
                if here != there:
                    findings.append(
                        f"{name}: `{phrase}` appears {here}x in {source} and "
                        f"{there}x in its mirror {mirror}"
                    )
            if pair_teaches:
                taught[name] += 1

    for name, rule in RULES.items():
        if taught[name] < rule["min_pairs"]:
            findings.append(
                f"{name}: taught by {taught[name]} pair(s) and {rule['min_pairs']} "
                f"are declared, so the rule left a pair that carried it"
            )

    print(f"  pairs: {compared} of {len(pairs)} declared pairs compared")
    for name, rule in RULES.items():
        print(f"  {name}: taught by {taught[name]} pair(s), {rule['min_pairs']} declared")

    if findings:
        print(f"FAILED {len(findings)} rule parity finding(s)")
        for finding in findings:
            print(f" - {finding}")
        return 1
    print(f"PASSED {len(RULES)} rules hold on both sides of every pair that teaches them")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: FIGJAM MODEL PRE-WRITE CHECK
# ───────────────────────────────────────────────────────────────

"""Check a FigJam diagram model before it is written to a board.

A board is slow to fix once it exists: the composer owns its layout, so every
fix is a new write. Worse, neither the composer nor the generated fallback
draws all that Mermaid can say, so a model can promise a reader something the
board never shows. The rules each diagram kind carries are checked on the
Mermaid model first, and a model that breaks one is never written. The same
parse is measured, so a shape that is legal and still hard to read, such as a
rank of six steps or a connector that doubles back, is caught here rather than
on the board.

Each Mermaid block in the file is one diagram, read by its header:

- `flowchart` is a user flow unless a `%% type: process` or
  `%% type: architecture` comment line says otherwise
- `sequenceDiagram`, `stateDiagram-v2`, `erDiagram` and `gantt` are the other
  four kinds Flow Mode draws
- any other header, such as `pie`, `mindmap` or `journey`, is a kind Flow
  Mode does not draw and fails

The rules for each kind live in `figjam_checks/`, and `references/types/`
explains each one. Flowcharts and state diagrams are parsed by
`vendored/mermaid_extract.py`, a byte copy of the shared diagram skill's
extractor kept in step through `vendor.json`. It parses text only and never
renders or runs anything in a label. Sequence, ER and gantt blocks are parsed
by their own modules, because the extractor drops a sequence's dropped
features, the fields of an aliased entity and every gantt chart. Every
diagram of one flow runs the same direction, so two user flows or two
processes in one file must agree on it. A user flow and a process must also
carry one `style` line, because the board marks the first glance with its one
accent and has no other way to know where it falls.
A model that passes is composed into a board by `compose_board.py`, which keeps
its own self-test.

Usage:
  flow_check.py <model.md|model.mmd>  -> 0 every diagram passes, 1 a rule fails, 2 unreadable
  flow_check.py --self-test           -> prove each rule fails on a planted model with its own message,
                                         that the good models, the templates and the examples pass,
                                         and that the style guide's palette record still measures true
"""
from __future__ import annotations

import contextlib
import io
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendored"))
sys.path.insert(0, str(HERE))
import mermaid_extract  # noqa: E402
from figjam_checks import flowchart, layout  # noqa: E402
from figjam_checks.common import (
    ACCENT_PAIRS,
    CANVAS,
    CHARCOAL,
    LANE_PAIR,
    content_lines,
    contrast,
    type_directive,
)  # noqa: E402
from figjam_checks.er import check_er  # noqa: E402
from figjam_checks.gantt import check_gantt  # noqa: E402
from figjam_checks.sequence import check_sequence  # noqa: E402
from figjam_checks.state import check_state, check_state_header  # noqa: E402

PACKET = HERE.parent
FLOWCHART_TYPES = (flowchart.USER_FLOW, flowchart.PROCESS, flowchart.ARCHITECTURE)
HEADER_KINDS = {"flowchart": "flowchart", "graph": "flowchart", "sequencediagram": "sequence",
                "statediagram-v2": "state", "statediagram": "state", "erdiagram": "er", "gantt": "gantt"}
# Figma's list of kinds the board generator does not draw.
UNSUPPORTED = {"pie", "mindmap", "venn", "classdiagram", "journey", "timeline", "quadrantchart", "c4context",
               "c4container", "c4component", "c4dynamic", "c4deployment", "gitgraph", "requirementdiagram",
               "sankey-beta", "xychart-beta", "block-beta", "packet-beta", "architecture-beta", "kanban"}
NAMES = {"user-flow": "user flow", "process": "process", "architecture": "architecture", "sequence": "sequence",
         "state": "state", "er": "ER", "gantt": "gantt"}


# ───────────────────────────────────────────────────────────────
# 1. PROFILES AND CHECKS
# ───────────────────────────────────────────────────────────────

def header_word(block_text: str) -> str:
    """The first word of a block after any frontmatter, lowercased, which names its kind."""
    lines = content_lines(block_text)
    in_frontmatter = bool(lines) and lines[0][1] == "---"
    for _, text in lines[1:] if in_frontmatter else lines:
        if in_frontmatter:
            in_frontmatter = text != "---"
            continue
        return text.split()[0].lower()
    return ""


def profile_of(block_text: str) -> tuple[str, list[str]]:
    """The profile a block is checked as, or an empty profile with the reason it has none."""
    word = header_word(block_text)
    directive = type_directive(block_text)
    if word in UNSUPPORTED:
        return "", [f"a {word} block: Flow Mode does not draw it, see references/flow-mode.md Section 3"]
    kind = HEADER_KINDS.get(word)
    if not kind:
        return "", [f"the block header {word or '(none)'} is no diagram kind Flow Mode draws"]
    if kind == "flowchart":
        directive = directive or flowchart.USER_FLOW
        if directive not in FLOWCHART_TYPES:
            return "", [f"%% type: {directive} is no flowchart type: write user-flow, process or architecture"]
        return directive, []
    if directive and directive != kind:
        return "", [f"%% type: {directive} on a {word} block: the header already names the kind"]
    return kind, []


def check_block(block: mermaid_extract.SourceBlock, block_text: str) -> tuple[str, list[str], str, str]:
    """Return the profile, its problems, the size and shape summary and the flowchart direction."""
    profile, problems = profile_of(block_text)
    if problems:
        return profile, problems, "", ""
    if profile == "sequence":
        found, participants, messages = check_sequence(block_text)
        return profile, found, f"{participants} participants and {messages} messages", ""
    if profile == "er":
        found, entities, relationships = check_er(block_text)
        return profile, found, f"{entities} entities and {relationships} relationships", ""
    if profile == "gantt":
        found, tasks, sections = check_gantt(block_text)
        return profile, found, f"{tasks} tasks in {sections} sections", ""
    if profile == "state":
        legacy = check_state_header(block_text)
        if legacy:
            return profile, legacy, "", ""
        diagram = mermaid_extract.parse_block(block)
        states = sum(1 for node in diagram.nodes if node.shape not in ("start", "end"))
        return profile, check_state(diagram, block_text), f"{states} states and {len(diagram.edges)} transitions", ""
    if profile == flowchart.ARCHITECTURE:
        text, backward = flowchart.rewrite_backward_edges(block_text)
        diagram = mermaid_extract.parse_block(mermaid_extract.SourceBlock(block.index, text, block.source_line))
        found = flowchart.check_architecture(diagram, block_text, backward)
    else:
        diagram = mermaid_extract.parse_block(block)
        found = flowchart.check_flow(diagram, block_text, profile)
    nodes = sum(1 for node in diagram.nodes if not node.container)
    measures, shape = layout.measure(diagram)
    return profile, found + measures, f"{nodes} nodes and {len(diagram.edges)} connectors, {shape}", diagram.direction


def check(path: Path) -> int:
    """Check every diagram in a model file, print the report and return the exit code."""
    try:
        blocks = mermaid_extract.load_blocks(path)
        results = [(block, check_block(block, block.text)) for block in blocks]
    except SystemExit:
        print(f"UNREADABLE {path}: the extractor refused it")
        return 2
    if not results:
        print(f"UNREADABLE {path}: no Mermaid block found")
        return 2
    failed, ways = 0, {}
    for number, (_, (profile, problems, size, direction)) in enumerate(results, 1):
        name = f"diagram {number}, {NAMES.get(profile, 'unknown')}"
        if problems:
            failed += 1
            for problem in problems:
                print(f"  {name}: {problem}")
        else:
            print(f"  {name}: ok, {size}")
        if profile in (flowchart.USER_FLOW, flowchart.PROCESS) and direction:
            ways.setdefault(profile, set()).add(flowchart.direction_family(direction))
    for profile, found in ways.items():
        if len(found) > 1:
            print(f"FAILED the {NAMES[profile]} diagrams in {path.name} run {' and '.join(sorted(found))}: "
                  "every diagram of one flow runs the same way")
            return 1
    if failed:
        print(f"FAILED {failed} of {len(results)} diagram(s) in {path.name}")
        return 1
    print(f"PASSED {len(results)} diagram(s) in {path.name}")
    return 0


# ───────────────────────────────────────────────────────────────
# 2. SELF-TEST
# ───────────────────────────────────────────────────────────────

# The shipped templates, the worked examples and their Project mirrors must
# keep passing the rules they teach. The mirrors are absent from a copy of the
# skill without the Project package, so a missing file is reported and not
# counted. A folder README under assets/ describes its files and is no model.
KNOWLEDGE = PACKET.parent / "claude project" / "knowledge"
SHIPPED_MODELS = (
    sorted(p for p in (PACKET / "assets").rglob("*.md") if p.name != "README.md")
    + [KNOWLEDGE / "Product Owner - Assets - Flow Templates.md"]
    + sorted(KNOWLEDGE.glob("Product Owner - Assets - Flow Templates - *.md"))
    + sorted(KNOWLEDGE.glob("Product Owner - Examples - Flow - *.md"))
)
STYLE_GUIDE = PACKET / "references" / "style-guide.md"
PALETTE_BLOCK = re.compile(r"<!-- FIGJAM_PALETTE:BEGIN -->(.*?)<!-- FIGJAM_PALETTE:END -->", re.S)
PALETTE_ROW = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*`(#[0-9A-Fa-f]{6})`\s*\|\s*`(#[0-9A-Fa-f]{6})`\s*"
    r"\|\s*([\d.]+):1\s*\|\s*([\d.]+):1\s*\|",
    re.M,
)


def palette_results() -> list[tuple[str, bool, str]]:
    """The style guide's palette record names exactly the pairs the check accepts, and its ratios measure true."""
    text = STYLE_GUIDE.read_text(encoding="utf-8") if STYLE_GUIDE.is_file() else ""
    block = PALETTE_BLOCK.search(text)
    if not block:
        return [("the style guide carries its palette record", False, f"no FIGJAM_PALETTE block in {STYLE_GUIDE}")]
    rows = PALETTE_ROW.findall(block.group(1))
    recorded = {fill.lower(): stroke.lower() for _, fill, stroke, _, _ in rows}
    expected = {**ACCENT_PAIRS, LANE_PAIR[0]: LANE_PAIR[1]}
    results = [("the palette record names the pairs the check accepts", recorded == expected,
                f"record {sorted(recorded.items())} against check {sorted(expected.items())}")]
    for role, fill, stroke, text_ratio, stroke_ratio in rows:
        measured = (round(contrast(CHARCOAL, fill.lower()), 2), round(contrast(stroke.lower(), CANVAS), 2))
        ok = measured == (float(text_ratio), float(stroke_ratio))
        results.append((f"the {role} row measures {text_ratio}:1 and {stroke_ratio}:1", ok, f"measured {measured}"))
    return results


def run_quietly(path: Path) -> tuple[int, str]:
    """Run the check on one file and return its exit code with the report it printed."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = check(path)
    return code, out.getvalue()


def self_test() -> int:
    """Prove each rule fires on its planted model and every good and shipped model passes."""
    from figjam_checks.fixtures import GOOD, PLANTED

    results = []
    with tempfile.TemporaryDirectory(prefix="po-flow-check-selftest-") as scratch:
        for name, model in GOOD.items():
            path = Path(scratch) / ("good.md" if model.startswith("```") else "good.mmd")
            path.write_text(model, encoding="utf-8")
            code, output = run_quietly(path)
            results.append((f"{name} passes", code == 0, output))
        for name, (model, message) in PLANTED.items():
            path = Path(scratch) / ("planted.md" if model.startswith("```") else "planted.mmd")
            path.write_text(model, encoding="utf-8")
            code, output = run_quietly(path)
            results.append((f"{name} fails with '{message}'", code == 1 and message in output, output))
    for model in SHIPPED_MODELS:
        if not model.is_file():
            print(f"SKIP  {model.name} is not in this install")
            continue
        if "```mermaid" not in model.read_text(encoding="utf-8"):
            # A shipped model that lost its diagram would otherwise drop out of the proof unseen.
            results.append((f"{model.name} carries a Mermaid block", False, "no ```mermaid block in a shipped model"))
            continue
        code, output = run_quietly(model)
        results.append((f"{model.relative_to(model.parents[1]) if PACKET in model.parents else model.name} passes",
                        code == 0, output))
    results += palette_results()
    skill_types = re.search(r'DIAGRAM_TYPES = \(([^)]*)\)', (PACKET / "SKILL.md").read_text(encoding="utf-8"))
    declared = set(re.findall(r'"([a-z-]+)"', skill_types.group(1))) if skill_types else set()
    results.append(("SKILL.md DIAGRAM_TYPES names the types this check dispatches", declared == set(NAMES),
                    f"SKILL.md {sorted(declared)} against the check {sorted(NAMES)}"))
    for name, ok, output in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            print("      " + output.strip().replace("\n", "\n      "))
    passed = sum(1 for _, ok, _ in results if ok)
    print(f"{passed} of {len(results)} self-test checks passed")
    return 0 if passed == len(results) else 1


# ───────────────────────────────────────────────────────────────
# 3. COMMAND LINE
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Dispatch the command line and return the exit code the usage lines document."""
    args = sys.argv[1:]
    if args == ["--self-test"]:
        return self_test()
    if len(args) != 1:
        print(__doc__.strip().split("Usage:")[1], file=sys.stderr)
        return 2
    return check(Path(args[0]))


if __name__ == "__main__":
    sys.exit(main())

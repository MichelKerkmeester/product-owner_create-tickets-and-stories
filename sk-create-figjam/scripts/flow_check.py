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
its own self-test. With node on the PATH the board is also composed in memory,
and a label the composer would wrap one word alone onto its last line is
reported, since a shorter label is the fix and a wider box is not. Without node,
or when the trace fails, it prints one `Label: skipped` line instead.
On a user flow or a process the same board prints a `Glance:` line, the order
a reader meets its nodes, the accent first and then column by column along the
flow, so the glance lines are planned from where the composer draws each node
rather than from its path. A `Row:` line, never a failure, names a line between
two main-row steps that bends off the row, with the node standing between them.
With `--notes`, the same board names the first side of each noted node that
holds a single sticky on a `Sides:` line, with how it lines up with the node,
or says the node is boxed in, so the gate can offer pins with a legend or a
recompose before any write.

Usage:
  flow_check.py <model.md|model.mmd>  -> 0 every diagram passes, 1 a rule fails, 2 unreadable
  flow_check.py <model.md> --notes <id,id>
                                      -> the same, plus a `Sides:` line for each noted node id
  flow_check.py --self-test           -> prove each rule fails on a planted model with its own message,
                                         that the good models, the templates and the examples pass,
                                         and that the style guide's palette record still measures true
"""
from __future__ import annotations

import contextlib
import io
import re
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendored"))
sys.path.insert(0, str(HERE))
import mermaid_extract  # noqa: E402
from figjam_checks import board_geometry as geometry, flowchart, layout  # noqa: E402
from figjam_checks.common import (
    ACCENT_PAIRS,
    CANVAS,
    CHARCOAL,
    LANE_PAIR,
    FOCUS_DIRECTIVE,
    content_lines,
    contrast,
    focus_line_problems,
    focus_reason,
    statements,
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
    profile, problems, size, direction = check_kind(block, block_text)
    # A focus line may say why the first glance falls there, in words short enough for the key.
    focus = focus_line_problems(block_text) if profile else []
    if profile in (flowchart.USER_FLOW, flowchart.PROCESS):
        focus += flow_focus_problems(block_text)
    return profile, problems + focus, size, direction


def flow_focus_problems(block_text: str) -> list[str]:
    """A focus line on a user flow or a process, which the composer refuses unless it gives the styled node a reason.

    The style line already places the accent there, so the focus line only says why, on that node.
    """
    values = FOCUS_DIRECTIVE.findall(block_text)
    if not values:
        return []
    styled = {words[1] for words in (s.split() for s in statements(block_text)) if len(words) > 2
              and words[0].lower() == "style"}
    target, reason = focus_reason(values[0])
    if len(values) > 1 or not reason or target not in styled:
        return ["%% focus on a user flow or a process: mark the first glance with a style line, and give its reason as "
                "%% focus: <styled id> because <reason>"]
    return []


def check_kind(block: mermaid_extract.SourceBlock, block_text: str) -> tuple[str, list[str], str, str]:
    """The kind's own rules: the profile, its problems, the size and shape summary and the flowchart direction."""
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


def composer_refusals(block: mermaid_extract.SourceBlock, number: int) -> list[str]:
    """What the composer refuses in a block this check passed, such as a goal line naming a step.

    The composer reads the comment lines this check does not, so a model it would refuse fails here too,
    rather than passing a gate the write then stops at.
    """
    # compose_board imports this module, so it is loaded here rather than at the top of the file.
    import compose_board

    model, problems, _ = compose_board.build_model(block, number)
    return problems if problems or model is not None else ["the composer built no board from this diagram"]


def board_lines(block: mermaid_extract.SourceBlock, number: int, notes: list[str] | None = None) -> list[str]:
    """The lines a board composed in memory gives the model: its labels, its reading order, its row and its notes.

    The composer fits a label inside its shape and never widens the box for it, so one word can be left alone
    on a last line and the model is the only place to shorten it. A missing node or a failed trace prints one
    skipped line, so the model reads its labels by hand instead of reading silence as a pass. A model that will
    not compose says nothing here, because the check reports it. A user flow or a process also gets a `Glance:`
    line, the order a reader meets its nodes, and a `Row:` line for each line that bends off the main row.
    Each id in `notes` also gets a `Sides:` line from the same board, naming the side its single sticky takes
    and how it lines up, or saying no side holds one.
    """
    flow = profile_of(block.text)[0] in (flowchart.USER_FLOW, flowchart.PROCESS)
    if not shutil.which("node"):
        skipped = ["Label: skipped, node is not on the PATH, so read each label for one word alone on its last line"]
        glance = ["Glance: skipped, node is not on the PATH, so plan the main row in path order and the nodes off "
                  "it last"] if flow else []
        return skipped + glance + [f"Sides: skipped for {node}, node is not on the PATH, so offer pins with a legend"
                                   for node in notes or []]
    # compose_board imports this module, so it is loaded here rather than at the top of the file.
    import compose_board
    from figjam_checks import design as board_design

    model, problems, _ = compose_board.build_model(block, number)
    if problems or model is None:
        return []
    design, _ = board_design.resolve()
    geometry.use_design(design)
    try:
        with tempfile.TemporaryDirectory(prefix="po-flow-check-labels-") as work:
            drawn = geometry.run_trace(compose_board.fill_template(model, board_design.theme(design)), Path(work))
    except (OSError, ValueError, RuntimeError) as error:
        # A node stack trace runs to many lines, and the skipped line keeps to one.
        first = str(error).splitlines()[0] if str(error).strip() else "no message"
        return ([f"Label: skipped, the trace failed ({first}), so read each label for one word alone on its last line"]
                + (["Glance: skipped, the trace failed, so plan the main row in path order and the nodes off it last"]
                   if flow else [])
                + [f"Sides: skipped for {node}, the trace failed, so offer pins with a legend" for node in notes or []])
    lines = [f"Label: {line}, so shorten it, or reword it in the source's words, when that keeps the meaning"
             for line in geometry.orphan_words(drawn)]
    if flow:
        lines += glance_lines(model, drawn)
    for node, label, side, align in geometry.sticky_sides(drawn, notes or []):
        if label is None:
            lines.append(f"Sides: {node} names no node: write the id of a node this diagram draws")
        elif side:
            lines.append(f"Sides: {label} takes its sticky {side}, {align}")
        else:
            lines.append(f"Sides: {label} is boxed in, no side holds a sticky, so offer pins with a legend "
                         "or a change to the model that frees a side before any write")
    return lines


def glance_lines(model: dict, drawn: dict) -> list[str]:
    """The `Glance:` line of a flow's reading order, and a `Row:` line for each line that bends off its row.

    The accent is marked as such and the goal too, since the glance lines split at the goal. A bend is advice,
    never a failure: the board still reads, and the model is where it is mended.
    """
    nodes = {n["id"]: n for n in model["nodes"]}
    name = {node_id: " ".join(n["label"].replace("<br>", " ").split()) or node_id for node_id, n in nodes.items()}
    marks = {node_id: " (" + ", ".join(m for m, on in (("accent", n.get("accent")), ("goal", n["kind"] == "success"))
                                       if on) + ")" if n.get("accent") or n["kind"] == "success" else ""
             for node_id, n in nodes.items()}
    lines = ["Glance: " + " > ".join(name[i] + marks[i] for i in geometry.reading_order(drawn, model))]
    for start, end, between in geometry.row_breaks(drawn, model):
        line = f"Row: the line from {name[start]} to {name[end]} bends off its row"
        if between:
            line += f" round {', '.join(name[i] for i in between)}"
        moved = [i for i in between if model["zoneMode"] == "stage" and model["zones"]
                 and nodes[i]["zone"] != nodes[end]["zone"]]
        if moved:
            line += (f", so move {', '.join(name[i] for i in moved)} into the zone {name[end]} sits in, "
                     "where it shares that step's column")
        else:
            line += ", so name the break at the gate and offer a model that keeps the row straight"
        lines.append(line)
    return lines


def check(path: Path, notes: list[str] | None = None) -> int:
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
    for number, (block, (profile, problems, size, direction)) in enumerate(results, 1):
        name = f"diagram {number}, {NAMES.get(profile, 'unknown')}"
        problems = problems or composer_refusals(block, number)
        if problems:
            failed += 1
            for problem in problems:
                print(f"  {name}: {problem}")
        else:
            print(f"  {name}: ok, {size}")
            # A label the board would strand one word on is the model's to shorten, so it never fails here.
            lines = board_lines(block, number, notes)
            for line in lines:
                print(line)
            # A notes id the board does not draw is a typo in the command, never a boxed-in node.
            failed += any(line.startswith("Sides:") and "names no node" in line for line in lines)
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
# counted. A folder README under assets/ describes its files and the design
# file holds the board's style, so neither is a model.
KNOWLEDGE = PACKET.parent / "claude project" / "knowledge"
NOT_MODELS = {"README.md", "figjam-design.md"}
SHIPPED_MODELS = (
    sorted(p for p in (PACKET / "assets").rglob("*.md") if p.name not in NOT_MODELS)
    + [KNOWLEDGE / "Product Owner - Assets - Flow Templates.md"]
    + sorted(KNOWLEDGE.glob("Product Owner - Assets - Flow Templates - *.md"))
    + sorted(KNOWLEDGE.glob("Product Owner - Examples - Flow - *.md"))
)
CHECK_BLOCK = re.compile(r"^### Check\n\n```text\n(.*?)\n```", re.S | re.M)
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


def label_results() -> list[tuple[str, bool, str]]:
    """A label the composer would wrap one word alone is reported for shortening, and a short one is not.

    The readings that compose a board need node on the PATH, so a missing node skips them the way an absent
    install skips a shipped model, and the skip itself is read on every machine.
    """
    # Only the self-test patches, so a plain check run never loads unittest.
    import unittest.mock

    results = []
    with tempfile.TemporaryDirectory(prefix="po-flow-check-labels-") as scratch:
        path = Path(scratch) / "labels.mmd"
        path.write_text("flowchart LR\n    a([Order placed]) --> b[Send the parcel]\n    b --> c([Parcel sent])\n"
                        "    style c fill:#CDF4D3\n", encoding="utf-8")
        # A skip read on every machine, so a label the check could not read never passes for a clean one.
        with unittest.mock.patch.object(shutil, "which", return_value=None):
            code, output = run_quietly(path)
        skip = "Label: skipped, node is not on the PATH"
        results.append(("a missing node prints a skipped Label line",
                        code == 0 and any(line.startswith(skip) for line in output.splitlines()), output))
    if not shutil.which("node"):
        print("SKIP  a label's last line needs node on the PATH to compose the board")
        return results
    cases = (
        ("a label that wraps one word alone is reported for shortening",
         "flowchart LR\n    a([Order placed]) --> b[Book a courier pickup]\n    b --> c([Parcel sent])\n"
         "    style c fill:#CDF4D3\n",
         "Label: Book a courier pickup leaves 'pickup' alone"),
        ("a label FigJam wraps narrower than the node measure is still reported",
         "flowchart LR\n    a([Email verified]) --> b([Editor with welcome tip])\n    style b fill:#CDF4D3\n",
         "Label: Editor with welcome tip may leave 'tip' alone"),
        ("a decision label FigJam strands at the traced diamond size is reported as leaving its word",
         "flowchart LR\n    a([Order list]) --> d{Drop-off point or courier?}\n    d -->|Drop-off| b([Drop-off booked])\n"
         "    d -->|Pickup| c([Pickup booked])\n    style d fill:#FFC2EC,stroke:#F849C1\n",
         "Label: Drop-off point or courier? leaves 'courier?' alone"),
        ("a decision label of wide letters whose last word FigJam strands is reported though it is 26 characters",
         "flowchart LR\n    a([Order list]) --> d{New price compared to old?}\n    d -->|Higher| b([Pay difference])\n"
         "    d -->|Lower| c([Credit difference])\n    style d fill:#FFC2EC,stroke:#F849C1\n",
         "Label: New price compared to old? leaves 'old?' alone"),
        ("a decision label that wraps clear at the glyph measure reports none though it is 27 characters",
         "flowchart LR\n    a([Order list]) --> d{Within 30 days of delivery?}\n    d -->|Yes| b([Return started])\n"
         "    d -->|No| c([Contact support])\n    style d fill:#FFC2EC,stroke:#F849C1\n",
         None),
        ("a decision label that wraps clear at that width reports none",
         "flowchart LR\n    a([Order list]) --> d{Drop-off or courier pickup?}\n    d -->|Drop-off| b([Drop-off booked])\n"
         "    d -->|Pickup| c([Pickup booked])\n    style d fill:#FFC2EC,stroke:#F849C1\n",
         None),
        ("a model with short labels reports none",
         "flowchart LR\n    a([Order placed]) --> b[Send the parcel]\n    b --> c([Parcel sent])\n"
         "    style c fill:#CDF4D3\n",
         None),
    )
    with tempfile.TemporaryDirectory(prefix="po-flow-check-labels-") as scratch:
        for name, model, wanted in cases:
            path = Path(scratch) / "labels.mmd"
            path.write_text(model, encoding="utf-8")
            code, output = run_quietly(path)
            reported = "\n".join(line for line in output.splitlines() if line.startswith("Label:"))
            results.append((name, code == 0 and (wanted in reported if wanted else not reported), output))
        path.write_text("flowchart LR\n    a([Order placed]) --> b[Send the parcel]\n    b --> c([Parcel sent])\n"
                        "    style c fill:#CDF4D3\n", encoding="utf-8")
        # A trace that dies is no fault of the model, so it says so rather than letting the label pass unread.
        with unittest.mock.patch.object(geometry, "run_trace", side_effect=RuntimeError("planted")):
            code, output = run_quietly(path)
        failed = "Label: skipped, the trace failed (planted)"
        results.append(("a failed trace prints a skipped Label line", code == 0 and failed in output, output))
        # The last node may widen the board to its right, and the middle one has the title above, the key
        # below and a neighbour on each side, so a compact board boxes it in.
        code, output = run_quietly(path, ["c", "b"])
        results.append(("a noted node names the side its sticky takes, or that it is boxed in",
                        code == 0 and "Sides: Parcel sent takes its sticky right" in output
                        and "Sides: Send the parcel is boxed in" in output, output))
        code, output = run_quietly(path, ["c", "ghost"])
        results.append(("a notes id the board does not draw fails the check instead of reading as boxed in",
                        code == 1 and "Sides: ghost names no node" in output and "boxed in" not in output, output))
        # A node off the path that takes a column of its own between two row steps is read between them, and
        # the row line bends round it, until the node joins the next step's zone and its column.
        zoned = ("flowchart LR\n    %% zone: Find: a, d, x{extra}\n    %% zone: Act: b{moved}, c\n    %% zone: Done: e\n"
                 "    a([Order list]) --> d{{Within 30 days?}}\n    d -->|Yes| b[Start a return]\n"
                 "    d -->|No| x([Contact support])\n    b --> c[Pick a reason]\n    c --> e([Return confirmed])\n"
                 "    style d fill:#FFC2EC,stroke:#F849C1\n")
        path.write_text(zoned.format(extra="", moved=", x").replace("a, d, x", "a, d"), encoding="utf-8")
        code, moved = run_quietly(path)
        path.write_text(zoned.format(extra="", moved=""), encoding="utf-8")
        code_split, split = run_quietly(path)
        glance = "Glance: Within 30 days? (accent) > Order list > Contact support > Start a return"
        results.append(("a flow prints the order a reader meets it, and a node between two row steps is met there "
                        "and named on a Row line", code_split == 0 and glance in split
                        and "Row: the line from Within 30 days? to Start a return bends off its row round Contact "
                        "support, so move Contact support into the zone Start a return sits in" in split, split))
        results.append(("the same node in the next step's zone shares its column and leaves the row straight",
                        code == 0 and "Glance: Within 30 days? (accent) > Order list > Start a return > Contact support"
                        in moved and "Row:" not in moved, moved))
        # A decision in the accent's lane is read in its column, after an entry to its left, and a decision joined
        # to the accent keeps its column place whether or not a node stands between them.
        path.write_text("%% type: process\nflowchart LR\n    subgraph customer [\"Customer\"]\n        report([Damage reported])\n"
                        "        photo[/Send the second photo/]\n    end\n    subgraph cs [\"CS agent\"]\n"
                        "        check{Damage clear in the photo?}\n        approve[Approve the claim]\n        log[(Claims table)]\n"
                        "    end\n    subgraph warehouse [\"Warehouse\"]\n        pickup[Book a courier]\n        inspect[Inspect the item]\n"
                        "        refund([Refund released])\n    end\n    report --> check\n    check -->|Unclear| photo\n"
                        "    photo --> check\n    check -->|Clear| approve\n    approve -->|Claim queued| pickup\n"
                        "    approve -->|Logs| log\n    pickup --> inspect\n    inspect --> refund\n"
                        "    style approve fill:#FFE0C2,stroke:#FF9E42\n", encoding="utf-8")
        code, output = run_quietly(path)
        results.append(("a decision in the accent's lane is read in its column, after an entry to its left",
                        code == 0 and "Glance: Approve the claim (accent) > Damage reported > Damage clear in the photo?"
                        in output, output))
        path.write_text("flowchart LR\n    %% goal: updated\n    page([Booking page]) --> dates[Pick new dates]\n"
                        "    dates --> free{Room free on those dates?}\n    free -->|Yes| price{New price?}\n"
                        "    free -->|No| other[See other rooms]\n    other -->|Pick a room| price\n"
                        "    price -->|Higher| pay[Pay difference]\n    price -->|Lower| credit[Credit difference]\n"
                        "    price -->|Same| merge((.))\n    pay --> merge\n    credit --> merge\n"
                        "    merge --> updated([Updated booking])\n    style price fill:#FFC2EC,stroke:#F849C1\n", encoding="utf-8")
        code, output = run_quietly(path)
        results.append(("a decision joined to the accent keeps its column place",
                        code == 0 and "Glance: New price? (accent) > Booking page" in output, output))
        path.write_text("flowchart LR\n    a([Order list]) --> b[Pick the item]\n    b --> d{Within 30 days?}\n"
                        "    d -->|Yes| r[Start a return]\n    d -->|No| s([Contact support])\n    r --> e([Return confirmed])\n"
                        "    style b fill:#FFC2EC,stroke:#F849C1\n    style d fill:#FFC2EC,stroke:#F849C1\n", encoding="utf-8")
        code, output = run_quietly(path)
        glance_line = next((line for line in output.splitlines() if line.startswith("Glance:")), "")
        results.append(("a second node in the accent fill joined to the first is named once",
                        code == 0 and glance_line.count("Within 30 days?") == 1, output))
        # A line that skips a step on its way to the next one bends on purpose, so it is never a broken row.
        path.write_text("flowchart LR\n    %% zone: Sign in: o, q, g\n    %% zone: Shop: h, k, p\n"
                        "    o([Open the app]) --> q{Logged in?}\n    q -->|No| g[Log in]\n    g --> h[Home screen]\n"
                        "    q -->|Yes| h\n    h --> k[Cart]\n    k --> p([Paid])\n    style q fill:#FFC2EC,stroke:#F849C1\n",
                        encoding="utf-8")
        code, output = run_quietly(path)
        results.append(("a line that skips a step on the row is no bent row", code == 0 and "Glance:" in output
                        and "Row:" not in output, output))
        path.write_text("flowchart LR\n    %% goal: b\n    a([Start]) --> b[Pack it]\n    b --> c([Done])\n"
                        "    style b fill:#FFC2EC,stroke:#F849C1\n", encoding="utf-8")
        code, output = run_quietly(path)
        results.append(("a goal line the composer refuses fails the check too", code == 1 and "is not an end" in output,
                        output))
    results.append(sides_boxed_result())
    return results


def sides_boxed_result() -> tuple[str, bool, str]:
    """A node with a shape on every side is boxed in, and freeing its right side gives the sticky that side."""
    def shape(name: str, x: int, y: int) -> dict:
        return {"id": name, "name": name, "type": "SHAPE_WITH_TEXT", "shape": "SQUARE", "x": x, "y": y,
                "w": 224, "h": 96, "text": name[5:], "parent": "Board"}
    board = {"id": "board", "name": "Board", "type": "SECTION", "x": 0, "y": 0, "w": 2400, "h": 2400,
             "text": "", "parent": ""}
    hemmed = [shape("node:noted", 1000, 1000), shape("node:right", 1300, 1000), shape("node:below", 1000, 1150),
              shape("node:above", 1000, 850), shape("node:left", 700, 1000)]
    boxed = geometry.sticky_sides({"nodes": [board, *hemmed], "connectors": []}, ["noted"])
    freed = geometry.sticky_sides({"nodes": [board, *[n for n in hemmed if n["name"] != "node:right"]],
                                   "connectors": []}, ["noted"])
    # Two noted nodes on adjacent rows: the first sticky takes the right, so the second goes below or left.
    stacked = geometry.sticky_sides({"nodes": [board, shape("node:upper", 1000, 1000), shape("node:lower", 1000, 1200)],
                                     "connectors": []}, ["upper", "lower"])
    # The lower node can only take the right, so the upper one gives up the right and takes the side above.
    pinned = geometry.sticky_sides({"nodes": [board, shape("node:upper", 1000, 1000), shape("node:lower", 1000, 1200),
                                              shape("node:under", 1000, 1350), shape("node:beside", 700, 1200)],
                                    "connectors": []}, ["upper", "lower"])
    # An end dot past the node pushes the right-hand sticky out, and past one sticky's width it reads as the dot's.
    def dotted(gap: int) -> list:
        dot = {"id": "node:__end1", "name": "node:__end1", "type": "SHAPE_WITH_TEXT", "shape": "ELLIPSE",
               "x": 1224 + gap, "y": 1032, "w": 32, "h": 32, "text": "", "parent": "Board"}
        line = {"name": "edge:noted->__end1", "line": "STRAIGHT", "label": "", "start": {"endpointNodeId": "node:noted",
                "magnet": "RIGHT"}, "end": {"endpointNodeId": "node:__end1", "magnet": "LEFT"}}
        return geometry.sticky_sides({"nodes": [board, shape("node:noted", 1000, 1000), dot], "connectors": [line]},
                                     ["noted"])
    near, far = dotted(76), dotted(276)
    ok = (boxed == [("noted", "noted", None, None)] and freed == [("noted", "noted", "right", "top aligned")]
          and stacked[0] == ("upper", "upper", "right", "top aligned") and stacked[1][2] in ("below", "left")
          and pinned == [("upper", "upper", "above", "left aligned"), ("lower", "lower", "right", "top aligned")]
          and near[0][2] == "right" and far[0][2] not in ("right", None))
    return ("a node with a shape on every side is boxed in, a freed side takes the sticky, a placed sticky "
            "takes its side from the next node, the sides are chosen so every noted node gets one and no sticky "
            "stands further than one sticky's width from its node", ok,
            f"boxed {boxed}, freed {freed}, stacked {stacked}, pinned {pinned}, near {near}, far {far}")


def run_quietly(path: Path, notes: list[str] | None = None) -> tuple[int, str]:
    """Run the check on one file and return its exit code with the report it printed."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = check(path, notes)
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
        shown = f"{model.relative_to(model.parents[1]) if PACKET in model.parents else model.name}"
        results.append((f"{shown} passes", code == 0, output))
        # A worked example shows the check's output, so a model copying it learns what the check really prints.
        printed = CHECK_BLOCK.search(model.read_text(encoding="utf-8"))
        if PACKET in model.parents and model.parent.name == "examples":
            # Every skill example shows its check, so a heading that drifts cannot drop it from this proof.
            results.append((f"{shown} carries a Check block", printed is not None, "no `### Check` text block"))
        if printed and shutil.which("node"):
            wanted = output.replace(f"in {model.name}", "in model.md").rstrip("\n")
            results.append((f"{shown} shows the output the check prints", printed.group(1) == wanted,
                            f"shown:\n{printed.group(1)}\nprinted:\n{wanted}"))
    results += label_results()
    results += palette_results()
    # The packet router declares DIAGRAM_TYPES in SKILL.md, or in the sibling ROUTER.md
    # SKILL.md links once the machine router moves there, so both are read in that order.
    skill_types = None
    for router_doc in ("SKILL.md", "ROUTER.md"):
        if (PACKET / router_doc).is_file():
            skill_types = re.search(r'DIAGRAM_TYPES = \(([^)]*)\)', (PACKET / router_doc).read_text(encoding="utf-8"))
        if skill_types:
            break
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
    notes = None
    if len(args) == 3 and args[1] == "--notes":
        notes = [node.strip() for node in args[2].split(",") if node.strip()]
        args = args[:1]
    if len(args) != 1:
        print(__doc__.strip().split("Usage:")[1], file=sys.stderr)
        return 2
    return check(Path(args[0]), notes)


if __name__ == "__main__":
    sys.exit(main())

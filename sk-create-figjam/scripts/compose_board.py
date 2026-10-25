#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: FIGJAM BOARD COMPOSITION
# ───────────────────────────────────────────────────────────────

"""Turn a checked diagram model into the use_figma code that composes its board.

The board is drawn by `assets/compose-board.js`, which lays out and styles the
diagram itself: a framed board with a title block, tinted zones, shapes sized to
their text, routed connectors and a key. This script fills that file's MODEL from
the same parse `flow_check.py` checks, so the board holds exactly what passed the
check and the read-back counts it against the same numbers. A model that fails
the check is refused, because a composed board is as wrong as the model it drew.

Board text comes from comment lines the generator never needed, so the model
stays plain Mermaid:

- `%% title: Start a return` names the board, and falls back to a Mermaid
  frontmatter title, a sequence or gantt `title` line, then the diagram's place
- `%% subtitle: ...` is one sentence under the title on who reads it and why
- `%% source: ...` is the line under the key naming the sources and what was
  left out
- `%% zone: Find the order: orders, detail` groups nodes into a tinted zone. A
  user flow or a process without lanes reads its zones in flow order, an ER
  diagram draws each one around its entities, and lanes and composite states
  are zones already
- `%% focus: id` names the one thing the first glance lands on in a diagram
  that takes no `style` line: a node of an architecture, a state or an ER
  diagram, a message's number in a sequence, a task's id or name in a gantt.
  It is optional, and a user flow or a process marks its first glance with a
  `style` line instead

The board's style comes from `assets/figjam-design.md`, read over the composer's
built-in design by `figjam_checks/design.py`. Only the tokens it changes are
sent, in the code's THEME. A token that cannot stand falls back to its built-in
value and a design file that cannot be read falls back whole, each named on a
`DESIGN` line on stderr, so a bad edit never stops a board.

Usage:
  compose_board.py <model.md> [--diagram N] [--out path]  -> 0 the filled code is written, 1 the model fails
                                                             the check, 2 unreadable or no such diagram
  compose_board.py <model.md> --model                      -> print the MODEL as JSON instead of the code
  compose_board.py --template                              -> print the compact code with its MODEL and THEME
                                                             placeholders, the text the Project's composer
                                                             Knowledge file carries
  compose_board.py --design-check                          -> print the design a board is drawn in, what it
                                                             changes, its measures and the THEME it sends: 0 the
                                                             design reads with no warning, 1 one or more warnings
  compose_board.py --self-test                             -> prove every shipped model composes, its counts
                                                             match the check, the code fits one use_figma call and
                                                             the board it draws keeps its geometry and its design
"""
from __future__ import annotations

import contextlib
import copy
import io
import itertools
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendored"))
sys.path.insert(0, str(HERE))
import flow_check  # noqa: E402
import mermaid_extract  # noqa: E402
from figjam_checks import board_geometry as geometry  # noqa: E402
from figjam_checks import design as board_design  # noqa: E402
from figjam_checks import er, flowchart, gantt, sequence, state  # noqa: E402
from figjam_checks.board_fixtures import MODELS as DEFECT_MODELS, NEEDS_STACKING  # noqa: E402
from figjam_checks.common import ACCENT_PAIRS, CANVAS, content_lines, contrast, statements  # noqa: E402
from figjam_checks.layout import closing_edges  # noqa: E402

PACKET = HERE.parent
TEMPLATE = PACKET / "assets" / "compose-board.js"
# The claude.ai Project has no Python, so its agent fills MODEL by hand from a copy of the compact code.
PROJECT_COPY = PACKET.parent / "claude project" / "knowledge" / "Product Owner - Assets - Flow Board Composer.md"
PROJECT_FENCE = re.compile(r"```javascript\n(.*?)\n```", re.S)
PROJECT_DESIGN = PROJECT_COPY.with_name("Product Owner - Assets - Flow Board Design.md")
PROJECT_THEME = re.compile(r"## 1\. THE THEME.*?```text\n(.*?)\n```", re.S)
PLACEHOLDER = "__MODEL__"
THEME_PLACEHOLDER = "__THEME__"
FILLED = re.compile(f"{PLACEHOLDER}|{THEME_PLACEHOLDER}")
# use_figma takes at most 50,000 characters of code, and the model rides inside it.
MAX_CODE_CHARS = 50_000
# The composer's gap between two zones. A zone within two of them on any side sits beside it and takes another tint.
ZONE_GAP = 48
DIRECTIVE = re.compile(r"^\s*%%\s*(title|subtitle|source|zone|focus)\s*:\s*(.+?)\s*$", re.I)
ARCHITECTURE_KINDS = {"client": "client", "gateway": "gateway", "service": "service", "datastore": "datastore",
                      "external": "external", "async": "queue"}
FLOW_SHAPES = {"rhombus": "decision", "circle": "merge", "cylinder": "datastore", "subroutine": "subprocess",
               "parallelogram": "io"}
# A styled end names its own outcome: red marks a failure, any other accent the goal.
ERROR_FILLS = {"#ffcdc2"}
ARROWS = {"->>": "request", "-->>": "reply", "-)": "async", "--)": "asyncReply"}
# A gantt bar is placed in whole days on a date chart and in minutes on a one-day chart.
SECONDS_PER_DAY, SECONDS_PER_MINUTE = 86400, 60
CARDINALITY_WORDS = {"||": "1", "|o": "0..1", "o|": "0..1", "}o": "0..n", "o{": "0..n", "}|": "1..n", "|{": "1..n"}


# ───────────────────────────────────────────────────────────────
# 1. BOARD TEXT AND ZONES
# ───────────────────────────────────────────────────────────────

def directives(block_text: str) -> tuple[dict[str, str], list[dict]]:
    """The title, subtitle and source comments, and the zones in the order they were written."""
    text, zones = {}, []
    for line in block_text.splitlines():
        match = DIRECTIVE.match(line)
        if not match:
            continue
        key, value = match.group(1).lower(), match.group(2)
        if key != "zone":
            text[key] = value
            continue
        label, _, members = value.rpartition(":")
        zone_id = re.sub(r"[^a-z0-9]+", "-", label.strip().lower()).strip("-") or f"zone{len(zones) + 1}"
        zones.append({"id": zone_id, "label": label.strip(),
                      "members": [m.strip() for m in members.split(",") if m.strip()]})
    return text, zones


def zone_problems(zones: list[dict], node_ids: list[str], every_node: bool) -> list[str]:
    """A zone names nodes that exist, a node sits in one zone at most, and in flow order every node sits in one."""
    problems, owner = [], {}
    for zone in zones:
        if not zone["label"]:
            problems.append("a %% zone line has no label: write %% zone: Label: id, id")
        if not zone["members"]:
            problems.append(f"zone {zone['label']} names no node")
        for member in zone["members"]:
            if member not in node_ids:
                problems.append(f"zone {zone['label']} names {member}, which is no node in the diagram")
            elif member in owner:
                problems.append(f"node {member} sits in zones {owner[member]} and {zone['label']}: one zone each")
            else:
                owner[member] = zone["label"]
    if zones and every_node:
        loose = [node for node in node_ids if node not in owner]
        if loose:
            problems.append(f"{', '.join(loose)} sit in no zone: once a flow has zones, every node sits in one")
    return problems


FOCUS_LINE = re.compile(r"^\s*%%\s*focus\s*:", re.I | re.M)


def focus_problems(model: dict, profile: str, target: str, lines: int) -> list[str]:
    """Mark the one thing a `%% focus:` line names, or say why it names nothing."""
    if profile in (flowchart.USER_FLOW, flowchart.PROCESS):
        return ["%% focus on a user flow or a process: mark the first glance with a style line"]
    if lines > 1:
        return [f"{lines} %% focus lines, at most 1: the first glance is one thing"]
    if profile == "sequence":
        marked = model["messages"][int(target) - 1: int(target)] if target.isdigit() else []
        what = "a message number that exists"
    elif profile == "gantt":
        tasks = [task for section in model["sections"] for task in section["tasks"]]
        marked = [task for task in tasks if target in (task["id"], task["name"])][:1]
        what = "a task id or name"
    else:
        marked = [node for node in model["nodes"] if node["id"] == target][:1]
        what = "a node id"
    if not marked:
        return [f"%% focus: {target or '(empty)'} names nothing: write {what}"]
    marked[0]["accent"] = True
    return []


def board_title(block_text: str, text: dict[str, str], number: int) -> str:
    """The board's title: a `%% title:` line, a frontmatter title, a `title` line, then the diagram's place."""
    if text.get("title"):
        return text["title"]
    lines = content_lines(block_text)
    if lines and lines[0][1] == "---":
        for _, line in lines[1:]:
            if line == "---":
                break
            if line.lower().startswith("title:"):
                return line.split(":", 1)[1].strip().strip('"')
    for _, line in lines:
        if line.split()[0] == "title":
            return line[len("title"):].strip()
    return f"Diagram {number}"


# ───────────────────────────────────────────────────────────────
# 2. ONE MODEL PER KIND
# ───────────────────────────────────────────────────────────────

def accent_fills(block_text: str) -> dict[str, str]:
    """The fill a `style` line gives each node, read the way the check reads it."""
    found = {}
    for statement in statements(block_text):
        words = statement.split()
        if len(words) > 2 and words[0].lower() == "style":
            fill = flowchart.colour(statement, "fill")
            stroke = flowchart.colour(statement, "stroke")
            found[words[1]] = fill or flowchart.PAIRED_FILL.get(stroke, "")
    return found


def longest_reach(steps: list[str], edges: list[mermaid_extract.Edge]) -> dict[str, int]:
    """How many steps the longest loop-free path from a start takes to reach each step."""
    following = {step: [] for step in steps}
    for edge in edges:
        if edge.source in following and edge.target in following:
            following[edge.source].append(edge.target)
    closing = closing_edges(steps, following)
    reach = {step: 0 for step in steps}
    for _ in steps:
        for source, targets in following.items():
            for target in targets:
                if (source, target) not in closing:
                    reach[target] = max(reach[target], reach[source] + 1)
    return reach


def flow_kinds(diagram: mermaid_extract.Diagram, block_text: str, profile: str,
               lanes: dict[str, str]) -> dict[str, str]:
    """The composer kind each step of a flowchart is drawn as, read from its shape, its lane and its style."""
    steps = [node for node in diagram.nodes if not node.container]
    fills = accent_fills(block_text)
    exits = {node.id: [e for e in diagram.edges if e.source == node.id] for node in steps}
    entries = {node.id: [e for e in diagram.edges if e.target == node.id] for node in steps}
    kinds, open_ends = {}, []
    for node in steps:
        if profile == flowchart.ARCHITECTURE:
            kinds[node.id] = ARCHITECTURE_KINDS.get(lanes.get(node.id, ""), "service")
        elif node.shape in FLOW_SHAPES:
            kinds[node.id] = FLOW_SHAPES[node.shape]
        elif node.shape == "stadium" and not entries[node.id]:
            kinds[node.id] = "start"
        elif node.shape == "stadium" and not exits[node.id]:
            fill = fills.get(node.id)
            if fill:
                kinds[node.id] = "error" if fill in ERROR_FILLS else "success"
            else:
                open_ends.append(node.id)
        elif fills.get(node.id):
            kinds[node.id] = "focus"
        else:
            kinds[node.id] = "screen" if profile == flowchart.USER_FLOW else "step"
    if open_ends:
        # With no end marked as the goal, the end the longest path reaches is the goal and the rest leave the flow.
        reach = longest_reach([node.id for node in steps], diagram.edges)
        goal_marked = any(kind == "success" for kind in kinds.values())
        goal = None if goal_marked else max(open_ends, key=lambda node: reach[node])
        for node in open_ends:
            kinds[node] = "success" if node == goal else "exit"
    return kinds


def flowchart_model(diagram: mermaid_extract.Diagram, block_text: str, profile: str,
                    zones: list[dict]) -> tuple[dict, list[str]]:
    """The MODEL for a user flow, a process or an architecture, with any problem its zones raise."""
    containers = [node for node in diagram.nodes if node.container]
    steps = [node for node in diagram.nodes if not node.container]
    lanes = {node.id: node.parent for node in steps if node.parent}
    problems, zone_of, model_zones, mode = [], {}, [], "stage"
    if containers:
        if zones:
            problems.append("%% zone lines on a diagram with lanes: the lanes are its zones already")
        order = list(flowchart.ARCHITECTURE_COLUMNS) if profile == flowchart.ARCHITECTURE else []
        ordered = sorted(containers, key=lambda lane: order.index(lane.id) if lane.id in order else len(order))
        model_zones = [{"id": lane.id, "label": lane.label or lane.id} for lane in ordered]
        zone_of = lanes
        mode = "stage" if profile == flowchart.ARCHITECTURE else "lane"
    elif zones:
        problems += zone_problems(zones, [node.id for node in steps], every_node=True)
        model_zones = [{"id": zone["id"], "label": zone["label"]} for zone in zones]
        zone_of = {member: zone["id"] for zone in zones for member in zone["members"]}
    kinds = flow_kinds(diagram, block_text, profile, lanes)
    styled = accent_fills(block_text)
    nodes = [{"id": node.id, "label": node.label, "kind": kinds[node.id], "zone": zone_of.get(node.id),
              **({"accent": True} if styled.get(node.id) else {})} for node in steps]
    edges, styles = [], []
    for edge in diagram.edges:
        entry = {"from": edge.source, "to": edge.target, "label": edge.label}
        if edge.style == "dashed":
            entry["style"] = "dashed"
            styles.append("dashedAsync" if profile == flowchart.ARCHITECTURE else "dashedOptional")
        if edge.bidirectional:
            entry["twoWay"] = True
            styles.append("twoWay")
        edges.append(entry)
    model = {"type": "graph", "profile": profile, "direction": "TB" if diagram.direction in ("TD", "TB") else "LR",
             "zoneMode": mode, "zones": model_zones, "nodes": nodes, "edges": edges,
             "edgeStyles": list(dict.fromkeys(styles)),
             "expect": {"nodes": len(nodes), "connectors": len(edges)}}
    return model, problems


def state_model(diagram: mermaid_extract.Diagram, block_text: str) -> tuple[dict, list[str]]:
    """The MODEL for a state diagram, with each composite drawn as the zone around its states."""
    stereotypes = {}
    for _, text in content_lines(block_text):
        match = state.STEREOTYPE.match(text)
        if match:
            stereotypes[match.group(1)] = match.group(2).lower()
    by_id = {node.id: node for node in diagram.nodes}
    zones = [{"id": node.id, "label": node.label or node.id} for node in diagram.nodes if node.container]
    nodes = []
    for node in diagram.nodes:
        if node.container:
            continue
        stereotype = stereotypes.get(node.id)
        if node.shape == "start":
            kind = "initial"
        elif node.shape == "end":
            kind = "final"
        elif stereotype == "choice":
            kind = "choice"
        elif stereotype in ("fork", "join"):
            kind = "fork"
        # Only the machine's own start and end colour a state. A composite's inner entry and exit are drawn
        # inside its zone, and a state that only leaves the composite has not ended the machine.
        elif any(by_id[e.source].shape == "start" and not by_id[e.source].parent and e.target == node.id
                 for e in diagram.edges):
            kind = "firstState"
        elif any(by_id[e.target].shape == "end" and not by_id[e.target].parent and e.source == node.id
                 for e in diagram.edges):
            kind = "finalState"
        else:
            kind = "state"
        nodes.append({"id": node.id, "label": node.label, "kind": kind, "zone": node.parent})
    edges = [{"from": e.source, "to": e.target, "label": e.label} for e in diagram.edges]
    model = {"type": "graph", "profile": "state", "direction": "TB" if diagram.direction in ("TD", "TB") else "LR",
             "zoneMode": "group", "zones": zones, "nodes": nodes, "edges": edges, "edgeStyles": [],
             "expect": {"nodes": len(nodes), "connectors": len(edges)}}
    return model, []


def er_model(block_text: str, zones: list[dict]) -> tuple[dict, list[str]]:
    """The MODEL for an ER diagram, with each entity's fields and each relationship's cardinality in words."""
    entities, fields, relationships, current, direction = {}, {}, [], None, "LR"
    for _, text in content_lines(block_text)[1:]:
        if current is not None:
            if text == "}":
                current = None
                continue
            attribute = er.ATTRIBUTE.match(text)
            if attribute:
                keys = ", ".join(re.findall(r"PK|FK|UK", attribute.group(3) or ""))
                fields[current].append({"type": attribute.group(1), "name": attribute.group(2), "keys": keys})
            continue
        if text.lower().startswith("direction "):
            direction = "TB" if text.split()[1].upper() in ("TB", "TD") else "LR"
            continue
        opened = er.ENTITY_OPEN.match(text)
        if opened:
            current = opened.group(1)
            entities[current] = opened.group(3) or current
            fields[current] = []
            continue
        relationship = er.RELATIONSHIP.match(text)
        if relationship and er.CARDINALITY.match(relationship.group(2)):
            relationships.append(relationship.groups())
            continue
        alone = er.ENTITY_ALONE.match(text)
        if alone:
            entities.setdefault(alone.group(1), alone.group(3) or alone.group(1))
            fields.setdefault(alone.group(1), [])
    edges, styles = [], []
    for left, cardinality, right, label in relationships:
        for end in (left, right):
            entities.setdefault(end, end)
            fields.setdefault(end, [])
        left_end, line, right_end = er.CARDINALITY.match(cardinality).groups()
        words = f"{CARDINALITY_WORDS.get(left_end, '?')} to {CARDINALITY_WORDS.get(right_end, '?')}"
        style = "dashed" if line == ".." else "solid"
        styles.append("nonIdentifying" if style == "dashed" else "identifying")
        edges.append({"from": left, "to": right, "label": f"{(label or '').strip().strip(chr(34))} ({words})",
                      "style": style, "undirected": True})
    problems = zone_problems(zones, list(entities), every_node=False)
    zone_of = {member: zone["id"] for zone in zones for member in zone["members"]}
    nodes = [{"id": entity, "label": alias, "kind": "entity", "fields": fields[entity], "zone": zone_of.get(entity)}
             for entity, alias in entities.items()]
    model = {"type": "graph", "profile": "er", "direction": direction, "zoneMode": "group",
             "zones": [{"id": zone["id"], "label": zone["label"]} for zone in zones], "nodes": nodes,
             "edges": edges, "edgeStyles": list(dict.fromkeys(sorted(styles))),
             "expect": {"nodes": len(nodes), "connectors": len(edges)}}
    return model, problems


def sequence_model(block_text: str) -> tuple[dict, list[str]]:
    """The MODEL for a sequence diagram, with the declared participants first and the rest as they are used."""
    declared, used, messages = [], [], []
    for _, text in content_lines(block_text)[1:]:
        participant = sequence.PARTICIPANT.match(text)
        if participant:
            if participant.group(2) not in declared:
                declared.append(participant.group(2))
            continue
        message = sequence.MESSAGE.match(text)
        if message:
            source, arrow, _, target, label = message.groups()
            for name in (source, target):
                if name not in used:
                    used.append(name)
            messages.append({"from": source, "to": target, "arrow": ARROWS.get(arrow, "request"),
                             "label": (label or "").strip()})
    names = declared + [name for name in used if name not in declared]
    model = {"type": "sequence", "participants": [{"id": name, "label": name} for name in names],
             "messages": messages, "expect": {"nodes": len(names), "connectors": len(messages)}}
    return model, []


def gantt_model(block_text: str) -> tuple[dict, list[str]]:
    """The MODEL for a gantt chart, with each bar placed in days or minutes from the earliest start."""
    date_format, section, tasks, ids = "", None, [], {}
    for number, text in content_lines(block_text)[1:]:
        first = text.split()[0]
        if first == "title":
            continue
        if first == "dateFormat":
            date_format = text[len(first):].strip()
            continue
        if first == "section":
            section = text[len(first):].strip()
            continue
        name, separator, meta = text.partition(":")
        if not separator:
            continue
        task, _ = gantt.parse_task(number, name.strip(), meta, date_format, ids)
        task["section"] = section
        tasks.append(task)
        if task["id"]:
            ids[task["id"]] = task
    spans, previous_end = {}, None
    for task in tasks:
        if task["start"]:
            begin = gantt.parses(task["start"], date_format)
        elif task["after"]:
            begin = max(spans[reference][1] for reference in task["after"])
        else:
            begin = previous_end
        if task["minutes"] is not None:
            finish = begin + timedelta(minutes=task["minutes"])
        else:
            finish = gantt.parses(task["end"], date_format)
        task["span"] = (begin, finish)
        if task["id"]:
            spans[task["id"]] = task["span"]
        previous_end = finish
    origin = min(task["span"][0] for task in tasks)
    unit = SECONDS_PER_DAY if date_format == "YYYY-MM-DD" else SECONDS_PER_MINUTE

    def offset(moment: datetime) -> float:
        return round((moment - origin).total_seconds() / unit, 2)

    sections = []
    for task in tasks:
        label = task["section"] or "Tasks"
        if not sections or sections[-1]["label"] != label:
            sections.append({"label": label, "tasks": []})
        sections[-1]["tasks"].append({"id": task["id"], "name": task["name"], "tags": task["tags"],
                                      "start": offset(task["span"][0]), "end": offset(task["span"][1])})
    model = {"type": "gantt", "unit": "day" if unit == SECONDS_PER_DAY else "minute",
             "origin": origin.strftime("%Y-%m-%d" if unit == SECONDS_PER_DAY else "%H:%M"),
             "span": max(offset(task["span"][1]) for task in tasks), "sections": sections,
             "expect": {"nodes": len(tasks), "connectors": 0}}
    return model, []


def build_model(block: mermaid_extract.SourceBlock, number: int) -> tuple[dict | None, list[str], str]:
    """Check one block, then build its MODEL. Returns the model, its problems and the check's summary."""
    profile, problems, size, _ = flow_check.check_block(block, block.text)
    if problems:
        return None, problems, size
    text, zones = directives(block.text)
    if profile in (flowchart.USER_FLOW, flowchart.PROCESS, flowchart.ARCHITECTURE):
        body = block.text
        if profile == flowchart.ARCHITECTURE:
            body, _ = flowchart.rewrite_backward_edges(block.text)
        diagram = mermaid_extract.parse_block(mermaid_extract.SourceBlock(block.index, body, block.source_line))
        model, found = flowchart_model(diagram, block.text, profile, zones)
    elif profile == "state":
        model, found = state_model(mermaid_extract.parse_block(block), block.text)
    elif profile == "er":
        model, found = er_model(block.text, zones)
    elif profile == "sequence":
        model, found = sequence_model(block.text)
    else:
        model, found = gantt_model(block.text)
    if zones and profile in ("state", "sequence", "gantt", flowchart.ARCHITECTURE):
        found.append(f"%% zone lines on a {flow_check.NAMES[profile]}: this kind draws its own grouping")
    if text.get("focus") or FOCUS_LINE.search(block.text):
        found += focus_problems(model, profile, text.get("focus", ""), len(FOCUS_LINE.findall(block.text)))
    model.update({"title": board_title(block.text, text, number), "subtitle": text.get("subtitle", ""),
                  "source": text.get("source", "")})
    return model, found, size


# ───────────────────────────────────────────────────────────────
# 3. COMPACT CODE
# ───────────────────────────────────────────────────────────────

# A space between two of these and anything else changes nothing in JavaScript, except where two signs
# would fuse into one token, which `squeeze` keeps apart.
LOOSE = set("{}()[],;:=+-*/<>!&|?.%^~")
FUSING = set("+-")


def squeeze(line: str) -> str:
    """One line of the composer with the spaces that carry no meaning taken out.

    Strings and template literals are copied as they stand, so no text the board prints changes. The
    composer has no regular expression literal, which would make `/` ambiguous, and the self-test runs
    every squeezed line, so a rule that broke the code would fail it.
    """
    out, i, n = [], 0, len(line)

    def quoted(start: int) -> int:
        """The index just past the string or template literal that opens at `start`."""
        quote, j = line[start], start + 1
        while j < n and line[j] != quote:
            if line[j] == "\\":
                j += 1
            elif quote == "`" and line.startswith("${", j):
                depth, j = 1, j + 2
                while depth:
                    if line[j] in "'\"`":
                        j = quoted(j) - 1
                    depth += (line[j] == "{") - (line[j] == "}")
                    j += 1
                continue
            j += 1
        return j + 1

    while i < n:
        char = line[i]
        if char in "'\"`":
            end = quoted(i)
            out.append(line[i:end])
            i = end
        elif line.startswith("/*", i):
            i = line.index("*/", i) + 2
        elif char == " ":
            j = i
            while j < n and line[j] == " ":
                j += 1
            before, after = out[-1][-1] if out else "", line[j] if j < n else ""
            loose = before in LOOSE or after in LOOSE or not before or not after
            fused = before in FUSING and after in FUSING
            if not loose or fused or (before == "/" and after in "/*"):
                out.append(" ")
            i = j
        else:
            out.append(char)
            i += 1
    return "".join(out)


def compact_template() -> str:
    """The composer code with its comments, indentation and idle spaces dropped and MODEL and THEME left placeholders."""
    template = TEMPLATE.read_text(encoding="utf-8")
    for placeholder in (PLACEHOLDER, THEME_PLACEHOLDER):
        if template.count(placeholder) != 1:
            raise SystemExit(f"{TEMPLATE} must hold {placeholder} exactly once")
    # The code is pasted into every call, so full-line comments, indentation and the spaces around operators
    # are dropped. None carries meaning in JavaScript, and no string in the composer spans a line.
    lines = [squeeze(line.strip()) for line in template.splitlines()]
    return "\n".join(line for line in lines if line and not line.startswith("//"))


def lean(value: object) -> object:
    """The model without the empty values the composer reads the same as an absent one.

    A blank label, a node in no zone, a field with no key and the default edge style are each a falsy or
    unknown value to the composer, so leaving them out saves code room for the board's own text.
    """
    if isinstance(value, dict):
        return {key: lean(item) for key, item in value.items()
                if item not in ("", None) and not (key == "style" and item == "solid") and not (key == "edgeStyles" and not item)}
    if isinstance(value, list):
        return [lean(item) for item in value]
    return value


def fill_template(model: dict, theme: dict | None = None) -> str:
    """The compact composer code with this model and this theme in place of their placeholders.

    Both are filled in one pass, so a label that happens to read like a placeholder is never filled itself.
    """
    filled = {PLACEHOLDER: board_design.compact(lean(model)), THEME_PLACEHOLDER: board_design.compact(theme or {})}
    return FILLED.sub(lambda match: filled[match.group(0)], compact_template())


# ───────────────────────────────────────────────────────────────
# 4. COMPOSE
# ───────────────────────────────────────────────────────────────

def design_warnings(notes: list[str]) -> str:
    """The count of DESIGN lines, as the COMPOSED line and the design check print it."""
    return f"{len(notes)} design warning{'' if len(notes) == 1 else 's'}"


def compose(path: Path, number: int, out: Path | None, model_only: bool) -> int:
    """Compose one diagram of a model file, write its code or its MODEL and return the exit code."""
    try:
        blocks = mermaid_extract.load_blocks(path)
    except SystemExit:
        print(f"UNREADABLE {path}: the extractor refused it", file=sys.stderr)
        return 2
    if not 1 <= number <= len(blocks):
        print(f"UNREADABLE {path}: no diagram {number}, the file holds {len(blocks)}", file=sys.stderr)
        return 2
    model, problems, size = build_model(blocks[number - 1], number)
    if problems or model is None:
        for problem in problems:
            print(f"  diagram {number}: {problem}", file=sys.stderr)
        print(f"FAILED diagram {number} in {path.name}: fix the model and run flow_check.py again", file=sys.stderr)
        return 1
    design, notes = board_design.resolve()
    sent = board_design.theme(design)
    payload = json.dumps(model, ensure_ascii=False, indent=1) if model_only else fill_template(model, sent)
    if not model_only and len(payload) > MAX_CODE_CHARS:
        cost = f", and the design's THEME takes {len(board_design.compact(sent))} of them" if sent else ""
        print(f"FAILED the code runs to {len(payload)} characters, over the {MAX_CODE_CHARS} one use_figma call takes{cost}",
              file=sys.stderr)
        return 1
    if out:
        out.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    # A design warning is the reply's to report, so each one gets its own line before the summary.
    for note in notes:
        print(f"DESIGN {note}", file=sys.stderr)
    where = f" in {out}" if out else ""
    fell = f", {design_warnings(notes)}" if notes else ""
    print(f"COMPOSED diagram {number}, {size}: {model['expect']['nodes']} nodes and "
          f"{model['expect']['connectors']} connectors to read back, {len(payload)} characters{where}, "
          f"drawn in the design {design['meta']['name']}{fell}", file=sys.stderr)
    return 0


def design_check() -> int:
    """Print the design a board is drawn in, what it changes and what it costs. Exit 1 on any design warning."""
    base = board_design.built_in()
    design, notes = board_design.resolve(base=base)
    sent = board_design.theme(design, base)
    swatch, accent = design["swatch"], design["accent"]
    stroke = swatch[accent["pair"]][1]
    room = MAX_CODE_CHARS - len(fill_template({}, sent)) + len(board_design.compact({}))
    changed = board_design.difference({g: design[g] for g in board_design.EDITABLE},
                                      {g: base[g] for g in board_design.EDITABLE}) or {}
    flat = []

    def walk(value: object, path: tuple) -> None:
        if isinstance(value, dict):
            for key, inner in value.items():
                walk(inner, path + (key,))
        else:
            flat.append(f"{board_design.dotted(path)} {json.dumps(value)} (built in {json.dumps(board_design.get(base, path))})")

    walk(changed, ())
    print(f"DESIGN {board_design.DESIGN_FILE.name}: {design['meta']['name']}")
    print(f"  changes from the built-in design: {'; '.join(flat) if flat else 'none'}")
    for role, kinds in board_design.used_roles(design).items():
        fill, _, text = swatch[design["role"][role]]
        print(f"  {role}: {design['role'][role]}, text {contrast(text, fill):.2f}:1 on its fill, drawn by {', '.join(kinds)}")
    hues = {role: board_design.apart(stroke, swatch[design["role"][role]][1]) for role in board_design.used_roles(design)
            if board_design.hue(swatch[design["role"][role]][1])[1] > board_design.SATURATED}
    nearest = min(hues, key=hues.get)
    print(f"  accent: {accent['pair']}, stroke {contrast(stroke, CANVAS):.2f}:1 on white, {accent['node']} px on a node and "
          f"{accent['message']} px on a message, nearest hue {nearest} at {hues[nearest]:.0f} degrees")
    tints = {t: board_design.apart(stroke, design["tint"][t]) for t in design["zone"]["cycle"]}
    print(f"  zone tints: {', '.join(design['zone']['cycle'])}, nearest the accent {min(tints, key=tints.get)} at "
          f"{min(tints.values()):.0f} degrees")
    size = design["type"]
    print(f"  type: {size['family']}, " + ", ".join(f"{step} {size[step]}" for step in
                                                     ("title", "subtitle", "zone", "node", "label", "field", "small")))
    print(f"THEME {board_design.compact(sent)}")
    print(f"  the theme costs {len(board_design.compact(sent))} characters and leaves {room:,} for the model in one use_figma call")
    for note in notes:
        print(f"DESIGN {note}")
    print(design_warnings(notes))
    return 1 if notes else 0


# ───────────────────────────────────────────────────────────────
# 5. SELF-TEST
# ───────────────────────────────────────────────────────────────

def accent_ids(model: dict) -> set[str]:
    """The node or task ids a model plans the accent on: a focus node, a flagged node or a flagged task."""
    if model["type"] == "gantt":
        return {f"{task['id'] or task['name']}" for section in model["sections"] for task in section["tasks"] if task.get("accent")}
    return {node["id"] for node in model["nodes"] if node.get("accent") or node["kind"] == "focus"}


LINE_ORDER = ("dashedOptional", "dashedAsync", "identifying", "nonIdentifying", "twoWay")
ARROW_ORDER = ("request", "reply", "async", "asyncReply")


def zone_tint_problems(drawn: dict, model: dict, design: dict) -> list[str]:
    """Zones and gantt bands whose tint repeats the hue of a node inside them or the tint of a zone beside them."""
    fills, tints = board_design.colour_names(design)
    labels = [z["label"] for z in model.get("zones", [])] or [s["label"] for s in model.get("sections", [])]
    problems, placed = [], []
    reach = 2 * ZONE_GAP
    for label in labels:
        section = next((n for n in drawn["nodes"] if n["type"] == "SECTION" and n["name"] == label), None)
        if section is None:
            continue
        tint = tints.get(geometry.hex_of(section["fill"]), "")
        hues = {board_design.family(fills.get(geometry.hex_of(n["fill"]), "")) for n in drawn["nodes"]
                if n["parent"] == label and n["name"].startswith("node:")}
        beside = [z for z in placed if z["x"] < section["x"] + section["w"] + reach and section["x"] < z["x"] + z["w"] + reach
                  and z["y"] < section["y"] + section["h"] + reach and section["y"] < z["y"] + z["h"] + reach]
        if not tint:
            problems.append(f"zone {label} is drawn in {geometry.hex_of(section['fill'])}, which is no FigJam tint")
        elif board_design.family(tint) in hues:
            problems.append(f"zone {label} takes the {tint} tint, the hue of a node inside it")
        else:
            problems += [f"zone {label} takes the {tint} tint of {z['name']} beside it" for z in beside if z["tint"] == tint]
        placed.append({**section, "tint": tint})
    return problems


def key_entries(drawn: dict) -> list[str]:
    """The key's entries in reading order, row by row: a sample's kind, a line's or an arrow's name, or the pin."""
    shapes = {n["id"]: n for n in drawn["nodes"]}
    key = next(n for n in drawn["nodes"] if n["type"] == "SECTION" and n["name"] == "Key")
    found = [(n["y"], n["x"], n["name"][4:]) for n in drawn["nodes"]
             if n["parent"] == "Key" and n["name"].startswith("key:") and n["name"].count(":") == 1]
    for c in drawn["connectors"]:
        if c["name"].startswith("key:"):
            start = shapes[c["start"]["endpointNodeId"]]
            found.append((start["y"], start["x"], c["name"][4:]))
    # A row starts 88 px down the key and the next 72 px below it, and every sample sits within 28 px of its row's top.
    row = lambda y: round((y - key["y"] - 102) / 72)  # noqa: E731
    return [name for _, _, name in sorted(found, key=lambda entry: (row(entry[0]), entry[1]))]


def key_problems(drawn: dict, design: dict) -> list[str]:
    """A key out of the order a reader meets the board in, or narrower than the diagram above it."""
    kinds = board_design.key_order(design)

    def place(name: str) -> int:
        if name == "focus":
            return 999
        if name in kinds:
            return kinds.index(name)
        if name in LINE_ORDER:
            return 100 + LINE_ORDER.index(name)
        return 200 + ARROW_ORDER.index(name) if name in ARROW_ORDER else 300

    entries = key_entries(drawn)
    problems = []
    if [place(e) for e in entries] != sorted(place(e) for e in entries):
        problems.append(f"the key reads {', '.join(entries)}, out of the design's order")
    key = next(n for n in drawn["nodes"] if n["type"] == "SECTION" and n["name"] == "Key")
    right = max(n["x"] + n["w"] for n in drawn["nodes"] if n["name"].startswith(("node:", "foot:")))
    if key["x"] + key["w"] < right - 1:
        problems.append(f"the key ends at {key['x'] + key['w']:.0f} and the diagram runs on to {right:.0f}")
    return problems


def title_gap_problems(drawn: dict) -> list[str]:
    """Routes that come within 48 px of the title block or within 40 px of the board's left edge."""
    board = next(n for n in drawn["nodes"] if n["type"] == "SECTION" and n["parent"] == "")
    top = min(n["y"] for n in drawn["nodes"] if n["name"].startswith(("node:", "via:")))
    head = max((n["y"] + n["h"] for n in drawn["nodes"] if n["type"] == "TEXT" and n["parent"] == board["name"]
                and n["y"] < top), default=board["y"])
    points = [point for e in geometry.drawn_edges(drawn) for path in e["paths"] for point in path]
    problems = []
    if points and min(p[1] for p in points) < head + 48:
        problems.append(f"a route climbs to {head + 48 - min(p[1] for p in points):.0f} px inside the gap under the title block")
    if points and min(p[0] for p in points) < board["x"] + 40:
        problems.append(f"a route runs {board['x'] + 40 - min(p[0] for p in points):.0f} px into the board's left margin")
    return problems


def pin_problems(drawn: dict, model: dict) -> list[str]:
    """Step pins that stand away from the lifeline their message leaves."""
    heads = {n["name"][5:]: n for n in drawn["nodes"] if n["name"].startswith("node:")}
    problems = []
    for k, m in enumerate(model["messages"], 1):
        pin = next((n for n in drawn["nodes"] if n["name"] == f"step:{k}"), None)
        head = heads[m["from"]]
        if pin is None or abs(pin["x"] + pin["w"] / 2 - head["x"] - head["w"] / 2) > 40:
            problems.append(f"step {k} stands away from the lifeline of {m['from']}")
    return problems


def drawn_checks(name: str, model: dict, drawn: dict, design: dict) -> list[tuple[str, bool, str]]:
    """What a run of the composer drew, held to the board's geometry rules and to the design it was drawn in."""
    results = []
    warnings = (drawn["result"] or {}).get("warnings", [])
    results.append((f"{name} draws with no error and no warning", drawn["error"] is None and not warnings,
                    drawn["error"] or "; ".join(warnings)))
    if drawn["error"]:
        return results
    keyed = key_problems(drawn, design)
    results.append((f"{name} keys every mark in the design's order, as wide as the diagram", not keyed, "; ".join(keyed)))
    if model["type"] == "sequence":
        wrong = geometry.arrow_heads(drawn, model["messages"])
        results.append((f"{name} ends each message in the arrow its Mermaid form names", not wrong, "; ".join(wrong)))
        marked = geometry.message_accent_problems(drawn, model["messages"])
        results.append((f"{name} draws the accent on the message the model plans and on no other", not marked, "; ".join(marked)))
        pins = pin_problems(drawn, model)
        results.append((f"{name} sets each step number beside the lifeline its message leaves", not pins, "; ".join(pins)))
    else:
        planned = accent_ids(model)
        marked = geometry.accent_problems(drawn, planned)
        what = f"draws the accent on {', '.join(sorted(planned))}, in its own pair, outweighing every other mark" if planned \
            else "draws no accent the model does not plan"
        results.append((f"{name} {what}", not marked, "; ".join(marked)))
        tinted = zone_tint_problems(drawn, model, design)
        results.append((f"{name} tints every zone apart from its members and its neighbour", not tinted, "; ".join(tinted)))
    if model["type"] != "graph":
        return results
    clear = title_gap_problems(drawn)
    results.append((f"{name} keeps every route clear of the title block and the board's margin", not clear, "; ".join(clear)))
    # Stage zones line up unless an edge skips a zone, which then keeps the way over or under it open.
    order = {z["id"]: i for i, z in enumerate(model["zones"])}
    zone_of = {n["id"]: n.get("zone") for n in model["nodes"]}
    skips = any(abs(order[zone_of[e["from"]]] - order[zone_of[e["to"]]]) > 1 for e in model["edges"]
                if zone_of.get(e["from"]) in order and zone_of.get(e["to"]) in order)
    if model["zoneMode"] == "stage" and len(model["zones"]) > 1 and not skips:
        edge = "y" if model["direction"] == "LR" else "x"
        lines = sorted({round(z[edge]) for z in geometry.zone_sections(drawn, [z["label"] for z in model["zones"]])})
        results.append((f"{name} lines its zones up along one {'top' if edge == 'y' else 'left'} edge", len(lines) == 1,
                        f"{len(lines)} edges at {lines}"))
    through = geometry.lines_through_boxes(drawn)
    results.append((f"{name} draws no edge through a box that is not its own", not through, "; ".join(through)))
    shared = geometry.shared_ports(drawn)
    results.append((f"{name} gives every edge its own magnet while one is free", not shared, "; ".join(shared)))
    labels = [z["label"] for z in model["zones"]]
    struck = geometry.lines_through_titles(drawn, labels)
    results.append((f"{name} draws no edge through a zone title", not struck, "; ".join(struck)))
    if model["zoneMode"] != "lane":
        strayed = geometry.lines_through_other_zones(drawn, labels)
        results.append((f"{name} draws no edge through a zone it does not join", not strayed, "; ".join(strayed)))
    along = geometry.lines_along_zones(drawn, labels)
    results.append((f"{name} draws no edge along a zone border", not along, "; ".join(along)))
    printed = geometry.labels_off_titles(drawn, labels)
    results.append((f"{name} prints no edge label on a zone title", not printed, "; ".join(printed)))
    tangled = geometry.labels_clear(drawn)
    results.append((f"{name} keeps every label off a node, another edge and another label", not tangled, "; ".join(tangled)))
    crossing = geometry.crossing_edges(drawn)
    results.append((f"{name} draws no edge across another", not crossing, "; ".join(crossing)))
    lying = geometry.shared_stretches(drawn)
    results.append((f"{name} draws no two edges on one trunk long enough for a label", not lying, "; ".join(lying)))
    doubled = geometry.edges_side_by_side(drawn)
    results.append((f"{name} draws no two edges side by side as a doubled line", not doubled, "; ".join(doubled)))
    if model["zoneMode"] == "group":
        clash = geometry.overlapping_zones(drawn, labels)
        results.append((f"{name} draws its zones apart", not clash, "; ".join(clash)))
    short = geometry.short_cards(drawn)
    results.append((f"{name} gives every card height for its lines", not short, "; ".join(short)))
    if model["zoneMode"] in ("lane", "stage") and model["direction"] == "LR":
        tall = geometry.tall_zones(drawn, labels, model["zoneMode"])
        results.append((f"{name} keeps each zone to its content", not tall, "; ".join(tall)))
    return results


def defect_checks(work: Path, sent: dict, design: dict) -> list[tuple[str, bool, str]]:
    """Each model that once drew a defect is composed again in the active design and measured."""
    results = []
    for name, model in DEFECT_MODELS.items():
        code = fill_template(model, sent)
        results.append((f"{name} fits one use_figma call", len(code) <= MAX_CODE_CHARS, f"{len(code)} characters"))
        drawn = geometry.run_trace(code, work)
        results += drawn_checks(name, model, drawn, design)
        if model["type"] == "gantt":
            critical = [n for n in drawn["nodes"] if n["name"].startswith("node:") and "critical" in n["text"]]
            heavy = [n for n in drawn["nodes"] if n["name"] == "key:crit" and (n.get("weight") or 0) > 2]
            named = [n for n in drawn["nodes"] if n["type"] == "TEXT" and "heavy outline" in n["text"]]
            results.append((f"{name} marks the critical bar in words and a heavy outline, and the key says so",
                            bool(critical) and all((n.get("weight") or 0) > 2 for n in critical) and bool(heavy and named),
                            f"{len(critical)} bars, {len(heavy)} key samples, {len(named)} key labels"))
        if name in NEEDS_STACKING:
            # Stacking is the one recovery for zones that clash, so with it removed the clash must stop the draw.
            code = fill_template(model, sent)
            refused = code.replace("zoneMode:M.zoneMode,stack:true", "zoneMode:M.zoneMode")
            stopped = geometry.run_trace(refused, work) if refused != code else {"error": None, "nodes": [{}]}
            results.append((f"{name} is refused before anything is drawn when its zones clash",
                            (stopped["error"] or "").startswith("nothing was drawn") and not stopped["nodes"],
                            f"error {stopped['error']!r}, {len(stopped['nodes'])} shapes drawn"))
    return results


def design_text(tokens: dict, version: int = board_design.SCHEMA_VERSION, name: str = "Planted") -> str:
    """A design file holding one json block with these tokens, the shape a team writes."""
    data = {"meta": {"name": name, "schemaVersion": version}, **tokens}
    return f"# A planted design\n\n```json\n{json.dumps(data, indent=1)}\n```\n"


def leaf_paths(value: object, path: tuple = ()) -> set[tuple]:
    """Every token path a nested design holds."""
    if isinstance(value, dict):
        return set().union(*(leaf_paths(inner, path + (key,)) for key, inner in value.items())) if value else set()
    return {path}


def design_checks(base: dict, design: dict, notes: list[str], sent: dict) -> list[tuple[str, bool, str]]:
    """The built-in design keeps every floor, the design file reads clean and a bad edit falls back by name."""
    results = []
    missed = board_design.floors(base)
    results.append(("the composer's built-in design keeps every floor: text, accent hue, contrast and weight, kinds apart "
                    "and type bounds", not missed, "; ".join(problem for problem, _ in missed)))
    results.append((f"{board_design.DESIGN_FILE.name} reads as one json block with no token falling back", not notes,
                    "; ".join(notes)))
    data, reason = board_design.read_block(board_design.DESIGN_FILE.read_text(encoding="utf-8")) \
        if board_design.DESIGN_FILE.is_file() else (None, "is missing")
    data = data or {}
    results.append((f"{board_design.DESIGN_FILE.name} lists FigJam's swatches and tints exactly as the composer draws them",
                    all(data.get(group) == base[group] for group in board_design.READ_ONLY), reason))
    shipped = leaf_paths({g: base[g] for g in board_design.EDITABLE})
    named = leaf_paths({g: data.get(g, {}) for g in board_design.EDITABLE})
    results.append((f"{board_design.DESIGN_FILE.name} names every token the composer reads", shipped <= named,
                    ", ".join(sorted(board_design.dotted(p) for p in shipped - named))))
    light = {pair[0].lower(): pair[1].lower() for name, pair in base["swatch"].items() if name.startswith("light")}
    results.append(("the check accepts exactly the composer's light pairs in a style line", light == ACCENT_PAIRS,
                    f"composer {sorted(light)}, check {sorted(ACCENT_PAIRS)}"))
    largest = max(DEFECT_MODELS.values(), key=lambda m: len(board_design.compact(lean(m))))
    code = fill_template(largest, sent)
    results.append(("the active design's theme leaves room for the largest planted model in one use_figma call",
                    len(code) <= MAX_CODE_CHARS, f"{len(code)} characters"))
    broken = [
        ("a design file with no json block", "# A design\n", "holds 0 json blocks", None),
        ("a design file with two json blocks", design_text({}) + design_text({}), "holds 2 json blocks", None),
        ("a json block that does not parse", "```json\n{\"meta\": \n```\n", "does not parse", None),
        ("a design for another schema version", design_text({}, 2), "schemaVersion 2", None),
        ("a group the composer does not read", design_text({"colours": {}}), "colours is no group", None),
        ("a token the composer does not read", design_text({"role": {"hero": "lightBlue"}}), "role.hero is no token", None),
        ("a role that names no swatch", design_text({"role": {"goal": "neonGreen"}}), "names 'neonGreen'", ("role", "goal")),
        ("a size written as text", design_text({"type": {"node": "20"}}), "type.node should be int", ("type", "node")),
        ("pink back in the tint cycle", design_text({"zone": {"cycle": ["blue", "orange", "pink"]}}), "pink zone tint sits",
         ("zone", "cycle")),
        ("a goal drawn in the exit's pair", design_text({"role": {"goal": "lightOrange"}}), "success and exit draw one shape",
         ("role", "goal")),
        ("a role drawn in the accent's pair", design_text({"role": {"goal": "lightPink"}}), "the accent's own pair",
         ("role", "goal")),
        ("an accent outline no heavier than an end state's ring", design_text({"accent": {"node": 6}}), "outweigh the 6 px ring",
         ("accent", "node")),
        ("small type under 14 px", design_text({"type": {"small": 10}}), "small type is under 14 px", ("type", "small")),
        ("an edited FigJam swatch", design_text({"swatch": {**base["swatch"], "white": ["#FFFFFF", "#000000", "#1E1E1E"]}}),
         "never changes", None),
        ("a tint cycle holding a list", design_text({"zone": {"cycle": [["blue"], "orange"]}}), "no FigJam section tints",
         ("zone", "cycle")),
        ("async messages drawn white", design_text({"line": {"async": "#FFFFFF"}}), "line.async measures 1.00:1",
         ("line", "async")),
        ("a key on the accent's hue", design_text({"key": {"tint": "pink"}}), "key's pink tint sits", ("key", "tint")),
        ("edge labels larger than node type", design_text({"type": {"label": 40}}), "larger than node type",
         ("type", "label")),
        ("a start dot drawn white", design_text({"role": {"pseudo": "white"}}), "initial dot draws", ("role", "pseudo")),
        ("a design name past 40 characters", design_text({}, name="x" * 41), "named unnamed", None),
        ("zone names over 24 px", design_text({"type": {"zone": 28}}), "over 24 px", ("type", "zone")),
        ("the key's tint in the zone cycle", design_text({"zone": {"cycle": ["blue", "gray"]}}), "the key's own tint",
         ("zone", "cycle")),
        ("a key title holding a lone surrogate", design_text({"key": {"title": "Key \ud800"}}), "not text", ("key", "title")),
    ]
    for name, text, message, path in broken:
        drawn_in, warned = board_design.resolve(text, base)
        kept = path is None or board_design.get(drawn_in, path) == board_design.get(base, path)
        results.append((f"{name} falls back with a warning that says '{message}'",
                        any(message in w for w in warned) and kept and not board_design.floors(drawn_in), "; ".join(warned)))
    every = board_design.resolve(design_text({"role": {role: "lightPink" for role in base["role"]}}), base)
    results.append(("every role on the accent's pair falls back, one warning each, until every floor holds",
                    not board_design.floors(every[0]) and not board_design.theme(every[0], base)
                    and len(every[1]) == len(base["role"]), f"{len(every[1])} warnings, theme {board_design.theme(every[0], base)}"))
    pair = board_design.resolve(design_text({"accent": {"message": 3}, "line": {"weight": 3}}), base)[0]
    results.append(("two edits that miss one floor together keep the one that can stand",
                    pair["accent"]["message"] == base["accent"]["message"] and pair["line"]["weight"] == 3,
                    f"accent.message {pair['accent']['message']}, line.weight {pair['line']['weight']}"))
    later = board_design.resolve(design_text({"accent": {"message": 3}, "line": {"weight": 4}}), base)
    results.append(("a token reverted before another can stand once that one is back",
                    later[0]["accent"]["message"] == 3 and later[0]["line"]["weight"] == base["line"]["weight"]
                    and len(later[1]) == 1, f"accent.message {later[0]['accent']['message']}, line.weight "
                    f"{later[0]['line']['weight']}, {'; '.join(later[1])}"))
    shipped_text = board_design.DESIGN_FILE.read_text(encoding="utf-8") if board_design.DESIGN_FILE.is_file() else ""
    windows = board_design.resolve(shipped_text.replace("\n", "\r\n"), base)[1]
    results.append((f"{board_design.DESIGN_FILE.name} saved with Windows line endings reads clean", not windows, "; ".join(windows)))
    unread = board_design.resolve(b"not text", base)
    results.append(("a design the reader cannot handle still draws the built-in design, with a warning",
                    not board_design.theme(unread[0], base) and any("could not be read" in w for w in unread[1]),
                    "; ".join(unread[1])))
    if PROJECT_DESIGN.is_file():
        mirror = PROJECT_DESIGN.read_text(encoding="utf-8")
        line = PROJECT_THEME.search(mirror)
        results.append((f"{PROJECT_DESIGN.name} gives the THEME line the design check prints",
                        bool(line) and line.group(1) == board_design.compact(sent),
                        f"carries {line.group(1) if line else 'no THEME line'}, the check prints {board_design.compact(sent)}"))
        results.append((f"{PROJECT_DESIGN.name} carries the json block of {board_design.DESIGN_FILE.name}",
                        board_design.FENCE.findall(mirror) == board_design.FENCE.findall(shipped_text),
                        "copy the skill's json block into it"))
    return results


def restyle_checks(work: Path, base: dict) -> list[tuple[str, bool, str]]:
    """A design that changes a role, the key's title, the tint cycle and the label size draws every change it makes."""
    tokens = {"role": {"goal": "lightTeal"}, "key": {"title": "Legend"}, "zone": {"cycle": ["green", "yellow", "teal"]},
              "type": {"label": 16}}
    design, warned = board_design.resolve(design_text(tokens), base)
    sent = board_design.theme(design, base)
    results = [("a restyle reads with no token falling back and sends only its own tokens and its id",
                not warned and set(sent) == {*tokens, "id"}, f"{'; '.join(warned)} sent {sorted(sent)}")]
    model = next(m for m in DEFECT_MODELS.values() if m["type"] == "graph" and any(n["kind"] == "success" for n in m["nodes"])
                 and m.get("zones"))
    drawn = geometry.run_trace(fill_template(model, sent), work)
    goal = [n for n in drawn["nodes"] if n["name"].startswith("node:") and n["fill"]
            and geometry.hex_of(n["fill"]) == base["swatch"]["lightTeal"][0].lower()]
    titled = any(n["type"] == "TEXT" and n["parent"] == "Key" and n["text"] == "Legend" for n in drawn["nodes"])
    _, tints = board_design.colour_names(design)
    zoned = {tints.get(geometry.hex_of(n["fill"])) for n in geometry.zone_sections(drawn, [z["label"] for z in model["zones"]])}
    results.append(("a restyled board draws its goal in the new role's pair, titles its key Legend and tints from the new cycle",
                    drawn["error"] is None and bool(goal) and titled and zoned <= {"green", "yellow", "teal"},
                    f"{drawn['error'] or ''} {len(goal)} goal shapes, key title {titled}, tints {sorted(map(str, zoned))}"))
    return results


def extreme_checks(work: Path, base: dict, design: dict) -> list[tuple[str, bool, str]]:
    """The planted models draw clean at the largest and the smallest sizes the floors allow, and a zone the tint
    cycle cannot fit repeats a cycle tint with a warning, never the key's gray."""
    results = []
    for name, sizes in (("largest", {"node": 24, "zone": 24, "label": 24, "field": 24, "small": 24, "subtitle": 128, "title": 128}),
                        ("smallest", {"node": 16, "zone": 16, "label": 14, "field": 14, "small": 14, "subtitle": 16, "title": 32})):
        tried, warned = board_design.resolve(design_text({"type": sizes}), base)
        geometry.use_design(tried)
        failed = []
        for label, model in DEFECT_MODELS.items():
            drawn = geometry.run_trace(fill_template(model, board_design.theme(tried, base)), work)
            failed += [check for check, ok, _ in drawn_checks(label, model, drawn, tried) if not ok]
        results.append((f"the planted models draw clean at the {name} type sizes the floors allow", not warned and not failed,
                        "; ".join(warned + failed[:3])))
    geometry.use_design(design)
    model = copy.deepcopy(next(m for m in DEFECT_MODELS.values() if m["type"] == "graph" and m.get("zones")))
    zone = model["zones"][0]
    members = [n for n in model["nodes"] if n.get("zone") == zone["id"]]
    for node, kind in zip(members, ("start", "exit")):
        node["kind"] = kind
    drawn = geometry.run_trace(fill_template(model, {"zone": {"cycle": ["blue", "orange"]}, "id": "Planted 0"}), work)
    section = next((n for n in drawn["nodes"] if n["type"] == "SECTION" and n["name"] == zone["label"]), None)
    fill = geometry.hex_of(section["fill"]) if section else ""
    said = any(w.startswith(f"zone {zone['label']} repeats") for w in (drawn["result"] or {}).get("warnings", []))
    results.append(("a zone the tint cycle cannot fit repeats a cycle tint with a warning, never the key's gray",
                    fill in {base["tint"]["blue"].lower(), base["tint"]["orange"].lower()} and said,
                    f"{drawn['error'] or ''} drawn in {fill}, warned {said}"))
    return results


def font_checks(work: Path) -> list[tuple[str, bool, str]]:
    """A family that will not load sets the board in Inter with a warning, and one that names its third weight SemiBold
    keeps its own face."""
    model = next(m for m in DEFECT_MODELS.values() if m["type"] == "graph")
    results = []
    for family, face, warns in (("Missing", "Inter", True), ("Semi", "Semi", False)):
        drawn = geometry.run_trace(fill_template(model, {"type": {"family": family}, "id": "Planted 0"}), work)
        fonts = {(n["font"]["family"], n["font"]["style"]) for n in drawn["nodes"] if n.get("font")}
        said = any(f"the font {family} did not load" in w for w in (drawn["result"] or {}).get("warnings", []))
        styles = {style for _, style in fonts}
        kept = {f for f, _ in fonts} == {face} and ("SemiBold" in styles if face == "Semi" else "Semi Bold" in styles)
        results.append((f"a board in the {family} family is set in {face}" + (" and says why" if warns else " with no warning"),
                        drawn["error"] is None and kept and said == warns,
                        f"{drawn['error'] or ''} fonts {sorted(fonts)}, warned {said}"))
    return results


def focus_checks(work: Path, sent: dict) -> list[tuple[str, bool, str]]:
    """A `%% focus:` line marks one thing on each diagram that takes no style line, and is refused where it names nothing."""
    from figjam_checks.fixtures import GOOD

    marked = {"an architecture": "orders", "a sequence": "2", "a state machine": "Pending", "an ER model": "Booking",
              "a gantt chart": "beta"}
    refused = [("an architecture", "%% focus: ghost", "names nothing"),
               ("a sequence", "%% focus: 9", "names nothing"),
               ("an architecture", "%% focus: orders\n%% focus: db", "at most 1"),
               ("a user flow with one accent", "%% focus: pick", "mark the first glance with a style line")]
    results = []
    for kind, target in marked.items():
        model, problems, _ = build_model(mermaid_extract.SourceBlock(1, f"{GOOD[kind]}\n%% focus: {target}\n", 1), 1)
        drawn = geometry.run_trace(fill_template(model, sent), work) if model else None
        found = [] if not drawn else (geometry.message_accent_problems(drawn, model["messages"]) if model["type"] == "sequence"
                                      else geometry.accent_problems(drawn, {target}))
        results.append((f"%% focus: {target} marks the first glance of {kind}", model is not None and not problems and not found,
                        "; ".join(problems + found)))
    for kind, lines, message in refused:
        _, problems, _ = build_model(mermaid_extract.SourceBlock(1, f"{GOOD[kind]}\n{lines}\n", 1), 1)
        results.append((f"{lines.splitlines()[0]} on {kind} is refused with '{message}'", any(message in p for p in problems),
                        "; ".join(problems)))
    return results


def lifeline_crossings(messages: list[dict], order: list[str]) -> int:
    """How many lifelines the messages cross in total when the participants stand in this order."""
    place = {name: i for i, name in enumerate(order)}
    return sum(max(0, abs(place[m["from"]] - place[m["to"]]) - 1) for m in messages)


def fewest_crossings(messages: list[dict], order: list[str]) -> int:
    """The least any order of the same participants could cross, found by trying every order up to seven."""
    if len(order) > 7:
        return lifeline_crossings(messages, order)
    return min(lifeline_crossings(messages, list(perm)) for perm in itertools.permutations(order))


def sequence_order_checks() -> list[tuple[str, bool, str]]:
    """A message that crosses a lifeline is inherent when no order of the participants avoids it.

    The board keeps the participants in the order the model declares them, because a reader takes the
    leftmost as the one that starts. So the declared order must cost no more crossings than any other, and
    a hub that talks to three others crosses one lifeline whichever way it is ordered.
    """
    results = []
    for name, model in DEFECT_MODELS.items():
        if model["type"] != "sequence":
            continue
        order = [p["id"] for p in model["participants"]]
        drawn, fewest = lifeline_crossings(model["messages"], order), fewest_crossings(model["messages"], order)
        results.append((f"{name} crosses {drawn} lifeline(s), as few as any order of its participants", drawn == fewest,
                        f"{drawn} against {fewest} in the best order"))
    loose = [{"from": "A", "to": "B"}, {"from": "B", "to": "C"}]
    results.append(("an order that crosses a lifeline an order could avoid is measured as worse",
                    lifeline_crossings(loose, ["A", "C", "B"]) > fewest_crossings(loose, ["A", "C", "B"]), ""))
    return results


def planted_board(zone: tuple[float, float, float, float] | None, edges: list[dict]) -> dict:
    """A hand-built trace: one node, an optional zone, and straight edges given as point lists.

    Each edge is `{"name", "pts"}`, drawn as legs through anchors, and may name the node magnets it leaves from
    and arrives at with `"from"` and `"to"`. The shapes are what the checks read, so a planted line can sit
    exactly where a defect would put it.
    """
    node = {"id": "n1", "name": "node:a", "type": "SHAPE_WITH_TEXT", "shape": "ROUNDED_RECTANGLE", "x": 0, "y": 0,
            "w": 224, "h": 96, "text": "", "parent": "Zone"}
    nodes = [node]
    if zone:
        nodes.append({"id": "z1", "name": "Zone", "type": "SECTION", "x": zone[0], "y": zone[1], "w": zone[2],
                      "h": zone[3], "text": "", "parent": ""})
    connectors = []
    for k, edge in enumerate(edges):
        pts, anchors = edge["pts"], []
        for i, (x, y) in enumerate(pts):
            anchors.append({"id": f"p{k}-{i}", "name": f"via:{k}:{i}", "type": "SHAPE_WITH_TEXT", "shape": "ELLIPSE",
                            "x": x - 8, "y": y - 8, "w": 16, "h": 16, "text": "", "parent": ""})
        nodes += anchors
        for i in range(len(pts) - 1):
            last = i == len(pts) - 2
            start = ({"endpointNodeId": "n1", "magnet": edge["from"]} if i == 0 and edge.get("from")
                     else {"endpointNodeId": anchors[i]["id"], "position": {"x": 8, "y": 8}})
            end = ({"endpointNodeId": "n1", "magnet": edge["to"]} if last and edge.get("to")
                   else {"endpointNodeId": anchors[i + 1]["id"], "position": {"x": 8, "y": 8}})
            connectors.append({"name": f"edge:{edge['name']}" if last else f"leg:{edge['name']}:{i + 1}", "start": start,
                               "end": end, "label": edge.get("label", "") if i == 0 else "", "line": "STRAIGHT",
                               "startCap": "NONE", "endCap": "NONE", "dash": [], "stroke": [], "weight": 2})
    return {"result": {}, "error": None, "nodes": nodes, "connectors": connectors}


def fan_in_checks(work: Path, sent: dict) -> list[tuple[str, bool, str]]:
    """Four sockets on a gateway of four magnets: the last one merges into an arrival instead of looping to a free magnet."""
    name = "an architecture with four clients on one gateway"
    drawn = geometry.run_trace(fill_template(DEFECT_MODELS[name], sent), work)
    into = [e for e in geometry.drawn_edges(drawn) if e["name"].endswith("->api")]
    long = [p for p in geometry.long_detours(drawn) if "->api" in p]
    merged = any({x for x in e["ports"] if x[2] == "in"} & {x for x in o["ports"] if x[2] == "in"}
                 for e in into for o in into if e is not o)
    return [(f"{name} runs every edge into the gateway within twice the gap between its boxes", len(into) == 4 and not long,
             "; ".join(long)),
            (f"{name} lets two sockets arrive at one magnet of the gateway", merged, "")]


def checker_checks() -> list[tuple[str, bool, str]]:
    """Each measure flags a line planted where its defect would put it, and passes one planted a little clear of it."""
    zone = (0, 0, 400, 300)
    along = lambda pts: geometry.lines_along_zones(planted_board(zone, [{"name": "e", "pts": pts}]), ["Zone"])
    trunk = lambda gap: geometry.shared_stretches(planted_board(None, [
        {"name": "x", "pts": [(0, 100), (200, 100)]}, {"name": "y", "pts": [(0, 100 + gap), (200, 100 + gap)]}]))
    ports = lambda first, second: geometry.shared_ports(planted_board(None, [
        {"name": "x", "pts": [(112, 96), (112, 150)], "from": first}, {"name": "y", "pts": [(112, 96), (300, 96)], "from": second}]))
    arrive = lambda a, b: geometry.shared_ports(planted_board(None, [
        {"name": "x", "pts": [(112, 300), (112, 96)], "to": a}, {"name": "y", "pts": [(112, 400), (112, 96)], "to": b}]))
    merge = lambda run: geometry.shared_stretches(planted_board(None, [
        {"name": "x", "pts": [(-run, 48), (0, 48)], "to": "LEFT"}, {"name": "y", "pts": [(-run, 48), (0, 48)], "to": "LEFT"}]))
    parallel = lambda gap: geometry.edges_side_by_side(planted_board(None, [
        {"name": "x", "pts": [(0, 100), (200, 100)]}, {"name": "y", "pts": [(0, 100 + gap), (200, 100 + gap)]}]))
    air = lambda gap: geometry.labels_clear(planted_board(None, [
        {"name": "x", "pts": [(0, 200), (300, 200)], "label": "reserves"},
        {"name": "y", "pts": [(150, 200 + gap), (150, 360)]}]))
    return [
        ("a run on a zone's bottom border is along it", bool(along([(40, 300), (200, 300)])), ""),
        ("a run 10 px outside a zone's border is along it", bool(along([(40, 310), (200, 310)])), ""),
        ("a run 24 px outside a zone's border, in the gap between zones, is clear", not along([(40, 324), (200, 324)]), ""),
        ("a run 30 px inside a zone's border is along it", bool(along([(40, 270), (200, 270)])), ""),
        ("a run 48 px inside a zone's border is clear", not along([(40, 252), (200, 252)]), ""),
        ("a run that crosses a zone's border at a right angle is clear", not along([(200, 150), (200, 400)]), ""),
        ("two runs 4 px apart for 200 px read as one trunk", bool(trunk(4)), ""),
        ("two runs 16 px apart are two lines", not trunk(16), ""),
        ("two edges leaving one magnet while three are free are flagged", bool(ports("RIGHT", "RIGHT")), ""),
        ("two edges leaving two magnets are clear", not ports("BOTTOM", "RIGHT"), ""),
        ("two edges that only arrive may share a magnet", not arrive("TOP", "TOP"), ""),
        ("two edges arriving at one magnet may merge along 150 px", not merge(150), ""),
        ("two edges arriving at one magnet may not run together for 250 px", bool(merge(250)), ""),
        ("two runs 34 px apart for 200 px read as a doubled line", bool(parallel(34)), ""),
        ("two runs 80 px apart are two lines", not parallel(80), ""),
        ("another edge's line 4 px from a label is a label at a junction", bool(air(16)), ""),
        ("another edge's line 20 px from a label is clear", not air(32), ""),
    ]


def self_test() -> int:
    """Prove every shipped model composes and draws true, and print one line per check."""
    results = []
    template = TEMPLATE.read_text(encoding="utf-8") if TEMPLATE.is_file() else ""
    for placeholder in (PLACEHOLDER, THEME_PLACEHOLDER):
        results.append((f"{TEMPLATE.name} holds {placeholder} once", template.count(placeholder) == 1, ""))
    # Every board below is drawn in the active design, so a restyle is proved on the same boards as the default.
    base = board_design.built_in()
    design, notes = board_design.resolve(base=base)
    sent = board_design.theme(design, base)
    geometry.use_design(design)
    models = [m for m in sorted((PACKET / "assets").rglob("*.md")) if "```mermaid" in m.read_text(encoding="utf-8")]
    node = shutil.which("node")
    for path in models:
        for number, block in enumerate(mermaid_extract.load_blocks(path), 1):
            with contextlib.redirect_stdout(io.StringIO()):
                model, problems, size = build_model(block, number)
            name = f"{path.relative_to(PACKET)} diagram {number}"
            if model is None:
                # A block kept to show a failing draft is the check's business, not the composer's.
                continue
            results.append((f"{name} composes", not problems, "; ".join(problems)))
            counted = re.findall(r"(\d+) (?:nodes|states|entities|participants|tasks)", size)
            wanted = int(counted[0]) if counted else None
            drawn = model["expect"]["nodes"]
            if model.get("profile") == "state":
                # The check counts a composite as a state, and the board draws it as the zone around its states.
                drawn = sum(1 for n in model["nodes"] if n["kind"] not in ("initial", "final")) + len(model["zones"])
            results.append((f"{name} draws the {wanted} the check counted", wanted == drawn, f"draws {drawn}"))
            code = fill_template(model, sent)
            results.append((f"{name} fits one use_figma call", len(code) <= MAX_CODE_CHARS, f"{len(code)} characters"))
            if node:
                with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False, encoding="utf-8") as handle:
                    handle.write("export async function run(figma) {\n" + code + "\n}\n")
                checked = subprocess.run([node, "--check", handle.name], capture_output=True, text=True)
                Path(handle.name).unlink()
                results.append((f"{name} is valid JavaScript", checked.returncode == 0, checked.stderr.strip()))
                with tempfile.TemporaryDirectory() as work:
                    results += drawn_checks(name, model, geometry.run_trace(code, Path(work)), design)
    planted = {
        "a zone naming a missing node": ("flowchart LR\n    %% zone: One: a, ghost\n    a([Start]) --> b([End])\n    style b fill:#CDF4D3\n",
                                         "ghost, which is no node"),
        "a node in two zones": ("flowchart LR\n    %% zone: One: a, b\n    %% zone: Two: b\n    a([Start]) --> b([End])\n    style b fill:#CDF4D3\n",
                                "one zone each"),
        "a node left out of the zones": ("flowchart LR\n    %% zone: One: a\n    a([Start]) --> b([End])\n    style b fill:#CDF4D3\n",
                                         "sit in no zone"),
    }
    for name, (text, message) in planted.items():
        block = mermaid_extract.SourceBlock(1, text, 1)
        _, problems, _ = build_model(block, 1)
        results.append((f"{name} is refused with '{message}'", any(message in p for p in problems), "; ".join(problems)))
    results += checker_checks()
    results += sequence_order_checks()
    results += design_checks(base, design, notes, sent)
    if node:
        with tempfile.TemporaryDirectory() as work:
            results += defect_checks(Path(work), sent, design)
            results += focus_checks(Path(work), sent)
            results += fan_in_checks(Path(work), sent)
            results += restyle_checks(Path(work), base)
            results += font_checks(Path(work))
            results += extreme_checks(Path(work), base, design)
    if PROJECT_COPY.is_file():
        block = PROJECT_FENCE.search(PROJECT_COPY.read_text(encoding="utf-8"))
        results.append((f"{PROJECT_COPY.name} carries the current compact code",
                        bool(block) and block.group(1) == compact_template(),
                        "rebuild its code block from compose_board.py --template"))
    if not node:
        print("SKIP  node is not on PATH, so the filled code was not syntax-checked")
    for name, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok and detail:
            print(f"      {detail}")
    passed = sum(1 for _, ok, _ in results if ok)
    print(f"{passed} of {len(results)} self-test checks passed")
    return 0 if passed == len(results) else 1


# ───────────────────────────────────────────────────────────────
# 6. COMMAND LINE
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Dispatch the command line and return the exit code the usage lines document."""
    args = sys.argv[1:]
    if args == ["--self-test"]:
        return self_test()
    if args == ["--template"]:
        print(compact_template())
        return 0
    if args == ["--design-check"]:
        return design_check()
    if not args or args[0].startswith("--"):
        print(__doc__.strip().split("Usage:")[1], file=sys.stderr)
        return 2
    path, number, out, model_only = Path(args[0]), 1, None, False
    rest = args[1:]
    while rest:
        flag = rest.pop(0)
        if flag == "--diagram" and rest:
            number = int(rest.pop(0))
        elif flag == "--out" and rest:
            out = Path(rest.pop(0))
        elif flag == "--model":
            model_only = True
        else:
            print(__doc__.strip().split("Usage:")[1], file=sys.stderr)
            return 2
    return compose(path, number, out, model_only)


if __name__ == "__main__":
    sys.exit(main())

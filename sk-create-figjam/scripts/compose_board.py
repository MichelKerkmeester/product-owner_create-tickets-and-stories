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

Usage:
  compose_board.py <model.md> [--diagram N] [--out path]  -> 0 the filled code is written, 1 the model fails
                                                             the check, 2 unreadable or no such diagram
  compose_board.py <model.md> --model                      -> print the MODEL as JSON instead of the code
  compose_board.py --template                              -> print the compact code with its MODEL placeholder, the
                                                             text the Project's composer Knowledge file carries
  compose_board.py --self-test                             -> prove every shipped model composes, its counts
                                                             match the check, the code fits one use_figma call and
                                                             the board it draws keeps its geometry
"""
from __future__ import annotations

import colorsys
import contextlib
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
from figjam_checks import er, flowchart, gantt, sequence, state  # noqa: E402
from figjam_checks.board_fixtures import MODELS as DEFECT_MODELS, NEEDS_STACKING  # noqa: E402
from figjam_checks.common import CANVAS, content_lines, contrast, statements  # noqa: E402
from figjam_checks.layout import closing_edges  # noqa: E402

PACKET = HERE.parent
TEMPLATE = PACKET / "assets" / "compose-board.js"
# The claude.ai Project has no Python, so its agent fills MODEL by hand from a copy of the compact code.
PROJECT_COPY = PACKET.parent / "claude project" / "knowledge" / "Product Owner - Assets - Flow Board Composer.md"
PROJECT_FENCE = re.compile(r"```javascript\n(.*?)\n```", re.S)
PLACEHOLDER = "__MODEL__"
# use_figma takes at most 50,000 characters of code, and the model rides inside it.
MAX_CODE_CHARS = 50_000
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
    """The composer code with its comments, indentation and idle spaces dropped and MODEL left a placeholder."""
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count(PLACEHOLDER) != 1:
        raise SystemExit(f"{TEMPLATE} must hold {PLACEHOLDER} exactly once")
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


def fill_template(model: dict) -> str:
    """The compact composer code with this model in place of its placeholder."""
    return compact_template().replace(PLACEHOLDER, json.dumps(lean(model), ensure_ascii=False, separators=(",", ":")))


# ───────────────────────────────────────────────────────────────
# 4. COMPOSE
# ───────────────────────────────────────────────────────────────

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
    payload = json.dumps(model, ensure_ascii=False, indent=1) if model_only else fill_template(model)
    if not model_only and len(payload) > MAX_CODE_CHARS:
        print(f"FAILED the code runs to {len(payload)} characters, over the {MAX_CODE_CHARS} one use_figma call takes",
              file=sys.stderr)
        return 1
    if out:
        out.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    where = f" in {out}" if out else ""
    print(f"COMPOSED diagram {number}, {size}: {model['expect']['nodes']} nodes and "
          f"{model['expect']['connectors']} connectors to read back, {len(payload)} characters{where}", file=sys.stderr)
    return 0


# ───────────────────────────────────────────────────────────────
# 5. SELF-TEST
# ───────────────────────────────────────────────────────────────

def accent_ids(model: dict) -> set[str]:
    """The node or task ids a model plans the accent on: a focus node, a flagged node or a flagged task."""
    if model["type"] == "gantt":
        return {f"{task['id'] or task['name']}" for section in model["sections"] for task in section["tasks"] if task.get("accent")}
    return {node["id"] for node in model["nodes"] if node.get("accent") or node["kind"] == "focus"}


def drawn_checks(name: str, model: dict, drawn: dict) -> list[tuple[str, bool, str]]:
    """What a run of the composer drew, held to the board's geometry rules."""
    results = []
    warnings = (drawn["result"] or {}).get("warnings", [])
    results.append((f"{name} draws with no error and no warning", drawn["error"] is None and not warnings,
                    drawn["error"] or "; ".join(warnings)))
    if drawn["error"]:
        return results
    if model["type"] == "sequence":
        wrong = geometry.arrow_heads(drawn, model["messages"])
        results.append((f"{name} ends each message in the arrow its Mermaid form names", not wrong, "; ".join(wrong)))
        marked = geometry.message_accent_problems(drawn, model["messages"])
        results.append((f"{name} draws the accent on the message the model plans and on no other", not marked, "; ".join(marked)))
    else:
        planned = accent_ids(model)
        marked = geometry.accent_problems(drawn, planned)
        what = f"draws the accent on {', '.join(sorted(planned))}, in pink, outweighing every other mark" if planned \
            else "draws no accent the model does not plan"
        results.append((f"{name} {what}", not marked, "; ".join(marked)))
    if model["type"] != "graph":
        return results
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


def defect_checks(work: Path) -> list[tuple[str, bool, str]]:
    """Each model that once drew a defect is composed again and measured."""
    results = []
    for name, model in DEFECT_MODELS.items():
        code = fill_template(model)
        results.append((f"{name} fits one use_figma call", len(code) <= MAX_CODE_CHARS, f"{len(code)} characters"))
        drawn = geometry.run_trace(code, work)
        results += drawn_checks(name, model, drawn)
        if model["type"] == "gantt":
            critical = [n for n in drawn["nodes"] if n["name"].startswith("node:") and "critical" in n["text"]]
            heavy = [n for n in drawn["nodes"] if n["name"] == "key:crit" and (n.get("weight") or 0) > 2]
            named = [n for n in drawn["nodes"] if n["type"] == "TEXT" and "heavy outline" in n["text"]]
            results.append((f"{name} marks the critical bar in words and a heavy outline, and the key says so",
                            bool(critical) and all((n.get("weight") or 0) > 2 for n in critical) and bool(heavy and named),
                            f"{len(critical)} bars, {len(heavy)} key samples, {len(named)} key labels"))
        if name in NEEDS_STACKING:
            # Stacking is the one recovery for zones that clash, so with it removed the clash must stop the draw.
            code = fill_template(model)
            refused = code.replace("zoneMode:M.zoneMode,stack:true", "zoneMode:M.zoneMode")
            stopped = geometry.run_trace(refused, work) if refused != code else {"error": None, "nodes": [{}]}
            results.append((f"{name} is refused before anything is drawn when its zones clash",
                            (stopped["error"] or "").startswith("nothing was drawn") and not stopped["nodes"],
                            f"error {stopped['error']!r}, {len(stopped['nodes'])} shapes drawn"))
    return results


SHAPE_PAIR = re.compile(r"^\s+(\w+): \{ fill: h\(0x(\w\w), 0x(\w\w), 0x(\w\w)\), stroke: h\(0x(\w\w), 0x(\w\w), 0x(\w\w)\)", re.M)
KIND_PAIR = re.compile(r"^\s+(\w+): \{ shape: '\w+', color: '(\w+)'", re.M)
MIN_HUE_APART = 45


def hue_of(hex_colour: str) -> tuple[float, float]:
    """A colour's hue in degrees and its saturation."""
    red, green, blue = (int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5))
    hue, _, saturation = colorsys.rgb_to_hls(red, green, blue)
    return hue * 360, saturation


def accent_palette_checks(template: str) -> list[tuple[str, bool, str]]:
    """The accent's pink belongs to the accent alone, sits well away from every kind's hue and passes the mark gate."""
    strokes = {name: "#" + "".join(parts[3:]) for name, *parts in SHAPE_PAIR.findall(template)}
    users = [kind for kind, pair in KIND_PAIR.findall(template) if pair == "lightPink"]
    others = {kind: strokes[pair] for kind, pair in KIND_PAIR.findall(template) if pair in strokes and pair != "lightPink"}
    pink = strokes.get("lightPink", "#000000")
    apart = {kind: min(abs(hue_of(pink)[0] - hue_of(stroke)[0]) % 360, 360 - abs(hue_of(pink)[0] - hue_of(stroke)[0]) % 360)
             for kind, stroke in others.items() if hue_of(stroke)[1] > 0.2}
    closest = min(apart, key=apart.get) if apart else ""
    return [
        ("the accent pink is drawn by the focus kind and by no other kind", users == ["focus"], f"drawn by {users}"),
        (f"the accent pink sits {MIN_HUE_APART} degrees or more from the hue of every kind",
         bool(apart) and apart[closest] >= MIN_HUE_APART, f"{closest} is {apart.get(closest, 0):.0f} degrees away"),
        ("the accent pink passes the 3:1 mark gate on a white canvas", contrast(pink, CANVAS) >= 3.0,
         f"{contrast(pink, CANVAS):.2f}:1"),
    ]


def focus_checks(work: Path) -> list[tuple[str, bool, str]]:
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
        drawn = geometry.run_trace(fill_template(model), work) if model else None
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


def fan_in_checks(work: Path) -> list[tuple[str, bool, str]]:
    """Four sockets on a gateway of four magnets: the last one merges into an arrival instead of looping to a free magnet."""
    name = "an architecture with four clients on one gateway"
    drawn = geometry.run_trace(fill_template(DEFECT_MODELS[name]), work)
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
    results.append((f"{TEMPLATE.name} holds {PLACEHOLDER} once", template.count(PLACEHOLDER) == 1, ""))
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
            code = fill_template(model)
            results.append((f"{name} fits one use_figma call", len(code) <= MAX_CODE_CHARS, f"{len(code)} characters"))
            if node:
                with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False, encoding="utf-8") as handle:
                    handle.write("export async function run(figma) {\n" + code + "\n}\n")
                checked = subprocess.run([node, "--check", handle.name], capture_output=True, text=True)
                Path(handle.name).unlink()
                results.append((f"{name} is valid JavaScript", checked.returncode == 0, checked.stderr.strip()))
                with tempfile.TemporaryDirectory() as work:
                    results += drawn_checks(name, model, geometry.run_trace(code, Path(work)))
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
    results += accent_palette_checks(template)
    if node:
        with tempfile.TemporaryDirectory() as work:
            results += defect_checks(Path(work))
            results += focus_checks(Path(work))
            results += fan_in_checks(Path(work))
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

#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: FLOWCHART PROFILES
# ───────────────────────────────────────────────────────────────

"""The three diagrams written as a Mermaid flowchart: a user flow, a process and an architecture.

They share one grammar and differ in how the board lays them out. A user flow
and a process are laid out in ranks, so the rules guard shape, exits,
connectors and colour. An architecture is placed by the lane each part sits in,
on the composed board and on Figma's generated fallback, so its rules are
Figma's lane and edge table, which the generator errors on or silently
mis-draws without.
"""
from __future__ import annotations

import dataclasses
import re
from typing import TYPE_CHECKING

from .common import (
    ACCENT_PAIRS,
    LANE_PAIR,
    NEEDS_QUOTES,
    PAIRED_FILL,
    hex_colour,
    id_problems,
    length_problems,
    raw_problems,
    statements,
)

if TYPE_CHECKING:
    from mermaid_extract import Diagram, Edge, Node

USER_FLOW, PROCESS, ARCHITECTURE = "user-flow", "process", "architecture"
DIRECTIONS = {"TD", "TB", "LR"}
# TD and TB are one direction under two names.
SAME_WAY = {"TB": "TD"}
MAX_DECISION_EXITS = 3
# Four connectors with one label say nothing the shape does not, and a decision's
# exits name their own branches, so those are not counted.
MAX_LABEL_REPEATS = 3
MERGE_DOT_LABELS = {"", "."}
USER_FLOW_SHAPES = {"stadium": "start or end", "rect": "step", "rhombus": "decision", "circle": "merge dot"}
# A process adds the FigJam shapes that carry a meaning of their own: a store, a
# step that is a process in itself, and data entering or leaving.
PROCESS_SHAPES = {**USER_FLOW_SHAPES, "cylinder": "datastore", "subroutine": "sub-process",
                  "parallelogram": "input or output"}
# A store and an input or output only need a connector. Every other node but a
# start or end needs a way in and a way out.
ENDPOINT_SHAPES = {"stadium", "cylinder", "parallelogram"}
# The general budget, and the lane budget sk-design-diagram sets for a process.
BUDGET = {USER_FLOW: (9, 12), PROCESS: (9, 12), ARCHITECTURE: (9, 12)}
LANED_PROCESS_BUDGET = (12, 16)
MIN_LANES, MAX_LANES = 2, 6
ARCHITECTURE_LANES = ("client", "gateway", "service", "datastore", "external", "async")
# The composed board stands the queue lane next to the service lane that writes to it and reads from it, so
# the two edges that join them stay short and the other lanes' edges no longer cross it.
ARCHITECTURE_COLUMNS = ("client", "gateway", "service", "async", "datastore", "external")
# Figma's allowed-edge table, as (from lane, to lane, kind).
ALLOWED_ARCHITECTURE_EDGES = {
    ("client", "gateway", "forward"), ("gateway", "service", "forward"),
    ("service", "service", "forward"), ("service", "datastore", "forward"),
    ("client", "gateway", "two-way"), ("service", "service", "two-way"),
    ("service", "service", "backward"),
    ("service", "async", "dotted"), ("async", "service", "dotted"), ("service", "external", "dotted"),
}
DOTTED_LANES = {"async", "external"}
# A laned process may name one lane as its status lane: the states a shared record moves through, drawn
# first, joined in order and moved by a step's dotted `-.->`. It is never an actor lane.
STATUS_DIRECTIVE = re.compile(r"^\s*%%\s*status\s*:\s*(.*?)\s*$", re.I | re.M)
# A step's body under its one-line label belongs to the Faithful detail level alone, which the model names.
LEVEL_DIRECTIVE = re.compile(r"^\s*%%\s*level\s*:\s*(.*?)\s*$", re.I | re.M)
DETAIL_DIRECTIVE = re.compile(r"^\s*%%\s*detail\s*:\s*(.*?)\s*$", re.I | re.M)
LEVELS = ("simplified", "balanced", "faithful")
DETAIL_LEVEL = "faithful"
MAX_BODY_LINES, MAX_BODY_CHARS = 10, 44
# A laned process at the Faithful level with detail cards keeps more of its source, so it reads at a larger budget.
DETAILED_PROCESS_BUDGET = (18, 24)
# A connector longer than `-->` or an invisible link renders differently from
# the arrow the rule names, and the extractor reads both as plain edges.
ODD_CONNECTOR = re.compile(r"-{3,}>|~~~")
STYLE_STATEMENT = re.compile(r"^(style|classDef|linkStyle)\s", re.I)
COLOUR = {key: re.compile(rf"\b{key}\s*:\s*([^,;\s]+)", re.I) for key in ("fill", "stroke")}
# `a <---|"Refund"| b` is a backward edge: the refund flows from b to a. The
# extractor cannot read it, so it is rewritten as `b -->|"Refund"| a` first.
BACKWARD_EDGE = re.compile(r"^(\s*)([\w.:-]+)\s*<---\s*(\|[^|]*\|)?\s*([\w.:-]+)\s*$")


def rewrite_backward_edges(block_text: str) -> tuple[str, set[tuple[str, str]]]:
    """Turn each `a <--- b` line into the forward edge the extractor reads, and name the pairs turned."""
    lines, backward = [], set()
    for line in block_text.splitlines():
        match = BACKWARD_EDGE.match(line)
        if match:
            indent, left, label, right = match.groups()
            backward.add((right, left))
            line = f"{indent}{right} -->{label or ''} {left}"
        lines.append(line)
    return "\n".join(lines), backward


def colour(statement: str, key: str) -> str:
    """The fill or stroke a style statement sets, as six-digit lower-case hex, or an empty string."""
    match = COLOUR[key].search(statement)
    return hex_colour(match.group(1)) if match else ""


def colour_problems(block_text: str, lanes: set[str], need_accent: bool = False) -> list[str]:
    """Every colour is a FigJam palette swatch, a lane takes the neutral pair, and one accent at most.

    A flow whose board is read for one thing needs that thing marked, so `need_accent` also asks for a
    `style` line on a node: the composer turns it into the one heavy outline the first glance lands on.
    """
    accents, problems, marked = set(), [], 0
    for statement in statements(block_text):
        if not STYLE_STATEMENT.match(statement):
            continue
        words = statement.split()
        keyword, target = words[0].lower(), (words[1] if len(words) > 1 else "")
        fill, stroke = colour(statement, "fill"), colour(statement, "stroke")
        if keyword == "style" and target in lanes:
            if (fill, stroke) != LANE_PAIR:
                problems.append(f"lane {target} takes fill {fill or 'none'} and stroke {stroke or 'none'}: "
                                "a lane takes the neutral pair fill:#F5F5F5,stroke:#B3B3B3")
            continue
        marked += keyword == "style" and bool(fill or stroke)
        if fill:
            if fill not in ACCENT_PAIRS:
                problems.append(f"fill {fill} is not a FigJam light fill: pick a pair from references/style-guide.md")
                continue
            if stroke and stroke != ACCENT_PAIRS[fill]:
                problems.append(f"fill {fill} takes the stroke {stroke}, but FigJam pairs it with {ACCENT_PAIRS[fill]}")
            accents.add(fill)
        elif stroke:
            if stroke not in PAIRED_FILL:
                problems.append(
                    f"stroke {stroke} is not a FigJam palette stroke: "
                    "pick a pair from references/style-guide.md"
                )
                continue
            accents.add(PAIRED_FILL[stroke])
    if need_accent and not marked:
        problems.append("the model has no accent: the first glance needs one style line on the node it names, "
                        "a decision, a failing end or the one step in focus, such as style pick fill:#FFC2EC,stroke:#F849C1")
    if len(accents) > 1:
        problems.append(f"{len(accents)} accent colours ({', '.join(sorted(accents))}), at most 1: "
                        "colour marks the happy path, one decision or one handoff")
    return problems


def quote_problems(owner: str, label: str, block_text: str) -> list[str]:
    """A label holding a parenthesis, a colon or a slash that the block leaves unquoted."""
    if NEEDS_QUOTES.search(label) and f'"{label}"' not in block_text:
        return [f"{owner} label holds a parenthesis, a colon or a slash: put it in double quotes"]
    return []


def label_problems(owner: str, label: str, block_text: str) -> list[str]:
    """Every length and quoting problem of one label."""
    return length_problems(owner, label) + quote_problems(owner, label, block_text)


def edges_of(diagram: Diagram, node_id: str) -> tuple[list[Edge], list[Edge]]:
    """The edges that leave a node and the edges that reach it."""
    exits = [edge for edge in diagram.edges if edge.source == node_id]
    entries = [edge for edge in diagram.edges if edge.target == node_id]
    return exits, entries


def node_problems(diagram: Diagram, node: Node, block_text: str, first_id: str, shapes: dict) -> list[str]:
    """What breaks one step of a user flow or a process: its id, its label, its shape or its ways in and out."""
    problems = id_problems(node.id) + label_problems(f"node {node.id}", node.label, block_text)
    if node.shape not in shapes:
        problems.append(f"node {node.id} has the shape {node.shape}, which this diagram does not use: "
                        f"{', '.join(f'{shape} for a {role}' for shape, role in shapes.items())}")
    exits, entries = edges_of(diagram, node.id)
    if not exits and not entries:
        return problems + [f"node {node.id} has no connector"]
    if node.shape == "rhombus":
        if not exits:
            problems.append(f"decision {node.id} has no exit")
        if len(exits) > MAX_DECISION_EXITS:
            problems.append(f"decision {node.id} has {len(exits)} exits, at most {MAX_DECISION_EXITS}")
        for edge in exits:
            if not edge.label.strip():
                problems.append(f"decision {node.id} exit to {edge.target} has no label")
    if node.shape == "circle" and node.label.strip() not in MERGE_DOT_LABELS:
        problems.append(f"merge dot {node.id} carries the label {node.label!r}: write (( . )) with no words")
    if node.shape == "stadium" and exits and entries and node.id != first_id:
        problems.append(f"stadium {node.id} sits mid-flow: a stadium starts or ends the flow, a step is a rectangle")
    if node.shape not in ENDPOINT_SHAPES and exits and not entries:
        problems.append(f"node {node.id} has no way in: only a stadium starts a flow")
    if node.shape not in ENDPOINT_SHAPES and node.shape != "rhombus" and entries and not exits:
        problems.append(f"node {node.id} has no way out: a flow ends on a stadium")
    return problems


def lane_problems(diagram: Diagram) -> tuple[list[str], set[str]]:
    """The problems with a process's lanes, and the lane ids the colour check exempts."""
    lanes = [node for node in diagram.nodes if node.container]
    lane_ids = {lane.id for lane in lanes}
    if not lanes:
        return [], lane_ids
    problems = []
    if not MIN_LANES <= len(lanes) <= MAX_LANES:
        problems.append(
            f"{len(lanes)} lanes, a laned process has {MIN_LANES} to {MAX_LANES}: "
            "one lane is no lane at all"
        )
    for lane in lanes:
        problems += id_problems(lane.id, "lane id")
        if lane.parent:
            problems.append(f"lane {lane.id} sits inside lane {lane.parent}: lanes do not nest")
        if not any(node.parent == lane.id and not node.container for node in diagram.nodes):
            problems.append(f"lane {lane.id} holds no step")
    for node in diagram.nodes:
        if not node.container and node.parent not in lane_ids:
            problems.append(
                f"node {node.id} sits outside every lane: "
                "once a process has lanes, every step has an owner"
            )
    for edge in diagram.edges:
        for end in (edge.source, edge.target):
            if end in lane_ids:
                problems.append(
                    f"edge {edge.source} to {edge.target} joins the lane {end}: "
                    "connect the steps inside it"
                )
    return problems, lane_ids


def status_problems(diagram: Diagram, block_text: str, profile: str, lane_ids: set[str]) -> tuple[list[str], set[str]]:
    """The problems with a status lane, and the ids of the states it holds."""
    named = STATUS_DIRECTIVE.findall(block_text)
    if not named:
        return [], set()
    if profile != PROCESS or not lane_ids:
        return ["%% status on a diagram without lanes: a status lane belongs to a laned process"], set()
    if len(named) > 1:
        return [f"{len(named)} %% status lines, at most 1: a record moves through one series of statuses"], set()
    lane = named[0]
    if lane not in lane_ids:
        return [f"%% status: {lane or '(empty)'} names no lane: write the id of the lane that holds the statuses"], set()
    problems = []
    first = next(node.id for node in diagram.nodes if node.container)
    if first != lane:
        problems.append(f"status lane {lane} is declared after lane {first}: declare it first, so the board draws it on top")
    states = {node.id for node in diagram.nodes if node.parent == lane and not node.container}
    for node in diagram.nodes:
        if node.id in states and node.shape != "rect":
            problems.append(f"status state {node.id} is drawn as a {node.shape}: write it [Label], "
                            "the board draws a status as a chevron")
    if len(states) < 2:
        problems.append(f"status lane {lane} holds {len(states)} states: a status lane holds two or more")
    following, preceding = {}, {}
    for edge in diagram.edges:
        name = f"edge {edge.source} to {edge.target}"
        if edge.source in states and edge.target in states:
            if edge.style != "solid":
                problems.append(f"{name} joins two statuses dotted: join them in order with -->")
            following.setdefault(edge.source, []).append(edge.target)
            preceding.setdefault(edge.target, []).append(edge.source)
        elif edge.source in states:
            problems.append(f"status state {edge.source} leads to {edge.target}: a status only moves, "
                            f"so draw the step's -.-> into the status instead")
        elif edge.target in states and edge.style != "dashed":
            problems.append(f"{name} is solid: a step moves the status with -.->")
    heads = [state for state in states if state not in preceding]
    walked, at = [], heads[0] if len(heads) == 1 else None
    while at and at not in walked:
        walked.append(at)
        at = following.get(at, [None])[0]
    chained = len(heads) == 1 and len(walked) == len(states) and all(len(v) == 1 for v in following.values()) \
        and all(len(v) == 1 for v in preceding.values())
    if states and not chained:
        problems.append(f"the states in lane {lane} form no single chain: join them in order with --> "
                        "from the first status to the last")
    moved = {edge.target for edge in diagram.edges if edge.target in states and edge.source not in states}
    for state in walked[1:] if chained else []:
        if state not in moved:
            problems.append(f"status {state} is never moved: draw -.-> into it from the step that moves the record there")
    for statement in statements(block_text):
        words = statement.split()
        if STYLE_STATEMENT.match(statement) and len(words) > 1 and words[1] in states:
            problems.append(f"status {words[1]} takes a style line: the accent goes on a decision, "
                            "a failing end or the one step in focus, never a status")
    return problems, states


def status_states(diagram: Diagram, block_text: str) -> set[str]:
    """The ids of the states a single `%% status:` line's lane holds, or none."""
    named = STATUS_DIRECTIVE.findall(block_text)
    lane = named[0] if len(named) == 1 else None
    return {node.id for node in diagram.nodes if lane and node.parent == lane and not node.container}


def work_view(diagram: Diagram, states: set[str]) -> Diagram:
    """The diagram without its status lane: the steps and the connectors the work moves along.

    A status move is no way out of a step and the status chain is no path the work takes, so the rules on
    ways in and out, the path lengths and the goal are read on this view.
    """
    if not states:
        return diagram
    lanes = {node.parent for node in diagram.nodes if node.id in states}
    return dataclasses.replace(diagram, nodes=[node for node in diagram.nodes if node.id not in states | lanes],
                               edges=[edge for edge in diagram.edges if edge.source not in states and edge.target not in states])


def detail_problems(diagram: Diagram, block_text: str, states: set[str]) -> tuple[list[str], int]:
    """The problems with the bodies `%% detail:` lines give steps, and how many steps carry one."""
    lines = DETAIL_DIRECTIVE.findall(block_text)
    levels = [value.lower() for value in LEVEL_DIRECTIVE.findall(block_text)]
    problems = []
    if len(levels) > 1:
        problems.append(f"{len(levels)} %% level lines, at most 1")
    for value in levels:
        if value not in LEVELS:
            problems.append(f"%% level: {value or '(empty)'} is no detail level: write {', '.join(LEVELS)}")
    if not lines:
        return problems, 0
    if DETAIL_LEVEL not in levels:
        problems.append(f"{len(lines)} %% detail lines need %% level: {DETAIL_LEVEL}: a body belongs to the Faithful "
                        "detail level, and Balanced and Simplified keep one-line labels")
    shapes = {node.id: node.shape for node in diagram.nodes if not node.container}
    seen = set()
    for value in lines:
        parts = [part.strip() for part in value.split("|")]
        node_id, body = parts[0], parts[1:]
        if node_id not in shapes:
            problems.append(f"%% detail: {node_id or '(empty)'} names no step: write %% detail: <step id> | line | line")
            continue
        if node_id in seen:
            problems.append(f"node {node_id} has two %% detail lines: write its whole body on one")
        seen.add(node_id)
        if shapes[node_id] != "rect" or node_id in states:
            problems.append(f"%% detail on {node_id}, a {'status' if node_id in states else shapes[node_id]}: "
                            "only a step [Label] carries a body")
        if not any(body):
            problems.append(f"%% detail: {node_id} has no body line: write %% detail: {node_id} | line | line")
        if len(body) > MAX_BODY_LINES:
            problems.append(f"node {node_id} carries {len(body)} body lines, at most {MAX_BODY_LINES}: "
                            "keep what a reader acts on and leave the rest in the source")
        for line in body:
            if not line:
                problems.append(f"node {node_id} has an empty body line: drop the extra |")
            elif len(line) > MAX_BODY_CHARS:
                problems.append(f"node {node_id} body line {line[:24]!r}... runs {len(line)} characters, "
                                f"at most {MAX_BODY_CHARS}: split it into two lines")
    return problems, len(seen)


def edge_problems(diagram: Diagram, block_text: str, allow_dotted: bool) -> list[str]:
    """Each edge that is not a one-way arrow this diagram draws, and each problem with an edge label."""
    problems = []
    for edge in diagram.edges:
        one_way = edge.arrowhead == "arrow" and not edge.bidirectional and not edge.undirected
        styled = edge.style == "solid" or (allow_dotted and edge.style == "dashed")
        if not (one_way and styled):
            wanted = "--> or -.->" if allow_dotted else "-->"
            problems.append(f"edge {edge.source} to {edge.target} is not a one-way arrow this diagram draws: "
                            f"write {wanted}, and put a status in the label")
        problems += label_problems(f"edge {edge.source} to {edge.target}", edge.label, block_text)
    return problems


def repeated_label_problems(diagram: Diagram, states: frozenset[str] = frozenset()) -> list[str]:
    """One label on four or more connectors says nothing: the shape already carries the step."""
    decisions = {node.id for node in diagram.nodes if node.shape == "rhombus"}
    counted, written = {}, {}
    for edge in diagram.edges:
        label = edge.label.strip()
        key = label.lower()
        if not key or edge.source in decisions or edge.target in states:
            continue
        counted[key] = counted.get(key, 0) + 1
        written.setdefault(key, label)
    return [f"{count} connectors carry the label {written[key]!r}, at most {MAX_LABEL_REPEATS}: "
            "cut them all, or keep one where the label says something the shape cannot"
            for key, count in sorted(counted.items()) if count > MAX_LABEL_REPEATS]


def self_loop_problems(diagram: Diagram) -> list[str]:
    """The edges from a node back onto the same node, which the board draws as no loop a reader can follow."""
    return [f"edge {edge.source} to itself: a node that returns to itself draws no loop, "
            "so write the retry into a label or draw the node it returns through"
            for edge in diagram.edges if edge.source == edge.target]


def check_flow(diagram: Diagram, block_text: str, profile: str) -> list[str]:
    """A user flow or a process, both laid out in ranks."""
    problems = raw_problems(block_text)
    if ODD_CONNECTOR.search("\n".join(statements(block_text))):
        problems.append("the block carries a long or invisible connector: every connector is written -->")
    if diagram.direction not in DIRECTIONS:
        problems.append(f"direction {diagram.direction}, a flow runs top to bottom (TD) or left to right (LR)")
    if profile == USER_FLOW:
        shapes, lane_ids = USER_FLOW_SHAPES, set()
        for node in diagram.nodes:
            if node.container:
                problems.append(f"subgraph {node.id}: a user flow has no subgraphs, split it into diagrams instead")
    else:
        shapes = PROCESS_SHAPES
        found, lane_ids = lane_problems(diagram)
        problems += found
    found, states = status_problems(diagram, block_text, profile, lane_ids)
    problems += found
    found, detailed = detail_problems(diagram, block_text, states)
    problems += found
    problems += colour_problems(block_text, lane_ids, need_accent=True)
    steps = [node for node in diagram.nodes if not node.container]
    first_id = next((node.id for node in steps if node.id not in states), "")
    work = work_view(diagram, states)
    for node in steps:
        if node.id in states:
            # A status has its own rules above: it is reached by moves and chained, never a step with a way through.
            problems += id_problems(node.id) + label_problems(f"node {node.id}", node.label, block_text)
            continue
        problems += node_problems(work, node, block_text, first_id, shapes)
    max_nodes, max_edges = LANED_PROCESS_BUDGET if lane_ids else BUDGET[profile]
    if lane_ids and detailed:
        max_nodes, max_edges = DETAILED_PROCESS_BUDGET
    if len(steps) > max_nodes:
        problems.append(f"{len(steps)} nodes, at most {max_nodes}: split the flow")
    if max_edges is not None and len(diagram.edges) > max_edges:
        problems.append(f"{len(diagram.edges)} connectors, at most {max_edges}: split the flow")
    problems += edge_problems(diagram, block_text, allow_dotted=profile == PROCESS)
    problems += self_loop_problems(diagram)
    problems += repeated_label_problems(diagram, frozenset(states))
    return problems


def edge_kind(edge: Edge, backward: set[tuple[str, str]]) -> str:
    """The kind of an architecture edge, named the way the allowed-edge table names kinds."""
    if (edge.source, edge.target) in backward:
        return "backward"
    if edge.bidirectional:
        return "two-way-dotted" if edge.style == "dashed" else "two-way"
    if edge.undirected or edge.arrowhead != "arrow" or edge.style == "thick":
        return "other"
    return "dotted" if edge.style == "dashed" else "forward"


def has_cycle(nodes: list[str], edges: list[tuple[str, str]]) -> bool:
    """Whether the directed edges between these nodes close a loop."""
    following = {node: [] for node in nodes}
    for source, target in edges:
        following.setdefault(source, []).append(target)
    state = {}

    def visit(node: str) -> bool:
        state[node] = "open"
        for target in following.get(node, []):
            if state.get(target) == "open" or (target not in state and visit(target)):
                return True
        state[node] = "done"
        return False

    return any(node not in state and visit(node) for node in list(following))


def check_architecture(diagram: Diagram, block_text: str, backward: set[tuple[str, str]]) -> list[str]:
    """Figma's architecture layout: fixed lanes, a table of allowed edges and a forward flow with no cycle."""
    problems = raw_problems(block_text)
    if ODD_CONNECTOR.search("\n".join(statements(block_text))):
        problems.append("the block carries a long or invisible connector: write -->, -.->, <--> or <---")
    if diagram.direction != "LR":
        problems.append(f"direction {diagram.direction}, an architecture runs left to right: write flowchart LR")
    if any(STYLE_STATEMENT.match(s) for s in statements(block_text)) or ":::" in block_text:
        problems.append("the block carries styling: the architecture layout colours each lane itself, drop it")
    if STATUS_DIRECTIVE.search(block_text) or DETAIL_DIRECTIVE.search(block_text):
        problems.append("the block carries %% status or %% detail: a status lane and detail cards belong to "
                        "a laned process, and an architecture keeps one-line services")
    lanes = [node for node in diagram.nodes if node.container]
    lane_of = {}
    seen_lanes = set()
    for lane in lanes:
        if lane.id not in ARCHITECTURE_LANES:
            problems.append(f"lane {lane.id} is not one of {', '.join(ARCHITECTURE_LANES)}: "
                            f"keep the id and put the title in the label, as subgraph service [\"Core Services\"]")
        if lane.id in seen_lanes:
            problems.append(f"lane {lane.id} is declared twice")
        seen_lanes.add(lane.id)
        if lane.parent:
            problems.append(f"lane {lane.id} sits inside lane {lane.parent}: lanes do not nest")
    steps = [node for node in diagram.nodes if not node.container]
    for node in steps:
        problems += id_problems(node.id) + label_problems(f"node {node.id}", node.label, block_text)
        if node.shape != "rect":
            problems.append(f"node {node.id} has the shape {node.shape}: the layout assigns shapes, write [label]")
        if node.parent not in ARCHITECTURE_LANES:
            problems.append(f"node {node.id} sits outside every lane: the layout cannot place it")
        lane_of[node.id] = node.parent
    if len(steps) > BUDGET[ARCHITECTURE][0]:
        problems.append(f"{len(steps)} nodes, at most {BUDGET[ARCHITECTURE][0]}: draw one flow per diagram")
    if len(diagram.edges) > BUDGET[ARCHITECTURE][1]:
        problems.append(
            f"{len(diagram.edges)} connectors, at most {BUDGET[ARCHITECTURE][1]}: "
            "draw one flow per diagram"
        )
    problems += self_loop_problems(diagram)
    pairs, forward, ways_in, ways_out = set(), [], {}, {}
    for edge in diagram.edges:
        name = f"edge {edge.source} to {edge.target}"
        if edge.source in seen_lanes or edge.target in seen_lanes:
            problems.append(f"{name} joins a lane: connect a node inside it")
            continue
        pair = frozenset((edge.source, edge.target))
        if pair in pairs:
            problems.append(f"{name} repeats a pair already joined: merge the two into one edge with one label")
        pairs.add(pair)
        problems += label_problems(name, edge.label, block_text)
        kind = edge_kind(edge, backward)
        source_lane, target_lane = lane_of.get(edge.source), lane_of.get(edge.target)
        if kind == "two-way-dotted":
            problems.append(f"{name} is a two-way dotted edge, which falls back to one way: draw two -.-> edges")
        elif (source_lane in DOTTED_LANES or target_lane in DOTTED_LANES) and kind != "dotted":
            lane = source_lane if source_lane in DOTTED_LANES else target_lane
            problems.append(f"{name} touches the {lane} lane: write it dotted, -.->")
        elif (source_lane, target_lane, kind) not in ALLOWED_ARCHITECTURE_EDGES:
            fix = ("the missing lane goes in between: a gateway between a client and a service"
                   if (source_lane, target_lane) == ("client", "service") else "a service mediates")
            problems.append(f"{name} runs {source_lane} to {target_lane} as a {kind} edge, which is not in the "
                            f"allowed-edge table: {fix}")
        if source_lane != target_lane and not edge.label.strip():
            problems.append(f"{name} crosses from {source_lane} to {target_lane} with no label")
        if target_lane == "external" and ": " not in edge.label:
            problems.append(f"{name} reaches an external system: label it \"Service: Purpose\"")
        if kind in ("forward", "two-way"):
            forward.append((edge.source, edge.target))
        ways_out.setdefault(edge.source, 0)
        ways_out[edge.source] += 1
        ways_in.setdefault(edge.target, 0)
        ways_in[edge.target] += 1
        if kind == "two-way":
            ways_out[edge.target] = ways_out.get(edge.target, 0) + 1
            ways_in[edge.source] = ways_in.get(edge.source, 0) + 1
    if has_cycle([node.id for node in steps], forward):
        problems.append("the forward and two-way edges form a cycle: draw the returning edge backward, a <--- b")
    for node in steps:
        if lane_of.get(node.id) == "service" and not (ways_in.get(node.id) and ways_out.get(node.id)):
            problems.append(
                f"service {node.id} needs a way in and a way out: "
                "an edge is missing or the node is not needed"
            )
        elif not ways_in.get(node.id) and not ways_out.get(node.id):
            problems.append(f"node {node.id} has no connector")
    return problems


def direction_family(direction: str) -> str:
    """A direction under its one canonical name, so TB and TD compare equal."""
    return SAME_WAY.get(direction, direction)

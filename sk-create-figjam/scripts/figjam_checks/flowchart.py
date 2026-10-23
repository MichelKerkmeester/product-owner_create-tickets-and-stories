# ───────────────────────────────────────────────────────────────
# COMPONENT: FLOWCHART PROFILES
# ───────────────────────────────────────────────────────────────

"""The three diagrams written as a Mermaid flowchart: a user flow, a process and an architecture.

They share one grammar and differ in what the board generator does with it.
A user flow and a process are laid out by ELK, so the rules guard shape,
exits, connectors and colour. An architecture goes to a separate grid layout
that places nodes by the lane they sit in, so its rules are Figma's lane and
edge table, which the generator errors on or silently mis-draws without.
"""
from __future__ import annotations

import re

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
# Figma's allowed-edge table, as (from lane, to lane, kind).
ALLOWED_ARCHITECTURE_EDGES = {
    ("client", "gateway", "forward"), ("gateway", "service", "forward"),
    ("service", "service", "forward"), ("service", "datastore", "forward"),
    ("client", "gateway", "two-way"), ("service", "service", "two-way"),
    ("service", "service", "backward"),
    ("service", "async", "dotted"), ("async", "service", "dotted"), ("service", "external", "dotted"),
}
DOTTED_LANES = {"async", "external"}
# A connector longer than `-->` or an invisible link renders differently from
# the arrow the rule names, and the extractor reads both as plain edges.
ODD_CONNECTOR = re.compile(r"-{3,}>|~~~")
STYLE_STATEMENT = re.compile(r"^(style|classDef|linkStyle)\s", re.I)
COLOUR = {key: re.compile(rf"\b{key}\s*:\s*([^,;\s]+)", re.I) for key in ("fill", "stroke")}
# `a <---|"Refund"| b` is a backward edge: the refund flows from b to a. The
# extractor cannot read it, so it is rewritten as `b -->|"Refund"| a` first.
BACKWARD_EDGE = re.compile(r"^(\s*)([\w.:-]+)\s*<---\s*(\|[^|]*\|)?\s*([\w.:-]+)\s*$")


def rewrite_backward_edges(block_text: str) -> tuple[str, set[tuple[str, str]]]:
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
    match = COLOUR[key].search(statement)
    return hex_colour(match.group(1)) if match else ""


def colour_problems(block_text: str, lanes: set[str]) -> list[str]:
    """Every colour is a FigJam palette swatch, a lane takes the neutral pair, and one accent at most."""
    accents, problems = set(), []
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
    if len(accents) > 1:
        problems.append(f"{len(accents)} accent colours ({', '.join(sorted(accents))}), at most 1: "
                        "colour marks the happy path, one decision or one handoff")
    return problems


def quote_problems(owner: str, label: str, block_text: str) -> list[str]:
    if NEEDS_QUOTES.search(label) and f'"{label}"' not in block_text:
        return [f"{owner} label holds a parenthesis, a colon or a slash: put it in double quotes"]
    return []


def label_problems(owner: str, label: str, block_text: str) -> list[str]:
    return length_problems(owner, label) + quote_problems(owner, label, block_text)


def edges_of(diagram, node_id: str) -> tuple[list, list]:
    exits = [edge for edge in diagram.edges if edge.source == node_id]
    entries = [edge for edge in diagram.edges if edge.target == node_id]
    return exits, entries


def node_problems(diagram, node, block_text: str, first_id: str, shapes: dict) -> list[str]:
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


def lane_problems(diagram) -> tuple[list[str], set[str]]:
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


def edge_problems(diagram, block_text: str, allow_dotted: bool) -> list[str]:
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


def repeated_label_problems(diagram) -> list[str]:
    """One label on four or more connectors says nothing: the shape already carries the step."""
    decisions = {node.id for node in diagram.nodes if node.shape == "rhombus"}
    counted, written = {}, {}
    for edge in diagram.edges:
        label = edge.label.strip()
        key = label.lower()
        if not key or edge.source in decisions:
            continue
        counted[key] = counted.get(key, 0) + 1
        written.setdefault(key, label)
    return [f"{count} connectors carry the label {written[key]!r}, at most {MAX_LABEL_REPEATS}: "
            "cut them all, or keep one where the label says something the shape cannot"
            for key, count in sorted(counted.items()) if count > MAX_LABEL_REPEATS]


def check_flow(diagram, block_text: str, profile: str) -> list[str]:
    """A user flow or a process, both laid out by ELK."""
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
    problems += colour_problems(block_text, lane_ids)
    steps = [node for node in diagram.nodes if not node.container]
    first_id = steps[0].id if steps else ""
    for node in steps:
        problems += node_problems(diagram, node, block_text, first_id, shapes)
    max_nodes, max_edges = LANED_PROCESS_BUDGET if lane_ids else BUDGET[profile]
    if len(steps) > max_nodes:
        problems.append(f"{len(steps)} nodes, at most {max_nodes}: split the flow")
    if max_edges is not None and len(diagram.edges) > max_edges:
        problems.append(f"{len(diagram.edges)} connectors, at most {max_edges}: split the flow")
    problems += edge_problems(diagram, block_text, allow_dotted=profile == PROCESS)
    problems += repeated_label_problems(diagram)
    return problems


def edge_kind(edge, backward: set[tuple[str, str]]) -> str:
    if (edge.source, edge.target) in backward:
        return "backward"
    if edge.bidirectional:
        return "two-way-dotted" if edge.style == "dashed" else "two-way"
    if edge.undirected or edge.arrowhead != "arrow" or edge.style == "thick":
        return "other"
    return "dotted" if edge.style == "dashed" else "forward"


def has_cycle(nodes: list[str], edges: list[tuple[str, str]]) -> bool:
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


def check_architecture(diagram, block_text: str, backward: set[tuple[str, str]]) -> list[str]:
    """Figma's architecture layout: fixed lanes, a table of allowed edges and a forward flow with no cycle."""
    problems = raw_problems(block_text)
    if ODD_CONNECTOR.search("\n".join(statements(block_text))):
        problems.append("the block carries a long or invisible connector: write -->, -.->, <--> or <---")
    if diagram.direction != "LR":
        problems.append(f"direction {diagram.direction}, an architecture runs left to right: write flowchart LR")
    if any(STYLE_STATEMENT.match(s) for s in statements(block_text)) or ":::" in block_text:
        problems.append("the block carries styling: the architecture layout colours each lane itself, drop it")
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
            problems.append(f"{name} runs {source_lane} to {target_lane} as a {kind} edge, which is not in the "
                            "allowed-edge table: a service mediates")
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
    return SAME_WAY.get(direction, direction)

#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: STATE PROFILE
# ───────────────────────────────────────────────────────────────

"""A state diagram: the states of one thing and what moves it between them.

Notes and styling are worse than dropped here. The generator reads the `X: text`
inside a note and the state names inside a style line as state definitions,
so the board grows phantom states. Both are refused, and colour or notes are
added afterwards through the hybrid workflow.
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from .common import content_lines, id_problems, length_problems, raw_problems

if TYPE_CHECKING:
    from mermaid_extract import Diagram, Node

MAX_STATES = 9
MAX_TRANSITIONS = 12
MAX_CHOICE_EXITS = 3
DIRECTIONS = {"LR", "TB", "TD"}
STEREOTYPE = re.compile(r"^state\s+([\w.:-]+)\s+<<(fork|join|choice)>>$", re.I)
REFUSED = (
    (re.compile(r"^note\b", re.I), "a note, which the generator turns into phantom states"),
    (re.compile(r"^(classDef|class|style)\s", re.I), "styling, which the generator turns into phantom states"),
)
PSEUDO = {"start", "end", "fork", "join", "choice"}


def check_state(diagram: Diagram, block_text: str) -> list[str]:
    """The problems with a state diagram, read from its parse and from the raw lines the parse cleans up."""
    problems = raw_problems(block_text)
    lines = content_lines(block_text)
    stereotypes = {}
    for number, text in lines:
        for pattern, what in REFUSED:
            if pattern.search(text):
                problems.append(f"line {number}: {what}: add it afterwards through the hybrid workflow")
        if ":::" in text:
            problems.append(f"line {number}: a ::: class, which the generator turns into phantom states")
        if re.search(r"(?<![-<])->(?!>)", text) and "-->" not in text:
            problems.append(f"line {number}: a transition is written -->")
        stereotype = STEREOTYPE.match(text)
        if stereotype:
            stereotypes[stereotype.group(1)] = stereotype.group(2).lower()
    if diagram.direction not in DIRECTIONS:
        problems.append(f"direction {diagram.direction}: a state machine runs LR or TB, and TD is another name for TB")
    def kind(node: Node) -> str:
        return stereotypes.get(node.id, node.shape)
    named = [node for node in diagram.nodes if kind(node) not in PSEUDO]
    by_id = {node.id: node for node in diagram.nodes}
    for node in named:
        problems += id_problems(node.id, "state id") + length_problems(f"state {node.id}", node.label)
        if node.container and node.parent:
            problems.append(
                f"composite {node.id} sits inside composite {node.parent}: "
                "draw the inner machine as its own diagram"
            )
        touching = [edge for edge in diagram.edges if node.id in (edge.source, edge.target)]
        if not touching and not node.container:
            problems.append(f"state {node.id} has no transition")
        # The composer anchors an edge to or from a composite on its inner start, so a composite without one
        # is placed against whichever member the model lists first.
        if node.container and not any(by_id[edge.source].shape == "start" and by_id[edge.source].parent == node.id
                                      for edge in diagram.edges):
            problems.append(
                f"composite {node.id} has no [*] entry: start it with [*] --> a state inside, "
                "which the composer needs to place the composite after the state that enters it"
            )
    if not any(by_id[edge.source].shape == "start" and by_id[edge.source].parent is None for edge in diagram.edges):
        problems.append("the machine has no entry: start it with [*] --> a state")
    for edge in diagram.edges:
        source, target = by_id[edge.source], by_id[edge.target]
        name = f"transition {display(source)} to {display(target)}"
        problems += length_problems(name, edge.label)
        if source.parent != target.parent:
            problems.append(f"{name} reaches into another composite: transition to or from the composite itself")
        between_states = kind(source) not in PSEUDO and kind(target) not in PSEUDO
        if between_states and not edge.label.strip():
            problems.append(f"{name} has no label: name the event that triggers it")
        # The board shows each state by its label, so a guard that names the id points at nothing a reader sees.
        for guard in re.finditer(r"\[from ([^\]]+)\]", edge.label, re.I):
            for named in re.split(r",|\bor\b", guard.group(1)):
                guarded = by_id.get(named.strip())
                if guarded and guarded.label != guarded.id:
                    problems.append(f"{name} guards on the id {guarded.id}: name the state by its label, {guarded.label}")
    for node in diagram.nodes:
        if kind(node) != "choice":
            continue
        exits = [edge for edge in diagram.edges if edge.source == node.id]
        if not 2 <= len(exits) <= MAX_CHOICE_EXITS:
            problems.append(f"choice {node.id} has {len(exits)} exits, a choice has 2 to {MAX_CHOICE_EXITS}")
        for edge in exits:
            if not edge.label.strip():
                problems.append(f"choice {node.id} exit to {edge.target} has no guard label")
    if len(named) > MAX_STATES:
        problems.append(f"{len(named)} states, at most {MAX_STATES}: split by phase or by entity")
    if len(diagram.edges) > MAX_TRANSITIONS:
        problems.append(f"{len(diagram.edges)} transitions, at most {MAX_TRANSITIONS}: split by phase")
    # The [*] arrows only mark entry and exit, so the ratio counts the moves between states.
    moves = [edge for edge in diagram.edges
             if by_id[edge.source].shape not in ("start", "end") and by_id[edge.target].shape not in ("start", "end")]
    if named and len(moves) > 2 * len(named):
        problems.append(f"{len(moves)} transitions between {len(named)} states: more than twice as many "
                        "usually means two state machines")
    return problems


def display(node: Node) -> str:
    """How a state reads in a message: its id, or [*] for the start or end marker."""
    return "[*]" if node.shape in ("start", "end") else node.id


def check_state_header(block_text: str) -> list[str]:
    """The legacy `stateDiagram` header, refused in favour of `stateDiagram-v2`."""
    lines = content_lines(block_text)
    if lines and lines[0][1] == "stateDiagram":
        return ["the legacy stateDiagram header: write stateDiagram-v2"]
    return []

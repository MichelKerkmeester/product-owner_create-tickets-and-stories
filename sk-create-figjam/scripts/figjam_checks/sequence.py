#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: SEQUENCE PROFILE
# ───────────────────────────────────────────────────────────────

"""A sequence diagram, held to the narrow subset the board generator draws.

The generator parses most of Mermaid's sequence grammar and then silently drops
notes, activations, every fragment (loop, alt, opt, par, critical, break),
coloured rects, boxes, numbering and participant aliases. A model holding one
of those would promise the reader something the board never shows, so each is
refused here and added afterwards through the hybrid workflow when it matters.
"""
from __future__ import annotations

import re

from .common import content_lines, id_problems, length_problems, raw_problems

MAX_PARTICIPANTS = 5
MAX_MESSAGES = 12
MIN_ID_CHARS, MAX_ID_CHARS = 3, 20
# A request, a return, and the async form of each. The rest render as one of
# these or as a line with no head, so they say nothing a reader can trust.
REFUSED_ARROWS = {
    "-x": "renders as ->>, the cross is not drawn",
    "--x": "renders as -->>, the cross is not drawn",
    "->": "has no arrowhead",
    "-->": "has no arrowhead",
    "<<->>": "is two-way, which hides which side starts: write a request and a return",
    "<<-->>": "is two-way, which hides which side starts: write a request and a return",
}
MESSAGE = re.compile(
    r"^([A-Za-z][\w]*)\s*(<<-->>|<<->>|-->>|->>|--\)|-\)|--x|-x|-->|->)"
    r"\s*([+-]?)\s*([A-Za-z][\w]*)\s*(?::\s*(.*))?$"
)
PARTICIPANT = re.compile(r"^(participant|actor)\s+(\S+?)(@\{.*\})?(?:\s+as\s+(.+))?$", re.I)
DROPPED = {
    "note": "a note", "activate": "an activation", "deactivate": "an activation", "loop": "a loop fragment",
    "alt": "an alt fragment", "else": "an alt fragment", "opt": "an opt fragment", "par": "a par fragment",
    "and": "a par fragment", "critical": "a critical fragment", "option": "a critical fragment",
    "break": "a break fragment", "rect": "a coloured rect", "box": "a participant box", "end": "a fragment end",
    "autonumber": "numbering", "link": "a link", "links": "a link", "create": "a created participant",
    "destroy": "a destroyed participant",
}


def check_sequence(block_text: str) -> tuple[list[str], int, int]:
    """The problems with a sequence block, and how many participants and messages it holds."""
    problems = raw_problems(block_text)
    lines = content_lines(block_text)
    if not lines or lines[0][1] != "sequenceDiagram":
        return problems + ["a sequence diagram starts with the line sequenceDiagram"], 0, 0
    declared, used, order, messages, dropped = [], set(), {}, 0, set()
    for number, text in lines[1:]:
        first = text.split()[0].lower()
        if first == "title":
            continue
        participant = PARTICIPANT.match(text)
        if participant:
            keyword, name, typed, alias = participant.groups()
            if keyword.lower() == "actor":
                problems.append(
                    f"line {number}: actor {name} renders as the same rectangle as a participant: "
                    "write participant"
                )
            if typed:
                problems.append(
                    f"line {number}: {name} carries a type annotation, which renders no differently: drop it"
                )
            if alias:
                problems.append(f"line {number}: {name} carries the alias {alias.strip()}, which the generator drops: "
                                "the id is what the board shows, so make the id readable")
            if name not in declared:
                declared.append(name)
            continue
        if first in DROPPED:
            if first not in dropped:
                problems.append(f"line {number}: {DROPPED[first]} is dropped by the generator: "
                                "draw it afterwards through the hybrid workflow")
                dropped.add(first)
            continue
        message = MESSAGE.match(text)
        if not message:
            problems.append(f"line {number} is outside the sequence subset the generator draws: {text!r}")
            continue
        source, arrow, activation, target, label = message.groups()
        messages += 1
        for name in (source, target):
            used.add(name)
            order.setdefault(name, number)
        if arrow in REFUSED_ARROWS:
            problems.append(f"line {number}: the arrow {arrow} {REFUSED_ARROWS[arrow]}: "
                            "write ->> for a request, -->> for a return, -) or --) when it is async")
        if activation:
            problems.append(f"line {number}: the {activation} after the arrow is an activation, which is dropped")
        label = (label or "").strip()
        if not label:
            problems.append(f"line {number}: the message {source} to {target} has no label")
        if ";" in label:
            problems.append(f"line {number}: the label holds a semicolon, which the generator turns into a full stop")
        problems += length_problems(f"line {number}: the message", label)
    participants = declared + sorted(used - set(declared), key=lambda name: order[name])
    for name in participants:
        problems += participant_problems(name)
    if len(participants) >= 3:
        for name in participants:
            if name not in declared:
                problems.append(f"participant {name} is not declared: with three or more participants, "
                                "declare each one so the board keeps their order")
    for name in declared:
        if name not in used:
            problems.append(f"participant {name} sends and receives nothing")
    if messages == 0:
        problems.append("the diagram has no message")
    if len(participants) > MAX_PARTICIPANTS:
        problems.append(f"{len(participants)} participants, at most {MAX_PARTICIPANTS}: split the sequence")
    if messages > MAX_MESSAGES:
        problems.append(f"{messages} messages, at most {MAX_MESSAGES}: split into a happy path and a detail")
    return problems, len(participants), messages


def participant_problems(name: str) -> list[str]:
    """A participant id that is reserved, malformed or too terse to read on the board."""
    problems = id_problems(name, "participant id")
    if problems:
        return problems
    if not MIN_ID_CHARS <= len(name) <= MAX_ID_CHARS or re.fullmatch(r"[a-z]\d*", name):
        problems.append(f"participant id {name} is what the board shows: write a readable name of "
                        f"{MIN_ID_CHARS} to {MAX_ID_CHARS} characters, such as AuthServer")
    return problems

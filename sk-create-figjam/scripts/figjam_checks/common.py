#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: RULES EVERY FIGJAM DIAGRAM SHARES
# ───────────────────────────────────────────────────────────────

"""What every diagram kind holds to, whatever its grammar, and the FigJam palette.

Figma's diagram guidance sets a handful of constraints on every kind the board
generator draws: no emoji, no HTML, no literal `\\n`, no reserved word as an id
and no underscore in one. The emoji ranges and the reserved words are adapted
from diagram-codebase (MIT), which lints Mermaid against the same generator.

The palette is FigJam's own. A colour the board recognises as a palette swatch
can be recoloured from FigJam's colour picker, so the check refuses any other
hex. `references/style-guide.md` records each pair and why it was chosen, and
the self-test recomputes that record's contrast numbers from these values.
"""
from __future__ import annotations

import re

MAX_LABEL_CHARS = 40
NEEDS_QUOTES = re.compile(r"[():/]")
CAMEL_CASE_ID = re.compile(r"[A-Za-z][A-Za-z0-9]*")
RESERVED_IDS = {"end", "subgraph", "graph"}
MERMAID_KEYWORDS = {"style", "class", "classdef", "click", "default", "flowchart", "direction", "linkstyle"}
EMOJI = re.compile(
    "[\U0001f000-\U0001faff\U0001fc00-\U0001fffd☀-➿⌀-⏿⬀-⯿"
    "↔-↙↩↪‼⁉™ℹⓂ©®"
    "▪▫▶◀◻-◾〰〽㊗㊙︀-️‍⃣"
    "\U000e0020-\U000e007f]"
)
# Symbols the ranges above cover that render as plain text unless a variation
# selector asks for the emoji form, which the ranges still catch on its own.
TEXT_SYMBOLS = set("™©®✓✔✗⌘↔↕ℹ")
# An opening, closing or self-closing tag. An arrow such as `<-->` never matches,
# because a tag name starts with a letter.
HTML_TAG = re.compile(r"</?[A-Za-z][A-Za-z0-9]*(?:\s[^<>]*)?/?>")
EMPHASIS = re.compile(r"\*\*|__\S|(?<![*\w])\*[^*\s][^*]*\*(?![*\w])|`")
STATE_GRAMMAR = re.compile(r"\[\*\]|<<(?:choice|fork|join)>>", re.I)
TYPE_DIRECTIVE = re.compile(r"^\s*%%\s*type\s*:\s*([A-Za-z-]+)\s*$", re.M)
FOCUS_DIRECTIVE = re.compile(r"^\s*%%\s*focus\s*:\s*(.*?)\s*$", re.I | re.M)
BECAUSE = re.compile(r"\s+because(?:\s+|$)", re.I)
# The key entry reads `In focus: <reason>`, and a key entry holds 40 characters, so the reason holds the rest.
FOCUS_REASON_MAX = MAX_LABEL_CHARS - len("In focus: ")

# FigJam's light fills, each with the darker stroke FigJam pairs it with. Dark
# text reads on every one of them. The saturated fills are left out: FigJam
# sets white text on them, Mermaid cannot set a text colour, and which colour
# the generator uses on a saturated fill was never observed.
ACCENT_PAIRS = {
    "#cdf4d3": "#66d575",  # light green
    "#c6faf6": "#5ad8cc",  # light teal
    "#c2e5ff": "#3dadff",  # light blue
    "#dcccff": "#874fff",  # light violet
    "#ffc2ec": "#f849c1",  # light pink
    "#ffcdc2": "#ff7556",  # light red
    "#ffe0c2": "#ff9e42",  # light orange
    "#ffecbd": "#ffc943",  # light yellow
    "#d9d9d9": "#b3b3b3",  # light gray
}
PAIRED_FILL = {stroke: fill for fill, stroke in ACCENT_PAIRS.items()}
# A lane is a container, never content, so it takes one neutral tint that never
# counts as the accent. Figma names this pair for a diagram's container.
LANE_PAIR = ("#f5f5f5", "#b3b3b3")
CHARCOAL = "#1e1e1e"
CANVAS = "#ffffff"


def statements(block_text: str) -> list[str]:
    """Split a block into statements on newlines and semicolons outside quotes, leaving out `%%` comments."""
    found = []
    for line in block_text.splitlines():
        if line.strip().startswith("%%"):
            continue
        current, quoted = "", False
        for char in line:
            if char == '"':
                quoted = not quoted
            if char == ";" and not quoted:
                found.append(current.strip())
                current = ""
            else:
                current += char
        found.append(current.strip())
    return [statement for statement in found if statement]


def content_lines(block_text: str) -> list[tuple[int, str]]:
    """Return (line number, stripped text) for every line that is not blank or a `%%` comment."""
    found = []
    for number, line in enumerate(block_text.splitlines(), 1):
        text = line.strip()
        if text and not text.startswith("%%"):
            found.append((number, text))
    return found


def focus_reason(value: str) -> tuple[str, str]:
    """A `%% focus:` value as the id it names and the reason after ` because `, empty when it gives none."""
    target, _, reason = BECAUSE.sub("\0", value, count=1).partition("\0")
    return target.strip(), reason.strip()


def focus_line_problems(block_text: str) -> list[str]:
    """A `%% focus: <id> because <reason>` line whose reason is missing or too long for the key."""
    problems = []
    for value in FOCUS_DIRECTIVE.findall(block_text):
        if not BECAUSE.search(value):
            continue
        target, reason = focus_reason(value)
        if not reason:
            problems.append(f"%% focus: {target} because names no reason: write the reason after because or drop because")
        elif len(reason) > FOCUS_REASON_MAX:
            problems.append(f"the focus reason runs to {len(reason)} characters, at most {FOCUS_REASON_MAX}, so the key's "
                            f"In focus: <reason> fits 40")
    return problems


def type_directive(block_text: str) -> str:
    """The kind a `%% type:` comment line names, lowercased, or an empty string when none does."""
    match = TYPE_DIRECTIVE.search(block_text)
    return match.group(1).lower() if match else ""


def raw_problems(block_text: str) -> list[str]:
    """Emoji, markup and a literal backslash-n, read from the raw block because a parser strips them."""
    problems = []
    # A state diagram's [*] marker and its <<choice>> stereotypes are grammar, not markup.
    text = STATE_GRAMMAR.sub("", "\n".join(statements(block_text)))
    emoji = sorted({char for char in EMOJI.findall(text) if char not in TEXT_SYMBOLS})
    if emoji:
        problems.append(f"the block carries an emoji ({' '.join(emoji)}), which the board generator rejects")
    if HTML_TAG.search(text) or EMPHASIS.search(text):
        problems.append("the block carries markup, which the board generator drops: write plain labels")
    if "\\n" in text:
        problems.append("the block carries a literal \\n, which the board generator rejects: split the label instead")
    return problems


def id_problems(node_id: str, what: str = "node id") -> list[str]:
    """Why an id cannot stand on the board: reserved, a Mermaid keyword, an underscore or not camelCase."""
    if node_id.lower() in RESERVED_IDS:
        return [f"{what} {node_id} is reserved by the board generator"]
    if node_id.lower() in MERMAID_KEYWORDS:
        return [f"{what} {node_id} is a Mermaid keyword"]
    if "_" in node_id:
        return [f"{what} {node_id} holds an underscore, which breaks connector routing: use camelCase"]
    if not CAMEL_CASE_ID.fullmatch(node_id):
        return [f"{what} {node_id} is not camelCase: letters and digits only, starting with a letter"]
    return []


def length_problems(owner: str, label: str) -> list[str]:
    """A label that breaks its line or runs past MAX_LABEL_CHARS."""
    problems = []
    if "\n" in label:
        problems.append(f"{owner} label carries a line break")
    if len(label) > MAX_LABEL_CHARS:
        problems.append(f"{owner} label runs to {len(label)} characters, at most {MAX_LABEL_CHARS}")
    return problems


def hex_colour(value: str) -> str:
    """A hex colour in lower case, with a three-digit shorthand spelled out to six digits."""
    value = value.lower()
    if re.fullmatch(r"#[0-9a-f]{3}", value):
        return "#" + "".join(digit * 2 for digit in value[1:])
    return value


def relative_luminance(value: str) -> float:
    """The WCAG relative luminance of a six-digit hex colour."""
    channels = []
    for i in (1, 3, 5):
        channel = int(value[i:i + 2], 16) / 255
        channels.append(channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4)
    red, green, blue = channels
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast(first: str, second: str) -> float:
    """The WCAG contrast ratio between two six-digit hex colours."""
    lighter, darker = sorted((relative_luminance(first), relative_luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)

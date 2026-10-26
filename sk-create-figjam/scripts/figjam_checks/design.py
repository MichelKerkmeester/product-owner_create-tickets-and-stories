#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: BOARD DESIGN
# ───────────────────────────────────────────────────────────────

"""The style a composed board is drawn in: the composer's built-in design, the design file and its floors.

`assets/compose-board.js` carries a built-in design, the values an empty theme draws. `assets/figjam-design.md`
is the copy a team edits: prose that says what each token means, then one fenced json block. `resolve` reads
that block over the built-in design token by token and holds the result to the floors every board keeps:
text that reads on its fill, an accent that wins by hue, contrast and weight, kinds a reader can tell apart
and type sizes inside their bounds. A token that is unknown, of the wrong type or under a floor falls back to
its built-in value, and a block that cannot be read at all falls back whole. Each fallback carries a warning
that names it, so a bad edit never stops a board and never passes in silence. `theme` is what the composer is
sent: only the tokens that differ from the built-in design.
"""
from __future__ import annotations

import colorsys
import copy
import hashlib
import json
import re
from pathlib import Path

from .common import CANVAS, contrast

PACKET = Path(__file__).resolve().parents[2]
COMPOSER = PACKET / "assets" / "compose-board.js"
DESIGN_FILE = PACKET / "assets" / "figjam-design.md"
SCHEMA_VERSION = 1
# The groups a team edits, and the two it reads: FigJam's own pairs and tints are named, never changed.
EDITABLE = ("role", "accent", "kind", "type", "line", "zone", "key")
READ_ONLY = ("swatch", "tint")
FENCE = re.compile(r"^```json[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)
LITERAL = re.compile(r"""\s*(?:(?P<text>'(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")|(?P<number>-?\d+(?:\.\d+)?)"""
                     r"""|(?P<word>[A-Za-z_$][\w$]*)|(?P<mark>[{}\[\],:])|(?P<other>\S))""")
HEX = re.compile(r"#[0-9A-F]{6}")
MAX_WORDS = 40
TEXT_GATE, MARK_GATE, MIN_HUE_APART, SATURATED = 4.5, 3.0, 45, 0.2
# An async message also carries an open head and a lifeline is a guide, so those two colours only have to show on
# white, where every connector's own colour holds the mark gate.
SHOW_GATE = 2.0
# The router keeps a zone's 96 px head clear of runs for a title up to this size, and a zone name is never smaller
# than a node label, so both stop here. A zone name at 28 px already pushes an edge through a zone it does not join.
ZONE_TYPE_MAX = 24
# Kinds drawn as a bare dot or bar with no label inside, which only their fill shows on the white board.
DOT_KINDS = ("initial", "final", "merge", "fork")
# The ring around an end state is the heaviest outline after the accent's, so the accent stays above it.
RING_WEIGHT = 6
# Two kinds that share a shape and an outline read apart in greyscale only when their fills differ by this much
# luma or more. FigJam's light pairs sit within 12 of one another, so those kinds differ by outline instead.
GREY_STEP = 25
# The kinds each type can draw on one board. Two of them never share a shape, a pair and an outline, so a
# reader who cannot read the label still tells them apart.
TYPE_KINDS = {
    "a user flow": ("start", "screen", "decision", "success", "exit", "error", "merge", "datastore", "subprocess", "io"),
    "a process": ("start", "step", "decision", "success", "exit", "error", "merge", "datastore", "subprocess", "io"),
    "an architecture": ("client", "gateway", "service", "queue", "datastore", "external"),
    "a state diagram": ("initial", "final", "firstState", "state", "finalState", "choice", "fork"),
    "a sequence": ("participant",),
    "an ER diagram": ("entity",),
    "a gantt chart": ("planned", "active", "done", "crit", "milestone"),
}


# ───────────────────────────────────────────────────────────────
# 1. THE BUILT-IN DESIGN
# ───────────────────────────────────────────────────────────────

def js_literal(source: str, name: str) -> object:
    """The value of `const NAME = ...` in the composer, read as the plain object, array or scalar it is."""
    start = source.index(f"const {name} = ") + len(f"const {name} = ")
    tokens = LITERAL.finditer(source, start)

    def value(token: re.Match) -> object:
        kind, text = token.lastgroup, token.group(token.lastgroup)
        if kind == "other":
            raise ValueError(f"const {name} holds {text!r}, which is no plain literal")
        if kind == "text":
            return text[1:-1].replace("\\'", "'") if text[0] == "'" else json.loads(text)
        if kind == "number":
            return float(text) if "." in text else int(text)
        if kind == "word":
            return {"true": True, "false": False, "null": None}[text]
        if text == "[":
            items = []
            for inner in tokens:
                if inner.group("mark") == "]":
                    return items
                if inner.group("mark") != ",":
                    items.append(value(inner))
        found = {}
        for inner in tokens:
            if inner.group("mark") == "}":
                return found
            if inner.group("mark") == ",":
                continue
            key = inner.group("word") or inner.group("text")[1:-1]
            next(tokens)
            found[key] = value(next(tokens))
        raise ValueError(f"const {name} never closes")

    return value(next(tokens))


def built_in(source: str | None = None) -> dict:
    """The composer's built-in design, with its swatches, tints and the shape and outline of every kind."""
    source = source if source is not None else COMPOSER.read_text(encoding="utf-8")
    design = js_literal(source, "D")
    design["swatch"] = js_literal(source, "SWATCH")
    design["tint"] = js_literal(source, "TINT")
    design["shape"] = js_literal(source, "SHAPES")
    design["outline"] = js_literal(source, "OUTLINE")
    return design


# ───────────────────────────────────────────────────────────────
# 2. READING THE DESIGN FILE
# ───────────────────────────────────────────────────────────────

def read_block(text: str) -> tuple[dict | None, str]:
    """The design file's one json block, or None with the reason it cannot be read."""
    name = DESIGN_FILE.name
    blocks = FENCE.findall(text.replace("\r\n", "\n").replace("\r", "\n"))
    if len(blocks) != 1:
        return None, f"{name} holds {len(blocks)} json blocks, and a design is exactly one"
    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError as err:
        return None, f"the json block in {name} does not parse: {err.msg} on line {err.lineno} of the block"
    if not isinstance(data, dict):
        return None, f"the json block in {name} is not an object"
    version = (data.get("meta") or {}).get("schemaVersion") if isinstance(data.get("meta"), dict) else None
    if version != SCHEMA_VERSION:
        return None, f"{name} names schemaVersion {version!r}, and this composer reads {SCHEMA_VERSION}"
    return data, ""


def dotted(path: tuple) -> str:
    return ".".join(str(part) for part in path)


def palette_colours(design: dict) -> set[str]:
    """Every colour FigJam's pairs hold: a line may take any of them and stays on the palette."""
    return {colour.upper() for pair in design["swatch"].values() for colour in pair}


def encodes(value: str) -> bool:
    """Whether a string is text the board can carry: a lone surrogate from a json escape is not."""
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def leaf_problem(path: tuple, value: object, design: dict) -> str:
    """Why one token's value cannot stand, judged on its own, or an empty string when it can."""
    group, last = path[0], path[-1]
    if group == "role" or path == ("accent", "pair"):
        return "" if value in design["swatch"] else f"names {value!r}, which is no FigJam swatch"
    if group == "kind" and last == "role":
        return "" if value in design["role"] else f"names {value!r}, which is no role"
    if path == ("key", "tint"):
        return "" if value in design["tint"] else f"names {value!r}, which is no FigJam section tint"
    if path == ("zone", "cycle"):
        unknown = [t for t in value if not isinstance(t, str) or t not in design["tint"]]
        if unknown:
            return f"names {', '.join(map(str, unknown))}, which are no FigJam section tints"
        return "" if len(value) >= 2 and len(set(value)) == len(value) else "needs two or more tints, each once"
    if group == "line" and last != "weight":
        return "" if isinstance(value, str) and value.upper() in palette_colours(design) \
            else f"is {value!r}, which is no colour of FigJam's pairs"
    if isinstance(value, str) and not encodes(value):
        return "holds a character that is not text"
    if path == ("type", "family"):
        return "" if 0 < len(value) <= 64 else "is empty or longer than 64 characters"
    if isinstance(value, str):
        if not value.strip() or "\n" in value or len(value) > MAX_WORDS:
            return f"is empty, breaks its line or runs past {MAX_WORDS} characters"
        return ""
    if isinstance(value, int) and not isinstance(value, bool) and value <= 0:
        return "is not a positive number"
    return ""


def overlay(base: dict, data: dict, path: tuple, design: dict, warnings: list[str]) -> None:
    """Lay the file's tokens over the built-in ones in place, keeping the built-in value of any that cannot stand.

    `base` is the part of `design` that `path` names, and `design` is the whole of it, which a token that names
    a swatch, a tint or a role is judged against.
    """
    for key, value in data.items():
        here = path + (key,)
        if key not in base:
            warnings.append(f"{dotted(here)} is no token this composer reads, so it was left out")
            continue
        old = base[key]
        if isinstance(old, dict):
            if isinstance(value, dict):
                overlay(old, value, here, design, warnings)
            else:
                warnings.append(f"{dotted(here)} should be an object, so it kept its built-in tokens")
            continue
        same_kind = (isinstance(value, bool) == isinstance(old, bool)
                     and (type(value) is type(old) or (isinstance(old, int) and isinstance(value, int))))
        if not same_kind:
            warnings.append(f"{dotted(here)} should be {type(old).__name__}, not {type(value).__name__}, "
                            f"so it fell back to {json.dumps(old)}")
            continue
        problem = leaf_problem(here, value, design)
        if problem:
            warnings.append(f"{dotted(here)} {problem}, so it fell back to {json.dumps(old)}")
            continue
        base[key] = value



# ───────────────────────────────────────────────────────────────
# 3. FLOORS
# ───────────────────────────────────────────────────────────────

def hue(colour: str) -> tuple[float, float]:
    """A colour's hue in degrees and its saturation."""
    red, green, blue = (int(colour[i:i + 2], 16) / 255 for i in (1, 3, 5))
    degrees, _, saturation = colorsys.rgb_to_hls(red, green, blue)
    return degrees * 360, saturation


def apart(first: str, second: str) -> float:
    """How many degrees of hue lie between two colours."""
    gap = abs(hue(first)[0] - hue(second)[0]) % 360
    return min(gap, 360 - gap)


def grey(colour: str) -> float:
    """A colour's luma, the lightness it keeps in greyscale."""
    red, green, blue = (int(colour[i:i + 2], 16) for i in (1, 3, 5))
    return 0.299 * red + 0.587 * green + 0.114 * blue


def used_roles(design: dict) -> dict[str, list[str]]:
    """Each role some kind draws, with the kinds that draw it, and the marker role the sequence pins draw."""
    roles: dict[str, list[str]] = {}
    for kind, token in design["kind"].items():
        if "role" in token:
            roles.setdefault(token["role"], []).append(kind)
    roles.setdefault("marker", []).append("the step pins")
    return roles


def floors(design: dict) -> list[tuple[str, list[tuple]]]:
    """Every floor the design misses, each with the token paths that together miss it."""
    found = []
    swatch, accent = design["swatch"], design["accent"]
    stroke = swatch[accent["pair"]][1]
    for role, kinds in used_roles(design).items():
        fill, _, text = swatch[design["role"][role]]
        if contrast(text, fill) < TEXT_GATE:
            found.append((f"text on the {role} fill measures {contrast(text, fill):.2f}:1, under {TEXT_GATE}:1",
                          [("role", role)]))
        if design["role"][role] == accent["pair"]:
            found.append((f"the {role} role draws {accent['pair']}, the accent's own pair", [("role", role), ("accent", "pair")]))
        role_stroke = swatch[design["role"][role]][1]
        if hue(role_stroke)[1] > SATURATED and apart(stroke, role_stroke) < MIN_HUE_APART:
            found.append((f"the accent sits under {MIN_HUE_APART} degrees of hue from the {role} role, at {apart(stroke, role_stroke):.0f}",
                          [("role", role), ("accent", "pair")]))
    if contrast(stroke, CANVAS) < MARK_GATE:
        found.append((f"the accent's stroke measures {contrast(stroke, CANVAS):.2f}:1 on white, under {MARK_GATE}:1",
                      [("accent", "pair")]))
    for tint in design["zone"]["cycle"]:
        colour = design["tint"][tint]
        if hue(colour)[1] > SATURATED and apart(stroke, colour) < MIN_HUE_APART:
            found.append((f"the {tint} zone tint sits under {MIN_HUE_APART} degrees of hue from the accent, at {apart(stroke, colour):.0f}",
                          [("zone", "cycle"), ("accent", "pair")]))
    if design["key"]["tint"] in design["zone"]["cycle"]:
        found.append((f"the zone cycle holds {design['key']['tint']}, the key's own tint", [("zone", "cycle"), ("key", "tint")]))
    key_tint = design["tint"][design["key"]["tint"]]
    if hue(key_tint)[1] > SATURATED and apart(stroke, key_tint) < MIN_HUE_APART:
        found.append((f"the key's {design['key']['tint']} tint sits under {MIN_HUE_APART} degrees of hue from the accent, at "
                      f"{apart(stroke, key_tint):.0f}", [("key", "tint"), ("accent", "pair")]))
    for name in ("color", "async", "lifeline"):
        colour = design["line"][name]
        if hue(colour)[1] > SATURATED and apart(stroke, colour) < MIN_HUE_APART:
            found.append((f"line.{name} sits under {MIN_HUE_APART} degrees of hue from the accent, at {apart(stroke, colour):.0f}",
                          [("line", name), ("accent", "pair")]))
        gate = MARK_GATE if name == "color" else SHOW_GATE
        if contrast(colour, CANVAS) < gate:
            found.append((f"line.{name} measures {contrast(colour, CANVAS):.2f}:1 on white, under {gate:g}:1",
                          [("line", name)]))
    for kind in DOT_KINDS:
        role = design["kind"][kind]["role"]
        fill = swatch[design["role"][role]][0]
        if contrast(fill, CANVAS) < MARK_GATE:
            found.append((f"the {kind} dot draws the {role} fill at {contrast(fill, CANVAS):.2f}:1 on white, under {MARK_GATE:g}:1",
                          [("kind", kind, "role"), ("role", role)]))
    if not RING_WEIGHT < accent["node"] <= 16:
        found.append((f"the accent outline is {accent['node']} px, and it must outweigh the {RING_WEIGHT} px ring and stay "
                      f"at 16 or under", [("accent", "node")]))
    if not design["line"]["weight"] < accent["message"] <= 8:
        found.append((f"the accent message is {accent['message']} px against {design['line']['weight']} px lines, and it "
                      f"must be heavier and stay at 8 or under", [("accent", "message"), ("line", "weight")]))
    if not 1 <= design["line"]["weight"] <= 4:
        found.append((f"lines are {design['line']['weight']} px, outside 1 to 4", [("line", "weight")]))
    for name, kinds in TYPE_KINDS.items():
        seen: dict[tuple, str] = {}
        for kind in kinds:
            role = design["kind"][kind]["role"]
            look = (design["shape"].get(kind, "ROUNDED_RECTANGLE"), design["role"][role], design["outline"].get(kind))
            if look in seen:
                other = seen[look]
                found.append((f"{other} and {kind} draw one shape in one pair on {name}",
                              [("kind", other, "role"), ("kind", kind, "role"),
                               ("role", design["kind"][other]["role"]), ("role", role)]))
            seen.setdefault(look, kind)
        # Kinds in two pairs still read as one in greyscale when nothing but the colour sets them apart.
        for i, first in enumerate(kinds):
            for second in kinds[i + 1:]:
                looks = [(design["shape"].get(k, "ROUNDED_RECTANGLE"), design["outline"].get(k),
                          design["role"][design["kind"][k]["role"]]) for k in (first, second)]
                gap = abs(grey(design["swatch"][looks[0][2]][0]) - grey(design["swatch"][looks[1][2]][0]))
                if looks[0][:2] == looks[1][:2] and looks[0][2] != looks[1][2] and gap < GREY_STEP:
                    found.append((f"{first} and {second} on {name} share a shape and an outline and their fills sit {gap:.0f} "
                                  f"apart in greyscale, under {GREY_STEP}, so they differ only by colour",
                                  [("kind", first, "role"), ("kind", second, "role"),
                                   ("role", design["kind"][first]["role"]), ("role", design["kind"][second]["role"])]))
    size = design["type"]
    bounds = [
        (size["small"] >= 14, "small type is under 14 px", [("type", "small")]),
        (size["small"] <= size["label"] <= size["node"], "label type is smaller than small type or larger than node type",
         [("type", "label"), ("type", "small"), ("type", "node")]),
        (size["small"] <= size["field"] <= size["node"], "field type is smaller than small type or larger than node type",
         [("type", "field"), ("type", "small"), ("type", "node")]),
        (16 <= size["node"] <= ZONE_TYPE_MAX, f"node type is outside 16 to {ZONE_TYPE_MAX} px", [("type", "node")]),
        (size["node"] <= size["zone"] <= ZONE_TYPE_MAX,
         f"zone type is smaller than node type or over {ZONE_TYPE_MAX} px", [("type", "zone"), ("type", "node")]),
        (size["zone"] <= size["subtitle"] <= size["title"], "the subtitle is smaller than zone type or larger than the title",
         [("type", "subtitle"), ("type", "zone"), ("type", "title")]),
        (2 * size["node"] <= size["title"] <= 128, "the title is under twice node type or over 128 px",
         [("type", "title"), ("type", "node")]),
    ]
    found += [(problem, paths) for ok, problem, paths in bounds if not ok]
    return found


def get(design: dict, path: tuple) -> object:
    for part in path:
        design = design[part]
    return design


def put(design: dict, path: tuple, value: object) -> None:
    for part in path[:-1]:
        design = design[part]
    design[path[-1]] = copy.deepcopy(value)


# ───────────────────────────────────────────────────────────────
# 4. RESOLVE AND THEME
# ───────────────────────────────────────────────────────────────

def resolve(text: str | None = None, base: dict | None = None) -> tuple[dict, list[str]]:
    """The design a board is drawn in, and a warning for every token that fell back.

    `text` is the design file's text, read from `assets/figjam-design.md` when left out. The result holds every
    built-in token, so the floors and the composer read one complete design. A design file that cannot be read
    for any reason, including one no rule below foresaw, falls back whole, so an edit never stops a board.
    """
    base = base if base is not None else built_in()
    try:
        return read_design(text, base)
    except Exception as err:  # noqa: BLE001 - every failure is a design the board cannot use, and it must still draw
        return dict(copy.deepcopy(base), meta={"name": "built-in"}), [
            f"{DESIGN_FILE.name} could not be read ({type(err).__name__}: {err}), so the board is drawn in the built-in design"]


def read_design(text: str | None, base: dict) -> tuple[dict, list[str]]:
    """`resolve` without its guard: the file's tokens over the built-in ones, held to the floors."""
    if text is None:
        if not DESIGN_FILE.is_file():
            return dict(copy.deepcopy(base), meta={"name": "built-in"}), [
                f"{DESIGN_FILE.name} is missing, so the board is drawn in the built-in design"]
        text = DESIGN_FILE.read_text(encoding="utf-8")
    data, reason = read_block(text)
    if data is None:
        return dict(copy.deepcopy(base), meta={"name": "built-in"}), [f"{reason}, so the board is drawn in the built-in design"]
    design = copy.deepcopy(base)
    warnings = []
    for group, value in data.items():
        if group == "meta":
            continue
        if group in READ_ONLY:
            if value != base[group]:
                warnings.append(f"{group} lists FigJam's own colours, which a design names and never changes, "
                                f"so the built-in {group} stands")
            continue
        if group not in EDITABLE:
            warnings.append(f"{group} is no group this composer reads, so it was left out")
            continue
        if not isinstance(value, dict):
            warnings.append(f"{group} should be an object, so it kept its built-in tokens")
            continue
        overlay(design[group], value, (group,), design, warnings)
    # A missed floor reverts the first token on it the file changed, and the floors are measured again, so a token
    # that only missed a floor beside another one stands once that one is back. Every pass reverts a changed token,
    # so the loop ends once every floor holds or nothing the file changed is left on a missed one.
    wanted, reverted = copy.deepcopy(design), {}
    while True:
        missed = floors(design)
        changed = [(problem, path) for problem, paths in missed for path in paths if get(design, path) != get(base, path)]
        if not changed:
            warnings += [f"the built-in design misses a floor: {problem}" for problem, _ in missed]
            break
        problem, path = changed[0]
        reverted[path] = f"{dotted(path)} fell back to {json.dumps(get(base, path))}: {problem}"
        put(design, path, get(base, path))
    # A token reverted early may stand once a later one is back, so each is tried again and kept where every floor holds.
    for path in list(reverted):
        trial = copy.deepcopy(design)
        put(trial, path, get(wanted, path))
        if not floors(trial):
            design = trial
            del reverted[path]
    warnings += list(reverted.values())
    meta = data.get("meta") if isinstance(data.get("meta"), dict) else {}
    name = meta.get("name") or "unnamed"
    if not isinstance(name, str) or not name.strip() or "\n" in name or len(name) > MAX_WORDS or not encodes(name):
        warnings.append(f"meta.name is empty, breaks its line, runs past {MAX_WORDS} characters or holds a character that "
                        f"is not text, so the design is named unnamed")
        name = "unnamed"
    design["meta"] = {"name": name, "schemaVersion": SCHEMA_VERSION}
    return design, warnings


def difference(now: object, then: object) -> object:
    """The tokens of `now` that differ from `then`, keeping their nesting, or None when nothing differs."""
    if isinstance(now, dict) and isinstance(then, dict):
        found = {key: difference(value, then.get(key)) for key, value in now.items()}
        found = {key: value for key, value in found.items() if value is not None}
        return found or None
    return None if now == then else now


def theme(design: dict, base: dict | None = None) -> dict:
    """What the composer is sent: the editable tokens that differ from its built-in design, and the design's id."""
    base = base if base is not None else built_in()
    found = difference({group: design[group] for group in EDITABLE}, {group: base[group] for group in EDITABLE}) or {}
    if found:
        digest = hashlib.sha1(json.dumps(found, sort_keys=True).encode()).hexdigest()[:8]
        found["id"] = f"{design['meta']['name']} {digest}"
    return found


def compact(value: object) -> str:
    """JSON with no space after a comma or a colon, the form the code carries."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


# ───────────────────────────────────────────────────────────────
# 5. WHAT A DRAWN BOARD SHOWS
# ───────────────────────────────────────────────────────────────

def family(name: str) -> str:
    """The hue a swatch or a tint is named for: lightBlue and blue are both blue."""
    return name.replace("light", "").lower()


def colour_names(design: dict) -> tuple[dict[str, str], dict[str, str]]:
    """Each swatch fill and each tint by its hex, so a drawn fill can be read back as the name it was drawn from."""
    fills = {pair[0].lower(): name for name, pair in design["swatch"].items()}
    tints = {colour.lower(): name for name, colour in design["tint"].items()}
    return fills, tints


def key_order(design: dict) -> list[str]:
    """The order of the key: every kind as the design lists them, then the lines, the arrows, the pin and the focus."""
    return [k for k in design["kind"] if k != "focus"]

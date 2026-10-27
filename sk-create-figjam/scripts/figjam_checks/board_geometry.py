#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: BOARD GEOMETRY CHECKS
# ───────────────────────────────────────────────────────────────

"""Measure what the composer draws, from a run against a recording stand-in for Figma.

`compose-trace.mjs` runs the filled composer code and reports every box and every
connector end. The checks here read that report: whether a line crosses a box it
does not belong to, whether two edges share a magnet while another is free, whether an edge rides a zone's border, whether zones lie on
one another, whether a card holds its lines, whether a lane stays as tall as
its content, whether a line or a label meets a zone's title, whether edges
cross, share a stretch long enough to carry a label, or sit under another
edge's label, and whether a sequence message ends in the arrow its Mermaid form
names. FigJam routes an elbowed connector itself, so a line's path is
estimated: it leaves a magnet straight out, turns at right angles, never doubles
back and arrives straight in, and the cheapest such path stands in for the real
one. The estimate is a model of the router, so a pass here says the layout leaves
the router no reason to cross a box, and only a read-back of the board proves what
FigJam drew.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from .common import CANVAS, contrast

TRACE = Path(__file__).resolve().parent.parent / "compose-trace.mjs"
STEP = 48
DIRECTIONS = {"LEFT": (-1, 0), "RIGHT": (1, 0), "TOP": (0, -1), "BOTTOM": (0, 1)}
# The composer's spacing constants, which the checks measure the board against.
ZONE_HEAD, ZONE_PAD, CROSS_GAP, CARD_PAD, PARAGRAPH, FIELD_LINE = 96, 48, 80, 48, 4, 24
# The composer snaps every box to an 8 px grid, so an edge it places sits within one step of where it is meant to.
GRID_STEP = 8
# A zone's title sits 32 px in from its corner. A label is its text plus a pad, 24 px tall, and sits on
# the middle of the line it names. Two edges may share their first stub, and nothing longer.
# A label's width is its characters at the trace's Inter proportion of the label size, which `use_design` sets.
# A node's own text wraps at a narrower average, NODE_WIDTH of the node size: at that measure the wraps match the
# ones rendered boards show, where the label proportion flags labels that fit.
# FigJam's own wrap runs narrower still on lowercase words: a rendered board fitted 19 characters where NODE_WIDTH
# fits 17, so a label is also read at NODE_NARROW and a stranded word at either measure is reported.
CHAR_WIDTH, NODE_WIDTH, NODE_NARROW = 0.56, 0.5, 0.45
TITLE_INSET, TITLE_GAP, LABEL_HEIGHT, LABEL_PAD, LABEL_CHAR, SHARE_MAX = 32, 8, 24, 16, 18 * CHAR_WIDTH, 56
NODE_CHAR = 20 * NODE_WIDTH
NODE_NARROW_CHAR = 20 * NODE_NARROW
# A FigJam sticky is a fixed square, and a single sticky keeps one sticky gap from its node, as the hybrid
# workflow sets them. Its sides are tried in the order that workflow names.
STICKY, STICKY_GAP = 240, 64
STICKY_SIDES = ("right", "below", "above", "left")
# The shapes whose text the composer fits into the inscribed half box, so the box a trace records is never the
# width its label wraps at. A parallelogram gives up its slanted ends the same way.
ROUND_SHAPES = {"DIAMOND", "ELLIPSE", "HEXAGON", "OCTAGON"}
# A run along a zone's edge reads as part of the border when it is closer than ZONE_OUT outside it or ZONE_IN
# inside it. The gap between two zones is 48 wide, so its middle clears both borders by 24, and the zone's
# own padding is 48, so a run inside it clears the border by that much. Two runs closer than CORRIDOR on
# parallel lines read as one trunk, two closer than SIDE_BY_SIDE read as a doubled line, and a label keeps
# LABEL_CLEAR of air from every other line.
ZONE_OUT, ZONE_IN, CORRIDOR, SIDE_BY_SIDE, LABEL_CLEAR, MERGE_MAX = 16, 40, 16, 56, 8, 200
DETOUR_LIMIT = 2.0
# A dot is at most this wide. An arrow into a gantt bar lands within this many pixels of the bar's left end, and
# the arrivals on one side of a node stand SPREAD apart where the side holds them.
DOT_WIDTH, GANTT_LANDING, SPREAD = 32, 72, 24
# A choice or a milestone is a diamond at most this wide, too small to give each arrival a point of its own.
JOIN_DIAMOND = 56


def use_design(design: dict) -> None:
    """Measure boards against the design they are drawn in: its text sizes and its accent's pair and weights."""
    global LABEL_CHAR, NODE_CHAR, NODE_NARROW_CHAR, ACCENT_STROKE, ACCENT_WEIGHT, ACCENT_LINE
    LABEL_CHAR = design["type"]["label"] * CHAR_WIDTH
    NODE_CHAR = design["type"]["node"] * NODE_WIDTH
    NODE_NARROW_CHAR = design["type"]["node"] * NODE_NARROW
    ACCENT_STROKE = design["swatch"][design["accent"]["pair"]][1].lower()
    ACCENT_WEIGHT, ACCENT_LINE = design["accent"]["node"], design["accent"]["message"]


def run_trace(code: str, workdir: Path) -> dict:
    """Run filled composer code under node and return what it drew."""
    node = shutil.which("node")
    if not node:
        raise RuntimeError("node is not on PATH")
    source = workdir / "board-under-test.js"
    source.write_text(code, encoding="utf-8")
    done = subprocess.run([node, str(TRACE), str(source)], capture_output=True, text=True)
    source.unlink()
    if done.returncode:
        raise RuntimeError(done.stderr.strip() or "the trace run failed")
    return json.loads(done.stdout)


def boxes_of(drawn: dict) -> dict[str, dict]:
    """Every shape that stands for a diagram node, by its model id."""
    return {n["name"][5:]: n for n in drawn["nodes"] if n["name"].startswith("node:")}


def _side(shape: dict, end: dict) -> str:
    """The side of its node a connector end holds: its magnet or the side nearest the point it is pinned to."""
    if "magnet" in end:
        return end["magnet"]
    x, y = end["position"]["x"], end["position"]["y"]
    gaps = {"TOP": y, "BOTTOM": shape["h"] - y, "LEFT": x, "RIGHT": shape["w"] - x}
    return min(gaps, key=gaps.get)


def _point(drawn_by_id: dict, end: dict) -> tuple[tuple[float, float], tuple[int, int] | None]:
    shape = drawn_by_id[end["endpointNodeId"]]
    if "position" in end:
        x, y = end["position"]["x"], end["position"]["y"]
        # A point at the centre joins two legs at an anchor and faces no way.
        if (x, y) == (shape["w"] / 2, shape["h"] / 2):
            return (shape["x"] + x, shape["y"] + y), None
        # A point on a side arrives straight against it. One stepped in to meet a round shape's sloped side is
        # measured where its line crosses the box's own edge, since the rest lies inside the box it belongs to.
        vx, vy = DIRECTIONS[_side(shape, end)]
        x, y = (max(vx, 0) * shape["w"], y) if vx else (x, max(vy, 0) * shape["h"])
        return (shape["x"] + x, shape["y"] + y), (vx, vy)
    vx, vy = DIRECTIONS[end["magnet"]]
    return (shape["x"] + shape["w"] / 2 * (1 + vx), shape["y"] + shape["h"] / 2 * (1 + vy)), (vx, vy)


def tidy(path: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """The path without repeated points or points in the middle of a straight run."""
    kept: list[tuple[float, float]] = []
    for pt in path:
        if kept and kept[-1] == pt:
            continue
        while len(kept) > 1 and ((kept[-1][0] - kept[-2][0]) * (pt[1] - kept[-1][1])
                                 == (kept[-1][1] - kept[-2][1]) * (pt[0] - kept[-1][0])):
            kept.pop()
        kept.append(pt)
    return kept


def path_length(path: list[tuple[float, float]]) -> float:
    """The length of a right-angle path, summed leg by leg."""
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in zip(path, path[1:]))


def candidate_paths(p: tuple[float, float], v: tuple[int, int] | None, q: tuple[float, float],
                    w: tuple[int, int] | None) -> list[list[tuple[float, float]]]:
    """The cheapest right-angle paths from p, leaving along v, to q, arriving against w."""
    # Two ports closer than a stub cannot both leave and arrive straight, so the stub is dropped then.
    for step in (STEP, 0):
        a = (p[0] + v[0] * step, p[1] + v[1] * step) if v else p
        z = (q[0] + w[0] * step, q[1] + w[1] * step) if w else q
        mx, my = (a[0] + z[0]) / 2, (a[1] + z[1]) / 2
        paths = []
        for middle in ([(z[0], a[1])], [(a[0], z[1])], [(mx, a[1]), (mx, z[1])], [(a[0], my), (z[0], my)]):
            raw = [p, a, *middle, z, q]
            path = [pt for i, pt in enumerate(raw) if i == 0 or pt != raw[i - 1]]
            backs = any((path[i][0] - path[i - 1][0]) * (path[i - 1][0] - path[i - 2][0])
                        + (path[i][1] - path[i - 1][1]) * (path[i - 1][1] - path[i - 2][1]) < 0
                        for i in range(2, len(path)))
            if not backs and tidy(path) not in paths:
                paths.append(tidy(path))
        if paths:
            best = min(path_length(path) for path in paths)
            return [path for path in paths if path_length(path) <= best + 1]
    return []


def _cuts(path: list[tuple[float, float]], box: dict) -> bool:
    return any(min(a[0], b[0]) < box["x"] + box["w"] - 1 and max(a[0], b[0]) > box["x"] + 1
               and min(a[1], b[1]) < box["y"] + box["h"] - 1 and max(a[1], b[1]) > box["y"] + 1
               for a, b in zip(path, path[1:]))


def lines_through_boxes(drawn: dict) -> list[str]:
    """The edges whose estimated line runs through a node other than its own two ends.

    A line through one of its own ends, or through the inside of a composite zone it
    leaves or enters, is not one a router draws, so only a path that has no such
    alternative counts.
    """
    shapes = {n["id"]: n for n in drawn["nodes"]}
    boxes = list(boxes_of(drawn).values())
    problems = []
    for c in drawn["connectors"]:
        if not c["name"].startswith(("edge:", "leg:")):
            continue
        (p, v), (q, w) = _point(shapes, c["start"]), _point(shapes, c["end"])
        ends = [shapes[c[side]["endpointNodeId"]] for side in ("start", "end")]
        own = {e["name"] for e in ends}
        paths = candidate_paths(p, v, q, w) if c["line"] == "ELBOWED" else [[p, q]]
        # A line through either end, or through the inside of a composite it leaves or enters, is not one a router draws.
        paths = [path for path in paths if not any(_cuts(path, b) for b in boxes if b["name"] in own)
                 and not any(_cuts(path, e) for e in ends if e["type"] == "SECTION")]
        crossed = {b["name"] for path in paths for b in boxes if b["name"] not in own and _cuts(path, b)}
        if not paths or crossed:
            problems.append(f"{c['name']} runs through {', '.join(sorted(crossed)) or 'its own ends'}")
    return problems


def shared_ports(drawn: dict) -> list[str]:
    """The nodes where an edge leaves from a magnet another edge uses while another magnet is free.

    A node has four magnets, so the edges the model draws apart each take their own while there is one to
    take, and a node with more than four edges shares only what it must. Edges that only arrive may merge on
    one magnet, which `shared_stretches` then holds to a short final stretch.
    """
    held: dict[str, list[tuple[str, str, str]]] = {}
    for e in drawn_edges(drawn):
        for name, magnet, role in e["ports"]:
            held.setdefault(name, []).append((magnet, e["who"], role))
    problems = []
    for name, ends in held.items():
        used = {magnet for magnet, _, _ in ends}
        if len(used) < min(4, len(ends)):
            # Edges that only arrive at a magnet may merge there, which is the way out when the others are taken.
            crowded = sorted(m for m in used if sum(1 for x, _, _ in ends if x == m) > 1
                             and any(role == "out" for x, _, role in ends if x == m))
            who = [w for m, w, _ in ends if m in crowded]
            if not crowded:
                continue
            problems.append(f"{name} {'/'.join(crowded)} holds {len(who)} edges while a magnet is free: {'; '.join(who)}")
    return problems


def lines_along_zones(drawn: dict, labels: list[str]) -> list[str]:
    """The edges with a run that lies along a zone's border, closer than ZONE_OUT outside it or ZONE_IN inside it.

    A run that crosses a border at a right angle is fine. One that rides it reads as part of the zone's
    outline, so a reader cannot tell which of the two it is.
    """
    zones = zone_sections(drawn, labels)
    found = []
    for e in drawn_edges(drawn):
        for z in zones:
            # Each side as (horizontal, coordinate, low end, high end, which way is outside).
            sides = ((True, z["y"], z["x"], z["x"] + z["w"], -1), (True, z["y"] + z["h"], z["x"], z["x"] + z["w"], 1),
                     (False, z["x"], z["y"], z["y"] + z["h"], -1), (False, z["x"] + z["w"], z["y"], z["y"] + z["h"], 1))
            if any(a[0] == side[0] and -ZONE_IN < (a[1] - side[1]) * side[4] < ZONE_OUT
                   and min(a[3], side[3]) - max(a[2], side[2]) > 0
                   for path in e["paths"] for a in _runs(path) for side in sides):
                found.append(f"{e['who']} runs along the border of {z['name']}")
                break
    return found


def lines_through_other_zones(drawn: dict, labels: list[str]) -> list[str]:
    """The edges whose line passes through a zone that neither holds one of their ends nor is one.

    A lane spans the whole board, so an edge between two lanes crosses any lane between them, and callers
    leave a laned process out. Every other zone is a block an edge can go round.
    """
    zones = zone_sections(drawn, labels)
    return [f"{e['who']} passes through the zone {z['name']} it does not join" for e in drawn_edges(drawn) for z in zones
            if z["name"] not in e["homes"] and any(_cuts(path, z) for path in e["paths"])]


def drawn_edges(drawn: dict) -> list[dict]:
    """Each model edge as the connectors that draw it: the paths it may take and where its label sits.

    A routed edge is a chain of legs through anchors that ends in the connector named `edge:`, so its legs
    are joined into one path set. The label rides on whichever leg holds the text.
    """
    shapes = {n["id"]: n for n in drawn["nodes"]}
    edges, legs = [], []
    for c in drawn["connectors"]:
        if not c["name"].startswith(("edge:", "leg:")):
            continue
        legs.append(c)
        if c["name"].startswith("leg:"):
            continue
        whole, carried = [[]], []
        for leg in legs:
            (p, v), (q, w) = _point(shapes, leg["start"]), _point(shapes, leg["end"])
            options = candidate_paths(p, v, q, w) if leg["line"] == "ELBOWED" else [[p, q]]
            whole = [tidy(joined + (option if not joined else option[1:])) for joined in whole for option in options]
            if leg["label"]:
                carried = options
        # A line through either end of its own edge is not one a router draws.
        ends = [shapes[legs[0]["start"]["endpointNodeId"]], shapes[c["end"]["endpointNodeId"]]]
        paths = []
        for path in whole:
            if path not in paths and not any(_cuts(path, e) for e in ends):
                paths.append(path)
        paths = paths or whole
        label = next((leg["label"] for leg in legs if leg["label"]), "")
        edges.append({"name": c["name"], "label": label, "who": f"{c['name']} ({label})" if label else c["name"],
                      "paths": paths, "label_paths": carried or paths,
                      "ends": {e["name"] for e in ends}, "boxes": ends,
                      "homes": {e["name"] if e["type"] == "SECTION" else e["parent"] for e in ends},
                      "ports": {(e["name"], _side(e, end), role) for e, end, role in
                                zip(ends, (legs[0]["start"], c["end"]), ("out", "in"))
                                if "magnet" in end or not e["name"].startswith("via:")}})
        legs = []
    return edges


def shared_arrivals(drawn: dict, gantt: bool = False) -> list[str]:
    """The edges that arrive at one point of one node, or closer than SPREAD along one side, which read as one arrowhead.

    A dot, a choice and a milestone are where paths join, so edges may meet on them, as the composer leaves them.
    Every other node gives each arrival its own point, SPREAD from the next where the side holds them all. A gantt
    bar takes its arrows within GANTT_LANDING of its left end, so a short bar spaces them closer to fit.
    """
    shapes = {n["id"]: n for n in drawn["nodes"]}
    seen: dict[tuple, str] = {}
    sides: dict[tuple, list[tuple[float, str]]] = {}
    problems = []
    for c in drawn["connectors"]:
        if not c["name"].startswith("edge:"):
            continue
        node = shapes[c["end"]["endpointNodeId"]]
        joins = {"ELLIPSE": DOT_WIDTH, "DIAMOND": JOIN_DIAMOND}.get(node.get("shape"), 0)
        if node["w"] <= joins:
            continue
        (x, y), way = _point(shapes, c["end"])
        spot = (node["name"], round(x), round(y))
        if spot in seen:
            problems.append(f"{seen[spot]} and {c['name']} arrive at one point of {node['name']}")
        seen.setdefault(spot, c["name"])
        if way:
            sides.setdefault((node["id"], way), []).append((x if way[1] else y, c["name"]))
    for (node_id, way), points in sides.items():
        node = shapes[node_id]
        room = node["w"] if way[1] else node["h"]
        if gantt:
            room = min(room, GANTT_LANDING) - 12
        need = min(SPREAD, room / max(1, len(points) - 1))
        points.sort()
        for (a, first), (b, second) in zip(points, points[1:]):
            if 0 < b - a < need - 0.5:
                problems.append(f"{first} and {second} arrive {round(b - a)} px apart on one side of {node['name']}, "
                                f"at least {round(need)} where the side holds them")
    return problems


def gantt_arrow_ends(drawn: dict) -> list[str]:
    """The gantt arrows that leave a bar anywhere but its right end, or land anywhere but the top of the next bar's left end.

    A milestone is one moment, so an arrow leaves it from its foot and reaches it at its top.
    """
    shapes = {n["id"]: n for n in drawn["nodes"]}
    problems = []
    for c in drawn["connectors"]:
        if not c["name"].startswith("edge:"):
            continue
        source, target = (shapes[c[side]["endpointNodeId"]] for side in ("start", "end"))
        (x0, _), _ = _point(shapes, c["start"])
        (x1, y1), _ = _point(shapes, c["end"])
        leaves = x0 == source["x"] + (source["w"] / 2 if source.get("shape") == "DIAMOND" else source["w"])
        lands = x1 == target["x"] + target["w"] / 2 if target.get("shape") == "DIAMOND" \
            else target["x"] < x1 <= target["x"] + min(GANTT_LANDING, target["w"])
        if not (leaves and lands and y1 == target["y"]):
            problems.append(f"{c['name']} leaves {source['name']} at x {x0:g} and lands on {target['name']} at {x1:g}, {y1:g}")
    return problems


def long_detours(drawn: dict, limit: float = DETOUR_LIMIT) -> list[str]:
    """The edges whose shortest drawn route runs more than `limit` times the gap between their two boxes.

    The gap is the least any route could run (the distance the boxes leave between them, taken along both
    axes), floored at one card so two touching boxes do not make every bend a detour. An edge that loops over
    a zone to reach a magnet is far above it, and the same edge sharing a magnet it only arrives at is not.
    """
    problems = []
    for e in drawn_edges(drawn):
        a, b = e["boxes"]
        dx = abs((a["x"] + a["w"] / 2) - (b["x"] + b["w"] / 2)) - (a["w"] + b["w"]) / 2
        dy = abs((a["y"] + a["h"] / 2) - (b["y"] + b["h"] / 2)) - (a["h"] + b["h"]) / 2
        gap = max(max(0, dx) + max(0, dy), 96)
        run = min(path_length(p) for p in e["paths"])
        if run > limit * gap:
            problems.append(f"{e['who']} runs {round(run)} px between boxes {round(gap)} px apart")
    return problems


def _label_box(label: str, path: list[tuple[float, float]]) -> dict:
    """The box a label takes: its text and a pad, centred on the middle of the path it rides."""
    half, centre = path_length(path) / 2, path[-1]
    for a, b in zip(path, path[1:]):
        run = abs(b[0] - a[0]) + abs(b[1] - a[1])
        if run and half <= run:
            centre = (a[0] + (b[0] - a[0]) * half / run, a[1] + (b[1] - a[1]) * half / run)
            break
        half -= run
    width = len(label) * LABEL_CHAR + LABEL_PAD
    return {"x": centre[0] - width / 2, "y": centre[1] - LABEL_HEIGHT / 2, "w": width, "h": LABEL_HEIGHT}


def _overlap(a: dict, b: dict) -> bool:
    """Whether two boxes share more than a pixel of area, the slack the composer allows a touch."""
    return (a["x"] < b["x"] + b["w"] - 1 and b["x"] < a["x"] + a["w"] - 1
            and a["y"] < b["y"] + b["h"] - 1 and b["y"] < a["y"] + a["h"] - 1)


def _grown(box: dict, gap: float) -> dict:
    return {"x": box["x"] - gap, "y": box["y"] - gap, "w": box["w"] + 2 * gap, "h": box["h"] + 2 * gap}


def title_boxes(drawn: dict, labels: list[str]) -> list[dict]:
    """Every zone's title text, which a line or a label must stay clear of."""
    return [n for n in drawn["nodes"] if n["type"] == "TEXT" and n["parent"] in labels]


def lines_through_titles(drawn: dict, labels: list[str]) -> list[str]:
    """The edges whose line passes through a zone's title, or within a few pixels of it."""
    titles = title_boxes(drawn, labels)
    return [f"{e['who']} runs through the title {t['text']}" for e in drawn_edges(drawn) for t in titles
            if any(_cuts(path, _grown(t, TITLE_GAP)) for path in e["paths"])]


def labels_off_titles(drawn: dict, labels: list[str]) -> list[str]:
    """The edges whose label would print on a zone's title."""
    titles = title_boxes(drawn, labels)
    return [f"{e['who']} prints on the title {t['text']}" for e in drawn_edges(drawn) if e["label"]
            for t in titles if any(_overlap(_label_box(e["label"], path), _grown(t, TITLE_GAP // 2)) for path in e["label_paths"])]


def labels_clear(drawn: dict) -> list[str]:
    """The labels that sit on a node or within LABEL_CLEAR of one, on another edge's line or on another label."""
    edges = drawn_edges(drawn)
    nodes = list(boxes_of(drawn).values())
    problems = []
    for e in edges:
        if not e["label"]:
            continue
        for path in e["label_paths"]:
            box = _label_box(e["label"], path)
            air = _grown(box, LABEL_CLEAR)
            on_node = next((n["name"] for n in nodes if n["name"] not in e["ends"] and _overlap(air, n)), None)
            on_line = next((o["who"] for o in edges if o is not e and any(_cuts(p, air) for p in o["paths"])), None)
            on_label = next((o["who"] for o in edges if o is not e and o["label"]
                             and any(_overlap(box, _label_box(o["label"], p)) for p in o["label_paths"])), None)
            found = on_node or on_line or on_label
            if found:
                problems.append(f"{e['who']} prints on {found}")
                break
    return problems


def labels_on_short_legs(drawn: dict) -> list[str]:
    """The labels that ride a straight leg shorter than themselves and their air, so the line reads as broken there."""
    shapes = {n["id"]: n for n in drawn["nodes"]}
    problems = []
    for c in drawn["connectors"]:
        if not c["label"] or c["line"] != "STRAIGHT" or not c["name"].startswith(("edge:", "leg:")):
            continue
        (p, _), (q, _) = _point(shapes, c["start"]), _point(shapes, c["end"])
        level = p[1] == q[1]
        need = (len(c["label"]) * LABEL_CHAR + LABEL_PAD if level else LABEL_HEIGHT) + 2 * LABEL_CLEAR
        run = abs(q[0] - p[0]) + abs(q[1] - p[1])
        if run < need:
            problems.append(f"{c['name']} ({c['label']}) rides a {run:g} px leg that needs {need:g}")
    return problems


def _runs(path: list[tuple[float, float]]) -> list[tuple[bool, float, float, float]]:
    """Each straight run of a path as (horizontal, fixed coordinate, low end, high end)."""
    runs = []
    for a, b in zip(path, path[1:]):
        horizontal = a[1] == b[1]
        runs.append((horizontal, a[1] if horizontal else a[0],
                     min(a[0], b[0]) if horizontal else min(a[1], b[1]),
                     max(a[0], b[0]) if horizontal else max(a[1], b[1])))
    return runs


def _meets(p: list[tuple[float, float]], q: list[tuple[float, float]]) -> bool:
    """Whether two paths cross or touch at a right angle anywhere but a point where both end.

    A bend that lands on another line reads as a crossing, however short the jog that follows it,
    while two edges arriving at one magnet share their end point and may join on the last stretch
    they merge along.
    """
    def on(run: tuple[bool, float, float, float], point: tuple[float, float]) -> bool:
        x, y = point
        return y == run[1] and run[2] <= x <= run[3] if run[0] else x == run[1] and run[2] <= y <= run[3]

    for a in _runs(p):
        for b in _runs(q):
            if a[0] == b[0] or not (a[2] <= b[1] <= a[3] and b[2] <= a[1] <= b[3]):
                continue
            point = (b[1], a[1]) if a[0] else (a[1], b[1])
            joined = p[-1] == q[-1] and on(_runs(p)[-1], point) and on(_runs(q)[-1], point)
            if not joined and not (point in (p[0], p[-1]) and point in (q[0], q[-1])):
                return True
    return False


def crossing_edges(drawn: dict) -> list[str]:
    """The pairs of edges that cross or touch in the middle of their runs, whichever way the router bends them."""
    edges = drawn_edges(drawn)
    found = []
    for i, e in enumerate(edges):
        for o in edges[i + 1:]:
            if any(_meets(p, q) for p in e["paths"] for q in o["paths"]):
                found.append(f"{e['who']} crosses {o['who']}")
    return found


def shared_stretches(drawn: dict) -> list[str]:
    """The pairs of edges that lie on one trunk for longer than a label needs, so a label there names both.

    Two parallel runs closer than CORRIDOR read as one line, so they count as one however they were snapped.
    Two edges that arrive at one magnet may share the final stretch they merge along, up to MERGE_MAX.
    """
    edges = drawn_edges(drawn)
    found = []
    for i, e in enumerate(edges):
        for o in edges[i + 1:]:
            longest = max((min(a[3], b[3]) - max(a[2], b[2]) for p in e["paths"] for q in o["paths"]
                           for a in _runs(p) for b in _runs(q) if a[0] == b[0] and abs(a[1] - b[1]) < CORRIDOR), default=0)
            merging = {x for x in e["ports"] if x[2] == "in"} & {x for x in o["ports"] if x[2] == "in"}
            if longest > (MERGE_MAX if merging else SHARE_MAX):
                found.append(f"{e['who']} and {o['who']} share {longest:g} px of one line")
    return found


def edges_side_by_side(drawn: dict) -> list[str]:
    """The pairs of edges whose runs lie parallel, closer than SIDE_BY_SIDE, for longer than a stub.

    Two lines a few pixels apart read as one doubled line, so a pair is either clearly apart or a merge
    that lasts no longer than SHARE_MAX. Runs closer than CORRIDOR are the trunk measure's. Two edges that
    arrive at one side of one node, each at its own point, may run side by side into it up to MERGE_MAX.
    """
    edges = drawn_edges(drawn)
    found = []
    for i, e in enumerate(edges):
        for o in edges[i + 1:]:
            longest = max((min(a[3], b[3]) - max(a[2], b[2]) for p in e["paths"] for q in o["paths"]
                           for a in _runs(p) for b in _runs(q)
                           if a[0] == b[0] and CORRIDOR <= abs(a[1] - b[1]) < SIDE_BY_SIDE), default=0)
            arriving = {x for x in e["ports"] if x[2] == "in"} & {x for x in o["ports"] if x[2] == "in"}
            if longest > (MERGE_MAX if arriving else SHARE_MAX):
                found.append(f"{e['who']} and {o['who']} run side by side for {longest:g} px")
    return found


def _text_width(shape: dict) -> float:
    """The width the composer fits a shape's label into, which is its box less what the shape takes of it."""
    w, kind = shape["w"], shape.get("shape")
    if kind in ROUND_SHAPES:
        return w / 2 - 32
    return w - (96 if kind == "PARALLELOGRAM_RIGHT" else 48)


def _wrapped(text: str, per: int) -> list[str]:
    """The text in lines of at most `per` characters, filled word by word after each break it carries."""
    lines = []
    for chunk in text.split("\n"):
        line = ""
        for word in chunk.split():
            if line and len(line) + 1 + len(word) > per:
                lines.append(line)
                line = word
            else:
                line = f"{line} {word}".strip()
        lines.append(line)
    return [line for line in lines if line]


def orphan_words(drawn: dict) -> list[str]:
    """The labels that wrap one word alone onto their last line, while holding two lines or more.

    A label wraps at the text width its shape leaves, which is narrower than the box on a round shape and
    narrower again on a parallelogram, so a box with room to spare can still strand one word. A line of one
    word reads as a stray word rather than as part of the label, so the label's shape is lost at a glance.
    This measure is advice for shortening the label before the board is written, never a failure.
    """
    found = []
    for n in drawn["nodes"]:
        if n["type"] != "SHAPE_WITH_TEXT" or not n["text"].strip():
            continue
        # The label is read at both measures, since FigJam may wrap at either.
        for per in sorted({max(1, int(_text_width(n) // NODE_CHAR)), max(1, int(_text_width(n) // NODE_NARROW_CHAR))}):
            lines = _wrapped(n["text"], per)
            if len(lines) > 1 and len(lines[-1].split()) == 1:
                found.append(f"{' '.join(n['text'].split())} leaves {lines[-1]!r} alone on its last line")
                break
    return found


def _end_dots(drawn: dict, node: dict) -> tuple[list[dict], list[str]]:
    """The end dots a node's own connectors run to, and the names of those connectors' edges."""
    dots, names = [], []
    for edge in drawn_edges(drawn):
        if node["name"] in edge["ends"]:
            others = [box for box in edge["boxes"] if box["name"] != node["name"]]
            if others and all(box["name"].startswith("node:__end") for box in others):
                dots += others
                names.append(edge["name"])
    return dots, names


def sticky_sides(drawn: dict, ids: list[str]) -> list[tuple[str, str, str | None]]:
    """For each noted node, its label and the side that holds its single sticky, or None when none does.

    An id the board does not draw comes back with no label, so the caller can name it as a typo.

    A side holds the sticky when the sticky's square and the gap between it and its node are clear of every
    other shape, text and the key, and no estimated line runs through them. The sticky stands level with its
    node on the right and the left, and lined up with it below and above, top or left aligned or centred. On
    the right, a node's own connector to its end dot does not take the side, so the sticky goes past the
    dot. Only the right may run past the board, which widens to hold it. A sticky placed for one node takes
    its square and the gap around it from the next, so the sides are chosen together: the first choice in
    side order that gives every noted node a sticky, or the one that gives the most.
    """
    boxes = boxes_of(drawn)
    board = next((n for n in drawn["nodes"] if n["type"] == "SECTION" and n["parent"] == ""), None)
    edges = drawn_edges(drawn)
    drawn_ids = [node_id for node_id in ids if node_id in boxes]

    def places(node: dict, placed: list[dict]) -> list[tuple[str, dict]]:
        """Every side and square that holds this node's sticky, in side order."""
        dots, own = _end_dots(drawn, node)
        ignore = {node["id"]} | {dot["id"] for dot in dots}
        blockers = [n for n in drawn["nodes"] if n["id"] not in ignore and n["parent"] != node["name"]
                    and (n["type"] != "SECTION" or n["name"] == "Key")] + placed
        x, y, w, h = node["x"], node["y"], node["w"], node["h"]
        right_from = max([x + w] + [dot["x"] + dot["w"] for dot in dots])
        spots = {
            "right": [(right_from, right_from + STICKY_GAP, yy) for yy in (y, y + h / 2 - STICKY / 2)],
            "left": [(x - STICKY_GAP - STICKY, x - STICKY_GAP - STICKY, yy) for yy in (y, y + h / 2 - STICKY / 2)],
            "below": [(xx, xx, y + h) for xx in (x, x + w / 2 - STICKY / 2)],
            "above": [(xx, xx, y - STICKY_GAP - STICKY) for xx in (x, x + w / 2 - STICKY / 2)],
        }
        found = []
        for side in STICKY_SIDES:
            for start, left, top in spots[side]:
                if side in ("right", "left"):
                    sticky = {"x": left, "y": top, "w": STICKY, "h": STICKY}
                    span = {"x": min(start, left), "y": top, "w": STICKY + STICKY_GAP, "h": STICKY}
                else:
                    top_edge = top if side == "above" else top + STICKY_GAP
                    sticky = {"x": left, "y": top_edge, "w": STICKY, "h": STICKY}
                    span = {"x": left, "y": min(top_edge, top), "w": STICKY, "h": STICKY + STICKY_GAP}
                if board is not None and side != "right" and not (
                        sticky["x"] >= board["x"] and sticky["y"] >= board["y"]
                        and sticky["x"] + STICKY <= board["x"] + board["w"]
                        and sticky["y"] + STICKY <= board["y"] + board["h"]):
                    continue
                if board is not None and side == "right" and (
                        sticky["y"] < board["y"] or sticky["y"] + STICKY > board["y"] + board["h"]):
                    continue
                if any(_overlap(span, b) for b in blockers):
                    continue
                if any(_cuts(path, span) for edge in edges if edge["name"] not in own for path in edge["paths"]):
                    continue
                found.append((side, sticky))
                break
        return found

    def choose(index: int, placed: list[dict]) -> list[str | None]:
        """The sides for the noted nodes from this one on: the first full choice, else the fullest."""
        if index == len(drawn_ids):
            return []
        best = None
        for side, sticky in places(boxes[drawn_ids[index]], placed) + [(None, None)]:
            rest = choose(index + 1, placed + ([_grown(sticky, STICKY_GAP)] if sticky else []))
            pick = [side] + rest
            if best is None or sum(s is not None for s in pick) > sum(s is not None for s in best):
                best = pick
            if None not in pick:
                break
        return best

    sides = dict(zip(drawn_ids, choose(0, [])))
    return [(node_id, " ".join(boxes[node_id]["text"].split()) or node_id, sides[node_id]) if node_id in boxes
            else (node_id, None, None) for node_id in ids]


def arrow_heads(drawn: dict, messages: list[dict]) -> list[str]:
    """Each sequence message ends in the head, line and colour its Mermaid arrow form names.

    A request and a reply end in a closed head, an async message and an async reply in an open one, and a
    reply or an async reply is dashed. An async message is the one blue arrow, so it reads as async at a glance.
    """
    wanted = {"request": ("ARROW_EQUILATERAL", False), "reply": ("ARROW_EQUILATERAL", True),
              "async": ("ARROW_LINES", False), "asyncReply": ("ARROW_LINES", True)}
    problems = []
    for k, m in enumerate(messages, 1):
        name = f"edge:{m['from']}->{m['to']}:{k}"
        c = next((c for c in drawn["connectors"] if c["name"] == name), None)
        if c is None:
            problems.append(f"message {k} {m['from']} to {m['to']} has no connector {name}")
            continue
        head, dashed = wanted[m["arrow"]]
        blue = bool(c["stroke"]) and abs(c["stroke"][0]["color"]["b"] - 1) < 0.01 and c["stroke"][0]["color"]["r"] < 0.3
        if c["endCap"] != head or bool(c["dash"]) != dashed or blue != (m["arrow"].startswith("async") and not m.get("accent")):
            problems.append(f"message {k} {m['arrow']} ends in {c['endCap']}, "
                            f"{'dashed' if c['dash'] else 'solid'}, {'blue' if blue else 'not blue'}; "
                            f"wants {head}, {'dashed' if dashed else 'solid'}")
    return problems


def zone_sections(drawn: dict, labels: list[str]) -> list[dict]:
    """The sections drawn for the model's zones, found by their labels."""
    return [n for n in drawn["nodes"] if n["type"] == "SECTION" and n["name"] in labels]


def overlapping_zones(drawn: dict, labels: list[str]) -> list[str]:
    """Zones drawn on one another, and nodes drawn inside a zone they do not belong to."""
    zones = zone_sections(drawn, labels)
    clash = [f"{a['name']} and {b['name']}" for i, a in enumerate(zones) for b in zones[i + 1:]
             if a["x"] < b["x"] + b["w"] and b["x"] < a["x"] + a["w"] and a["y"] < b["y"] + b["h"] and b["y"] < a["y"] + a["h"]]
    boxes = boxes_of(drawn)
    return clash + [f"{name} sits inside {z['name']}" for z in zones for name, b in boxes.items()
                    if b["parent"] != z["name"] and z["x"] < b["x"] + b["w"] and b["x"] < z["x"] + z["w"]
                    and z["y"] < b["y"] + b["h"] and b["y"] < z["y"] + z["h"]]


def short_cards(drawn: dict) -> list[str]:
    """Entity cards too short for their lines: a title, then each field with its paragraph gap."""
    short = []
    for n in drawn["nodes"]:
        lines = n["text"].split("\n")
        if n["name"].startswith("node:") and n["shape"] == "SQUARE" and len(lines) > 1:
            need = CARD_PAD + 20 + PARAGRAPH + (len(lines) - 1) * (FIELD_LINE + PARAGRAPH)
            if n["h"] < need:
                short.append(f"{n['name']} is {n['h']} high and its {len(lines)} lines need {need}")
    return short


def tall_zones(drawn: dict, labels: list[str], mode: str, slack: int = ZONE_PAD) -> list[str]:
    """Zones that hold more cross-axis space than their members ask for, on a left to right board.

    A stage zone's top is the row's shared top edge or, where its row keeps its own fit, its own members' head, within
    one grid step. Its bottom is one pad below its lowest member, so it is measured from its own top
    whichever of the two it took. A lane is never taller than its members stacked one above another with the
    standard gap, plus the head and the pad, because no packing of them is taller. The slack is the second pad a zone
    takes when an edge loops back inside it.
    """
    boxes = boxes_of(drawn)
    zones = zone_sections(drawn, labels)
    top = min((b["y"] for z in zones for b in boxes.values() if b["parent"] == z["name"]), default=0)
    tall = []
    for z in zones:
        inside = [b for b in boxes.values() if b["parent"] == z["name"]]
        if not inside:
            continue
        lowest = max(b["y"] + b["h"] for b in inside)
        if mode == "stage":
            own, shared = min(b["y"] for b in inside) - ZONE_HEAD, top - ZONE_HEAD
            if min(abs(z["y"] - own), abs(z["y"] - shared)) > GRID_STEP or z["y"] + z["h"] > lowest + ZONE_PAD + slack:
                tall.append(f"{z['name']} runs from {z['y']} to {z['y'] + z['h']} around members reaching {lowest}, where its "
                            f"top is {shared} or {own} and its bottom at most {lowest + ZONE_PAD + slack}")
            continue
        stacked = sum(b["h"] for b in inside) + CROSS_GAP * (len(inside) - 1)
        allowed = stacked + ZONE_HEAD + ZONE_PAD + slack
        if z["h"] > allowed:
            tall.append(f"{z['name']} is {z['h']} high around {stacked} of members, at most {allowed}")
    return tall


# The accent is the only 8 px outline on a board, and the only pink. A message that carries it is drawn 4 px.
ACCENT_WEIGHT, ACCENT_LINE, ACCENT_STROKE, OUTWEIGH = 8, 4, "#f849c1", 1.5


def _hex(paint: list | None) -> str:
    colour = (paint or [{"color": {"r": 0, "g": 0, "b": 0}}])[0]["color"]
    return "#" + "".join(f"{round(colour[c] * 255):02x}" for c in "rgb")


def hex_of(paint: list | None) -> str:
    """The six-digit hex of a drawn fill or stroke, black when it has none."""
    return _hex(paint)


def ink(mark: dict) -> float:
    """What a mark puts on a greyscale copy of the board: its line weight times its contrast on the canvas."""
    return (mark.get("weight") or 0) * contrast(_hex(mark.get("stroke")), CANVAS)


def accent_problems(drawn: dict, planned: set[str]) -> list[str]:
    """The accent sits on exactly the nodes the model plans, in the accent pink, and outweighs every other mark.

    The weight test is made on ink, so it holds on a greyscale copy, where the start pill's blue and the
    accent's pink are both just grey and only the line is left to tell them apart.
    """
    marks = {name: n for name, n in boxes_of(drawn).items()}
    heavy = {name for name, n in marks.items() if (n.get("weight") or 0) >= ACCENT_WEIGHT}
    problems = []
    if heavy != planned:
        problems.append(f"the accent is drawn on {sorted(heavy) or 'nothing'}, the model plans it on {sorted(planned) or 'nothing'}")
    others = max((ink(n) for name, n in marks.items() if name not in planned), default=0)
    for name in sorted(planned & set(marks)):
        if _hex(marks[name].get("stroke")) != ACCENT_STROKE:
            problems.append(f"{name} carries the accent in {_hex(marks[name].get('stroke'))}, not the accent pink")
        if ink(marks[name]) < OUTWEIGH * others:
            problems.append(f"{name} puts {ink(marks[name]):.1f} of ink on a greyscale copy against {others:.1f} "
                            f"for the heaviest other mark, under {OUTWEIGH:g} times")
    return problems


def message_accent_problems(drawn: dict, messages: list[dict]) -> list[str]:
    """The sequence message the model plans as the accent is drawn in the accent pink and 4 px, and no other is."""
    problems = []
    for k, m in enumerate(messages, 1):
        who = f"{m['from']}->{m['to']}:{k}"
        lines = [c for c in drawn["connectors"] if c["name"] == f"edge:{who}" or c["name"].startswith(f"leg:{who}:")]
        marked = bool(lines) and all(_hex(c["stroke"]) == ACCENT_STROKE and c["weight"] == ACCENT_LINE for c in lines)
        plain = all(_hex(c["stroke"]) != ACCENT_STROKE and c["weight"] != ACCENT_LINE for c in lines)
        if bool(m.get("accent")) != marked or (not m.get("accent") and not plain):
            problems.append(f"message {k} {'is not' if m.get('accent') else 'is'} drawn as the accent")
    return problems

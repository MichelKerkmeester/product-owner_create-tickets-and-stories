# ───────────────────────────────────────────────────────────────
# COMPONENT: LAYOUT MEASURES
# ───────────────────────────────────────────────────────────────

"""How much shape a diagram asks a reader to hold, measured on the same parse.

A count says how much a diagram holds and nothing about how hard it reads: a rank
of six steps, a chain of nine and two connectors that swap sides all pass one
count. The generator owns the layout, so a shape that reads badly cannot be
rearranged once the board exists. These measures run before the write, and one
out of band is fixed in the model before a write is spent.

A flow may loop back, so the connectors that close a loop are dropped before the
ranks are read. The crossing count is an estimate: the generator chooses where a
rank sits, and the order the writer declared the steps stands in for it.
"""

from __future__ import annotations

from .common import MAX_LABEL_CHARS

# A reader holds one rank at a time, so a rank wider than this cannot be read in
# one pass down the page.
MAX_RANK_WIDTH = 4
# One step under the largest diagram a type may hold: a flow read as one chain of
# nine steps is where a reader stops following the thread.
MAX_LONGEST_PATH = 8
# A pair of connectors that swap sides has to be followed across the diagram to
# see where it lands, and more than two of those is a tangle.
MAX_CROSSINGS = 2
# A label may reach 40 characters, and a rank of labels near that cap is a wall of
# text, so the average has to leave a reader room to skim.
MAX_LABEL_AVERAGE = MAX_LABEL_CHARS * 7 // 10
# Steps joined more than twice over are joined more than they are read.
MAX_CONNECTORS_PER_STEP = 2.0


def steps_of(diagram) -> list[str]:
    """The drawable step ids, in the order the writer declared them."""
    return [node.id for node in diagram.nodes if not node.container]


def following_of(diagram, steps: list[str]) -> dict[str, list[str]]:
    """The steps each step reaches, leaving out the connectors that touch a lane."""
    kept = set(steps)
    following = {step: [] for step in steps}
    for edge in diagram.edges:
        if edge.source in kept and edge.target in kept:
            following[edge.source].append(edge.target)
    return following


def closing_edges(steps: list[str], following: dict[str, list[str]]) -> set[tuple[str, str]]:
    """The connectors that close a loop, found by walking forward from each step."""
    open_steps, closed, closing = set(), set(), set()
    for start in steps:
        if start in closed:
            continue
        open_steps.add(start)
        stack = [(start, iter(following.get(start, ())))]
        while stack:
            step, targets = stack[-1]
            for target in targets:
                if target in open_steps:
                    closing.add((step, target))
                elif target not in closed:
                    open_steps.add(target)
                    stack.append((target, iter(following.get(target, ()))))
                    break
            else:
                stack.pop()
                open_steps.discard(step)
                closed.add(step)
    return closing


def ranks_of(steps: list[str], following: dict[str, list[str]],
             closing: set[tuple[str, str]]) -> dict[str, int]:
    """The number of steps on the longest path that reaches each step."""
    ranks = {step: 0 for step in steps}
    pairs = [(source, target) for source, targets in following.items()
             for target in targets if (source, target) not in closing]
    for _ in range(len(steps)):
        settled = True
        for source, target in pairs:
            if ranks[target] < ranks[source] + 1:
                ranks[target] = ranks[source] + 1
                settled = False
        if settled:
            break
    return ranks


def crossing_count(edges, ranks: dict[str, int], position: dict[str, int]) -> int:
    """Connector pairs from one rank to the next whose ends were declared in opposite order."""
    groups: dict[tuple[int, int], list] = {}
    for edge in edges:
        if ranks[edge.source] == ranks[edge.target]:
            continue
        groups.setdefault((ranks[edge.source], ranks[edge.target]), []).append(edge)
    total = 0
    for group in groups.values():
        for index, first in enumerate(group):
            for second in group[index + 1:]:
                if first.source == second.source:
                    continue
                source_way = position[first.source] - position[second.source]
                target_way = position[first.target] - position[second.target]
                if source_way * target_way < 0:
                    total += 1
    return total


def measure(diagram) -> tuple[list[str], str]:
    """The shape problems to fix, and one line naming every measure."""
    steps = steps_of(diagram)
    if not steps:
        return [], ""
    following = following_of(diagram, steps)
    ranks = ranks_of(steps, following, closing_edges(steps, following))
    inside = [edge for edge in diagram.edges if edge.source in ranks and edge.target in ranks]
    position = {node.id: index for index, node in enumerate(diagram.nodes)}
    widths: dict[int, int] = {}
    for rank in ranks.values():
        widths[rank] = widths.get(rank, 0) + 1
    widest = max(widths.values())
    longest = max(ranks.values()) + 1
    crossings = crossing_count(inside, ranks, position)
    labels = [node.label.strip() for node in diagram.nodes if not node.container and node.label.strip()]
    average = round(sum(len(label) for label in labels) / len(labels)) if labels else 0
    per_step = len(inside) / len(steps)
    problems = []
    if widest > MAX_RANK_WIDTH:
        problems.append(f"a rank holds {widest} steps, at most {MAX_RANK_WIDTH}: "
                        "split the flow so a rank reads at a glance")
    if longest > MAX_LONGEST_PATH:
        problems.append(f"the longest path runs {longest} steps, at most {MAX_LONGEST_PATH}: "
                        "split the flow")
    if crossings > MAX_CROSSINGS:
        problems.append(f"{crossings} connector pairs swap sides, at most {MAX_CROSSINGS}: "
                        "order the steps so each route stays on its side")
    if average > MAX_LABEL_AVERAGE:
        problems.append(f"labels average {average} characters, at most {MAX_LABEL_AVERAGE}: "
                        "cut each label to four words")
    if per_step > MAX_CONNECTORS_PER_STEP:
        problems.append(f"{len(inside)} connectors for {len(steps)} steps, at most "
                        f"{MAX_CONNECTORS_PER_STEP:g} per step: join the two steps once and label that connector")
    summary = (f"widest rank {widest} steps, longest path {longest} steps, {per_step:.1f} connectors per step, "
               f"labels average {average} characters, {crossings} crossing pairs")
    return problems, summary

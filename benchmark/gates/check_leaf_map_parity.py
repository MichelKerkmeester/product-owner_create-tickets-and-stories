#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: LEAF MAP PARITY GATE
# ───────────────────────────────────────────────────────────────

"""Check that every router lane maps to a packet manifest and registered leaf.

Each vendored packet's lane has to equal the leaf set of the intent its own
SKILL.md calls common, because the packet routes the rest.

It also replays the FLOW keywords of the ROUTER.md block against the hub gold
rows, the way the shared leaf-route-replay script scores a block: one point of
weight per keyword found in the lowercased request, and every intent within one
point of the top score kept. No other gate reads that block, so a FigJam
request it cannot see would pass every check while the leaf router found no
intent for it.

Usage:
  check_leaf_map_parity.py -> exit 0 when every lane, packet and gold row agree, exit 1 otherwise
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parents[2]

# The human-facing router uses intent lanes while the manifest uses packet names.
# This crosswalk is the one deliberate translation between those key sets.
LANE_TO_PACKET = {
    "TASK": "sk-product-owner",
    "BUG": "sk-product-owner",
    "DOC": "sk-product-owner",
    "STORY": "sk-product-owner",
    "EPIC": "sk-product-owner",
    "INTERACTIVE": "sk-product-owner",
    "FLOW": "sk-create-figjam",
    "CLICK_UP": "mcp-click-up",
    "FIGMA": "mcp-figma",
}
DEFAULT_PACKET = "sk-product-owner"
FIGJAM_PACKET = "sk-create-figjam"
# A vendored packet routes inside its own SKILL.md, so the hub lane for it is the
# leaf set of that packet's common intent and the packet adds the rest. The
# lane has to equal that entry, or the hub loads leaves the packet would not.
VENDORED_LANE_INTENT = {"CLICK_UP": "CUPT_DAILY", "FIGMA": "CREATE_RENDER"}
ARTIFACT_LANES = {"TASK", "BUG", "DOC", "STORY", "EPIC"}
# The shared replay keeps every intent within this many points of the top score.
AMBIGUITY_DELTA = 1
CASES = Path("benchmark/hub-routing-cases.json")


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────

def fail(message: str, errors: list[str]) -> None:
    """Record one finding on the shared error list."""
    errors.append(message)


def parse_router() -> tuple[list[str], dict[str, list[str]], dict[str, dict]]:
    """Read DEFAULT_RESOURCE, RESOURCE_MAP and INTENT_SIGNALS from the ROUTER.md Python block."""
    source = (ROOT / "ROUTER.md").read_text(encoding="utf-8")
    match = re.search(r"```python\s*(.*?)\s*```", source, re.S)
    if not match:
        raise ValueError("ROUTER.md has no Python resource map")
    tree = ast.parse(match.group(1))
    values = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in {"DEFAULT_RESOURCE", "RESOURCE_MAP", "INTENT_SIGNALS"}:
                values[name] = ast.literal_eval(node.value)
    return values["DEFAULT_RESOURCE"], values["RESOURCE_MAP"], values["INTENT_SIGNALS"]


def packet_leaves(packet: str, intent: str) -> list[str]:
    """The packet-qualified leaves a vendored packet's RESOURCE_MAP gives one intent."""
    source = (ROOT / packet / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^RESOURCE_MAP = (\{.*?^\})", source, re.S | re.M)
    if not match:
        raise ValueError(f"{packet}/SKILL.md has no RESOURCE_MAP")
    entry = ast.literal_eval(match.group(1))[intent]
    return [f"{packet}/{leaf}" for leaf in entry if leaf.startswith(("references/", "assets/"))]


def replay_intents(request: str, signals: dict[str, dict]) -> set[str]:
    """Score a request the way the shared replay does, with FLOW ranked below an artifact.

    A FigJam board named beside an artifact is that artifact's subject, so FLOW
    drops out whenever any artifact intent scores. The keyword block cannot say
    that itself, which is why the settling sits here.
    """
    text = " ".join(request.lower().replace("\u2019", "'").split())
    scores = {
        intent: sum(entry["weight"] for keyword in entry["keywords"] if keyword.lower() in text)
        for intent, entry in signals.items()
    }
    scores = {intent: score for intent, score in scores.items() if score > 0}
    if scores.keys() & ARTIFACT_LANES:
        scores.pop("FLOW", None)
    if not scores:
        return set()
    top = max(scores.values())
    return {intent for intent, score in scores.items() if top - score <= AMBIGUITY_DELTA}


def replay_problems(signals: dict[str, dict]) -> list[str]:
    """Hold the FLOW keywords to the hub gold rows that name the FigJam packet."""
    problems: list[str] = []
    try:
        cases = json.loads((ROOT / CASES).read_text(encoding="utf-8"))["cases"]
    except (OSError, KeyError, json.JSONDecodeError) as error:
        return [f"replay could not read {CASES}: {error}"]
    for case in cases:
        request, expect = case["request"], case["expect"]
        kept = replay_intents(request, signals)
        if expect == FIGJAM_PACKET and kept != {"FLOW"}:
            problems.append(f"ROUTER.md keywords replay {request!r} as {sorted(kept) or 'no intent'}, expected FLOW")
        if expect == DEFAULT_PACKET and kept == {"FLOW"}:
            problems.append(f"ROUTER.md keywords replay {request!r} as FLOW, but the hub keeps it in {DEFAULT_PACKET}")
    return problems


# ───────────────────────────────────────────────────────────────
# 3. ENTRY POINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Run every lane, packet and replay check and print one verdict."""
    errors: list[str] = []
    try:
        default_resources, resource_map, intent_signals = parse_router()
        manifest = json.loads((ROOT / "leaf-manifest.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, KeyError, SyntaxError, json.JSONDecodeError) as error:
        print(f"FAILED leaf map parity: {error}")
        return 1

    modes = {entry["workflowMode"]: entry for entry in manifest.get("modes", [])}
    lane_keys = set(resource_map)
    crosswalk_keys = set(LANE_TO_PACKET)
    if lane_keys != crosswalk_keys:
        fail(f"ROUTER.md lanes {sorted(lane_keys)} differ from documented crosswalk {sorted(crosswalk_keys)}", errors)

    packets = set(LANE_TO_PACKET.values())
    if set(modes) != packets:
        fail(f"leaf-manifest workflow modes {sorted(modes)} differ from mapped packets {sorted(packets)}", errors)

    def check_resources(label: str, packet: str, resources: list[str]) -> None:
        """Require each resource to be packet-qualified, registered and on disk."""
        entry = modes.get(packet)
        if entry is None:
            fail(f"{label} maps to missing manifest packet {packet}", errors)
            return
        registered = set(entry.get("leaves", []))
        for resource in resources:
            prefix = f"{packet}/"
            if not resource.startswith(prefix):
                fail(f"{label} resource {resource} is not packet-qualified for {packet}", errors)
                continue
            leaf = resource[len(prefix):]
            if leaf not in registered:
                fail(f"{label} resource {resource} is absent from {packet} manifest leaves", errors)
            if not (ROOT / resource).is_file():
                fail(f"{label} resource {resource} is missing on disk", errors)

    check_resources("DEFAULT_RESOURCE", DEFAULT_PACKET, default_resources)
    for lane, packet in LANE_TO_PACKET.items():
        resources = resource_map.get(lane, [])
        if not resources:
            fail(f"ROUTER.md lane {lane} has no resources", errors)
        check_resources(lane, packet, resources)

    errors.extend(replay_problems(intent_signals))
    for lane, intent in VENDORED_LANE_INTENT.items():
        try:
            wanted = packet_leaves(LANE_TO_PACKET[lane], intent)
        except (OSError, ValueError, KeyError, SyntaxError) as error:
            fail(f"{lane} could not be compared with its packet: {error}", errors)
            continue
        if resource_map.get(lane) != wanted:
            fail(f"{lane} loads {resource_map.get(lane)}, but the {LANE_TO_PACKET[lane]} {intent} intent loads {wanted}", errors)

    if errors:
        print(f"FAILED leaf map parity: {len(errors)} finding(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"PASSED {len(lane_keys)} router lanes and DEFAULT_RESOURCE match {len(modes)} packet manifests, "
        "including FLOW, and the FLOW keywords replay every hub gold row"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

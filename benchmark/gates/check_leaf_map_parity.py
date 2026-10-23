#!/usr/bin/env python3
"""Check that every router lane maps to a packet manifest and registered leaf."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

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


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def parse_router() -> tuple[list[str], dict[str, list[str]]]:
    source = (ROOT / "ROUTER.md").read_text(encoding="utf-8")
    match = re.search(r"```python\s*(.*?)\s*```", source, re.S)
    if not match:
        raise ValueError("ROUTER.md has no Python resource map")
    tree = ast.parse(match.group(1))
    values = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in {"DEFAULT_RESOURCE", "RESOURCE_MAP"}:
                values[name] = ast.literal_eval(node.value)
    return values["DEFAULT_RESOURCE"], values["RESOURCE_MAP"]


def main() -> int:
    errors: list[str] = []
    try:
        default_resources, resource_map = parse_router()
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

    if errors:
        print(f"FAILED leaf map parity: {len(errors)} finding(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASSED {len(lane_keys)} router lanes and DEFAULT_RESOURCE match {len(modes)} packet manifests, including FLOW")
    return 0


if __name__ == "__main__":
    sys.exit(main())

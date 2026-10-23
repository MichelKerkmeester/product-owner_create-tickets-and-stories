#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: HUB GATE
# ───────────────────────────────────────────────────────────────

"""Hold the hub files, the packet registry and stage one routing together.

The repository root is a parent hub. The hub `SKILL.md`, `mode-registry.json`
and `hub-router.json` pick a packet, and each packet routes inside itself. A
hub drifts without a sound: a new packet folder nobody registers, a default
that names a different packet in each file, or a packet `SKILL.md` that lost
its pointer to the router and grew a routing section again. None of those
breaks a fixture, because the fixtures call the packet router directly.

This gate reads the hub the way Moneybird Accountant's route-table checker
does, with one exemption that system has no use for. A vendored packet is a
byte-identical copy of a shared skill, so it carries no Product Owner
`ROUTER.md` and routes inside its own `SKILL.md`. A registry row marked
`"vendored": true` is held to that shape instead, and only when `vendor.json`
lists the same folder and the row is a non-default tool packet, so the mark
cannot excuse a packet nobody vendors or lift the router checks off the default.

The gold rows replay stage one. They are the requests most likely to be
misrouted when the tool packet sits beside the default one: a bare request,
the existing figma Task fixture, a request that names only a figma-ds-cli
operation, negated mentions, and tool mentions inside an artifact request or
beside a `$` command.
Stage two is the router fixtures' job, so the figma row only proves its
fixture still exists and still routes to Task.

Usage:
  check_hub.py             -> exit 0 when the hub, the registry and the gold rows agree
  check_hub.py --self-test -> prove the gate fails on five planted defects
"""
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("PO_ROOT") or HERE.parent.parent)

HUB_FILES = ("SKILL.md", "mode-registry.json", "hub-router.json")
VENDOR_FILE = "vendor.json"
ROUTER_STATE_LINE = "router_state: active"
SKILL_POINTER_LINE = "skill_pointer: SKILL.md"
# A router emptied to its frontmatter still passes the header lines, so its body
# must keep the sections differential.py and the model read.
ROUTER_SECTIONS = ("## 2. SMART ROUTING", "### Semantic Topics", "### Resource Loading Levels", "### Executable Contract")
# A packet SKILL.md that carries one of these again has a second router beside ROUTER.md.
EMBEDDED_ROUTER_MARKS = ("### Semantic Topics", "### Resource Loading Levels", "### Executable Contract", "### Confidence Thresholds")
PACKET_KINDS = {True: "workflow", False: "tool"}
FRONTMATTER_NAME = re.compile(r"^name:\s*(.+)$", re.M)
FIXTURES = Path("benchmark/router/fixtures.json")

GOLD_ROWS = (
    ("a bare request", "the onboarding checklist skips step two for new creators", "product-owner"),
    ("the existing figma Task fixture", "figma says the padding is 8px off on the empty state", "product-owner"),
    ("a figma-ds-cli-only request", "figma-ds-cli fj nodes", "mcp-figma"),
    ("a negated figma-ds-cli mention", "do not use figma-ds-cli, the empty state padding is off", "product-owner"),
    ("a negation far back in its clause", "do not under any circumstances use figma-ds-cli", "product-owner"),
    ("a curly-apostrophe negation", "don\u2019t use figma-ds-cli, fix the padding", "product-owner"),
    ("a negation in an earlier clause", "don't worry, figma-ds-cli fj nodes", "mcp-figma"),
    ("a tool named inside a task request", "run figma-ds-cli fj nodes and write a task for the spacing", "product-owner"),
    ("a tool named beside a command", "$d figma-ds-cli fj nodes", "product-owner"),
    ("a tool named inside a document request", "document how figma-ds-cli handles auth", "product-owner"),
    ("a tool named inside a PRD request", "write a PRD for the figma-ds-cli rollout", "product-owner"),
)
FIGMA_FIXTURE = GOLD_ROWS[1][1]
FIGMA_FIXTURE_INTENT = "TASK"


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def frontmatter(text: str) -> list[str]:
    lines = text.split("\n")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return []
    return lines[1:lines.index("---", 1)]


def vendored_folders() -> set[str]:
    data = read_json(ROOT / VENDOR_FILE)
    packages = data.get("packages") if isinstance(data, dict) else None
    return {str(item.get("local_path")) for item in packages or [] if isinstance(item, dict)}


def check_packet(mode: dict, hub_text: str, vendored: set[str], problems: list[str]) -> None:
    packet = str(mode.get("packet"))
    skill = ROOT / packet / "SKILL.md"
    if not skill.is_file():
        problems.append(f"registry packet has no SKILL.md: {packet}")
        return
    skill_text = read_text(skill)
    expected_kind = PACKET_KINDS[mode.get("default") is True]
    if mode.get("packetKind") != expected_kind:
        problems.append(f"registry packetKind of {packet} is {mode.get('packetKind')}, expected {expected_kind}")
    declared = FRONTMATTER_NAME.search("\n".join(frontmatter(skill_text)))
    if not declared or mode.get("packetSkillName") != declared.group(1).strip("\"'"):
        problems.append(f"registry packetSkillName of {packet} does not match its SKILL.md name")

    if mode.get("vendored") is True:
        if mode.get("default") is True or mode.get("packetKind") != PACKET_KINDS[False]:
            problems.append(f"vendored packet {packet} must be a non-default {PACKET_KINDS[False]} packet")
        if packet not in vendored:
            problems.append(f"registry marks {packet} vendored but {VENDOR_FILE} does not list it")
        if mode.get("router") != f"{packet}/SKILL.md":
            problems.append(f"vendored packet router is not {packet}/SKILL.md: {mode.get('router')}")
        if f"({packet}/SKILL.md)" not in hub_text:
            problems.append(f"hub SKILL.md does not link the vendored packet: {packet}/SKILL.md")
        return

    if mode.get("router") != f"{packet}/ROUTER.md":
        problems.append(f"registry router is not {packet}/ROUTER.md: {mode.get('router')}")
    router_text = read_text(ROOT / packet / "ROUTER.md")
    header = frontmatter(router_text)
    if not header:
        problems.append(f"packet has no router: {packet}/ROUTER.md")
    else:
        for line in (ROUTER_STATE_LINE, SKILL_POINTER_LINE):
            if line not in header:
                problems.append(f"{packet}/ROUTER.md frontmatter lacks: {line}")
        for section in ROUTER_SECTIONS:
            if section not in router_text:
                problems.append(f"{packet}/ROUTER.md lacks its section: {section}")
    if f"({packet}/ROUTER.md)" not in hub_text:
        problems.append(f"hub SKILL.md does not link the packet router: {packet}/ROUTER.md")
    for mark in EMBEDDED_ROUTER_MARKS:
        if mark in skill_text:
            problems.append(f"packet SKILL.md embeds a router: {packet}/SKILL.md holds {mark}")
    if "](ROUTER.md)" not in skill_text:
        problems.append(f"packet SKILL.md does not point to its router: {packet}/SKILL.md")


def check_hub() -> list[str]:
    problems = [f"missing hub file: {name}" for name in HUB_FILES if not (ROOT / name).is_file()]
    registry = read_json(ROOT / "mode-registry.json")
    modes = registry.get("modes") if isinstance(registry, dict) else None
    if not isinstance(modes, list) or not modes or not all(isinstance(mode, dict) for mode in modes):
        return problems + ["mode-registry.json has no modes list of objects"]
    defaults = [mode.get("workflowMode") for mode in modes if mode.get("default") is True]
    if len(defaults) != 1:
        problems.append(f"mode-registry.json needs exactly one default mode, found {len(defaults)}")
    hub_text = read_text(ROOT / "SKILL.md")
    vendored = vendored_folders()
    for mode in modes:
        check_packet(mode, hub_text, vendored, problems)

    packets = {str(mode.get("packet")) for mode in modes}
    for entry in sorted(os.listdir(ROOT)):
        if not entry.startswith(".") and entry not in packets and (ROOT / entry / "SKILL.md").is_file():
            problems.append(f"packet folder is not in mode-registry.json: {entry}")

    stage_one = read_json(ROOT / "hub-router.json")
    policy = stage_one.get("routerPolicy") if isinstance(stage_one, dict) else None
    signals = stage_one.get("signals") if isinstance(stage_one, dict) else None
    if not isinstance(policy, dict) or not isinstance(signals, dict):
        return problems + ["hub-router.json needs a routerPolicy and a signals object"]
    if defaults and policy.get("defaultMode") != defaults[0]:
        problems.append(f"hub-router.json defaultMode {policy.get('defaultMode')} is not the registry default {defaults[0]}")
    if sorted(signals) != sorted(str(mode.get("workflowMode")) for mode in modes):
        problems.append("hub-router.json signals do not name the registry modes")
    for name, values in sorted(signals.items()):
        if not isinstance(values, list) or not all(isinstance(value, str) and value.strip() for value in values):
            problems.append(f"hub-router.json signals for {name} are not a list of phrases")
        elif not values and name not in defaults:
            problems.append(f"hub-router.json signals for {name} are empty and it is not the default")
    for key in ("artifactWords", "negations"):
        if not isinstance(policy.get(key), list) or not policy.get(key):
            problems.append(f"hub-router.json routerPolicy needs a non-empty {key} list")
    return problems


def _word(phrase: str) -> re.Pattern:
    # Whole words only, and a hyphen counts as part of a word, so figma never matches inside figma-ds-cli.
    return re.compile(r"(?<![\w-])" + re.escape(phrase.lower()) + r"(?![\w-])")


def route_stage_one(request: str, stage_one: dict) -> str:
    """Pick the packet for a request, by the rules the hub SKILL.md states."""
    policy, signals = stage_one["routerPolicy"], stage_one["signals"]
    # A curly apostrophe and a doubled space are the same request as their plain forms.
    text = " ".join(request.lower().replace("\u2019", "'").split())
    if re.search(r"(?<!\S)\$[a-z]", text):
        return policy["defaultMode"]
    if any(_word(word).search(text) for word in policy["artifactWords"]):
        return policy["defaultMode"]
    negations = {word.lower() for word in policy["negations"]}
    hits = set()
    # A negation reaches back to the start of its clause and no further.
    for clause in re.split(r"[,.;:!?]", text):
        for mode, phrases in signals.items():
            for phrase in phrases:
                for match in _word(phrase).finditer(clause):
                    if not negations.intersection(re.findall(r"[\w'-]+", clause[:match.start()])):
                        hits.add(mode)
    return hits.pop() if len(hits) == 1 else policy["defaultMode"]


def gold_problems() -> list[str]:
    stage_one = read_json(ROOT / "hub-router.json")
    try:
        routed = [(label, request, expected, route_stage_one(request, stage_one)) for label, request, expected in GOLD_ROWS]
    except (KeyError, TypeError) as error:
        return [f"hub gold rows could not run: hub-router.json lacks {error}"]
    problems = [f"hub gold row {label}: {request!r} routed to {got}, expected {expected}"
                for label, request, expected, got in routed if got != expected]
    fixtures = read_json(ROOT / FIXTURES) or []
    row = next((item for item in fixtures if isinstance(item, dict) and item.get("input") == FIGMA_FIXTURE), None)
    if row is None or row.get("expect", {}).get("intent") != FIGMA_FIXTURE_INTENT:
        problems.append(f"hub gold row the existing figma Task fixture: {FIXTURES} no longer holds {FIGMA_FIXTURE!r} as {FIGMA_FIXTURE_INTENT}")
    return problems


def check() -> int:
    problems = check_hub()
    if not problems:
        problems = gold_problems()
    if problems:
        for problem in problems:
            print(f"  {problem}")
        print(f"FAILED {len(problems)} hub problem(s)")
        return 1
    print(f"PASSED the hub, {len(read_json(ROOT / 'mode-registry.json')['modes'])} registry packets and {len(GOLD_ROWS)} gold rows")
    return 0


def self_test() -> int:
    """Copy the hub to a scratch tree, plant five defects one at a time, require each to fail."""
    global ROOT
    original = ROOT
    results = []
    with tempfile.TemporaryDirectory(prefix="po-hub-selftest-") as scratch:
        tree = Path(scratch)
        for relative in (*HUB_FILES, VENDOR_FILE, "sk-product-owner/SKILL.md", "sk-product-owner/ROUTER.md",
                         "mcp-figma/SKILL.md", str(FIXTURES)):
            target = tree / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original / relative, target)
        ROOT = tree
        try:
            results.append(("the clean copy passes", check() == 0))

            stray = tree / "sk-stray"
            stray.mkdir()
            (stray / "SKILL.md").write_text("---\nname: sk-stray\n---\n", encoding="utf-8")
            results.append(("an unregistered packet folder fails", check() == 1))
            shutil.rmtree(stray)

            hub_router = tree / "hub-router.json"
            clean = hub_router.read_text(encoding="utf-8")
            data = json.loads(clean)
            data["routerPolicy"]["defaultMode"] = "mcp-figma"
            hub_router.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            results.append(("a wrong defaultMode fails", check() == 1))
            hub_router.write_text(clean, encoding="utf-8")

            skill = tree / "sk-product-owner" / "SKILL.md"
            clean = skill.read_text(encoding="utf-8")
            skill.write_text(clean.replace("](ROUTER.md)", "](router.md)"), encoding="utf-8")
            results.append(("a missing ](ROUTER.md) pointer fails", check() == 1))
            skill.write_text(clean, encoding="utf-8")

            vendor = tree / VENDOR_FILE
            clean = vendor.read_text(encoding="utf-8")
            vendor.write_text(json.dumps({"packages": []}) + "\n", encoding="utf-8")
            results.append(("a vendored row vendor.json does not list fails", check() == 1))
            vendor.write_text(clean, encoding="utf-8")

            registry = tree / "mode-registry.json"
            clean = registry.read_text(encoding="utf-8")
            data = json.loads(clean)
            data["modes"][0]["vendored"] = True
            registry.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            results.append(("a default packet marked vendored fails", check() == 1))
            registry.write_text(clean, encoding="utf-8")

            results.append(("the restored copy passes", check() == 0))
        finally:
            ROOT = original
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return 0 if all(ok for _, ok in results) else 1


def main() -> int:
    if "--self-test" in sys.argv[1:]:
        return self_test()
    return check()


if __name__ == "__main__":
    sys.exit(main())

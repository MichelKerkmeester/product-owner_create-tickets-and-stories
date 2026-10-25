#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: HUB GATE
# ───────────────────────────────────────────────────────────────

"""Hold the hub files, the packet registry and stage one routing together.

The hub is the repository root and follows the skilled parent-hub contract:
`mode-registry.json` and `hub-router.json` pick a mode, the root `ROUTER.md`
maps the request's intent to that mode's leaves, and each workflow packet
routes inside its own `SKILL.md` Section 2. A hub drifts without a sound: a new
packet folder nobody registers, a default that names a vendored packet, or a
packet that grows its own `ROUTER.md` or identity file again. None of those
breaks a fixture, because the fixtures call the packet router directly.

The skilled checker holds the schema. This gate holds what only Product Owner
has: the vendored packets, which are byte copies of shared skills and route
inside their own `SKILL.md`, and the stage one rules the hub `SKILL.md` states.
A packet the registry's `vendored-packets` extension names must also be listed
in `vendor.json`, and the default may never be one, so the mark cannot excuse a
packet nobody vendors or lift the packet checks off the default. Every other
packet is a workflow packet that keeps its routing in `SKILL.md` Section 2,
held to the skilled smart-router markers.

The gold rows in `benchmark/hub-routing-cases.json` replay stage
one. Stage two is the router fixtures' job, so the figma row only proves its
fixture still exists and still routes to Task.

Usage:
  check_hub.py             -> exit 0 when the hub, the registry and the gold rows agree
  check_hub.py --self-test -> prove the gate fails on eleven planted defects
"""
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("PO_ROOT") or HERE.parent.parent)

HUB_FILES = ("SKILL.md", "ROUTER.md", "mode-registry.json", "hub-router.json",
             "description.json", "graph-metadata.json", "leaf-manifest.json")
VENDOR_FILE = "vendor.json"
VENDOR_EXTENSION = "vendored-packets"
CASES = Path("benchmark/hub-routing-cases.json")
FIXTURES = Path("benchmark/router/fixtures.json")
ROUTER_STATE_LINE = "router_state: active"
SKILL_POINTER_LINE = "skill_pointer: SKILL.md"
# Only the hub carries a router or an identity, so a packet holding one of these has a second.
PACKET_RESIDUE = ("ROUTER.md", "graph-metadata.json", "description.json", "leaf-manifest.json",
                  "leaf-manifest.config.json", "leaf-aliases.json")
# The skilled validator reads these in a packet's SMART ROUTING section.
SMART_ROUTER_MARKERS = ("discover_markdown_resources", "_guard_in_skill", "UNKNOWN_FALLBACK")
SMART_ROUTING_SECTION = re.compile(r"^## 2\. SMART ROUTING\n(.*?)(?=^## )", re.M | re.S)
WORKFLOW_KIND = "workflow"
FRONTMATTER_NAME = re.compile(r"^name:\s*(.+)$", re.M)
FIGMA_FIXTURE_LABEL = "the existing figma Task fixture"
FIGMA_FIXTURE_INTENT = "TASK"
STAGE_ONE_RULES = (
    ("packet-commands", "commands", {
        "routerPolicy.packetCommands",
        "routerPolicy.energyCommands",
        "routerPolicy.defaultMode",
    }),
    ("artifact-request-before-opening-signal", "artifact-request", {
        "vocabularyClasses.artifact-request-verbs",
        "vocabularyClasses.artifact-request-fillers",
        "vocabularyClasses.artifact-request-nouns",
        "vocabularyClasses.artifact-request-indefinite-verbs",
        "vocabularyClasses.artifact-request-indefinite-openers",
        "routerPolicy.defaultMode",
    }),
    ("opening-packet-signal", "opening-signal", {
        "routerSignals",
        "vocabularyClasses",
        "routerPolicy.defaultMode",
    }),
    ("default-artifact-word", "artifact-word", {
        "routerSignals[defaultMode]",
        "vocabularyClasses",
        "routerPolicy.defaultMode",
    }),
    ("single-packet-signal", "single-signal", {
        "routerSignals",
        "vocabularyClasses",
        "routerPolicy.negations",
        "routerPolicy.defaultMode",
    }),
    ("default-mode", "default", {"routerPolicy.defaultMode"}),
)
STAGE_ONE_POINTER = "routerPolicy.stageOneOrder"
STAGE_ONE_FIRST_MATCH = "first matching rule wins"


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────

def hub() -> Path:
    """The hub root, read at call time so the self-test can point it at a scratch tree."""
    return ROOT


def read_json(path: Path) -> Any:
    """The parsed JSON at path, or None when it is missing or malformed."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def read_text(path: Path) -> str:
    """The text at path, or an empty string when it cannot be read."""
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def frontmatter(text: str) -> list[str]:
    """The lines between the opening and closing `---`, or nothing when there is no frontmatter."""
    lines = text.split("\n")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return []
    return lines[1:lines.index("---", 1)]


def vendored_folders() -> set[str]:
    """Every local path vendor.json lists as a vendored package."""
    data = read_json(ROOT / VENDOR_FILE)
    packages = data.get("packages") if isinstance(data, dict) else None
    return {str(item.get("local_path")) for item in packages or [] if isinstance(item, dict)}


def vendored_packets(registry: dict) -> set[str]:
    """Every packet the registry's vendored-packets extension marks."""
    extension = (registry.get("extensions") or {}).get(VENDOR_EXTENSION)
    packets = extension.get("packets") if isinstance(extension, dict) else None
    return {str(packet) for packet in packets or []}


def class_keywords(router: dict, mode: str) -> list[str]:
    """Every keyword of the vocabulary classes a mode's routerSignals entry names."""
    signal = router["routerSignals"][mode]
    classes = router["vocabularyClasses"]
    return [word for name in signal["classes"] for word in classes[name]["keywords"]]


# ───────────────────────────────────────────────────────────────
# 3. HUB CHECKS
# ───────────────────────────────────────────────────────────────

def check_packet(mode: dict, hub_text: str, vendored: set[str], listed: set[str], problems: list[str]) -> None:
    """Hold one registry packet to its SKILL.md, the hub link and the vendored or workflow rules."""
    packet = str(mode.get("packet"))
    skill = hub() / packet / "SKILL.md"
    if not skill.is_file():
        problems.append(f"registry packet has no SKILL.md: {packet}")
        return
    skill_text = read_text(skill)
    declared = FRONTMATTER_NAME.search("\n".join(frontmatter(skill_text)))
    if not declared or mode.get("packetSkillName") != declared.group(1).strip("\"'"):
        problems.append(f"registry packetSkillName of {packet} does not match its SKILL.md name")
    if f"({packet}/SKILL.md)" not in hub_text:
        problems.append(f"hub SKILL.md does not link the packet: {packet}/SKILL.md")

    if packet in vendored:
        if packet not in listed:
            problems.append(f"registry marks {packet} vendored but {VENDOR_FILE} does not list {packet}")
        return

    if mode.get("packetKind") != WORKFLOW_KIND:
        problems.append(f"registry packetKind of {packet} is {mode.get('packetKind')}, expected {WORKFLOW_KIND}")
    for name in PACKET_RESIDUE:
        if (hub() / packet / name).exists():
            problems.append(f"packet carries a hub-only file: {packet}/{name}")
    section = SMART_ROUTING_SECTION.search(skill_text)
    if not section:
        problems.append(f"packet SKILL.md has no Section 2 SMART ROUTING: {packet}/SKILL.md")
    else:
        for marker in SMART_ROUTER_MARKERS:
            if marker not in section.group(1):
                problems.append(f"{packet}/SKILL.md Section 2 lacks the smart-router marker {marker}")


def check_router(problems: list[str]) -> None:
    """Require the hub ROUTER.md frontmatter to mark the router active and point at SKILL.md."""
    header = frontmatter(read_text(hub() / "ROUTER.md"))
    for line in (ROUTER_STATE_LINE, SKILL_POINTER_LINE):
        if line not in header:
            problems.append(f"ROUTER.md frontmatter lacks: {line}")


def check_hub() -> list[str]:
    """Every structural problem in the hub files, the registry and hub-router.json."""
    problems = [f"missing hub file: {name}" for name in HUB_FILES if not (hub() / name).is_file()]
    registry = read_json(hub() / "mode-registry.json")
    modes = registry.get("modes") if isinstance(registry, dict) else None
    if not isinstance(modes, list) or not modes or not all(isinstance(mode, dict) for mode in modes):
        return problems + ["mode-registry.json has no modes list of objects"]
    names = [str(mode.get("workflowMode")) for mode in modes]
    vendored = vendored_packets(registry)
    if not vendored <= {str(mode.get("packet")) for mode in modes}:
        problems.append(f"the {VENDOR_EXTENSION} extension names a packet the registry does not hold")
    hub_text = read_text(hub() / "SKILL.md")
    listed = vendored_folders()
    for mode in modes:
        check_packet(mode, hub_text, vendored, listed, problems)
    check_router(problems)

    packets = {str(mode.get("packet")) for mode in modes}
    # A folder the repo-root-hub extension declares the repository's own, such
    # as the vendored Code Mode server, may carry a SKILL.md without being a mode.
    repo_paths = set(((registry.get("extensions") or {}).get("repo-root-hub") or {}).get("repoPaths") or [])
    for entry in sorted(os.listdir(hub())):
        if entry.startswith(".") or entry in packets or entry in repo_paths:
            continue
        if (hub() / entry / "SKILL.md").is_file():
            problems.append(f"packet folder is not in mode-registry.json: {entry}")

    router = read_json(hub() / "hub-router.json")
    policy = router.get("routerPolicy") if isinstance(router, dict) else None
    signals = router.get("routerSignals") if isinstance(router, dict) else None
    classes = router.get("vocabularyClasses") if isinstance(router, dict) else None
    if not isinstance(policy, dict) or not isinstance(signals, dict) or not isinstance(classes, dict):
        return problems + ["hub-router.json needs a routerPolicy, a routerSignals and a vocabularyClasses object"]
    problems.extend(stage_one_order_problems(router))
    hub_stage_one = read_text(hub() / "SKILL.md")
    if STAGE_ONE_POINTER not in hub_stage_one or STAGE_ONE_FIRST_MATCH not in hub_stage_one:
        problems.append("hub SKILL.md Stage One Rules must point to hub-router.json and state that the first matching rule wins")
    default = policy.get("defaultMode")
    if default not in names:
        problems.append(f"hub-router.json defaultMode {default} is not a registry mode")
    elif default in vendored:
        problems.append(f"hub-router.json defaultMode {default} is a vendored packet")
    if sorted(signals) != sorted(names):
        problems.append("hub-router.json routerSignals do not name the registry modes")
    for name, signal in sorted(signals.items()):
        named = signal.get("classes") if isinstance(signal, dict) else None
        if not isinstance(named, list) or not named:
            problems.append(f"hub-router.json routerSignals for {name} name no vocabulary class")
            continue
        for cls in named:
            words = (classes.get(cls) or {}).get("keywords") if isinstance(classes.get(cls), dict) else None
            if not isinstance(words, list) or not words or not all(
                isinstance(word, str) and word.strip() for word in words
            ):
                problems.append(f"hub-router.json vocabulary class {cls} for {name} is not a non-empty list of phrases")
    for key in ("negations", "energyCommands"):
        if not isinstance(policy.get(key), list) or not policy.get(key):
            problems.append(f"hub-router.json routerPolicy needs a non-empty {key} list")
    commands = policy.get("packetCommands")
    if not isinstance(commands, dict):
        problems.append("hub-router.json routerPolicy needs a packetCommands object")
    else:
        for name, values in sorted(commands.items()):
            if name not in names or name == default:
                problems.append(
                    f"hub-router.json packetCommands names {name}, which is not a non-default registry mode"
                )
            elif not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.startswith("$") for value in values
            ):
                problems.append(f"hub-router.json packetCommands for {name} are not a list of $ commands")
    return problems


def stage_one_order_problems(router: dict) -> list[str]:
    """Require the declared rule contract to keep its stable, executable order."""
    policy = router.get("routerPolicy") if isinstance(router, dict) else None
    rules = policy.get("stageOneOrder") if isinstance(policy, dict) else None
    if not isinstance(rules, list):
        return ["hub-router.json routerPolicy.stageOneOrder must be an ordered list of rule objects"]
    expected_ids = [rule_id for rule_id, _, _ in STAGE_ONE_RULES]
    actual_ids = [rule.get("id") if isinstance(rule, dict) else None for rule in rules]
    problems = []
    if actual_ids != expected_ids:
        problems.append(
            "hub-router.json routerPolicy.stageOneOrder ids must appear in canonical order: "
            + ", ".join(expected_ids)
        )
    for index, (rule_id, kind, required_reads) in enumerate(STAGE_ONE_RULES):
        rule = rules[index] if index < len(rules) else None
        if not isinstance(rule, dict):
            problems.append(f"hub-router.json stage-one rule {rule_id} must be an object")
            continue
        if rule.get("kind") != kind:
            problems.append(f"hub-router.json stage-one rule {rule_id} must have kind {kind}")
        reads = rule.get("reads")
        if not isinstance(reads, list) or not all(isinstance(item, str) for item in reads):
            problems.append(f"hub-router.json stage-one rule {rule_id} must declare string read keys")
        elif not required_reads <= set(reads):
            missing = sorted(required_reads - set(reads))
            problems.append(f"hub-router.json stage-one rule {rule_id} omits read keys: {missing}")
    return problems


# ───────────────────────────────────────────────────────────────
# 4. STAGE ONE REPLAY
# ───────────────────────────────────────────────────────────────

def _word(phrase: str) -> re.Pattern:
    """A whole-word pattern for one phrase.

    A hyphen counts as part of a word, so figma never matches inside figma-ds-cli.
    """
    return re.compile(r"(?<![\w-])" + re.escape(phrase.lower()) + r"(?![\w-])")


def _phrase_at(tokens: list[str], index: int, phrase: str) -> bool:
    """Check a vocabulary phrase at a token position after request normalization."""
    phrase_tokens = phrase.lower().split()
    return tokens[index:index + len(phrase_tokens)] == phrase_tokens


def _artifact_request_matches(router: dict, rule: dict, text: str) -> bool:
    """Match a creation phrase followed by an artifact noun, using its declared classes."""
    classes = router["vocabularyClasses"]
    read = {
        key.split(".", 1)[1]: [word.lower() for word in classes[key.split(".", 1)[1]]["keywords"]]
        for key in rule["reads"]
        if key.startswith("vocabularyClasses.")
    }
    verbs = read.get("artifact-request-verbs", [])
    nouns = set(read.get("artifact-request-nouns", []))
    fillers = set(read.get("artifact-request-fillers", []))
    if not verbs or not nouns:
        return False
    # "add a task" asks for a new artifact, while "add the task to the sprint" acts on one
    # that already exists, so these verbs count only when an indefinite opener follows them.
    indefinite_verbs = read.get("artifact-request-indefinite-verbs", [])
    openers = set(read.get("artifact-request-indefinite-openers", []))
    tokens = re.findall(r"[\w-]+", text.lower())
    for start in range(len(tokens)):
        for verb in verbs + indefinite_verbs:
            if not _phrase_at(tokens, start, verb):
                continue
            cursor = start + len(verb.split())
            if verb in indefinite_verbs:
                if cursor >= len(tokens) or tokens[cursor] not in openers:
                    continue
                cursor += 1
            gap = 0
            while cursor < len(tokens) and tokens[cursor] in fillers and gap < 3:
                cursor += 1
                gap += 1
            if cursor < len(tokens) and tokens[cursor] in nouns:
                return True
    return False


def route_stage_one(request: str, router: dict) -> str:
    """Execute the hub-router.json stage-one rules in their declared order."""
    policy = router["routerPolicy"]
    default = policy["defaultMode"]
    signals = {mode: class_keywords(router, mode) for mode in router["routerSignals"] if mode != default}
    # A curly apostrophe and a doubled space are the same request as their plain forms.
    text = " ".join(request.lower().replace("’", "'").split())
    tokens = set(re.findall(r"(?<!\S)\$[a-z][\w-]*", text))
    energy_commands = {word.lower() for word in policy["energyCommands"]}
    default_words = class_keywords(router, default)
    negations = {word.lower() for word in policy["negations"]}

    for rule in policy["stageOneOrder"]:
        kind = rule["kind"]
        if kind == "commands":
            commands = tokens - energy_commands
            if commands:
                owners = [
                    mode for mode, words in policy["packetCommands"].items()
                    if commands <= {word.lower() for word in words}
                ]
                return owners[0] if len(owners) == 1 else default
        elif kind == "artifact-request":
            if _artifact_request_matches(router, rule, text):
                return default
        elif kind == "opening-signal":
            openers = {
                mode for mode, phrases in signals.items()
                if any((match := _word(phrase).search(text)) and match.start() == 0 for phrase in phrases)
            }
            if len(openers) == 1:
                return openers.pop()
        elif kind == "artifact-word":
            if any(_word(word).search(text) for word in default_words):
                return default
        elif kind == "single-signal":
            hits = set()
            # A full stop ends a clause only before a space or the end, so the dots in a
            # figma.com/board link stay inside the clause that carries the signal.
            for clause in re.split(r"[,;:!?]|\.(?=\s|$)", text):
                for mode, phrases in signals.items():
                    for phrase in phrases:
                        for match in _word(phrase).finditer(clause):
                            if not negations.intersection(re.findall(r"[\w'-]+", clause[:match.start()])):
                                hits.add(mode)
            if len(hits) == 1:
                return hits.pop()
        elif kind == "default":
            return default
        else:
            raise ValueError(f"unknown stage-one rule kind: {kind}")
    raise ValueError("hub-router.json routerPolicy.stageOneOrder has no matching default rule")


def gold_rows() -> list[dict]:
    """Every case object the hub gold rows file holds."""
    data = read_json(ROOT / CASES)
    cases = data.get("cases") if isinstance(data, dict) else None
    return [case for case in cases or [] if isinstance(case, dict)]


def gold_problems() -> list[str]:
    """Replay each gold row through stage one and confirm the figma row's fixture still exists."""
    router = read_json(hub() / "hub-router.json")
    rows = gold_rows()
    if not rows:
        return [f"hub gold rows are missing: {CASES} holds no cases"]
    try:
        routed = [
            (row["label"], row["request"], row["expect"], route_stage_one(row["request"], router))
            for row in rows
        ]
    except (KeyError, TypeError) as error:
        return [f"hub gold rows could not run: a case or hub-router.json lacks {error}"]
    problems = [f"hub gold row {label}: {request!r} routed to {got}, expected {expected}"
                for label, request, expected, got in routed if got != expected]
    figma = next((row["request"] for row in rows if row.get("label") == FIGMA_FIXTURE_LABEL), None)
    fixtures = read_json(ROOT / FIXTURES) or []
    row = next((item for item in fixtures if isinstance(item, dict) and figma and item.get("input") == figma), None)
    if row is None or row.get("expect", {}).get("intent") != FIGMA_FIXTURE_INTENT:
        problems.append(
            f"hub gold row {FIGMA_FIXTURE_LABEL}: {FIXTURES} no longer holds {figma!r} as {FIGMA_FIXTURE_INTENT}"
        )
    return problems


# ───────────────────────────────────────────────────────────────
# 5. CORE LOGIC
# ───────────────────────────────────────────────────────────────

def check() -> int:
    """Run the hub checks, then the gold rows once the hub is sound, and print one verdict."""
    problems = check_hub()
    if not problems:
        problems = gold_problems()
    if problems:
        for problem in problems:
            print(f"  {problem}")
        print(f"FAILED {len(problems)} hub problem(s)")
        return 1
    print(
        f"PASSED the hub, {len(read_json(hub() / 'mode-registry.json')['modes'])} registry packets and "
        f"{len(gold_rows())} gold rows"
    )
    return 0


# ───────────────────────────────────────────────────────────────
# 6. SELF-TEST
# ───────────────────────────────────────────────────────────────

def _edit_json(path: Path, change: Callable[[Any], Any]) -> str:
    """Apply one change to a JSON file and return its clean text for the restore."""
    clean = path.read_text(encoding="utf-8")
    data = json.loads(clean)
    change(data)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return clean


def self_test() -> int:
    """Copy the hub to a scratch tree and require each planted defect to fail."""
    global ROOT
    original = ROOT
    results = []
    packets = ("sk-product-owner", "sk-create-figjam", "mcp-figma", "mcp-click-up")
    with tempfile.TemporaryDirectory(prefix="po-hub-selftest-") as scratch:
        tree = Path(scratch)
        copies = [Path(name) for name in HUB_FILES]
        copies += [Path(packet) / "SKILL.md" for packet in packets]
        copies += [Path(VENDOR_FILE), CASES, FIXTURES]
        for relative in copies:
            target = tree / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original / relative, target)
        ROOT = tree
        hub_dir = tree
        hub_router = hub_dir / "hub-router.json"
        registry = hub_dir / "mode-registry.json"
        try:
            results.append(("the clean copy passes", check() == 0))

            stray = hub_dir / "sk-stray"
            stray.mkdir()
            (stray / "SKILL.md").write_text("---\nname: sk-stray\n---\n", encoding="utf-8")
            results.append(("an unregistered packet folder fails", check() == 1))
            shutil.rmtree(stray)

            owned = hub_dir / "mcp-code-mode"
            owned.mkdir()
            (owned / "SKILL.md").write_text("---\nname: mcp-code-mode\n---\n", encoding="utf-8")
            listed = "mcp-code-mode" in json.loads(registry.read_text(encoding="utf-8"))["extensions"][
                "repo-root-hub"
            ]["repoPaths"]
            results.append(("a skill folder the repository declares in repoPaths passes", listed and check() == 0))
            shutil.rmtree(owned)

            clean = _edit_json(hub_router, lambda data: data["routerPolicy"].update(defaultMode="mcp-figma"))
            results.append(("a vendored defaultMode fails", check() == 1))
            hub_router.write_text(clean, encoding="utf-8")

            def reorder_artifact_request(data: dict) -> None:
                """Swap the artifact-request rule with the opening-signal rule."""
                rules = data["routerPolicy"]["stageOneOrder"]
                request_index = next(i for i, rule in enumerate(rules)
                                     if rule["id"] == "artifact-request-before-opening-signal")
                signal_index = next(i for i, rule in enumerate(rules)
                                    if rule["id"] == "opening-packet-signal")
                rules[request_index], rules[signal_index] = rules[signal_index], rules[request_index]

            clean = _edit_json(hub_router, reorder_artifact_request)
            reordered = read_json(hub_router)
            routed_after_reorder = route_stage_one(
                "figjam the checkout flow, then write a story", reordered
            )
            results.append((
                "the JSON order executes and a reordered rule fails",
                routed_after_reorder == "sk-create-figjam" and check() == 1,
            ))
            hub_router.write_text(clean, encoding="utf-8")

            clean = _edit_json(
                hub_router,
                lambda data: data["routerPolicy"]["stageOneOrder"].pop(3),
            )
            results.append(("a missing stage-one rule fails", check() == 1))
            hub_router.write_text(clean, encoding="utf-8")

            residue = hub_dir / "sk-product-owner" / "ROUTER.md"
            residue.write_text("---\nrouter_state: active\n---\n", encoding="utf-8")
            results.append(
                (
                    "a packet ROUTER.md fails",
                    any("hub-only file" in problem for problem in check_hub()) and check() == 1,
                )
            )
            residue.unlink()

            vendor = tree / VENDOR_FILE
            clean = vendor.read_text(encoding="utf-8")
            vendor.write_text(json.dumps({"packages": []}) + "\n", encoding="utf-8")
            results.append(("a vendored packet vendor.json does not list fails", check() == 1))
            vendor.write_text(clean, encoding="utf-8")

            clean = _edit_json(
                registry,
                lambda data: data["extensions"][VENDOR_EXTENSION]["packets"].append("sk-product-owner"),
            )
            results.append(("a default packet marked vendored fails",
                            any("is a vendored packet" in problem for problem in check_hub()) and check() == 1))
            registry.write_text(clean, encoding="utf-8")

            cases_path = tree / CASES
            clean_cases = cases_path.read_text(encoding="utf-8")
            cases = json.loads(clean_cases)
            cases["cases"].append({
                "label": "a default artifact word before a packet signal",
                "request": "task figma-ds-cli",
                "expect": "sk-product-owner",
            })
            cases_path.write_text(json.dumps(cases, indent=2) + "\n", encoding="utf-8")

            def drop_task(data: dict) -> None:
                """Remove the word task from the default packet's artifact vocabulary."""
                words = data["vocabularyClasses"]["product-owner-artifacts"]["keywords"]
                data["vocabularyClasses"]["product-owner-artifacts"]["keywords"] = [
                    word for word in words if word != "task"
                ]
            clean = _edit_json(hub_router, drop_task)
            results.append(("a default artifact word gold row fails when its JSON term is missing",
                            check() == 1))
            hub_router.write_text(clean, encoding="utf-8")
            cases_path.write_text(clean_cases, encoding="utf-8")

            clean = _edit_json(
                hub_router,
                lambda data: data["routerPolicy"]["packetCommands"].update({"sk-create-figjam": ["$figjam"]}),
            )
            results.append(
                ("a Flow command missing from packetCommands fails its gold row", check_hub() == [] and check() == 1)
            )
            hub_router.write_text(clean, encoding="utf-8")

            skill = hub_dir / "sk-create-figjam" / "SKILL.md"
            clean = skill.read_text(encoding="utf-8")
            skill.write_text(clean.replace("_guard_in_skill", "_guard"), encoding="utf-8")
            results.append(("a packet Section 2 without a smart-router marker fails", check() == 1))
            skill.write_text(clean, encoding="utf-8")

            clean = _edit_json(registry, lambda data: data["modes"][1].update(packetKind="transport"))
            results.append(("a workflow packet registered as a transport fails", check() == 1))
            registry.write_text(clean, encoding="utf-8")

            results.append(("the restored copy passes", check() == 0))
        finally:
            ROOT = original
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return 0 if all(ok for _, ok in results) else 1


# ───────────────────────────────────────────────────────────────
# 7. ENTRY POINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Run the self-test when asked, the gate otherwise."""
    if "--self-test" in sys.argv[1:]:
        return self_test()
    return check()


if __name__ == "__main__":
    sys.exit(main())

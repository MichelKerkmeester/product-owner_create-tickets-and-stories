#!/usr/bin/env python3
"""Differential gate between the executable router and the router contract's pseudocode.

`references/router-contract.md` carries a Smart Router pseudocode block, the
exact algorithm the skill's prose routing section in `SKILL.md` summarizes,
and the executable route contract carries the same router as running Python.
Prose and code drift silently because nothing executes the prose, so this
gate executes it: the pseudocode block is lifted out of the markdown, run as
a real module, and compared against the route contract on every input in the
corpus.

Five guards fire, each on its own:

0. Prose parity. `SKILL.md` is what a model actually reads, and it carries a
   compact semantic topic table so a request reaching the scoring step can be
   routed from the prose alone. That table is a summary rather than a copy, so
   it is checked as a subset: every topic it names must exist in the
   executable tables in the same order, with the same route and the same
   confidence override, and every trigger word it prints must be a real
   synonym. A prose table that drifts is worse than no table, because it tells
   the reader to score vocabulary the router does not carry.
1. Copy parity. The Claude Project kernel used to inline the same block, and
   the check held that copy byte-identical to this one. A Project reads the
   contract as an uploaded Knowledge document instead, so the kernel now names
   that document and is held to carrying no python fence of its own, and the
   byte comparison runs against the uploaded copy the Project routes from.
2. Table parity. Semantic topics (order included, since order is the score
   tie-break), confidence thresholds, token and phrase regexes, resource lanes
   and the disambiguation checklist must match value for value. A table that
   drifts is caught here even when no corpus input happens to expose it.
3. Behavior parity. Every corpus input is routed through both, compared at the
   component level (energy, commands, framing, top topic and score) and then at
   the whole route object. Component comparison is what names the layer that
   drifted instead of only reporting a different answer.
4. Corpus coverage. Every artifact command and alias, every documented
   false-prefix case and every semantic topic must be exercised by the corpus,
   so behavior parity cannot pass by leaving a table untested.

The two implementations report a route differently, and the adapter below
reconciles the shapes without hiding a disagreement. The pseudocode names its
sources in prose ("explicit artifact command") where the contract uses a fixed
enum, it omits the confidence it already computed on the bare fallback branch,
and it carries a Doc drafting gate the contract deliberately does not simulate
because a bare request string supplies no source context. Everything else is
compared as-is.

Python 3.9 compatible.
"""
from __future__ import annotations

import ast
import json
import re
import sys
import types
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import route_contract as rc  # noqa: E402  (needs HERE on the path first)

REPO_ROOT = HERE.parent.parent
SKILL_MD = REPO_ROOT / "sk-product-owner" / "SKILL.md"
ROUTER_CONTRACT_MD = REPO_ROOT / "sk-product-owner" / "references" / "router-contract.md"
PROJECT_MD = REPO_ROOT / "claude project" / "Custom Instructions.md"
CORPUS_PATH = HERE / "differential_corpus.json"
FIXTURES_PATH = HERE / "fixtures.json"

KNOWLEDGE_ROOT = REPO_ROOT / "claude project" / "knowledge"

PSEUDOCODE_HEADING = "### Smart Router Pseudocode"
SKILL_TOPIC_TABLE_HEADING = "### Semantic Topics"
CONTRACT_HEADING = "### Executable Contract"

# Any fence a markdown renderer will highlight as python. A check written as the
# single literal "```python" anchored to a whole line is a check every ordinary
# spelling of the same fence walks straight past: the "py" alias, a capital in
# the language name, the trailing space an editor leaves behind, a fence opened
# with four backticks or with tildes, and the three spaces of indentation
# markdown still reads as a fence. A guard that names one spelling of the thing
# it forbids is a guard against typing that spelling.
#
# The braced forms walk past it too. A fence opened "```{python}" or
# "``` {.python}" is the executable-cell spelling several markdown toolchains
# read and highlight, so a router pasted back in under one of them is the same
# uncompared copy wearing a different hat.
PYTHON_FENCE_RE = re.compile(
    r"^[ ]{0,3}(?:`{3,}|~{3,})[ \t]*\{?[ \t]*\.?(?:python|python3|py|py3|ipython|sage)\b",
    re.M | re.I,
)

# Every spelling the matcher has to catch, pinned as a fixture. The matcher is
# the one thing standing between an always-loaded instruction file and a
# re-inlined router, and each system's harness carries its own copy of it, so
# each copy proves its own strength here rather than trusting a sibling.
PYTHON_FENCE_SPELLINGS = (
    "```python", "```py", "```python3", "```py3", "```ipython", "```sage",
    "```Python", "```python ", "````python", "~~~python", "   ```python",
    "```{python}", "``` {.python}",
)

# The prose table names a route where the tables name an intent.
ROUTE_LABEL_TO_INTENT = {"Task": "TASK", "Bug": "BUG", "Doc": "DOC", "Story": "STORY"}

# Enough trigger words per topic that the table is usable on its own. A row
# trimmed down to one word would still pass the subset check while telling a
# reader almost nothing about when the topic fires.
MIN_PROSE_TRIGGERS = 3

# The pseudocode reports its route decision in prose. The contract reports it as
# a fixed enum. Same decision, two vocabularies.
SOURCE_VOCABULARY = {
    "explicit artifact command": "command",
    "explicit artifact framing": "framing",
    "conflicting artifact commands": "conflict",
    "conflicting artifact framing": "conflict",
    "high-confidence semantic routing": "semantic",
    "medium-confidence semantic routing": "semantic",
    "quick semantic routing": "semantic",
    "quick task fallback": "quick-fallback",
    "fallback": "fallback",
}

# The pseudocode selects a mode by template name where the contract names the
# intent directly.
TEMPLATE_TO_INTENT = {
    "Task Mode": "TASK",
    "Bug Mode": "BUG",
    "Doc Mode": "DOC",
    "Story Mode": "STORY",
}

# Tokens that look like a command and must never fire one. Named here so the
# coverage guard can prove the corpus still exercises each of them.
REQUIRED_FALSE_PREFIXES = [
    "$document", "$docs", "$debug", "$prds", "$stories",
    "$sort", "$epics", "$email", "$e.md", "$d.md", "$doc/path",
]


# ---------------------------------------------------------------------------
# Guard 0: the prose topic table a model routes from
# ---------------------------------------------------------------------------

def parse_skill_topic_table() -> List[Tuple[str, str, List[str], Optional[float]]]:
    """Read the semantic topic table out of SKILL.md.

    Returns (topic, route label, trigger words, override) per row. The heading
    anchors the search, and the first non-table line after the rows begin ends
    it, so an unrelated later table cannot be read as more topics.
    """
    text = SKILL_MD.read_text(encoding="utf-8")
    if SKILL_TOPIC_TABLE_HEADING not in text:
        raise LookupError(f"SKILL.md has no {SKILL_TOPIC_TABLE_HEADING!r} section")
    tail = text[text.index(SKILL_TOPIC_TABLE_HEADING):]
    rows: List[Tuple[str, str, List[str], Optional[float]]] = []
    for line in tail.splitlines()[1:]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if rows:
                break
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) != 4:
            continue
        if cells[0].lower() == "topic" or set(cells[0]) <= set("-: "):
            continue
        triggers = [trigger.lower() for trigger in re.findall(r"`([^`]+)`", cells[2])]
        override = None if cells[3].strip().lower() == "none" else float(cells[3])
        rows.append((cells[0], cells[1], triggers, override))
    return rows


def check_prose_table_parity() -> List[str]:
    """Prove the table in SKILL.md is a true subset of the executable tables.

    Prose and code drift silently in both directions. Guard 2 already pins the
    pseudocode against the contract, but neither of those is the surface a
    model reads to route a request, and moving the pseudocode out of SKILL.md
    once left the prose instructing a scoring step whose vocabulary it no
    longer carried. Every gate stayed green while five of eighteen real
    requests became unroutable. This is the check that would have failed.
    """
    failures: List[str] = []
    rows = parse_skill_topic_table()
    if not rows:
        return [f"prose parity: no topic rows found under {SKILL_TOPIC_TABLE_HEADING!r}"]

    prose_topics = [row[0] for row in rows]
    contract_topics = list(rc.SEMANTIC_TOPICS)
    if prose_topics != contract_topics:
        return [
            f"prose parity topic order: SKILL.md {prose_topics}, contract {contract_topics}"
        ]

    for topic, route, triggers, override in rows:
        config = rc.SEMANTIC_TOPICS[topic]
        expected_intent = config["intent"]
        if ROUTE_LABEL_TO_INTENT.get(route) != expected_intent:
            failures.append(
                f"prose parity route[{topic}]: SKILL.md {route!r}, contract {expected_intent!r}"
            )
        if override != config.get("confidence"):
            failures.append(
                f"prose parity override[{topic}]: SKILL.md {override!r}, "
                f"contract {config.get('confidence')!r}"
            )
        if len(triggers) < MIN_PROSE_TRIGGERS:
            failures.append(
                f"prose parity triggers[{topic}]: {len(triggers)} listed, "
                f"at least {MIN_PROSE_TRIGGERS} needed to be usable"
            )
        synonyms = {synonym.lower() for synonym in config["synonyms"]}
        unknown = [trigger for trigger in triggers if trigger not in synonyms]
        if unknown:
            failures.append(
                f"prose parity triggers[{topic}]: {unknown} are printed in SKILL.md "
                "but are not synonyms the router scores"
            )
    return failures


# ---------------------------------------------------------------------------
# Guard 1: lift the pseudocode and confirm the mirror copy matches
# ---------------------------------------------------------------------------

def extract_pseudocode(path: Path) -> str:
    """Return the Smart Router pseudocode block from a markdown file.

    The heading anchors the search so an unrelated python fence elsewhere in the
    document can never be picked up by accident.
    """
    text = path.read_text(encoding="utf-8")
    if PSEUDOCODE_HEADING not in text:
        raise LookupError(f"{path.name} has no {PSEUDOCODE_HEADING!r} section")
    tail = text[text.index(PSEUDOCODE_HEADING):]
    match = re.search(r"```python\n(.*?)\n```", tail, re.S)
    if not match:
        raise LookupError(f"{path.name} has no python block under {PSEUDOCODE_HEADING!r}")
    return match.group(1)


def _section(text: str, heading: str) -> str:
    """Return one heading's own body, ending where the next heading begins."""
    tail = text[text.index(heading) + len(heading):]
    nxt = re.search(r"\n#{2,4} ", tail)
    return tail[:nxt.start()] if nxt else tail


def knowledge_mirror() -> Tuple[Path, str]:
    """Return the uploaded Knowledge document mirroring the router contract, and its label.

    The sync compiler and its manifest are retired, and Knowledge documents are
    written by hand, so the mirror is found by name in the knowledge root rather
    than declared in a manifest. A Claude Project holds no filesystem and no
    references folder, so the uploaded Knowledge document is the only copy of the
    contract a kernel can reach, and exactly one document may carry it. The label
    is the document as a kernel writes it, without the system prefix the upload
    carries or the version suffix the filename appends.
    """
    candidates = sorted(path for path in KNOWLEDGE_ROOT.glob("*.md")
                        if "Router Contract" in path.name)
    if len(candidates) != 1:
        raise LookupError(
            f"the knowledge root holds {len(candidates)} Router Contract documents, so no "
            "single uploaded document is the one a kernel can point at"
        )
    label = re.sub(r" - v[0-9.]+\.md$", "", candidates[0].name.split(" - ", 1)[-1])
    return candidates[0], label


def check_copy_parity() -> List[str]:
    """Prove the kernel points at the router contract instead of carrying a copy of it.

    The kernel used to inline the contract's whole python fence, and this guard
    used to hold that inline copy byte-identical to the reference. The reasoning
    behind the inline copy was that a Claude Project has no filesystem to load a
    reference from, which is true of a reference and false of a Knowledge
    document, and the contract is registered as one. So the fence was a second
    full copy of a document the Project could already read, paid for on every
    conversation in the one file that is always in context, and the byte check on
    it was protecting the wrong copy.

    Three properties replace it, and together they are stronger than the one they
    replace. The kernel carries no python fence at all, so the router cannot come
    back inline under any spelling, and cannot come back untagged either, because
    the contract's own function signatures are searched for as well. The kernel
    names the Knowledge document, because an authority no surface names is an
    authority no runtime reaches. And that uploaded document stays byte-identical
    to the reference this gate executes, which is the original protection moved
    onto the copy the Project actually routes from: a cross-system overwrite
    lands as a whole block that parses, declares every expected table and still
    routes another system's requests, so table and behaviour parity can both
    agree with it and only the bytes disagree.
    """
    failures: List[str] = []

    for spelling in PYTHON_FENCE_SPELLINGS:
        if not PYTHON_FENCE_RE.search(f"{spelling}\nx = 1\n"):
            failures.append(
                f"copy parity: the python fence matcher no longer catches {spelling!r}, so a "
                "router pasted back under that spelling would clear every check below"
            )

    kernel_text = PROJECT_MD.read_text(encoding="utf-8")
    contract_block = extract_pseudocode(ROUTER_CONTRACT_MD)

    if PYTHON_FENCE_RE.search(kernel_text):
        failures.append(
            "copy parity: the Claude Project kernel carries a python fence, so the router is "
            "inlined in an instruction file again, paid for on every conversation, in a copy "
            f"nothing executes and nothing compares against {ROUTER_CONTRACT_MD.name}"
        )
    pasted = sorted({
        f"def {node.name}(" for node in ast.parse(contract_block).body
        if isinstance(node, ast.FunctionDef) and f"def {node.name}(" in kernel_text
    })
    if pasted:
        failures.append(
            f"copy parity: the kernel carries the contract's own definitions {pasted}, so the "
            "router is inlined under a fence tag no list anticipates, or under none at all"
        )

    try:
        mirror_path, label = knowledge_mirror()
    except LookupError as problem:
        return failures + [f"copy parity: {problem}"]

    if CONTRACT_HEADING not in kernel_text:
        failures.append(
            f"copy parity: the kernel has no {CONTRACT_HEADING!r} section, so the router it "
            "stopped carrying is named by nothing the Project reads"
        )
    elif label not in _section(kernel_text, CONTRACT_HEADING):
        failures.append(
            f"copy parity: the kernel's {CONTRACT_HEADING.strip('# ')} section never names the "
            f"{label!r} Knowledge document, so the routing authority is unreachable from the "
            "one surface a Project loads every conversation"
        )

    if not mirror_path.exists():
        failures.append(
            f"copy parity: the kernel points at {label!r} and {mirror_path.name} is not in the "
            "uploaded Knowledge folder, so the pointer reaches nothing"
        )
    elif mirror_path.read_bytes() != ROUTER_CONTRACT_MD.read_bytes():
        failures.append(
            f"copy parity: the uploaded {label!r} Knowledge document is no longer "
            f"byte-identical to {ROUTER_CONTRACT_MD.name} "
            f"({len(ROUTER_CONTRACT_MD.read_bytes())} vs {len(mirror_path.read_bytes())} "
            "bytes), so the Project routes from a copy this gate never executed"
        )

    skill_text = SKILL_MD.read_text(encoding="utf-8")
    if PYTHON_FENCE_RE.search(skill_text):
        failures.append(
            "copy parity: SKILL.md carries a python fence again, so the router exists in a "
            "copy no guard executes and no guard compares against the reference that owns it "
            f"({ROUTER_CONTRACT_MD.name})"
        )
    if CONTRACT_HEADING not in skill_text:
        failures.append(
            f"copy parity: SKILL.md has no {CONTRACT_HEADING!r} section, so the reference it "
            "stopped carrying is named by nothing a model reads"
        )
    else:
        relative = f"references/{ROUTER_CONTRACT_MD.name}"
        if relative not in _section(skill_text, CONTRACT_HEADING):
            failures.append(
                f"copy parity: SKILL.md's {CONTRACT_HEADING.strip('# ')} section names no path "
                f"to {relative}, so the executable contract is unreachable from the prose that "
                "replaced it"
            )
    return failures


def build_skill_router() -> types.ModuleType:
    """Execute the router contract's pseudocode as a module.

    `load` and `show_user` are the two runtime effects the pseudocode names but
    does not define, and both are side effects rather than routing decisions, so
    stubbing them changes nothing the gate compares. `__file__` points at
    `SKILL_MD`, a sibling of the `references/` and `assets/` folders the block's
    own resource discovery walks, even though the pseudocode text itself now
    comes from `ROUTER_CONTRACT_MD`, which sits one directory deeper.
    """
    module = types.ModuleType("skill_pseudocode_router")
    module.__dict__.update({
        "__file__": str(SKILL_MD),
        "load": lambda relative_path: None,
        "show_user": lambda *args, **kwargs: None,
    })
    source = extract_pseudocode(ROUTER_CONTRACT_MD)
    exec(compile(source, f"{ROUTER_CONTRACT_MD.name}::pseudocode", "exec"), module.__dict__)
    return module


# ---------------------------------------------------------------------------
# Guard 2: table parity
# ---------------------------------------------------------------------------

def _skill_topics(skill: types.ModuleType) -> List[Tuple[str, Tuple[str, ...], Optional[float], str]]:
    return [
        (
            topic,
            tuple(config["synonyms"]),
            config.get("confidence"),
            TEMPLATE_TO_INTENT.get(config["template"], "TASK"),
        )
        for topic, config in skill.SEMANTIC_TOPICS.items()
    ]


def _contract_topics() -> List[Tuple[str, Tuple[str, ...], Optional[float], str]]:
    return [
        (topic, tuple(config["synonyms"]), config.get("confidence"), config["intent"])
        for topic, config in rc.SEMANTIC_TOPICS.items()
    ]


def check_table_parity(skill: types.ModuleType) -> List[str]:
    failures: List[str] = []

    def compare(label: str, expected: Any, actual: Any) -> None:
        if expected != actual:
            failures.append(f"table parity {label}: skill {expected!r}, contract {actual!r}")

    skill_topics = _skill_topics(skill)
    contract_topics = _contract_topics()
    if [t[0] for t in skill_topics] != [t[0] for t in contract_topics]:
        failures.append(
            "table parity semantic topic order: skill "
            f"{[t[0] for t in skill_topics]}, contract {[t[0] for t in contract_topics]}"
        )
    else:
        for expected, actual in zip(skill_topics, contract_topics):
            topic = expected[0]
            if expected[1] != actual[1]:
                only_skill = [s for s in expected[1] if s not in actual[1]]
                only_contract = [s for s in actual[1] if s not in expected[1]]
                failures.append(
                    f"table parity synonyms[{topic}]: missing from contract {only_skill}, "
                    f"extra in contract {only_contract}"
                )
            compare(f"confidence[{topic}]", expected[2], actual[2])
            compare(f"intent[{topic}]", expected[3], actual[3])

    compare("CONFIDENCE_THRESHOLDS", skill.CONFIDENCE_THRESHOLDS, rc.CONFIDENCE_THRESHOLDS)
    compare("TOKEN_START", skill.TOKEN_START, rc.TOKEN_START)
    compare("TOKEN_END", skill.TOKEN_END, rc.TOKEN_END)
    compare("PHRASE_GAP_WORDS", skill.PHRASE_GAP_WORDS, rc.PHRASE_GAP_WORDS)
    compare("PHRASE_GAP", skill.PHRASE_GAP, rc.PHRASE_GAP)
    compare("FRAME_MODIFIER", skill.FRAME_MODIFIER, rc.FRAME_MODIFIER)

    # The skill's ALWAYS lane names the skill document itself and then skips it
    # while loading, because the document is already in context. The contract
    # lists only what it actually preloads.
    skill_always = [n for n in skill.RESOURCE_MAP["ALWAYS"] if n != "sk-product-owner/SKILL.md"]
    compare("ALWAYS", skill_always, rc.ALWAYS)
    compare("ON_DEMAND", skill.RESOURCE_MAP["ON_DEMAND"], rc.ON_DEMAND)
    for intent in ("TASK", "BUG", "DOC", "STORY", "INTERACTIVE"):
        compare(f"RESOURCE_MAP[{intent}]", skill.RESOURCE_MAP[intent], rc.RESOURCE_MAP[intent])

    # The shape tables decide which single scaffold the Story lane loads. They
    # drift the same way the intent tables do, and a drifted one is invisible
    # to behavior parity whenever no corpus input happens to reach the shape it
    # broke, so they are compared value for value here.
    compare("SHAPE_COMMANDS", skill.SHAPE_COMMANDS, rc.SHAPE_COMMANDS)
    compare("SHAPE_TEMPLATES", skill.SHAPE_TEMPLATES, rc.SHAPE_TEMPLATES)
    compare("SHAPE_PRECEDENCE", skill.SHAPE_PRECEDENCE, rc.SHAPE_PRECEDENCE)
    compare("SHAPE_FRAMES", skill.SHAPE_FRAMES, rc.SHAPE_FRAMES)
    compare("disambiguation checklist", skill.UNKNOWN_FALLBACK_CHECKLIST, rc.DISAMBIGUATION_CHECKLIST)
    return failures


# ---------------------------------------------------------------------------
# Guard 3: behavior parity
# ---------------------------------------------------------------------------

def skill_route(skill: types.ModuleType, text: str) -> Dict[str, Any]:
    """Adapt the pseudocode's route dict onto the contract's fixed field set."""
    raw = skill.route_product_owner_resources(text)
    named_source = raw.get("source")
    if named_source is None:
        # The LOW band returns a clarify target rather than a named source. It
        # is still the ask-one-question outcome the contract calls a fallback.
        source = "fallback"
    elif named_source in SOURCE_VOCABULARY:
        source = SOURCE_VOCABULARY[named_source]
    else:
        raise ValueError(f"unmapped pseudocode source {named_source!r} for {text!r}")

    confidence = raw.get("confidence")
    if confidence is None and named_source == "fallback":
        # The bare fallback branch tested a score and then dropped it from the
        # result. Recover it from the same function the branch called.
        confidence = skill.score_semantic_topics(text)[0].score

    resources = list(raw.get("resources") or [])
    inventory = skill.discover_markdown_resources()
    on_demand = [
        name for name in skill.RESOURCE_MAP["ON_DEMAND"]
        if name in inventory and name not in resources
    ]
    return {
        "intent": raw["intent"],
        "energy": raw["energy"],
        "source": source,
        # An Interactive outcome names no artifact, so it resolves no shape in
        # either router.
        "shape": raw.get("shape"),
        "confidence": confidence,
        # Both routers ask a question on exactly the Interactive outcomes, and
        # the contract's own output is asserted against that identity below, so
        # deriving it here cannot mask a disagreement.
        "needs_disambiguation": raw["intent"] == "INTERACTIVE",
        "resources": resources,
        "on_demand": on_demand,
    }


def compare_input(skill: types.ModuleType, text: str) -> List[str]:
    failures: List[str] = []
    normalized = " ".join((text or "").split())

    controls = skill.detect_controls(text)
    contract_energy = rc.detect_energy(normalized)
    if controls["energy"] != contract_energy:
        failures.append(f"energy: skill {controls['energy']!r}, contract {contract_energy!r}")

    contract_commands = rc.detect_commands(normalized)
    if controls["artifact_commands"] != contract_commands:
        failures.append(
            f"commands: skill {sorted(controls['artifact_commands'])}, "
            f"contract {sorted(contract_commands)}"
        )

    skill_frame = skill.detect_artifact_frame(text)
    contract_frame = rc.detect_framing(normalized)
    if skill_frame != contract_frame:
        failures.append(f"framing: skill {skill_frame!r}, contract {contract_frame!r}")

    best = skill.score_semantic_topics(text)[0]
    topic, score, _ = rc.score_semantic_topics(normalized)
    if (best.topic, best.score) != (topic, score):
        failures.append(
            f"semantic: skill {best.topic!r}@{best.score}, contract {topic!r}@{score}"
        )

    expected = skill_route(skill, text)
    actual = rc.route_request(text)
    schema_errors = rc.validate_route_object(actual)
    if schema_errors:
        failures.append(f"contract route object is not schema-valid: {schema_errors}")
        return failures
    if actual["needs_disambiguation"] != (actual["intent"] == "INTERACTIVE"):
        failures.append("contract asks a question on a route that is not Interactive")
    for field in rc.ROUTE_FIELDS:
        if expected[field] != actual[field]:
            failures.append(f"{field}: skill {expected[field]!r}, contract {actual[field]!r}")
    return failures


# ---------------------------------------------------------------------------
# Guard 4: corpus coverage
# ---------------------------------------------------------------------------

def check_coverage(skill: types.ModuleType, corpus: List[str]) -> List[str]:
    failures: List[str] = []

    tokens = sorted(set(rc.ARTIFACT_COMMANDS) | rc.QUICK_TOKENS)
    for token in tokens:
        if not any(rc.has_exact_token(text, token) for text in corpus):
            failures.append(f"coverage: no corpus input carries the command {token}")

    for prefix in REQUIRED_FALSE_PREFIXES:
        if not any(prefix.lower() in text.lower() for text in corpus):
            failures.append(f"coverage: no corpus input carries the false prefix {prefix}")

    reached = {rc.score_semantic_topics(" ".join(text.split()))[0] for text in corpus}
    for topic in rc.SEMANTIC_TOPICS:
        if topic not in reached:
            failures.append(f"coverage: no corpus input scores the {topic} topic highest")

    # Each shape has to be reached by something, or the split could drop a
    # scaffold from the loading contract and every gate would still pass.
    routed_shapes = {rc.route_request(text)["shape"] for text in corpus}
    for shape in rc.SHAPE_TEMPLATES:
        if shape not in routed_shapes:
            failures.append(f"coverage: no corpus input resolves the {shape} shape")
    return failures


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def read_json(path: Path) -> Any:
    """Read one of this harness's own input files, or say which one is missing.

    A renamed or deleted input is the one failure a gate must never blur into
    something else. An unhandled traceback here read as a Python bug rather than
    as "the corpus this run measured is not there", so the message names the file
    and the exit stays non-zero.
    """
    if not path.is_file():
        print(f"differential input missing: {path}", file=sys.stderr)
        sys.exit(2)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"invalid JSON in {path}: {exc}", file=sys.stderr)
        sys.exit(2)


def load_corpus() -> List[str]:
    """Fixture inputs first, then the grouped differential corpus, deduped."""
    corpus: List[str] = []
    seen = set()

    for fixture in read_json(FIXTURES_PATH):
        text = fixture["input"]
        if text not in seen:
            seen.add(text)
            corpus.append(text)

    groups = read_json(CORPUS_PATH)
    for group, inputs in groups.items():
        if not isinstance(inputs, list):
            raise ValueError(f"corpus group {group!r} is not a list of inputs")
        for text in inputs:
            if text not in seen:
                seen.add(text)
                corpus.append(text)
    return corpus


def main() -> int:
    failures = check_prose_table_parity()
    failures.extend(check_copy_parity())
    if failures:
        print("FAILED differential gate")
        for failure in failures:
            print(" -", failure)
        return 1

    skill = build_skill_router()
    failures.extend(check_table_parity(skill))

    corpus = load_corpus()
    failures.extend(check_coverage(skill, corpus))

    divergent = 0
    for text in corpus:
        problems = compare_input(skill, text)
        if problems:
            divergent += 1
            failures.append(f"input {text!r}")
            failures.extend(f"    {problem}" for problem in problems)

    if failures:
        print(f"FAILED differential gate: {divergent}/{len(corpus)} inputs diverge")
        for failure in failures:
            print(" -", failure)
        return 1

    prose_rows = parse_skill_topic_table()
    print(f"PASSED {len(corpus)}/{len(corpus)} differential inputs "
          f"({len(rc.SEMANTIC_TOPICS)} topics, "
          f"{sum(len(c['synonyms']) for c in rc.SEMANTIC_TOPICS.values())} synonyms in parity, "
          f"{sum(len(row[2]) for row in prose_rows)} SKILL.md triggers checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

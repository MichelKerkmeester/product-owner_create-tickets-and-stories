#!/usr/bin/env python3
"""Convert the scratch Product Owner copy into a parent hub. Run once on a fresh copy."""
import difflib
import json
import re
import sys
from pathlib import Path

PO = Path(sys.argv[1])
SKILL = PO / "sk-product-owner" / "SKILL.md"
ROUTER = PO / "sk-product-owner" / "ROUTER.md"
AGENTS = PO / "AGENTS.md"


def sub(path: Path, old: str, new: str, count: int = 1) -> None:
    text = path.read_text()
    assert text.count(old) >= 1, (path, old[:80])
    path.write_text(text.replace(old, new, count))


old_skill = SKILL.read_text().split("\n")
old_agents = AGENTS.read_text().split("\n")

# ── 1. Move SKILL.md Section 2 into ROUTER.md ─────────────────────────
start = old_skill.index("## 2. SMART ROUTING")
end = old_skill.index("## 3. HOW IT WORKS")
body = old_skill[start + 2:end]          # skip heading and its blank line
while body and body[-1] in ("", "---"):
    body.pop()
assert body[0].startswith("This section is the single Product Owner router"), body[0]
body[0] = body[0].replace("This section is the single Product Owner router",
                          "This file is the single Product Owner router", 1)

router_head = """---
title: "Product Owner Router"
description: "Stage two routing of the Product Owner packet."
trigger_phrases:
  - "product owner router"
importance_tier: important
contextType: general
version: 1.0.0.0
router_state: active
skill_pointer: SKILL.md
---

# Product Owner Router

## 1. OVERVIEW

The hub [`SKILL.md`](../SKILL.md) picks this packet, this file routes inside it and [`SKILL.md`](SKILL.md) holds its contract.

---

## 2. SMART ROUTING
"""
ROUTER.write_text(router_head + "\n" + "\n".join(body) + "\n")

pointer = ("Routing lives in [`ROUTER.md`](ROUTER.md). Read the hub [`SKILL.md`](../SKILL.md) first, "
           "then `ROUTER.md`, then this file.")
new_skill = old_skill[:start + 2] + [pointer, "", "---", ""] + old_skill[end:]
SKILL.write_text("\n".join(new_skill))
sub(SKILL, "Section 2 owns the full trigger vocabulary.", "`ROUTER.md` owns the full trigger vocabulary.")
sub(SKILL, "as the CONDITIONAL row in Section 2 pairs them.", "as the CONDITIONAL row in `ROUTER.md` pairs them.")

# The always-loaded row now names the hub and the router ahead of the contract.
sub(ROUTER, "| ALWAYS | `sk-product-owner/SKILL.md`,",
    "| ALWAYS | the hub `SKILL.md`, `sk-product-owner/ROUTER.md`, `sk-product-owner/SKILL.md`,")

# ── 2. Hub files at the repository root ───────────────────────────────
(PO / "SKILL.md").write_text("""---
name: product-owner
description: "Hub for the Product Owner packets. Picks the Product Owner packet or the vendored Figma tool packet for a request and hands stage two routing to that packet."
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, mcp__code_mode__call_tool_chain]
version: 1.0.0.0
---

# Product Owner Hub

The repository root is a parent hub over two packets. This file picks the packet. The packet's own router then routes inside it, and its `SKILL.md` holds its contract. Each packet has its own router, so a request reads only the routing of the packet it uses.

---

## 1. WHEN TO USE

| Packet | Use it for | Folder | Router |
|---|---|---|---|
| **product-owner** | Every task, bug, Story, Epic, Doc and clarification request. The default | `sk-product-owner/` | [`sk-product-owner/ROUTER.md`](sk-product-owner/ROUTER.md) |
| **mcp-figma** | A request that names a `figma-ds-cli` operation and nothing else | `mcp-figma/` | [`mcp-figma/SKILL.md`](mcp-figma/SKILL.md), a vendored packet that routes inside its own `SKILL.md` |

### When NOT to Use

- Production code or a live fix. The Product Owner packet reframes the request or declines it

---

## 2. SMART ROUTING

Routing has two stages. Stage one picks the packet here, from `mode-registry.json` and `hub-router.json`. Stage two is the packet's router.

1. A request starts in the Product Owner packet, the registry default
2. A request that names a tool signal and nothing else starts in the `mcp-figma` packet. The signals are `figma-ds-cli`, `mcp-figma` and `figma cli`, as in `figma-ds-cli fj nodes`. A signal matches whole words only. The bare word "figma" is no signal here, because the Product Owner router reads it as UI refinement feedback and routes it to Task Mode
3. A request that carries any `$` command, or asks for a task, subtask, bug, ticket, Story, PRD, Epic, Doc, document, guide or runbook, starts in the Product Owner packet even when it names a tool
4. A signal with a negation word earlier in its clause, such as "do not use figma-ds-cli", starts no tool packet. The negation words are not, no, never, without, don't and skip

`hub-router.json` holds the signals, the artifact words and the negation words these rules name. `benchmark/gates/check_hub.py` checks that the hub files, the registry packets and their routers agree, that `sk-product-owner/SKILL.md` embeds no router again, and replays the hub gold rows against these rules.

---

## 3. HOW IT WORKS

```text
Product Owner/
  AGENTS.md            bootstrap: reads this file first
  SKILL.md             this hub, stage one
  mode-registry.json   the packets, their folders and routers
  hub-router.json      stage one signals and the default packet
  vendor.json          upstream record of the vendored packet
  sk-product-owner/    Product Owner packet: SKILL.md, ROUTER.md
  mcp-figma/           vendored Figma packet: SKILL.md
```

The vendored packet is a byte-identical copy of the shared skill. `vendor.json` records its upstream and `scripts/vendor-sync.py` keeps it in step, so it carries no Product Owner `ROUTER.md` and its routing stays in its own `SKILL.md`.

---

## 4. RULES

### ALWAYS

- **ALWAYS** read this file, then the packet's router, then the packet's `SKILL.md`
- **ALWAYS** keep the Product Owner routing in `sk-product-owner/ROUTER.md` and its contract in `sk-product-owner/SKILL.md`

### NEVER

- **NEVER** put a route table or a routing section back into `sk-product-owner/SKILL.md`
- **NEVER** edit `mcp-figma/` without moving the change through `scripts/vendor-sync.py push`

---

## 5. REFERENCES

- [`sk-product-owner/ROUTER.md`](sk-product-owner/ROUTER.md): stage two routing of the Product Owner packet
- [`mode-registry.json`](mode-registry.json) and [`hub-router.json`](hub-router.json): stage one
- [`sk-product-owner/SKILL.md`](sk-product-owner/SKILL.md) and [`mcp-figma/SKILL.md`](mcp-figma/SKILL.md): the packet contracts
""")

(PO / "mode-registry.json").write_text(json.dumps({
    "version": "1.0.0.0",
    "hub": "product-owner",
    "modes": [
        {"workflowMode": "product-owner", "packet": "sk-product-owner", "packetSkillName": "sk-product-owner",
         "packetKind": "workflow", "router": "sk-product-owner/ROUTER.md", "default": True},
        {"workflowMode": "mcp-figma", "packet": "mcp-figma", "packetSkillName": "mcp-figma",
         "packetKind": "tool", "router": "mcp-figma/SKILL.md", "vendored": True, "default": False},
    ],
}, indent=2) + "\n")

(PO / "hub-router.json").write_text(json.dumps({
    "version": "1.0.0.0",
    "routerPolicy": {
        "defaultMode": "product-owner",
        "handoff": "A request that names a tool signal, no $ command and no Product Owner artifact starts in the mcp-figma packet",
        "artifactWords": ["task", "tasks", "subtask", "subtasks", "bug", "bugs", "ticket", "tickets", "story", "stories",
                          "prd", "prds", "epic", "epics", "doc", "docs", "document", "documentation", "guide", "guides",
                          "runbook", "runbooks"],
        "negations": ["not", "no", "never", "without", "don't", "dont", "skip"],
    },
    "signals": {
        "product-owner": [],
        "mcp-figma": ["figma-ds-cli", "mcp-figma", "figma cli"],
    },
}, indent=2) + "\n")

# ── 2b. Hub gate and its runner entries ───────────────────────────────
GATES = PO / "benchmark" / "gates"
(GATES / "check_hub.py").write_text((Path(__file__).resolve().parent / "check_hub.py").read_text())
sub(GATES / "run_gates.sh", '  "vendor sync tests|python3 scripts/tests/test_vendor_sync.py"\n',
    '  "vendor sync tests|python3 scripts/tests/test_vendor_sync.py"\n'
    '  "hub check|python3 benchmark/gates/check_hub.py"\n'
    '  "hub check self-test|python3 benchmark/gates/check_hub.py --self-test"\n')

# ── 3. AGENTS.md read order ───────────────────────────────────────────
sub(AGENTS, "> These instructions define WHICH documents to load and WHEN. `sk-product-owner/SKILL.md` defines HOW to route.",
    "> These instructions define WHICH documents to load and WHEN. `sk-product-owner/ROUTER.md` defines HOW to route.")
sub(AGENTS, "Read `sk-product-owner/SKILL.md` before processing any request. On load",
    "Read the hub `SKILL.md`, `sk-product-owner/ROUTER.md` and `sk-product-owner/SKILL.md`, in that order, before processing any request. A request naming only a `figma-ds-cli` operation goes to `mcp-figma/` instead. On load")
sub(AGENTS, "read `sk-product-owner/SKILL.md` directly and apply its routing,",
    "read the three files named below directly and apply their routing,")
sub(AGENTS, "AGENTS.md\n  -> sk-product-owner/SKILL.md\n  -> the HVR card",
    "AGENTS.md\n  -> SKILL.md (hub)\n  -> sk-product-owner/ROUTER.md\n  -> sk-product-owner/SKILL.md\n  -> the HVR card")
sub(AGENTS, "`sk-product-owner/SKILL.md` is the routing authority.", "`sk-product-owner/ROUTER.md` is the routing authority.")
agents_text = AGENTS.read_text()
dag = agents_text[agents_text.index("## Full DAG With File Paths"):]
first = dag.index("  +-> sk-product-owner/SKILL.md")
AGENTS.write_text(agents_text.replace(
    dag, dag[:first] + "  +-> SKILL.md (hub)\n  |\n  +-> sk-product-owner/ROUTER.md\n  |\n" + dag[first:], 1))

# ── 4. differential.py reads the moved prose from ROUTER.md ───────────
DIFF = PO / "benchmark" / "router" / "differential.py"
sub(DIFF, 'SKILL_MD = REPO_ROOT / "sk-product-owner" / "SKILL.md"\n',
    'SKILL_MD = REPO_ROOT / "sk-product-owner" / "SKILL.md"\n'
    '# The hub moved the prose routing section out of SKILL.md into ROUTER.md, so the\n'
    '# topic table and the contract pointer are read there, and both files are held\n'
    '# free of a pasted router.\n'
    'ROUTER_MD = REPO_ROOT / "sk-product-owner" / "ROUTER.md"\n')
sub(DIFF, "exact algorithm the skill's prose routing section in `SKILL.md` summarizes,",
    "exact algorithm the skill's prose routing section in `ROUTER.md` summarizes,")
sub(DIFF, "0. Prose parity. `SKILL.md` is what a model actually reads, and it carries a",
    "0. Prose parity. `ROUTER.md` is what a model actually reads, and it carries a")
sub(DIFF, "   tree, while SKILL.md grows no python fence of its own and no Router",
    "   tree, while SKILL.md and ROUTER.md grow no python fence and no Router")
sub(DIFF, '    """Read the semantic topic table out of SKILL.md.', '    """Read the semantic topic table out of ROUTER.md.')
sub(DIFF, "    text = SKILL_MD.read_text(encoding=\"utf-8\")\n    if SKILL_TOPIC_TABLE_HEADING not in text:\n        raise LookupError(f\"SKILL.md has no",
    "    text = ROUTER_MD.read_text(encoding=\"utf-8\")\n    if SKILL_TOPIC_TABLE_HEADING not in text:\n        raise LookupError(f\"ROUTER.md has no")
sub(DIFF, '    """Prove the table in SKILL.md is a true subset of the executable tables.',
    '    """Prove the table in ROUTER.md is a true subset of the executable tables.')
sub(DIFF, 'f"prose parity topic order: SKILL.md {prose_topics}', 'f"prose parity topic order: ROUTER.md {prose_topics}')
sub(DIFF, 'f"prose parity route[{topic}]: SKILL.md {route!r}', 'f"prose parity route[{topic}]: ROUTER.md {route!r}')
sub(DIFF, 'f"prose parity override[{topic}]: SKILL.md {override!r}, "', 'f"prose parity override[{topic}]: ROUTER.md {override!r}, "')
sub(DIFF, 'are printed in SKILL.md "', 'are printed in ROUTER.md "')
sub(DIFF, "    is uploaded, and SKILL.md carries no copy, because the CLI reads the",
    "    is uploaded, and neither SKILL.md nor ROUTER.md carries a copy, because the CLI reads the")
sub(DIFF, '    skill_text = SKILL_MD.read_text(encoding="utf-8")\n\n    if PYTHON_FENCE_RE.search(skill_text):\n        failures.append(\n            "copy parity: SKILL.md carries a python fence, so the router exists in a "\n            "copy no guard executes and no guard compares against the reference that owns it "\n            f"({ROUTER_CONTRACT_MD.name})"\n        )\n    pasted = sorted({\n        f"def {node.name}(" for node in ast.parse(contract_block).body\n        if isinstance(node, ast.FunctionDef) and f"def {node.name}(" in skill_text\n    })\n    if pasted:\n        failures.append(\n            f"copy parity: SKILL.md carries the contract\'s own definitions {pasted}, so the "\n            "router is inlined under a fence tag no list anticipates, or under none at all"\n        )\n',
    '    router_text = ROUTER_MD.read_text(encoding="utf-8")\n\n    for prose_path in (SKILL_MD, ROUTER_MD):\n        prose_text = prose_path.read_text(encoding="utf-8")\n        if PYTHON_FENCE_RE.search(prose_text):\n            failures.append(\n                f"copy parity: {prose_path.name} carries a python fence, so the router exists in a "\n                "copy no guard executes and no guard compares against the reference that owns it "\n                f"({ROUTER_CONTRACT_MD.name})"\n            )\n        pasted = sorted({\n            f"def {node.name}(" for node in ast.parse(contract_block).body\n            if isinstance(node, ast.FunctionDef) and f"def {node.name}(" in prose_text\n        })\n        if pasted:\n            failures.append(\n                f"copy parity: {prose_path.name} carries the contract\'s own definitions {pasted}, so the "\n                "router is inlined under a fence tag no list anticipates, or under none at all"\n            )\n')
sub(DIFF, "    if CONTRACT_HEADING not in skill_text:\n        failures.append(\n            f\"copy parity: SKILL.md has no",
    "    if CONTRACT_HEADING not in router_text:\n        failures.append(\n            f\"copy parity: ROUTER.md has no")
sub(DIFF, "        if relative not in _section(skill_text, CONTRACT_HEADING):\n            failures.append(\n                f\"copy parity: SKILL.md's",
    "        if relative not in _section(router_text, CONTRACT_HEADING):\n            failures.append(\n                f\"copy parity: ROUTER.md's")
sub(DIFF, "SKILL.md triggers checked)", "ROUTER.md triggers checked)")

# ── 5. README ─────────────────────────────────────────────────────────
README = PO / "README.md"
sub(README, "   `SKILL.md` Section 2 resolves one route before any template loads.",
    "   The hub `SKILL.md` picks the packet, and `sk-product-owner/ROUTER.md` resolves one route before any template loads.")
sub(README, "61 SKILL.md triggers checked)", "61 ROUTER.md triggers checked)")
sub(README, "├── README.md                        this guide\n├── SYNC.md",
    "├── README.md                        this guide\n"
    "├── SKILL.md                         hub, picks the packet for a request\n"
    "├── SYNC.md")
sub(README, "├── benchmark/\n", "├── benchmark/\n", 1)
sub(README, "│   └── router/                      route_contract.py, 117 fixtures and the differential\n",
    "│   └── router/                      route_contract.py, 117 fixtures and the differential\n")
sub(README, "├── export/                          generated artifacts, ignored by git\n│   └── benchmark/                   empty until the next playbook run is collected\n",
    "├── export/                          generated artifacts, ignored by git\n│   └── benchmark/                   empty until the next playbook run is collected\n"
    "├── hub-router.json                  hub stage one signals and the default packet\n"
    "├── mcp-figma/                       vendored Figma packet, kept in step by scripts/vendor-sync.py\n"
    "├── mode-registry.json               hub packets, their folders and routers\n"
    "├── scripts/                         vendor-sync.py and its tests\n")
sub(README, "└── sk-product-owner/\n    ├── README.md                    skill guide\n    ├── SKILL.md                     router, rules and delivery protocol\n",
    "├── sk-product-owner/\n│   ├── README.md                    skill guide\n│   ├── ROUTER.md                    stage two router of the Product Owner packet\n│   ├── SKILL.md                     rules and delivery protocol\n")
text = README.read_text()
tree_tail_old = """    ├── graph-metadata.json          skill graph edges and trigger phrases
    ├── leaf-manifest.config.json    which folders hold the routed docs
    ├── leaf-manifest.json           generated list of the routed docs
    ├── leaf-aliases.json            generated identity map of those docs
    ├── assets/                      six templates
    │   └── examples/                21 worked artifacts in task/, bug/, doc/ and story/
    ├── changelog/                   29 release notes, v0.1.0.0 to v1.2.1.0
    ├── manual-testing-playbook/     14 two-turn scenarios in 10 category folders
    └── references/                  11 rule files, loaded always, per route or on demand
```"""
assert tree_tail_old in text
tree_tail_new = "\n".join(("│" + line[1:]) if line.startswith("    ") else line for line in tree_tail_old.split("\n")[:-1])
tree_tail_new += "\n└── vendor.json                      upstream record of the vendored packet\n```"
README.write_text(text.replace(tree_tail_old, tree_tail_new))

# ── 6. Remap line citations of SKILL.md and AGENTS.md ─────────────────
new_skill_lines = SKILL.read_text().split("\n")
new_router_lines = ROUTER.read_text().split("\n")
new_agents_lines = AGENTS.read_text().split("\n")


def line_map(old, new):
    mapping = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mapping[i1 + k + 1] = j1 + k + 1
    return mapping


skill_map = line_map(old_skill, new_skill_lines)
agents_map = line_map(old_agents, new_agents_lines)
router_offset = new_router_lines.index("## 2. SMART ROUTING") + 2  # body line 0 sits here (0-based)


def locate(name, number):
    if name == "AGENTS.md":
        return ("AGENTS.md", agents_map.get(number))
    if number in skill_map:
        return ("SKILL.md", skill_map[number])
    if start + 3 <= number <= end:
        index = number - (start + 3)                     # 0-based into body
        candidate = router_offset + index + 1
        if 0 < candidate <= len(new_router_lines) and new_router_lines[candidate - 1].strip() == old_skill[number - 1].strip().replace("This section is the single", "This file is the single"):
            return ("ROUTER.md", candidate)
    return (name, None)


CITE = re.compile(r"(`?)(SKILL\.md|AGENTS\.md)\1 (lines?) (\d+)((?:(?:, | and | to )\d+)*)")
unresolved = []
changed_files = 0
for doc in sorted((PO / "sk-product-owner" / "manual-testing-playbook").rglob("*.md")):
    text = doc.read_text()

    def repl(match):
        tick, name, word, first_num, rest = match.groups()
        numbers = [int(first_num)] + [int(n) for n in re.findall(r"\d+", rest)]
        separators = re.findall(r", | and | to ", rest)
        located = [locate(name, n) for n in numbers]
        targets = {t for t, _ in located}
        if any(n is None for _, n in located) or len(targets) != 1:
            unresolved.append(f"{doc.relative_to(PO)}: {match.group(0)} -> {located}")
            return match.group(0)
        target = targets.pop()
        out = f"{tick}{target}{tick} {word} {located[0][1]}"
        for sep, (_, n) in zip(separators, located[1:]):
            out += f"{sep}{n}"
        return out

    new_text = CITE.sub(repl, text)
    if new_text != text:
        doc.write_text(new_text)
        changed_files += 1
print(f"remapped citations in {changed_files} playbook files")
for item in unresolved:
    print("UNRESOLVED", item)

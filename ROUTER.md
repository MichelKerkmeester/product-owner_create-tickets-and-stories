---
title: "Product Owner Surface Router: per-intent leaf sets"
description: "Stage two of the product-owner hub. hub-router.json selects the workflow mode, and this document maps a request's intent to the exact packet-local leaves that mode loads, as canonical (workflowMode, leafResourceId) pairs."
trigger_phrases:
  - "product owner surface router"
  - "product owner leaf routing"
  - "product owner resource map"
importance_tier: important
contextType: general
version: 1.0.0.0
router_state: active
skill_pointer: SKILL.md
---

# Product Owner Surface Router: per-intent leaf sets

## 1. OVERVIEW

This is the product-owner hub's second-layer router, at the hub root beside [`SKILL.md`](SKILL.md). The hub selects a mode in [`hub-router.json`](hub-router.json) (`sk-product-owner`, `sk-create-figjam`, `mcp-click-up` or `mcp-figma`), and this document maps the request's intent to the exact packet-local leaves that mode loads. Every path is packet-qualified (`<packet>/references|assets/...`, where `<packet>` is the mode's `mode-registry.json` `packet` field) and converts to the canonical `(workflowMode, leafResourceId)` pair at the one contract boundary, `.skilled/skills/sk-doc/sk-create-skill/scripts/lib/leaf-resource-contract.cjs` in the skills library. A packet's `INSTALL-GUIDE.md` sits at its packet root, outside that contract, so it is never a leaf here: `mcp-click-up/SKILL.md` loads it from its own `ROOT_RESOURCES` on an install route, and the hub map below names only the packet's `references/` leaves.

Routing is two stages: the hub picks the mode, this router picks the leaves within it. The two layers stay separate, so the hub never emits leaf paths and this router never re-decides the mode. Inside a packet, its own router, `SKILL.md` Section 2 and the sibling `ROUTER.md` it links when it has one, still decides the details this map cannot, such as a command conflict, Quick energy or the Doc source gate.

---

## 2. INTENT MODEL

- **TASK leaves**: `task-mode.md` and `task-templates.md`, for `$task`, `$t`, `$task --subtask` and task wording such as "create a task", "write a subtask" or "acceptance criteria for", and for UI refinement feedback, which stays a Task
- **BUG leaves**: `bug-mode.md` and `bug-report-template.md`, for `$bug`, `$b` and bug wording such as "write a bug", "bug report" or "it crashes when"
- **DOC leaves**: `doc-mode.md` and `doc-templates.md`, for `$doc`, `$d` and documentation wording such as "document how", "write a runbook" or "api reference"
- **STORY leaves**: `story-mode.md` and `story-template.md`, for `$story`, `$s`, `$prd`, `$p` and Story wording such as "write a PRD", "user story" or "draft for PM"
- **EPIC leaves**: `story-mode.md` and `epic-template.md`, for `$epic`, `$e` and Epic wording such as "write an epic" or "refine this epic". Story Mode resolves one shape and loads only its scaffold, so STORY and EPIC never load together
- **INTERACTIVE leaves**: `interactive-mode.md` and `interactive-response-templates.md`, for a request that asks for one question first, names two artifact commands or names no artifact at all
- **FLOW leaves**: `flow-mode.md` and `flow-templates.md` from `sk-create-figjam`, for `$flow`, `$figjam`, FigJam output wording such as "make a FigJam flow" or "a sequence diagram in FigJam" and a request to add notes to or update a FigJam board, including one that carries a `figma.com/board` link. The packet's own Section 2 then adds the chosen type's reference and template. `flow-mode.md` Section 4 carries the intake rounds that fill the Brief before a type is chosen
- **CLICK_UP leaves**: the `cupt` command reference, for a `cupt` or ClickUp MCP operation. It is the leaf of the packet's `CUPT_DAILY` intent, the common one, and the packet's own Section 2 adds the MCP tool guide or the troubleshooting leaf when the request is an MCP, install or troubleshooting operation
- **FIGMA leaves**: the `figma-ds-cli` command reference and the tool surface, for a `figma-ds-cli` operation. They are the leaves of the packet's create, token and inspect intents, and the packet's own Section 2 adds the MCP wiring guide, the troubleshooting leaf or the setup assets for the intents that need them

`DEFAULT_RESOURCE` is the two Human Voice cards, `hvr-core.md` and `conciseness.md`, which `AGENTS.md` loads on every request. It is not `routerPolicy.defaultResource` in `hub-router.json`, which is the suggestion offered beside the clarifying question when no intent matches. One dominant intent routes to one leaf set. Two intents that tie name two artifacts, so the request takes the INTERACTIVE set and its one question rather than a union. A FLOW beside another artifact's wording never reaches that tie, so the artifact's set loads alone, because FigJam there is that artifact's subject unless an output verb asks for a board. A board asked for that way is a second output, and it forms an ordered pair in stage two with the artifact first.


### Stage One Rules

Stage one follows `routerPolicy.stageOneOrder` in [`hub-router.json`](hub-router.json), and the first matching rule wins, as the hub `SKILL.md` Section 2 states.

Examples: `cupt list my open tasks` stays in `mcp-click-up` because `tasks` is data, while `figma-ds-cli fj nodes` opens in `mcp-figma`. `figma-ds-cli fj nodes and write a task for the spacing` and `figjam the checkout flow, then write a story` start in `sk-product-owner` because each asks for an artifact. The bare words "figma" and "clickup" remain subjects, and a negated signal such as "do not use figma-ds-cli" starts no packet. A `figma.com/board` link is a FigJam signal, because that address is a FigJam file, while a `figma.com/design` link is not. A full stop ends a clause only before a space, so the dots inside a link stay in the clause that carries it.

A Flow request that stage one keeps in the Product Owner packet follows the single-route handoff contract in [`sk-product-owner/ROUTER.md`](sk-product-owner/ROUTER.md) Section 3. A command conflict such as `$task $flow` follows that packet's Interactive route.

### Outcomes

- `single`: one packet's commands or signals route to that one mode
- `orderedBundle`: never formed here. Signals of two packets start in the default mode, whose Interactive Mode asks which comes first. A FigJam second output beside an artifact is the exception, because it forms an ordered pair in stage two with the artifact first, while two artifacts still ask
- `defer`: a request with no packet command or signal starts in the default mode, and one it cannot route there gets one clarifying question

`benchmark/hub-routing-cases.json` holds the hub gold rows, and `benchmark/gates/check_hub.py` replays them against these rules and checks that the hub files, the registry, the router and the packets agree.

### How To Read This

- One dominant intent routes to one mode's leaf set, beside `DEFAULT_RESOURCE`
- Two artifact intents name two artifacts, which is the conflict the Product Owner packet answers with one question, so the request loads the INTERACTIVE set instead of a union
- No keyword match is the hub's `defer` outcome: the request starts in `sk-product-owner`, whose router scores its semantic topics and asks one clarifying question when no topic clears the threshold
- The keywords above are the trigger set a reader can apply directly, not every synonym. `sk-product-owner/references/router-contract.md` carries the full regexes and scoring, and `sk-product-owner/references/routing.md` the steps and the topic table

### Related Resources

- [`SKILL.md`](SKILL.md) - The hub and its stage one rules
- [`hub-router.json`](hub-router.json) and [`mode-registry.json`](mode-registry.json) - Stage one
- [`sk-product-owner/SKILL.md`](sk-product-owner/SKILL.md) and [`sk-create-figjam/SKILL.md`](sk-create-figjam/SKILL.md) - The workflow packets, which link their own routing in a sibling `ROUTER.md`

---

## 3. MACHINE ROUTER

The single machine-readable projection of the intent model above. The prose is the human-facing contract, and this block is the source sk-create-skill's `leaf-route-replay.cjs` parses when it is run against this hub. `benchmark/gates/check_leaf_map_parity.py` replays the FLOW keywords against the hub gold rows. FLOW gives way to any artifact intent that scores, because FigJam there is that artifact's subject. Keep them in sync: when a map row changes above, update the matching `RESOURCE_MAP` entry here. Every `RESOURCE_MAP` path resolves on disk and is registered in `leaf-manifest.json`, so each dual-reads to a canonical typed pair.

```python
# The two Human Voice cards load on every request, as the bootstrap requires.
DEFAULT_RESOURCE = [
    "sk-product-owner/references/hvr-core.md",
    "sk-product-owner/references/conciseness.md",
]

SHARED_CONTROL_RESOURCES = []

INTENT_SIGNALS = {
    "TASK":        {"weight": 4, "keywords": ["$task", "$t", "$task --subtask", "create a task", "write a task", "add a task", "make a task", "create a ticket", "write a ticket", "write a subtask", "acceptance criteria for", "polish", "spacing", "alignment"]},
    "BUG":         {"weight": 4, "keywords": ["$bug", "$b", "write a bug", "log a bug", "create a bug", "file a bug", "bug report", "defect", "crashes when", "steps to reproduce"]},
    "DOC":         {"weight": 4, "keywords": ["$doc", "$d", "document how", "write a doc", "write a guide", "write a runbook", "api reference", "architecture document", "decision record"]},
    "STORY":       {"weight": 4, "keywords": ["$story", "$s", "$prd", "$p", "write a prd", "user story", "story for", "draft for pm"]},
    "EPIC":        {"weight": 4, "keywords": ["$epic", "$e", "write an epic", "epic for", "refine this epic"]},
    "INTERACTIVE": {"weight": 4, "keywords": ["ask me first", "clarifying questions", "not sure what to write"]},
    "FLOW":        {"weight": 4, "keywords": ["$flow", "$figjam", "figjam flow", "figjam board", "user flow on figjam", "figjam diagram", "figjam chart", "figjam process", "figjam architecture", "figjam sequence", "figjam state", "figjam er diagram", "figjam gantt", "figma.com/board", "in figjam", "on figjam", "on a figjam"]},
    "CLICK_UP":    {"weight": 4, "keywords": ["cupt", "mcp-click-up", "clickup mcp"]},
    "FIGMA":       {"weight": 4, "keywords": ["figma-ds-cli", "mcp-figma", "figma cli"]},
}

RESOURCE_MAP = {
    "TASK": [
        "sk-product-owner/references/task-mode.md",
        "sk-product-owner/assets/task-templates.md"
    ],
    "BUG": [
        "sk-product-owner/references/bug-mode.md",
        "sk-product-owner/assets/bug-report-template.md"
    ],
    "DOC": [
        "sk-product-owner/references/doc-mode.md",
        "sk-product-owner/assets/doc-templates.md"
    ],
    "STORY": [
        "sk-product-owner/references/story-mode.md",
        "sk-product-owner/assets/story-template.md"
    ],
    "EPIC": [
        "sk-product-owner/references/story-mode.md",
        "sk-product-owner/assets/epic-template.md"
    ],
    "INTERACTIVE": [
        "sk-product-owner/references/interactive-mode.md",
        "sk-product-owner/assets/interactive-response-templates.md"
    ],
    "FLOW": [
        "sk-create-figjam/references/flow-mode.md",
        "sk-create-figjam/assets/flow-templates.md"
    ],
    "CLICK_UP": [
        "mcp-click-up/references/cupt-commands.md"
    ],
    "FIGMA": [
        "mcp-figma/references/figma-cli-reference.md",
        "mcp-figma/references/tool-surface.md"
    ],
}
```

### Compiled Routing

The compiled-routing directive the hub `SKILL.md` points at. It resolves the mode before the stage one rules run.

> **Compiled routing (default-on, flag-gated, additive).** Resolve the mode via the compiled router contract first:
> ```bash
> node .skilled/bin/compiled-route.cjs --hub product-owner --prompt "<task>"
> ```
> Follow the returned decision: `route` (use its `targets`), `clarify` or `defer` (disambiguate) or `reject` (refuse). On a `{"servingAuthority":"legacy"}` sentinel or any error, use the routing below. The front door self-gates on serving-authority. Compiled routing is the default for `product-owner`. Set `SPECKIT_COMPILED_ROUTING=0`, the explicit kill-switch, to force legacy routing fleet-wide.

`product-owner` ships without a compiled activation manifest, so the directive above returns the legacy sentinel and the stage one rules below route every request. A Product Owner clone that has no `.skilled/bin/` gets an error from the same command and takes the same path.

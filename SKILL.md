---
name: product-owner
description: "Product Owner hub: routes backlog, doc and FigJam diagram requests and two vendored tool packets via mode-registry.json."
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, mcp__code_mode__call_tool_chain]
version: 1.0.3.0
---

<!-- Keywords: product-owner, sk-product-owner, sk-create-figjam, mcp-click-up, mcp-figma, backlog, task, bug report, user story, epic, prd, product documentation, figjam, user flow, clickup -->

# Product Owner Hub

One public skill identity over three workflow packets and one transport packet. This hub holds no packet-local logic. It routes by `workflowMode` through `mode-registry.json`, uses `hub-router.json` for router policy, signals and outcomes, and hands stage two to the root `ROUTER.md`, which maps the request's intent to the packet's leaves.

**Version authority.** This file's `version` frontmatter is the hub's release version and matches the newest entry under `changelog/`. `description.json`, `mode-registry.json` and `hub-router.json` carry the same value. `ROUTER.md` keeps its own document version, and each packet keeps its own release line.

---

## 1. WHEN TO USE

Use this skill for Barter backlog and documentation work, for diagrams drawn on FigJam boards, and for the ClickUp and Figma operations those artifacts travel through.

| Mode | Kind | Use it for | Packet |
|------|------|------------|--------|
| **sk-product-owner** | workflow | Every task, bug, Story, Epic, Doc and clarification request. The default | [`sk-product-owner/`](sk-product-owner/SKILL.md) |
| **sk-create-figjam** | workflow | A diagram drawn on a FigJam board, from a user flow to a sequence, state, ER or gantt chart: `$flow`, `$figjam` or FigJam output wording with no Product Owner artifact named | [`sk-create-figjam/`](sk-create-figjam/SKILL.md) |
| **mcp-click-up** | workflow | A request that opens with a `cupt` or ClickUp MCP operation, or names one and no Product Owner artifact. Vendored | [`mcp-click-up/`](mcp-click-up/SKILL.md) |
| **mcp-figma** | transport | A request that opens with a `figma-ds-cli` operation, or names one and no Product Owner artifact. Vendored, read-only in this workspace | [`mcp-figma/`](mcp-figma/SKILL.md) |

### When NOT to Use

- Production code or a live fix. The Product Owner packet reframes the request or declines it
- Editing a vendored packet. A change to `mcp-click-up/` or `mcp-figma/` goes upstream through `scripts/vendor-sync.py push`

---

## 2. SMART ROUTING

Routing is registry-driven in two stages. Stage one picks the mode here, from `mode-registry.json` and `hub-router.json`. Stage two is the root [`ROUTER.md`](ROUTER.md), which maps the request's intent to the exact packet-local leaves that mode loads, and the packet's own `SKILL.md` Section 2 routes inside the packet. The hub never emits leaf paths, and `ROUTER.md` never re-decides the mode.

> **Compiled routing (default-on, flag-gated, additive).** Resolve the mode via the compiled router contract first:
> ```bash
> node .skilled/bin/compiled-route.cjs --hub product-owner --prompt "<task>"
> ```
> Follow the returned decision: `route` (use its `targets`), `clarify` or `defer` (disambiguate) or `reject` (refuse). On a `{"servingAuthority":"legacy"}` sentinel or any error, use the routing below. The front door self-gates on serving-authority. Compiled routing is the default for `product-owner`. Set `SPECKIT_COMPILED_ROUTING=0`, the explicit kill-switch, to force legacy routing fleet-wide.

`product-owner` ships without a compiled activation manifest, so the directive above returns the legacy sentinel and the stage one rules below route every request. A Product Owner clone that has no `.skilled/bin/` gets an error from the same command and takes the same path.

### Stage One Rules

Stage one follows the ordered rules in [`hub-router.json`](hub-router.json) `routerPolicy.stageOneOrder`. The first matching rule wins. Packet commands run first, then an artifact request, then an opening packet signal, a default artifact word, one non-negated packet signal, and the default mode.

Examples: `cupt list my open tasks` stays in `mcp-click-up` because `tasks` is data, while `figma-ds-cli fj nodes` opens in `mcp-figma`. `figma-ds-cli fj nodes and write a task for the spacing` and `figjam the checkout flow, then write a story` start in `sk-product-owner` because each asks for an artifact. The bare words "figma" and "clickup" remain subjects, and a negated signal such as "do not use figma-ds-cli" starts no packet. A `figma.com/board` link is a FigJam signal, because that address is a FigJam file, while a `figma.com/design` link is not. A full stop ends a clause only before a space, so the dots inside a link stay in the clause that carries it.

A Flow request that stage one keeps in the Product Owner packet follows the single-route handoff contract in [`sk-product-owner/SKILL.md`](sk-product-owner/SKILL.md) Section 2. A command conflict such as `$task $flow` follows that packet's Interactive route.


### Outcomes

- `single`: one packet's commands or signals route to that one mode
- `orderedBundle`: never formed here. Signals of two packets start in the default mode, whose Interactive Mode asks which comes first. A FigJam second output beside an artifact is the exception, because it forms an ordered pair in stage two with the artifact first, while two artifacts still ask
- `defer`: a request with no packet command or signal starts in the default mode, and one it cannot route there gets one clarifying question

`benchmark/hub-routing-cases.json` holds the hub gold rows, and `benchmark/gates/check_hub.py` replays them against these rules and checks that the hub files, the registry, the router and the packets agree.

---

## 3. HOW IT WORKS

### Layout

```text
Product Owner/            the repository root is the hub
  SKILL.md                 this routing hub
  ROUTER.md                stage two: intent to packet-local leaves
  mode-registry.json       the four modes and the discriminator
  hub-router.json          router policy, signals and vocabulary classes
  description.json         hub advisor descriptor
  graph-metadata.json      the ONE advisor identity for the whole hub
  leaf-manifest.json       generated (workflowMode, leaf) pairs
  changelog/  manual-testing-playbook/  benchmark/
  sk-product-owner/        workflow: tasks, bugs, Stories, Epics, docs
  sk-create-figjam/        workflow: FigJam diagrams
  mcp-click-up/            workflow: vendored ClickUp transport
  mcp-figma/               transport: vendored Figma Desktop bridge
  mcp-code-mode/           the vendored Code Mode server, a repository file and no packet
  AGENTS.md  SYNC.md  vendor.json  opencode.json  LICENSE  Favicon.jpg
  specs/  export/  claude project/  scripts/
                           repository files, declared in the repo-root-hub extension
```

`mcp-code-mode/` carries its own `leaf-manifest.json` because it is the Code Mode server this repository ships beside the packets, not a workflow packet, so the rule against a leaf manifest inside a packet does not reach it. The hub shares the repository root with the bootstrap `AGENTS.md`, the Claude Project package, the spec packets, the exports, the system gates in `benchmark/` and the tooling in `scripts/`. `mode-registry.json` lists those repository entries in its `repo-root-hub` extension, so the skilled checkers skip them and read the hub id from the folder name in kebab case. Each vendored packet is a byte-identical copy of a shared skill: `vendor.json` records its upstream and `scripts/vendor-sync.py` keeps it in step, so its routing stays in its own `SKILL.md`. Only this hub carries a `graph-metadata.json`, so the advisor discovers one `product-owner` identity.

---

## 4. RULES

### ALWAYS

- **ALWAYS** read `AGENTS.md` first when it is not already loaded, as when a runtime opens this skill directly, because it holds the export protocol and the identity handoff
- **ALWAYS** resolve a packet through `mode-registry.json`, then read `ROUTER.md` and the packet's `SKILL.md`
- **ALWAYS** keep each workflow packet's routing in its `SKILL.md` Section 2 and its leaf map in the root `ROUTER.md`
- **ALWAYS** regenerate `leaf-manifest.json` with the sk-create-skill generator after a packet gains or loses a reference or asset

### NEVER

- **NEVER** add a `ROUTER.md`, `graph-metadata.json` or leaf-manifest file inside a packet
- **NEVER** edit `mcp-figma/` or `mcp-click-up/` without moving the change through `scripts/vendor-sync.py push`
- **NEVER** put packet logic in this hub

### ESCALATE IF

- A new kind of Product Owner work needs its own packet. Extend `mode-registry.json`, `hub-router.json` and `ROUTER.md` together and open the packet
- A request names two packets' signals and the Product Owner packet cannot tell which comes first

---

## 5. REFERENCES

- Registry: [`mode-registry.json`](mode-registry.json). Hub router: [`hub-router.json`](hub-router.json). Stage two: [`ROUTER.md`](ROUTER.md)
- Advisor descriptor: [`description.json`](description.json). Skill-graph identity: [`graph-metadata.json`](graph-metadata.json)
- Packets: [`sk-product-owner/SKILL.md`](sk-product-owner/SKILL.md), [`sk-create-figjam/SKILL.md`](sk-create-figjam/SKILL.md), [`mcp-click-up/SKILL.md`](mcp-click-up/SKILL.md) and [`mcp-figma/SKILL.md`](mcp-figma/SKILL.md)
- Hub companions: [`changelog/`](changelog/), [`manual-testing-playbook/`](manual-testing-playbook/manual-testing-playbook.md) and [`benchmark/`](benchmark/README.md)

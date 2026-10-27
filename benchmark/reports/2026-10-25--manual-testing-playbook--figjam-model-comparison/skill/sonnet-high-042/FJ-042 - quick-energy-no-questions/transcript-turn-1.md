# FJ-042 turn 1 transcript

**User:** $flow $quick the Fernhouse damaged-item flow on a new board in our Fernhouse Product plan. Just do it, no questions.

Write the board into the existing FigJam file with key <draft-file-key> rather than a new file. That file is in the plan named above.

**Assistant:**

I'll load the Flow skill logic first.

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/SKILL.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\tname: product-owner\n3\tdescription: \"Product Owner hub: routes backlog, doc and FigJam diagram requests and two vendored tool packets via mode-registry.json.\"\n4\tallowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, mcp__code_mode__call_tool_chain]\n5\tversion: 1.0.8.0\n6\t---\n7\t\n8\t<!-- Keywords: product-owner, sk-product-owner, sk-create-figjam, mcp-click-up, mcp-figma, backlog, task, bug report, user story, epic, prd, product documentation, figjam, user flow, clickup -->\n9\t\n10\t# Product Owner Hub\n11\t\n12\tOne public skill identity over three workflow packets and one transport packet. This hub holds no packet-local logic. It routes by `workflowMode` through `mode-registry.json`, uses `hub-router.json` for router policy, signals and outcomes, and hands stage two to the root `ROUTER.md`, which maps the request's intent to the packet's leaves.\n13\t\n14\t**Version authority.** This file's `version` frontmatter is the hub's release version and matches the newest entry under `changelog/`. `description.json`, `mode-registry.json` and `hub-router.json` carry the same value. `ROUTER.md` keeps its own document version, and each packet keeps its own release line.\n15\t\n16\t---\n17\t\n18\t## 1. WHEN TO USE\n19\t\n20\tUse this skill for Barter backlog and documentation work, for diagrams drawn on FigJam boards, and for the ClickUp and Figma operations those artifacts travel through.\n21\t\n22\t| Mode | Kind | Use it for | Packet |\n23\t|---
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/ROUTER.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"Product Owner Surface Router: per-intent leaf sets\"\n3\tdescription: \"Stage two of the product-owner hub. hub-router.json selects the workflow mode, and this document maps a request's intent to the exact packet-local leaves that mode loads, as canonical (workflowMode, leafResourceId) pairs.\"\n4\ttrigger_phrases:\n5\t  - \"product owner surface router\"\n6\t  - \"product owner leaf routing\"\n7\t  - \"product owner resource map\"\n8\timportance_tier: important\n9\tcontextType: general\n10\tversion: 1.0.0.0\n11\trouter_state: active\n12\tskill_pointer: SKILL.md\n13\t---\n14\t\n15\t# Product Owner Surface Router: per-intent leaf sets\n16\t\n17\t## 1. OVERVIEW\n18\t\n19\tThis is the product-owner hub's second-layer router, at the hub root beside [`SKILL.md`](SKILL.md). The hub selects a mode in [`hub-router.json`](hub-router.json) (`sk-product-owner`, `sk-create-figjam`, `mcp-click-up` or `mcp-figma`), and this document maps the request's intent to the exact packet-local leaves that mode loads. Every path is packet-qualified (`<packet>/references|assets/...`, where `<packet>` is the mode's `mode-registry.json` `packet` field) and converts to the canonical `(workflowMode, leafResourceId)` pair at the one contract boundary, `.skilled/skills/sk-doc/sk-create-skill/scripts/lib/leaf-resource-contract.cjs` in the skills library. A packet's `INSTALL-GUIDE.md` sits at its packet root, outside that contract, so it is never a leaf here: `mcp-click-up/SKILL.md` loads
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/sk-create-figjam/SKILL.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\tname: sk-create-figjam\n3\tdescription: \"Draws FigJam diagrams, from user flows to sequence, state, ER and gantt, as checked Mermaid models composed into framed boards.\"\n4\tallowed-tools: [Read, Write, Edit, Bash, Glob, Grep, mcp__code_mode__call_tool_chain]\n5\tversion: 1.0.8.0\n6\t---\n7\t\n8\t<!-- Keywords: sk-create-figjam, flow mode, figjam, user flow, process, architecture, sequence diagram, state diagram, er diagram, gantt, flowchart, mermaid, board, $flow, $figjam -->\n9\t\n10\t# FigJam Diagrams\n11\t\n12\tThe Product Owner packet that draws FigJam diagrams. It picks the diagram type the reader's question needs, turns screenshots, a Figma flow, a product doc, a schema or a plan into a Mermaid model of that type with a provenance table, checks the model and, after a yes, composes it into a framed FigJam board with a title, zones, colour by kind and a key. Seven types are drawn: user flow, process, architecture, sequence, state, ER and gantt. The hub [`../SKILL.md`](../SKILL.md) picks this packet, the hub [`../ROUTER.md`](../ROUTER.md) maps a Flow request to its leaves, and Section 2 routes inside it.\n13\t\n14\t---\n15\t\n16\t## 1. WHEN TO USE\n17\t\n18\t- `$flow` or `$figjam`, with no other artifact command\n19\t- FigJam output wording such as \"make a FigJam flow from these screenshots\" or \"a sequence diagram in FigJam\"\n20\t- A request to add notes to or update a FigJam board, including one that carries a `figma.com/board` link\n21\t- A Flow route 
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/sk-create-figjam/references/flow-mode.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"Product Owner - Templates - Flow Mode\"\n3\tdescription: \"Product Owner flow-mode workflow: screenshots, Figma flows, product docs, schemas and plans turned into a checked Mermaid model of the right FigJam diagram type, written to a board and delivered as the board URL with a read-back line and the HVR self-scan line.\"\n4\tcontextType: implementation\n5\timportance_tier: important\n6\ttrigger_phrases:\n7\t  - \"flow mode\"\n8\t  - \"$flow figjam board\"\n9\t  - \"figjam diagram type\"\n10\t  - \"figjam flow from screenshots\"\n11\t  - \"flow model pre-write check\"\n12\t  - \"board url read-back\"\n13\tversion: 1.0.7.0\n14\t---\n15\t\n16\t# Product Owner - Templates - Flow Mode\n17\t\n18\tFlow-mode guidance for FigJam diagrams. The workflow picks the diagram type the reader's question needs, turns screenshots, a Figma flow, a product doc, a schema or a plan into a Mermaid model of that type, checks it, writes it to a FigJam board and reads the board back before replying.\n19\t\n20\t**Loading Condition:** ALWAYS on a Flow route, as half of the routed pair with `assets/flow-templates.md`\n21\t**Purpose:** Provides the flow-mode workflow, the type choice, the intake, the rules every type shares, the write routes and the delivery reply when `$flow`, `$figjam` or FigJam output wording is detected\n22\t**Scope:** Type choice, intake per input type, the model, the pre-write check, the quality pass, the write gate, the composed, generated and `fj` write routes,
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/sk-product-owner/references/hvr-core.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"Rules - Human Voice Core\"\n3\tdescription: \"Human Voice hard blockers carried inline, loaded on every request so the banned terms are in view while writing.\"\n4\tcontextType: general\n5\timportance_tier: critical\n6\ttrigger_phrases:\n7\t  - \"human voice card\"\n8\t  - \"hard blockers\"\n9\t  - \"hvr self-scan\"\n10\tversion: 0.100.0.0\n11\t---\n12\t\n13\t# Rules - Human Voice Core\n14\t\n15\tHuman Voice hard blockers carried inline, loaded on every request so the banned terms are in view while writing.\n16\t\n17\t**Loading Condition:** ALWAYS\n18\t**Purpose:** Carries the Human Voice hard blockers inline so the banned terms are in view on every request, without loading the full standard\n19\t**Scope:** Punctuation, hard blocker words and phrases, banned metaphors and cliches, setup language, generalisation fixes, output warnings, structural bans, always-cut modifiers and the before-delivery self-scan report line\n20\t**Output Path:** None. The card governs the wording of an artifact another file writes, and produces none of its own\n21\t**Authority:** `Rules - Human Voice - EN` is the full standard, symlinked into every consuming system as its own human-voice reference. Carried here: punctuation, hard blocker words and phrases, banned metaphors, setup phrases, generalisation fixes, output warnings, structural bans, always-cut modifiers. Left there: soft deductions, context-dependent flags, voice directives, the precedence hierarchy and the point scor
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/sk-product-owner/references/conciseness.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"Rules - Conciseness\"\n3\tdescription: \"The conciseness layer above the Human Voice card: what to cut, what is never cut, and the test that decides which is which.\"\n4\tcontextType: general\n5\timportance_tier: critical\n6\ttrigger_phrases:\n7\t  - \"conciseness layer\"\n8\t  - \"reconstruction test\"\n9\t  - \"concise not robotic\"\n10\t  - \"over-compression\"\n11\tversion: 0.100.0.0\n12\t---\n13\t\n14\t# Rules - Conciseness\n15\t\n16\tThe conciseness layer above the Human Voice card: what to cut, what is never cut, and the test that decides which is which.\n17\t\n18\t**Loading Condition:** ALWAYS, and rules only. A file paid for on every turn stays small enough to be worth paying for\n19\t**Purpose:** Carries the cut rules, the keep rules and the reconstruction test that decides between them, so every delivery is sized as well as checked for banned wording\n20\t**Scope:** Quantity, structure and load-bearing-ness, so an artifact that clears every hard blocker is not still three times too long. Nothing routes to it, since being ALWAYS-loaded is what makes it unroutable\n21\t**Output Path:** None. The layer governs the length of an artifact another file writes, and produces none of its own\n22\t**Loads With:** the consuming system's skill entry and `Rules - Human Voice Core`. That card governs word choice and this file governs quantity, so both run on every delivery\n23\t**Authority:** `Rules - Conciseness - On Demand Rationale` carries the reason behi
```

**Tool call:** `Bash` `{"command": "grep -ril \"fernhouse\" . 2>/dev/null | head -20; ls export 2>/dev/null | head; ls \"claude project/local\" 2>/dev/null", "description": "Search repo for Fernhouse sources"}`

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/sk-create-figjam/assets/flow-templates.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"Product Owner Flow Templates\"\n3\tdescription: \"User-flow Mermaid patterns, the provenance table and the reply shape for Product Owner Flow Mode, each pattern passing the pre-write check.\"\n4\tcontextType: general\n5\timportance_tier: important\n6\ttrigger_phrases:\n7\t  - \"flow templates\"\n8\t  - \"mermaid flow patterns\"\n9\t  - \"flow provenance table\"\n10\t  - \"flow reply shape\"\n11\tversion: 1.0.4.0\n12\t---\n13\t\n14\t# Product Owner Flow Templates\n15\t\n16\tCopy/apply patterns for Product Owner Flow Mode models.\n17\t\n18\t**Loading Condition:** CONDITIONAL, with `references/flow-mode.md` whenever Flow intent is selected\n19\t**Purpose:** Provides the user-flow patterns, the provenance table every diagram type keeps and the reply shape every type delivers\n20\t**Scope:** Five user-flow patterns, the intake questions, the provenance table and the reply shape. The other types keep their patterns in `assets/templates/`\n21\t**Output Path:** None. The model is working data and the board is the deliverable\n22\t\n23\t---\n24\t\n25\t## 1. OVERVIEW\n26\t\n27\t### Purpose\n28\t\n29\tEvery pattern below passes `scripts/flow_check.py` as a user flow, and `scripts/compose_board.py` composes it into a board. Start from the pattern closest to the flow, rename the nodes after the real screens and triggers, add the board lines below and run the check before the write gate. A process, an architecture, a sequence, a state diagram, an ER diagram or a gantt 
```

**Tool result (error):** `Bash`

```text
"Exit code 1\n./sk-create-figjam/references/types/process.md\n./sk-create-figjam/references/types/user-flow.md\n./sk-create-figjam/scripts/compose_board.py\n./sk-create-figjam/assets/screenshots/README.md\n./sk-create-figjam/assets/examples/user-flow-fernhouse-return.md\n./sk-create-figjam/assets/examples/process-fernhouse-refund.md\n./context/fernhouse-context.md\n./leaf-manifest.json"
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/context/fernhouse-context.md"}`

**Tool result:** `Read`

```text
"1\t# Fernhouse company context\n2\t\n3\tOwned by Lotte, Head of Product, and kept in the Product space. Every team reads it before writing a ticket, and the owning team updates it when a surface, service or convention changes. Last updated 2026-09-18, after the 4.8 app releases.\n4\t\n5\tFernhouse sells its own range of cookware, tableware, kitchen textiles, storage and small furniture direct to consumers in five markets: the Netherlands, Belgium, Germany, France and the UK. There are no shops and no resellers. Everything ships from one warehouse in the Netherlands.\n6\t\n7\t## Product and surfaces\n8\t\n9\tCustomers buy on three surfaces, and staff work in a fourth.\n10\t\n11\t| Surface | Used by | What it covers |\n12\t|---------|---------|----------------|\n13\t| `Web` | Customers | The storefront: search, category pages, product pages, cart, checkout, account, order history and wishlist. One responsive build for desktop and mobile browsers |\n14\t| `iOS` | Customers | The Fernhouse app, with the same shopping flows as web plus push notifications for promotions and for a shipped order |\n15\t| `Android` | Customers | The same app scope as iOS, released on the same two-week cycle |\n16\t| `Admin` | Staff | The back office for orders, refunds, returns, customers, the catalog and promotions. Desktop web only |\n17\t\n18\tWeb takes about 61% of revenue and the apps about 39%. The apps carry more repeat business: returning customers place 68% of app orders against 44% on web.\
```

**Tool call:** `Bash` `{"command": "ls -la context sk-create-figjam/assets/screenshots; grep -il \"damage\" -r context sk-create-figjam/assets 2>/dev/null", "description": "List context and screenshot assets"}`

**Tool result:** `Bash`

```text
"context:\ntotal 344\ndrwxr-xr-x@ 27 michelkerkmeester  staff    864 27 Oct 11:48 .\ndrwxr-xr-x@ 29 michelkerkmeester  staff    928 27 Oct 11:48 ..\n-rw-r--r--@  1 michelkerkmeester  staff   4760 25 Sep 20:55 fernhouse-carrier-label-api-notes.md\n-rw-r--r--@  1 michelkerkmeester  staff   4346 25 Sep 20:55 fernhouse-carrier-label-thread.md\n-rw-r--r--@  1 michelkerkmeester  staff   4237 25 Sep 20:55 fernhouse-carrier-tracking-api-facts.md\n-rw-r--r--@  1 michelkerkmeester  staff  13744 25 Sep 20:55 fernhouse-context.md\n-rw-r--r--@  1 michelkerkmeester  staff   3809 25 Sep 20:55 fernhouse-order-tracking-pm-brief.md\n-rw-r--r--@  1 michelkerkmeester  staff   5230 25 Sep 20:55 fernhouse-promotions-rules.md\n-rw-r--r--@  1 michelkerkmeester  staff   3102 25 Sep 20:55 fernhouse-save-card-draft.md\n-rw-r--r--@  1 michelkerkmeester  staff   2756 25 Sep 20:55 fernhouse-wishlist-feedback.md\n-rw-r--r--@  1 michelkerkmeester  staff  12258 25 Sep 20:54 loomlist-context.md\n-rw-r--r--@  1 michelkerkmeester  staff   2879 25 Sep 20:54 loomlist-email-template-inventory.md\n-rw-r--r--@  1 michelkerkmeester  staff   2783 25 Sep 20:52 loomlist-notification-spec.md\n-rw-r--r--@  1 michelkerkmeester  staff   3017 25 Sep 20:54 loomlist-offline-mode-brief.md\n-rw-r--r--@  1 michelkerkmeester  staff   3144 25 Sep 20:54 loomlist-recurring-todos-parent-task.md\n-rw-r--r--@  1 michelkerkmeester  staff   4163 25 Sep 20:54 loomlist-recurring-todos-pm-brief.md\n-rw-r--r--@  1 michelkerkmeester  staff   3
```

**Tool call:** `Bash` `{"command": "grep -in -B2 -A2 \"damag\" context/fernhouse-carrier-tracking-api-facts.md sk-create-figjam/assets/examples/process-fernhouse-refund.md sk-create-figjam/assets/screenshots/README.md | head -60", "description": "Show damage mentions in sources"}`

**Tool result:** `Bash`

```text
"context/fernhouse-carrier-tracking-api-facts.md-27-| `OD` | Out for delivery | Always carries `eta_window`. Can come again after an `EX` |\ncontext/fernhouse-carrier-tracking-api-facts.md-28-| `DL` | Delivered | Carries `delivered_to`: `recipient`, `neighbour` or `parcel_point` |\ncontext/fernhouse-carrier-tracking-api-facts.md:29:| `EX` | Exception | Carries `exception_code`: `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED` |\ncontext/fernhouse-carrier-tracking-api-facts.md-30-\ncontext/fernhouse-carrier-tracking-api-facts.md-31-After an `EX` with `NOT_HOME` the carrier tries again the next working day, which sends a new `OD`. After a second `NOT_HOME` the parcel goes to a parcel point, and a `DL` with `delivered_to` set to `parcel_point` comes when the parcel is dropped there, not when the customer collects it. Confirmed on the call.\n--\nsk-create-figjam/assets/examples/process-fernhouse-refund.md-19-\nsk-create-figjam/assets/examples/process-fernhouse-refund.md-20-```text\nsk-create-figjam/assets/examples/process-fernhouse-refund.md:21:make a FigJam process of how a damaged-item refund moves between the customer, CS and the warehouse, from the support runbook\nsk-create-figjam/assets/examples/process-fernhouse-refund.md-22-```\nsk-create-figjam/assets/examples/process-fernhouse-refund.md-23-\nsk-create-figjam/assets/examples/process-fernhouse-refund.md-24-| Runbook line | Says | Class |\nsk-create-figjam/assets/examples/process-fernhouse-refund.md-25-|---|---|---|\n
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/sk-create-figjam/references/types/process.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"FigJam Type - Process\"\n3\tdescription: \"A business process or decision flow drawn as a FigJam flowchart, with optional actor lanes, stores and data in or out, held to sk-design-diagram's process budget.\"\n4\tcontextType: implementation\n5\timportance_tier: important\n6\ttrigger_phrases:\n7\t  - \"figjam process flow\"\n8\t  - \"decision flowchart figjam\"\n9\t  - \"figjam swimlane\"\n10\t  - \"process lanes\"\n11\t  - \"approval flow figjam\"\n12\tversion: 1.0.4.0\n13\t---\n14\t\n15\t# FigJam Type - Process\n16\t\n17\tA process is work that moves through steps, decisions and often several people or teams: a refund, an approval, a release, an onboarding checklist, a decision tree. It is a flowchart marked `%% type: process`, so the check holds it to process rules rather than user-flow rules.\n18\t\n19\t**Loading Condition:** CONDITIONAL, when the Flow route draws a process or decision flowchart\n20\t**Purpose:** The grammar, rules, budget and read-back for a process\n21\t**Pairs With:** `assets/templates/process.md`\n22\t\n23\t---\n24\t\n25\t## 1. WHEN TO USE\n26\t\n27\t**The reader's question:** who does what, in which order, and where does the work change hands?\n28\t\n29\t- A process across teams or roles, drawn with one lane per actor\n30\t- A decision tree or a pipeline with no actors, drawn without lanes\n31\t- A process that reads from or writes to a store, or takes data in and hands data out\n32\t\n33\tUse a user flow when the subject is one pe
```

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-042/devin-compare-bench/FJ-042/context/fernhouse-carrier-tracking-api-facts.md"}`

**Tool result:** `Read`

```text
"1\t# Parcel carrier tracking API, facts for order tracking\n2\t\n3\tWritten by Yusuf, Backend engineer, Fulfilment, on 2026-09-21. Source: the parcel carrier's tracking events guide (version 2.4) and a call with their integration engineer on 2026-09-19, where they confirmed the points marked as confirmed below. The label events are in Joris's label API notes and follow the same delivery rules.\n4\t\n5\t## The event\n6\t\n7\tThere is one event type, `tracking.updated`, sent for every scan of a parcel. The carrier posts it to `/webhooks/carrier/tracking` on shipping-service. The label events have their own path, and the two stay separate because the carrier signs each subscription with its own secret.\n8\t\n9\t| Field | Meaning |\n10\t|-------|---------|\n11\t| `event_id` | Unique per event, and the same on every retry of that event |\n12\t| `shipment_id` | The shipment created with `POST /v1/shipments` |\n13\t| `tracking_number` | As printed on the label |\n14\t| `status_code` | One of the five codes below |\n15\t| `occurred_at` | When the scan happened, with its UTC offset |\n16\t| `sent_at` | When the carrier sent this delivery |\n17\t| `eta_window` | The expected delivery window as `from` and `to`, each with its offset. Can be missing |\n18\t| `exception_code` | Only on `EX` |\n19\t| `location` | Depot or hub, with city and country |\n20\t\n21\t## Status codes\n22\t\n23\t| Code | Meaning | Notes |\n24\t|------|---------|-------|\n25\t| `PU` | Picked up at our warehouse | O
```

**Assistant:**

Quick energy, so no intake rounds. I read the Fernhouse context and picked a type, and nothing has been written to Figma yet.

"Just do it" can't skip the reading check or the write gate, because the board lands in a shared plan. I asked no intake questions and filled every row from the sources, marking the guesses as assumed.

**No source covers damaged items.** `context/fernhouse-context.md` (updated 2026-09-18) describes the returns path in Key flows 6 and the roles. It has no damaged-item steps. The only damaged-item material is the worked example in `assets/examples/process-fernhouse-refund.md`, which cites a support runbook that isn't in this repo. I haven't used it as a source.

**Type: process with lanes.** The question is who handles a damaged item and where it changes hands. A user flow has no screens to chart, because the context says there is no self-serve return today.

| Row | Value | Status |
|---|---|---|
| Reader | A Fernhouse teammate who needs to see who owns each step | assumed, settled by naming the reader |
| Question | Who handles a damaged item from first contact to refund, and where does it change hands? | assumed |
| Outcome | The reader can see which role owns each step and where the €200 approval enters | assumed |
| Scope | The standard returns path, with damage as the reason it starts | assumed |
| Entry | The customer tells CS the item arrived damaged | assumed, the context says customers contact CS but never mentions damage |
| Exit | Refund issued | captured |
| Actors | Customer, CS agent, Warehouse operator, CS lead | captured |
| Decisions | One: refund over €200, where a CS lead approves | captured |
| Sources and class | `fernhouse-context.md`, current behavior | captured |

**Outline, 4 lanes, 7 nodes, 7 connectors:**
* Customer: Damage reported to CS
* CS agent: Create return, email label
* Customer: Send the item back (assumed, the context implies it without stating it)
* Warehouse operator: Check the item
* CS agent: Refund over €200?
  * Up to €200 goes straight to Refund issued
  * Over €200 goes to CS lead: Approve the refund, then Refund issued

**Look:**
* First glance: Refund issued, the goal. This is assumed, because no source says which handoff is slowest.
* Audience Mixed, detail Balanced, distance Laptop, all by default.
* Title: Damaged item: return and refund.

**Left out, none of it in the sources:**
* Damage evidence such as a photo
* Replacement instead of refund
* Who pays for the return label
* What happens after the 30-day window
* What Fernhouse does with a carrier `DAMAGED` exception

If the runbook behind that example is real Fernhouse practice, send it and I'll redraw from it. It would settle most of those gaps.

Does this reading hold, or should I change a row before the write gate?

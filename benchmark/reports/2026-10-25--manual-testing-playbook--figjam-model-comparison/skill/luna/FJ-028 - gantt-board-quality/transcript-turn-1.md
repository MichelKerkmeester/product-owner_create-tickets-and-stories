# FJ-028 turn 1 transcript

**User:** put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November 2026 with two weeks of conflict-screen design, the sync engine takes three weeks from the same day, the conflict screen build follows its design for two weeks, and desktop and iOS integration starts when both builds are done, one week, and is the critical path. Then a two-week beta for 5 percent of workspaces and the release. Android follows in the next quarter, not yet approved.

Write the board into the existing FigJam file with key <test-file-key> rather than a new file.

**Assistant:**

I’m loading the FigJam flow instructions and checking the connected board tools so I can map the dates and dependencies into the existing file.

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"pwd && rg --files -g 'SKILL.md' -g 'ROUTER.md' -g '*flow-mode.md' -g '*flow-templates.md' -g 'hvr-core.md' -g 'conciseness.md' -g 'interactive-response-templates.md' | sed -n '1,100p'\"", "changes": null}`

**Tool result:** `command_execution`

```text
/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/devin-compare-bench/FJ-028
mcp-click-up/SKILL.md
SKILL.md
ROUTER.md
mcp-code-mode/SKILL.md
sk-create-figjam/SKILL.md
sk-product-owner/SKILL.md
sk-create-figjam/references/flow-mode.md
sk-create-figjam/assets/flow-templates.md
sk-product-owner/references/conciseness.md
sk-product-owner/references/hvr-core.md
sk-product-owner/assets/interactive-response-templates.md
mcp-figma/SKILL.md

```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc 'cat SKILL.md ROUTER.md sk-create-figjam/SKILL.md'", "changes": null}`

**Tool result:** `command_execution`

```text
---
name: product-owner
description: "Product Owner hub: routes backlog, doc and FigJam diagram requests and two vendored tool packets via mode-registry.json."
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, mcp__code_mode__call_tool_chain]
version: 1.0.4.0
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
| **sk-product-owner** | workflow | Every task, bug, Story, Epic, Doc and 
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc 'cat sk-product-owner/references/hvr-core.md sk-product-owner/references/conciseness.md sk-create-figjam/references/flow-mode.md sk-create-figjam/assets/flow-templates.md sk-create-figjam/references/types/gantt.md sk-create-figjam/assets/templates/gantt.md sk-create-figjam/references/quality-rubric.md sk-create-figjam/references/style-guide.md'", "changes": null}`

**Tool result:** `command_execution`

```text
---
title: "Rules - Human Voice Core"
description: "Human Voice hard blockers carried inline, loaded on every request so the banned terms are in view while writing."
contextType: general
importance_tier: critical
trigger_phrases:
  - "human voice card"
  - "hard blockers"
  - "hvr self-scan"
version: 0.100.0.0
---

# Rules - Human Voice Core

Human Voice hard blockers carried inline, loaded on every request so the banned terms are in view while writing.

**Loading Condition:** ALWAYS
**Purpose:** Carries the Human Voice hard blockers inline so the banned terms are in view on every request, without loading the full standard
**Scope:** Punctuation, hard blocker words and phrases, banned metaphors and cliches, setup language, generalisation fixes, output warnings, structural bans, always-cut modifiers and the before-delivery self-scan report line
**Output Path:** None. The card governs the wording of an artifact another file writes, and produces none of its own
**Authority:** `Rules - Human Voice - EN` is the full standard, symlinked into every consuming system as its own human-voice reference. Carried here: punctuation, hard blocker words and phrases, banned metaphors, setup phrases, generalisation fixes, output warnings, structural bans, always-cut modifiers. Left there: soft deductions, context-dependent flags, voice directives, the precedence hierarchy and the point scoring. Load the standard ON_DEMAND to settle a borderline term or run a scored pass.

---

## 1. OVERVIEW

#
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"wc -l sk-product-owner/references/hvr-core.md sk-product-owner/references/conciseness.md sk-create-figjam/references/flow-mode.md sk-create-figjam/assets/flow-templates.md sk-create-figjam/references/types/gantt.md sk-create-figjam/assets/templates/gantt.md sk-create-figjam/references/quality-rubric.md sk-create-figjam/references/style-guide.md && rg -n '\"'^#{1,3} '\"' sk-create-figjam/references/flow-mode.md sk-create-figjam/assets/flow-templates.md sk-create-figjam/references/types/gantt.md sk-create-figjam/assets/templates/gantt.md sk-create-figjam/references/qu`

**Tool result:** `command_execution`

```text
     136 sk-product-owner/references/hvr-core.md
     161 sk-product-owner/references/conciseness.md
     489 sk-create-figjam/references/flow-mode.md
     214 sk-create-figjam/assets/flow-templates.md
     110 sk-create-figjam/references/types/gantt.md
      63 sk-create-figjam/assets/templates/gantt.md
     151 sk-create-figjam/references/quality-rubric.md
     241 sk-create-figjam/references/style-guide.md
    1565 total
sk-create-figjam/references/style-guide.md:16:# FigJam Diagram Style Guide
sk-create-figjam/references/style-guide.md:26:## 1. OVERVIEW
sk-create-figjam/references/style-guide.md:42:## 2. KINDS
sk-create-figjam/references/style-guide.md:46:### Flows and processes
sk-create-figjam/references/style-guide.md:66:### Architecture
sk-create-figjam/references/style-guide.md:70:### State, ER, sequence and gantt
sk-create-figjam/references/style-guide.md:85:### Lines and zones
sk-create-figjam/references/style-guide.md:101:## 3. PALETTE
sk-create-figjam/references/style-guide.md:103:### Accent and lane pairs
sk-create-figjam/references/style-guide.md:124:### What a `style` line means
sk-create-figjam/references/style-guide.md:137:### The accent
sk-create-figjam/references/style-guide.md:156:### Note palettes
sk-create-figjam/references/style-guide.md:170:## 4. GATES
sk-create-figjam/references/style-guide.md:178:### Recorded departures
sk-create-figjam/references/style-guide.md:191:## 5. TYPE AND GRID
sk-create-figjam/references/style-guide.md:213:## 6. WHAT HOLDS 
```

**Assistant:**

The target file key is explicit, so I’m opening a FigJam session and reading the current file before deciding where the new Gantt should sit.

**Tool call:** `figma.create_session` `{"fileKey": "<test-file-key>", "description": "Add Loomlist offline mode launch Gantt to the existing Loomlist Product plan FigJam file"}`

**Tool result:** `figma.create_session`

```text
{'content': [{'type': 'text', 'text': '{"sessionId":"d6ff383e-3f4e-4c30-aa91-7b62a015ae76"}'}], '_meta': {'mcpRequestId': '8f322357-a06d-44c9-9132-b6871bf1c8fe', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgoZXuEHAAARfklEQVR4Ae1de4xU1Rn/zr1zd5ddWFgRorEvAkrUAhURSgx2MI3PVEvMbuTV1jZVu2Aq/GGFBBhsUtBUaNr6jNZWqCbMH2gbEK3pbtWGiiBBomktCbamUSG47rLvmXtPf9+5c5fdZRd2Zu7unoHvJPO6j3O+8/se5zvf+c4dIimCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgYAsCyhZCCqVDEzmUTDqF3k/Jgu/EjY2BSl
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "d6ff383e-3f4e-4c30-aa91-7b62a015ae76", "includeImagesOfNodes": false}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "d6ff383e-3f4e-4c30-aa91-7b62a015ae76", "includeImagesOfNodes": false}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "d6ff383e-3f4e-4c30-aa91-7b62a015ae76", "includeImagesOfNodes": false}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '57,108p' sk-create-figjam/references/flow-mode.md && sed -n '109,200p' sk-create-figjam/references/flow-mode.md && sed -n '247,317p' sk-create-figjam/references/flow-mode.md && sed -n '336,456p' sk-create-figjam/references/flow-mode.md && sed -n '1,110p' sk-create-figjam/references/types/gantt.md && sed -n '1,80p' sk-create-figjam/assets/templates/gantt.md && sed -n '132,214p' sk-create-figjam/assets/flow-templates.md && sed -n '1,151p' sk-create-figjam/references/quality-rubric.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
## 2. WORKFLOW

1. **Route.** `$flow`, `$figjam`, FigJam output wording or a request to add notes to or change a FigJam board selects this mode. Notes on a board already written follow `references/hybrid-workflow.md` on node ids from a `get_figjam` read, and a change to what the board says is a revision that composes the board again, as Section 6 sets out
2. **Pick the type.** Name the reader's question and the type that answers it, as Section 3 sets out, and load that type's reference and template. The outline pass below tests that answer against a second framing before anything is drawn
3. **Intake.** Read every source by its input type, as Section 4 sets out, classify each claim, set the detail level, the audience and the reading distance, and ask the questions the brief leaves open until the draw-ready threshold below is met, then settle the one sentence the board answers. That sentence is the `userIntent` the remove test and the write call both use. The intake writes one record per item, node or edge, before any Mermaid, into the provenance table that `assets/flow-templates.md` Section 3 lays out: the item, its kind, its source, its source class, its confidence and the rung of the inference ladder in Section 4 that reached it. Where a frame name and the heading a reader sees differ, both land in the row and the heading labels the node. No item reaches the model without a row
4. **Model.** Run the outline pass below first, so the shape is agreed as text before a line is d
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc 'cat sk-create-figjam/references/types/gantt.md sk-create-figjam/assets/templates/gantt.md'", "changes": null}`

**Tool result:** `command_execution`

```text
---
title: "FigJam Type - Gantt"
description: "Tasks, phases and milestones on a time axis, drawn as a FigJam gantt chart in one of two date formats, with no styling, anchored dependencies, twelve tasks and five parallel bars per section."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam gantt chart"
  - "roadmap timeline figjam"
  - "launch plan figjam"
  - "milestones on figjam"
version: 1.0.3.0
---

# FigJam Type - Gantt

A gantt chart puts tasks and phases on a time axis, with milestones as points. The composer draws each section as a tinted band, each task as a named row with its bar on a shared axis and each milestone as a diamond, and picks the tick spacing from the chart's length. Neither it nor the generated fallback honours colour, axis, weekend or marker settings, so the check refuses them.

**Loading Condition:** CONDITIONAL, when the Flow route draws a gantt chart
**Purpose:** The grammar, rules, budget and read-back for a gantt chart
**Pairs With:** `assets/templates/gantt.md`

---

## 1. WHEN TO USE

**The reader's question:** which tasks and phases are active when?

- A release plan or a launch plan with dates
- A sprint or a phase plan with dependencies between tasks
- A one-day run of show, in hours

Use a process when there are no dates and the order of steps is the point. Figma's `timeline` kind is not drawn, so a list of dated events with no durations is a gantt chart of milestones.

---

## 2. WHAT THE BOARD DRAWS

```t
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '298,317p' sk-create-figjam/references/flow-mode.md && sed -n '336,489p' sk-create-figjam/references/flow-mode.md && sed -n '1,260p' sk-create-figjam/references/hybrid-workflow.md && sed -n '42,100p' sk-create-figjam/references/style-guide.md && sed -n '101,156p' sk-create-figjam/references/style-guide.md && sed -n '191,241p' sk-create-figjam/references/style-guide.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
## 5. RULES EVERY TYPE SHARES

The check enforces these on every diagram, and each type adds its own in `references/types/`.

- **No emoji, no markup and no literal `\n`.** The board shows every label exactly as the model writes it, so markup would land as literal characters, and the `generate_diagram` fallback rejects emoji and a literal `\n`. Markup means an HTML tag, emphasis stars or underscores and backticks, anywhere in the block but a `%%` comment
- **Labels of at most 40 characters on one line.** Detail moves onto an edge label or into a second node
- **camelCase ids.** Letters and digits only, starting with a letter. No underscore, which breaks connector routing on the `generate_diagram` fallback, and never `end`, `subgraph`, `graph` or another Mermaid keyword. The composer names every layer after its id, such as `node:refund` and `edge:refund->done`, so the read-back finds each one by name
- **A budget per type.** sk-design-diagram's general budget of 9 nodes and 12 connectors applies unless the type sets its own. Over budget, split rather than shrink, and offer the overview board and the detail board together rather than choosing one quietly
- **Allocate before the first block.** The ordered source list is divided into diagram-sized groups before any Mermaid is written, each group ending on a hand-off node and named after that hand-off, so the ledger checks an allocation rather than a model that already overran. A group still over budget takes the fixed cut order t
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"rg -n '\"'^#{1,3} '\"' sk-create-figjam/references/hybrid-workflow.md && sed -n '1,180p' sk-create-figjam/references/hybrid-workflow.md && sed -n '395,438p' sk-create-figjam/references/flow-mode.md && sed -n '420,456p' sk-create-figjam/references/flow-mode.md && sed -n '457,489p' sk-create-figjam/references/flow-mode.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
15:# FigJam Hybrid Workflow
25:## 1. WHEN TO EXTEND
45:## 2. THE PATTERN
58:## 3. RECIPES
60:### Numbered pins with a sticky legend
118:### A single sticky
124:## 4. WHAT AN EXTENSION NEVER DOES
136:## 5. GATE AND ROLLBACK
144:## 6. READ-BACK
157:## 7. WHEN AN EXTENSION FAILS
163:## 8. A BOARD OF SEVERAL DIAGRAMS
---
title: "FigJam Hybrid Workflow"
description: "How to add notes the model cannot carry to a composed FigJam board: numbered pins with a sticky legend or a single sticky, each additive, gated and reversible, plus how a board of several diagrams is planned."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam hybrid workflow"
  - "annotate figjam diagram"
  - "sticky legend"
  - "numbered pins"
  - "use_figma extension"
version: 1.0.1.0
---

# FigJam Hybrid Workflow

A model cannot put a note on a step. The composer draws everything else a model carries: the title, the zones, the colour of every kind, the sequence's step numbers and the key. So the hybrid workflow adds one thing, notes, with `use_figma` inside the board the write returned. Every note is a new node on top of the board. A composed node is never moved, resized or restyled.

**Loading Condition:** ON_DEMAND, when the request asks for notes, callouts or data on specific nodes that the model cannot carry
**Purpose:** When to add notes to a composed board, the two recipes, their gate and their rollback, and how a board of several diagrams is planned
**Scope:** Additions thro
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"rg --files /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/devin-compare-bench/FJ-028 | rg '(\"'^|/)(figma-use|figma-use-figjam)(/|$)|figma-use.*SKILL'\"' | sed -n '1,40p'\"", "changes": null}`

**Tool result:** `command_execution`

```text
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/SKILL.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-slides/SKILL.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-motion/SKILL.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-label.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-connector.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-section.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/figjam-colors.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/edit-text.md
/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-
```

**Assistant:**

The FigJam flow guide requires the Figma authoring skills before the write call. I found them in the connected Figma plugin and am reading their board and note guidance now.

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc 'cat /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use/SKILL.md /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/SKILL.md && cat /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-sticky.md /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/`

**Tool result:** `command_execution`

```text
---
name: figma-use
description: "**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically."
disable-model-invocation: false
---

# use_figma — Figma Plugin API Skill

Use the `use_figma` tool to execute JavaScript in Figma files via the Plugin API. All detailed reference docs live in `references/`.

**Always include `figma-use` in the comma-separated `skillNames` parameter when calling `use_figma`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use`).** This is a logging parameter used to track skill usage — it does not affect execution.

**If Figma MCP tools appear as deferred tools, batch-load all their schemas in a single `ToolSearch` call** using the `select:` syntax — e.g. `ToolSearch query="select:use_figma,get_screenshot,get_metadata,create_new_file"`. One round trip beats six.

**If the task involves building or updating a full page, screen, or multi-section layout in Figma from code**, also load [figma-generate-design](../fi
```

**Assistant:**

## Playback

- **Reader:** Readers of the Loomlist Product plan
- **Question:** When can offline mode reach release, and which dependency chain sets that date?
- **Outcome:** Show the overlaps, critical path, 5% workspace beta and Android follow-up
- **Scope:** The schedule runs from 2 November 2026 through release. Android will appear as an unapproved note, without a dated task bar. Owners were not supplied, so I’d leave out owner lanes
- **Source status:** The core schedule’s approval status wasn’t stated. I’d present its dates as the supplied plan without marking it approved

**Date reading:** I’d treat each week as a calendar week and show dates as start and finish boundaries. That gives conflict-screen design from 2–16 November, sync engine build from 2–23 November, conflict-screen build from 16–30 November, desktop and iOS integration from 30 November–7 December, beta from 7–21 December, and release on 21 December.

**Critical path:** I’d highlight the full seven-week chain: conflict-screen design → conflict-screen build → desktop and iOS integration → beta → release. The sync-engine route takes six weeks. Integration stays the focal task because your plan identifies it as critical.

**Android:** I’d add a note reading “Android follows next quarter; not yet approved. Start date and duration are not set.”

The existing FigJam page already has sections titled “Offline mode launch.” I’d add a distinct section titled **Loomlist offline mode launch schedule** and leave existing content intact.

**Framing:** I recommend a Gantt with “Design and build” and “Launch” sections, dependency arrows and the critical chain highlighted. A simple phase sequence would be shorter, but would hide the parallel work and schedule dates.

**Visual reading:** Integration is the first glance; its dependency chain and the 21 December release follow; the Android note and missing owner details stay secondary.

Does this reading fit, especially treating the durations as calendar weeks and highlighting the full seven-week chain as critical?

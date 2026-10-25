# Product Owner - Create Tickets & Stories

[![GitHub Stars](https://img.shields.io/github/stars/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&logo=github&color=fce566&labelColor=222222)](https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories/stargazers)
[![License](https://img.shields.io/github/license/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&color=7bd88f&labelColor=222222)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&color=5ad4e6&labelColor=222222)](https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories/commits/main)

> Like it? https://buymeacoffee.com/michelkerkmeester

&nbsp;

## 1. 📝 SUMMARY

A product owner in a folder: turns rough product requests into clear developer tasks, bug reports, stories, and docs, with adjustable templates and examples to fit your team.

It asks one question when a fact is missing and never invents one to fill the gap. Every artifact lands on disk before the reply mentions it.

Built for agent CLIs that read `AGENTS.md` and for claude.ai Projects through `claude project/`

**What's inside**

- **Smart Router** - exact `$` commands, artifact framing and nine scored topics resolve each request to Task, Bug, Doc, Story, Flow or Interactive
- **One-Question Intake** - every missing fact goes into one consolidated question, saved as a `-clarification` file before anything is drafted
- **Source-Safe Docs** - five claim classes, a four-step authority order and a gate that blocks any claim no source covers
- **Artifact Templates** - four task shapes, a fixed bug report, five Doc shapes and the Barter house Story and Epic, with 21 worked examples and 7 FigJam examples
- **Blocking Quality Floors** - six dimensions scored out of 10, with a floor of 8 for five of them and 9 for Accuracy
- **Verified Delivery** - numbered export files, a read-back receipt and a ClickUp push only after an explicit yes, to the target you set locally or a private doc
- **FigJam Diagrams** - seven diagram types drawn after an intake that recommends an answer to every question, checked before the write and read back from the board
- **Checks Without a Model** - 141 router fixtures, 234 differential inputs and 59 format cases run from a fresh clone

&nbsp;

## 2. 🗺️ OVERVIEW

### THE FOUNDATION

Three building blocks carry a request through Product Owner:

1. **Routing**

   The hub `SKILL.md` picks the packet, the hub `ROUTER.md` maps the request to the leaves it loads, and the packet's `SKILL.md` Section 2 resolves one route before any template loads. A FigJam diagram goes to `sk-create-figjam/` instead. A command wins first, then artifact framing, then a topic score.

2. **Shaping**

   The route loads one mode reference and its template, never a second pair, plus at most one worked example.

3. **Gates and delivery**

   Source safety, six quality floors, the Human Voice card and the conciseness layer run before export. The file is saved and read back before the reply names its path.

From request to delivered artifact:

```text
                          YOUR REQUEST
                               │
                               ▼
        ┌────────────────────────────────────────────┐
        │                SMART ROUTER                │
        │                                            │
        │  1. Exact command    $task $bug $doc $epic │
        │  2. Artifact framing "a task to document"  │
        │  3. Nine topics      0.25 per hit          │
        │  4. Under 0.60       Interactive Mode      │
        └──────────────────────┬─────────────────────┘
                               │
                               ▼
        ┌────────────────────────────────────────────┐
        │  ALWAYS LOADED          ONE ROUTED PAIR    │
        │  hvr-core.md            mode reference     │
        │  conciseness.md         plus its template  │
        └──────────────────────┬─────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
        CONTEXT IS THERE              CONTEXT IS MISSING
                │                             │
                │                  one consolidated question,
                │                  saved as -clarification.md,
                │                  then wait for the answer
                ▼
        ┌────────────────────────────────────────────┐
        │  Discover → Engineer → Prototype           │
        │           → Test → Harmonize               │
        │                                            │
        │  Doc gate     PENDING, BLOCKED or READY    │
        │  Six floors   8 each, Accuracy 9           │
        │  Voice card and conciseness pass           │
        └──────────────────────┬─────────────────────┘
                               │
                               ▼
               export/[###] - task-[description].md
                      saved, then read back
                               │
                               ▼
             ClickUp push only after an explicit yes
```

### Smart Router

One request, one route.

Exact commands set the route before any wording is scored.

- `$task`, `$bug`, `$doc`, `$story` and `$epic` match only as standalone tokens, so `$document` or `$debug` never trigger a route
- Framing beats topic words: "create a task to document X" is a Task, "document how X works" is a Doc
- `benchmark/router/route_contract.py --request` prints the route any request gets, with no model involved

### One-Question Intake

Asks once, then waits.

A request that lacks scope, evidence or source authority gets one question that covers all of it.

- An ambiguous request with no command opens that question with a Quick or Deeper choice
- The question is saved as a file such as `export/001 - task-creator-payout-pause-clarification.md`. The answer becomes the next number in the same lane
- One round only. Once you answer, the next reply drafts, and each gap with a safe default is listed under Open items for you to confirm or strike. Only a source conflict with no clear winner, a promised source that has not arrived or a decision you called unsettled earns a second question
- `$quick` may skip routine Task and Bug questions. It never skips a Doc authority or conflict question

### Source-Safe Documentation

Docs that never pass a proposal off as shipped.

Doc Mode classifies every material claim before it drafts a line.

- Five classes: current behavior, approved direction, proposal, retired material and unknown, each with its own status label
- Recency, filenames and duplicate wording never settle a conflict, and an unresolved one stops the draft
- A requested claim about a subject no supplied source covers is blocked as well

### Quality Gates

Floors that block, not scores that advise.

Six dimensions are scored out of 10 before export.

- Five need 8 and Accuracy needs 9, because an invented fact reads as confidently as a verified one
- One dimension under its floor is a repair. Two or more send the draft back to be rebuilt
- The Human Voice card blocks on its own, whatever the six scores say
- Three revision cycles is the ceiling

### Verified Delivery

Saved, read back, then reported.

- The reply opens with the path and a `Verified:` receipt carrying the saved file's line count
- A failed read-back removes the `Path:` line and the delivery claim
- ClickUp delivery waits for an explicit yes in the current conversation, every time

&nbsp;

## 3. 🚀 QUICK START

### Installation

```bash
git clone https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories.git
cd product-owner_create-tickets-and-stories
```

Open the folder in an agent CLI that reads `AGENTS.md` and point the model at that file. It reads the hub `SKILL.md` and `ROUTER.md`, then `sk-product-owner/SKILL.md`, and works as the Product Owner from then on. Writing tickets, stories and docs needs no package and no API key. The router checks need Bash and Python 3, and the format check needs Node.js. Pushing to ClickUp or reading Figma takes the one-time Code Mode setup below.

### Verify Installation

```bash
bash benchmark/router/run_fixtures.sh
```

```text
PASSED 141/141 fixtures
PASSED 234/234 differential inputs (9 topics, 114 synonyms in parity, 61 routing.md triggers checked)
```

The check calls no model and no network. Section 11 lists the format check and the rest.

### Connect ClickUp and Figma (optional)

In Claude Desktop or claude.ai, the Project uses ClickUp's and Figma's own connectors instead, and [USER-GUIDE.md](./USER-GUIDE.md) walks through adding them, switching them on and checking they work. The steps below are for terminal agents.

The repository carries its own Code Mode setup: `.utcp_config.json` registers the `clickup_official` and `figma` manuals, and `.mcp.json` and `opencode.json` start the vendored server in `mcp-code-mode/` through `scripts/code-mode.cjs`. The server needs Node 24, because its `isolated-vm` sandbox has no build for a later Node, and the launcher finds an installed Node 24 through nvm, fnm, volta or `PATH` even when your default `node` is newer.

```bash
cp .env.example .env                      # figma_FIGMA_API_KEY, optional
nvm install 24                            # or any manager, as long as a Node 24 is installed
cd mcp-code-mode/mcp-server && nvm exec 24 npm ci && nvm exec 24 npm run build && cd ../..
```

Flow Mode draws through Figma's hosted MCP when the agent CLI connects it, and through Figma Desktop when it does not. The desktop route uses `figma-ds-cli` and draws user flows and processes with no lanes, node by node into the FigJam file you have open. It is set up once per machine:

```bash
bash mcp-figma/scripts/install.sh          # figma-ds-cli 1.2.0 or later, from the silships repository
figma-ds-cli --version                     # must print 1.2.0 or later
```

Then, in Figma Desktop, import the bridge plugin once through Plugins, Development, Import plugin from manifest, picking `~/.figma-ds-cli/source/plugin/manifest.json`. That folder is hidden, so on macOS press Cmd+Shift+G in the file picker and paste the path. In each session, open the FigJam file, run Plugins, Development, FigCli and keep it open, then run `figma-ds-cli connect --safe`. Safe mode patches nothing. The plain `figma-ds-cli connect` patches Figma Desktop and breaks when Figma updates, so use it only on purpose and undo it with `figma-ds-cli unpatch`. `mcp-figma/INSTALL-GUIDE.md` covers the daemon and troubleshooting.

Your ClickUp push targets live in `claude project/local/Product Owner - Local - Push Targets.md`, which git ignores: each list and doc by name under its team, filled from `claude project/templates/`. The delivery offer names the one that fits, asks when several could, and without the file asks where. The Claude Project reads the same file once you upload it. Restart the agent CLI so it reads `.mcp.json` or `opencode.json`. The first ClickUp call opens a ClickUp sign-in in the browser, since `mcp-remote` authenticates with OAuth and needs no key. `node_modules/` and `dist/` stay local and gitignored, and a later `scripts/vendor-sync.py pull` keeps them.

### First Use

```text
$task I need a task for the creator payout pause feature.
```

A feature name is not a scope, so the reply saves one question as `export/001 - task-creator-payout-pause-clarification.md` and drafts nothing. Answer it in one message and the task lands in `export/002 - task-creator-payout-pause.md`. This is playbook scenario `STK-001`, and a collected playbook run keeps both files under that prefix.

### Use It in a claude.ai Project

1. Paste `claude project/Custom Instructions.md` into the custom instructions of a Project named **Product Owner**
2. Remove superseded knowledge uploads, then upload all 64 files in `claude project/knowledge/` with their filenames unchanged
3. Run the smoke matrix in [the Project README](claude%20project/README.md) and confirm a Deliverable Block appears first, since a Project cannot write files
4. Optionally fill `claude project/templates/Product Owner - Local - Push Targets.md` with your ClickUp lists and docs by team, keep the copy in the gitignored `claude project/local/` and upload it to your own Project, so the ClickUp offer names the one that fits. [USER-GUIDE.md](./USER-GUIDE.md) Section 4 walks through it

&nbsp;

## 4. 🧭 MODES AND ROUTING

Every request resolves to one route object before a template loads. Quick changes the depth of the work, never the route.

#### Commands

| Command | Shortcut | Route | Routed pair |
|---|---|---|---|
| `$task` | `$t` | Task | `task-mode.md` with `task-templates.md` |
| `$task --subtask` | none | Task, child scope | `task-mode.md` with `task-templates.md` |
| `$bug` | `$b` | Bug | `bug-mode.md` with `bug-report-template.md` |
| `$doc` | `$d` | Doc | `doc-mode.md` with `doc-templates.md` |
| `$story` | `$s`, `$prd`, `$p` | Story, Story shape | `story-mode.md` with `story-template.md` |
| `$epic` | `$e` | Story, Epic shape | `story-mode.md` with `epic-template.md` |
| `$quick` | `$q` | Energy only | nothing extra |

Tokens match whole, after case normalization. `$d,` counts, while `$document`, `$debug`, `$epics` and `$e.md` do not. [AGENTS.md](AGENTS.md) spells out the token rules.

#### Detection Order

1. Pull out `$quick`, `$q` or quick framing as energy. Energy never selects an artifact
2. Check `$task --subtask` before the bare `$task`
3. One exact command wins over any wording. Two that name different routes become one question. `$story` and `$epic` both mean Story Mode, so together they only choose the shape
4. With no command, match artifact framing such as "write a bug report about" or "turn this into a PRD". Framing beats topic words, and two framing matches are a conflict too
5. Route polish, spacing, wording and Figma feedback to Task even beside "fix" or "broken", because Bug Mode is for unexpected system behavior
6. Score the nine topics and route by confidence band
7. Send every Doc route through the source-authority gate before drafting, under Quick energy too

Three shapes count as framing without naming an artifact. Symptom wording such as "freezes" routes to Bug, a role denied a capability routes to Story and initiative-scale wording routes to Story with the Epic shape.

#### Topics and Confidence

Nine topics score a request that carries no command and no framing. `bug` routes to Bug, `documentation` to Doc, `story` to Story and the other six to Task. Each word-boundary hit adds 0.25, capped at 0.95. One hit on `ui_refinement` scores at least 0.80, and one on `documentation` or `prd` at least 0.85. The trigger words live in [router-contract.md](sk-product-owner/references/router-contract.md).

- 0.85 and up routes directly
- 0.60 to 0.84 routes with a one-line confirmation of the mode
- 0.40 to 0.59 names the likely mode and asks through Interactive Mode
- Under 0.40 gets one comprehensive question

Under Quick energy the router trusts a score down to 0.40 and only below that falls back to Task, the narrow safe default. A `$token` is stripped before scoring, so a sentence about `$epics` on the roadmap is not a request to write one.

#### Precedence, By Example

Each line is the output of `route_contract.py --request` on this tree.

- `$doc write a bug report about the outage` routes to Doc, because one command beats every word after it
- `Create a task to document Feed v2` routes to Task, because the artifact it names is a task
- `Document bug behavior for failed payments` routes to Doc, because "Document" frames the artifact and "bug" is only the subject
- `the app freezes when I open the inbox` routes to Bug on symptom wording with no defect noun
- `refine the settings panel spacing` routes to Task at 0.80 through the UI-refinement override
- `$task $doc explain Feed v2` becomes one Interactive question, because two commands name two routes
- `$document the flow` routes to Interactive at 0.0, because `$document` is not a command

#### The Route Object

Run any request through the same code the fixtures test:

```bash
python3 benchmark/router/route_contract.py --request "write an epic for creator verification"
```

```json
{
  "intent": "STORY",
  "energy": "STANDARD",
  "source": "framing",
  "shape": "EPIC",
  "confidence": null,
  "needs_disambiguation": false,
  "resources": [
    "references/hvr-core.md",
    "references/conciseness.md",
    "references/story-mode.md",
    "assets/epic-template.md"
  ],
  "on_demand": [
    "references/human-voice-rules.md"
  ]
}
```

`confidence` is `null` for command, framing and conflict routes and a number for semantic and fallback routes. `shape` is set only on the Story lane, which is why an Epic request loads `epic-template.md` and never `story-template.md`. `resources` is what the route preloads and `on_demand` is what it names without loading.

#### Energy Levels

- Raw skips the phase flow, while safety and delivery rules still apply. Only the words "skip depth" select it, never `$quick`
- Quick comes from `$quick`, `$q` or "quick", "fast" and "just do it" as framing. It runs Discover, Prototype and Harmonize, with 1 to 2 perspectives recommended
- Standard is the default for every mode. It runs Discover, Engineer, Prototype, Test and Harmonize with at least 3 perspectives and a target of 5
- Deep is for complex, high-risk or multi-source work. It extends the full flow and uses all 5 perspectives

The five perspectives are User, Business, Technical, Risk and Delivery. `$quick $doc` and `$doc $quick` mean the same thing. "Quick" as subject matter sets no energy: "create a task for the quick-reply feature" routes at Standard.

&nbsp;

## 5. 💬 CLARIFICATION AND SOURCE SAFETY

Product Owner asks before it guesses, and it asks once. For Doc work a second gate decides which sources may be stated as fact.

#### When It Stops to Ask

- Any explicit artifact command, `$task`, `$bug`, `$doc`, `$story`, `$epic` or one of their aliases, however much the request already says. A command picks the route and does not supply the direction, so only `$quick` may skip this question
- Two artifact commands that name different routes, or no command and a topic score under 0.60
- A Doc request missing purpose, audience, source set, authority, status, shape or scope
- A Story request where the role, the value, the requirements or the choice between Story and Epic cannot be inferred
- Supplied sources that contradict each other with no clear winner

It asks once. After your answer the next reply drafts, and every remaining gap with a safe default goes under Open items in the reply. A second question comes only for a source conflict with no clear winner, a promised source still missing or a decision you called unsettled.

#### The Question Is a File

A clarification is exported like any artifact, in the lane of the route it belongs to, with `-clarification` added to the name. A request with no resolved artifact uses `intake` in place of the artifact word. The file holds the question and nothing else: no draft, no partial artifact and no guessed answer. When the user replies, the artifact takes the next number and the clarification file stays untouched.

Example names, one per lane:

```text
export/001 - task-creator-payout-pause-clarification.md     $task with only a feature name
export/001 - doc-payout-pause-clarification.md              two notes that disagree
export/001 - Story-payout-pause-clarification.md            "Turn these notes into a PRD"
export/001 - intake-creator-payout-flow-clarification.md    no artifact named at all
```

#### The Intake Question

For an ambiguous request with no command, the question has seven numbered blocks, 0 to 6, and block 0 is always the energy choice. This is the opening of the real `SIR-001` clarification file:

```markdown
**0. How should I work this?**
- Quick - lean pass with smart defaults, minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Deliverable type:**
- Task - Development task with QA checklist
- Bug - Defect report with evidence and reproduction steps
- Story - A Story or Epic in the Barter house format, new or refined, with numbered Given/When/Then acceptance criteria
- Doc - Product or engineering guide, behavior reference, runbook, technical reference or proposal
```

Blocks 2 to 6 cover scope, requirements, sources with their authority, extra context and the assumptions worth challenging. With no energy picked, the work runs at Standard. A command-routed request gets a shorter question from its own lane, and [interactive-response-templates.md](sk-product-owner/assets/interactive-response-templates.md) holds the Task, Bug, Story and Doc versions.

#### Five Source Classes

Doc Mode classifies each material claim, down to a section, a table row or a single claim when one file mixes them. Current behavior is stated as current only within the scope its source verifies. Approved direction is stated as intended and kept apart from current behavior. A proposal keeps its proposal framing and its open decisions. Retired material stays visible as history and never overrides active material. An unknown is labelled as unverified or asked about before any definite claim. Each class carries its own label:

```text
Status: Current behavior — verified for {scope}
Status: Approved direction — not confirmed as shipped
Status: Proposal — not current product behavior
Status: Retired material — retained for historical context
Status: Unverified — source authority is not established
```

Labels such as `draft`, `new`, `exists, verify` and `legacy` never get normalized into current behavior. A present-tense sentence is not proof, and neither is a file named "canonical" that contradicts itself.

#### Authority Order

When two sources disagree about the same claim, authority resolves in this order, each signal only within the scope it covers:

1. Explicit user designation
2. Explicit source declaration of lifecycle or approval
3. Repository placement, such as a folder named legacy or proposal
4. Independent corroboration within the same scope

A newer timestamp, a confident filename, majority wording and byte-identical duplicates never decide. With no clear winner the draft stops, and every conflict is listed under one question.

#### The Doc Gate

Every Doc route, Quick included, passes `finalize_artifact_route` in `router-contract.md` before drafting. `PENDING` means the request and sources are not yet evaluated. `BLOCKED` means a missing field, an open conflict, an unapproved restructure or a claim subject no source covers stopped the draft. `READY` means every check cleared and drafting may start.

The subject check catches the case the other checks miss. A request to compare two services can name a purpose, an audience, a source set and a scope while the sources describe only one of them. The gate blocks and asks either for a source on the other service or for that service to leave the scope.

Scenario `SDK-002` shows the conflict path. Note A says a payout pause holds for 24 hours and then releases. Note B says it holds until the brand clears it. Turn 1 stopped and asked which note governs. After the answer, the behavior reference stated Note A as current and kept Note B visible as retired material.

&nbsp;

## 6. 🧱 OUTPUT FORMAT

Each route fills one template. Two grammars exist and never mix:

- Task and Bug put `---` between sections, use `-` bullets and `- []` checklists, and write `## About` at H2 and the other sections at H3, without icons
- Doc, Story and Epic put `* * *` under every content heading, use `*   ` bullets and write headings in sentence case. A Doc writes checklists as `*   []`, and a Story uses `- []` for its requirement items, Mark-as-done and the optional Ready and Done gates. Every checkbox is written `[]`, with no space

Interactive intake questions use plain `-` bullets and bold labels. No newly written bullet in any artifact ends with a full stop.

#### Task Shapes

A task takes one of four shapes: a canonical task, a parent task that coordinates one linked subtask per requirement, a subtask for one bounded area or a Quick task with one unnumbered requirement group. Each has a worked example in [assets/examples/task/](sk-product-owner/assets/examples/task/).

The Requirements opening of the canonical template in `assets/task-templates.md`, down to the first requirement group's checklist:

```markdown
### Requirements

---

### **{Category Name}**

---

1.  **{Item Title}**

---

{1-2 short paragraphs describing the expected outcome and why it matters.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}
```

[task-templates.md](sk-product-owner/assets/task-templates.md) holds the full template, from the title and About through all three requirement groups.

- Requirement groups are numbered only once there are two or more
- Every group ends in a `**Checklist**` of literal `- []` items a QA engineer can verify
- References, Epic, Parent task, Related tasks and Related tickets appear only when they add value or the source task already has them. A parent named without a link stays as backticked text, never an invented URL
- A table in a ticket carries at most 4 columns, and a table of per-size values leads with Size
- Refining an existing task keeps its section names, order and filename

#### Bug Shape

The opening of the template in `assets/bug-report-template.md`, down to its field table:

```markdown
# {Bug Title}

## About

---

{1-2 sentence description of the bug and where it occurs in the application.}

| Field           | Value                                        |
| --------------- | -------------------------------------------- |
| Frequency       | {Always / Sometimes / Rarely / Not provided} |
| Severity        | {Critical/High/Medium/Low}                   |
| Platform        | {iOS/Android/Web}                            |
| Device          | {Device name/model}                          |
| OS Version      | {OS version}                                 |
| Browser         | {Browser name - if web}                      |
| Browser Version | {Browser version - if web}                   |
```

The full template in [bug-report-template.md](sk-product-owner/assets/bug-report-template.md) continues with Observed Behavior, Steps to Reproduce, Expected Behavior and the four-item checklist.

- An unsupplied field reads `Not provided`, never a plausible guess
- Frequency comes from what the source says, not from a count. Three support tickets are three reports, not a frequency
- A root cause appears only as a supplied fact or a labelled hypothesis, and the four checklist items stay exactly as written
- A design review with no shareable link is recorded under `**Design review**` and closed with `(link not provided)`
- `### BDD Scenarios` is added only when a Given, When and Then flow makes the bug clearer

#### Doc Shapes

The shape follows the reader's job, not whether the subject is product or engineering. A Guide is for following an order or applying a standard. A Catalog is for finding and comparing repeated entries. A Behavior reference predicts behavior in a given state. A Proposal puts an option that is not current behavior up for review and names the decision sought before any current state. A Narrative overview orients the reader through prose. Each has a worked example in [assets/examples/doc/](sk-product-owner/assets/examples/doc/).

A Doc may carry source-backed code, APIs, schemas and runbook steps. Analysis nobody approved is labelled as a proposal.

New Docs use ClickUp's grammar. This is the opening of the Guide scaffold in `assets/doc-templates.md`, with one status label filled in:

```markdown
# {Guide Title}

* * *
> **Status: Approved direction — not confirmed as shipped**
* * *

## Overview
* * *
{What this guide enables, who should use it, and why the outcome matters.}

### Before you start
* * *
*   **Required context** — {Input, permission, dependency, or verified starting state}
*   **Known limitation** — {Status condition, constraint, or unresolved dependency}
```

- `* * *` sits on the line directly under every content heading, and `---` never appears
- H1 is the title only. H2 stays a minority, 3 or 4 in a document of about 10 headings, and a bold lead replaces anything deeper than H4
- A section is narrative (full sentences, why before what) or reference (terse bullets, tables, identifiers), and one paragraph never mixes the two
- Empty spacer headings belong only in content pasted into ClickUp, never in the saved file
- A refinement keeps the source's filename, headings, order, links, identifiers, tables and even its typos. It changes only what was asked

#### Story and Epic

Story and Epic are two separate artifacts, not size tiers. Detail grows with scope while the section order stays fixed.

- A Story opens with `# {Persona} - {Area} - {Feature}` then `## Problem` in three to five sentences on the business problem and `## Solution` closing on a bold Expected outcomes label, and References. Its `## Requirements` holds hard constraints only and is left out when there are none. Its acceptance criteria work at screen level
- An Epic opens with `# Epic - {Persona} - {Area}` and an About of `#### Problem`, `#### Goal` and `#### Solution`, with References only when a link is supplied. A `## Scope` of child stories, with an optional Added Later group, takes the place of Requirements. Its acceptance criteria work at release level

The Requirements section of a real Story from the 2026-09-18 run's `SST-001` scenario, its items shown in the current `- []` form:

```markdown
## Requirements
* * *
**Pending payout pause**
* * *
- [] A pause of a pending payout lasts exactly `24 hours`
- [] The reason field is required
- [] The toggle that starts a pause reads `Pause payout`
- [] The payout row of a paused payout shows a `paused` badge
* * *
##   
```

The run did not keep the Story file itself. [The scenario's reply](benchmark/reports/2026-09-18--manual-testing-playbook--glm-5-3-flash-high/skill/SST-001%20-%20story-shape-hard-values/turn-2.md) reports what landed in it, and [story-template.md](sk-product-owner/assets/story-template.md) holds the full template.

- Every hard value the source supplied lands in Requirements verbatim, in backticks and in the source's own units. `32px` never becomes "updated spacing" and `Link Instagram` never becomes "updated copy"
- A supplied value stays out of the acceptance criteria, which describe outcomes and leave the mechanism to the developer
- Requirements hold constraints a build can fail. Each is a `- []` item holding one constraint. An item that only describes what a screen shows is struck, and a `**Checklist**` label or a plain `*   ` bullet never appears there
- Each criterion is a numbered `1 )` block closed by its Mark-as-done checkbox, with no divider before the next one. The `* * *` above the `##   ` spacer closes the section
- `## Delivery` (Estimation, Rabbit holes, No-gos) is added only on request or when an `**Open:**` line or an undated external constraint forces it
- No ticket header fields, story points or INVEST notes appear. The reply names the kind: Story or Epic

Nine optional enrichments exist for a Story that earns them. They include a Connextra promise block, a Rule block for an exact threshold, Definition of Ready and Done gates and a single `← PRIO` marker. `story-example-complete.md` shows seven of them in one Story, and most stories use none.

#### What Never Enters an Artifact

A delivered file carries the deliverable and nothing about how it was made. These travel in the chat reply instead:

- A score, a dimension breakdown, a total or a pass or fail verdict
- The `HVR self-scan:` line or any blocker count
- A bracketed `Assumes:` tag, a perspective roster or a phase trace
- A Mode, Template, Perspectives, Quality Score or Energy header

The one exception renders as nothing: a line-1 HTML comment. The bug report from the 2026-09-18 run opens with `<!-- Bug Mode · Product Owner Bug Report Template v0.100 -->`.

&nbsp;

## 7. 🎯 QUALITY GATES

Six dimensions are scored out of 10 against every artifact before export. A dimension under its floor stops the export and names the work.

| Dimension | Floor | Clears its floor when |
|---|---:|---|
| Completeness | 8 | You cannot name a section a reader would have to ask about |
| Clarity | 8 | No sentence exists that two implementers would build differently |
| Actionability | 8 | No criterion's success condition merely restates the work |
| Accuracy | 9 | The three most specific claims each name the supplied line they rest on |
| Relevance | 8 | No more than one section could be rebuilt from what remains |
| Mechanism depth | 8 | The stated why settles an edge case the artifact never mentions |

Accuracy sits a point higher because an invented fact reads as confidently as a verified one and costs more downstream.

#### Bands and Shapes

Just under the floor is a near miss: 5 to 7 with one named defect standing, or 6 to 8 on Accuracy with an unsupplied claim standing. Lower than that means required content is absent or a claim contradicts a supplied source. A 10 is not a target. It records that a deliberate second pass found nothing.

Each shape has a deciding dimension: Actionability for a Task, Accuracy for a Bug, Accuracy and Relevance for a Doc, Clarity and Mechanism depth for a Story and Completeness, read against the Epic shape, for an Epic. Scoring an Epic down for having no Requirements is a rubric error. [quality-scoring.md](sk-product-owner/references/quality-scoring.md) gives the standard near miss for each shape.

#### Revision Ladder

With no dimension under its floor the status is PASS, and the artifact is harmonized and exported. One dimension under is REVISION NEEDED: fix it at the phase that owns it, then score again. Two or more is REJECTED and goes back to Engineer to rebuild the shape.

Completeness and Relevance return to Discover. Actionability and Accuracy return to Engineer. Clarity and Mechanism depth return to Prototype. Three cycles is the ceiling: after the third, the best version ships with a one-line note in the chat reply naming the dimension still short.

#### Voice and Length Rules

Two rule files load on every request and sit beside the scores rather than inside them:

- `hvr-core.md` is the Human Voice card. It lists 37 hard-blocker words, 22 phrases and 20 metaphors, plus bans on em dashes, semicolons, Oxford commas and curly quotes. A blocker fails the artifact on its own, whatever the six dimensions scored
- `conciseness.md` is the length layer. It carries 13 named cut rules such as question echo, hedge stack and terminal recap. It also carries 9 keep rules such as semantic connectives and the specific number, plus a reconstruction test: a cut is free only when a reader could recover what was removed

Every delivery reply reports the card on one line:

```text
HVR self-scan: N hard blockers. Fixed: <terms>. Kept with reason: <terms>.
```

The six scores and the perspective counts are model judgements, and no script can certify a number a model reports about its own work. The mechanical rules are gated instead: `benchmark/format/validate-output-format.cjs` checks dividers, heading adjacency, the metadata-header ban, the Requirements shape and the H4 depth cap on any saved artifact.

&nbsp;

## 8. 📤 EXPORT AND CLICKUP DELIVERY

The save happens before the reply, and the reply reports only what the save proved.

#### File Naming

```text
export/[###] - task-[description].md
export/[###] - bug-[description].md
export/[###] - doc-[description].md
export/[###] - Story-[description].md
export/[###] - Story-[description]/[###] - Story-[description].md
export/[###] - Story-[description]/[###].[n] - task-[description].md
export/[###] - Epic-[description].md
export/[###] - {task|bug|doc|Story|Epic}-[description]-clarification.md
export/[original-source-filename].md
```

A new artifact takes the next free three-digit number and a short lowercase hyphenated description. A Story asked for with its task breakdown saves as one folder under one number, holding the Story and one `[###].[n]` task file per task, each linked to the others. A clarification with no resolved artifact uses `intake` as its artifact word. A refinement is saved under the exact source filename, such as `export/Barter deal - Image(s).md`, so it can be compared with the original. The supplied source itself is never overwritten.

#### Read-Back Before Reply

1. Save the file
2. Read it back from the exact path. Only non-empty content returned by that read counts, and a planned path, a write result or a remembered draft does not
3. Use the last line number the read returns as `N`
4. If the read fails, retry the save once. If it fails again, print no `Path:` line, claim no delivery and report the export as blocked

A real reply from the 2026-09-18 run, scenario `SIR-001`, turn 2:

```text
`export/002 - task-payout-pause-reason-on-detail-screen.md`

Verified: read-back succeeded; 21 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: "paused" and "payout detail screen" repeated deliberately, since they are the fixed state and surface labels the synonym-cycling rule tells a writer to repeat.

Quality: single requirement group with a QA checklist (Quick task shape, no numbering needed for one group), every checklist item testable, About states the WHY, and the `---` dividers follow the task corpus.
```

The reply never pastes the artifact. It follows one Delivery Reply Shape: the path, the receipt, the self-scan line, one quality line, a two- or three-sentence summary, numbered Open items for every addition and assumption, and one closing line, the ClickUp offer when ClickUp tooling is connected. A Doc quality line names Source safety, Shape fit, ClickUp layout, Readability and Voice, each marked pass or attention.

The same run shows why the receipt is checked rather than trusted. Every skill-side save was read back, yet the printed line count matched the file within one line in only 5 of 13 replies.

#### ClickUp Delivery

The push has to use a parameter that keeps the markdown:

- Create or update a task with `markdown_description`. The ClickUp MCP has no `markdown_content` parameter
- Create, update or read a document page with `content_format: "text/md"`
- Read a task back with `include: ["description"]` on `clickup_get_task`

`mcp-click-up/SKILL.md` owns this contract.

The plain `description` field stores markdown as literal text, so visible `###` or `**` in ClickUp means the wrong parameter was used.

- The export never asks permission. A ClickUp create, update or delete always does, as an explicit yes in the current conversation. An earlier yes does not carry forward
- The artifact's H1 becomes the ClickUp name and leaves the body. HTML comments and process metadata are stripped. Everything else travels verbatim
- After a push the task is read back with markdown enabled to confirm the formatting survived

#### Push Targets

Copy `claude project/templates/Product Owner - Local - Push Targets.md` into `claude project/local/`, which is gitignored, and add each ClickUp list and doc by name under the team that owns it. When one fits the artifact, the reply offers it and a private doc. When several could fit, it asks which, and when none does, it asks where and recommends a private doc. A document lands as a new page in the named doc. The claude.ai Project reads the same file once you upload it to your own Project.

#### What Git Keeps

`.gitignore` ignores everything under `export/` except `.gitkeep` and `export/benchmark/`. Your own artifacts stay on your machine, and the public repository carries only the deliverables from the benchmark run.

&nbsp;

## 9. 📚 TEMPLATES AND EXAMPLES

A route loads its template together with its mode reference. A worked example loads only when a filled instance helps, one file at most and only from the routed mode's folder.

#### Template Assets

[sk-product-owner/assets/](sk-product-owner/assets/) holds six templates. Five cover Task, Bug, Doc, Story and Epic. `interactive-response-templates.md` holds the comprehensive question plus the Task, Bug, Story and Doc questions.

#### Worked Examples

[sk-product-owner/assets/examples/](sk-product-owner/assets/examples/) holds 21 filled artifacts: 5 in `task/`, 4 in `bug/`, 7 in `doc/` and 5 in `story/`, one of them an Epic. Each names in its frontmatter the template section it instantiates. Twenty use invented products, so they teach form without carrying real Barter material. `task-example-ds-variables.md` is the exception: the three tickets of a real Barter design token release, kept as the pattern for the next one.

#### Reference Files

[sk-product-owner/references/](sk-product-owner/references/) holds 12 rule files. `hvr-core.md` and `conciseness.md` load on every request. The five mode files, `task-mode.md`, `bug-mode.md`, `doc-mode.md`, `story-mode.md` and `interactive-mode.md`, load with their route. Flow Mode's `flow-mode.md` and `flow-templates.md` live in [sk-create-figjam/](sk-create-figjam/SKILL.md), its own packet, with one reference per diagram type, a style guide, a quality rubric, the hybrid workflow and the pre-write check `scripts/flow_check.py`. `quality-scoring.md`, `routing.md`, `router-contract.md`, `human-voice-rules.md` and `conciseness-rationale.md` load on demand.

&nbsp;

## 10. 🧩 CLAUDE PROJECT PACKAGE

`claude project/` carries the same system for a claude.ai Project, which has no filesystem and never loads `SKILL.md`.

- `Custom Instructions.md` is the kernel, v1.2.3, aligned to skill v1.2.1.0. It carries the full router and rules and is the routing authority inside the Project
- `knowledge/` holds 64 files: 36 core documents (six mode references, seven templates, four shared rule files, quality scoring, the connector setup reference and the 17 FigJam type, type template, style, quality, hybrid and board composer documents) and the 28 worked examples
- `README.md` holds the upload steps, the source-to-mirror map and the smoke matrix
- `kernel-review.json` is a dated record of one kernel review, read by no tool

#### What Changes in a Project

| Skill in a CLI | claude.ai Project |
|---|---|
| Saves to `export/` and reads the file back | Renders a Deliverable Block as a Canvas Artifact in the side panel |
| Reports `Path:` and the `Verified:` receipt | Reports `Export-equivalent path:`, with `NNN` where the next number is unknown |
| Loads mode files from `references/` and `assets/` | Consults the matching knowledge document |
| Pushes to ClickUp through a connected MCP server | Pushes to ClickUp through the claude.ai connector, when present |

The kernel never claims a save, a read-back or a push the Project did not perform. Setup is the three steps in Quick Start.

#### Hand-Written, Not Generated

Every knowledge file is written by hand from its skill source. It drops loading preambles, routed-by lines and file-path routing. It keeps the decision rules, output shapes and examples. Four files are byte copies instead, the shared rule files, which are regular-file copies of cards maintained in a shared knowledge folder. No Router Contract document ships, because the kernel's Router Code section carries the router code. `SYNC.md` holds the manual parity method and the dated review notes.

The live Project is a separate manual upload, so a matching local package proves nothing about what is deployed.

&nbsp;

## 11. 🧪 BENCHMARKS AND CHECKS

#### Checks That Run From a Clone

| Command | What it checks | Result on this tree |
|---|---|---|
| `bash benchmark/router/run_fixtures.sh` | 141 route fixtures, then the differential against `router-contract.md` | `PASSED 141/141 fixtures` and `PASSED 234/234 differential inputs` |
| `bash benchmark/format/run_fixtures.sh` | 59 cases over 19 fixture files through the output validator | One `PASS` line per case, then `PASSED all format-validator fixtures` |
| `python3 benchmark/gates/example_lint.py` | Every worked example and Project example mirror through the output validator, and every worked reply against the Delivery Reply Shape | `PASSED 56 example files and the worked replies on both packagings` |
| `python3 benchmark/gates/check_hub.py` | The hub files at the root, the registry packets, their routing sections and the stage one gold rows | `PASSED the hub, 4 registry packets and 41 gold rows` |
| `bash benchmark/gates/run_gates.sh` | Router fixtures, format fixtures, rule parity, example lint, vendor sync, Markdown links, hub and Flow checks, the board composer, leaf-map parity, their self-tests and the two sk-create-skill contracts | `all 15 gates pass`, or `11 of 15 gates pass, 4 skipped` from a clone with no shared skill folder |
| `python3 benchmark/router/route_contract.py --self-check` | One sample per detection layer | `self-check passed 5 routing expectations` |
| `node benchmark/format/validate-output-format.cjs "<file>"` | One saved artifact against the output rules | `Product Owner output format validation passed across 1 artifact file(s)` |
| `bash benchmark/grader/check_report.sh <report-folder>` | The voice lint of every captured reply, then twin agreement | Writes `hvr-lint.csv` into the folder it reads |

#### What the Router Differential Proves

`route_contract.py` is the router as a program. `router-contract.md` carries the same router as pseudocode, which is what the skill reads. `differential.py` lifts that pseudocode out of the markdown, runs it and compares the two on five guards:

- Prose-table parity: the routing prose stays within the executable topic table
- Copy parity: the kernel's Router Code section is the same code block with its comments removed, and no Router Contract Knowledge document ships
- Table parity: topics and their order, overrides, thresholds, regexes, resource lanes and the fallback checklist match value for value
- Corpus coverage: every command, alias, false-prefix case and topic is exercised
- Per-input behavior parity: every corpus input matches layer by layer (energy, commands, framing, top topic and score) and then as a whole route object

Prose and code cannot drift apart without one of the five failing.

#### What the Format Validator Catches

- Prose em dashes, with a dash inside a file path left exempt, and the sanctioned definition, status and Catalog entry shapes left exempt
- A divider between a Mark-as-done checkbox and the next criterion
- House grammar breaks: a heading with no divider under it, a `---` rule, a heading deeper than H4, a Checklist or checkbox in Requirements, asterisk emphasis, a second `← PRIO` and too many ellipses or emoji
- Requirements bullets that narrate a screen instead of stating a constraint
- Conciseness breaks: banned openers, heading echo, hedge stacks and terminal recaps
- A Delivery section whose every slot is a placeholder, reported as advice rather than a block

Silent fixtures pin the other side: a compliant house Story, the sanctioned delimiter shapes and near-miss prose must all pass.

#### The Manual Testing Playbook

[The playbook](sk-product-owner/manual-testing-playbook/manual-testing-playbook.md) turns the contract into 68 conversations: 34 for the skill (`S` IDs) and a twin of each for the Project (`P` IDs), set at Roamstay, Loomlist and Fernhouse. The baseline backlog and document scenarios cover 8 tasks, 3 bugs, 5 docs, 5 Stories and 4 Epics. Eight routing scenarios per runtime cover Flow pairing, Story bundles, Bug pairing and grouping, clarification lanes, Quick fallback, energy resolution and ClickUp handoff. The playbook includes one Flow Mode request run with no Figma connector, which ends in a checked model and no board. The routing additions contribute 20 user turns per runtime, including seven independent energy probes, for 136 turns in all.

#### Captured Runs

Two runs of the full playbook sit in `benchmark/reports/`, each with its verdicts, grading notes and captured replies.

- The 2026-09-17 run, Claude Sonnet 5 at medium effort, scored 4 PASS and 3 FAIL on the skill and 2 PASS and 5 FAIL on the Project. Twins disagreed in 2 of 7 pairs, and 3 of 28 replies were lint-clean
- The 2026-09-18 run, GLM 5.3 Flash through Pi at high thinking, scored 6 PASS and 1 PARTIAL on each side. No twins disagreed, and 14 of 28 replies were lint-clean

What the runs found:

- In the Sonnet run, no-command Doc and Story requests skipped the consolidated question on both sides, and both sides opened the ambiguous-intake question with artifact types instead of the energy choice
- In the same run the Project answered `$task` and `$bug` intake as plain chat, without a Deliverable Block. Those are the two twins that disagreed
- 25 of the Sonnet run's 28 replies carried a banned em dash or semicolon. 18 of those 25 held a self-scan line, and every one of them reported 0 hard blockers
- In the GLM run only the Doc guide pair, `SDK-001` and `PDK-001`, fell short
- In the first GLM pass `SST-001` read a sibling scenario's export and copied a requirement nobody supplied. The rerun inside an operating-system sandbox no longer carried it

Three re-measure rounds of the Doc guide pair, three runs per side each, sit in `remeasure/`, `remeasure-2/` and `remeasure-3/` inside the GLM report. The first round measured the v0.9.2 repair: 2 of 3 runs passed on each side, and no run asked for the notes alone any more. Findings from the rounds drove the v0.9.3 and v0.9.4 releases.

#### What `export/benchmark/` Shows

`export/benchmark/` is empty. The deliverables of the earlier runs were removed so the next playbook run starts from a clean folder, and that run's collector fills it again, one file per scenario export or Deliverable Block. Each captured run keeps its replies, verdicts and grading notes in its own folder under `benchmark/reports/`.

#### Maintainer Scripts

`benchmark/parity/` holds five wrappers and `benchmark/gates/` holds `rule_parity.py` beside the example lint, the hub check and the gate runner. The first two compare the Claude Project package against the skill sources by calling a shared sync toolkit that lives one folder above this repository in the maintainer's monorepo and is not published. From a clone they stop on the missing file: `rule_parity.py` and `run_parity.sh` both exit 2. Use the checks above instead.

&nbsp;

## 12. 🗂️ REPOSITORY STRUCTURE

```text
.                                    the repository root is the hub: one skill identity over four packets
├── SKILL.md                         hub, picks the packet for a request
├── ROUTER.md                        stage two, maps each intent to the leaves it loads
├── mode-registry.json               the four modes, the discriminator and the repository paths
├── hub-router.json                  stage one commands, signals and the default packet
├── description.json                 hub advisor descriptor
├── graph-metadata.json              the one skill graph identity
├── leaf-manifest.json               generated list of the routed docs
├── changelog/                       hub release notes
├── manual-testing-playbook/         7 hub routing scenarios
├── mcp-click-up/                    vendored ClickUp packet, kept in step by scripts/vendor-sync.py
├── mcp-code-mode/                   vendored Code Mode server, built locally under Node 24, kept in step by scripts/vendor-sync.py
├── mcp-figma/                       vendored Figma packet, kept in step by scripts/vendor-sync.py
├── sk-create-figjam/                FigJam diagram packet: seven type references, flow_check.py and 68 playbook scenarios
├── sk-product-owner/
│   ├── README.md                    skill guide
│   ├── SKILL.md                     rules, delivery protocol and its router in Section 2
│   ├── assets/                      six templates
│   │   └── examples/                21 worked artifacts in task/, bug/, doc/ and story/
│   ├── changelog/                   29 release notes, v0.1.0.0 to v1.2.1.0
│   ├── manual-testing-playbook/     68 scenarios in 12 category folders
│   └── references/                  12 rule files, loaded always, per route or on demand
├── .env.example                     the Code Mode credential keys, copied to a gitignored .env
├── .mcp.json                        starts Code Mode for Claude Code through scripts/code-mode.cjs
├── .utcp_config.json                the Code Mode manuals: clickup_official and figma
├── .gitignore                       keeps export/, .env and the Code Mode build local, except the benchmark deliverables
├── AGENTS.md                        CLI entry point, export protocol and command registry
├── Favicon.jpg                      repository icon
├── LICENSE                          MIT license
├── README.md                        this guide
├── SYNC.md                          manual parity method and dated review notes
├── USER-GUIDE.md                    connecting ClickUp and Figma to the Project in Claude Desktop
├── benchmark/
│   ├── README.md                    the hub's routing baseline
│   ├── hub-routing-cases.json       the hub's 41 gold rows
│   ├── format/                      output validator, 19 fixtures and their runner
│   ├── gates/                       rule_parity.py, example_lint.py, check_hub.py and run_gates.sh
│   ├── grader/                      hvr_lint.py, reply linter and twin comparison
│   ├── parity/                      five wrappers into the shared parity gate, maintainer only
│   ├── reports/                     dated playbook and benchmark runs
│   └── router/                      route_contract.py, 141 fixtures and the differential
├── claude project/
│   ├── Custom Instructions.md       claude.ai kernel v1.2.3
│   ├── README.md                    upload steps, mirror map and smoke matrix
│   ├── kernel-review.json           dated record of one kernel review
│   └── knowledge/                   64 knowledge files
├── export/                          generated artifacts, ignored by git
│   └── benchmark/                   empty until the next playbook run is collected
├── opencode.json                    starts Code Mode for OpenCode through scripts/code-mode.cjs
├── scripts/                         vendor-sync.py, code-mode.cjs, the vendor sync tests and vendored/code-mode, the Code Mode launcher
├── specs/                           spec packets for changes to this system
└── vendor.json                      upstream record of the vendored packets
```

`mode-registry.json` lists the repository's own entries, from `specs/` to `vendor.json`, in its `repo-root-hub` extension, so the skilled checkers read only the hub and its packets as the skill. `AGENTS.md` points an agent CLI at the skill. A claude.ai Project reads `claude project/Custom Instructions.md` and the files under `claude project/knowledge/` instead.

&nbsp;

## 13. ❓ FAQ

**Q: Does Product Owner implement the task it writes?**

No. It writes backlog and documentation artifacts. A Doc may explain source-backed code or a runbook, but live implementation and live diagnosis are out of scope.

**Q: Why did `$task` ask me a question instead of drafting?**

A command picks the route and does not supply the scope. `$task` with only a feature name still gets its context question. Adding `$quick` is the one way to skip routine intake and accept smart defaults.

**Q: What does `$quick` skip?**

Length and optional sections. It never skips source classification, conflict gates, factuality, refinement fidelity or the export receipt. A Quick doc is shorter, not looser.

**Q: What happens when two sources disagree?**

The draft stops. One question lists the conflicting claims and asks which source governs each. Recency and duplicate wording never decide.

**Q: What if I state one requirement and the model finds four?**

Your count wins. Clauses, states and edge cases inside a stated requirement never become extra requirements. A supplied source that labels a different count goes into the intake question rather than silently overriding yours.

**Q: Why is a question saved as a file?**

A question that exists only in chat is gone when the terminal clears, and it often lists evidence someone has to go and collect.

**Q: Where does the quality score appear?**

In the chat reply only. A score written inside the artifact is itself a defect, unless it sits in a line-1 HTML comment that renders as nothing.

**Q: Does it push to ClickUp on its own?**

No. The local file is saved first, without asking. A ClickUp write waits for an explicit yes in the current conversation, every time.

**Q: Where does a ClickUp push go?**

To the list or doc in your push targets catalog, `claude project/local/Product Owner - Local - Push Targets.md`, whose name and team fit the artifact. The offer names it and also offers a private doc, asks which when several could fit, and asks where with a private doc recommended when none does. The claude.ai Project uses the same file once you upload it.

**Q: Do I need the claude.ai package?**

No. The CLI skill is complete on its own. The Project package exists for people who work in claude.ai.

&nbsp;

## 14. 🔧 TROUBLESHOOTING

**The route does not match the request**

A token is not an exact standalone command, or framing outranked a topic word. Check the route with `python3 benchmark/router/route_contract.py --request "<request>"`, then use one command.

**`$task` or `$bug` replies with a question**

The command routed the request but the scope is missing. Answer in one reply, or resend with `$quick` to accept smart defaults.

**A Doc request stops before drafting**

The Doc gate is `BLOCKED` on a field, a conflict or an uncovered subject. Answer the consolidated question with the source or decision it names.

**No `Path:` or `Verified:` line**

The read-back failed twice. Treat the artifact as undelivered and rerun the request.

**The `Verified:` line count differs from the file**

The model printed a different number than the read returned. Trust the file on disk. The playbook grades the read, not the number.

**ClickUp shows raw `###` or `**`**

The push used the plain `description` field. Push again with `markdown_description`.

**UI feedback routed to Bug**

The wording read as a defect, such as "fix" or "broken" with no polish, spacing or Figma term. Use `$task`, or phrase it as polish or Figma alignment.

**A Story has no Requirements section**

The source supplied no hard value. Supply the sizes, limits or exact strings the build must meet.

**`run_parity.sh` or `rule_parity.py` exits 2**

They need a sync toolkit outside this repository, in the maintainer's monorepo. Use the router and format checks, which run from a clone.

**`check_report.sh` changed a report folder**

It writes `hvr-lint.csv` beside the replies it lints. Run it on a copy of the folder.

&nbsp;

## 15. 📚 RELATED DOCUMENTS

**System guides**

- **[→ Agent Bootstrap](AGENTS.md)** - entry point, export protocol and command registry
- **[→ Hub](SKILL.md)** - picks the packet for a request
- **[→ Hub Router](ROUTER.md)** - maps each intent to the leaves it loads
- **[→ Product Owner Routing](sk-product-owner/references/routing.md)** - routing steps, thresholds, topics and Story shapes
- **[→ Product Owner Skill](sk-product-owner/SKILL.md)** - rules and delivery protocol
- **[→ Skill README](sk-product-owner/README.md)** - mode-by-mode guide to the skill folder
- **[→ Task Mode](sk-product-owner/references/task-mode.md)** - task, parent-task and subtask rules
- **[→ Bug Mode](sk-product-owner/references/bug-mode.md)** - defect evidence and reproduction rules
- **[→ Doc Mode](sk-product-owner/references/doc-mode.md)** - source classes, authority order and refinement fidelity
- **[→ Story Mode](sk-product-owner/references/story-mode.md)** - house grammar, Story and Epic, optional enrichments
- **[→ Interactive Mode](sk-product-owner/references/interactive-mode.md)** - one-question flow and state machine
- **[→ Quality Scoring](sk-product-owner/references/quality-scoring.md)** - bands, per-shape reading and the revision ladder
- **[→ Router Contract](sk-product-owner/references/router-contract.md)** - the router as running Python
- **[→ Worked Examples](sk-product-owner/assets/examples/)** - 21 filled artifacts by mode
- **[→ Manual Testing Playbook](sk-product-owner/manual-testing-playbook/manual-testing-playbook.md)** - the 68 scenarios and their pass criteria
- **[→ Latest Release Notes](sk-product-owner/changelog/v1.2.1.0.md)** - v1.2.1.0, one reply shape and one question round. The [hub release notes](changelog/v1.0.1.0.md) record the plugin removal, and [v1.0.0.0](changelog/v1.0.0.0.md) the parent-hub packaging

**Claude Project package**

- **[→ Project Setup](claude%20project/README.md)** - upload steps, mirror map and smoke matrix
- **[→ Project Kernel](claude%20project/Custom%20Instructions.md)** - the claude.ai custom instructions
- **[→ Parity Notes](SYNC.md)** - manual parity method and dated review notes

**Benchmark guides**

- **[→ Router Checks](benchmark/router/README.md)** - route object, decision rules and the differential
- **[→ Format Checks](benchmark/format/README.md)** - the output validator and its fixtures
- **[→ Reply Grader](benchmark/grader/README.md)** - voice lint and twin comparison
- **[→ Rule Parity Gate](benchmark/gates/README.md)** - maintainer check of rules across the two packages
- **[→ Parity Wrappers](benchmark/parity/README.md)** - maintainer wrappers into the shared parity gate
- **[→ GLM 5.3 Flash Run](benchmark/reports/2026-09-18--manual-testing-playbook--glm-5-3-flash-high/results.md)** - verdicts, speed, voice and re-measure rounds
- **[→ Claude Sonnet 5 Run](benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/README.md)** - verdicts, twin comparison and voice findings

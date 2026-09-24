# Product Owner - Create Tickets & Stories

> Like it? https://buymeacoffee.com/michelkerkmeester

[![GitHub Stars](https://img.shields.io/github/stars/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&logo=github&color=fce566&labelColor=222222)](https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories/stargazers)
[![License](https://img.shields.io/github/license/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&color=7bd88f&labelColor=222222)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&color=5ad4e6&labelColor=222222)](https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories/commits/main)

## 1. SUMMARY

A product owner in a folder: it turns a half-formed product request into a task, bug report, product requirements document or source-safe document.

It asks one question when a fact is missing and never invents one to fill the gap. Every artifact lands on disk before the reply mentions it.

Built for agent CLIs that read `AGENTS.md` and for claude.ai Projects through `claude project/`

**What's inside**

- 🧭 **Smart Router** - exact `$` commands, artifact framing and nine scored topics resolve each request to Task, Bug, Doc, Story or Interactive
- 💬 **One-Question Intake** - every missing fact goes into one consolidated question, saved as a `-clarification` file before anything is drafted
- 🔒 **Source-Safe Docs** - five claim classes, a four-step authority order and a gate that blocks any claim no source covers
- 📋 **Artifact Templates** - four task shapes, a fixed bug report, five Doc shapes and the Barter house Story and Epic, with 21 worked examples
- 🎯 **Blocking Quality Floors** - six dimensions scored out of 10, with a floor of 8 for five of them and 9 for Accuracy
- 📤 **Verified Delivery** - numbered export files, a read-back receipt and a ClickUp push only after an explicit yes
- 🧪 **Checks Without a Model** - 117 router fixtures, 189 differential inputs and 35 format cases run from a fresh clone

**Why it earns a place**

- **Nothing invented:** a bug report with no supplied root cause gets none, and every missing field reads `Not provided`
- **Nothing lost:** a clarification question is saved to `export/` under the next number, so it survives a closed terminal
- **Measured, not claimed:** one 14-scenario playbook runs against both the CLI skill and the claude.ai package, and two captured runs sit in `benchmark/reports/`

&nbsp;

## 2. 🎁 OVERVIEW

### THE FOUNDATION

Three building blocks carry a request through Product Owner:

1. **Routing**

   `SKILL.md` Section 2 resolves one route before any template loads. A command wins first, then artifact framing, then a topic score.

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

**Prerequisites**

- Git to clone the repository
- An agent CLI that reads `AGENTS.md` and runs the model you choose
- Bash and Python 3 for the router checks, Node.js for the format checks
- For claude.ai, a Project that accepts custom instructions and knowledge files

```bash
git clone https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories.git
cd product-owner_create-tickets-and-stories
```

Open the folder in your agent CLI and point the model at `AGENTS.md`. It reads `sk-product-owner/SKILL.md` plus the two always-loaded rule files, `hvr-core.md` and `conciseness.md`. From then on it works as the Product Owner. The repository itself has no package to install and no API key to set.

### Verify Installation

Run the two standalone checks from the repository root:

```bash
bash benchmark/router/run_fixtures.sh
```

Expected output:

```text
PASSED 117/117 fixtures
PASSED 189/189 differential inputs (9 topics, 114 synonyms in parity, 61 SKILL.md triggers checked)
```

```bash
bash benchmark/format/run_fixtures.sh
```

The run prints one `PASS` line per case, 35 in all, then ends with:

```text
PASSED all format-validator fixtures
```

Neither check calls a model or the network.

### First Use

The two-turn flow below is scenario `STK-001` from the manual testing playbook, with the file names the 2026-09-18 benchmark run produced.

Turn 1:

```text
$task I need a task for the creator payout pause feature.
```

The command picks Task Mode, but a feature name is not a scope. The reply saves one question and stops:

```text
export/001 - task-creator-payout-pause-clarification.md
```

That file asks who pauses payouts and at what level, what happens on resume, which value and surfaces are involved and what QA must verify. No task is drafted.

Turn 2:

```text
Standalone task. Creators need a pause indicator for pending payouts, and the pause reason must be stored. Acceptance: the reason field is required, the indicator appears in the payout row, and QA can verify the pause in the payout history.
```

The answer becomes the next file in the lane, with three numbered requirement groups and a checklist under each:

```text
export/002 - task-creator-payout-pause.md
```

Both files are in `export/benchmark/skill/` under the `STK-001` prefix.

Other requests to try:

| Request | Route | What comes back |
|---|---|---|
| `$bug login returns the wrong error message` | Bug | An evidence question, then a report with the field table and `Not provided` where evidence is missing |
| `$doc document how notification delivery works` | Doc | A Doc intake question covering sources, authority, status, shape and scope |
| `$story saved searches for creators` | Story, Story shape | A question on role, value and requirements, then a PRD in the Barter house format |
| `$epic creator verification` | Story, Epic shape | After intake, a Goal, a Scope of child stories and release-level criteria |
| `$quick $doc a short guide for rotating the signing key` | Doc, Quick energy | A short guide with optional sections dropped. With no notes supplied, the source question is still asked |
| `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.` | Interactive | One question that opens with Quick or Deeper |

### Use It in a claude.ai Project

1. Create or open a Project named **Product Owner**
2. Paste `claude project/Custom Instructions.md` into its custom instructions
3. Remove superseded knowledge uploads, then upload all 38 files in `claude project/knowledge/` with their filenames unchanged
4. Run the smoke matrix in [the Project README](claude%20project/README.md) and confirm the Deliverable Block appears first

A Project cannot write files, so each artifact arrives as a rendered Deliverable Block with an `Export-equivalent path:` label. Section 10 covers what else changes.

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

Tokens match whole, after case normalization. `$d,` counts. `$document`, `$docs`, `$debug`, `$d.md`, `$doc/path`, `$stories`, `$prds`, `$sort`, `$epics`, `$email` and `$e.md` do not.

#### Detection Order

1. Pull out `$quick`, `$q` or quick framing as energy. Energy never selects an artifact
2. Check `$task --subtask` before the bare `$task`
3. Collect every exact command. One command wins over any wording. Two that name different routes become one question. `$story` and `$epic` both mean Story Mode, so together they only choose the shape
4. With no command, match artifact framing such as "write a bug report about", "turn this into a PRD" or "write an epic for". Framing beats topic words, and two framing matches are a conflict too
5. Apply the UI-refinement override: polish, spacing, wording and Figma feedback route to Task even beside "fix" or "broken", because Bug Mode is for unexpected system behavior
6. Score the nine topics and route by confidence band
7. Send every Doc route through the source-authority gate before drafting, under Quick energy too

Three request shapes are caught as framing even though they name no artifact. Symptom wording such as "freezes" or "returns a 500" routes to Bug. A role denied a capability routes to Story. Initiative-scale wording routes to Story with the Epic shape.

#### Topics and Confidence

Each word-boundary hit adds 0.25 to its topic, capped at 0.95, and table order breaks a tie. `bug` matches "file a bug" but never "debugging". A `$token` is stripped before scoring, so a sentence about `$epics` on the roadmap is not a request to write one.

| Topic | Route | Sample trigger words | Single-hit override |
|---|---|---|---|
| bug | Bug | `bug`, `fix`, `defect`, `broken`, `crash`, `repro` | none |
| feature | Task | `capability`, `enhancement`, `new`, `add` | none |
| acceptance | Task | `criteria`, `definition of done`, `success condition` | none |
| user_need | Task | `user need`, `persona`, `journey`, `as a user` | none |
| technical_task | Task | `refactor`, `optimize`, `debt`, `update dependency` | none |
| integration | Task | `api`, `connect`, `sync`, `webhook` | none |
| ui_refinement | Task | `polish`, `spacing`, `alignment`, `casing`, `figma` | 0.80 |
| documentation | Doc | `document how`, `runbook`, `api reference`, `decision record` | 0.85 |
| prd | Story | `prd`, `user story`, `epic`, `given when then`, `changing how` | 0.85 |

| Band | Score | What happens at Standard energy |
|---|---|---|
| HIGH | 0.85 and up | Routes directly |
| MEDIUM | 0.60 to 0.84 | Routes with a one-line confirmation of the mode |
| LOW | 0.40 to 0.59 | Names the likely mode and asks through Interactive Mode |
| FALLBACK | under 0.40 | One comprehensive question |

Under Quick energy the router trusts a score down to 0.40 and only below that falls back to Task, the narrow safe default.

#### Precedence, By Example

Every row below is the output of `route_contract.py --request` on this tree.

| Request | Route | Why |
|---|---|---|
| `$doc write a bug report about the outage` | Doc, from the command | One command beats every word after it |
| `Create a task to document Feed v2` | Task, from framing | The artifact named is a task |
| `Document bug behavior for failed payments` | Doc, from framing | "Document" frames the artifact and "bug" is only the subject |
| `Write a bug report about documentation export naming` | Bug, from framing | The same rule the other way round |
| `Create a task to write a PRD about search` | Task, from framing | A task whose subject is another artifact stays a task |
| `write a full story for saved searches` | Story, Story shape | One qualifier inside a phrase is absorbed |
| `the whole creator verification programme` | Story, Epic shape | Initiative-scale framing |
| `the app freezes when I open the inbox` | Bug, from framing | Symptom wording with no defect noun |
| `brands cant filter by engagement rate` | Story, Story shape | A role denied a capability |
| `refine the settings panel spacing` | Task at 0.80 | The UI-refinement override |
| `we are changing how creator ratings work` | Story at 0.85 | A behavior change with no artifact named |
| `$prd $epic onboarding` | Story, Epic shape | Not a conflict: the Epic signal picks the shape |
| `$task $doc explain Feed v2` | Interactive, conflict | Two commands, two routes, one question |
| `$document the flow` | Interactive at 0.0 | `$document` is not a command |
| `this is not a quick task, fix the login copy` | Interactive at 0.25 | Negated "quick" sets no energy, and one hit on "fix" is under 0.40 |
| `$quick` | Task, Quick energy | Quick alone keeps the narrow Task fallback |

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

`confidence` is `null` for command, framing and conflict routes and a number for semantic and fallback routes. `shape` is set only on the Story lane, which is why an Epic request loads `epic-template.md` and never `story-template.md`. `resources` is what the route preloads and `on_demand` is what it names without loading. The schema rejects unknown fields and any file listed in both.

#### Energy Levels

| Energy | Selected by | Phase flow | Perspectives |
|---|---|---|---|
| Raw | the words "skip depth", never `$quick` | Skipped. Safety and delivery rules still apply | none required |
| Quick | `$quick`, `$q` or "quick" and "fast" as framing | Discover, Prototype, Harmonize | 1 to 2 recommended |
| Standard | the default for every mode | Discover, Engineer, Prototype, Test, Harmonize | at least 3, 5 targeted |
| Deep | complex, high-risk or multi-source work | The full flow, extended | all 5 |

The five perspectives are User, Business, Technical, Risk and Delivery. Deep also runs all four cognitive techniques: perspective inversion, assumption audit, constraint reversal and mechanism first. `$quick $doc` and `$doc $quick` mean the same thing. "Quick" as subject matter sets no energy: "create a task for the quick-reply feature" routes at Standard.

&nbsp;

## 5. 💬 CLARIFICATION AND SOURCE SAFETY

Product Owner asks before it guesses, and it asks once. For Doc work a second gate decides which sources may be stated as fact.

#### When It Stops to Ask

- `$task` or `$bug` with little more than a feature name. A command picks the route and does not supply the scope, so only `$quick` may skip this question
- Two artifact commands that name different routes, or no command and a topic score under 0.60
- A Doc request missing purpose, audience, source set, authority, status, shape or scope
- A Story request where the role, the value, the requirements or the choice between Story and Epic cannot be inferred
- Supplied sources that contradict each other with no clear winner

#### The Question Is a File

A clarification is exported like any artifact, in the lane of the route it belongs to, with `-clarification` added to the name. A request with no resolved artifact uses `intake` in place of the artifact word. The file holds the question and nothing else: no draft, no partial artifact and no guessed answer. When the user replies, the artifact takes the next number and the clarification file stays untouched.

Real names from the 2026-09-18 run:

```text
export/001 - task-creator-payout-pause-clarification.md     $task with only a feature name
export/001 - doc-payout-pause-clarification.md              two notes that disagree
export/001 - PRD-payout-pause-clarification.md              "Turn these notes into a PRD"
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
- Story - Product requirements document in the Barter house format, new or refined, with numbered Given/When/Then acceptance criteria
- Doc - Product or engineering guide, behavior reference, runbook, technical reference or proposal
```

Blocks 2 to 6 cover scope, requirements, sources with their authority, extra context and the assumptions worth challenging. With no energy picked, the work runs at Standard.

A command-routed request gets a shorter question from its own lane:

| Route | The one question covers |
|---|---|
| Task | Format and scope, requirements, design and platform, dependencies, what to question |
| Bug | Observed and expected behavior with steps, environment, design reference, evidence, root-cause assumptions to avoid |
| Story | New or refine, role and value, the requirement list (none means an Epic), shared machinery, exact values and links |
| Doc | Operation, purpose and audience, domain and depth, source set, authority per conflict, status, scope and shape, refinement boundaries |

#### Five Source Classes

Doc Mode classifies each material claim, down to a section, a table row or a single claim when one file mixes them.

| Class | How the document may state it | Label it carries |
|---|---|---|
| Current behavior | As current, only within the scope the source verifies | `Status: Current behavior — verified for {scope}` |
| Approved direction | As intended, kept apart from current behavior | `Status: Approved direction — not confirmed as shipped` |
| Proposal | With proposal framing and its open decisions | `Status: Proposal — not current product behavior` |
| Retired material | Visible as history, never overriding active material | `Status: Retired material — retained for historical context` |
| Unknown | Labelled as unverified or asked about before any definite claim | `Status: Unverified — source authority is not established` |

Labels such as `draft`, `new`, `exists, verify` and `legacy` never get normalized into current behavior. A present-tense sentence is not proof, and neither is a file named "canonical" that contradicts itself.

#### Authority Order

When two sources disagree about the same claim, authority resolves in this order, each signal only within the scope it covers:

1. Explicit user designation
2. Explicit source declaration of lifecycle or approval
3. Repository placement, such as a folder named legacy or proposal
4. Independent corroboration within the same scope

A newer timestamp, a confident filename, majority wording and byte-identical duplicates never decide. With no clear winner the draft stops, and every conflict is listed under one question.

#### The Doc Gate

Every Doc route, Quick included, passes `finalize_artifact_route` in `router-contract.md` before drafting:

| State | Meaning |
|---|---|
| `PENDING` | Doc is selected and the request and sources are not yet evaluated |
| `BLOCKED` | Stopped by a missing field, an open conflict, an unapproved restructure or a claim subject no source covers |
| `READY` | Every check clears and drafting may start |

The subject check catches the case the other checks miss. A request to compare two services can name a purpose, an audience, a source set and a scope while the sources describe only one of them. The gate blocks and asks either for a source on the other service or for that service to leave the scope.

Scenario `SDK-002` shows the conflict path. Note A says a payout pause holds for 24 hours and then releases. Note B says it holds until the brand clears it. Turn 1 stopped and asked which note governs. After the answer, the behavior reference stated Note A as current and kept Note B visible as retired material.

&nbsp;

## 6. 🧱 OUTPUT FORMAT

Each route fills one template. Two grammars exist and never mix:

| Artifacts | Dividers | Bullets and checklists | Headings |
|---|---|---|---|
| Task, Bug | `---` between sections | `-` and `- [ ]` | H3 sections without icons |
| Doc, Story, Epic | `* * *` under every content heading | `*   ` bullets, `*   [ ]` in a Doc, `- [ ]` in a Story only for Mark-as-done and the optional Ready and Done gates | Sentence case |

Interactive intake questions use plain `-` bullets and bold labels. No newly written bullet in any artifact ends with a full stop.

#### Task Shapes

| Shape | Use it for | Worked example |
|---|---|---|
| Canonical task | About, optional context blocks and numbered requirement groups | `task-example-ui-refinement.md` |
| Parent task | Coordinating subtasks, one linked child per requirement | `task-example-standard-feature.md` |
| Subtask | One bounded area inside a parent | `task-example-subtask.md` |
| Quick task | A small explicit change with one unnumbered requirement group | `task-example-quick.md` |

The canonical template from `assets/task-templates.md`, trimmed to one context block and the first of its three requirement groups:

```markdown
# {Task Title}

### About

---

{1-3 short paragraphs describing the task, why it matters and what outcome it should create.}

**Epic**

---

- `{Epic name}`

### Requirements

---

### **{Category Name}**

---

1.  **{Item Title}**

---

{1-2 short paragraphs describing the expected outcome and why it matters.}

**Checklist**

- [ ] {Actionable requirement}
- [ ] {Actionable requirement}

**User Story**

- **Given:** {context}
- **When:** {action}
- **Then:** {outcome}
```

- Requirement groups are numbered only once there are two or more
- Every group ends in a `**Checklist**` of literal `- [ ]` items a QA engineer can verify
- References, Epic, Parent task, Related tasks and Related tickets appear only when they add value or the source task already has them. A parent named without a link stays as backticked text, never an invented URL
- A table in a ticket carries at most 4 columns, and a table of per-size values leads with Size
- Refining an existing task keeps its section names, order and filename

#### Bug Shape

The template from `assets/bug-report-template.md`, trimmed to the parts every report carries:

```markdown
# {Bug Title}

### About

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

---

### Bug

---

**1. Observed Behavior**

---

{ Describe what happens when the bug is triggered }
- { What the user sees }
- { Any error messages displayed }

Steps to Reproduce:
1. { First action to take }
2. { Second action to take }

---

**2. Expected Behavior**

---

{ Describe what should happen instead. }
- { Design specifications }
- { Previous working behavior }

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced
```

- An unsupplied field reads `Not provided`, never a plausible guess
- Frequency comes from what the source says, not from a count. Three support tickets are three reports, not a frequency
- A root cause appears only as a supplied fact or a labelled hypothesis, and the four checklist items stay exactly as written
- A design review with no shareable link is recorded under `**Design review**` and closed with `(link not provided)`
- `### BDD Scenarios` is added only when a Given, When and Then flow makes the bug clearer

#### Doc Shapes

| Shape | The reader needs to | The first screen answers | Example |
|---|---|---|---|
| Guide | Follow an order or apply a standard | What they can do after following it | `doc-example-guide.md` |
| Catalog | Find and compare repeated entries | What it holds and what is out of scope | `doc-example-catalog.md` |
| Behavior reference | Predict behavior in a given state | The behavior, its boundary and why to predict it | `doc-example-behavior-reference.md` |
| Proposal | Review an option that is not current behavior | The decision sought, before any current state | `doc-example-proposal.md` |
| Narrative overview | Get oriented through prose | The situation, the stakes and where things stand | `doc-example-readme.md` |

The shape follows the reader's job, not whether the subject is product or engineering. A Doc may carry source-backed code, APIs, schemas and runbook steps. Analysis nobody approved is labelled as a proposal.

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

Story and Epic are two kinds of product requirements document, not size tiers. Detail grows with scope while the section order stays fixed.

| Part | Story | Epic |
|---|---|---|
| H1 | `# {Persona} - {Area} - {Feature}` | `# Epic - {Persona} - {Area}` |
| About | Problem, Solution, Expected outcomes, References | Problem, Goal, Solution, References |
| Middle section | `## Requirements`, hard constraints only, left out when there are none | `## Scope` of child stories, plus an optional Added Later group |
| Acceptance criteria | Screen level | Release level |

A real Story from the 2026-09-18 run, `export/benchmark/skill/SST-001 - 002 - PRD-payout-pause.md`, from Requirements to the end of the file:

```markdown
## Requirements
* * *
**Pending payout pause**
* * *
*   A pause of a pending payout lasts exactly `24 hours`
*   The reason field is required
*   The toggle that starts a pause reads `Pause payout`
*   The payout row of a paused payout shows a `paused` badge
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A brand pauses a payout that has not released**
* * *
*   **Given** a payout that is still pending
*   **When** the brand pauses it
*   **Then** the payout waits instead of releasing
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The payout releases when the pause ends**
* * *
*   **Given** a payout that is paused
*   **When** the pause ends
*   **Then** the payout releases on its own
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

- Every hard value the source supplied lands in Requirements verbatim, in backticks and in the source's own units. `32px` never becomes "updated spacing" and `Link Instagram` never becomes "updated copy"
- A supplied value stays out of the acceptance criteria, which describe outcomes and leave the mechanism to the developer
- Requirements hold constraints a build can fail. A bullet that only describes what a screen shows is struck, and a `**Checklist**` or `- [ ]` item never appears there
- Each criterion is a numbered `1\.` block closed by its Mark-as-done checkbox, with no divider before the next one. The `* * *` above the `##   ` spacer closes the section
- `## Delivery` (Estimation, Rabbit holes, No-gos) is added only on request or when an `**Open:**` line or an undated external constraint forces it
- No ticket header fields, story points or INVEST notes appear. The reply names the kind: Story or Epic

Nine optional enrichments exist for a Story that earns them. They include a Connextra promise block, a Rule block for an exact threshold, Definition of Ready and Done gates and a single `← PRIO` marker. `prd-example-complete.md` shows seven of them in one Story, and most stories use none.

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

#### Bands

| Band | Completeness, Clarity, Actionability, Relevance, Mechanism depth | Accuracy |
|---|---|---|
| Below the near miss | 0 to 4, required content absent | 0 to 5, a claim contradicts a supplied source |
| Near miss | 5 to 7, one named defect stands | 6 to 8, an unsupplied claim stands |
| Clears the floor | 8 to 10 | 9 to 10 |

A 10 is not a target. It records that a deliberate second pass found nothing.

#### Which Dimension Decides Each Shape

| Shape | Decided by | The standard near miss |
|---|---|---|
| Task | Actionability | A checklist item with no observable end state |
| Bug | Accuracy | A root cause or step no evidence supports, where `Not provided` belonged |
| Doc | Accuracy and Relevance | A claim no source covers, even under a spotless layout |
| Story | Clarity and Mechanism depth | A supplied `32px` written as "updated spacing", which drops Accuracy to 7 |
| Epic | Completeness, read against the Epic shape | Scoring an Epic down for having no Requirements, which is a rubric error |

#### Revision Ladder

| Dimensions under floor | Status | Action |
|---|---|---|
| None | PASS | Harmonize and export |
| One | REVISION NEEDED | Fix it at the phase that owns it, then re-score |
| Two or more | REJECTED | Return to Engineer and rebuild the shape |

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
export/[###] - PRD-[description].md
export/[###] - Epic-[description].md
export/[###] - {task|bug|doc|PRD|Epic}-[description]-clarification.md
export/[original-source-filename].md
```

A new artifact takes the next free three-digit number and a short lowercase hyphenated description. A clarification with no resolved artifact uses `intake` as its artifact word. A refinement is saved under the exact source filename, such as `export/Barter deal - Image(s).md`, so it can be compared with the original. The supplied source itself is never overwritten.

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

The reply never pastes the artifact. It carries the path, the receipt, the self-scan line, a quality summary and a two- or three-sentence summary, plus one ClickUp offer when ClickUp tooling is connected. A Doc reply gives one verdict line each for Source safety, Shape fit, ClickUp layout, Readability and Voice, marked pass or attention.

The same run shows why the receipt is checked rather than trusted. Every skill-side save was read back, yet the printed line count matched the file within one line in only 5 of 13 replies.

#### ClickUp Delivery

| Operation | Parameter that keeps the markdown |
|---|---|
| Create task | `markdown_description` |
| Update task | `markdown_content` (the claude.ai connector uses `markdown_description`) |
| Create document or page | `content` with `content_format: "markdown"` |
| Read a task back | `include_markdown_description=true` |

- The export never asks permission. A ClickUp create, update or delete always does, as an explicit yes in the current conversation. An earlier yes does not carry forward
- The artifact's H1 becomes the ClickUp name and leaves the body. HTML comments and process metadata are stripped. Everything else travels verbatim
- The plain `description` field stores markdown as literal text, so visible `###` or `**` in ClickUp means the wrong parameter was used
- After a push the task is read back with markdown enabled to confirm the formatting survived

#### What Git Keeps

`.gitignore` ignores everything under `export/` except `.gitkeep` and `export/benchmark/`. Your own artifacts stay on your machine, and the public repository carries only the deliverables from the benchmark run.

&nbsp;

## 9. 📚 TEMPLATES AND EXAMPLES

A route loads its template together with its mode reference. A worked example loads only when a filled instance helps, one file at most and only from the routed mode's folder.

#### Template Assets

| Asset | What it holds |
|---|---|
| `sk-product-owner/assets/task-templates.md` | Canonical, parent, subtask and Quick task scaffolds and the numbering rule |
| `sk-product-owner/assets/bug-report-template.md` | The bug scaffold, the Frequency rules and the design-review rule |
| `sk-product-owner/assets/doc-templates.md` | Five Doc shapes, the ClickUp contract, a Quick adaptation, a refinement overlay and a source-conflict hold |
| `sk-product-owner/assets/story-template.md` | The Story scaffold and its opt-in Delivery close |
| `sk-product-owner/assets/epic-template.md` | The Epic scaffold with Goal and Scope |
| `sk-product-owner/assets/interactive-response-templates.md` | The comprehensive question and the Task, Bug, Story and Doc questions |

#### Worked Examples

`sk-product-owner/assets/examples/` holds 21 filled artifacts. Each names in its frontmatter the template section it instantiates.

| File | Subject | What it shows |
|---|---|---|
| `task/task-example-ui-refinement.md` | Meridian settings screen | Canonical task for design-parity work, no functional change, cross-device accessibility checks |
| `task/task-example-standard-feature.md` | Vantage Analytics filter presets | Parent task: shared scope stated once, child tasks carry their own detail |
| `task/task-example-subtask.md` | Corsair search empty states | Subtask keeping zero-result and request-failure recovery apart |
| `task/task-example-quick.md` | Ledgerly trial-expiry banner copy | Quick task: exact replacement copy, a zero-day variant, no layout change |
| `task/task-example-ds-variables.md` | DS Variables v1.0.7, size variables and disabled states | Parent plus one subtask per app, in the ClickUp format the team ships |
| `bug/bug-example-frontend-visual.md` | Country dropdown behind the checkout payment modal | Visual defect with cross-browser evidence, exact design tokens and a BDD scenario |
| `bug/bug-example-backend-api.md` | Orders endpoint returning duplicate rows across pages | API defect with paired request evidence and conditional reproduction |
| `bug/bug-example-mobile-crash.md` | Crash attaching a large photo on Android 12 | Crash log plus a memory-pressure cause labelled as a hypothesis |
| `bug/bug-example-quick.md` | Terms of Service footer link returning 404 | Quick report with missing environment data marked honestly |
| `doc/doc-example-guide.md` | Driftboard empty-state copy | Guide: one writing standard across four empty-state intents, one of which needs no action |
| `doc/doc-example-catalog.md` | Prism Design System color token roles | Catalog with current, approved and proposed entries labelled one by one |
| `doc/doc-example-behavior-reference.md` | Fieldnote Editor form autosave | Behavior reference with timing, offline and conflict precedence and one edge left open |
| `doc/doc-example-how-it-works.md` | Vantage Billing subscription lifecycle | Behavior reference at system scale, prose-first: renewal, dunning, cancellation and pause |
| `doc/doc-example-proposal.md` | Meridian Mobile dark mode rollout | Proposal: verified context kept apart from candidate design, decision owner still open |
| `doc/doc-example-readme.md` | Ledgerly Payments payout integration docs | Narrative overview as a folder README with an earned reading map |
| `doc/doc-example-quick.md` | Rotating the Ledgerly API signing key | Quick guide: optional sections dropped, status notice and one unverified step kept |
| `story/prd-example-simple.md` | Fieldstack inline project rename | Smallest Story: no Requirements, two criteria, ends on Acceptance criteria |
| `story/prd-example-medium.md` | Lumen profile identity updates | Three safeguards on one settings form, criteria grouped by surface |
| `story/prd-example-complex.md` | Keystone payout release pipeline | Four payout types sharing one pipeline described once in Solution, one `← PRIO` marker |
| `story/prd-example-complete.md` | Presale access windows and redemption limits | Every optional enrichment filled in, as a reference rather than a default |
| `story/prd-example-epic.md` | Gatherwell Event Check-in v2 | Epic: Goal, Scope of child stories with an Added Later group, release-level criteria |

Twenty examples use invented products so they teach form without carrying real Barter material. `task-example-ds-variables.md` is the exception: the three tickets of a real Barter design token release, kept as the pattern for the next one.

#### Reference Files

| File in `sk-product-owner/references/` | Loaded | What it holds |
|---|---|---|
| `hvr-core.md` | Always | Every Human Voice hard blocker inline, plus the self-scan line |
| `conciseness.md` | Always | The reconstruction test, cut and keep rules and format choice |
| `task-mode.md` | Task route | Task shapes, requirement groups, the table rule and source sync |
| `bug-mode.md` | Bug route | The fixed bug structure, evidence handling and the four-item QA checklist |
| `doc-mode.md` | Doc route | Source classes, authority order, the conflict gate and refinement fidelity |
| `story-mode.md` | Story route | The house grammar, Story or Epic selection and the nine optional enrichments |
| `interactive-mode.md` | Interactive route | The single-question flow, its state machine and the clarification export |
| `quality-scoring.md` | On demand | Bands, the per-shape reading and the revision ladder |
| `router-contract.md` | On demand | The router as running Python, checked by the differential |
| `human-voice-rules.md` | On demand | The full voice standard behind the card |
| `conciseness-rationale.md` | On demand | The reason behind each conciseness rule |

&nbsp;

## 10. 🧩 CLAUDE PROJECT PACKAGE

`claude project/` carries the same system for a claude.ai Project, which has no filesystem and never loads `SKILL.md`.

| Part | What it is |
|---|---|
| `Custom Instructions.md` | The kernel, v1.12.6, aligned to skill v1.8.4. It carries the full router and rules and is the routing authority inside the Project |
| `knowledge/` | 38 files: 17 core documents (five mode references, six templates, four shared rule files, quality scoring and the router contract) and the 21 worked examples |
| `README.md` | Upload steps, the source-to-mirror map and the smoke matrix |
| `kernel-review.json` | A dated record of one kernel review, read by no tool |

#### What Changes in a Project

| Skill in a CLI | claude.ai Project |
|---|---|
| Saves to `export/` and reads the file back | Renders a Deliverable Block as a Canvas Artifact in the side panel |
| Reports `Path:` and the `Verified:` receipt | Reports `Export-equivalent path:`, with `NNN` where the next number is unknown |
| Loads mode files from `references/` and `assets/` | Consults the matching knowledge document |
| Pushes to ClickUp through a connected MCP server | Pushes to ClickUp through the claude.ai connector, when present |

The kernel never claims a save, a read-back or a push the Project did not perform. Setup is the four steps in Quick Start.

#### Hand-Written, Not Generated

Every knowledge file is written by hand from its skill source. It drops loading preambles, routed-by lines and file-path routing. It keeps the decision rules, output shapes and examples. Five files are byte copies instead: the four shared rule files, which are regular-file copies of cards maintained in a shared knowledge folder, and the Router Contract, whose code block the router differential compares byte for byte. `SYNC.md` holds the manual parity method and the dated review notes.

The live Project is a separate manual upload, so a matching local package proves nothing about what is deployed.

&nbsp;

## 11. 🧪 BENCHMARKS AND CHECKS

#### Checks That Run From a Clone

| Command | What it checks | Result on this tree |
|---|---|---|
| `bash benchmark/router/run_fixtures.sh` | 117 route fixtures, then the differential against `router-contract.md` | `PASSED 117/117 fixtures` and `PASSED 189/189 differential inputs` |
| `bash benchmark/format/run_fixtures.sh` | 35 cases over 13 fixture files through the output validator | `PASSED all format-validator fixtures` |
| `python3 benchmark/router/route_contract.py --self-check` | One sample per detection layer | `self-check passed 5 routing expectations` |
| `node benchmark/format/validate-output-format.cjs "<file>"` | One saved artifact against the output rules | `Product Owner output format validation passed across 1 artifact file(s)` |
| `bash benchmark/grader/check_report.sh <report-folder>` | The voice lint of every captured reply, then twin agreement | Writes `hvr-lint.csv` into the folder it reads |

#### What the Router Differential Proves

`route_contract.py` is the router as a program. `router-contract.md` carries the same router as pseudocode, which is what the skill reads. `differential.py` lifts that pseudocode out of the markdown, runs it and compares the two on four guards:

- Copy parity: the Project's Router Contract carries the same code block byte for byte
- Table parity: topics and their order, overrides, thresholds, regexes, resource lanes and the fallback checklist match value for value
- Behavior parity: every corpus input matches layer by layer (energy, commands, framing, top topic and score) and then as a whole route object
- Corpus coverage: every command, alias, false-prefix case and topic is exercised

Prose and code cannot drift apart without one of the four failing.

#### What the Format Validator Catches

- Prose em dashes, with a dash inside a file path left exempt
- A divider between a Mark-as-done checkbox and the next criterion
- House grammar breaks: a heading with no divider under it, a `---` rule, a heading deeper than H4, a Checklist or checkbox in Requirements, asterisk emphasis, a second `← PRIO` and too many ellipses or emoji
- Requirements bullets that narrate a screen instead of stating a constraint
- Conciseness breaks: banned openers, heading echo, hedge stacks and terminal recaps
- A Delivery section whose every slot is a placeholder, reported as advice rather than a block

Silent fixtures pin the other side: a compliant house Story, the sanctioned delimiter shapes and near-miss prose must all pass.

#### The Manual Testing Playbook

`sk-product-owner/manual-testing-playbook/` turns the contract into 14 two-turn conversations: seven for the skill (`S` IDs) and a twin of each for the Project (`P` IDs).

| Twin | What it checks |
|---|---|
| `SID-001` / `PID-001` | The delivery identity: a real path and read-back, or a Deliverable Block and no save claim |
| `STK-001` / `PTK-001` | `$task` asks one question, then turns the answer into a checklisted task |
| `SBG-001` / `PBG-001` | `$bug` waits for evidence and marks what is missing `Not provided` |
| `SDK-001` / `PDK-001` | A Doc request with the notes still to come asks every open field at once |
| `SDK-002` / `PDK-002` | Two conflicting notes stop the draft until one is chosen |
| `SST-001` / `PST-001` | "Turn these notes into a PRD" keeps every hard value verbatim |
| `SIR-001` / `PIR-001` | An ambiguous request opens its question with the energy choice |

#### Captured Runs

Two runs of the full playbook sit in `benchmark/reports/`, each with its verdicts, grading notes and captured replies.

| Run | Skill | Project | Twins that disagree | Lint-clean replies |
|---|---|---|---|---|
| 2026-09-17, Claude Sonnet 5 at medium effort | 4 PASS, 3 FAIL | 2 PASS, 5 FAIL | 2 of 7 | 3 of 28 |
| 2026-09-18, GLM 5.3 Flash through Pi at high thinking | 6 PASS, 1 PARTIAL | 6 PASS, 1 PARTIAL | 0 of 7 | 14 of 28 |

- In the Sonnet run, no-command Doc and Story requests skipped the consolidated question on both sides, and both sides opened the ambiguous-intake question with artifact types instead of the energy choice
- In the same run the Project answered `$task` and `$bug` intake as plain chat, without a Deliverable Block. Those are the two twins that disagreed
- 25 of the Sonnet run's 28 replies carried a banned em dash or semicolon. 18 of those 25 held a self-scan line, and every one of them reported 0 hard blockers
- The GLM run agreed on all seven twins. Only the Doc guide pair, `SDK-001` and `PDK-001`, fell short
- In the first GLM pass `SST-001` read a sibling scenario's export and copied a requirement nobody supplied. The rerun inside an operating-system sandbox no longer carried it

Three re-measure rounds of the Doc guide pair, three runs per side each, sit in `remeasure/`, `remeasure-2/` and `remeasure-3/` inside the GLM report. The first round measured the v1.8.2 repair: 2 of 3 runs passed on each side, and no run asked for the notes alone any more. Findings from the rounds drove the v1.8.3 and v1.8.4 releases.

#### What `export/benchmark/` Shows

The 60 files in `export/benchmark/` all come from the GLM run, collected by `run/collect_exports.py` in its report folder.

- `skill/` holds the 12 files the skill scenarios wrote, renamed `<scenario id> - <file name>`
- `claude project/` holds the 12 Deliverable Blocks the Project scenarios returned, saved under the path each reply reported. `PID-001 - NNN - task-payout-pause-toggle.md` keeps the `NNN` a Project cannot know
- 10 of those 24 files are `-clarification` questions, saved before any draft existed
- The other 36 are the re-measure rounds: 3 rounds of 3 runs, one clarification and one guide per run, on both sides

Files worth opening first:

- `skill/STK-001 - 002 - task-creator-payout-pause.md`, three requirement groups built only from the supplied acceptance list
- `skill/SBG-001 - 002 - bug-payout-pause-toggle-reverts-off.md`, Frequency `Always (per reporter)` with Severity, Device and OS Version marked `Not provided`
- `skill/SDK-002 - 002 - doc-payout-pause-behavior-reference.md`, Note A stated as current and Note B kept as retired
- `skill/SST-001 - 002 - PRD-payout-pause.md`, four supplied values carried verbatim into Requirements

#### Maintainer Scripts

`benchmark/parity/` holds five wrappers and `benchmark/gates/` holds `rule_parity.py`. They compare the Claude Project package against the skill sources by calling a shared sync toolkit that lives one folder above this repository in the maintainer's monorepo and is not published. From a clone they stop on the missing file: `rule_parity.py` and `run_parity.sh` both exit 2. Use the checks above instead.

&nbsp;

## 12. 🗂️ REPOSITORY STRUCTURE

```text
.
├── .gitignore                       keeps export/ local except the benchmark deliverables
├── AGENTS.md                        CLI entry point, export protocol and command registry
├── Favicon.jpg                      repository icon
├── LICENSE                          MIT license
├── README.md                        this guide
├── SYNC.md                          manual parity method and dated review notes
├── benchmark/
│   ├── format/                      output validator, 13 fixtures and their runner
│   ├── gates/                       rule_parity.py, maintainer only
│   ├── grader/                      hvr_lint.py, reply linter and twin comparison
│   ├── parity/                      five wrappers into the shared parity gate, maintainer only
│   ├── reports/                     two captured playbook runs
│   └── router/                      route_contract.py, 117 fixtures and the differential
├── claude project/
│   ├── Custom Instructions.md       claude.ai kernel v1.12.6
│   ├── README.md                    upload steps, mirror map and smoke matrix
│   ├── kernel-review.json           dated record of one kernel review
│   └── knowledge/                   38 knowledge files
├── export/                          generated artifacts, ignored by git
│   └── benchmark/                   60 deliverables from the GLM run
└── sk-product-owner/
    ├── README.md                    skill guide
    ├── SKILL.md                     router, rules and delivery protocol
    ├── description.json             skill metadata and trigger examples
    ├── graph-metadata.json          skill graph edges and trigger phrases
    ├── assets/                      six templates
    │   └── examples/                21 worked artifacts in task/, bug/, doc/ and story/
    ├── changelog/                   14 release notes, v1.0.0.0 to v1.8.4.0
    ├── manual-testing-playbook/     14 two-turn scenarios in 10 category folders
    └── references/                  11 rule files, loaded always, per route or on demand
```

`AGENTS.md` points an agent CLI at the skill. A claude.ai Project reads `claude project/Custom Instructions.md` and the files under `claude project/knowledge/` instead.

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

**Q: Do I need the claude.ai package?**

No. The CLI skill is complete on its own. The Project package exists for people who work in claude.ai.

&nbsp;

## 14. 🔧 TROUBLESHOOTING

| What you see | Cause | Fix |
|---|---|---|
| The route does not match the request | A token is not an exact standalone command, or framing outranked a topic word | Check it with `python3 benchmark/router/route_contract.py --request "<request>"`, then use one command |
| `$task` or `$bug` replies with a question | The command routed the request but the scope is missing | Answer in one reply, or resend with `$quick` to accept smart defaults |
| A Doc request stops before drafting | The Doc gate is `BLOCKED` on a field, a conflict or an uncovered subject | Answer the consolidated question with the source or decision it names |
| No `Path:` or `Verified:` line | The read-back failed twice | Treat the artifact as undelivered and rerun the request |
| The `Verified:` line count differs from the file | The model printed a different number than the read returned | Trust the file on disk. The playbook grades the read, not the number |
| ClickUp shows raw `###` or `**` | The push used the plain `description` field | Push again with `markdown_description` or `markdown_content` |
| UI feedback routed to Bug | The wording read as a defect, such as "fix" or "broken" with no polish, spacing or Figma term | Use `$task`, or phrase it as polish or Figma alignment |
| A Story has no Requirements section | The source supplied no hard value | Supply the sizes, limits or exact strings the build must meet |
| `run_parity.sh` or `rule_parity.py` exits 2 | They need a sync toolkit outside this repository | Use the router and format checks, which run from a clone |
| `check_report.sh` changed a report folder | It writes `hvr-lint.csv` beside the replies it lints | Run it on a copy of the folder |

&nbsp;

## 15. 📚 RELATED DOCUMENTS

**System guides**

- **[→ Agent Bootstrap](AGENTS.md)** - entry point, export protocol and command registry
- **[→ Product Owner Skill](sk-product-owner/SKILL.md)** - router, rules and delivery protocol
- **[→ Skill README](sk-product-owner/README.md)** - mode-by-mode guide to the skill folder
- **[→ Task Mode](sk-product-owner/references/task-mode.md)** - task, parent-task and subtask rules
- **[→ Bug Mode](sk-product-owner/references/bug-mode.md)** - defect evidence and reproduction rules
- **[→ Doc Mode](sk-product-owner/references/doc-mode.md)** - source classes, authority order and refinement fidelity
- **[→ Story Mode](sk-product-owner/references/story-mode.md)** - house grammar, Story and Epic, optional enrichments
- **[→ Interactive Mode](sk-product-owner/references/interactive-mode.md)** - one-question flow and state machine
- **[→ Quality Scoring](sk-product-owner/references/quality-scoring.md)** - bands, per-shape reading and the revision ladder
- **[→ Router Contract](sk-product-owner/references/router-contract.md)** - the router as running Python
- **[→ Worked Examples](sk-product-owner/assets/examples/)** - 21 filled artifacts by mode
- **[→ Manual Testing Playbook](sk-product-owner/manual-testing-playbook/manual-testing-playbook.md)** - the 14 scenarios and their pass criteria
- **[→ Latest Release Notes](sk-product-owner/changelog/v1.8.4.0.md)** - v1.8.4.0, the closed Doc intake field list

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

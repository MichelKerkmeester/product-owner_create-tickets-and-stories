# Product Owner - Create Tickets & Stories

> Turns product requests into evidence-based tickets, stories and source-safe documentation.

&nbsp;

> Like it? Please don't buy me unwanted coffee: https://buymeacoffee.com/michelkerkmeester

[![GitHub Stars](https://img.shields.io/github/stars/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&logo=github&color=fce566&labelColor=222222)](https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories/stargazers)
[![License](https://img.shields.io/github/license/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&color=7bd88f&labelColor=222222)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/MichelKerkmeester/product-owner_create-tickets-and-stories?style=for-the-badge&color=5ad4e6&labelColor=222222)](https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories/commits/main)

## 1. SUMMARY

A product owner in a folder: it turns a half-formed product request into a task, bug report, product requirements document or source-safe document.

It never invents a fact to fill a gap, and every artifact lands as a file before the reply mentions it.

Built for any capable model in an agent CLI that reads `AGENTS.md`, and for claude.ai Projects through `claude project/`

**What's inside**

- 🧭 **Smart Router** - selects Task, Bug, Doc, Story or Interactive handling from exact commands and request framing
- 📋 **Backlog Artifacts** - shapes tasks, subtasks, bugs, Stories and Epics around outcomes and acceptance conditions
- 📖 **Five Doc Shapes** - writes guides, catalogs, behavior references, proposals and narrative overviews
- 🧰 **Templates and Examples** - six templates and 21 worked examples across task, bug, doc and story
- 🎯 **Quality Gates** - checks six quality dimensions, source fidelity and Human Voice Rules
- 📤 **Verified Delivery** - saves artifacts before it reports a path, with optional ClickUp delivery

**Why it earns a place**

- **Clear routing:** explicit commands and artifact framing keep requests on one output path
- **Source safety:** documentation preserves the status of verified facts, proposals and unknowns
- **Visible delivery:** every saved artifact receives a read-back check before the response

---

## 2. 🎁 OVERVIEW

### THE FOUNDATION

Three building blocks carry a request through Product Owner:

1. **Routing** selects the artifact intent and its matching workflow.

2. **Shaping** applies the template and source rules for that artifact.

3. **Validation and delivery** check quality, save the file and verify it before the response.

From request to delivered artifact:

```text
                         YOUR REQUEST
                               │
                               ▼
                ┌────────────────────────────┐
                │       SMART ROUTER         │
                │                            │
                │  Exact command or framing  │
                │  Semantic route if needed  │
                │  One question if unclear   │
                └──────────────┬─────────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │     MODE AND TEMPLATE      │
                │                            │
                │  Task, Bug, Doc or Story   │
                │  One routed template       │
                │  Source status checked     │
                └──────────────┬─────────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │    QUALITY AND DELIVERY    │
                │                            │
                │  Six quality dimensions    │
                │  Voice and format checks   │
                │  Export and read-back      │
                └──────────────┬─────────────┘
                               │
                               ▼
                         VERIFIED FILE
                               │
                               ▼
             Optional ClickUp push after approval
```

### Smart Router

One request, one artifact.

Exact commands set the route before any topic scoring begins.

- `$task`, `$bug`, `$doc`, `$story` and `$epic` match only as standalone tokens, so `$document` or `$debug` never trigger a route
- Plain language routes by artifact framing: "create a task to document X" is a Task, "document how X works" is a Doc
- Two conflicting commands get one consolidated question instead of a guess

### Backlog Artifacts

Tickets a delivery team can build from.

Each backlog shape states what should change and why, then leaves the how to the team.

- Tasks carry numbered requirement groups with checklists a QA engineer can verify
- Bug reports never invent a root cause, and every missing field reads `Not provided`
- Stories and Epics use the Barter house format with Given, When and Then acceptance criteria

### Source-Safe Documentation

Docs that never pass a proposal off as shipped.

Doc Mode keeps current behavior, approved direction, proposals, retired material and unknown claims apart.

- Every material claim gets one of five status classes before drafting starts
- Recency alone is never authority, and an unresolved contradiction stops the draft with one question
- Five adaptive shapes match the reader's job, from an ordered guide to a prose-first overview

### Quality Gates

Floors that block, not scores that advise.

Six dimensions check that an artifact is complete, clear, actionable, accurate, relevant and deep enough on mechanism.

- Five dimensions carry a floor of 8 out of 10 and Accuracy carries 9
- A dimension under its floor stops the export and names the work
- Human Voice Rules, source fidelity and output-format checks run alongside the score

### Verified Delivery

Saved, read back, then reported.

Each artifact is written under `export/` and read back before the response names its path.

- The reply carries the path and a `Verified:` receipt with the saved file's line count
- No receipt means the artifact is undelivered
- ClickUp delivery waits for an explicit yes in the current conversation, every time

---

## 3. 🚀 QUICK START

### Installation

**Prerequisites**

- Git to clone the repository
- An agent CLI that reads `AGENTS.md` and accepts your model
- Bash, Python 3 and Node.js for the benchmark checks
- For claude.ai, a Project that accepts custom instructions and knowledge files

Clone the repository and open it in your agent CLI:

```bash
git clone https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories.git
cd product-owner_create-tickets-and-stories
```

Point the model at `AGENTS.md`. It loads `sk-product-owner/SKILL.md`, and from then on the model works as the Product Owner.

### Verify Installation

Run the fixture checks from the repository root:

```bash
bash benchmark/router/run_fixtures.sh
```

Expected output:

```text
PASSED 117/117 fixtures
PASSED 189/189 differential inputs (9 topics, 114 synonyms in parity, 61 SKILL.md triggers checked)
```

The format check runs fixed Markdown cases through the output validator:

```bash
bash benchmark/format/run_fixtures.sh
```

Expected final line:

```text
PASSED all format-validator fixtures
```

Both checks run without a model or a network connection.

### First Use

Try one of these requests once the CLI has read `AGENTS.md`:

| Request | Route | What comes back |
|---|---|---|
| `$task define the saved-deal empty state` | Task | A scoped task file with testable requirements |
| `$bug login returns the wrong error message` | Bug | An evidence-based defect report |
| `$doc document how notification delivery works` | Doc | A source-checked document in the matching shape |
| `$story saved searches for creators` | Story | A product requirements document with outcome criteria |
| `$quick $doc a short guide for rotating the signing key` | Doc with Quick energy | A shorter document with the same safety gates |

Most requests first get one consolidated question about purpose, scope or evidence. Once answered, the response names the saved path, gives a quality summary and confirms the read-back. New files land in `export/` as Markdown.

A verified response carries a path and receipt:

```text
Path: export/001 - task-saved-deal-empty-state.md
Verified: read-back succeeded; N lines
```

### Use It in a claude.ai Project

The Project package gives claude.ai the same routing and artifact rules through its own instructions and knowledge files.

1. Create or open a Project named **Product Owner**
2. Paste `claude project/Custom Instructions.md` into its custom instructions
3. Upload every file in `claude project/knowledge/` with its filename unchanged
4. Update the instructions and the knowledge files together when the package changes

A Project has no filesystem, so each artifact arrives as one markdown Deliverable Block labelled with its export-equivalent path.

The package contains 38 knowledge files. See [the Project README](claude%20project/README.md) for its file map and upload steps.

---

## 4. 🧭 MODES AND ROUTING

Product Owner routes requests to one artifact intent. Quick changes the amount of detail, not the selected intent.

#### Request Routes

| Route | Commands | Output |
|---|---|---|
| Task | `$task`, `$t`, `$task --subtask` | Tasks, subtasks and parent tasks |
| Bug | `$bug`, `$b` | Evidence-based bug reports |
| Doc | `$doc`, `$d` | Product and engineering documentation |
| Story | `$story`, `$s`, `$prd`, `$p` | Story-shaped product requirements documents |
| Story Mode, Epic shape | `$epic`, `$e` | Epic-shaped product requirements documents |
| Interactive | No command or conflicting intent | One consolidated question |

The router has five user-facing outcomes: Task, Bug, Doc, Story and Interactive. Epic selects a Story Mode shape.

#### Routing Precedence

| Signal | Behavior |
|---|---|
| Exact command | Selects its route before natural-language scoring |
| Artifact framing | Selects the named deliverable when no command applies |
| Semantic topic | Scores the remaining request when no command or framing applies |
| Conflicting commands | Asks one question that resolves the artifact choice |
| Quick token | Sets energy only and never selects an artifact |

#### Precedence, By Example

| Request | Routes to |
|---|---|
| "Create a task to document Feed v2" | Task |
| "Write a bug report about documentation export naming" | Bug |
| "Document bug behavior for failed payments" | Doc |
| "Document how geo targeting works" | Doc, Behavior reference shape |
| "Recommend a ranking approach and document it" | Doc, labelled Proposal |
| "Write a user story for saved searches" | Story |
| "Create a task to write a PRD about search" | Task |
| "Refine the settings panel spacing" | Task, the UI-refinement override |
| `$task $doc explain Feed v2` | One clarification question, no artifact |

Command tokens are exact: `$d,` counts, while `$document`, `$docs`, `$debug` and `$d.md` do not. Negated phrasing such as "this is not a quick task" never triggers Quick energy.

#### Doc Shapes

Doc Mode selects one of five shapes by the reader's job:

| Shape | Use it when the reader needs to |
|---|---|
| Guide | Follow a sequence or apply a standard |
| Catalog | Locate and compare repeated entries |
| Behavior reference | Predict system behavior in a given state |
| Proposal | Review an option that is not current behavior |
| Narrative overview | Get oriented through prose, such as a README or handover |

#### Story and Epic

Story and Epic are two artifact kinds under Story Mode.

- **Story:** one feature area with outcomes and acceptance criteria, plus hard requirements only when the source supplies them
- **Epic:** an initiative split into child stories, with a Goal and Scope but no Requirements section

Both use numbered Given, When and Then criteria. Delivery details appear only when requested or required by an open question or external constraint.

#### Energy Levels

| Energy | How it changes the work |
|---|---|
| Raw | Skips the phase flow only when explicitly requested, while safety and delivery rules remain |
| Quick (`$quick`, `$q`) | Uses smart defaults and trims optional detail without skipping gates |
| Standard | Uses the full phase flow with at least three perspectives |
| Deep | Uses expanded analysis with all five perspectives |

---

## 5. 🧱 OUTPUT FORMAT AND QUALITY GATES

Every artifact follows its routed template and keeps process notes out of the deliverable.

#### Task Shape

Task output says what changes and why it matters, then lists verifiable requirements:

```markdown
# Task Title

### About

---

What should change, why it matters and the outcome it creates.

### Requirements

---

1.  **First requirement group**

---

Short outcome description.

**Checklist**

- [ ] Literal, verifiable requirement
- [ ] Another requirement

**User Story**

- **Given:** context
- **When:** action
- **Then:** outcome
```

#### Bug Shape

Bug output records what was observed and what should happen:

```markdown
# Bug Title

### About

---

Scope, affected users and the report window.

### Bug

---

1. **Observed Behavior:** what happens
2. **Expected Behavior:** what should happen instead

**Steps to Reproduce**

1. Exact step from the reported flow
2. Another supported step
```

A diagnosis appears only when the source supplies it or the report marks it as a hypothesis. Missing severity, device or environment details stay marked as not provided.

#### Doc Shape

New Docs use ClickUp Markdown grammar. A title and major headings organize the artifact. Each content heading receives its divider.

```markdown
# Document Title

* * *

## Overview
* * *

Opening prose that orients the reader.

### Subsection
* * *

Source-backed detail belongs under the matching section.
```

Definition entries use a bold term followed by a definition. New Doc files use the same Markdown rules as an approved ClickUp push.

#### Story and Epic Shape

Story Mode uses the Barter house format and keeps hard constraints apart from outcomes. The `##   ` spacer headings belong to the format:

```markdown
# {Persona} - {Area} - {Feature}
* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
{What this story covers.}

### Problem
* * *
{What breaks or is missing today.}

### Solution
* * *
{The approach, written as a decision.}

#### **Expected outcomes**
* * *
*   {Result for users or the business}

##   
## Requirements
* * *
**{Constraint group}**
* * *
*   {A hard requirement the delivery must satisfy}
* * *

##   
## Acceptance criteria
* * *
1\. **{What the user can now rely on}**
* * *
*   **Given** {the situation the user is in}
*   **When** {what they do}
*   **Then** {the outcome they experience}
* * *
- [ ] _Mark as done, if the criteria are met_
* * *

##   
```

Requirements appear only when the source supplies a hard constraint, and every supplied value travels verbatim. An Epic swaps Requirements for a `## Scope` of child stories. A `## Delivery` section closes the artifact only on request.

#### Quality Scoring

The quality gate checks six dimensions:

| Dimension | What it checks | Floor |
|---|---|---:|
| Completeness | Required sections and supplied evidence | 8 |
| Clarity | One reading for each requirement and criterion | 8 |
| Actionability | Observable outcomes | 8 |
| Accuracy | Claims trace to evidence or carry their correct status | 9 |
| Relevance | The requested scope, without adjacent work | 8 |
| Mechanism depth | Enough rationale to settle a nearby case | 8 |

Every dimension scores out of 10. Accuracy sits a point higher because an invented fact reads as confidently as a verified one and costs more downstream.

Source classification and Human Voice Rules run alongside the quality review. A failed blocking gate keeps the artifact from delivery.

#### Quality by Energy

| Energy | Perspectives | Validation |
|---|---|---|
| Quick | One or two recommended | Safety, factuality and delivery gates stay active |
| Standard | At least three | Full quality and voice review |
| Deep | Five | Full review with expanded analysis |
| Raw | No phase flow | Safety and delivery rules stay active |

---

## 6. 📤 EXPORT AND CLICKUP DELIVERY

Export happens before the response. The system verifies the saved file before it reports delivery.

#### File Naming

New artifacts use a numbered path:

```text
export/[###] - task-[description].md
export/[###] - bug-[description].md
export/[###] - doc-[description].md
export/[###] - PRD-[description].md
export/[###] - Epic-[description].md
```

A new artifact takes the next free sequence number. A refinement keeps the source filename so it can be compared against the original.

The response reports the path, a read-back receipt, a quality summary and the required Human Voice self-scan line. It does not paste the full artifact.

#### Read-Back Receipt

A path alone does not verify a save. Product Owner reads the saved file and uses the returned line count in its receipt.

```text
Verified: read-back succeeded; N lines
```

If the read-back fails, the response does not claim delivery.

#### ClickUp Delivery

ClickUp delivery requires explicit approval in the current conversation. The local export never waits for that approval.

| Operation | Markdown-aware parameter |
|---|---|
| Create task | `markdown_description` |
| Update task | `markdown_content` |
| Create document or page | `content` with `content_format: "markdown"` |
| Read task back | `include_markdown_description=true` |

The artifact's H1 becomes the ClickUp item name and drops out of the body. The plain `description` field stores markdown as literal text, so a push that shows `###` or `**` in ClickUp used the wrong parameter.

#### Local Output Rules

Generated deliverables stay local. The root `.gitignore` ignores everything in `export/` except `.gitkeep` and the benchmark deliverables in `export/benchmark/`.

This lets the public repo carry the tool and its checks without publishing generated user artifacts.

---

## 7. 📚 TEMPLATES AND EXAMPLES

The templates give each artifact a known starting shape. Routed loading keeps unrelated examples out of a request.

#### Template Assets

| Asset | Use |
|---|---|
| `sk-product-owner/assets/task-templates.md` | Canonical task, parent-task, subtask and Quick-task shapes |
| `sk-product-owner/assets/bug-report-template.md` | Bug sections and evidence fields |
| `sk-product-owner/assets/doc-templates.md` | Five adaptive Doc shapes and refinement overlay |
| `sk-product-owner/assets/story-template.md` | Story scaffold |
| `sk-product-owner/assets/epic-template.md` | Epic scaffold |
| `sk-product-owner/assets/interactive-response-templates.md` | One-question intake templates |

These six template assets cover Task, Bug, Doc, Story, Epic and Interactive requests.

#### Worked Examples

`sk-product-owner/assets/examples/` holds 21 filled artifacts. Twenty use invented products, and one is a real design token release.

| Folder | Files | Example content |
|---|---:|---|
| `task/` | 5 | Task, subtask and UI refinement patterns |
| `bug/` | 4 | API, visual and crash reports |
| `doc/` | 7 | Guides, catalogs, behavior references and proposals |
| `story/` | 5 | Stories and Epics |

Load a single example when the routed template benefits from a concrete instance.

#### Reference Files

| Group | Purpose |
|---|---|
| `references/` | Mode workflows, router behavior, scoring and writing rules |
| `manual-testing-playbook/` | Scenario steps and expected outcomes for manual checks |
| `changelog/` | Skill release notes |

The Project package keeps 38 knowledge files with the same user-facing routing and rules. Its instructions and files are hand-maintained for claude.ai use.

---

## 8. 🧪 BENCHMARKS AND CHECKS

Two checks run from a fresh clone, from the repository root, with no model involved:

| Command | What it checks | Expected result |
|---|---|---|
| `bash benchmark/router/run_fixtures.sh` | Router fixtures and the differential check | `PASSED 117/117 fixtures` and `PASSED 189/189 differential inputs` |
| `bash benchmark/format/run_fixtures.sh` | Fixed Markdown cases through the output validator | `PASSED all format-validator fixtures` |

The differential check lifts the Smart Router pseudocode out of `SKILL.md`, runs it and proves it agrees with `route_contract.py`, so prose and code cannot drift apart unnoticed.

#### Captured Runs

`benchmark/reports/` holds two manual-testing-playbook runs, each with its results, verdicts and captured replies. The deliverables those runs wrote sit in `export/benchmark/`. `bash benchmark/grader/check_report.sh <report-folder>` lints a run's replies and flags any scenario where the skill and the Project reached different verdicts.

#### Maintainer Scripts

`benchmark/parity/` and `benchmark/gates/` compare the Claude Project package against the skill sources. They call a shared sync toolkit that is not part of this repository, so they do not run from a clone.

---

## 9. 🗂️ REPOSITORY STRUCTURE

The root separates the skill source, Claude Project package, benchmark checks and local export folder.

```text
.
├── .gitignore                       ignores local export outputs
├── AGENTS.md                        CLI entry point
├── Favicon.jpg                      repository icon
├── LICENSE                          MIT license
├── README.md                        public repository guide
├── SYNC.md                          Project package parity notes
├── benchmark/
│   ├── format/                      output-format fixtures
│   ├── gates/                       maintainer rule-parity check
│   ├── grader/                      reply and run-report checks
│   ├── parity/                      maintainer Project drift scripts
│   ├── reports/                     captured benchmark runs
│   └── router/                      route fixtures and contract
├── claude project/
│   ├── Custom Instructions.md       claude.ai Project instructions
│   ├── README.md                    Project upload guide
│   └── knowledge/                   38 Project Knowledge files
├── export/                          generated outputs, kept local
│   └── benchmark/                   deliverables from the captured runs
└── sk-product-owner/
    ├── README.md                    skill guide
    ├── SKILL.md                     routing and operating rules
    ├── assets/                      six templates and examples/
    │   └── examples/                21 worked artifacts
    ├── changelog/                   skill release notes
    ├── manual-testing-playbook/     manual validation scenarios
    └── references/                  routed rules and mode guides
```

`AGENTS.md` points an agent CLI at the skill. A claude.ai Project reads `claude project/Custom Instructions.md` and the files under `claude project/knowledge/` instead.

---

## 10. ❓ FAQ

**Q: Does Product Owner implement the task it writes?**

No. Product Owner writes backlog and documentation artifacts. Another workflow or team handles implementation.

**Q: Can a Doc include technical details?**

Yes. Doc Mode can describe source-backed code, APIs, schemas, operations and architecture. Recommendations remain proposals until a source establishes approval.

**Q: What happens when two sources disagree?**

The draft pauses at the conflict. Product Owner asks one consolidated question instead of combining claims with different authority.

**Q: Does Quick energy skip the checks?**

No. Quick trims optional depth while source safety and delivery gates remain active.

**Q: Does it send a task to ClickUp automatically?**

No. It saves the local file first and waits for approval before a ClickUp write.

**Q: What if I state one requirement and the model finds four?**

Your stated count wins. Clauses, edge cases and acceptance checks inside a stated requirement never create extra requirements.

---

## 11. 🔧 TROUBLESHOOTING

| What you see | Cause | Fix |
|---|---|---|
| The route does not match the request | A token may not be an exact standalone command | Use one supported command or state the artifact in the request |
| A Doc request stops for clarification | Source authority, scope or status is unresolved | Answer the consolidated question with the source or decision |
| No `Verified:` line or `Path:` appears | The saved output did not pass read-back | Treat the artifact as undelivered and rerun the request |
| ClickUp shows raw `###` or `**` | The push used the plain `description` field | Push again with the markdown-aware parameters in section 6 |
| A UI feedback request routed to Bug | "Fix" appeared next to design-parity wording | Use `$task`, or phrase it as polish or Figma alignment |
| `run_parity.sh` fails with a missing file | The parity scripts need a sync toolkit outside this repo | Use the router and format checks, which run standalone |

---

## 12. 📚 RELATED DOCUMENTS

**System guides**

- **[→ Agent Bootstrap](AGENTS.md)** - entry point for an agent CLI
- **[→ Product Owner Skill](sk-product-owner/SKILL.md)** - router, quality rules and artifact protocol
- **[→ Product Owner README](sk-product-owner/README.md)** - detailed capability and mode guide
- **[→ Task Mode](sk-product-owner/references/task-mode.md)** - task and subtask structure
- **[→ Bug Mode](sk-product-owner/references/bug-mode.md)** - defect evidence and reproduction rules
- **[→ Doc Mode](sk-product-owner/references/doc-mode.md)** - source authority and documentation shapes
- **[→ Story Mode](sk-product-owner/references/story-mode.md)** - Story and Epic contracts
- **[→ Interactive Mode](sk-product-owner/references/interactive-mode.md)** - one-question fallback
- **[→ Templates](sk-product-owner/assets/task-templates.md)** - task, parent-task, subtask and Quick-task shapes
- **[→ Worked Examples](sk-product-owner/assets/examples/)** - examples grouped by artifact type

**Claude Project package**

- **[→ Project Setup](claude%20project/README.md)** - custom instructions, knowledge files and upload steps
- **[→ Parity Notes](SYNC.md)** - hand-authored package parity notes

**Benchmark guides**

- **[→ Router Checks](benchmark/router/README.md)** - route fixtures and differential checks
- **[→ Format Checks](benchmark/format/README.md)** - ClickUp and Barter output grammar
- **[→ Parity Checks](benchmark/parity/README.md)** - read-only commit-date comparison

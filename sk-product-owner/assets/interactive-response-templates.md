---
title: "Product Owner - Assets - Interactive Response Templates"
description: "Copy/apply response templates for Product Owner intake questions and the one delivery reply shape every reply follows."
contextType: general
importance_tier: important
trigger_phrases:
  - "interactive response templates"
  - "comprehensive intake question"
  - "task format question"
  - "bug context question"
  - "story context question"
  - "Story context question"
  - "document context question"
  - "source authority question"
  - "one question intake"
version: 0.17.0.11
---

# Product Owner - Assets - Interactive Response Templates

Copy/apply response templates for Product Owner interactive intake, and the one reply shape every delivery and clarification reply follows.

**Loading Condition:** Section 3 ALWAYS, before the first reply of a session. Sections 1 and 2 CONDITIONAL, with `references/interactive-mode.md` whenever a request reaches the one-question flow
**Purpose:** Provides the intake prompts each artifact lane asks when required information is missing, so one question covers every unresolved decision, and the delivery reply shape every other surface points at
**Scope:** The comprehensive question, the Task, Bug, Story and Doc context questions, the source-authority question, the response formatting rules and the delivery reply shape with its worked replies
**Output Path:** `export/[###] - {task|bug|doc|Story|Epic}-[description]-clarification.md`

---

## 1. OVERVIEW

### Purpose

Provides reusable multi-line markdown prompts for default intake, task-specific intake, bug-specific intake, Story intake and product- or engineering-document creation or refinement.

### Usage

Load this asset with Interactive Mode. Copy the appropriate question template, keep the multi-line markdown structure and ask one consolidated question before waiting for the user. For Doc requests, populate only unresolved fields and list every known source conflict in the same question. When artifact commands conflict, include artifact selection and any conditional Doc fields together so one response can resolve routing and Doc context. Do not end a newly authored or rewritten bullet item with a full stop.

---

## 2. RESPONSE TEMPLATES

**CRITICAL: All templates must be multi-line markdown. Never convert to single-line text.**

### Comprehensive Question (Default)

```markdown
Welcome! Let's create exactly what you need.

Please provide the following information at once:

[If artifact commands conflict: I detected these deliverables: {detected_artifacts}. Choose one primary deliverable and complete its relevant fields below.]

**0. How should I work this?**
- Quick - lean pass with smart defaults, minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Deliverable type:**
- Task - Development task with QA checklist
- Bug - Defect report with evidence and reproduction steps
- Story - A Story or Epic in the Barter house format, new or refined, with numbered Given/When/Then acceptance criteria, and Connextra lines or Definition of Ready/Done gates only where the artifact earns them
- Doc - Product or engineering guide, catalog, behavior reference, runbook, technical reference, or proposal; new or refined

**2. Scope & complexity:**
- For tasks: Backend/Frontend/Mobile/Full-stack/DevOps/QA
- For bugs: Platform, affected area, severity and reproduction context
- For Stories: Create or refine, the user role and value, how many requirements, and whether they share one mechanism
- For docs: Create or refine, product/engineering/mixed domain, purpose, audience, required technical depth, requested scope and preferred shape if known

**3. Requirements:**
- What needs to be built/fixed
- Why does this matter? (problem being solved)
- What does success look like?
- For docs: What should readers understand, decide or do after reading?

**4. Sources, authority & status:**
- For docs: Source files or links, which source controls any conflict, and whether claims are current behavior, approved direction, proposal, retired material or unknown
- For tasks and bugs: References, evidence, dependencies and relevant constraints

**5. Additional context:**
- Target audience, product or engineering constraints, dependencies
- Figma references? Platforms? (iOS / Android / Web / All)

**6. Assumptions to challenge:**
- What am I likely to assume incorrectly?
- What "impossible" options should I consider?
```

### Task Format Question

```markdown
I'll create your task. Quick questions:

**Format & scope:** Backend/Frontend/Mobile/Full-stack/DevOps/QA
**Requirements:** What needs to be built/fixed? Acceptance criteria? Technical constraints?
**Design & platform:** Figma links? Platforms? (iOS / Android / Web / All)
**Dependencies:** Related or dependent tickets?
**Validation:** What am I likely misunderstanding? What constraints should I question?
```

### Bug Context Question

```markdown
I'll create your bug report. Quick questions:

**Bug details:** Unexpected behavior? Expected behavior? Steps to reproduce?
**Environment:** Where does this occur? Platform(s)? (iOS / Android / Web / All)
**Design reference:** Figma references showing expected design?
**Evidence:** Screenshots, error logs, console output? When first noticed? Known workaround?
**Validation:** What should I NOT assume about root cause? Related bug reports?
```

### Story Context Question

Use this when an explicit Story or Epic command selects Story intent, or when Story intent is selected but role, value, requirement shape or artifact kind (Story or Epic) cannot be inferred safely. Populate only unresolved fields and wait once.

```markdown
I'll create or refine your Story or Epic. Before drafting, I need the unresolved decisions below in one response:

**Operation:** New Story or Epic, or refine an existing one? For a refinement, which file - I will preserve its structure and only add or adjust what you name.
**Role & value:** Who is the user, and what benefit should the Story deliver? (This becomes the Connextra "As a ..., I want ..., so that ..." line.)
**Requirements:** Which concrete requirements should the Story cover? List them for a Story; if there are none - an initiative split across child stories with a Goal - it is an Epic.
**Shared machinery:** Do the requirements run through one common mechanism (a pipeline, rule ladder, state machine or lifecycle)? If so, describe it once.
**Evidence & links:** Any governing docs, technical identifiers, thresholds or task links to carry into the spec blocks - exact values, please.
**Validation:** What am I likely to assume incorrectly about the user or the promise?
```

### Doc Context and Clarification Question

Use this single pattern for new-document intake, refinement intake, missing source authority, source-status ambiguity and contradictory sources. Include only unresolved items, state known conflicts explicitly, then wait once for the complete response.

```markdown
I'll create or refine the product or engineering document. Before drafting, I need the unresolved decisions below in one response:

**Operation, purpose & audience:** Create or refine? What should the document help its readers understand, decide or do, and who are those readers?
**Domain & detail:** Is this product, engineering, operational, security, compliance or mixed documentation? What technical HOW, code, architecture, API, schema, data-model, debugging or evidence detail does the audience need?
**Source set:** Which files, links or supplied materials may I use? For a refinement, what is the source filename?
**Authority & conflicts:** Which source or claim controls each conflict listed here? [List every known conflict or missing canonical source.]
**Document status:** Should the result describe current behavior, approved direction, proposal, retired material or unknown?
**Scope & shape:** What must be included or excluded? Choose Guide, Catalog, Behavior reference or Proposal/future state, or ask me to infer the shape from the confirmed purpose.
**Layout & refinement boundaries:** New documents use the ClickUp `* * *` divider and `*   ` bullet grammar. For a refinement, what exactly should change? I will preserve existing headings, dividers, bullet markers, order, links, identifiers, tables, code fences, status notices and untouched literal copy outside that scope. State whether structural rewriting or ClickUp normalization is explicitly allowed.
**Validation:** Which claims remain unverified, and what should I avoid presenting as fact?
```

---

## 3. DELIVERY REPLY SHAPE

Every reply after a saved artifact, a saved clarification or a rendered Deliverable Block uses this one shape. `AGENTS.md`, `SKILL.md`, the mode references and the kernel point here instead of restating it. Models copy a worked reply more closely than they follow a rule, so the worked replies below are part of the contract.

### Line Order

1. The path line: `Path: ` and the repository-relative export path in backticks. In a Claude Project it reads `Export-equivalent path: ` and comes after the Deliverable Block
2. `Verified: read-back succeeded; N lines`, on the skill only
3. The `HVR self-scan:` line in its exact shape
4. One quality line, `Quality: {verdict} | Kind: {kind} | Energy: {energy}`
5. Two or three sentences on what the artifact covers
6. The `### Open items` heading, then the numbered items or the one line `None identified`
7. One closing line

A Story bundle repeats lines 1 and 2 for each file, Story first, then gives one `HVR self-scan:` line for the whole bundle. When an export is still blocked after its retry, the reply prints no path line, opens with `Export blocked:` and the reason, and claims no delivery.

### The First Line

Nothing comes before the path line: no status line, no sentence announcing the reply, no report of the checks and no divider. After the last check, the next words written are the path.

- Wrong first line: `Export complete. The task is saved and read back.`
- Right first line: ``Path: `export/009 - task-payout-pause.md` ``

### The Quality Line

- `{verdict}` reads `every floor met` when all six dimensions clear their floors, names the dimension still short when the three-cycle ceiling was reached, such as `Clarity short after three cycles`, and reads `not scored, clarification only` for a clarification
- For a Doc, `{verdict}` names the five Doc checks in order, each `pass` or `attention`, and an attention names its item in brackets: `Source safety pass, Shape fit pass, ClickUp layout attention (two headings missing the trailing divider), Readability pass, Voice pass`
- `{kind}` is Task, Subtask, Parent task, Bug, Story, Epic, Story bundle, or Doc with its shape, such as `Doc (Guide)`
- `{energy}` is Quick, Standard or Deep

The line keeps the pipe separators with a space on each side, carries no bold and holds nothing else. The checks behind it run silently, so no checklist, gate roster, validation display or note about a check that did not run appears anywhere in the reply.

### Open Items

Every addition, assumption, safe default and unresolved point goes here, never into a second question and never into prose elsewhere in the reply. Number each item from 1 with its topic in bold, such as `1. **Owner time zone**`. Directly below it, indented three spaces, come two bullets: `- **Situation:**` followed on the same line by what the source said or what you added, then `- **Open:**` followed on the same line by what the user should confirm or strike. The text after each label starts with a capital.

No blank line sits inside an item or between items, because claude.ai joins a label that stands on a line of its own to the line above it, while a bullet keeps its own line whatever the spacing. An item with nothing left to confirm keeps its number, and its Open bullet reads `Nothing to confirm`. When nothing applies, the section holds the one line `None identified`.

### The Closing Line

- After a delivered artifact, when ClickUp tooling is available: `Want me to push this to ClickUp?`
- After a delivered artifact otherwise: `Want me to change anything?`
- After a clarification: `Answer in one message and I'll draft the {kind}.`, naming the kind and never the artifact's path

Nothing follows the closing line.

### Rules For Every Line

- No bullet ends with a full stop, Open items included
- No em dash and no semicolon in reply prose
- No absolute or temporary path, only the repository-relative export path
- The skill reply never pastes the artifact

### Worked Replies

A delivered task on the skill:

```text
Path: `export/009 - task-payout-pause.md`
Verified: read-back succeeded; 58 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Task | Energy: Standard

The task pauses creator payouts while a dispute is open and restarts them once Finance closes it. It covers the payout screen banner, the paused state in the admin list and the restart rule.

### Open items
1. **Restart cut-off**
   - **Situation:** The brief names Finance as the owner but gives no time zone for the restart cut-off
   - **Open:** Confirm the cut-off runs on Europe/Amsterdam time
2. **Empty state**
   - **Situation:** I added an empty state for an admin list with no paused payouts
   - **Open:** Strike it if the list can never be empty

Want me to change anything?
```

A clarification on the skill:

```text
Path: `export/008 - task-payout-pause-clarification.md`
Verified: read-back succeeded; 16 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Task | Energy: Standard

The file asks one question in four parts: who owns the restart, which payout states count as paused, what the creator sees and what QA signs off. The task comes next once you answer.

### Open items
None identified

Answer in one message and I'll draft the task.
```

A delivered Story in a Claude Project, after the Deliverable Block:

```text
Export-equivalent path: `export/NNN - Story-saved-searches.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Story | Energy: Standard

The Story lets brands save a creator search and get alerts when new creators match it. Requirements carry the supplied limit of ten saved searches and the exact alert copy.

### Open items
1. **Alert frequency**
   - **Situation:** The notes ask for alerts but name no frequency, so the Story uses a daily digest
   - **Open:** Confirm a daily digest or name the frequency
2. **Limit**
   - **Situation:** The notes state ten saved searches per brand
   - **Open:** Nothing to confirm

Want me to push this to ClickUp?
```

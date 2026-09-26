---
title: "PTK-002 -- Design notes FE task"
description: "Validates that a task command pointing at Roamstay date picker design notes renders one context question block, then a front end task block in a Claude Project that carries every stay limit and copy string from the notes and every scope fact from the answer."
version: 1.0.0.1
---

# PTK-002 -- Design notes FE task

This scenario validates the explicit `$task` path from a designer's handover notes to a rendered front end task block, through one clarification turn.

---

## 1. OVERVIEW

A Roamstay PM asks for the front end task behind the date picker stay limits and points at Ines's handover notes. `$task` fixes Task Mode, which still asks its context question before drafting, so Turn 1 renders a task-lane clarification block. Turn 2 answers with the facts the notes do not hold: one task across iOS, Android and web, no parent, the Search squad and the 8.13.0 train, search-service left alone, and QA on all three platforms in en-GB and en-US. The notes carry the rest: the limits, the five picker states, the six copy keys with their en-GB strings, the edge cases, the platform differences and what stays out of this work.

A task that reads like the team's own carries a title in the `{Discipline} - {Surface} - {Feature code} - {Title}` pattern, here `FE`, Guest app and `SRCH`, an About that states the problem the notes give (search-service turns down stays over 30 nights after the guest taps Search, and Guest Support logged 23 chats about it in August), the frame `Date picker / Stay limits` as a plain-text reference, and numbered requirement groups for the limits, the states and copy, the edge cases and the platforms, each with a `**Checklist**`. The corpus closes such tasks with a Resolution Checklist that checks iOS, Android and web and a QA sign-off. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

Design handover notes are the most common input to a front end task, and the Project's block is what a human pastes into the board. A block that hard-codes the limits the notes say come from config, stretches the 365-day rule to check-out or paraphrases the helper text ships a picker that disagrees with the design and with search-service.

---

## 2. SCENARIO CONTRACT

- Objective: Verify task routing, the single context question and a front end task block that keeps every value from the design notes and every fact from the answer
- Real user request: `Can we get Ines's date picker notes into a ticket for the Search squad?`
- Prompt: `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-date-picker-design-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 in the same conversation and inspect the rendered task block
- Expected signals: `$task` still asks its context question once and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Task Mode` line 30, `Product Owner - System - Interactive Mode` line 101), shaped like the Task Format question (`Product Owner - Assets - Interactive Response Templates` line 67). The question renders as its own block, then `Export-equivalent path: export/[NNN] - task-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line, with no file claim and no task (`Product Owner - System - Interactive Mode` lines 62 and 70, root section 5, Clarification turns). A question that asks for a fact the notes already state is recorded only (root section 5, Ticket realism). Turn 2 renders the task as the Deliverable Block before any commentary, fenced where there is no Canvas panel (`Custom Instructions.md` line 85), then `Export-equivalent path: export/[NNN] - task-[description].md` (line 223) and the `HVR self-scan:` line (line 89), with no claim that a file was written (line 101). The block follows the Canonical Task template (`Product Owner - Assets - Task Templates` line 19): H1, `### About` and `### Requirements` (`Product Owner - Templates - Task Mode` lines 52 to 58) and numbered groups each with a `**Checklist**` of `- [ ]` items (lines 82 to 92). It names the frame `Date picker / Stay limits` as plain text with no invented link (`Product Owner - Templates - Task Mode` line 111) and carries the notes verbatim: a stay of 1 night to `30 nights`, check-in at most `365 days` ahead while check-out may land past it, the property minimum of 1 night to `14 nights` on the property page only, the buttons `Select check-in date`, `Select check-out date` and `Show prices`, the helper text `Stays can be up to 30 nights` and `This property has a 3-night minimum` with the property's own number, grey days that stay tappable, limits read from search-service config and the property details and never hard-coded, the design-system calendar on iOS and Android, two months side by side on desktop web and the Monday week start except in `en-US` (`roamstay-date-picker-design-notes.md` lines 15 to 62). It keeps every Turn 2 fact and leaves flexible dates, prices in the calendar and any tracking change out, as the notes do (lines 66 to 68)
- Desired user-visible outcome: One task-lane question block, then a front end task block for the date picker stay limits built from the notes and the answer, each labelled export-equivalent with no file claim
- Size band (advisory): 70 to 150 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question rendered as its own block under an export-equivalent `task` lane `-clarification` label with the `HVR self-scan:` line and renders no task, and Turn 2 renders one task block under an export-equivalent `task` label with the `HVR self-scan:` line and no file claim, carrying its H1, `### About` and `### Requirements` with checklisted requirement groups, the stay limits and the five copy strings exactly as the notes give them, and every Turn 2 fact. FAIL if Turn 1 renders the task, a reply prints `Path:`, `Saved:` or `Verified:` or claims a file, the task hard-codes the limits in the apps, applies the 365-day limit to check-out, changes a number or a copy string, adds a tracking event, a search-service change or a flexible-dates requirement that no turn or attachment asks for without naming it as an addition, drops a Turn 2 fact, invents a link for the frame or leaves a template slot in the block
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.` | Read both attachments, ask the task context question once, render it as a clarification block with an export-equivalent label and the `HVR self-scan:` line and wait. Claim no file and render no task | Task Mode and the date picker stay limits stay selected, no task block exists | Turn 1 reply, rendered clarification block, its label and the no-file statement |
| 2 | `One FE task for iOS, Android and web together, no parent, and the Search squad takes it into the 8.13.0 train. Leave search-service as it is, its own 30-night check stays as the backstop. QA signs it off on all three platforms in en-GB and en-US.` | Render the task block from the notes and the answer, then its export-equivalent label and the `HVR self-scan:` line, with no file claim | The notes' limits and copy and every Turn 2 fact survive into Requirements | Turn 2 reply, rendered task block, its label and the no-file statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.`

### Commands

1. `sandbox: stage context/roamstay-context.md and context/roamstay-date-picker-design-notes.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `operator: confirm one context question block and no task block -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered task block -> operator: grade the sections, requirement groups, limits, copy strings, Turn 2 facts, labels and the no-file boundary`

### Expected

Step 1 fixes the panel baseline with both attachments staged. Step 2 returns one context question as its own block with a `-clarification` label. Step 3 proves the wait state and state retention. Step 4 finds an H1, `### About`, `### Requirements` and numbered groups with `**Checklist**` items carrying `30 nights`, `365 days`, `14 nights`, `Select check-in date`, `Select check-out date`, `Show prices`, `Stays can be up to 30 nights` and `This property has a 3-night minimum`, the limits read from config, check-out free of the 365-day rule, and the Turn 2 scope, team, train, search-service boundary and QA locales, under an export-equivalent label.

### Evidence

Capture both replies, both rendered blocks and which form each took, the two export-equivalent labels, the self-scan lines, the no-file statements and block excerpts showing the limits, the five copy strings, the platform notes and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question block under a task-lane clarification label, no early task block, then one task block with the required sections, checklisted groups, every limit and copy string from the notes and every fact from the answer, and no file claim
- **Fail**: The runtime renders the task before Turn 2, prints `Path:` or `Saved:`, claims a file, hard-codes or stretches a limit, paraphrases a copy string, adds tracking or a search-service change unasked, drops a Turn 2 fact, invents a frame link or leaves a template slot

### Failure triage

1. Check the explicit-command question rule at `Custom Instructions.md` line 108 and `Product Owner - System - Interactive Mode` line 101, then the clarification label at `Custom Instructions.md` line 228
2. Compare the block with the Canonical Task template at `Product Owner - Assets - Task Templates` line 19 and the requirement grammar at `Product Owner - Templates - Task Mode` lines 82 to 92
3. Diff every limit and copy string against `roamstay-date-picker-design-notes.md` lines 15 to 62 and every scope fact against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-002 | Design notes FE task | Verify design notes and one answer become a faithful front end task block | `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Confirm wait and submit Turn 2 -> 4. Inspect the task block | Step 1: baseline known. Step 2: one question block with a clarification label. Step 3: state retained. Step 4: required sections, checklisted groups, limits, copy and Turn 2 facts intact | Both replies, rendered blocks, labels, no-file statements and artifact excerpts | PASS if routing, the context gate and a faithful task block all match with no file claim. FAIL otherwise | 1. Check the `$task` rule. 2. Check the task template. 3. Diff limits, copy and Turn 2 facts |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the explicit-command question rule, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.305.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.305.md) | Project task workflow, required sections, requirement grammar and the plain-text reference rule |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Project Canonical Task scaffold |
| [`Product Owner - System - Interactive Mode - v0.406.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.406.md) | Direct `$task` row and clarification delivery |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Task Format question wording |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: surfaces, squads, the `SRCH` code, locales and the title convention |
| [`roamstay-date-picker-design-notes.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md) | Attachment: stay limits, picker states, copy keys, edge cases, platforms and exclusions |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/design-notes-fe-task.md`

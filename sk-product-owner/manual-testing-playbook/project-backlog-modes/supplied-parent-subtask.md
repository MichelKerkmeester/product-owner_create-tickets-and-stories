---
title: "PTK-005 -- Supplied parent subtask"
description: "Validates that a subtask command against a supplied Loomlist parent task renders one context question block, then an Android recurring to-dos subtask block in a Claude Project that names its parent in plain text, keeps the parent's shared rules and holds only Android client work."
version: 1.0.0.1
---

# PTK-005 -- Supplied parent subtask

This scenario validates the `$task --subtask` path from a finished parent task to a rendered Android subtask block, through one clarification turn.

---

## 1. OVERVIEW

A Loomlist engineer hands over the finished recurring to-dos parent and asks for its Android subtask. `$task --subtask` is checked before `$task` and routes to Task Mode with child-task scope, which still asks its context question before drafting, so Turn 1 renders a task-lane clarification block. Turn 2 answers with what the parent does not hold: it is the Android entry from the parent's list, it covers phones and tablets, Oskar's team takes it into the 5.4.0 release, and the back end builds the engine in parallel, so the app shows the next due date the back end returns and never works it out on the device.

The parent carries the shared rules the subtask builds on Android: Repeat on the detail sheet with the hint `Add a due date to repeat`, the options `Daily`, `Weekdays`, `Weekly`, `Monthly` and `Custom` with N from `1 to 99`, `Ends` with `Never`, `On date` and `After` from 1 to `365`, one occurrence at a time with assignee and reminder carried over at the same local time, `Skip this one` in the to-do menu, the `500` limit sheet, the `owner's time zone`, Plus and Team only with a Plus badge on Free, the `recurring_todos` flag, the tracking events `todo_repeat_set` and `todo_occurrence_skipped`, and three design frames. The context adds the Android fact that turns the carried-over reminder into work for this subtask: on iOS and Android a reminder is a local notification the app schedules from the UTC time reminders-service hands over.

A subtask that reads like the team's own takes its title from the parent's own list, `FE - Android - TODO - Recurring to-dos`, names its parent `FS - TODO - Recurring to-dos` in a `**Parent task**` block as plain text, names the three frames as plain-text references and groups the Android work under numbered requirement groups, each with a `**Checklist**`. The corpus closes such tasks with a Resolution Checklist that checks Android phones and tablets and a QA sign-off. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

A subtask that loses its parent, pulls iOS or engine work into the Android ticket or has the app work out due dates the back end owns splits one feature into four behaviors. The Project's block is the ticket a human pastes under the parent, so it has to name that parent itself.

---

## 2. SCENARIO CONTRACT

- Objective: Verify subtask routing, the single context question and an Android subtask block that names its supplied parent, keeps the parent's shared rules and holds only Android client work
- Real user request: `Oskar's team needs its Android ticket under the recurring to-dos parent.`
- Prompt: `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-recurring-todos-parent-task.md](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-parent-task.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 in the same conversation and inspect the rendered subtask block
- Expected signals: `$task --subtask` routes to the task context question with child-task scope (`Product Owner - System - Interactive Mode` line 122), and an explicit command still asks once and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Task Mode` line 30). The question renders as its own block, then `Export-equivalent path: export/[NNN] - task-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line, with no file claim and no subtask (`Product Owner - System - Interactive Mode` lines 62 and 70, root section 5, Clarification turns). A question that asks for a fact the parent already states is recorded only (root section 5, Ticket realism). Turn 2 renders the subtask as the Deliverable Block before any commentary, fenced where there is no Canvas panel (`Custom Instructions.md` line 85), then `Export-equivalent path: export/[NNN] - task-[description].md` (line 223) and the `HVR self-scan:` line (line 89), with no claim that a file was written (line 101). The block follows the Subtask template (`Product Owner - Assets - Task Templates` line 195): H1, `### About` and `### Requirements` (`Product Owner - Templates - Task Mode` lines 52 to 58), an area heading and numbered groups each with a `**Checklist**` of `- [ ]` items (lines 82 to 92). It names the parent `FS - TODO - Recurring to-dos` as backticked plain text with no invented link (`Product Owner - Templates - Task Mode` line 111, `Product Owner - Assets - Task Templates` line 140), names the three frames as plain text (`loomlist-recurring-todos-parent-task.md` lines 19 to 21) and carries the parent's shared rules verbatim for the Android client (lines 59 to 109). The carried-over reminder becomes a local notification Android schedules from the UTC time reminders-service hands over (`loomlist-context.md` line 77). Every Turn 2 fact survives: the Android entry, phones and tablets, Oskar's team, the 5.4.0 release, and the next due date taken from the back end and never worked out on the device
- Desired user-visible outcome: One task-lane question block, then an Android subtask block under its named parent that an Android engineer can build and test from, each labelled export-equivalent with no file claim
- Size band (advisory): 60 to 130 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question rendered as its own block under an export-equivalent `task` lane `-clarification` label with the `HVR self-scan:` line and renders no subtask, and Turn 2 renders one subtask block under an export-equivalent `task` label with the `HVR self-scan:` line and no file claim, carrying its H1, `### About` and `### Requirements` with checklisted requirement groups, the parent named as `FS - TODO - Recurring to-dos`, the shared rules with `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`, `Never`, `On date`, `After`, `365`, `Skip this one`, `500`, `recurring_todos` and the `owner's time zone` as the parent gives them, Android as the only client in scope, and every Turn 2 fact. FAIL if Turn 1 renders the subtask, a reply prints `Path:`, `Saved:` or `Verified:` or claims a file, the subtask drops its parent or links it to an invented URL, takes in iOS, web, Desktop or engine work, has the app work out the next due date, changes an option, range, limit, sheet copy or plan rule, adds an Android requirement no turn or attachment states, such as a widget or a notification action, without the reply naming it as an addition, drops a Turn 2 fact or leaves a template slot in the block
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.` | Read both attachments, ask the task context question once, render it as a clarification block with an export-equivalent label and the `HVR self-scan:` line and wait. Claim no file and render no subtask | Task Mode with child-task scope, the Android subtask and its parent stay selected, no subtask block exists | Turn 1 reply, rendered clarification block, its label and the no-file statement |
| 2 | `It is the Android one from that list, phones and tablets, and Oskar's team takes it into the 5.4.0 release. BE builds the engine in parallel, so the app shows the next due date BE returns and never works it out on the device.` | Render the Android subtask block from the parent, the context and the answer, then its export-equivalent label and the `HVR self-scan:` line, with no file claim | The named parent, the shared rules, Android-only scope and every Turn 2 fact survive | Turn 2 reply, rendered subtask block, its label and the no-file statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.`

### Commands

1. `sandbox: stage context/loomlist-context.md and context/loomlist-recurring-todos-parent-task.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `operator: confirm one context question block and no subtask block -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered subtask block -> operator: grade the sections, the named parent, the Android scope, the shared rules, the reminder handling, the Turn 2 facts, the label and the no-file boundary`

### Expected

Step 1 fixes the panel baseline with both attachments staged. Step 2 returns one context question as its own block with a `-clarification` label. Step 3 proves the wait state and state retention. Step 4 finds an H1, `### About`, the parent named as `FS - TODO - Recurring to-dos` in plain text, `### Requirements` with checklisted groups for Repeat and its options, Ends, occurrences and Skip this one, the `500` limit sheet, the owner's time zone, the Plus gate, the flag and the two tracking events, the carried-over reminder scheduled as a local notification, the next due date taken from the back end, and the Turn 2 team, release and device scope, under an export-equivalent label.

### Evidence

Capture both replies, both rendered blocks and which form each took, the two export-equivalent labels, the self-scan lines, the no-file statements and subtask excerpts showing the parent block, each requirement group, the shared rule values and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question block under a task-lane clarification label, no early subtask block, then one subtask block with the required sections, its parent named in plain text, the parent's shared rules intact, Android as the only client, every Turn 2 fact and no file claim
- **Fail**: The runtime renders the subtask before Turn 2, prints `Path:` or `Saved:`, claims a file, drops or links the parent to an invented URL, pulls in another platform or the engine, has the app compute due dates, changes a shared rule, adds an unnamed Android requirement, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the `$task --subtask` route at `Product Owner - System - Interactive Mode` line 122 and the explicit-command question rule at `Custom Instructions.md` line 108, then the clarification label at line 228
2. Compare the block with the Subtask template at `Product Owner - Assets - Task Templates` line 195 and the named-but-unlinked rule at `Product Owner - Templates - Task Mode` line 111
3. Diff every shared rule against `loomlist-recurring-todos-parent-task.md` lines 59 to 109, the reminder handling against `loomlist-context.md` line 77 and the scope against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-005 | Supplied parent subtask | Verify a supplied parent and one answer become a faithful Android subtask block | `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Confirm wait and submit Turn 2 -> 4. Inspect the subtask block | Step 1: baseline known. Step 2: one question block with a clarification label. Step 3: state retained. Step 4: required sections, named parent, shared rules, Android-only scope and Turn 2 facts intact | Both replies, rendered blocks, labels, no-file statements and artifact excerpts | PASS if routing, the context gate and a faithful Android subtask block all match with no file claim. FAIL otherwise | 1. Check the subtask route. 2. Check the Subtask template and the parent block. 3. Diff the rules and the scope |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the explicit-command question rule, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.305.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.305.md) | Project task workflow, subtask type, required sections and the named-but-unlinked rule |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Project Subtask scaffold and the Notes For Use |
| [`Product Owner - System - Interactive Mode - v0.406.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.406.md) | The `$task --subtask` state route and clarification delivery |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: platforms, reminder delivery on Android, the owner's time zone and the title convention |
| [`loomlist-recurring-todos-parent-task.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-parent-task.md) | Attachment: the supplied parent, its four subtask titles, shared rules, frames, flag and tracking |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-005
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/supplied-parent-subtask.md`

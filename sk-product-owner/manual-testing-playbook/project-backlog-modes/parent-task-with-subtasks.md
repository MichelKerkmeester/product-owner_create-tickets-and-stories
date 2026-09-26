---
title: "PTK-004 -- Parent task with subtasks"
description: "Validates that a task command for a Loomlist parent task renders one context question block, then one parent task block in a Claude Project that lists its iOS, Android, web and back end subtasks by title and states the recurring to-do rules from the PM brief once."
version: 1.0.0.1
---

# PTK-004 -- Parent task with subtasks

This scenario validates the explicit `$task` path from a PM brief to a rendered parent task block that coordinates four platform subtasks, through one clarification turn.

---

## 1. OVERVIEW

A Loomlist PM asks for the parent task behind recurring to-dos, built from Ines's brief, with subtasks for iOS, Android, web and back end. `$task` fixes Task Mode, which still asks its context question before drafting, so Turn 1 renders a task-lane clarification block. Turn 2 settles what the brief cannot: only the parent is written now, the platform leads write their own subtasks from it, the four are listed by title the way the board names them, the shared rules are stated once in the parent, iOS and Android aim for the 5.4.0 release, and web and back end ship dark before that.

The brief carries the rules the parent states once: Repeat on the detail sheet with the hint `Add a due date to repeat`, the options `Daily`, `Weekdays`, `Weekly`, `Monthly` and `Custom` with N from `1 to 99`, the Monthly day rule, `Ends` with `Never` as the default, `On date` and `After` from 1 to `365`, one occurrence at a time with assignee and reminder carried over, `Skip this one` counting toward an After limit, the `500` limit and its sheet copy, the `owner's time zone`, `Plus` and Team only, the `recurring_todos` flag, the `10%` success measure, two tracking events, three design frames, the out-of-scope list and one question still open. It also says Desktop gets the feature through the web client and needs no subtask of its own.

A parent that reads like the team's own carries the `FS - TODO - Recurring to-dos` shape the context's title rule gives a parent spanning platforms, an About with the demand the brief cites, the three frames as plain-text references, a Requirements list with one numbered entry per subtask named `FE - iOS - TODO - ...`, `FE - Android - TODO - ...`, `FE - Web - TODO - ...` and `BE - TODO - ...`, and a shared rules block. No routed template asks for a title code, so a parent or subtask title without one is recorded, never graded (root section 5, Ticket realism).

### Why this matters

A parent task is what four teams read before they split off their own work, and the Project's block is the copy that reaches the board. A block that adds a Desktop subtask, puts Repeat on Free or links subtasks that do not exist yet sends every team building from a different picture.

---

## 2. SCENARIO CONTRACT

- Objective: Verify task routing, the single context question and one parent task block that lists four subtasks by title and states the brief's shared rules once
- Real user request: `I need the parent ticket for recurring to-dos so the platform leads can split off their own work.`
- Prompt: `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-recurring-todos-pm-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-pm-brief.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 in the same conversation and inspect the rendered parent task block
- Expected signals: `$task` still asks its context question once and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Task Mode` line 30, `Product Owner - System - Interactive Mode` line 101). The question renders as its own block, then `Export-equivalent path: export/[NNN] - task-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line, with no file claim and no task (`Product Owner - System - Interactive Mode` lines 62 and 70, root section 5, Clarification turns). A question that asks for a fact the brief already states is recorded only (root section 5, Ticket realism). Turn 2 renders one parent task as the Deliverable Block before any commentary, fenced where there is no Canvas panel (`Custom Instructions.md` line 85), and no subtask blocks, then `Export-equivalent path: export/[NNN] - task-[description].md` (line 223) and the `HVR self-scan:` line (line 89), with no claim that a file was written (line 101). The block follows the Parent Task template (`Product Owner - Assets - Task Templates` line 146): H1, `### About` and `### Requirements` (`Product Owner - Templates - Task Mode` lines 52 to 58) with one numbered entry per subtask for iOS, Android, web and back end, each named as backticked plain text with no invented link (`Product Owner - Templates - Task Mode` line 111, `Product Owner - Assets - Task Templates` line 140). It states the shared rules once with the brief's values verbatim (`loomlist-recurring-todos-pm-brief.md` lines 12 to 47), names the three frames as plain text (line 58), keeps the tracking events and the out-of-scope list (lines 62 to 69), leaves the activity-history question open (line 73) and gives Desktop no subtask (line 55). Every Turn 2 fact survives: only the parent, subtasks written by the platform leads, the four listed by board-style title, the shared rules stated once, iOS and Android on 5.4.0, and web and back end shipping dark first
- Desired user-visible outcome: One task-lane question block, then one parent task block that lists four subtasks by title and states the recurring to-do rules once, each labelled export-equivalent with no file claim
- Size band (advisory): 60 to 130 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question rendered as its own block under an export-equivalent `task` lane `-clarification` label with the `HVR self-scan:` line and renders no task, and Turn 2 renders one parent task block under an export-equivalent `task` label with the `HVR self-scan:` line and no file claim, carrying its H1, `### About` and `### Requirements` with one numbered entry each for iOS, Android, web and back end named in plain text, the shared rules with `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`, `Never`, `On date`, `After`, `365`, `Skip this one`, `500`, `recurring_todos`, `Plus` and the `owner's time zone` as the brief gives them, and every Turn 2 fact. FAIL if Turn 1 renders the task, a reply prints `Path:`, `Saved:` or `Verified:` or claims a file, Turn 2 renders subtask blocks as well, the parent adds a Desktop or Support console subtask, gives a subtask an invented link or a `(url)` slot, offers Repeat on Free, changes a range, the limit or the sheet copy, adds repeating from the check-off date or a per-weekday time, presents the activity-history question as decided, drops a Turn 2 fact or leaves a template slot in the block
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.` | Read both attachments, ask the task context question once, render it as a clarification block with an export-equivalent label and the `HVR self-scan:` line and wait. Claim no file and render no task | Task Mode, the parent task and the four platforms stay selected, no task block exists | Turn 1 reply, rendered clarification block, its label and the no-file statement |
| 2 | `Only the parent for now, the platform leads write their own subtasks from it, so list the four by title the way our board names them. State the shared rules once in the parent so the subtasks can point at it. iOS and Android aim for the 5.4.0 release, and web and BE ship dark before that.` | Render one parent task block from the brief and the answer and no subtask blocks, then its export-equivalent label and the `HVR self-scan:` line, with no file claim | Four subtasks listed by title, the shared rules stated once and every Turn 2 fact survive | Turn 2 reply, rendered parent block, its label and the no-file statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.`

### Commands

1. `sandbox: stage context/loomlist-context.md and context/loomlist-recurring-todos-pm-brief.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `operator: confirm one context question block and no task block -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered blocks -> operator: confirm one parent block and no subtask blocks, then grade the sections, the four subtask entries, the shared rules, the Turn 2 facts, the label and the no-file boundary`

### Expected

Step 1 fixes the panel baseline with both attachments staged. Step 2 returns one context question as its own block with a `-clarification` label. Step 3 proves the wait state and state retention. Step 4 finds exactly one parent block with an H1, `### About`, `### Requirements` holding four numbered subtask entries named in plain text for iOS, Android, web and back end, a shared rules block carrying the brief's options, ranges, limit, time zone, plan, flag and tracking rules verbatim, the three frames, the out-of-scope list, the open activity-history question left open and the Turn 2 release plan, under an export-equivalent label.

### Evidence

Capture both replies, the rendered blocks and which form each took, the two export-equivalent labels, the self-scan lines, the no-file statements and parent excerpts showing each subtask entry, the shared rules, the frames and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question block under a task-lane clarification label, no early task block, then exactly one parent block with the required sections, four subtasks listed by plain-text title, the brief's shared rules intact, every Turn 2 fact and no file claim
- **Fail**: The runtime renders a task before Turn 2, prints `Path:` or `Saved:`, claims a file, renders subtask blocks, adds a Desktop or Support console subtask, invents a subtask link, changes a rule or value from the brief, decides the open question, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the explicit-command question rule at `Custom Instructions.md` line 108 and `Product Owner - System - Interactive Mode` line 101, then the clarification label at `Custom Instructions.md` line 228
2. Compare the block with the Parent Task template at `Product Owner - Assets - Task Templates` line 146 and the named-but-unlinked rule at `Product Owner - Templates - Task Mode` line 111
3. Diff every shared rule against `loomlist-recurring-todos-pm-brief.md` lines 12 to 73 and the subtask set against Turn 2 and brief line 55

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-004 | Parent task with subtasks | Verify a PM brief and one answer become one parent task block listing four subtasks | `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Confirm wait and submit Turn 2 -> 4. Inspect the parent block | Step 1: baseline known. Step 2: one question block with a clarification label. Step 3: state retained. Step 4: one parent block, four plain-text subtask entries, shared rules and Turn 2 facts intact | Both replies, rendered blocks, labels, no-file statements and artifact excerpts | PASS if routing, the context gate and a faithful parent block all match with no file claim. FAIL otherwise | 1. Check the `$task` rule. 2. Check the Parent Task template. 3. Diff the rules and the subtask set |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the explicit-command question rule, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.305.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.305.md) | Project task workflow, parent task type, required sections and the named-but-unlinked rule |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Project Parent Task scaffold and the Notes For Use |
| [`Product Owner - System - Interactive Mode - v0.406.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.406.md) | Direct `$task` row and clarification delivery |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: surfaces, plans, the `TODO` code, the owner's time zone and the title convention |
| [`loomlist-recurring-todos-pm-brief.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-pm-brief.md) | Attachment: recurrence rules, limit, plans, flag, tracking, frames, the build split and the open question |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-004
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/parent-task-with-subtasks.md`

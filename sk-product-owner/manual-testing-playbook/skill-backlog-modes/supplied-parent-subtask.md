---
title: "STK-005 -- Supplied parent subtask"
description: "Validates that a subtask command against a supplied Loomlist parent task asks one context question, then saves the Android recurring to-dos subtask that names its parent in plain text, keeps the parent's shared rules and holds only Android client work."
version: 1.1.0.0
---

# STK-005 -- Supplied parent subtask

This scenario validates the `$task --subtask` path from a finished parent task to a saved Android subtask, through one clarification turn.

---

## 1. OVERVIEW

A Loomlist engineer hands over the finished recurring to-dos parent and asks for its Android subtask. `$task --subtask` is checked before `$task` and routes to Task Mode with child-task scope, which still asks its context question before drafting, so Turn 1 saves a task-lane clarification. Turn 2 answers with what the parent does not hold: it is the Android entry from the parent's list, it covers phones and tablets, Oskar's team takes it into the 5.4.0 release, and the back end builds the engine in parallel, so the app shows the next due date the back end returns and never works it out on the device.

The parent carries the shared rules the subtask builds on Android: Repeat on the detail sheet with the hint `Add a due date to repeat`, the options `Daily`, `Weekdays`, `Weekly`, `Monthly` and `Custom` with N from `1 to 99`, `Ends` with `Never`, `On date` and `After` from 1 to `365`, one occurrence at a time with assignee and reminder carried over at the same local time, `Skip this one` in the to-do menu, the `500` limit sheet, the `owner's time zone`, Plus and Team only with a Plus badge on Free, the `recurring_todos` flag, the tracking events `todo_repeat_set` and `todo_occurrence_skipped`, and three design frames. The context adds the Android fact that turns the carried-over reminder into work for this subtask: on iOS and Android a reminder is a local notification the app schedules from the UTC time reminders-service hands over.

A subtask that reads like the team's own takes its title from the parent's own list, `FE - Android - TODO - Recurring to-dos`, names its parent `FS - TODO - Recurring to-dos` in a `**Parent task**` block as plain text, names the three frames as plain-text references and groups the Android work under numbered requirement groups, each with a `**Checklist**`. The corpus closes such tasks with a Resolution Checklist that checks Android phones and tablets and a QA sign-off. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

A subtask that loses its parent, pulls iOS or engine work into the Android ticket or has the app work out due dates the back end owns splits one feature into four behaviors. The supplied parent exists so each subtask builds the same rules.

---

## 2. SCENARIO CONTRACT

- Objective: Verify subtask routing, the single context question and an Android subtask that names its supplied parent, keeps the parent's shared rules and holds only Android client work
- Real user request: `Oskar's team needs its Android ticket under the recurring to-dos parent.`
- Prompt: `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-recurring-todos-parent-task.md](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-parent-task.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, answer in Turn 2 in the same session and inspect the subtask export
- Expected signals: `$task --subtask` is checked before `$task` and selects child-task scope (`AGENTS.md` lines 191 and 205), and Task Mode still asks its context question once and waits (`AGENTS.md` line 287, `references/task-mode.md` line 50, `references/interactive-mode.md` line 145). The question is saved as `export/[###] - task-[description]-clarification.md`, holding the question and nothing else, read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` line 82, root section 5, Clarification turns). A question that asks for a fact the parent already states is recorded only (root section 5, Ticket realism). Turn 2 saves the subtask under the `task` word as `export/[###] - task-[description].md` on the next number (`AGENTS.md` line 96), reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line (`AGENTS.md` lines 46 and 47). The subtask follows the Subtask template (`assets/task-templates.md` line 214): H1, `## About` and `### Requirements` (`references/task-mode.md` lines 72 to 78), an area heading and numbered groups each with a `**Checklist**` of `- []` items (lines 102 to 112). It names the parent `FS - TODO - Recurring to-dos` as backticked plain text with no invented link (`references/task-mode.md` line 133, `assets/task-templates.md` line 159), names the three frames as plain text (`loomlist-recurring-todos-parent-task.md` lines 19 to 21) and carries the parent's shared rules verbatim for the Android client (lines 59 to 109). The carried-over reminder becomes a local notification Android schedules from the UTC time reminders-service hands over (`loomlist-context.md` line 77). Every Turn 2 fact survives: the Android entry, phones and tablets, Oskar's team, the 5.4.0 release, and the next due date taken from the back end and never worked out on the device
- Desired user-visible outcome: One saved task-lane question, then a saved Android subtask under its named parent that an Android engineer can build and test from
- Size band (advisory): 60 to 130 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, saves it under a `task` lane `-clarification` name reported with its path, the `Verified:` line and the `HVR self-scan:` line and drafts no task, and Turn 2 saves one `task` export on the next number, read back and reported the same way, carrying its H1, `## About` and `### Requirements` with checklisted requirement groups, the parent named as `FS - TODO - Recurring to-dos`, the shared rules with `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `99`, `Never`, `On date`, `After`, `365`, `Skip this one`, `500`, `recurring_todos` and the `owner's time zone` as the parent gives them, Android as the only client in scope, and every Turn 2 fact. FAIL if Turn 1 drafts the task, the subtask drops its parent or links it to an invented URL, takes in iOS, web, Desktop or engine work, has the app work out the next due date, changes an option, range, limit, sheet copy or plan rule, adds an Android requirement no turn or attachment states, such as a widget or a notification action, without the reply naming it as an addition, drops a Turn 2 fact or leaves a template slot in the body
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.` | Read both attachments, ask the task context question once, save it as a task-lane clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Draft no subtask | Task Mode with child-task scope, the Android subtask and its parent stay selected, one new `-clarification` file, `context/` unchanged | Turn 1 reply, clarification file, read-back result and side-effect ledger |
| 2 | `It is the Android one from that list, phones and tablets, and Oskar's team takes it into the 5.4.0 release. BE builds the engine in parallel, so the app shows the next due date BE returns and never works it out on the device.` | Build the Android subtask from the parent, the context and the answer, save it on the next number, read it back and reply path first with the `Verified:` line and the `HVR self-scan:` line | The named parent, the shared rules, Android-only scope and every Turn 2 fact survive, the clarification file stays untouched | Turn 2 reply, subtask export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.`

### Commands

1. `sandbox: stage context/loomlist-context.md and context/loomlist-recurring-todos-parent-task.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new subtask export -> operator: grade the sections, the named parent, the Android scope, the shared rules, the reminder handling and the Turn 2 facts against the parent and the answer`

### Expected

Step 1 fixes the baseline with both attachments staged. Step 2 returns one context question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds an H1, `## About`, the parent named as `FS - TODO - Recurring to-dos` in plain text, `### Requirements` with checklisted groups for Repeat and its options, Ends, occurrences and Skip this one, the `500` limit sheet, the owner's time zone, the Plus gate, the flag and the two tracking events, the carried-over reminder scheduled as a local notification, the next due date taken from the back end, and the Turn 2 team, release and device scope.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the self-scan lines and subtask excerpts showing the parent block, each requirement group, the shared rule values and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question saved as a task-lane clarification, no early draft, then one readable subtask export with the required sections, its parent named in plain text, the parent's shared rules intact, Android as the only client and every Turn 2 fact
- **Fail**: The runtime drafts before Turn 2, drops or links the parent to an invented URL, pulls in another platform or the engine, has the app compute due dates, changes a shared rule, adds an unnamed Android requirement, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the `$task --subtask` route at `AGENTS.md` lines 191 and 205 and `references/interactive-mode.md` line 145, then the clarification export at `AGENTS.md` line 82
2. Compare the subtask with the Subtask template at `assets/task-templates.md` line 214 and the named-but-unlinked rule at `references/task-mode.md` line 133
3. Diff every shared rule against `loomlist-recurring-todos-parent-task.md` lines 59 to 109, the reminder handling against `loomlist-context.md` line 77 and the scope against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-005 | Supplied parent subtask | Verify a supplied parent and one answer become a faithful Android subtask | `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the subtask export | Step 1: baseline known. Step 2: one question and one clarification. Step 3: state retained. Step 4: required sections, named parent, shared rules, Android-only scope and Turn 2 facts intact | Both replies, ledger, clarification and subtask export paths, read-back lines and artifact excerpts | PASS if routing, the context gate and a faithful Android subtask all match. FAIL otherwise | 1. Check the subtask route. 2. Check the Subtask template and the parent block. 3. Diff the rules and the scope |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | The `$task --subtask` command, its check order, the explicit-command question rule, the export names and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Export names and the HVR self-scan line |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, subtask type, required sections and the named-but-unlinked rule |
| [`task-templates.md`](../../assets/task-templates.md) | Subtask scaffold and the Notes For Use |
| [`interactive-mode.md`](../../references/interactive-mode.md) | The `$task --subtask` state route and the clarification export |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: platforms, reminder delivery on Android, the owner's time zone and the title convention |
| [`loomlist-recurring-todos-parent-task.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-parent-task.md) | Attachment: the supplied parent, its four subtask titles, shared rules, frames, flag and tracking |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-005
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/supplied-parent-subtask.md`

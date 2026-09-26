---
title: "STK-004 -- Parent task with subtasks"
description: "Validates that a task command for a Loomlist parent task asks one context question, then saves one parent task that lists its iOS, Android, web and back end subtasks by title and states the recurring to-do rules from the PM brief once."
version: 1.0.0.0
---

# STK-004 -- Parent task with subtasks

This scenario validates the explicit `$task` path from a PM brief to a saved parent task that coordinates four platform subtasks, through one clarification turn.

---

## 1. OVERVIEW

A Loomlist PM asks for the parent task behind recurring to-dos, built from Ines's brief, with subtasks for iOS, Android, web and back end. `$task` fixes Task Mode, which still asks its context question before drafting, so Turn 1 saves a task-lane clarification. Turn 2 settles what the brief cannot: only the parent is written now, the platform leads write their own subtasks from it, the four are listed by title the way the board names them, the shared rules are stated once in the parent, iOS and Android aim for the 5.4.0 release, and web and back end ship dark before that.

The brief carries the rules the parent states once: Repeat on the detail sheet with the hint `Add a due date to repeat`, the options `Daily`, `Weekdays`, `Weekly`, `Monthly` and `Custom` with N from `1 to 99`, the Monthly day rule, `Ends` with `Never` as the default, `On date` and `After` from 1 to `365`, one occurrence at a time with assignee and reminder carried over, `Skip this one` counting toward an After limit, the `500` limit and its sheet copy, the `owner's time zone`, `Plus` and Team only, the `recurring_todos` flag, the `10%` success measure, two tracking events, three design frames, the out-of-scope list and one question still open. It also says Desktop gets the feature through the web client and needs no subtask of its own.

A parent that reads like the team's own carries the `FS - TODO - Recurring to-dos` shape the context's title rule gives a parent spanning platforms, an About with the demand the brief cites, the three frames as plain-text references, a Requirements list with one numbered entry per subtask named `FE - iOS - TODO - ...`, `FE - Android - TODO - ...`, `FE - Web - TODO - ...` and `BE - TODO - ...`, and a shared rules block. No routed template asks for a title code, so a parent or subtask title without one is recorded, never graded (root section 5, Ticket realism).

### Why this matters

A parent task is what four teams read before they split off their own work. A parent that adds a Desktop subtask, puts Repeat on Free or links subtasks that do not exist yet sends every team building from a different picture.

---

## 2. SCENARIO CONTRACT

- Objective: Verify task routing, the single context question and one parent task that lists four subtasks by title and states the brief's shared rules once
- Real user request: `I need the parent ticket for recurring to-dos so the platform leads can split off their own work.`
- Prompt: `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-recurring-todos-pm-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-pm-brief.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, answer in Turn 2 in the same session and inspect the parent task export
- Expected signals: `$task` routes to Task Mode by command (`AGENTS.md` line 190) and still asks its context question once and waits (`AGENTS.md` line 287, `references/task-mode.md` line 50, `references/interactive-mode.md` line 124). The question is saved as `export/[###] - task-[description]-clarification.md`, holding the question and nothing else, read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` line 82, root section 5, Clarification turns). A question that asks for a fact the brief already states is recorded only (root section 5, Ticket realism). Turn 2 saves one parent task as `export/[###] - task-[description].md` on the next number and no subtask files, reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line (`AGENTS.md` lines 46 and 47). The parent follows the Parent Task template (`assets/task-templates.md` line 165): H1, `## About` and `### Requirements` (`references/task-mode.md` lines 72 to 78) with one numbered entry per subtask for iOS, Android, web and back end, each named as backticked plain text with no invented link (`references/task-mode.md` line 133, `assets/task-templates.md` line 159). It states the shared rules once with the brief's values verbatim (`loomlist-recurring-todos-pm-brief.md` lines 12 to 47), names the three frames as plain text (line 58), keeps the tracking events and the out-of-scope list (lines 62 to 69), leaves the activity-history question open (line 73) and gives Desktop no subtask (line 55). Every Turn 2 fact survives: only the parent, subtasks written by the platform leads, the four listed by board-style title, the shared rules stated once, iOS and Android on 5.4.0, and web and back end shipping dark first
- Desired user-visible outcome: One saved task-lane question, then one saved parent task that lists four subtasks by title and states the recurring to-do rules once
- Size band (advisory): 60 to 130 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, saves it under a `task` lane `-clarification` name reported with its path, the `Verified:` line and the `HVR self-scan:` line and drafts no task, and Turn 2 saves one parent `task` export on the next number, read back and reported the same way, carrying its H1, `## About` and `### Requirements` with one numbered entry each for iOS, Android, web and back end named in plain text, the shared rules with `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`, `Never`, `On date`, `After`, `365`, `Skip this one`, `500`, `recurring_todos`, `Plus` and the `owner's time zone` as the brief gives them, and every Turn 2 fact. FAIL if Turn 1 drafts the task, Turn 2 saves subtask files as well, the parent adds a Desktop or Support console subtask, gives a subtask an invented link or a `(url)` slot, offers Repeat on Free, changes a range, the limit or the sheet copy, adds repeating from the check-off date or a per-weekday time, presents the activity-history question as decided, drops a Turn 2 fact or leaves a template slot in the body
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.` | Read both attachments, ask the task context question once, save it as a task-lane clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Draft no task | Task Mode, the parent task and the four platforms stay selected, one new `-clarification` file, `context/` unchanged | Turn 1 reply, clarification file, read-back result and side-effect ledger |
| 2 | `Only the parent for now, the platform leads write their own subtasks from it, so list the four by title the way our board names them. State the shared rules once in the parent so the subtasks can point at it. iOS and Android aim for the 5.4.0 release, and web and BE ship dark before that.` | Build one parent task from the brief and the answer, save it on the next number with no subtask files, read it back and reply path first with the `Verified:` line and the `HVR self-scan:` line | Four subtasks listed by title, the shared rules stated once and every Turn 2 fact survive, the clarification file stays untouched | Turn 2 reply, parent task export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.`

### Commands

1. `sandbox: stage context/loomlist-context.md and context/loomlist-recurring-todos-pm-brief.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: list the export folder -> operator: confirm one parent task and no subtask files, then grade the sections, the four subtask entries, the shared rules and the Turn 2 facts against the brief and the answer`

### Expected

Step 1 fixes the baseline with both attachments staged. Step 2 returns one context question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds exactly one new task file with an H1, `## About`, `### Requirements` holding four numbered subtask entries named in plain text for iOS, Android, web and back end, a shared rules block carrying the brief's options, ranges, limit, time zone, plan, flag and tracking rules verbatim, the three frames, the out-of-scope list, the open activity-history question left open and the Turn 2 release plan.

### Evidence

Capture both replies, the side-effect ledger and folder listing, both export paths and read-back lines, the self-scan lines and parent excerpts showing each subtask entry, the shared rules, the frames and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question saved as a task-lane clarification, no early draft, then exactly one readable parent task with the required sections, four subtasks listed by plain-text title, the brief's shared rules intact and every Turn 2 fact
- **Fail**: The runtime drafts before Turn 2, writes subtask files, adds a Desktop or Support console subtask, invents a subtask link, changes a rule or value from the brief, decides the open question, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the direct `$task` rule at `AGENTS.md` line 287 and `references/interactive-mode.md` line 124, then the clarification export at `AGENTS.md` line 82
2. Compare the parent with the Parent Task template at `assets/task-templates.md` line 165 and the named-but-unlinked rule at `references/task-mode.md` line 133
3. Diff every shared rule against `loomlist-recurring-todos-pm-brief.md` lines 12 to 73 and the subtask set against Turn 2 and brief line 55

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-004 | Parent task with subtasks | Verify a PM brief and one answer become one parent task listing four subtasks | `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the parent export | Step 1: baseline known. Step 2: one question and one clarification. Step 3: state retained. Step 4: one parent, four plain-text subtask entries, shared rules and Turn 2 facts intact | Both replies, ledger, clarification and parent export paths, read-back lines and artifact excerpts | PASS if routing, the context gate and a faithful parent all match. FAIL otherwise | 1. Check the `$task` rule. 2. Check the Parent Task template. 3. Diff the rules and the subtask set |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Command registry, the explicit-command question rule, the clarification export and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Export names and the HVR self-scan line |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, parent task type, required sections and the named-but-unlinked rule |
| [`task-templates.md`](../../assets/task-templates.md) | Parent Task scaffold and the Notes For Use |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Direct `$task` row and the clarification export |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: surfaces, plans, the `TODO` code, the owner's time zone and the title convention |
| [`loomlist-recurring-todos-pm-brief.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-pm-brief.md) | Attachment: recurrence rules, limit, plans, flag, tracking, frames, the build split and the open question |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-004
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/parent-task-with-subtasks.md`

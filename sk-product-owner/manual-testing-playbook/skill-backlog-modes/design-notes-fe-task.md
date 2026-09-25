---
title: "STK-002 -- Design notes FE task"
description: "Validates that a task command pointing at Roamstay date picker design notes asks one context question, then saves a front end task that carries every stay limit and copy string from the notes and every scope fact from the answer."
version: 1.0.0.0
---

# STK-002 -- Design notes FE task

This scenario validates the explicit `$task` path from a designer's handover notes to a saved front end task, through one clarification turn.

---

## 1. OVERVIEW

A Roamstay PM asks for the front end task behind the date picker stay limits and points at Ines's handover notes. `$task` fixes Task Mode, which still asks its context question before drafting, so Turn 1 saves a task-lane clarification. Turn 2 answers with the facts the notes do not hold: one task across iOS, Android and web, no parent, the Search squad and the 8.13.0 train, search-service left alone, and QA on all three platforms in en-GB and en-US. The notes carry the rest: the limits, the five picker states, the six copy keys with their en-GB strings, the edge cases, the platform differences and what stays out of this work.

A task that reads like the team's own carries a title in the `{Discipline} - {Surface} - {Feature code} - {Title}` pattern, here `FE`, Guest app and `SRCH`, an About that states the problem the notes give (search-service turns down stays over 30 nights after the guest taps Search, and Guest Support logged 23 chats about it in August), the frame `Date picker / Stay limits` as a plain-text reference, and numbered requirement groups for the limits, the states and copy, the edge cases and the platforms, each with a `**Checklist**`. The corpus closes such tasks with a Resolution Checklist that checks iOS, Android and web and a QA sign-off. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

Design handover notes are the most common input to a front end task. A task that hard-codes the limits the notes say come from config, stretches the 365-day rule to check-out or paraphrases the helper text ships a picker that disagrees with the design and with search-service.

---

## 2. SCENARIO CONTRACT

- Objective: Verify task routing, the single context question and a front end task that keeps every value from the design notes and every fact from the answer
- Real user request: `Can we get Ines's date picker notes into a ticket for the Search squad?`
- Prompt: `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-date-picker-design-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, answer in Turn 2 in the same session and inspect the task export
- Expected signals: `$task` routes to Task Mode by command (`AGENTS.md` line 190) and still asks its context question once and waits (`AGENTS.md` line 287, `references/task-mode.md` line 50, `references/interactive-mode.md` line 124), shaped like the Task Format question (`assets/interactive-response-templates.md` line 90). The question is saved as `export/[###] - task-[description]-clarification.md`, holding the question and nothing else, read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` line 82, root section 5, Clarification turns). A question that asks for a fact the notes already state is recorded only (root section 5, Ticket realism). Turn 2 saves `export/[###] - task-[description].md` on the next number, reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line (`AGENTS.md` lines 46 and 47). The task follows the Canonical Task template (`assets/task-templates.md` line 38): H1, `### About` and `### Requirements` (`references/task-mode.md` lines 72 to 78) and numbered groups each with a `**Checklist**` of `- [ ]` items (lines 102 to 112). It names the frame `Date picker / Stay limits` as plain text with no invented link (`references/task-mode.md` line 133) and carries the notes verbatim: a stay of 1 night to `30 nights`, check-in at most `365 days` ahead while check-out may land past it, the property minimum of 1 night to `14 nights` on the property page only, the buttons `Select check-in date`, `Select check-out date` and `Show prices`, the helper text `Stays can be up to 30 nights` and `This property has a 3-night minimum` with the property's own number, grey days that stay tappable, limits read from search-service config and the property details and never hard-coded, the design-system calendar on iOS and Android, two months side by side on desktop web and the Monday week start except in `en-US` (`roamstay-date-picker-design-notes.md` lines 15 to 62). It keeps every Turn 2 fact and leaves flexible dates, prices in the calendar and any tracking change out, as the notes do (lines 66 to 68)
- Desired user-visible outcome: One saved task-lane question, then a saved front end task for the date picker stay limits built from the notes and the answer
- Size band (advisory): 70 to 150 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, saves it under a `task` lane `-clarification` name reported with its path, the `Verified:` line and the `HVR self-scan:` line and drafts no task, and Turn 2 saves one `task` export on the next number, read back and reported the same way, carrying its H1, `### About` and `### Requirements` with checklisted requirement groups, the stay limits and the five copy strings exactly as the notes give them, and every Turn 2 fact. FAIL if Turn 1 drafts the task, the task hard-codes the limits in the apps, applies the 365-day limit to check-out, changes a number or a copy string, adds a tracking event, a search-service change or a flexible-dates requirement that no turn or attachment asks for without naming it as an addition, drops a Turn 2 fact, invents a link for the frame or leaves a template slot in the body
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.` | Read both attachments, ask the task context question once, save it as a task-lane clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Draft no task | Task Mode and the date picker stay limits stay selected, one new `-clarification` file, `context/` unchanged | Turn 1 reply, clarification file, read-back result and side-effect ledger |
| 2 | `One FE task for iOS, Android and web together, no parent, and the Search squad takes it into the 8.13.0 train. Leave search-service as it is, its own 30-night check stays as the backstop. QA signs it off on all three platforms in en-GB and en-US.` | Build the task from the notes and the answer, save it on the next number, read it back and reply path first with the `Verified:` line and the `HVR self-scan:` line | The notes' limits and copy and every Turn 2 fact survive into Requirements, the clarification file stays untouched | Turn 2 reply, task export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.`

### Commands

1. `sandbox: stage context/roamstay-context.md and context/roamstay-date-picker-design-notes.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new task export -> operator: grade the sections, requirement groups, limits, copy strings and Turn 2 facts against the notes and the answer`

### Expected

Step 1 fixes the baseline with both attachments staged. Step 2 returns one context question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds an H1, `### About`, `### Requirements` and numbered groups with `**Checklist**` items carrying `30 nights`, `365 days`, `14 nights`, `Select check-in date`, `Select check-out date`, `Show prices`, `Stays can be up to 30 nights` and `This property has a 3-night minimum`, the limits read from config, check-out free of the 365-day rule, and the Turn 2 scope, team, train, search-service boundary and QA locales.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the self-scan lines and task excerpts showing the limits, the five copy strings, the platform notes and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question saved as a task-lane clarification, no early draft, then one readable task export with the required sections, checklisted groups, every limit and copy string from the notes and every fact from the answer
- **Fail**: The runtime drafts before Turn 2, hard-codes or stretches a limit, paraphrases a copy string, adds tracking or a search-service change unasked, drops a Turn 2 fact, invents a frame link or leaves a template slot

### Failure triage

1. Check the direct `$task` rule at `AGENTS.md` line 287 and `references/interactive-mode.md` line 124, then the clarification export at `AGENTS.md` line 82
2. Compare the task with the Canonical Task template at `assets/task-templates.md` line 38 and the requirement grammar at `references/task-mode.md` lines 102 to 112
3. Diff every limit and copy string against `roamstay-date-picker-design-notes.md` lines 15 to 62 and every scope fact against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-002 | Design notes FE task | Verify design notes and one answer become a faithful front end task | `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the task export | Step 1: baseline known. Step 2: one question and one clarification. Step 3: state retained. Step 4: required sections, checklisted groups, limits, copy and Turn 2 facts intact | Both replies, ledger, clarification and task export paths, read-back lines and artifact excerpts | PASS if routing, the context gate and a faithful task all match. FAIL otherwise | 1. Check the `$task` rule. 2. Check the task template. 3. Diff limits, copy and Turn 2 facts |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Command registry, the explicit-command question rule, the clarification export and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Export names and the HVR self-scan line |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, required sections, requirement grammar and the plain-text reference rule |
| [`task-templates.md`](../../assets/task-templates.md) | Canonical Task scaffold |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Direct `$task` row and the clarification export |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Task Format question wording |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: surfaces, squads, the `SRCH` code, locales and the title convention |
| [`roamstay-date-picker-design-notes.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md) | Attachment: stay limits, picker states, copy keys, edge cases, platforms and exclusions |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/design-notes-fe-task.md`

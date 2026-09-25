---
title: "SID-001 -- Skill identity handover"
description: "Validates the skill runtime identity on a two-turn Loomlist task, where a task-lane clarification and then the task are each saved, read back and reported with a real export path."
version: 1.0.0.0
---

# SID-001 -- Skill identity handover

This scenario validates the skill runtime before any other skill-side scenario runs. It passes only when both replies prove the filesystem delivery contract that the Project runtime cannot produce.

---

## 1. OVERVIEW

The runtime runs from `AGENTS.md` with `sk-product-owner/` loaded and the Loomlist context page staged at `context/loomlist-context.md`. A Loomlist engineer asks for a small front end task for a new "Due today" filter chip on the To-dos view. `$task` routes to Task Mode, which still asks its context question before drafting, so Turn 1 delivers a task-lane clarification and Turn 2 delivers the task. Each delivery is saved, read back and reported with a real path, the `Verified: read-back succeeded` line and the `HVR self-scan:` line. The Project runtime has no such contract, so a reply carrying Project delivery wording fails this scenario.

### Why this matters

Every later skill scenario assumes the runtime can save a file, read it back and report the real path, for a clarification as well as for an artifact. An identity mistake here puts the whole skill set in question.

---

## 2. SCENARIO CONTRACT

- Objective: Verify skill identity through two filesystem deliveries, a task-lane clarification and then the task, each with a real readable export path and the read-back confirmation
- Real user request: `Can you set up a small front end task for a "Due today" filter chip on the Loomlist To-dos view? The chips we have today are described in the context page.`
- Prompt: `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: A disposable copy with an empty `export/` folder and `loomlist-context.md` staged at `context/loomlist-context.md`. This handover runs first in the skill set
- Expected execution process: Start a fresh skill session, submit Turn 1, inspect the clarification export, submit Turn 2 in the same session, then inspect the task export and compare both replies
- Expected signals: Turn 1 routes by command to Task Mode, which asks its context question once and waits (`AGENTS.md` line 287, `references/task-mode.md` line 50). The question is saved as `export/[###] - task-due-today-chip-clarification.md`, holding the question and nothing else, read back, and the reply carries that path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` lines 79 and 82). Turn 2 saves `export/[###] - task-due-today-chip.md` on the next number, reads it back and replies path first with the `Verified:` line, the `HVR self-scan:` line and a quality summary (`AGENTS.md` lines 46 and 47). The task carries its H1, `### About` and `### Requirements` (`references/task-mode.md` lines 72 to 78) and keeps the Turn 2 facts: Web as the platform, the chip right after Overdue, to-dos not checked off that are due today in the owner's time zone, the due-date sort, one active chip at a time, and `filter_selected` sent with `due_today`
- Desired user-visible outcome: A saved task-lane question, then a saved task for the "Due today" chip, each reported path first with the skill-only delivery lines
- Size band (advisory): 30 to 70 lines for the Turn 2 task body
- Pass/fail: PASS if both replies name a readable `export/` path and print the `Verified: read-back succeeded` line and the `HVR self-scan:` line, the Turn 1 file holds only the question under a `task` lane `-clarification` name, and the Turn 2 file is a `task` on the next number carrying its H1, `### About` and `### Requirements` with the Turn 2 facts intact and no invented fact or unfilled slot. FAIL if either reply prints `Export-equivalent path:`, claims no file was written or speaks of a Canvas Artifact, Turn 1 drafts the task instead of asking, a named path does not read back, or the task scopes work on iOS or Android, renames "Due today" or drops the owner's time zone
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md` | Route to Task Mode by command, ask the Task Mode context question once, save it as a task-lane clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Draft no task | One new export, the `-clarification` file, and `context/loomlist-context.md` unchanged | Turn 1 reply, clarification file, read-back result, side-effect ledger and folder listing |
| 2 | `Front end, Web only for now, Desktop gets it through the web client and the apps follow later. The chip goes right after Overdue and shows to-dos not checked off that are due today in the owner's time zone, sorted by due date like the other chips, and only one chip is active at a time. Picking it sends filter_selected with filter set to due_today, which Yara has already added to the tracking plan. No Figma, reuse the existing chip, and nothing else depends on it.` | Build the task from the answer, save it on the next number, read it back and reply path first with the `Verified:` line, the `HVR self-scan:` line and a quality summary | One new task export on the next number, the clarification file untouched and `context/` unchanged | Turn 2 reply, task file, read-back result, side-effect ledger and folder listing |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md`

### Commands

1. `sandbox: stage context/loomlist-context.md -> sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: list the export folder -> operator: open the clarification file and confirm it holds only the question`
4. `user: submit Turn 2 in the same session -> filesystem: list the export folder -> operator: open the task file and compare both replies against the skill contract`

### Expected

Step 1 fixes the baseline with the attachment in place. Step 2 produces one clarification export and the skill delivery lines. Step 3 proves the path is real and the file holds no draft. Step 4 produces one task on the next number with the skill delivery lines and the Turn 2 facts.

### Evidence

Capture both replies, the per-turn side-effect ledger, the export folder listing after each turn, both read-back results, both `HVR self-scan:` lines and both file bodies. For each delivery, record the line count the reply printed beside the final line number its Read call returned, which `AGENTS.md` line 46 makes the value of `N`.

Identity split proof from the worktree root:

- `grep -c "read-back succeeded" "AI Systems/Product Owner/AGENTS.md"` -> `2`, exit `0`
- `grep -c "read-back succeeded" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/AGENTS.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `4`, exit `0`

The skill identity string `read-back succeeded` is absent from the Project kernel, and the Project identity string `Canvas Artifact` is absent from the skill identity file. `AGENTS.md` carries the skill string twice, at line 47 for a single file and at line 91 for a Story bundle. A reply that could have come from either runtime, or that carries the other runtime's delivery wording, is a FAIL.

Fixture payload (skill delivery line): `Verified: read-back succeeded` followed by the line count, printed once per delivered file

### Pass / fail

- **Pass**: Both replies name a readable export path and print the `Verified: read-back succeeded` line and the `HVR self-scan:` line, the Turn 1 file is a question-only `task` lane clarification, and the Turn 2 file is a `task` on the next number with its H1, `### About` and `### Requirements`, the Turn 2 facts intact and no invented fact or unfilled slot
- **Fail**: Either reply prints `Export-equivalent path:`, speaks of a Canvas Artifact or claims no file was written, Turn 1 drafts the task instead of asking, a named path does not read back, or the task scopes iOS or Android work, renames "Due today" or drops the owner's time zone

### Failure triage

1. Re-run Turn 1 in a clean session and inspect the export folder before reading the reply
2. Compare the delivery wording with the skill delivery contract in `AGENTS.md` lines 46 to 50 and the clarification rule at lines 79 and 82
3. If the runtime emits Project vocabulary, state the identity failure at the top of the run report and keep grading the skill set, as the root's Handovers in an automated run section asks

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SID-001 | Skill identity handover | Verify the skill runtime through two read-back deliveries, a task-lane clarification and the task | `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification -> 4. Submit Turn 2 and inspect the task | Step 1: baseline known. Step 2: one clarification and the skill lines. Step 3: question only. Step 4: one task on the next number with the skill lines | Both replies, folder listings, both read-back results and both file bodies | PASS if both turns print the skill lines with readable paths and the task keeps the Turn 2 facts. FAIL on Project wording, an unreadable path or a drafted Turn 1 | 1. Re-run in a clean session. 2. Compare with the delivery contract. 3. Flag identity drift at the top of the run report and keep grading the set |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Skill identity, filesystem delivery and clarification export contract |
| [`SKILL.md`](../../SKILL.md) | Routing, export and read-back rules |
| [`task-mode.md`](../../references/task-mode.md) | Routed Task Mode workflow and its context question rule |
| [`task-templates.md`](../../assets/task-templates.md) | Routed task scaffold |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Task Format Question the Turn 1 clarification follows |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment, the current To-dos view chips and the owner's time zone rule |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Contrast kernel that sets the Project identity string |

---

## 5. SOURCE METADATA

- Group: Skill identity
- Playbook ID: SID-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-identity/identity-handover.md`

---
title: "PID-001 -- Project identity handover"
description: "Validates the Project runtime identity on a two-turn Loomlist task, where a task-lane clarification and then the task each render as a Deliverable Block with an export-equivalent label and no file claim."
version: 1.0.0.3
---

# PID-001 -- Project identity handover

This scenario validates the Project runtime before any other Project-side scenario runs. It passes only when both replies prove the Deliverable Block contract that the skill runtime will not emit.

---

## 1. OVERVIEW

The runtime runs from `claude project/Custom Instructions.md` with the full Project Knowledge set attached and the Loomlist context page staged at `context/loomlist-context.md`. A Loomlist engineer asks for a small front end task for a new "Due today" filter chip on the To-dos view. `$task` routes to Task Mode, which still asks its context question before drafting, so Turn 1 renders a task-lane clarification and Turn 2 renders the task. Each reply opens with its Deliverable Block, a Canvas Artifact where a Canvas panel exists and one delimited block where none does, then reports `Export-equivalent path:` and the `HVR self-scan:` line and claims no file. The skill runtime has a real filesystem contract, so a reply carrying a real path or a read-back claim fails this scenario.

### Why this matters

Every later Project scenario assumes the runtime renders a Deliverable Block and never claims a local save, for a clarification as well as for an artifact. An identity mistake here puts the whole Project set in question.

---

## 2. SCENARIO CONTRACT

- Objective: Verify Project identity through two rendered Deliverable Blocks, a task-lane clarification and then the task, each with an export-equivalent label and no file claim
- Real user request: `Can you set up a small front end task for a "Due today" filter chip on the Loomlist To-dos view? The chips we have today are described in the context page.`
- Prompt: `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: A fresh Project conversation with an empty Canvas panel baseline and `loomlist-context.md` staged at `context/loomlist-context.md`. This handover runs first in the Project set
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the rendered clarification block and the labels beside it, submit Turn 2 in the same conversation, then capture the rendered task block and compare both replies
- Expected signals: Turn 1 routes by command to Task Mode, which asks its context question once and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Task Mode` line 30). The reply opens with the question rendered as its own block holding the question and nothing else, then `Export-equivalent path: export/[NNN] - task-due-today-chip-clarification.md` and the `HVR self-scan:` line (`Custom Instructions.md` lines 85 and 228, `Product Owner - System - Interactive Mode` lines 70 and 74). Turn 2 opens with the task rendered as its own block, then `Export-equivalent path: export/[NNN] - task-due-today-chip.md`, the `HVR self-scan:` line and a quality summary (`Custom Instructions.md` lines 85, 86 and 223). Neither reply claims a file was saved, written or read back (`Custom Instructions.md` lines 101 and 233). The task carries its H1, `### About` and `### Requirements` (`Product Owner - Templates - Task Mode` lines 52 to 58) and keeps the Turn 2 facts: Web as the platform, the chip right after Overdue, to-dos not checked off that are due today in the owner's time zone, the due-date sort, one active chip at a time, and `filter_selected` sent with `due_today`
- Desired user-visible outcome: A rendered task-lane question, then a rendered task for the "Due today" chip, each with its export-equivalent label and no file claim
- Size band (advisory): 30 to 70 lines for the Turn 2 task body
- Pass/fail: PASS if both replies open with their rendered block, report `Export-equivalent path:` with a `task` lane name, the `-clarification` name on Turn 1, and print the `HVR self-scan:` line, neither reply claims a file was saved, written or read back, the Turn 1 block holds only the question, and the Turn 2 task carries its H1, `### About` and `### Requirements` with the Turn 2 facts intact and no invented fact or unfilled slot. The words `Canvas Artifact` are not required in either reply. FAIL if either reply prints `Path:`, `Saved:` or `Verified: read-back succeeded` or claims any local save, either block is missing or follows other reply text, Turn 1 renders the task instead of asking, or the task scopes work on iOS or Android, renames "Due today" or drops the owner's time zone
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md` | Route to Task Mode by command, ask the Task Mode context question once, render it as its own clarification block first, then report the export-equivalent label and the `HVR self-scan:` line. Render no task | The question renders as its own block, no file path is claimed and `context/loomlist-context.md` is unchanged | Turn 1 reply, rendered clarification block and the labels beside it |
| 2 | `Front end, Web only for now, Desktop gets it through the web client and the apps follow later. The chip goes right after Overdue and shows to-dos not checked off that are due today in the owner's time zone, sorted by due date like the other chips, and only one chip is active at a time. Picking it sends filter_selected with filter set to due_today, which Yara has already added to the tracking plan. No Figma, reuse the existing chip, and nothing else depends on it.` | Build the task from the answer, render it as its own block first, then report the export-equivalent label, the `HVR self-scan:` line and a quality summary | The task renders as its own block, the no-file-write boundary holds and `context/` is unchanged | Turn 2 reply, rendered task block and the labels beside it |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md`

### Commands

1. `sandbox: stage context/loomlist-context.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered clarification block -> operator: confirm it opens the reply and holds only the question`
4. `user: submit Turn 2 in the same conversation -> canvas: inspect the rendered task block -> operator: confirm no file was claimed and compare both replies against the Project contract`

### Expected

Step 1 fixes the panel baseline with the attachment in place. Step 2 produces one rendered clarification block and the Project delivery lines. Step 3 proves the block rendered first and holds no draft. Step 4 produces one rendered task with the Project delivery lines, the Turn 2 facts and no file claim.

### Evidence

Capture both replies, both rendered blocks, both export-equivalent labels, both `HVR self-scan:` lines, the form each block took and the absence of any real path claim.

Identity split proof from the worktree root:

- `grep -c "read-back succeeded" "AI Systems/Product Owner/AGENTS.md"` -> `2`, exit `0`
- `grep -c "read-back succeeded" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/AGENTS.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `4`, exit `0`

The Project identity string `Canvas Artifact` is absent from the skill identity file, and the skill identity string `read-back succeeded` is absent from the Project kernel. `Custom Instructions.md` carries the Project string at lines 76, 181, 221 and 235. A reply that could have come from either runtime, or that carries the other runtime's delivery wording, is a FAIL.

### Pass / fail

- **Pass**: Both replies open with their rendered block, report `Export-equivalent path:` with a `task` lane name and the `HVR self-scan:` line and claim no file, the Turn 1 block holds only the question under the `-clarification` name, and the Turn 2 task carries its H1, `### About` and `### Requirements` with the Turn 2 facts intact and no invented fact or unfilled slot
- **Fail**: Either reply prints `Path:`, `Saved:` or `Verified: read-back succeeded` or claims a local save, either block is missing or follows other reply text, Turn 1 renders the task instead of asking, or the task scopes iOS or Android work, renames "Due today" or drops the owner's time zone

### Failure triage

1. Re-run Turn 1 in a fresh Project and inspect where the block rendered
2. Compare the delivery wording with the Deliverable Block and export-equivalent rules in `Custom Instructions.md` lines 85, 86 and 219 to 233
3. If the runtime claims a local file, state the identity failure at the top of the run report and keep grading the Project set, as the root's Handovers in an automated run section asks

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PID-001 | Project identity handover | Verify the Project runtime through two rendered blocks, a task-lane clarification and the task, with no file claim | `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification block -> 4. Submit Turn 2 and inspect the task block | Step 1: baseline known. Step 2: one clarification block and the Project lines. Step 3: block first, question only. Step 4: one task block with the Project lines | Both replies, both rendered blocks, both labels and the no-file-write evidence | PASS if both turns render their block first with the Project lines and the task keeps the Turn 2 facts. FAIL on any real path, save claim or a drafted Turn 1 | 1. Re-run in a fresh Project. 2. Compare with the Deliverable Block rules. 3. Flag identity drift at the top of the run report and keep grading the set |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project identity, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.306.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.306.md) | Routed Task Mode workflow and its context question rule |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Routed task scaffold |
| [`Product Owner - System - Interactive Mode - v0.407.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.407.md) | Clarification block contract |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Task Format Question the Turn 1 clarification follows |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | Project routing authority |
| [`Product Owner - Rules - Human Voice Core - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Rules%20-%20Human%20Voice%20Core%20-%20v0.100.md) | HVR self-scan source |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment, the current To-dos view chips and the owner's time zone rule |
| [`AGENTS.md`](../../../AGENTS.md) | Contrast identity file that sets the skill identity string |

---

## 5. SOURCE METADATA

- Group: Project identity
- Playbook ID: PID-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-identity/identity-handover.md`

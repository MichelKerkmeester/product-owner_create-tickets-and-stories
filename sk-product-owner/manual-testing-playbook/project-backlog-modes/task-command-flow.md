---
title: "PTK-001 -- Task command flow"
description: "Validates task-command routing, the one-question context gate and the Task Deliverable Block in a Claude Project."
version: 1.0.0.0
---

# PTK-001 -- Task command flow

This scenario validates the explicit `$task` path from a low-context command to a rendered Task Deliverable Block.

---

## 1. OVERVIEW

The command fixes Task Mode. The Project should ask one consolidated context question, render it as a clarification block with an export-equivalent label, wait, then render the task block with `### About`, `### Requirements` and a `- [ ]` checklist while claiming no file was written.

### Why this matters

The Project cannot save files. Task QA handoff still depends on the same context gate and checklist that the skill runtime uses.

---

## 2. SCENARIO CONTRACT

- Objective: Verify task routing, the single context question, wait behavior and the Task Deliverable Block
- Real user request: `I need to get the creator payout pause feature written up as a task.`
- Prompt: `$task I need a task for the creator payout pause feature.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 and inspect the rendered task block
- Expected signals: Turn 1 asks one consolidated question, governed by the direct `$task` row at the Interactive Mode knowledge document line 101, renders a clarification block with `Export-equivalent path: export/[NNN] - task-payout-pause-feature-clarification.md` and claims no file was written. Turn 2 renders the task block, reports `Export-equivalent path: export/[NNN] - task-payout-pause-feature.md` and carries the HVR self-scan line
- Desired user-visible outcome: One task-context question followed by a task block and an export-equivalent label
- Pass/fail: PASS if the runtime waits, the task block carries the supplied facts and a checklist, and every path is labelled export-equivalent with no file claim. FAIL if it renders the final task before Turn 2, prints `Path:` or claims a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task I need a task for the creator payout pause feature.` | Ask one task-context question (the direct `$task` rule at the Interactive Mode knowledge document line 101), render it as a clarification block with an export-equivalent label and wait. Claim no file and render no task | Task Mode and the payout pause feature remain selected | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Standalone task. Creators need a pause indicator for pending payouts, and the pause reason must be stored. Acceptance: the reason field is required, the indicator appears in the payout row, and QA can verify the pause in the payout history.` | Render the task block from the supplied facts with its export-equivalent label and the HVR self-scan line | The supplied acceptance list and the standalone scope survive into Requirements | Turn 2 reply, rendered task block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task I need a task for the creator payout pause feature.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `operator: confirm one context question and no task draft -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered task block -> operator: grade sections, checklist, labels and the no-file-write boundary`

### Expected

Step 1 fixes the panel baseline. Step 2 returns one context question as a Canvas Artifact. Step 3 proves the wait state and state retention. Step 4 finds `### About`, `### Requirements` and a `- [ ]` checklist carrying the supplied acceptance items, under an export-equivalent label.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the no-file-write statements and the task sections showing the pause indicator, the stored reason and the payout history check.

### Pass / fail

- **Pass**: One context question, no early task block, one rendered task block with the supplied facts and a checklist, and no file claim
- **Fail**: The runtime renders the task before Turn 2, prints `Path:` or `Saved:`, claims a local file, or omits the export-equivalent label

### Failure triage

1. Check the direct `$task` routing rule at the Interactive Mode knowledge document line 101, then the task context gate and required sections in the Templates - Task Mode knowledge document
2. Compare the Turn 1 question with the task intake in the Task Templates knowledge document
3. Re-render the task block and confirm every claim stays inside the rendered artifact

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-001 | Task command flow | Verify explicit task routing through a rendered Task Deliverable Block | `$task I need a task for the creator payout pause feature.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Confirm wait and submit Turn 2 -> 4. Inspect the task block | Step 1: baseline known. Step 2: one context question. Step 3: state retained. Step 4: task block with checklist and label | Both replies, rendered blocks, labels and artifact excerpts | PASS if routing, context gate and block shape all match. FAIL otherwise | 1. Check Interactive Mode knowledge line 101. 2. Check the context question. 3. Check the block and checklist |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Canvas Artifact and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.305.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.305.md) | Project task workflow and structure rules |
| [`Product Owner - Assets - Task Templates - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.101.md) | Project task scaffold |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/task-command-flow.md`

---
title: "STK-001 -- Task command flow"
description: "Validates task-command routing, the one-question context gate and the exported task artifact with its QA checklist."
version: 1.0.0.0
---

# STK-001 -- Task command flow

This scenario validates the explicit `$task` path from a low-context command to a saved task export.

---

## 1. OVERVIEW

The command fixes Task Mode. The runtime should ask one consolidated context question for the missing requirement and acceptance detail, export that question as a clarification, wait, then export a task with `### About` and `### Requirements` and a `- [ ]` checklist.

### Why this matters

Task Mode is the default backlog lane. A task that skips the context gate or drops the checklist fails QA handoff.

---

## 2. SCENARIO CONTRACT

- Objective: Verify task routing, the single context question, wait behavior and canonical task output
- Real user request: `I need to get the creator payout pause feature written up as a task.`
- Prompt: `$task I need a task for the creator payout pause feature.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts
- Expected execution process: Start fresh, submit Turn 1, capture the context question and its clarification export, answer in Turn 2 and inspect the next task export
- Expected signals: Turn 1 asks one consolidated question, governed by the direct `$task` row at `interactive-mode.md` line 124, exports `export/[###] - task-payout-pause-feature-clarification.md`, reads it back and creates no task draft. Turn 2 keeps Task Mode, validates HVR, saves `export/[###] - task-payout-pause-feature.md`, reads it back and replies path-first with the HVR self-scan line
- Desired user-visible outcome: One task-context question followed by a validated task export
- Pass/fail: PASS if the runtime waits, keeps the payout pause feature, and every Turn 2 fact lands in a structured task with a checklist. FAIL if it saves the task before Turn 2, guesses acceptance criteria, or skips the read-back
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task I need a task for the creator payout pause feature.` | Ask one task-context question covering format and scope, requirements, acceptance criteria, dependencies and validation (the direct `$task` rule at `interactive-mode.md` line 124), export it as a clarification and wait. Create no task draft | Task Mode and the payout pause feature remain selected and no task draft exists | Turn 1 reply, clarification export, read-back result and clean task-draft ledger |
| 2 | `Standalone task. Creators need a pause indicator for pending payouts, and the pause reason must be stored. Acceptance: the reason field is required, the indicator appears in the payout row, and QA can verify the pause in the payout history.` | Build the task from the supplied facts, save the next task export, read it back and reply path-first with the HVR self-scan line | The supplied acceptance list and the standalone scope survive into Requirements | Turn 2 reply, exported task and read-back result |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task I need a task for the creator payout pause feature.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new task export -> operator: grade sections, checklist and retained facts`

### Expected

Step 1 fixes the baseline. Step 2 returns one context question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds `### About`, `### Requirements` and a `- [ ]` checklist carrying the supplied acceptance items.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the task sections showing the pause indicator, the stored reason and the payout history check.

### Pass / fail

- **Pass**: One context question, no early task draft, one readable task export with the supplied facts and a checklist
- **Fail**: The runtime saves the task before Turn 2, re-asks for mode, invents acceptance criteria or omits the read-back

### Failure triage

1. Check the direct `$task` routing rule at `interactive-mode.md` line 124, then the task context gate and required sections in `task-mode.md`
2. Compare the Turn 1 question with the Task Format question in `interactive-response-templates.md`
3. Reconcile the exported task with the supplied acceptance items and the export numbering rule

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-001 | Task command flow | Verify explicit task routing through a saved, validated task export | `$task I need a task for the creator payout pause feature.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the task export | Step 1: baseline known. Step 2: one context question and one clarification. Step 3: state retained. Step 4: compliant task with checklist | Both replies, ledger, clarification and task export paths and artifact excerpts | PASS if routing, context gate and task shape all match. FAIL otherwise | 1. Check the direct `$task` rule and Task Mode. 2. Check the context question. 3. Check the export and checklist |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, required sections and checklist grammar |
| [`task-templates.md`](../../assets/task-templates.md) | Canonical task scaffold |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Task context question wording |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/task-command-flow.md`

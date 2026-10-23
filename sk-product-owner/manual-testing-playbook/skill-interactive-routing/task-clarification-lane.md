---
title: "SIR-007 -- Task clarification keeps the Task lane"
description: "Validates that missing Task context uses the task clarification label rather than the generic intake lane."
version: 1.0.0.0
---

# SIR-007 -- Task clarification keeps the Task lane

This scenario validates the routing contract for task clarification keeps the task lane in the skill runtime.

---

## 1. OVERVIEW

A clarification about a known artifact must stay in that artifact lane so the answer resumes the right mode and numbering sequence.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that missing Task context uses the task clarification label rather than the generic intake lane.
- Real user request: $task Improve checkout reliability for Fernhouse.
- Prompt: `$task Improve checkout reliability for Fernhouse.`
- Attachments: None
- Runtime profile: skill, using `AGENTS.md` and `sk-product-owner/`
- Precondition: Start a fresh session. No attachments are required.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: Turn 1 writes a clarification in the Task lane and does not draft a Task. Turn 2 writes the Task under the next number. The runtime saves and reads back the artifact, then replies with the real export path and the read-back line. Any clarification saves the clarification in the named lane and reads it back. It claims no local save unless the path was read back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$task Improve checkout reliability for Fernhouse.` | Task Mode asks one context question, saves only the question as task-[description]-clarification.md and waits. | The clarification file uses the Task prefix and is outside any Story folder. | Reply capture and state ledger |
| 2 | `Add an inline retry message after payment declines on iOS and Android. Keep the entered address. Success means the shopper can retry without entering the address again.` | Task Mode writes the Task after the answer, under the next number in the Task lane. | The clarification stays untouched and the Task carries the answer. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task Improve checkout reliability for Fernhouse.`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

Turn 1 writes a clarification in the Task lane and does not draft a Task. Turn 2 writes the Task under the next number.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check the clarification lane sentence in interactive-mode.md Section 2
2. Check the Task clarification label in the response template


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-007 | Task clarification keeps the Task lane | Verify that missing Task context uses the task clarification label rather than the generic intake lane. | `$task Improve checkout reliability for Fernhouse.` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | Turn 1 writes a clarification in the Task lane and does not draft a Task. Turn 2 writes the Task under the next number. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check the clarification lane sentence in interactive-mode.md Section 2. Check the Task clarification label in the response template |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Interactive clarification contract`](../../references/interactive-mode.md) | Contract or paired runtime reference |
| [`Task Mode`](../../references/task-mode.md) | Contract or paired runtime reference |
| [`Response template`](../../assets/interactive-response-templates.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: skill interactive routing
- Playbook ID: SIR-007
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/task-clarification-lane.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

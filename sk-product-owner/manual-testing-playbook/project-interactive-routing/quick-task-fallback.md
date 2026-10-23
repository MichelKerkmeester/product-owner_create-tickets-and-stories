---
title: "PIR-008 -- Quick without an artifact uses Task fallback"
description: "Validates that a bare Quick energy command retains the narrow Task fallback."
version: 1.0.0.0
---

# PIR-008 -- Quick without an artifact uses Task fallback

This scenario validates the routing contract for quick without an artifact uses task fallback in the Project runtime.

---

## 1. OVERVIEW

Quick changes effort but does not select an artifact. Its no-intent fallback is intentionally limited to Task.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a bare Quick energy command retains the narrow Task fallback.
- Real user request: $q
- Prompt: `$q`
- Attachments: None
- Runtime profile: Project, using `claude project/Custom Instructions.md` and its Knowledge documents
- Precondition: Start a fresh session. Do not infer an artifact before the router applies its Quick fallback.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: The bare $q request selects Task at Quick energy. Its clarification stays in the Task lane and the answer produces a Task. The runtime renders one Deliverable Block with an export-equivalent path. Any clarification renders a clarification block in the named lane. It claims no local file write or read-back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$q` | The router selects Quick energy with the narrow Task fallback. Task Mode asks what work the requester needs and saves its clarification in the Task lane. | The question is labelled task, not intake, and no Task is drafted. | Reply capture and state ledger |
| 2 | `Create a saved-search empty state with the copy "No saved searches yet" and a button that starts a search.` | Task Mode writes one Task under the next Task number and preserves the exact copy. | The Task answers the request without changing its artifact lane. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$q`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

The bare $q request selects Task at Quick energy. Its clarification stays in the Task lane and the answer produces a Task.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check the Quick fallback reference in Custom Instructions Section 10
2. Check the Project Interactive Mode Task fallback pointer


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-008 | Quick without an artifact uses Task fallback | Verify that a bare Quick energy command retains the narrow Task fallback. | `$q` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | The bare $q request selects Task at Quick energy. Its clarification stays in the Task lane and the answer produces a Task. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check the Quick fallback reference in Custom Instructions Section 10. Check the Project Interactive Mode Task fallback pointer |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Quick fallback pointer`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode.md) | Contract or paired runtime reference |
| [`Project router`](../../../claude%20project/Custom%20Instructions.md) | Contract or paired runtime reference |
| [`Task Mode`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-008
- Runtime: Project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/quick-task-fallback.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

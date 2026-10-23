---
title: "PIR-006 -- Grouped bugs route to Task"
description: "Validates that grouped bugs, a consolidation ticket and bug-fix work route to Task Mode."
version: 1.0.0.0
---

# PIR-006 -- Grouped bugs route to Task

This scenario validates the routing contract for grouped bugs route to task in the Project runtime.

---

## 1. OVERVIEW

A Bug report covers one isolated defect. A request that groups defects or asks for a bug-fix task belongs to Task Mode.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that grouped bugs, a consolidation ticket and bug-fix work route to Task Mode.
- Real user request: $quick Make one bug-fix task for these three Fernhouse checkout defects: payment double-submits, the address clears after a decline, and retry is disabled after a timeout. Keep all three in one checkout reliability task for the Storefront team. Success means none can recur in the checkout suite.
- Prompt: `$quick Make one bug-fix task for these three Fernhouse checkout defects: payment double-submits, the address clears after a decline, and retry is disabled after a timeout. Keep all three in one checkout reliability task for the Storefront team. Success means none can recur in the checkout suite.`
- Attachments: None
- Runtime profile: Project, using `claude project/Custom Instructions.md` and its Knowledge documents
- Precondition: Start a fresh session. No ClickUp write is part of this scenario.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: Task Mode owns the grouped bug request. The output is one Task, not a Bug report or a set of individual reports. The runtime renders one Deliverable Block with an export-equivalent path. Any clarification renders a clarification block in the named lane. It claims no local file write or read-back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick Make one bug-fix task for these three Fernhouse checkout defects: payment double-submits, the address clears after a decline, and retry is disabled after a timeout. Keep all three in one checkout reliability task for the Storefront team. Success means none can recur in the checkout suite.` | The request routes to Task Mode and produces one task covering the three related fixes. It does not create three Bug reports. | The task stays one artifact with one checkout reliability scope and the stated success condition. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick Make one bug-fix task for these three Fernhouse checkout defects: payment double-submits, the address clears after a decline, and retry is disabled after a timeout. Keep all three in one checkout reliability task for the Storefront team. Success means none can recur in the checkout suite.`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

Task Mode owns the grouped bug request. The output is one Task, not a Bug report or a set of individual reports.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check the Bug-to-Task Routing Contract in Templates - Bug Mode Section 1
2. Check the Task route in Custom Instructions Section 10


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-006 | Grouped bugs route to Task | Verify that grouped bugs, a consolidation ticket and bug-fix work route to Task Mode. | `$quick Make one bug-fix task for these three Fernhouse checkout defects: payment double-submits, the address clears after a decline, and retry is disabled after a timeout. Keep all three in one checkout reliability task for the Storefront team. Success means none can recur in the checkout suite.` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | Task Mode owns the grouped bug request. The output is one Task, not a Bug report or a set of individual reports. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check the Bug-to-Task Routing Contract in Templates - Bug Mode Section 1. Check the Task route in Custom Instructions Section 10 |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Bug-to-Task contract`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Bug%20Mode.md) | Contract or paired runtime reference |
| [`Task Mode`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode.md) | Contract or paired runtime reference |
| [`Project kernel`](../../../claude%20project/Custom%20Instructions.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-006
- Runtime: Project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/grouped-bugs-to-task.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

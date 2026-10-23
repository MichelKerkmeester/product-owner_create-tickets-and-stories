---
title: "PIR-004 -- Story bundle after command conflict"
description: "Validates that a new Story with tasks uses the bundle path, while explicit $story $task commands first remain an Interactive conflict."
version: 1.0.0.0
---

# PIR-004 -- Story bundle after command conflict

This scenario validates the routing contract for story bundle after command conflict in the Project runtime.

---

## 1. OVERVIEW

A Story and its requested task breakdown form one dependent deliverable after the user selects that path. Two explicit artifact commands still require the user to resolve the command conflict first.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a new Story with tasks uses the bundle path, while explicit $story $task commands first remain an Interactive conflict.
- Real user request: $story $task Write a Story for Fernhouse order tracking, with one frontend task and one carrier-webhook task.
- Prompt: `$story $task Write a Story for Fernhouse order tracking, with one frontend task and one carrier-webhook task.`
- Attachments: None
- Runtime profile: Project, using `claude project/Custom Instructions.md` and its Knowledge documents
- Precondition: Start a fresh session. No attachments are required because Turn 3 supplies the user goal and each task boundary.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: Turn 1 asks one command-conflict question in the intake lane. Turn 2 resolves it to Story and triggers the Story context question. Turn 3 produces a Story bundle with a Story file and two ordered task files. The runtime renders one Deliverable Block with an export-equivalent path. Any clarification renders a clarification block in the named lane. It claims no local file write or read-back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$story $task Write a Story for Fernhouse order tracking, with one frontend task and one carrier-webhook task.` | Interactive Mode asks which artifact to create and saves one intake clarification. It does not choose the Story or the Task command. | No Story bundle folder exists before the user resolves the explicit command conflict. | Reply capture and state ledger |
| 2 | `Choose the Story as one bundle with the frontend and carrier-webhook tasks.` | The answer resolves the conflict as Story. Story Mode asks its own context question and keeps the clarification in the Story lane outside the future bundle folder. | The Story context question is asked after the command conflict answer. | Reply capture and state ledger |
| 3 | `The goal is to let Fernhouse guests see carrier progress after checkout. The frontend task shows the carrier status timeline. The webhook task accepts tracking.updated and ignores duplicate event_id values. Keep the Story and both tasks in that order.` | Story Mode writes one numbered Story folder. The Story lists two sibling Tasks. The files use the bundle numbering and the Canonical Task template. | The folder contains one Story and tasks .1 and .2. Each file is read back on the skill side or rendered as its own Project block. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$story $task Write a Story for Fernhouse order tracking, with one frontend task and one carrier-webhook task.`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

Turn 1 asks one command-conflict question in the intake lane. Turn 2 resolves it to Story and triggers the Story context question. Turn 3 produces a Story bundle with a Story file and two ordered task files.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check command collection in Custom Instructions Section 10
2. Check the Story bundle owner in Templates - Story Mode Section 7
3. Check the Task Mode path pointer and Assets - Task Templates


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-004 | Story bundle after command conflict | Verify that a new Story with tasks uses the bundle path, while explicit $story $task commands first remain an Interactive conflict. | `$story $task Write a Story for Fernhouse order tracking, with one frontend task and one carrier-webhook task.` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | Turn 1 asks one command-conflict question in the intake lane. Turn 2 resolves it to Story and triggers the Story context question. Turn 3 produces a Story bundle with a Story file and two ordered task files. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check command collection in Custom Instructions Section 10. Check the Story bundle owner in Templates - Story Mode Section 7. Check the Task Mode path pointer and Assets - Task Templates |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Story-to-Task contract`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode.md) | Contract or paired runtime reference |
| [`Task Mode pointer`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode.md) | Contract or paired runtime reference |
| [`Project kernel`](../../../claude%20project/Custom%20Instructions.md) | Contract or paired runtime reference |
| [`Interactive Mode`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-004
- Runtime: Project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/story-bundle-command-conflict.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

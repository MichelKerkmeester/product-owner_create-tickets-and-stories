---
title: "PIR-010 -- ClickUp handoff follows one owner"
description: "Validates verify mode guidance points to the one ClickUp Handoff owner and the reply waits for approval without a ClickUp write."
version: 1.0.0.0
---

# PIR-010 -- ClickUp handoff follows one owner

This scenario validates the routing contract for clickup handoff follows one owner in the Project runtime.

---

## 1. OVERVIEW

Mode references should point to one handoff contract. An offer must never create a ClickUp item before explicit approval.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify mode guidance points to the one ClickUp Handoff owner and the reply waits for approval without a ClickUp write.
- Real user request: $quick $task Disable Confirm after its first tap until the checkout response returns. Re-enable it after an error so the shopper can retry.
- Prompt: `$quick $task Disable Confirm after its first tap until the checkout response returns. Re-enable it after an error so the shopper can retry.`
- Attachments: None
- Runtime profile: Project, using `claude project/Custom Instructions.md` and its Knowledge documents
- Precondition: Do not use a live ClickUp account or call a ClickUp tool. Stop at the offer and record the owner pointer.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: The delivery reply points to the current ClickUp owner and offers the next step only. The explicit no-push answer causes no external write. The runtime renders one Deliverable Block with an export-equivalent path. Any clarification renders a clarification block in the named lane. It claims no local file write or read-back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $task Disable Confirm after its first tap until the checkout response returns. Re-enable it after an error so the shopper can retry.` | Task Mode asks its context question if required, then delivers the task and ends with the ClickUp offer when tooling is available. | The offer points to the single ClickUp Handoff owner. No ClickUp tool is called. | Reply capture and state ledger |
| 2 | `Do not push this yet.` | The runtime confirms the task is ready and performs no ClickUp write. | No external side effect occurs. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Disable Confirm after its first tap until the checkout response returns. Re-enable it after an error so the shopper can retry.`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

The delivery reply points to the current ClickUp owner and offers the next step only. The explicit no-push answer causes no external write.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check Custom Instructions Section 9, ClickUp Handoff
2. Check Knowledge mode references for the same owner pointer
3. Confirm no ClickUp call was made


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-010 | ClickUp handoff follows one owner | Verify mode guidance points to the one ClickUp Handoff owner and the reply waits for approval without a ClickUp write. | `$quick $task Disable Confirm after its first tap until the checkout response returns. Re-enable it after an error so the shopper can retry.` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | The delivery reply points to the current ClickUp owner and offers the next step only. The explicit no-push answer causes no external write. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check Custom Instructions Section 9, ClickUp Handoff. Check Knowledge mode references for the same owner pointer. Confirm no ClickUp call was made |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`ClickUp Handoff owner`](../../../claude%20project/Custom%20Instructions.md) | Contract or paired runtime reference |
| [`Task Mode pointer`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode.md) | Contract or paired runtime reference |
| [`Story Mode pointer`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode.md) | Contract or paired runtime reference |
| [`Doc Mode pointer`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-010
- Runtime: Project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/clickup-handoff-owner.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

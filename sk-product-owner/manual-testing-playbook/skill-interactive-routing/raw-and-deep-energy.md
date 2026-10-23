---
title: "SIR-009 -- Raw and Deep energy resolution"
description: "Validates verify explicit skip depth selects Raw, documented Deep words select Deep, and Quick always wins over Raw."
version: 1.0.0.0
---

# SIR-009 -- Raw and Deep energy resolution

This scenario validates the routing contract for raw and deep energy resolution in the skill runtime.

---

## 1. OVERVIEW

The resolver must use the same ordered energy signals in the interactive guidance, executable contract and Project kernel.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify explicit skip depth selects Raw, documented Deep words select Deep, and Quick always wins over Raw.
- Real user request: skip depth and write a task to add a clear error state when checkout fails
- Prompt: `skip depth and write a task to add a clear error state when checkout fails`
- Attachments: None
- Runtime profile: skill, using `AGENTS.md` and `sk-product-owner/`
- Precondition: Run each row in a separate fresh session. No ClickUp or Figma connector is needed.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: The first input resolves Raw. Each documented Deep phrase resolves Deep. The last two inputs resolve Quick despite the Raw phrase. The runtime saves and reads back the artifact, then replies with the real export path and the read-back line. Any clarification saves the clarification in the named lane and reads it back. It claims no local save unless the path was read back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `skip depth and write a task to add a clear error state when checkout fails` | Raw is selected from the explicit skip depth phrase. The phase flow is skipped while factual and scope gates still apply. | The route is Task at Raw energy. | Reply capture and state ledger |
| 2 | `deep write a task for the checkout retry` | Deep is selected from deep. | The route is Task at Deep energy. | Reply capture and state ledger |
| 3 | `think longer and write a story for saved searches` | Deep is selected from think longer. | The route is Story at Deep energy. | Reply capture and state ledger |
| 4 | `full depth on the api runbook` | Deep is selected from full depth. | The route is Doc at Deep energy. | Reply capture and state ledger |
| 5 | `complex multi-source work for the billing migration` | Deep is selected from complex multi-source work. | The route keeps the semantic artifact result and Deep energy. | Reply capture and state ledger |
| 6 | `$quick skip depth, write a task for checkout spacing` | Quick takes precedence over Raw. | The route is Task at Quick energy. | Reply capture and state ledger |
| 7 | `just do it skip depth and write a task for checkout spacing` | Just-do-it selects Quick and never Raw. | The route is Task at Quick energy. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `skip depth and write a task to add a clear error state when checkout fails`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

The first input resolves Raw. Each documented Deep phrase resolves Deep. The last two inputs resolve Quick despite the Raw phrase.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check energy order in interactive-mode.md Section 2
2. Compare ENERGY_SIGNAL_VOCABULARY in router-contract.md and route_contract.py
3. Run the differential energy corpus


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-009 | Raw and Deep energy resolution | Verify explicit skip depth selects Raw, documented Deep words select Deep, and Quick always wins over Raw. | `skip depth and write a task to add a clear error state when checkout fails` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | The first input resolves Raw. Each documented Deep phrase resolves Deep. The last two inputs resolve Quick despite the Raw phrase. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check energy order in interactive-mode.md Section 2. Compare ENERGY_SIGNAL_VOCABULARY in router-contract.md and route_contract.py. Run the differential energy corpus |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Energy resolver owner`](../../references/interactive-mode.md) | Contract or paired runtime reference |
| [`Prose router pointer`](../../references/routing.md) | Contract or paired runtime reference |
| [`Executable resolver`](../../references/router-contract.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: skill interactive routing
- Playbook ID: SIR-009
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/raw-and-deep-energy.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

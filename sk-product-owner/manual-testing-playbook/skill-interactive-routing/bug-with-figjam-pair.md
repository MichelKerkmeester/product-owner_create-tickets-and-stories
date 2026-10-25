---
title: "SIR-005 -- Bug paired with a FigJam sequence"
description: "Validates that a Bug route can carry a paired Flow output and uses the existing Flows reference slot only after a matching board read-back."
version: 1.0.0.0
---

# SIR-005 -- Bug paired with a FigJam sequence

This scenario validates the routing contract for bug paired with a figjam sequence in the skill runtime.

---

## 1. OVERVIEW

The route contract already pairs a Bug with a board. The Bug scaffold needs a place for a verified board link, and it already has a Flows reference group.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a Bug route can carry a paired Flow output and uses the existing Flows reference slot only after a matching board read-back.
- Real user request: $quick $bug On the Fernhouse checkout, one tap on Pay charges twice in 2 of 5 tries. Expected one charge, actual two. Add a FigJam sequence diagram of the attempt.
- Prompt: `$quick $bug On the Fernhouse checkout, one tap on Pay charges twice in 2 of 5 tries. Expected one charge, actual two. Add a FigJam sequence diagram of the attempt.`
- Attachments: None
- Runtime profile: skill, using `AGENTS.md` and `sk-product-owner/`
- Precondition: Start with no Figma connector. Do not call an external tool or create a board.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: The route object pairs Bug then Flow. The bug scaffold already provides References > Flows. Flow Mode stops at its playback with no model first, and after the playback's yes gives a checked model without a board URL when no connector is present. The reply does not claim a board or add a link when no board read-back is possible. The runtime saves and reads back the artifact, then replies with the real export path and the read-back line. Any clarification saves the clarification in the named lane and reads it back. It claims no local save unless the path was read back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $bug On the Fernhouse checkout, one tap on Pay charges twice in 2 of 5 tries. Expected one charge, actual two. Add a FigJam sequence diagram of the attempt.` | The route selects Bug with then: FLOW. The Bug is prepared first, then Flow Mode stops at its playback with no model and no board URL. | The bug template keeps its References > Flows slot. No invented board URL is added without a matching read-back. | Reply capture and state ledger |
| 2 | `Yes, that reading is right.` | With no Figma connector, Flow Mode gives a checked model and no board URL. | The bug template keeps its References > Flows slot. No invented board URL is added without a matching read-back. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $bug On the Fernhouse checkout, one tap on Pay charges twice in 2 of 5 tries. Expected one charge, actual two. Add a FigJam sequence diagram of the attempt.`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

The route object pairs Bug then Flow. The bug scaffold already provides References > Flows. Flow Mode stops at its playback with no model first, and after the playback's yes gives a checked model without a board URL when no connector is present. The reply does not claim a board or add a link when no board read-back is possible.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check the paired route in router-contract.md
2. Check the existing Flows group in the Bug Report Template
3. Check Flow Mode Section 8 for the link gate


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-005 | Bug paired with a FigJam sequence | Verify that a Bug route can carry a paired Flow output and uses the existing Flows reference slot only after a matching board read-back. | `$quick $bug On the Fernhouse checkout, one tap on Pay charges twice in 2 of 5 tries. Expected one charge, actual two. Add a FigJam sequence diagram of the attempt.` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | The route object pairs Bug then Flow. The bug scaffold already provides References > Flows. Flow Mode stops at its playback with no model first, and after the playback's yes gives a checked model without a board URL when no connector is present. The reply does not claim a board or add a link when no board read-back is possible. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check the paired route in router-contract.md. Check the existing Flows group in the Bug Report Template. Check Flow Mode Section 8 for the link gate |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Bug Mode pointer`](../../references/bug-mode.md) | Contract or paired runtime reference |
| [`Bug scaffold Flows slot`](../../assets/bug-report-template.md) | Contract or paired runtime reference |
| [`Flow pair contract`](../../../sk-create-figjam/references/flow-mode.md) | Contract or paired runtime reference |
| [`Router contract`](../../references/router-contract.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: skill interactive routing
- Playbook ID: SIR-005
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/bug-with-figjam-pair.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

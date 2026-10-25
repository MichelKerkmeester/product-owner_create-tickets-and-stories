---
title: "SIR-003 -- Flow first paired Story route"
description: "Validates that a FigJam opening signal followed by a Story request reaches the Product Owner packet and carries an ordered Story then Flow route."
version: 1.0.0.0
---

# SIR-003 -- Flow first paired Story route

This scenario validates the routing contract for flow first paired story route in the skill runtime.

---

## 1. OVERVIEW

The hub must keep the artifact request in the default packet, then the packet must hand the paired board to Flow Mode after the Story path.

### Why this matters

A routing rule is useful only when the selected mode and its next action agree with the documented contract.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a FigJam opening signal followed by a Story request reaches the Product Owner packet and carries an ordered Story then Flow route.
- Real user request: figjam the checkout flow, then write a story
- Prompt: `figjam the checkout flow, then write a story`
- Attachments: None
- Runtime profile: skill, using `AGENTS.md` and `sk-product-owner/`
- Precondition: Use a fresh session with no Figma connector. The no-connector path keeps the model reviewable and prevents a board write.
- Expected execution process: Start a fresh session for each independent case, submit the prompt exactly, capture the route and response, and inspect the specified export or Deliverable Block
- Expected signals: The opening FigJam signal does not take the request away from its Story request. The selected pair is Story then Flow. The Story question and artifact stay first. Flow Mode stops at its playback with no model first, and after the playback's yes returns a checked model without a board URL when no connector is present. The runtime saves and reads back the artifact, then replies with the real export path and the read-back line. Any clarification saves the clarification in the named lane and reads it back. It claims no local save unless the path was read back
- Desired user-visible outcome: The requested route completes with its stated lane, pair and next step, while the runtime avoids an unsupported artifact or external write
- Pass/fail: PASS if every route and handoff matches the contract and every side effect stays within this scenario. FAIL if the request selects another mode, the paired order changes, the clarification lane changes, a board URL is invented or ClickUp is written without approval
- Record SKIP only when a named runtime blocker prevents the behavior from being observed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `figjam the checkout flow, then write a story` | Stage one selects sk-product-owner. Stage two selects Story with then: FLOW. Story Mode asks its one context question and saves no Story yet. | The question stays in the Story lane and no Flow output starts before the Story is settled. | Reply capture and state ledger |
| 2 | `Quick is fine. A shopper needs to see payment processing, payment confirmed or payment declined. The Story goal is to reduce checkout support contacts. Draw one user flow from Pay through those three outcomes.` | Story Mode delivers the Story first, then hands the request to Flow Mode, which stops at its playback with no model and no board URL. | No board URL or Flow link is invented. The source stays in the Story lane and the flow model is not called a board. | Reply capture and state ledger |
| 3 | `Yes, that reading is right.` | With no Figma connector, Flow Mode returns a checked model and no board URL. | No board URL or Flow link is invented and the flow model is not called a board. | Reply capture and state ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `figjam the checkout flow, then write a story`

### Commands

1. `session: start fresh -> operator: capture the baseline`
2. `user: submit each prompt exactly as listed, using a new session when the scenario has independent cases`
3. `operator: verify the selected mode, energy, output order and clarification lane against the expected signals`
4. `filesystem: inspect the export and read-back, skill side only -> canvas: inspect the Deliverable Block, Project side only`
5. `operator: confirm no disallowed external write occurred`

### Expected

The opening FigJam signal does not take the request away from its Story request. The selected pair is Story then Flow. The Story question and artifact stay first. Flow Mode stops at its playback with no model first, and after the playback's yes returns a checked model without a board URL when no connector is present.

### Evidence

Capture each exact prompt and reply, the selected mode and energy when observable, clarification or delivery label, the side-effect ledger and the exported file or Deliverable Block.

### Pass / fail

- **Pass**: Every case selects the mode, energy and paired order stated here, keeps clarification in the correct lane, and makes no unsupported board link or external write
- **Fail**: A route selects the wrong mode, a paired output changes order, the clarification uses the wrong lane, a board URL is invented or ClickUp is written before approval

### Failure triage

1. Check the artifact-request-before-opening-signal rule in hub-router.json
2. Check the Flow handoff in SKILL.md Section 2
3. Check the paired-output contract in Flow Mode Section 8


| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-003 | Flow first paired Story route | Verify that a FigJam opening signal followed by a Story request reaches the Product Owner packet and carries an ordered Story then Flow route. | `figjam the checkout flow, then write a story` | 1. Start fresh -> 2. Submit each listed prompt -> 3. Inspect route and output -> 4. Check side effects | The opening FigJam signal does not take the request away from its Story request. The selected pair is Story then Flow. The Story question and artifact stay first. Flow Mode stops at its playback with no model first, and after the playback's yes returns a checked model without a board URL when no connector is present. | Replies, route evidence, side-effect ledger and delivery proof | PASS if every listed route and output matches. FAIL otherwise | Check the artifact-request-before-opening-signal rule in hub-router.json. Check the Flow handoff in SKILL.md Section 2. Check the paired-output contract in Flow Mode Section 8 |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario index |
| [`Product Owner packet routing`](../../SKILL.md) | Contract or paired runtime reference |
| [`Hub Stage One routing`](../../../SKILL.md) | Contract or paired runtime reference |
| [`Flow pair contract`](../../../sk-create-figjam/references/flow-mode.md) | Contract or paired runtime reference |
| [`Story Mode`](../../references/story-mode.md) | Contract or paired runtime reference |


---

## 5. SOURCE METADATA

- Group: skill interactive routing
- Playbook ID: SIR-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/flow-first-story-pair.md`

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes or no with reason |

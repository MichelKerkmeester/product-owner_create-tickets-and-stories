---
title: "FJ-010 -- A user flow from a product doc"
description: "This scenario validates a user flow from a product doc for `FJ-010`. It checks that a screen-by-screen request becomes a user flow of at most 9 nodes with labelled decision exits and a gate that waits."
version: 1.0.0.0
---

# FJ-010 -- A user flow from a product doc

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-010`.

---

## 1. OVERVIEW

This scenario validates a user flow from a product doc for `FJ-010`. It checks that a screen-by-screen request becomes a user flow of at most 9 nodes with labelled decision exits and a gate that waits.

### Why This Matters

The user flow is the strictest type, because a reader compares it node by node with the screens. A loose node or an unlabelled exit is a board nobody can trust.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-010` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a screen-by-screen request becomes a user flow of at most 9 nodes with labelled decision exits and a gate that waits
- Real user request: `$flow make a FigJam flow of Fernhouse returns on a new board in our Fernhouse Product plan. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`
- Prompt: `$flow make a FigJam flow of Fernhouse returns on a new board in our Fernhouse Product plan. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`
- Expected execution process: Pick the user flow, stop at the playback, which waits for its own yes and comes after an intake round only when the run opens one, then write one `flowchart` model with stadium ends, rectangle steps and rhombus decisions, check it, walk the rubric and end on the gate
- Expected signals: Turn 1 ends on the playback and shows no model. Turn 2 carries a model with at most 9 nodes, every decision exit labelled, camelCase ids and no `%% type:` line, the check prints `user flow: ok` with exit 0, and the gate waits. No write tool is called
- Desired user-visible outcome: A checked returns flow and a gate that waits
- Pass/fail: PASS if the run stops at the playback first, the model is a user flow that passes the check, every doc step is drawn or listed as left out, and the gate waits with nothing written. FAIL if the model breaks a user flow rule, a doc step disappears without a `Left out:` entry, or a write tool is called before the gate's yes

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow make a FigJam flow of Fernhouse returns on a new board in our Fernhouse Product plan. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-010 | A user flow from a product doc | Verify that a screen-by-screen request becomes a user flow of at most 9 nodes with labelled decision exits and a gate that waits | `$flow make a FigJam flow of Fernhouse returns on a new board in our Fernhouse Product plan. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm no model is shown and nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 2. `user: Yes, that reading is right. -> operator: confirm the reply is the gate, whose one question asks about the write alone` -> 3. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md` | Step 1 returns the playback with no model. Step 2 returns the gate, whose one question asks about the write alone. Step 3 prints `diagram 1, user flow: ok` with exit 0 | The reply, the tool calls, the model with its provenance table and the operator's check run | PASS if the run stops at the playback first, the model is a user flow that passes the check, every doc step is drawn or listed as left out, and the gate waits with nothing written. FAIL if the model breaks a user flow rule, a doc step disappears without a `Left out:` entry, or a write tool is called before the gate's yes | 1. Check the model against `references/types/user-flow.md` Section 3 2. Compare it with `assets/examples/user-flow-fernhouse-return.md` |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm no model is shown and nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
2. `user: Yes, that reading is right. -> operator: confirm the reply is the gate, whose one question asks about the write alone`
3. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md`

### Expected

Step 1 returns the playback with no model. Step 2 returns the gate, whose one question asks about the write alone. Step 3 prints `diagram 1, user flow: ok` with exit 0

### Evidence

The reply, the tool calls, the model with its provenance table and the operator's check run

### Pass / Fail

- **Pass**: the run stops at the playback first, the model is a user flow that passes the check, every doc step is drawn or listed as left out, and the gate waits with nothing written
- **Fail**: the model breaks a user flow rule, a doc step disappears without a `Left out:` entry, or a write tool is called before the gate's yes

### Failure Triage

1. Check the model against `references/types/user-flow.md` Section 3
2. Compare it with `assets/examples/user-flow-fernhouse-return.md`

---

## 4. SOURCE FILES

### Playbook Sources

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario summary |
| Feature catalog | No dedicated catalog entry: the packet has no feature catalog, so `SKILL.md` and the references below are the contract |

### Implementation And Test Anchors

| File | Role |
|---|---|
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | User flow rules |
| [`assets/flow-templates.md`](../../assets/flow-templates.md) | User flow patterns and the provenance table |
| [`assets/examples/user-flow-fernhouse-return.md`](../../assets/examples/user-flow-fernhouse-return.md) | Worked example |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-010
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/user-flow-from-product-doc.md`

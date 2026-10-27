---
title: "FJ-001 -- A sequence picked from an API brief"
description: "This scenario validates a sequence picked from an API brief for `FJ-001`. It checks that a request for the order of calls between services becomes a checked sequence model and a gate that waits, with no board written."
version: 1.0.2.0
---

# FJ-001 -- A sequence picked from an API brief

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-001`.

---

## 1. OVERVIEW

This scenario validates a sequence picked from an API brief for `FJ-001`. It checks that a request for the order of calls between services becomes a checked sequence model and a gate that waits, with no board written.

### Why This Matters

A sequence answers which party speaks when. Drawn as a flowchart, the same brief loses its participants and its reply arrows, and the board cannot be fixed by dragging because the composer owns the layout.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-001` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request for the order of calls between services becomes a checked sequence model and a gate that waits, with no board written
- Real user request: `$figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201.`
- Prompt: `$figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201.`
- Expected execution process: Route to Flow Mode on `$figjam`, pick the sequence type, load its reference and template, stop at the playback, which waits for its own yes and comes after the intake rounds the run opens, if any, then write one sequence model with a provenance table, check it until it passes, walk the quality rubric and end on a gate that names the plan, a new file, the effect and the rollback
- Expected signals: Turn 1 ends on the playback, which names the sequence type, and shows no model and no write. Turn 2 carries a `sequenceDiagram` model with four declared participants and no aliases, notes or fragments, shows a check run whose last result is `PASSED` with exit 0 and ends on a gate that waits. No write tool is called
- Desired user-visible outcome: A checked sequence model of the payment and a gate that waits
- Pass/fail: PASS if the run stops at the playback first, the type is sequence, the model passes the check, the gate names the plan, a new file, the effect and the rollback and waits, and nothing is written. FAIL if the model is a flowchart, the check never ran or failed, a write tool is called before the gate's yes, or the reply claims a board

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-001 | A sequence picked from an API brief | Verify that a request for the order of calls between services becomes a checked sequence model and a gate that waits, with no board written | `$figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201.` | 1. `sandbox: record the connected tool list -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm no model is shown and nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 3. `user: Yes, that reading is right. -> operator: confirm the reply is the gate, whose one question asks about the write alone` -> 4. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md` | Step 2 returns the playback with no model. Step 3 returns the gate, whose one question asks about the write alone. Step 4 prints `diagram 1, sequence: ok` with exit 0, and the tool calls hold no write tool or `fj` create verb | The reply, the tool calls with every check run and its exit status, the model with its provenance table and the operator's own check run | PASS if the run stops at the playback first, the type is sequence, the model passes the check, the gate names the plan, a new file, the effect and the rollback and waits, and nothing is written. FAIL if the model is a flowchart, the check never ran or failed, a write tool is called before the gate's yes, or the reply claims a board | 1. Check the type table in `references/flow-mode.md` Section 3 and the type detection in `SKILL.md` Section 2 2. Check the model against `references/types/sequence.md` Section 3 and rerun the check on it 3. Check the gate against `references/flow-mode.md` Section 2 step 7 |

### Commands

1. `sandbox: record the connected tool list -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm no model is shown and nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last`
3. `user: Yes, that reading is right. -> operator: confirm the reply is the gate, whose one question asks about the write alone`
4. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md`

### Expected

Step 2 returns the playback with no model. Step 3 returns the gate, whose one question asks about the write alone. Step 4 prints `diagram 1, sequence: ok` with exit 0, and the tool calls hold no write tool or `fj` create verb

### Evidence

The reply, the tool calls with every check run and its exit status, the model with its provenance table and the operator's own check run

### Pass / Fail

- **Pass**: the run stops at the playback first, the type is sequence, the model passes the check, the gate names the plan, a new file, the effect and the rollback and waits, and nothing is written
- **Fail**: the model is a flowchart, the check never ran or failed, a write tool is called before the gate's yes, or the reply claims a board

### Failure Triage

1. Check the type table in `references/flow-mode.md` Section 3 and the type detection in `SKILL.md` Section 2
2. Check the model against `references/types/sequence.md` Section 3 and rerun the check on it
3. Check the gate against `references/flow-mode.md` Section 2 step 7

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Type table, workflow and gate |
| [`references/types/sequence.md`](../../references/types/sequence.md) | Sequence rules and budget |
| [`assets/templates/sequence.md`](../../assets/templates/sequence.md) | Sequence patterns |
| [`scripts/flow_check.py`](../../scripts/flow_check.py) | The pre-write check |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/sequence-from-api-brief.md`

---
title: "FJ-041 -- A named type that does not answer the brief"
description: "This scenario validates a named type that does not answer the brief for `FJ-041`. It checks that a request that names a state diagram over a brief that describes a path through screens gets one question naming the mismatch and the recommended type, and only the confirmed type is modelled."
version: 1.0.0.0
---

# FJ-041 -- A named type that does not answer the brief

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-041`.

---

## 1. OVERVIEW

This scenario validates a named type that does not answer the brief for `FJ-041`. It checks that a request that names a state diagram over a brief that describes a path through screens gets one question naming the mismatch and the recommended type, and only the confirmed type is modelled.

### Why This Matters

The reader's question picks the type, not the word they used. A state diagram over a screen path drops the order and the choices, and a type change made in silence hides the change.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-041` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request that names a state diagram over a brief that describes a path through screens gets one question naming the mismatch and the recommended type, and only the confirmed type is modelled
- Real user request: `$figjam a state diagram of the Fernhouse return flow on a new board in our Fernhouse Product plan: a customer opens an order, taps Return an item, picks a reason, chooses a refund or store credit and sees a confirmation`
- Prompt: `$figjam a state diagram of the Fernhouse return flow on a new board in our Fernhouse Product plan: a customer opens an order, taps Return an item, picks a reason, chooses a refund or store credit and sees a confirmation`
- Expected execution process: Route to Flow Mode, compare the named type with what the brief describes, ask one question that names the mismatch and recommends the type for the reader's question, then stop at the playback over the confirmed type and model it
- Expected signals: The first reply asks one question that names the state diagram, the screen path the brief describes and the type it recommends, and writes no model. The second reply is the reader round, or the playback over the confirmed type when the run opens no intake round, and shows no model. The third reply models the confirmed type, checks it and ends on a gate that waits
- Desired user-visible outcome: A checked flow of the screens, chosen with one word from the user
- Pass/fail: PASS if one question names the mismatch and the recommended type, and the model carries the confirmed type after the playback over it. FAIL if the named type is modelled over a brief it does not fit, the type changes with no question, or more than one question is asked

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam a state diagram of the Fernhouse return flow on a new board in our Fernhouse Product plan: a customer opens an order, taps Return an item, picks a reason, chooses a refund or store credit and sees a confirmation`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-041 | A named type that does not answer the brief | Verify that a request that names a state diagram over a brief that describes a path through screens gets one question naming the mismatch and the recommended type, and only the confirmed type is modelled | `$figjam a state diagram of the Fernhouse return flow on a new board in our Fernhouse Product plan: a customer opens an order, taps Return an item, picks a reason, chooses a refund or store credit and sees a confirmation` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: read the reply and the tool calls` -> 2. `user: reply use your recommendation -> operator: confirm the reply is the reader round or, when the run opens no intake round, the playback over the recommended type, and that no model or Figma tool call has happened` -> 3. `user: Yes, that reading is right. -> operator: read the type at the top of the model, the check run and the gate` | Step 1 returns one question naming the mismatch and the recommended type, with no model. Step 2 finds the reader round, or the playback over the recommended type when the run opens no intake round, with no model and no Figma tool call. Step 3 finds the recommended type in the model, a passing check and a gate that waits | Both replies, the model with its provenance table and the check output with its exit status | PASS if one question names the mismatch and the recommended type, and the model carries the confirmed type after the playback over it. FAIL if the named type is modelled over a brief it does not fit, the type changes with no question, or more than one question is asked | 1. Check the type table in `references/flow-mode.md` Section 3 2. Check the type detection in `SKILL.md` Section 2 3. Check the ambiguous-type recovery in `references/flow-mode.md` Section 9 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: read the reply and the tool calls`
2. `user: reply use your recommendation -> operator: confirm the reply is the reader round or, when the run opens no intake round, the playback over the recommended type, and that no model or Figma tool call has happened`
3. `user: Yes, that reading is right. -> operator: read the type at the top of the model, the check run and the gate`

### Expected

Step 1 returns one question naming the mismatch and the recommended type, with no model. Step 2 finds the reader round, or the playback over the recommended type when the run opens no intake round, with no model and no Figma tool call. Step 3 finds the recommended type in the model, a passing check and a gate that waits

### Evidence

Both replies, the model with its provenance table and the check output with its exit status

### Pass / Fail

- **Pass**: one question names the mismatch and the recommended type, and the model carries the confirmed type
- **Fail**: the named type is modelled over a brief it does not fit, the type changes with no question, or more than one question is asked

### Failure Triage

1. Check the type table in `references/flow-mode.md` Section 3
2. Check the type detection in `SKILL.md` Section 2
3. Check the ambiguous-type recovery in `references/flow-mode.md` Section 9

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Type choice and recovery |
| [`SKILL.md`](../../SKILL.md) | Type detection |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-041
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/named-type-does-not-fit.md`

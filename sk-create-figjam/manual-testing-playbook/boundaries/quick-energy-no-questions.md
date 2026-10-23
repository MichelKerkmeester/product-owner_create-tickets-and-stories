---
title: "FJ-042 -- A thin brief at Quick energy with no questions"
description: "This scenario validates a thin brief at Quick energy with no questions for `FJ-042`. It checks that a thin brief sent at Quick energy with a plain no-questions request asks nothing, models the best reading of the brief, marks each inferred fact assumed and names the assumptions in the playback before the gate."
version: 1.0.0.0
---

# FJ-042 -- A thin brief at Quick energy with no questions

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-042`.

---

## 1. OVERVIEW

This scenario validates a thin brief at Quick energy with no questions for `FJ-042`. It checks that a thin brief sent at Quick energy with a plain no-questions request asks nothing, models the best reading of the brief, marks each inferred fact assumed and names the assumptions in the playback before the gate.

### Why This Matters

Quick energy removes the round of questions, not the record. A run that asks anyway ignores the request, and a run that fills the gap in silence hands the user a board of facts they never chose.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-042` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a thin brief sent at Quick energy with a plain no-questions request asks nothing, models the best reading of the brief, marks each inferred fact assumed and names the assumptions in the playback before the gate
- Real user request: `$flow $quick the Fernhouse damaged-item flow on a new board in our Fernhouse Product plan. Just do it, no questions.`
- Prompt: `$flow $quick the Fernhouse damaged-item flow on a new board in our Fernhouse Product plan. Just do it, no questions.`
- Expected execution process: Route to Flow Mode at Quick energy, ask nothing, take the damage and refund flow from the brief as the best reading, run the check and end on a gate whose playback names each assumed fact
- Expected signals: The reply asks no question, carries a checked model, marks every step and actor it inferred as assumed, names each one in the playback before the gate and waits for the yes. No write tool is called
- Desired user-visible outcome: A checked flow, a named record of what was assumed and a gate that waits
- Pass/fail: PASS if no question is asked, every inferred fact is marked assumed and named in the playback, and the gate waits with nothing written. FAIL if a question is asked, an inferred fact reaches the model unmarked, an assumption is missing from the playback, or a write tool is called before the yes

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow $quick the Fernhouse damaged-item flow on a new board in our Fernhouse Product plan. Just do it, no questions.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-042 | A thin brief at Quick energy with no questions | Verify that a thin brief sent at Quick energy with a plain no-questions request asks nothing, models the best reading of the brief, marks each inferred fact assumed and names the assumptions in the playback before the gate | `$flow $quick the Fernhouse damaged-item flow on a new board in our Fernhouse Product plan. Just do it, no questions.` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: read the reply, the model and the tool calls` -> 2. `operator: list every fact the brief does not state and compare it with the playback` | Step 1 returns the model, the playback and the gate with no question. Step 2 finds each fact the brief does not state named as assumed | The reply, the model with its provenance table and the tool calls with the check output | PASS if no question is asked, every inferred fact is marked assumed and named in the playback, and the gate waits with nothing written. FAIL if a question is asked, an inferred fact reaches the model unmarked, an assumption is missing from the playback, or a write tool is called before the yes | 1. Check the `$flow` energy line in `references/flow-mode.md` Section 1 and the intake in Section 4 2. Check the gate in `references/flow-mode.md` Section 2 step 7 and the playback in Section 8 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: read the reply, the model and the tool calls`
2. `operator: list every fact the brief does not state and compare it with the playback`

### Expected

Step 1 returns the model, the playback and the gate with no question. Step 2 finds each fact the brief does not state named as assumed

### Evidence

The reply, the model with its provenance table and the tool calls with the check output

### Pass / Fail

- **Pass**: no question is asked, every inferred fact is marked assumed and named in the playback, and the gate waits with nothing written
- **Fail**: a question is asked, an inferred fact reaches the model unmarked, an assumption is missing from the playback, or a write tool is called before the yes

### Failure Triage

1. Check the `$flow` energy line in `references/flow-mode.md` Section 1 and the intake in Section 4
2. Check the gate in `references/flow-mode.md` Section 2 step 7 and the playback in Section 8

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | The `$flow` energy line, intake and delivery |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | The reply checks |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-042
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/quick-energy-no-questions.md`

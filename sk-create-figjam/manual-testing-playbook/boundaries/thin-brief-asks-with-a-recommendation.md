---
title: "FJ-039 -- A thin brief gets a question with a recommended answer"
description: "This scenario validates a thin brief gets a question with a recommended answer for `FJ-039`. It checks that a brief that names a flow and no steps gets one round of questions, each with the reading of the brief, a recommended answer and a one-line reason, and the run then models on those answers with each one marked assumed and named in the playback."
version: 1.0.0.0
---

# FJ-039 -- A thin brief gets a question with a recommended answer

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-039`.

---

## 1. OVERVIEW

This scenario validates a thin brief gets a question with a recommended answer for `FJ-039`. It checks that a brief that names a flow and no steps gets one round of questions, each with the reading of the brief, a recommended answer and a one-line reason, and the run then models on those answers with each one marked assumed and named in the playback.

### Why This Matters

A thin brief is the commonest request this packet sees. A reader who does not know the answer needs a recommendation to accept, and a run that stops on its question leaves that reader with nothing.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-039` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a brief that names a flow and no steps gets one round of questions, each with the reading of the brief, a recommended answer and a one-line reason, and the run then models on those answers with each one marked assumed and named in the playback
- Real user request: `$flow the Fernhouse return flow on a new board in our Fernhouse Product plan`
- Prompt: `$flow the Fernhouse return flow on a new board in our Fernhouse Product plan`
- Expected execution process: Route to Flow Mode, ask what the board needs in one round, each question carrying a reading and a recommended answer, then model on those answers once the user takes them
- Expected signals: The first reply asks one round of questions, each naming what the brief shows, a recommended answer and a one-line reason, and writes no model. The second reply carries a checked model, marks each fact it read rather than found as assumed, names the assumptions in the playback and ends on a gate that waits
- Desired user-visible outcome: A checked flow built on readings the user could see and correct
- Pass/fail: PASS if every question carries a reading and a recommended answer, the run takes them and asks no second round, and each assumption is marked and named in the playback before the gate. FAIL if the run stops on an unanswered question, asks the same questions again, models a fact it never marked as assumed, or leaves an assumption out of the playback

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow the Fernhouse return flow on a new board in our Fernhouse Product plan`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-039 | A thin brief gets a question with a recommended answer | Verify that a brief that names a flow and no steps gets one round of questions, each with the reading of the brief, a recommended answer and a one-line reason, and the run then models on those answers with each one marked assumed and named in the playback | `$flow the Fernhouse return flow on a new board in our Fernhouse Product plan` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: read the questions and the tool calls` -> 2. `user: reply go with your recommendations -> operator: read the model, the playback, the gate and every tool call` | Step 1 returns one round of questions with a reading and a recommended answer each. Step 2 finds no model and no Figma tool call. Step 3 finds a passing check and a gate that waits, with each assumed fact named in the playback | Both replies, the tool calls with the check output and its exit status, the model with its provenance table and the playback | PASS if every question carries a reading and a recommended answer, the run takes them and asks no second round, and each assumption is marked and named in the playback before the gate. FAIL if the run stops on an unanswered question, asks the same questions again, models a fact it never marked as assumed, or leaves an assumption out of the playback | 1. Check the intake questions in `assets/flow-templates.md` 2. Check the draw-ready threshold in `references/flow-mode.md` Section 2 and the intake in Section 4 3. Check the playback and the gate in `references/flow-mode.md` Section 8 and Section 2 step 7 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: read the questions and the tool calls`
2. `user: reply go with your recommendations -> operator: read the model, the playback, the gate and every tool call`

### Expected

Step 1 returns one round of questions with a reading and a recommended answer each. Step 2 finds no model and no Figma tool call. Step 3 finds a passing check and a gate that waits, with each assumed fact named in the playback

### Evidence

Both replies, the tool calls with the check output and its exit status, the model with its provenance table and the playback

### Pass / Fail

- **Pass**: every question carries a reading and a recommended answer, the run takes them and asks no second round, and each assumption is marked and named in the playback before the gate
- **Fail**: the run stops on an unanswered question, asks the same questions again, models a fact it never marked as assumed, or leaves an assumption out of the playback

### Failure Triage

1. Check the intake questions in `assets/flow-templates.md`
2. Check the draw-ready threshold in `references/flow-mode.md` Section 2 and the intake in Section 4
3. Check the playback and the gate in `references/flow-mode.md` Section 8 and Section 2 step 7

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
| [`assets/flow-templates.md`](../../assets/flow-templates.md) | The intake questions and their recommended answers |
| [`references/flow-mode.md`](../../references/flow-mode.md) | Intake, the draw-ready threshold, the playback and the gate |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-039
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/thin-brief-asks-with-a-recommendation.md`

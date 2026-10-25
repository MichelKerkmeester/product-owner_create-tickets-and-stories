---
title: "FJ-011 -- A laned process with the handoff in focus"
description: "This scenario validates a laned process with the handoff in focus for `FJ-011`. It checks that work that changes hands between teams becomes a process with one lane per actor, the neutral lane pair and one `style` line that puts the handoff step in focus."
version: 1.0.1.0
---

# FJ-011 -- A laned process with the handoff in focus

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-011`.

---

## 1. OVERVIEW

This scenario validates a laned process with the handoff in focus for `FJ-011`. It checks that work that changes hands between teams becomes a process with one lane per actor, the neutral lane pair and one `style` line that puts the handoff step in focus.

### Why This Matters

A process answers who does what. Without lanes the reader cannot see where a claim waits between teams, which is usually the reason the diagram was asked for.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-011` and confirm the expected signals without contradictory evidence.

- Objective: Verify that work that changes hands between teams becomes a process with one lane per actor, the neutral lane pair and one `style` line that puts the handoff step in focus
- Real user request: `draw how a Fernhouse damaged-item refund moves between the customer, a CS agent and the warehouse as a FigJam process on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse`
- Prompt: `draw how a Fernhouse damaged-item refund moves between the customer, a CS agent and the warehouse as a FigJam process on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse`
- Expected execution process: Pick the process type, stop at the playback, which waits for its own yes and comes after an intake round only when the run opens one, then start the block with `%% type: process`, put each actor in a lane with the neutral lane pair, add one `style` line on the CS step that hands the claim to the warehouse, check it and end on the gate
- Expected signals: Turn 1 ends on the playback and shows no model. Turn 2 carries a model that opens with `%% type: process`, holds 2 to 6 lanes with `#F5F5F5` and `#B3B3B3` and carries one `style` line from the style guide on the step that hands the work to the warehouse and no `linkStyle`. The check prints `process: ok` with exit 0. The gate waits
- Desired user-visible outcome: A checked laned process and a gate that waits
- Pass/fail: PASS if the run stops at the playback first, the model is a laned process that passes the check with one `style` line on the handoff step, and nothing is written. FAIL if the lanes are missing or nested, more than one accent is set, the handoff is marked with a `linkStyle` on a connector (which passes the check and draws nothing), the `%% type:` line is missing or a write tool is called before the gate's yes

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `draw how a Fernhouse damaged-item refund moves between the customer, a CS agent and the warehouse as a FigJam process on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-011 | A laned process with the handoff in focus | Verify that work that changes hands between teams becomes a process with one lane per actor, the neutral lane pair and one `style` line that puts the handoff step in focus | `draw how a Fernhouse damaged-item refund moves between the customer, a CS agent and the warehouse as a FigJam process on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm no model is shown and nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 2. `user: Yes, that reading is right. -> operator: confirm the reply is the gate` -> 3. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md` | Step 1 returns the playback with no model. Step 2 returns the gate. Step 3 prints `diagram 1, process: ok` with exit 0 | The reply, the tool calls, the model and the operator's check run | PASS if the run stops at the playback first, the model is a laned process that passes the check with one `style` line on the handoff step, and nothing is written. FAIL if the lanes are missing or nested, more than one accent is set, the handoff is marked with a `linkStyle` on a connector (which passes the check and draws nothing), the `%% type:` line is missing or a write tool is called before the gate's yes | 1. Check `references/types/process.md` Section 3 for lanes and the budget 2. Check the `style` line against `references/style-guide.md` Section 3, What a `style` line means |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm no model is shown and nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
2. `user: Yes, that reading is right. -> operator: confirm the reply is the gate`
3. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md`

### Expected

Step 1 returns the playback with no model. Step 2 returns the gate. Step 3 prints `diagram 1, process: ok` with exit 0

### Evidence

The reply, the tool calls, the model and the operator's check run

### Pass / Fail

- **Pass**: the run stops at the playback first, the model is a laned process that passes the check with one `style` line on the handoff step, and nothing is written
- **Fail**: the lanes are missing or nested, more than one accent is set, the handoff is marked with a `linkStyle` on a connector (which passes the check and draws nothing), the `%% type:` line is missing or a write tool is called before the gate's yes

### Failure Triage

1. Check `references/types/process.md` Section 3 for lanes and the budget
2. Check the `style` line against `references/style-guide.md` Section 3, What a `style` line means

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
| [`references/types/process.md`](../../references/types/process.md) | Process rules |
| [`assets/templates/process.md`](../../assets/templates/process.md) | Process patterns |
| [`assets/examples/process-fernhouse-refund.md`](../../assets/examples/process-fernhouse-refund.md) | Worked example |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-011
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/laned-process-from-handoffs.md`

---
title: "FJ-022 -- User flow board quality"
description: "This scenario validates user flow board quality for `FJ-022`. It checks that a written user flow is legible, laid out in one direction, carries one accent and answers a fresh reader's questions from the screenshot alone."
version: 1.0.0.0
---

# FJ-022 -- User flow board quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-022`.

---

## 1. OVERVIEW

This scenario validates user flow board quality for `FJ-022`. It checks that a written user flow is legible, laid out in one direction, carries one accent and answers a fresh reader's questions from the screenshot alone.

### Why This Matters

A user flow is compared screen by screen with the product. A board that fails a five-second read sends the reader back to the screenshots it was meant to replace.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-022` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written user flow is legible, laid out in one direction, carries one accent and answers a fresh reader's questions from the screenshot alone
- Real user request: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review.`
- Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review.`
- Expected execution process: Pick the user flow, model 9 nodes with the 30-day decision and the method decision, leave the proposal out by name, accent the confirmation, check, gate, write on the yes and read back
- Expected signals: The board holds 9 of 9 nodes, 9 of 9 connectors and 2 of 2 decisions with every exit labelled, top to bottom. The one accent sits on Return confirmed, and the reply carries `Left out:` naming the proposal. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-022 | User flow board quality | Verify that a written user flow is legible, laid out in one direction, carries one accent and answers a fresh reader's questions from the screenshot alone | `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate` -> 3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 6. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts 9 of 9 nodes, 9 of 9 connectors and 2 of 2 decisions with every exit labelled, top to bottom. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Is the free pickup over 100 euros live? Answer: it is not on the board, and the reply names it under Left out. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate`
3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
6. `operator: score the four Hygiene checks against the first and last read and score Reply`
7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts 9 of 9 nodes, 9 of 9 connectors and 2 of 2 decisions with every exit labelled, top to bottom. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Is the free pickup over 100 euros live? Answer: it is not on the board, and the reply names it under Left out. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8
2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late
3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior
4. When Clarity lost points, name the question the reader missed and the node or label that misled them

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
| [`assets/examples/user-flow-fernhouse-return.md`](../../assets/examples/user-flow-fernhouse-return.md) | The model this request should produce |
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | User flow rules and read-back |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | Board and reply checks |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-022
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/user-flow-board-quality.md`

---
title: "FJ-023 -- Process board quality"
description: "This scenario validates process board quality for `FJ-023`. It checks that a written process keeps each step in its lane, puts the one handoff step the request names in focus and reads in greyscale."
version: 1.0.2.0
---

# FJ-023 -- Process board quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-023`.

---

## 1. OVERVIEW

This scenario validates process board quality for `FJ-023`. It checks that a written process keeps each step in its lane, puts the one handoff step the request names in focus and reads in greyscale.

### Why This Matters

Lanes are the reason a process exists. A step drawn in the wrong lane tells the reader the wrong team owns it.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-023` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written process keeps each step in its lane, puts the one handoff step the request names in focus and reads in greyscale
- Real user request: `make a FigJam process of how a Fernhouse damaged-item refund moves between the customer, CS and the warehouse, on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse. From the support runbook: the customer reports damage with a photo through the help form. A CS agent checks the photo, approves clear damage on the spot and asks for a second photo when it is unclear. An approved claim goes to the warehouse queue, where an operator books a courier pickup, inspects the item on arrival and releases the refund. Every decision is logged in the claims table. Refunds under 20 euros skip the pickup, a pilot that is not yet live.`
- Prompt: `make a FigJam process of how a Fernhouse damaged-item refund moves between the customer, CS and the warehouse, on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse. From the support runbook: the customer reports damage with a photo through the help form. A CS agent checks the photo, approves clear damage on the spot and asks for a second photo when it is unclear. An approved claim goes to the warehouse queue, where an operator books a courier pickup, inspects the item on arrival and releases the refund. Every decision is logged in the claims table. Refunds under 20 euros skip the pickup, a pilot that is not yet live.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after an intake round only when the run opens one. Then pick the process, put each actor in a lane with the lane pair, add one `style` line on Approve the claim, the step that hands the claim to the warehouse, leave the pilot out by name, check, stop at the gate, compose on the gate's yes and read back
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 8 of 8 nodes, 8 of 8 connectors, 1 of 1 decision with both exits labelled and 3 of 3 lanes, each step in its lane. The only mark is Approve the claim drawn in focus in light pink with the pink outline and named In focus in the key. Every other step keeps the colour of its kind. The greyscale copy still answers Q3 from the lane labels. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `make a FigJam process of how a Fernhouse damaged-item refund moves between the customer, CS and the warehouse, on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse. From the support runbook: the customer reports damage with a photo through the help form. A CS agent checks the photo, approves clear damage on the spot and asks for a second photo when it is unclear. An approved claim goes to the warehouse queue, where an operator books a courier pickup, inspects the item on arrival and releases the refund. Every decision is logged in the claims table. Refunds under 20 euros skip the pickup, a pilot that is not yet live.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-023 | Process board quality | Verify that a written process keeps each step in its lane, puts the one handoff step the request names in focus and reads in greyscale | `make a FigJam process of how a Fernhouse damaged-item refund moves between the customer, CS and the warehouse, on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse. From the support runbook: the customer reports damage with a photo through the help form. A CS agent checks the photo, approves clear damage on the spot and asks for a second photo when it is unclear. An approved claim goes to the warehouse queue, where an operator books a courier pickup, inspects the item on arrival and releases the refund. Every decision is logged in the claims table. Refunds under 20 euros skip the pickup, a pilot that is not yet live.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 8 of 8 nodes, 8 of 8 connectors, 1 of 1 decision with both exits labelled and 3 of 3 lanes, each step in its lane. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Who books the courier pickup? Answer: the warehouse operator. Q2: What happens when the damage is unclear? Answer: the customer sends a second photo and CS checks again. Q3: Where does the claim change teams? Answer: from CS approving the claim to the warehouse booking the pickup. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet`
4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 8 of 8 nodes, 8 of 8 connectors, 1 of 1 decision with both exits labelled and 3 of 3 lanes, each step in its lane. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Who books the courier pickup? Answer: the warehouse operator. Q2: What happens when the damage is unclear? Answer: the customer sends a second photo and CS checks again. Q3: Where does the claim change teams? Answer: from CS approving the claim to the warehouse booking the pickup. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8
2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late
3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior
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
| [`assets/examples/process-fernhouse-refund.md`](../../assets/examples/process-fernhouse-refund.md) | The model this request should produce |
| [`references/types/process.md`](../../references/types/process.md) | Lanes, rules and read-back |
| [`references/style-guide.md`](../../references/style-guide.md) | The lane pair and what a `style` line means |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-023
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/process-board-quality.md`

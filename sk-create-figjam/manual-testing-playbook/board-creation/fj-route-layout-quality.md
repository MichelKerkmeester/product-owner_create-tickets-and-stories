---
title: "FJ-035 -- Layout quality on the fj route"
description: "This scenario validates layout quality on the fj route for `FJ-035`. It checks that a user flow written node by node through fj has no overlap, even spacing and every edge label beside its own connector."
version: 1.0.1.0
---

# FJ-035 -- Layout quality on the fj route

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-035`.

---

## 1. OVERVIEW

This scenario validates layout quality on the fj route for `FJ-035`. It checks that a user flow written node by node through fj has no overlap, even spacing and every edge label beside its own connector.

### Why This Matters

The fj route has no layout verb, so every position is computed by the runtime. This is the route most likely to produce a board that is correct and hard to read.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-035` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a user flow written node by node through fj has no overlap, even spacing and every edge label beside its own connector
- Real user request: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`
- Prompt: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after an intake round only when the run opens one. Then model and check the flow, run fj info, stop at the gate naming the open file, write with fj shape, fj connect and fj text on the gate's yes and read back with fj nodes -l
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 9 of 9 nodes, 9 of 9 connectors and 4 of 4 edge labels as text nodes. No two nodes overlap, the gaps between rows differ by at most a quarter of the largest gap, each edge label sits closer to its own connector than to any other, and no fj delete or fj eval is called. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a written node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when Figma Desktop or the figma-ds-cli daemon is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-035 | Layout quality on the fj route | Verify that a user flow written node by node through fj has no overlap, even spacing and every edge label beside its own connector | `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.` | 1. `sandbox: confirm Figma Desktop holds an empty FigJam file and the figma-ds-cli daemon runs, with no hosted MCP -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 3. `user: Yes, that reading is right. -> operator: confirm fj info ran before the gate and that nothing is written yet` -> 4. `user: Yes, go ahead. -> operator: record every fj command and run fj nodes -l` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 9 of 9 nodes, 9 of 9 connectors and 4 of 4 edge labels as text nodes. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Where does the flow start? Answer: the order list. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a written node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when Figma Desktop or the figma-ds-cli daemon is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as a limit of the `fj` route 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm Figma Desktop holds an empty FigJam file and the figma-ds-cli daemon runs, with no hosted MCP -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
3. `user: Yes, that reading is right. -> operator: confirm fj info ran before the gate and that nothing is written yet`
4. `user: Yes, go ahead. -> operator: record every fj command and run fj nodes -l`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 9 of 9 nodes, 9 of 9 connectors and 4 of 4 edge labels as text nodes. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Where does the flow start? Answer: the order list. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a written node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when Figma Desktop or the figma-ds-cli daemon is unavailable in this environment, naming that blocker

### Failure Triage

1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8
2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late
3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as a limit of the `fj` route
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
| [`references/flow-mode.md`](../../references/flow-mode.md) | The fj route |
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | User flow rules |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-035
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/fj-route-layout-quality.md`

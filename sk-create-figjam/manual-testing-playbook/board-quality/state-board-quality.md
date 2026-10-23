---
title: "FJ-026 -- State board with status tint quality"
description: "This scenario validates state board with status tint quality for `FJ-026`. It checks that a written state diagram with its end states tinted keeps every transition labelled, places the tint behind the three end states and covers no label."
version: 1.0.0.0
---

# FJ-026 -- State board with status tint quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-026`.

---

## 1. OVERVIEW

This scenario validates state board with status tint quality for `FJ-026`. It checks that a written state diagram with its end states tinted keeps every transition labelled, places the tint behind the three end states and covers no label.

### Why This Matters

Support reads a lifecycle to answer where a booking can go next. A tint that covers a label or misses an end state hides the one answer the colour was added for.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-026` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written state diagram with its end states tinted keeps every transition labelled, places the tint behind the three end states and covers no label
- Real user request: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Expected execution process: Pick the state type, model the composite Confirmed state, plan one status tint, check, gate naming the tint, write, add the tint with insertChild(0) and read back
- Expected signals: The board holds every state of the model, every transition with its label and 1 of 1 status tint behind Completed, Cancelled and NoShow. The tint extends 24 pixels past the end states on every side, sits behind them and covers no label, and the reply carries `Extensions: 1 of 1 status tint, 0 overlaps`. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-026 | State board with status tint quality | Verify that a written state diagram with its end states tinted keeps every transition labelled, places the tint behind the three end states and covers no label | `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate` -> 3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 6. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts every state of the model, every transition with its label and 1 of 1 status tint behind Completed, Cancelled and NoShow. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which states end a booking? Answer: Completed, Cancelled and No-show. Q2: From which states can a guest cancel? Answer: Pending and Confirmed. Q3: What moves a booking from Upcoming to In stay? Answer: check in. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate`
3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
6. `operator: score the four Hygiene checks against the first and last read and score Reply`
7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts every state of the model, every transition with its label and 1 of 1 status tint behind Completed, Cancelled and NoShow. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which states end a booking? Answer: Completed, Cancelled and No-show. Q2: From which states can a guest cancel? Answer: Pending and Confirmed. Q3: What moves a booking from Upcoming to In stay? Answer: check in. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

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
| [`assets/examples/state-roamstay-booking.md`](../../assets/examples/state-roamstay-booking.md) | The model this request should produce |
| [`references/types/state.md`](../../references/types/state.md) | State rules and read-back |
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | The status tint recipe |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-026
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/state-board-quality.md`

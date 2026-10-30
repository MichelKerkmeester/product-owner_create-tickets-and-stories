---
title: "FJ-036 -- A dense flow at the budget"
description: "This scenario validates a dense flow at the budget for `FJ-036`. It checks that a user flow at the node budget with a three-way decision keeps every exit label readable and no connector crossing."
version: 1.0.4.0
---

# FJ-036 -- A dense flow at the budget

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-036`.

---

## 1. OVERVIEW

This scenario validates a dense flow at the budget for `FJ-036`. It checks that a user flow at the node budget with a three-way decision keeps every exit label readable and no connector crossing.

### Why This Matters

Boards degrade first at the budget: labels crowd, exits cross and the reader loses which branch is which. This finds that limit before a user does.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-036` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a user flow at the node budget with a three-way decision keeps every exit label readable and no connector crossing
- Real user request: `$flow how a Roamstay guest changes their booking dates in the app, on a new board in our Roamstay Product plan. From the booking page they tap Change dates and pick new dates. If the room is not free on those dates they see other rooms. If the new price is higher they pay the difference, if it is lower they get the difference back as credit, and if it is the same nothing is charged. Then they see the updated booking. The help article also says: the date picker shows only nights the hotel has open, the other rooms list shows up to 3 rooms at the same hotel with their price for the new dates, a higher price is charged to the card on file, credit is kept for 12 months, and the updated booking is also sent by email.`
- Prompt: `$flow how a Roamstay guest changes their booking dates in the app, on a new board in our Roamstay Product plan. From the booking page they tap Change dates and pick new dates. If the room is not free on those dates they see other rooms. If the new price is higher they pay the difference, if it is lower they get the difference back as credit, and if it is the same nothing is charged. Then they see the updated booking. The help article also says: the date picker shows only nights the hotel has open, the other rooms list shows up to 3 rooms at the same hotel with their price for the new dates, a higher price is charged to the card on file, credit is kept for 12 months, and the updated booking is also sent by email.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any. Then pick the user flow, model the availability decision and the three-way price decision within 9 nodes, check, stop at the gate, write on the gate's yes and read back
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds every node of the model within 9, every connector and 2 of 2 decisions with all 5 exits labelled. No connector crosses another, and every exit label reads at 100% zoom without touching another label. Where the source excerpt describes a step, a zone or a party, the board carries it at the Balanced or Faithful level, in a detail card under the step's label or a note under the zone's or lane's title, so a reader answers Q4 and Q5 from the board alone. The scorecard totals at least 20 of 24, with Composition, Fidelity, the four Hygiene checks, Reply and Substance at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow how a Roamstay guest changes their booking dates in the app, on a new board in our Roamstay Product plan. From the booking page they tap Change dates and pick new dates. If the room is not free on those dates they see other rooms. If the new price is higher they pay the difference, if it is lower they get the difference back as credit, and if it is the same nothing is charged. Then they see the updated booking. The help article also says: the date picker shows only nights the hotel has open, the other rooms list shows up to 3 rooms at the same hotel with their price for the new dates, a higher price is charged to the card on file, credit is kept for 12 months, and the updated booking is also sent by email.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-036 | A dense flow at the budget | Verify that a user flow at the node budget with a three-way decision keeps every exit label readable and no connector crossing | `$flow how a Roamstay guest changes their booking dates in the app, on a new board in our Roamstay Product plan. From the booking page they tap Change dates and pick new dates. If the room is not free on those dates they see other rooms. If the new price is higher they pay the difference, if it is lower they get the difference back as credit, and if it is the same nothing is charged. Then they see the updated booking. The help article also says: the date picker shows only nights the hotel has open, the other rooms list shows up to 3 rooms at the same hotel with their price for the new dates, a higher price is charged to the card on file, credit is kept for 12 months, and the updated booking is also sent by email.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q5 -> operator: score Clarity on Q1 to Q3 and Substance on Q4 and Q5, and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts every node of the model within 9, every connector and 2 of 2 decisions with all 5 exits labelled. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What happens when the room is not free on the new dates? Answer: the guest sees other rooms. Q2: What happens when the new price is lower? Answer: the difference comes back as credit. Q3: Is anything charged when the price is the same? Answer: no. Source questions for Substance: Q4: How many other rooms does the guest see? Answer: up to 3, at the same hotel. Q5: How long is the credit kept? Answer: 12 months. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them
5. When Substance lost points, name the excerpt line the board left out and the card or note that would carry it |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last`
3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet`
4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q5 -> operator: score Clarity on Q1 to Q3 and Substance on Q4 and Q5, and total the scorecard`

### Expected

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts every node of the model within 9, every connector and 2 of 2 decisions with all 5 exits labelled. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What happens when the room is not free on the new dates? Answer: the guest sees other rooms. Q2: What happens when the new price is lower? Answer: the difference comes back as credit. Q3: Is anything charged when the price is the same? Answer: no. Source questions for Substance: Q4: How many other rooms does the guest see? Answer: up to 3, at the same hotel. Q5: How long is the credit kept? Answer: 12 months. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8
2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late
3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior
4. When Clarity lost points, name the question the reader missed and the node or label that misled them
5. When Substance lost points, name the excerpt line the board left out and the card or note that would carry it

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
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | Budget, decisions and exits |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | The board checks |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-036
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/dense-flow-at-budget.md`

---
title: "FJ-027 -- ER board with domain zones quality"
description: "This scenario validates ER board with domain zones quality for `FJ-027`. It checks that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two `%% zone:` sections."
version: 1.0.3.0
---

# FJ-027 -- ER board with domain zones quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-027`.

---

## 1. OVERVIEW

This scenario validates ER board with domain zones quality for `FJ-027`. It checks that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two `%% zone:` sections.

### Why This Matters

An ER diagram is read to answer how many of one thing another holds. A cardinality label that is cut off, or a zone that splits the wrong tables, answers that wrongly.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-027` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two `%% zone:` sections
- Real user request: `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.`
- Prompt: `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any. Then pick the ER type, model six entities with their keys, add two `%% zone:` lines, Guest side and Partner side, check, stop at the gate naming one composed board, compose with one `use_figma` call on the gate's yes and read back
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, in 2 of 2 zones. The Guest side zone holds Guest, Booking and Payment and the Partner side zone holds Property, Room and Rate Plan. Neither zone covers a label. Each relationship's cardinality reads from the marks at its two ends and from its label, such as `makes (1 to 0..n)`, at 100% zoom. No extension call is made and the reply carries no `Extensions:` line. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when an extension call is made. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-027 | ER board with domain zones quality | Verify that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two `%% zone:` sections | `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, in 2 of 2 zones. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: How many rooms does one booking reserve? Answer: one. Q2: Which entity publishes rate plans? Answer: Property. Q3: Can one booking hold several payments? Answer: yes. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when an extension call is made. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last`
3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet`
4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, in 2 of 2 zones. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: How many rooms does one booking reserve? Answer: one. Q2: Which entity publishes rate plans? Answer: Property. Q3: Can one booking hold several payments? Answer: yes. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when an extension call is made. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`assets/examples/er-roamstay-stays.md`](../../assets/examples/er-roamstay-stays.md) | The model this request should produce |
| [`references/types/er.md`](../../references/types/er.md) | ER rules, zones and read-back |
| [`references/flow-mode.md`](../../references/flow-mode.md) | Zones as a layout lever and the ER connector read |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-027
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/er-board-quality.md`

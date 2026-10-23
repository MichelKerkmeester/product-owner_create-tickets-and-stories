---
title: "FJ-027 -- ER board with domain tints quality"
description: "This scenario validates eR board with domain tints quality for `FJ-027`. It checks that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two domain tints."
version: 1.0.0.0
---

# FJ-027 -- ER board with domain tints quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-027`.

---

## 1. OVERVIEW

This scenario validates eR board with domain tints quality for `FJ-027`. It checks that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two domain tints.

### Why This Matters

An ER diagram is read to answer how many of one thing another holds. Cardinality marks too small to read, or tints that split the wrong tables, answer that wrongly.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-027` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two domain tints
- Real user request: `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.`
- Prompt: `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.`
- Expected execution process: Pick the ER type, model six entities with their keys, plan two domain tints, check, gate naming both tints, write, add the tints and read back
- Expected signals: The board holds 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, plus 2 of 2 domain tints. The guest tint holds Guest, Booking and Payment and the partner tint holds Property, Room and Rate Plan, neither covers a label, and the crow's-foot marks read at 100% zoom. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| FJ-027 | ER board with domain tints quality | Verify that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two domain tints | `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate` -> 3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 6. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, plus 2 of 2 domain tints. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: How many rooms does one booking reserve? Answer: one. Q2: Which entity publishes rate plans? Answer: Property. Q3: Can one booking hold several payments? Answer: yes, at least one and possibly more. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate`
3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
6. `operator: score the four Hygiene checks against the first and last read and score Reply`
7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, plus 2 of 2 domain tints. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: How many rooms does one booking reserve? Answer: one. Q2: Which entity publishes rate plans? Answer: Property. Q3: Can one booking hold several payments? Answer: yes, at least one and possibly more. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

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
| [`assets/examples/er-roamstay-stays.md`](../../assets/examples/er-roamstay-stays.md) | The model this request should produce |
| [`references/types/er.md`](../../references/types/er.md) | ER rules and read-back |
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | Tints behind a group |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-027
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/er-board-quality.md`

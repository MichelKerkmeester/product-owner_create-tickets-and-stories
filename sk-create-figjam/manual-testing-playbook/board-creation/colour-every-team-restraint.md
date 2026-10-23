---
title: "FJ-034 -- A request to colour every team"
description: "This scenario validates a request to colour every team for `FJ-034`. It checks that a request to colour each step by team keeps one accent on the board, explains why and offers a laned process instead."
version: 1.0.0.0
---

# FJ-034 -- A request to colour every team

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-034`.

---

## 1. OVERVIEW

This scenario validates a request to colour every team for `FJ-034`. It checks that a request to colour each step by team keeps one accent on the board, explains why and offers a laned process instead.

### Why This Matters

Colour by category breaks the one-accent rule and the greyscale test. Lanes answer who does what without colour carrying the meaning.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-034` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request to colour each step by team keeps one accent on the board, explains why and offers a laned process instead
- Real user request: `$flow the Fernhouse damaged-item refund as a FigJam flow on a new board in our Fernhouse Product plan, and colour each step by the team that does it: customer reports damage with a photo, CS checks it and approves or asks for a second photo, the warehouse books a pickup, inspects the item and releases the refund`
- Prompt: `$flow the Fernhouse damaged-item refund as a FigJam flow on a new board in our Fernhouse Product plan, and colour each step by the team that does it: customer reports damage with a photo, CS checks it and approves or asks for a second photo, the warehouse books a pickup, inspects the item and releases the refund`
- Expected execution process: Find a category colour request, explain the one-accent rule, offer a process with a lane per team, and on the yes to the process write it with the lane pair and at most one accent
- Expected signals: The board holds 3 of 3 lanes with the lane pair and at most one accent. Turn 1 writes nothing, the board shows no colour per team, and the greyscale copy answers all three questions. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the board carries a colour per team or Turn 1 writes before the offer is answered. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow the Fernhouse damaged-item refund as a FigJam flow on a new board in our Fernhouse Product plan, and colour each step by the team that does it: customer reports damage with a photo, CS checks it and approves or asks for a second photo, the warehouse books a pickup, inspects the item and releases the refund`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-034 | A request to colour every team | Verify that a request to colour each step by team keeps one accent on the board, explains why and offers a laned process instead | `$flow the Fernhouse damaged-item refund as a FigJam flow on a new board in our Fernhouse Product plan, and colour each step by the team that does it: customer reports damage with a photo, CS checks it and approves or asks for a second photo, the warehouse books a pickup, inspects the item and releases the refund` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply explains one accent and offers lanes, with no write` -> 3. `user: Yes, use lanes. -> operator: confirm the passing check and the gate` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts 3 of 3 lanes with the lane pair and at most one accent. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Who inspects the item? Answer: the warehouse. Q2: What does CS do when the photo is unclear? Answer: asks for a second photo. Q3: How many teams take part? Answer: three. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the board carries a colour per team or Turn 1 writes before the offer is answered. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply explains one accent and offers lanes, with no write`
3. `user: Yes, use lanes. -> operator: confirm the passing check and the gate`
4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts 3 of 3 lanes with the lane pair and at most one accent. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Who inspects the item? Answer: the warehouse. Q2: What does CS do when the photo is unclear? Answer: asks for a second photo. Q3: How many teams take part? Answer: three. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the board carries a colour per team or Turn 1 writes before the offer is answered. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`references/style-guide.md`](../../references/style-guide.md) | One accent and colour never carrying meaning alone |
| [`references/types/process.md`](../../references/types/process.md) | Lanes |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-034
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/colour-every-team-restraint.md`

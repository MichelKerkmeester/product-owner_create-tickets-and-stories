---
title: "FJ-031 -- A revision replaces the diagram on its own board"
description: "This scenario validates a revision replaces the diagram on its own board for `FJ-031`. It checks that a change to a written flow deletes only the nodes the first write created after a yes, regenerates into the same file and leaves one diagram on the board."
version: 1.0.0.0
---

# FJ-031 -- A revision replaces the diagram on its own board

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-031`.

---

## 1. OVERVIEW

This scenario validates a revision replaces the diagram on its own board for `FJ-031`. It checks that a change to a written flow deletes only the nodes the first write created after a yes, regenerates into the same file and leaves one diagram on the board.

### Why This Matters

A second write beside the first duplicates the diagram, and a deletion beyond the write's own nodes destroys someone else's work. Both are invisible until the board is shared.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-031` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a change to a written flow deletes only the nodes the first write created after a yes, regenerates into the same file and leaves one diagram on the board
- Real user request: `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support`
- Prompt: `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support`
- Expected execution process: On the FJ-022 board, read it with get_figjam, ask before deleting the nodes the first write created, delete only those on the yes, regenerate with the same fileKey and read back
- Expected signals: The board holds one diagram, 9 of 9 nodes and 9 of 9 connectors, with Request an exception in place of Contact support. The delete waits for the yes, removes only the first write's nodes and connectors, the operator's sticky is untouched, and the regenerate call carries the same fileKey. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the operator's sticky is deleted or moved, a second diagram stands beside the first, or anything is deleted before the yes. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-031 | A revision replaces the diagram on its own board | Verify that a change to a written flow deletes only the nodes the first write created after a yes, regenerates into the same file and leaves one diagram on the board | `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `operator: complete FJ-022 to its written board in this session, then add one sticky of the operator's own beside it` -> 3. `user: submit the prompt exactly -> operator: confirm the reply reads the board and asks before deleting` -> 4. `user: Yes, delete and redraw it. -> operator: record the delete call, the generate_diagram call with its fileKey and the read-back` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts one diagram, 9 of 9 nodes and 9 of 9 connectors, with Request an exception in place of Contact support. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Request an exception. Q2: How many return flows does the board show? Answer: one. Q3: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the operator's sticky is deleted or moved, a second diagram stands beside the first, or anything is deleted before the yes. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `operator: complete FJ-022 to its written board in this session, then add one sticky of the operator's own beside it`
3. `user: submit the prompt exactly -> operator: confirm the reply reads the board and asks before deleting`
4. `user: Yes, delete and redraw it. -> operator: record the delete call, the generate_diagram call with its fileKey and the read-back`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts one diagram, 9 of 9 nodes and 9 of 9 connectors, with Request an exception in place of Contact support. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Request an exception. Q2: How many return flows does the board show? Answer: one. Q3: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the operator's sticky is deleted or moved, a second diagram stands beside the first, or anything is deleted before the yes. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Rollback on an existing board and the read-back mismatch recovery |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-031
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/revision-same-board.md`

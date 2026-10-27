---
title: "FJ-031 -- A revision replaces the diagram on its own board"
description: "This scenario validates a revision replaces the diagram on its own board for `FJ-031`. It checks that a change to a written flow composes the new board first, reads it back, then after its own yes deletes the old board section found by its tag and leaves one board in the file."
version: 1.0.3.0
---

# FJ-031 -- A revision replaces the diagram on its own board

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-031`.

---

## 1. OVERVIEW

This scenario validates a revision replaces the diagram on its own board for `FJ-031`. It checks that a change to a written flow composes the new board first, reads it back, then after its own yes deletes the old board section found by its tag and leaves one board in the file.

### Why This Matters

A second write beside the first duplicates the diagram, and a deletion beyond the write's own board section destroys someone else's work. Both are invisible until the board is shared.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-031` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a change to a written flow composes the new board first, reads it back, then after its own yes deletes the old board section found by its tag and leaves one board in the file
- Real user request: `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support`
- Prompt: `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support`
- Expected execution process: On the FJ-022 board, read it with get_figjam, open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any, then stop at the gate for the compose, compose the new board with the same fileKey on the gate's yes and read it back, ask before deleting the old board section, delete only the section found by its tag on that second yes and read back
- Expected signals: Turn 1 reads the board with get_figjam, ends on the playback and writes nothing. Turn 2 ends on the gate for the compose and writes nothing. Turn 3 composes the new board, reads it back, asks before deleting in a question that names the old board by its title and its write time and deletes nothing. Turn 4 deletes the old board section. The file ends with one board, every node of the model within 9 and every connector, with Request an exception in place of Contact support. The new board is composed and read back before anything is deleted. The gate's yes covers the compose and never the delete. The delete waits for its own yes, asked after the read-back. It removes only the old board section found by its tag. The operator's sticky is untouched and the compose call carries the same fileKey. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the operator's sticky is deleted or moved, a second board stands beside the new one after the delete, the old board is deleted before the new one is composed and read back, anything is deleted before the delete's own yes or anything is written before the gate's yes. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| FJ-031 | A revision replaces the diagram on its own board | Verify that a change to a written flow composes the new board first, reads it back, then after its own yes deletes the old board section found by its tag and leaves one board in the file | `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `operator: complete FJ-022 to its written board in this session, then add one sticky of the operator's own beside it` -> 3. `user: submit the prompt exactly -> operator: confirm the reply reads the board and is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 4. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, which names the new board first and the deletion of the old one second, with nothing written yet` -> 5. `user: Yes, go ahead. -> operator: record the compose call with its fileKey and the read-back, and confirm nothing is deleted and the reply asks before deleting the old board section` -> 6. `user: Yes, delete the old board. -> operator: record the delete call, confirm it targets the section found by its tag and read the file again` -> 7. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 8. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 9. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 10. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | Turn 1 reads the board with get_figjam, ends on the playback and writes nothing. Turn 2 ends on the gate for the compose and writes nothing. Turn 3 composes the new board, reads it back, asks before deleting in a question that names the old board by its title and its write time and deletes nothing. Turn 4 deletes the old board section. The read-back counts one board, every node of the model within 9 and every connector, with Request an exception in place of Contact support. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Request an exception. Q2: How many return flows does the board show? Answer: one. Q3: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the operator's sticky is deleted or moved, a second board stands beside the new one after the delete, the old board is deleted before the new one is composed and read back, anything is deleted before the delete's own yes or anything is written before the gate's yes. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `operator: complete FJ-022 to its written board in this session, then add one sticky of the operator's own beside it`
3. `user: submit the prompt exactly -> operator: confirm the reply reads the board and is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last`
4. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, which names the new board first and the deletion of the old one second, with nothing written yet`
5. `user: Yes, go ahead. -> operator: record the compose call with its fileKey and the read-back, and confirm nothing is deleted and the reply asks before deleting the old board section`
6. `user: Yes, delete the old board. -> operator: record the delete call, confirm it targets the section found by its tag and read the file again`
7. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
8. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
9. `operator: score the four Hygiene checks against the first and last read and score Reply`
10. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

Turn 1 reads the board with get_figjam, ends on the playback and writes nothing. Turn 2 ends on the gate for the compose and writes nothing. Turn 3 composes the new board, reads it back, asks before deleting in a question that names the old board by its title and its write time and deletes nothing. Turn 4 deletes the old board section. The read-back counts one board, every node of the model within 9 and every connector, with Request an exception in place of Contact support. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What does a customer see more than 30 days after delivery? Answer: Request an exception. Q2: How many return flows does the board show? Answer: one. Q3: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the operator's sticky is deleted or moved, a second board stands beside the new one after the delete, the old board is deleted before the new one is composed and read back, anything is deleted before the delete's own yes or anything is written before the gate's yes. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Rollback on an existing board, the compose-first revision and the read-back mismatch recovery |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-031
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/revision-same-board.md`

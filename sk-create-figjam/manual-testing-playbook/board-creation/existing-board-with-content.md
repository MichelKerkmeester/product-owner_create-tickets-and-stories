---
title: "FJ-032 -- A write onto a board with content"
description: "This scenario validates a write onto a board with content for `FJ-032`. It checks that a diagram written into an existing board lands clear of the content already there and changes none of it."
version: 1.0.0.0
---

# FJ-032 -- A write onto a board with content

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-032`.

---

## 1. OVERVIEW

This scenario validates a write onto a board with content for `FJ-032`. It checks that a diagram written into an existing board lands clear of the content already there and changes none of it.

### Why This Matters

Most real boards already hold workshop stickies. A diagram drawn over them, or a write that nudges them, damages work the requester did not own.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-032` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a diagram written into an existing board lands clear of the content already there and changes none of it
- Real user request: `$figjam add the Roamstay booking status lifecycle to our existing retro board <fileKey of the prepared board>. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Prompt: `$figjam add the Roamstay booking status lifecycle to our existing retro board <fileKey of the prepared board>. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Expected execution process: Read the named board first, gate naming that fileKey and a rollback limited to the nodes this write creates, write with the fileKey and read back the new diagram and the existing nodes
- Expected signals: The board holds every state and labelled transition of the model, and every node that was on the board before, at its old position. The prepared stickies and section keep their count, positions and sizes between the two reads, and the new diagram's bounds overlap none of them. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when a prepared node moves, changes or is covered, or the gate offers to delete the file as the rollback. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam add the Roamstay booking status lifecycle to our existing retro board <fileKey of the prepared board>. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-032 | A write onto a board with content | Verify that a diagram written into an existing board lands clear of the content already there and changes none of it | `$figjam add the Roamstay booking status lifecycle to our existing retro board <fileKey of the prepared board>. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `operator: prepare a FigJam board in the operator's plan with six stickies and a section, record its fileKey and read it with get_figjam` -> 3. `user: submit the prompt with the fileKey filled in -> operator: confirm the gate names that file and the scoped rollback` -> 4. `user: Yes, go ahead. -> operator: record the generate_diagram call and read the board again` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts every state and labelled transition of the model, and every node that was on the board before, at its old position. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which states end a booking? Answer: Completed, Cancelled and No-show. Q2: What moves a booking from Pending to Confirmed? Answer: the card is authorised. Q3: Is the retro content still readable? Answer: yes, nothing covers it. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when a prepared node moves, changes or is covered, or the gate offers to delete the file as the rollback. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `operator: prepare a FigJam board in the operator's plan with six stickies and a section, record its fileKey and read it with get_figjam`
3. `user: submit the prompt with the fileKey filled in -> operator: confirm the gate names that file and the scoped rollback`
4. `user: Yes, go ahead. -> operator: record the generate_diagram call and read the board again`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts every state and labelled transition of the model, and every node that was on the board before, at its old position. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which states end a booking? Answer: Completed, Cancelled and No-show. Q2: What moves a booking from Pending to Confirmed? Answer: the card is authorised. Q3: Is the retro content still readable? Answer: yes, nothing covers it. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when a prepared node moves, changes or is covered, or the gate offers to delete the file as the rollback. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Hosted route on an existing board and its rollback |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-032
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/existing-board-with-content.md`

---
title: "FJ-028 -- Gantt board quality"
description: "This scenario validates gantt board quality for `FJ-028`. It checks that a written gantt chart keeps task order, dependencies and the milestone readable, marks the critical task and lets a reader find the release date."
version: 1.0.4.0
---

# FJ-028 -- Gantt board quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-028`.

---

## 1. OVERVIEW

This scenario validates gantt board quality for `FJ-028`. It checks that a written gantt chart keeps task order, dependencies and the milestone readable, marks the critical task and lets a reader find the release date.

### Why This Matters

A launch plan is read for what blocks what and when it ships. The composer widens very short bars, so order and dependencies carry the meaning and must survive on the board.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-028` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written gantt chart keeps task order, dependencies and the milestone readable, marks the critical task and lets a reader find the release date
- Real user request: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November 2026 with two weeks of conflict-screen design, the sync engine takes three weeks from the same day, the conflict screen build follows its design for two weeks, and desktop and iOS integration starts when both builds are done, one week, and is the critical path. Then a two-week beta for 5 percent of workspaces and the release. Android follows in the next quarter, not yet approved. The plan also says: the conflict screen design covers the merge view and the undo banner, the platform team owns the sync engine, and integration covers desktop and iOS only.`
- Prompt: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November 2026 with two weeks of conflict-screen design, the sync engine takes three weeks from the same day, the conflict screen build follows its design for two weeks, and desktop and iOS integration starts when both builds are done, one week, and is the critical path. Then a two-week beta for 5 percent of workspaces and the release. Android follows in the next quarter, not yet approved. The plan also says: the conflict screen design covers the merge view and the undo banner, the platform team owns the sync engine, and integration covers desktop and iOS only.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any. Then pick the gantt type, model three sections with dependencies and the release milestone, mark integration critical, leave Android out by name, check, stop at the gate, write on its yes and read back
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 3 of 3 sections, 5 of 5 tasks and 1 of 1 milestone in the model's order. Integration carries the critical marking and the reply names Android under `Left out:`. Every `after` in the model is drawn as an arrow from the bar it names, and the reader reads order from the bars and the arrows, not the bar lengths. The board carries what the source excerpt says about each task in its name, its section or the subtitle, so a reader answers Q4 and Q5 from the board alone. The scorecard totals at least 20 of 24, with Composition, Fidelity, the four Hygiene checks, Reply and Substance at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November 2026 with two weeks of conflict-screen design, the sync engine takes three weeks from the same day, the conflict screen build follows its design for two weeks, and desktop and iOS integration starts when both builds are done, one week, and is the critical path. Then a two-week beta for 5 percent of workspaces and the release. Android follows in the next quarter, not yet approved. The plan also says: the conflict screen design covers the merge view and the undo banner, the platform team owns the sync engine, and integration covers desktop and iOS only.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-028 | Gantt board quality | Verify that a written gantt chart keeps task order, dependencies and the milestone readable, marks the critical task and lets a reader find the release date | `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November 2026 with two weeks of conflict-screen design, the sync engine takes three weeks from the same day, the conflict screen build follows its design for two weeks, and desktop and iOS integration starts when both builds are done, one week, and is the critical path. Then a two-week beta for 5 percent of workspaces and the release. Android follows in the next quarter, not yet approved. The plan also says: the conflict screen design covers the merge view and the undo banner, the platform team owns the sync engine, and integration covers desktop and iOS only.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q5 -> operator: score Clarity on Q1 to Q3 and Substance on Q4 and Q5, and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 3 of 3 sections, 5 of 5 tasks and 1 of 1 milestone in the model's order. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which task is on the critical path? Answer: Integration. Q2: What must finish before integration starts? Answer: the sync engine and the conflict screen build. Q3: When is the release? Answer: 21 December 2026, after the beta. Source questions for Substance: Q4: Which platforms does integration cover? Answer: desktop and iOS. Q5: Which team owns the sync engine? Answer: the platform team. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them
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

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts 3 of 3 sections, 5 of 5 tasks and 1 of 1 milestone in the model's order. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which task is on the critical path? Answer: Integration. Q2: What must finish before integration starts? Answer: the sync engine and the conflict screen build. Q3: When is the release? Answer: 21 December 2026, after the beta. Source questions for Substance: Q4: Which platforms does integration cover? Answer: desktop and iOS. Q5: Which team owns the sync engine? Answer: the platform team. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

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
| [`assets/examples/gantt-loomlist-offline.md`](../../assets/examples/gantt-loomlist-offline.md) | The model this request should produce |
| [`references/types/gantt.md`](../../references/types/gantt.md) | Gantt rules and read-back |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-028
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/gantt-board-quality.md`

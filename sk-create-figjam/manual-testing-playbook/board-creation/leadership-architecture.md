---
title: "FJ-033 -- An architecture written for leadership"
description: "This scenario validates an architecture written for leadership for `FJ-033`. It checks that the same system asked for a leadership audience lands with capability names and fewer parts than the engineering board, and a non-engineer reader answers its questions."
version: 1.0.0.0
---

# FJ-033 -- An architecture written for leadership

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-033`.

---

## 1. OVERVIEW

This scenario validates an architecture written for leadership for `FJ-033`. It checks that the same system asked for a leadership audience lands with capability names and fewer parts than the engineering board, and a non-engineer reader answers its questions.

### Why This Matters

Flow Mode sets an audience and a detail level at intake. A leadership board in component names fails its reader even when every count matches, and Simplified is the one level that collapses deployable units into capabilities.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-033` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the same system asked for a leadership audience lands with capability names and fewer parts than the engineering board, and a non-engineer reader answers its questions
- Real user request: `draw how Loomlist block sync works as a FigJam architecture diagram for the leadership update, on a new board in our Loomlist Product plan: desktop, web and iOS apps talk to our sync platform, which stores every change and wakes sleeping iPhones through Apple's push service.`
- Prompt: `draw how Loomlist block sync works as a FigJam architecture diagram for the leadership update, on a new board in our Loomlist Product plan: desktop, web and iOS apps talk to our sync platform, which stores every change and wakes sleeping iPhones through Apple's push service.`
- Expected execution process: Pick the architecture, set the audience to Executive and the detail level to Simplified, name parts as capabilities and drop infrastructure, check, gate, write with the layout code and read back
- Expected signals: The board holds at most 6 nodes in capability words, such as Apps, Sync platform and Apple Push, every connector of the model and its lanes. The reply or the gate names the Executive audience and the Simplified level, no label uses an internal service name such as sync-service or Push Worker, and the reader is told only that they are a non-engineer. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `draw how Loomlist block sync works as a FigJam architecture diagram for the leadership update, on a new board in our Loomlist Product plan: desktop, web and iOS apps talk to our sync platform, which stores every change and wakes sleeping iPhones through Apple's push service.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-033 | An architecture written for leadership | Verify that the same system asked for a leadership audience lands with capability names and fewer parts than the engineering board, and a non-engineer reader answers its questions | `draw how Loomlist block sync works as a FigJam architecture diagram for the leadership update, on a new board in our Loomlist Product plan: desktop, web and iOS apps talk to our sync platform, which stores every change and wakes sleeping iPhones through Apple's push service.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate` -> 3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 6. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The read-back counts at most 6 nodes in capability words, such as Apps, Sync platform and Apple Push, every connector of the model and its lanes. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which outside service does Loomlist depend on? Answer: Apple's push service. Q2: What do the apps talk to? Answer: the sync platform. Q3: What happens when something changes while an iPhone sleeps? Answer: Loomlist wakes it through Apple's push service. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a generated node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as generator behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the passing check and the gate`
3. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
4. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
5. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
6. `operator: score the four Hygiene checks against the first and last read and score Reply`
7. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The read-back counts at most 6 nodes in capability words, such as Apps, Sync platform and Apple Push, every connector of the model and its lanes. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which outside service does Loomlist depend on? Answer: Apple's push service. Q2: What do the apps talk to? Answer: the sync platform. Q3: What happens when something changes while an iPhone sleeps? Answer: Loomlist wakes it through Apple's push service. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Intake: the audience and the detail level |
| [`references/types/architecture.md`](../../references/types/architecture.md) | The deployable-unit rule Simplified collapses |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | Naming fits the audience |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-033
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/leadership-architecture.md`

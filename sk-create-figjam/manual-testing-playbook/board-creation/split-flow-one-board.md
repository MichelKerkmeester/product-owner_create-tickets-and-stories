---
title: "FJ-029 -- A flow over budget split into two boards in one file"
description: "This scenario validates a flow over budget split into two boards in one file for `FJ-029`. It checks that a request too long for one user flow becomes two composed boards in one file, the second composed into the first one's file, titled `1. Signup` and `2. Workspace setup`, placed left to right 400 pixels apart with no overlap and the reply naming the board to open first."
version: 1.0.1.0
---

# FJ-029 -- A flow over budget split into two boards in one file

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-029`.

---

## 1. OVERVIEW

This scenario validates a flow over budget split into two boards in one file for `FJ-029`. It checks that a request too long for one user flow becomes two composed boards in one file, the second composed into the first one's file, titled `1. Signup` and `2. Workspace setup`, placed left to right 400 pixels apart with no overlap and the reply naming the board to open first.

### Why This Matters

Splitting keeps each diagram readable, but two files or two boards with nothing marking where each one starts lose the thread between them. The second call must reuse the first call's file, and the composer places each new board 400 pixels to the right of the last, so the pair reads left to right the same way to every reader.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-029` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request too long for one user flow becomes two composed boards in one file, the second composed into the first one's file, titled `1. Signup` and `2. Workspace setup`, placed left to right 400 pixels apart with no overlap and the reply naming the board to open first
- Real user request: `$flow the Loomlist signup and first workspace setup on a new board in our Loomlist Product plan. From the onboarding doc: the landing page, sign up with email or Google, verify the email code, where a wrong code shows an error with a resend, pick a free or team plan, where a team plan asks for teammates' emails and lets you skip, name the workspace, pick a template or start blank, and the editor opens with a welcome tip.`
- Prompt: `$flow the Loomlist signup and first workspace setup on a new board in our Loomlist Product plan. From the onboarding doc: the landing page, sign up with email or Google, verify the email code, where a wrong code shows an error with a resend, pick a free or team plan, where a team plan asks for teammates' emails and lets you skip, name the workspace, pick a template or start blank, and the editor opens with a welcome tip.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after an intake round only when the run opens one. Then pick the user flow, find the request over 9 nodes, split it at the plan choice into Signup and Workspace setup, give each `%% title:` its ordinal, check both, stop at the gate naming two diagrams in one new file, compose the first on the gate's yes, pass its fileKey to the second and read both back
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The file holds two composed boards, Signup and Workspace setup, each within 9 nodes and titled `1. Signup` and `2. Workspace setup`, the second 400 pixels to the right of the first with its top level, with one shared hand-off label where the first ends and the second starts. The second `use_figma` call carries the first call's fileKey, the boards do not overlap and neither sits inside the other. Each title reads as its ordinal and the diagram's name. The read-back line names `start here: 1. Signup`, that one line counts both diagrams and `Left out:` names the split. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the second diagram lands in a new file, overlaps the first or sits inside it, a board title carries no ordinal or the boards do not read left to right in write order. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow the Loomlist signup and first workspace setup on a new board in our Loomlist Product plan. From the onboarding doc: the landing page, sign up with email or Google, verify the email code, where a wrong code shows an error with a resend, pick a free or team plan, where a team plan asks for teammates' emails and lets you skip, name the workspace, pick a template or start blank, and the editor opens with a welcome tip.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-029 | A flow over budget split into two boards in one file | Verify that a request too long for one user flow becomes two composed boards in one file, the second composed into the first one's file, titled `1. Signup` and `2. Workspace setup`, placed left to right 400 pixels apart with no overlap and the reply naming the board to open first | `$flow the Loomlist signup and first workspace setup on a new board in our Loomlist Product plan. From the onboarding doc: the landing page, sign up with email or Google, verify the email code, where a wrong code shows an error with a resend, pick a free or team plan, where a team plan asks for teammates' emails and lets you skip, name the workspace, pick a template or start blank, and the editor opens with a welcome tip.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts two boards, Signup and Workspace setup, each within 9 nodes and titled `1. Signup` and `2. Workspace setup`, the second 400 pixels to the right of the first, with one shared hand-off label where the first ends and the second starts. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What happens after a wrong verification code? Answer: an error with a resend. Q2: Can a team plan skip inviting teammates? Answer: yes. Q3: Which board does a reader open first? Answer: 1. Signup, the first of the two. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0. FAIL if any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the second diagram lands in a new file, overlaps the first or sits inside it, a board title carries no ordinal or the boards do not read left to right in write order. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet`
4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
7. `operator: score the four Hygiene checks against the first and last read and score Reply`
8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts two boards, Signup and Workspace setup, each within 9 nodes and titled `1. Signup` and `2. Workspace setup`, the second 400 pixels to the right of the first, with one shared hand-off label where the first ends and the second starts. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What happens after a wrong verification code? Answer: an error with a resend. Q2: Can a team plan skip inviting teammates? Answer: yes. Q3: Which board does a reader open first? Answer: 1. Signup, the first of the two. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks and no scored dimension scores 0
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. It also fails when the second diagram lands in a new file, overlaps the first or sits inside it, a board title carries no ordinal or the boards do not read left to right in write order. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | Budget and splitting |
| [`references/flow-mode.md`](../../references/flow-mode.md) | One file per work, the fileKey rule and the 400 pixel placement |
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | A board of several diagrams, Section 8 |

---

## 5. SOURCE METADATA

- Group: Board creation
- Playbook ID: FJ-029
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-creation/split-flow-one-board.md`

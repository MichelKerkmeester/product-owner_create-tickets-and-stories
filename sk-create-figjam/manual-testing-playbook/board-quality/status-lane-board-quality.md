---
title: "FJ-049 -- Status lane board quality"
description: "This scenario validates status lane board quality for `FJ-049`. It checks that a laned process with a status lane draws the record's statuses on top in order, moves each one with a dotted line from the step that changes it, carries the policy's detail on its steps at the Faithful level and puts the decision the request names in focus."
version: 1.0.0.0
---

# FJ-049 -- Status lane board quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-049`.

---

## 1. OVERVIEW

This scenario validates status lane board quality for `FJ-049`. It checks that a laned process with a status lane draws the record's statuses on top in order, moves each one with a dotted line from the step that changes it, carries the policy's detail on its steps at the Faithful level and puts the decision the request names in focus.

### Why This Matters

A reader of a shared record asks two things at once: who acts, and what state the record is in. A status lane answers the second on the same board, and a detail card keeps the rule a step follows next to the step.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-049` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a laned process with a status lane draws its statuses on top in order, moves each with a dotted line, carries detail cards at Faithful and puts the named decision in focus
- Real user request: `make a FigJam process of how a Roamstay damage claim moves between the hotel, the guest and Roamstay support, on a new board in our Roamstay Product plan, with the status the claim holds at each step, and keep the policy's detail on the steps. Highlight where the guest decides. From the claims policy: after check-out the hotel reports damage with photos and a repair quote, and the claim is Reported. Support sends the claim to the guest with the photos and the quote, and the claim is With the guest. The guest has 7 days to accept or dispute it. An accepted claim is charged to the card on file. A disputed claim is Under review while support reads the photos and the guest's reply and decides within 5 working days to uphold it, which charges the card, or to drop it. Either way the claim ends Closed. Claims under 25 euros are waived, a rule that is not yet live.`
- Prompt: `make a FigJam process of how a Roamstay damage claim moves between the hotel, the guest and Roamstay support, on a new board in our Roamstay Product plan, with the status the claim holds at each step, and keep the policy's detail on the steps. Highlight where the guest decides. From the claims policy: after check-out the hotel reports damage with photos and a repair quote, and the claim is Reported. Support sends the claim to the guest with the photos and the quote, and the claim is With the guest. The guest has 7 days to accept or dispute it. An accepted claim is charged to the card on file. A disputed claim is Under review while support reads the photos and the guest's reply and decides within 5 working days to uphold it, which charges the card, or to drop it. Either way the claim ends Closed. Claims under 25 euros are waived, a rule that is not yet live.`
- Expected execution process: Open with an intake round, since the prompt leaves the reader unstated, then the playback, which waits for its own yes and comes after the last intake round. Nothing is modelled or checked before the playback's answer. Then pick the process with a status lane declared first, four statuses in one `-->` chain, three actor lanes, a dotted `-.->` from each step that changes the status, `%% level: faithful` with `%% detail:` lines for the policy's rules, one `style` line on the guest's decision, the waiver left out by name, check, stop at the gate, compose on the gate's yes and read back
- Expected signals: The prompt leaves the reader unstated, so under the Standard energy rule in the root playbook Section 5 Turn 1 is an intake round that ends on its closing question, and no model is written and no check runs before the playback's answer, read from the tool stream. Turn 2 ends on the playback, which names the question, the outcome and the three dials, and writes nothing. Turn 3 ends on the gate and writes nothing. Turn 4 writes after the gate's yes. A further intake round moves the later turn numbers by one, as the root playbook Section 4 sets out. The status lane sits on top and holds Reported, With the guest, Under review and Closed as chevrons in that order, joined by the status line. Each status after the first is reached by a dotted line the key names Moves the status. Hotel, Guest and Roamstay support are lanes below it, each step in its lane, and both decisions have both exits labelled. At least the step that sends the claim and the step that reviews a dispute are detail cards, a one-line label over the policy's lines. The only mark is the guest's decision drawn in focus with the pink outline and named In focus in the key. Every count in the read-back matches the model. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `make a FigJam process of how a Roamstay damage claim moves between the hotel, the guest and Roamstay support, on a new board in our Roamstay Product plan, with the status the claim holds at each step, and keep the policy's detail on the steps. Highlight where the guest decides. From the claims policy: after check-out the hotel reports damage with photos and a repair quote, and the claim is Reported. Support sends the claim to the guest with the photos and the quote, and the claim is With the guest. The guest has 7 days to accept or dispute it. An accepted claim is charged to the card on file. A disputed claim is Under review while support reads the photos and the guest's reply and decides within 5 working days to uphold it, which charges the card, or to drop it. Either way the claim ends Closed. Claims under 25 euros are waived, a rule that is not yet live.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-049 | Status lane board quality | Verify that a laned process with a status lane draws its statuses on top in order, moves each with a dotted line, carries detail cards at Faithful and puts the named decision in focus | `make a FigJam process of how a Roamstay damage claim moves between the hotel, the guest and Roamstay support, on a new board in our Roamstay Product plan, with the status the claim holds at each step, and keep the policy's detail on the steps. Highlight where the guest decides. From the claims policy: after check-out the hotel reports damage with photos and a repair quote, and the claim is Reported. Support sends the claim to the guest with the photos and the quote, and the claim is With the guest. The guest has 7 days to accept or dispute it. An accepted claim is charged to the card on file. A disputed claim is Under review while support reads the photos and the guest's reply and decides within 5 working days to uphold it, which charges the card, or to drop it. Either way the claim ends Closed. Claims under 25 euros are waived, a rule that is not yet live.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is an intake round that ends on its closing question, with nothing modelled, checked or written` -> 3. `user: Use your recommended answers. -> operator: confirm the playback names the question, the outcome, the detail level, the audience and the distance, what each source settled and every assumed row, with nothing written` -> 4. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 5. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 6. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 7. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 8. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 9. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard` | The prompt leaves the reader unstated, so under the Standard energy rule in the root playbook Section 5 Turn 1 is an intake round that ends on its closing question, and no model is written and no check runs before the playback's answer, read from the tool stream. Turn 2 ends on the playback, which names the question, the outcome and the three dials, and writes nothing. Turn 3 ends on the gate and writes nothing. Turn 4 writes after the gate's yes. A further intake round moves the later turn numbers by one, as the root playbook Section 4 sets out. The read-back counts every node, connector, decision exit and lane of the model, the status lane among the lanes. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What status is the claim in while the guest decides? Answer: With the guest. Q2: Who decides a disputed claim? Answer: Roamstay support. Q3: How long does support take to decide? Answer: 5 working days. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is an intake round that ends on its closing question, with nothing modelled, checked or written`
3. `user: Use your recommended answers. -> operator: confirm the playback names the question, the outcome, the detail level, the audience and the distance, what each source settled and every assumed row, with nothing written`
4. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet`
5. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read`
6. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale`
7. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost`
8. `operator: score the four Hygiene checks against the first and last read and score Reply`
9. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q3 -> operator: score Clarity and total the scorecard`

### Expected

The prompt leaves the reader unstated, so under the Standard energy rule in the root playbook Section 5 Turn 1 is an intake round that ends on its closing question, and no model is written and no check runs before the playback's answer, read from the tool stream. Turn 2 ends on the playback, which names the question, the outcome and the three dials, and writes nothing. Turn 3 ends on the gate and writes nothing. Turn 4 writes after the gate's yes. A further intake round moves the later turn numbers by one, as the root playbook Section 4 sets out. The read-back counts every node, connector, decision exit and lane of the model, the status lane among the lanes. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: What status is the claim in while the guest decides? Answer: With the guest. Q2: Who decides a disputed claim? Answer: Roamstay support. Q3: How long does support take to decide? Answer: 5 working days. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 18 of 22, Composition, Fidelity, the four Hygiene checks and Reply score full marks, no scored dimension scores 0 and every expected signal is present
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 18. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`assets/examples/process-fernhouse-commission.md`](../../assets/examples/process-fernhouse-commission.md) | The board shape this request should produce, on another record |
| [`references/types/process.md`](../../references/types/process.md) | The status lane, detail cards, rules and read-back |
| [`references/style-guide.md`](../../references/style-guide.md) | The lane pair and what a `style` line means |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-049
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/status-lane-board-quality.md`

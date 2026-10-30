---
title: "FJ-026 -- State board quality"
description: "This scenario validates state board quality for `FJ-026`. It checks that a written state diagram has its end states drawn light gray by the composer, the Confirmed composite drawn as a named zone around its substates and every transition labelled, with no tint."
version: 1.0.4.0
---

# FJ-026 -- State board quality

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-026`.

---

## 1. OVERVIEW

This scenario validates state board quality for `FJ-026`. It checks that a written state diagram has its end states drawn light gray by the composer, the Confirmed composite drawn as a named zone around its substates and every transition labelled, with no tint.

### Why This Matters

Support reads a lifecycle to answer where a booking can go next. An end state that does not stand apart, or a composite that does not show which substates it holds, hides the answers the colour and the grouping are there for.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-026` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a written state diagram has its end states drawn light gray by the composer, the Confirmed composite drawn as a named zone around its substates and every transition labelled, with no tint
- Real user request: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in. The booking doc also says: a booking stays Pending at most 15 minutes while the card is checked. While Upcoming the guest can still change dates, and while In stay the hotel can add charges to the room. A cancel within 48 hours of check-in keeps the first night's price. The hotel can mark a No-show from 6 hours after the check-in time.`
- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in. The booking doc also says: a booking stays Pending at most 15 minutes while the card is checked. While Upcoming the guest can still change dates, and while In stay the hotel can add charges to the room. A cancel within 48 hours of check-in keeps the first night's price. The hotel can mark a No-show from 6 hours after the check-in time.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any. Then pick the state type, model the composite Confirmed state, check, stop at the gate naming one composed board and no extension, compose with one `use_figma` call on the gate's yes and read back
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds every state of the model, every transition with its label and the Confirmed composite as a named zone around Upcoming and InStay. Completed, Cancelled and NoShow are light gray, as the key's Final state entry says. No tint sits behind them. No extension call is made and the reply carries no `Extensions:` line. Where the source excerpt says what holds in a state, the board carries it at the Balanced or Faithful level in a detail card under the state's label, so a reader answers Q4 and Q5 from the board alone. The scorecard totals at least 20 of 24, with Composition, Fidelity, the four Hygiene checks, Reply and Substance at full marks and no scored dimension at 0
- Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured
- Pass/fail: PASS if the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. It also fails when an extension call is made or a tint sits behind an end state. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in. The booking doc also says: a booking stays Pending at most 15 minutes while the card is checked. While Upcoming the guest can still change dates, and while In stay the hotel can add charges to the room. A cancel within 48 hours of check-in keeps the first night's price. The hotel can mark a No-show from 6 hours after the check-in time.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-026 | State board quality | Verify that a written state diagram has its end states drawn light gray by the composer, the Confirmed composite drawn as a named zone around its substates and every transition labelled, with no tint | `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in. The booking doc also says: a booking stays Pending at most 15 minutes while the card is checked. While Upcoming the guest can still change dates, and while In stay the hotel can add charges to the room. A cancel within 48 hours of check-in keeps the first night's price. The hotel can mark a No-show from 6 hours after the check-in time.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: record the reply, every tool call and each get_figjam read` -> 5. `operator: write down the glance order the model plans, then screenshot the whole board and the diagram at 100% zoom and copy the reading one in greyscale` -> 6. `operator: score Composition, Crossings, Shared trunks, Label collisions, Fidelity, Legibility and Signal, and name a location and a fix for each point lost` -> 7. `operator: score the four Hygiene checks against the first and last read and score Reply` -> 8. `reader: give a fresh reader the two colour screenshots and ask Q1 to Q5 -> operator: score Clarity on Q1 to Q3 and Substance on Q4 and Q5, and total the scorecard` | Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts every state of the model, every transition with its label and the Confirmed composite as a named zone around Upcoming and InStay, with Completed, Cancelled and NoShow in light gray and no tint behind them. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which states end a booking? Answer: Completed, Cancelled and No-show. Q2: From which states can a guest cancel? Answer: Pending and Confirmed. Q3: What moves a booking from Upcoming to In stay? Answer: check in. Source questions for Substance: Q4: What can a guest still do while a booking is Upcoming? Answer: change the dates. Q5: When can the hotel mark a No-show? Answer: from 6 hours after the check-in time. Every score is recorded with the evidence that set it, and every point lost names its location and its fix | Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score | PASS if the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present. FAIL if an expected signal is missing, any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. It also fails when an extension call is made or a tint sits behind an end state. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When Fidelity or Reply lost points, compare the model, the read-back and the reply line by line against `references/flow-mode.md` Sections 7 and 8 2. When Composition lost points, compare the overview with the planned glance order and name the part that arrives early or late 3. When Crossings, Shared trunks, Label collisions or Legibility lost points, check whether the model caused it, such as declaration order or a long label, before recording it as composer behavior 4. When Clarity lost points, name the question the reader missed and the node or label that misled them
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

Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The read-back counts every state of the model, every transition with its label and the Confirmed composite as a named zone around Upcoming and InStay, with Completed, Cancelled and NoShow in light gray and no tint behind them. The overview reads in the planned glance order. The reader answers from the two colour screenshots. Q1: Which states end a booking? Answer: Completed, Cancelled and No-show. Q2: From which states can a guest cancel? Answer: Pending and Confirmed. Q3: What moves a booking from Upcoming to In stay? Answer: check in. Source questions for Substance: Q4: What can a guest still do while a booking is Upcoming? Answer: change the dates. Q5: When can the hotel mark a No-show? Answer: from 6 hours after the check-in time. Every score is recorded with the evidence that set it, and every point lost names its location and its fix

### Evidence

Every reply, every tool call with its arguments, each get_figjam read, the planned glance order, the overview screenshot, the reading and greyscale screenshots, the reader's answers and the scorecard with one reason, one location and one fix per score

### Pass / Fail

- **Pass**: the board quality scorecard in the root playbook Section 3 totals at least 20 of 24, Composition, Fidelity, the four Hygiene checks, Reply and Substance score full marks, no scored dimension scores 0 and every expected signal is present
- **Fail**: any count differs from the model, a composed node moved, the reply misstates a count, a dimension scores 0, a point lost names no location or no fix or the total is under 20. It also fails when an extension call is made or a tint sits behind an end state. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| [`assets/examples/state-roamstay-booking.md`](../../assets/examples/state-roamstay-booking.md) | The model this request should produce |
| [`references/types/state.md`](../../references/types/state.md) | State rules, zones and read-back |
| [`references/style-guide.md`](../../references/style-guide.md) | The kinds the composer colours, including the Final state |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-026
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/state-board-quality.md`

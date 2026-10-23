---
title: "FJ-017 -- A status tint lands after the write"
description: "This scenario validates a status tint lands after the write for `FJ-017`. It checks that after a yes that named a tint, the state diagram is written, the tint is added through `use_figma` behind the end states, and the reply carries an `Extensions:` line."
version: 1.0.0.0
---

# FJ-017 -- A status tint lands after the write

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-017`.

---

## 1. OVERVIEW

This scenario validates a status tint lands after the write for `FJ-017`. It checks that after a yes that named a tint, the state diagram is written, the tint is added through `use_figma` behind the end states, and the reply carries an `Extensions:` line.

### Why This Matters

An extension is a second write onto a shared board. It must add beside the generated nodes, never move or restyle them, and the reply must prove what it added.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-017` and confirm the expected signals without contradictory evidence.

- Objective: Verify that after a yes that named a tint, the state diagram is written, the tint is added through `use_figma` behind the end states, and the reply carries an `Extensions:` line
- Real user request: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Expected execution process: Run Turn 1 as `FJ-007`, then on the yes call `generate_diagram`, add one tint rectangle behind Completed, Cancelled and NoShow through `use_figma` with `insertChild(0)`, read the board back and reply
- Expected signals: Turn 2 calls `generate_diagram` once and `use_figma` once, moves no generated node, and replies with the board URL, a `Read-back:` line, `Extensions: 1 of 1 status tint, 0 overlaps` and the `HVR self-scan:` line
- Desired user-visible outcome: A board with the end states tinted and both writes counted
- Pass/fail: PASS if the tint lands behind the three end states, no generated node moved, and the reply counts the extension. FAIL if a generated node is moved or restyled, the tint covers a node, or the reply has no `Extensions:` line. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-017 | A status tint lands after the write | Verify that after a yes that named a tint, the state diagram is written, the tint is added through `use_figma` behind the end states, and the reply carries an `Extensions:` line | `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.` | 1. `sandbox: confirm the hosted Figma MCP is connected -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the gate names the tint` -> 3. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and confirm the tint sits behind the three end states` | Step 2 finds the gate naming the tint. Step 3 finds the two writes, an `Extensions:` line and a tint behind the three end states with no generated node moved | Both replies, the `use_figma` code, the board URL and a screenshot of the tinted states | PASS if the tint lands behind the three end states, no generated node moved, and the reply counts the extension. FAIL if a generated node is moved or restyled, the tint covers a node, or the reply has no `Extensions:` line. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. Check the status tint recipe in `references/hybrid-workflow.md` Section 3 2. Check the read-back line in `references/hybrid-workflow.md` Section 6 |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the gate names the tint`
3. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and confirm the tint sits behind the three end states`

### Expected

Step 2 finds the gate naming the tint. Step 3 finds the two writes, an `Extensions:` line and a tint behind the three end states with no generated node moved

### Evidence

Both replies, the `use_figma` code, the board URL and a screenshot of the tinted states

### Pass / Fail

- **Pass**: the tint lands behind the three end states, no generated node moved, and the reply counts the extension
- **Fail**: a generated node is moved or restyled, the tint covers a node, or the reply has no `Extensions:` line. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the status tint recipe in `references/hybrid-workflow.md` Section 3
2. Check the read-back line in `references/hybrid-workflow.md` Section 6

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
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | Recipes, gate and read-back |
| [`assets/examples/state-roamstay-booking.md`](../../assets/examples/state-roamstay-booking.md) | Worked example |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-017
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/hybrid-extension-written.md`

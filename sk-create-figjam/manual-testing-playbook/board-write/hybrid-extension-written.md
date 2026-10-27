---
title: "FJ-017 -- Notes land after the write"
description: "This scenario validates notes land after the write for `FJ-017`. It checks that after a yes that named notes, the state diagram is composed with one `use_figma` call and the notes are added with a second `use_figma` call inside the board as single stickies, no composed node moves and the reply carries an `Extensions:` line."
version: 1.0.3.0
driver: new-file
---

# FJ-017 -- Notes land after the write

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-017`.

---

## 1. OVERVIEW

This scenario validates notes land after the write for `FJ-017`. It checks that after a yes that named notes, the state diagram is composed with one `use_figma` call and the notes are added with a second `use_figma` call inside the board as single stickies, no composed node moves and the reply carries an `Extensions:` line.

### Why This Matters

An extension is a second write onto a shared board. It must add beside the composed nodes, never move or restyle them, and the reply must prove what it added.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-017` and confirm the expected signals without contradictory evidence.

- Objective: Verify that after a yes that named notes, the state diagram is composed with one `use_figma` call and the notes are added with a second `use_figma` call inside the board as single stickies, no composed node moves and the reply carries an `Extensions:` line
- Real user request: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Expected execution process: Run Turns 1 and 2 as `FJ-007` to reach the gate, then on the gate's yes call `whoami` and `create_new_file`, compose the board with one `use_figma` call, add one sticky beside Cancelled and one beside NoShow with a second `use_figma` call inside the board, read the board back and reply
- Expected signals: Turn 1 ends on the playback and Turn 2 ends on the gate, and both write nothing. Turn 3 calls `use_figma` twice, once to compose the board and once to add the two notes as single stickies, with no pin and no legend column. It moves no composed node, draws no colour and replies with the board URL, a `Read-back:` line, `Extensions: 2 of 2 notes, 0 overlaps`, a `Finding:` line naming any sticky that sits below or left of its node and the `HVR self-scan:` line
- Desired user-visible outcome: A board with a note beside Cancelled and beside NoShow and both writes counted
- Pass/fail: PASS if each sticky lands inside the board beside its node, no composed node moved and the reply counts the extension. FAIL if a write precedes the gate's yes, a composed node is moved or restyled, a sticky covers a node or lands outside the board, the notes land as pins with a legend column or the reply has no `Extensions:` line. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-017 | Notes land after the write | Verify that after a yes that named notes, the state diagram is composed with one `use_figma` call and the notes are added with a second `use_figma` call inside the board as single stickies, no composed node moves and the reply carries an `Extensions:` line | `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.` | 1. `sandbox: confirm the hosted Figma MCP is connected -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 3. `user: Yes, that reading is right. -> operator: confirm the gate names the notes and that nothing is written yet` -> 4. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and confirm each sticky stands inside the board beside Cancelled and NoShow` | Step 2 finds the playback and no write. Step 3 finds the gate naming the notes and no write. Step 4 finds the two `use_figma` writes, an `Extensions: 2 of 2 notes, 0 overlaps` line and a single sticky beside each of the two end states, with no pin, no legend column and no composed node moved | All three replies, the code of both `use_figma` calls, the board URL and a screenshot of the notes | PASS if each sticky lands inside the board beside its node, no composed node moved and the reply counts the extension. FAIL if a write precedes the gate's yes, a composed node is moved or restyled, a sticky covers a node or lands outside the board, the notes land as pins with a legend column or the reply has no `Extensions:` line. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. Check the single sticky recipe in `references/hybrid-workflow.md` Section 3 2. Check the read-back line in `references/hybrid-workflow.md` Section 6 |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
3. `user: Yes, that reading is right. -> operator: confirm the gate names the notes and that nothing is written yet`
4. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and confirm each sticky stands inside the board beside Cancelled and NoShow`

### Expected

Step 2 finds the playback and no write. Step 3 finds the gate naming the notes and no write. Step 4 finds the two `use_figma` writes, an `Extensions: 2 of 2 notes, 0 overlaps` line and a single sticky beside each of the two end states, with no pin, no legend column and no composed node moved

### Evidence

All three replies, the code of both `use_figma` calls, the board URL and a screenshot of the notes

### Pass / Fail

- **Pass**: each sticky lands inside the board beside its node, no composed node moved and the reply counts the extension
- **Fail**: a write precedes the gate's yes, a composed node is moved or restyled, a sticky covers a node or lands outside the board, the notes land as pins with a legend column or the reply has no `Extensions:` line. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the single sticky recipe in `references/hybrid-workflow.md` Section 3
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

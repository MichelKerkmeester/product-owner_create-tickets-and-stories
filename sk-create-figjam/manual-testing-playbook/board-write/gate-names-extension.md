---
title: "FJ-007 -- The gate names a planned extension"
description: "This scenario validates the gate names a planned extension for `FJ-007`. It checks that a state diagram request that asks for notes the model cannot carry ends on a gate that names the notes as an extension, before any write."
version: 1.0.2.0
---

# FJ-007 -- The gate names a planned extension

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-007`.

---

## 1. OVERVIEW

This scenario validates the gate names a planned extension for `FJ-007`. It checks that a state diagram request that asks for notes the model cannot carry ends on a gate that names the notes as an extension, before any write.

### Why This Matters

A state model cannot put a note on a state, so the notes are a second write through `use_figma`. A yes that did not cover them does not cover that write. The end states need no write at all, because the composer already draws them light gray and names them Final state in the key.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-007` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a state diagram request that asks for notes the model cannot carry ends on a gate that names the notes as an extension, before any write
- Real user request: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any. Then pick the state type, load its reference, template and the style guide, write the model, pass the check, plan two single stickies through the hybrid workflow and end on a gate that names the diagram and the notes
- Expected signals: Turn 1 ends on the playback and writes nothing. After the playback's yes, the model's header is `stateDiagram-v2` with no styling and the check passes. Turn 2 ends on the gate, which names the plan, a new file, the composed state diagram, two single-sticky notes on Cancelled and NoShow, the calls the write will spend and the rollback, then waits. The gate plans no colour step, because the composer already draws the end states light gray and names them Final state in the key. No write tool is called
- Desired user-visible outcome: A checked state model and a gate that names both writes
- Pass/fail: PASS if the run stops at the playback first and the gate that follows the playback's yes names the state diagram and the notes and waits, the model passes and has no styling, and nothing is written. FAIL if the model sets colour with `classDef` or `style`, the gate leaves the notes out, the gate plans a colour step for the end states or a write tool is called

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
| FJ-007 | The gate names a planned extension | Verify that a state diagram request that asks for notes the model cannot carry ends on a gate that names the notes as an extension, before any write | `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 2. `user: Yes, that reading is right. -> operator: confirm the reply is the gate naming the notes and that nothing is written` -> 3. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md` | Step 1 returns the playback and writes nothing. Step 2 returns the gate naming the extension. Step 3 prints `diagram 1, state: ok` with exit 0 | Both replies, the tool calls with every check run and the operator's own check run | PASS if the run stops at the playback first and the gate that follows the playback's yes names the state diagram and the notes and waits, the model passes and has no styling, and nothing is written. FAIL if the model sets colour with `classDef` or `style`, the gate leaves the notes out, the gate plans a colour step for the end states or a write tool is called | 1. Check `references/types/state.md` Section 5 and `references/hybrid-workflow.md` Section 1 2. Check the gate against `references/flow-mode.md` Section 2 step 7 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last`
2. `user: Yes, that reading is right. -> operator: confirm the reply is the gate naming the notes and that nothing is written`
3. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md`

### Expected

Step 1 returns the playback and writes nothing. Step 2 returns the gate naming the extension. Step 3 prints `diagram 1, state: ok` with exit 0

### Evidence

Both replies, the tool calls with every check run and the operator's own check run

### Pass / Fail

- **Pass**: the run stops at the playback first and the gate that follows the playback's yes names the state diagram and the notes and waits, the model passes and has no styling, and nothing is written
- **Fail**: the model sets colour with `classDef` or `style`, the gate leaves the notes out, the gate plans a colour step for the end states or a write tool is called

### Failure Triage

1. Check `references/types/state.md` Section 5 and `references/hybrid-workflow.md` Section 1
2. Check the gate against `references/flow-mode.md` Section 2 step 7

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
| [`references/types/state.md`](../../references/types/state.md) | State rules, colour and notes |
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | When to extend and the single sticky recipe, Sections 1 and 3 |
| [`references/style-guide.md`](../../references/style-guide.md) | The kinds the composer colours, including the Final state, Section 2 |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-007
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/gate-names-extension.md`

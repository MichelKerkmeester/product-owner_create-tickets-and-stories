---
title: "FJ-008 -- A written ER diagram is read back"
description: "This scenario validates a written ER diagram is read back for `FJ-008`. It checks that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts."
version: 1.0.3.0
driver: new-file
---

# FJ-008 -- A written ER diagram is read back

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-008`.

---

## 1. OVERVIEW

This scenario validates a written ER diagram is read back for `FJ-008`. It checks that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts.

### Why This Matters

A board URL alone proves nothing about what the composer drew. The read-back is the only proof that every entity and relationship landed.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-008` and confirm the expected signals without contradictory evidence.

- Objective: Verify that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts
- Real user request: `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.`
- Prompt: `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after the intake rounds the run opens, if any. Then pick the ER type, model and check it, stop at the gate, then on the gate's yes call `whoami` and `create_new_file`, compose the board with one `use_figma` call, read it with `get_figjam` on the returned board id and reply with the URL, the read-back line and the self-scan line
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 calls `whoami`, `create_new_file`, one `use_figma` and one `get_figjam`, and replies with the board URL first, a `Read-back:` line counting entities, relationships and attributes, and the `HVR self-scan:` line
- Desired user-visible outcome: A board link with counts measured on the board
- Pass/fail: PASS if the board holds every entity and relationship of the model and the reply's read-back counts match the board. FAIL if the write happens before the gate's yes, the read-back line is missing or does not match the board, or the reply calls a mismatched board done. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-008 | A written ER diagram is read back | Verify that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts | `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.` | 1. `sandbox: confirm the hosted Figma MCP is connected and record the tool list -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last` -> 3. `user: Yes, that reading is right. -> operator: confirm the gate and the passing check, with nothing written yet` -> 4. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and count entities and relationships by hand` | Step 2 finds the playback and no write. Step 3 finds the gate and a passing check. Step 4 finds one `use_figma` call that carries the composer's code, a read-back by `get_figjam` on the returned board id and counts that match the operator's own count | All three replies, the tool calls, the board URL and the operator's count | PASS if the board holds every entity and relationship of the model and the reply's read-back counts match the board. FAIL if the write happens before the gate's yes, the read-back line is missing or does not match the board, or the reply calls a mismatched board done. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. Check the composed route in `references/flow-mode.md` Section 6 and the read-back in Section 7 2. Check `references/types/er.md` Section 7 for what the ER read-back counts |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected and record the tool list -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens intake rounds first, answer each with the recommended answers and confirm the playback follows the last`
3. `user: Yes, that reading is right. -> operator: confirm the gate and the passing check, with nothing written yet`
4. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and count entities and relationships by hand`

### Expected

Step 2 finds the playback and no write. Step 3 finds the gate and a passing check. Step 4 finds one `use_figma` call that carries the composer's code, a read-back by `get_figjam` on the returned board id and counts that match the operator's own count

### Evidence

All three replies, the tool calls, the board URL and the operator's count

### Pass / Fail

- **Pass**: the board holds every entity and relationship of the model and the reply's read-back counts match the board
- **Fail**: the write happens before the gate's yes, the read-back line is missing or does not match the board, or the reply calls a mismatched board done. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the composed route in `references/flow-mode.md` Section 6 and the read-back in Section 7
2. Check `references/types/er.md` Section 7 for what the ER read-back counts

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Write routes, read-back and delivery |
| [`references/types/er.md`](../../references/types/er.md) | ER read-back |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-008
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/write-and-read-back.md`

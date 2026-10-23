---
title: "FJ-008 -- A written ER diagram is read back"
description: "This scenario validates a written ER diagram is read back for `FJ-008`. It checks that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts."
version: 1.0.0.0
---

# FJ-008 -- A written ER diagram is read back

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-008`.

---

## 1. OVERVIEW

This scenario validates a written ER diagram is read back for `FJ-008`. It checks that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts.

### Why This Matters

A board URL alone proves nothing about what the generator drew. The read-back is the only proof that every entity and relationship landed.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-008` and confirm the expected signals without contradictory evidence.

- Objective: Verify that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts
- Real user request: `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.`
- Prompt: `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.`
- Expected execution process: Pick the ER type, model and check it, gate, then on the yes call `generate_diagram`, read the board with `get_figjam` node by node and reply with the URL, the read-back line and the self-scan line
- Expected signals: Turn 1 ends on the gate. Turn 2 calls `generate_diagram` once, reads the board back, and replies with the board URL first, a `Read-back:` line counting entities, relationships and attributes, and the `HVR self-scan:` line
- Desired user-visible outcome: A board link with counts measured on the board
- Pass/fail: PASS if the board holds every entity and relationship of the model and the reply's read-back counts match the board. FAIL if the write happens before the yes, the read-back line is missing or does not match the board, or the reply calls a mismatched board done. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| FJ-008 | A written ER diagram is read back | Verify that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts | `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.` | 1. `sandbox: confirm the hosted Figma MCP is connected and record the tool list -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the gate and the passing check` -> 3. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and count entities and relationships by hand` | Step 2 finds the gate and a passing check. Step 3 finds one `generate_diagram` call, a read-back by `get_figjam`, and counts that match the operator's own count | Both replies, the tool calls, the board URL and the operator's count | PASS if the board holds every entity and relationship of the model and the reply's read-back counts match the board. FAIL if the write happens before the yes, the read-back line is missing or does not match the board, or the reply calls a mismatched board done. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. Check the hosted route in `references/flow-mode.md` Section 6 and the read-back in Section 7 2. Check `references/types/er.md` Section 7 for what the ER read-back counts |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected and record the tool list -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the gate and the passing check`
3. `user: Yes, go ahead. -> operator: read the reply and tool calls, open the board and count entities and relationships by hand`

### Expected

Step 2 finds the gate and a passing check. Step 3 finds one `generate_diagram` call, a read-back by `get_figjam`, and counts that match the operator's own count

### Evidence

Both replies, the tool calls, the board URL and the operator's count

### Pass / Fail

- **Pass**: the board holds every entity and relationship of the model and the reply's read-back counts match the board
- **Fail**: the write happens before the yes, the read-back line is missing or does not match the board, or the reply calls a mismatched board done. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the hosted route in `references/flow-mode.md` Section 6 and the read-back in Section 7
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

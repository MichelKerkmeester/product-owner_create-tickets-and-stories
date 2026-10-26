---
title: "FJ-019 -- An architecture composed in its six lanes"
description: "This scenario validates an architecture composed in its six lanes for `FJ-019`. It checks that with the hosted Figma MCP connected, one `use_figma` call composes the architecture with its lanes as columns and the read-back counts its lanes."
version: 1.0.2.0
driver: new-file
---

# FJ-019 -- An architecture composed in its six lanes

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-019`.

---

## 1. OVERVIEW

This scenario validates an architecture composed in its six lanes for `FJ-019`. It checks that with the hosted Figma MCP connected, one `use_figma` call composes the architecture with its lanes as columns and the read-back counts its lanes.

### Why This Matters

The lane decides each part's column and colour, so a part in the wrong lane tells the reader the wrong thing. A composed board is fixed by reshaping the model and composing again, never by dragging a node.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-019` and confirm the expected signals without contradictory evidence.

- Objective: Verify that with the hosted Figma MCP connected, one `use_figma` call composes the architecture with its lanes as columns and the read-back counts its lanes
- Real user request: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`
- Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`
- Expected execution process: Open with one intake round, because the prompt names the parts and no calls between them, then the playback and then the gate. The checked model is the one `FJ-012` sets out. On the gate's yes call `whoami` and `create_new_file`, compose the board with one `use_figma` call, read it with `get_figjam` and reply
- Expected signals: Turn 1 writes nothing and ends on an intake round that asks for the calls between the parts with a recommended answer for each. Turn 2 ends on the playback and writes nothing. Turn 3 ends on the gate and writes nothing. Turn 4 writes after the gate's yes. The one `use_figma` call carries the code `compose_board.py` printed. The board holds six lane sections as columns, left to right as client, gateway, service, async, datastore and external, with each part inside its lane. The reply's `Read-back:` line counts nodes, connectors and lanes. When `use_figma` is not connected and the generated fallback runs, its one `generate_diagram` call also carries `useArchitectureLayoutCode: "FIGMA_DIAGRAM_2026"`, which is recorded as a secondary signal
- Desired user-visible outcome: An architecture board in lanes with counts measured on it
- Pass/fail: PASS if one `use_figma` call composes the board, each part sits in its lane as a column and the counts match. FAIL if a write precedes the gate's yes, the board is drawn by another route while `use_figma` is connected, a part sits in the wrong lane or the counts do not match. On the generated fallback a missing layout code is a secondary finding and the lane counts decide the verdict. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-019 | An architecture composed in its six lanes | Verify that with the hosted Figma MCP connected, one `use_figma` call composes the architecture with its lanes as columns and the read-back counts its lanes | `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service` | 1. `sandbox: confirm the hosted Figma MCP is connected with use_figma among its tools -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is an intake round that asks for the calls between the parts, gives a recommended answer for each and writes nothing` -> 3. `user: Use your recommended answers. -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written` -> 4. `user: Yes, that reading is right. -> operator: confirm the gate and that nothing is written yet` -> 5. `user: Yes, go ahead. -> operator: read the call arguments and the reply, and count lanes on the board` | Step 2 finds the intake round and no write. Step 3 finds the playback and no write. Step 4 finds the gate and no write. Step 5 finds one `use_figma` call and lane counts that match the board | All four replies, the call arguments, the `get_figjam` read and the board URL | PASS if one `use_figma` call composes the board, each part sits in its lane as a column and the counts match. FAIL if a write precedes the gate's yes, the board is drawn by another route while `use_figma` is connected, a part sits in the wrong lane or the counts do not match. On the generated fallback a missing layout code is a secondary finding and the lane counts decide the verdict. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. Check the composed route in `references/flow-mode.md` Section 6 2. Check `references/types/architecture.md` Sections 6 and 7 |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected with use_figma among its tools -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is an intake round that asks for the calls between the parts, gives a recommended answer for each and writes nothing`
3. `user: Use your recommended answers. -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written`
4. `user: Yes, that reading is right. -> operator: confirm the gate and that nothing is written yet`
5. `user: Yes, go ahead. -> operator: read the call arguments and the reply, and count lanes on the board`

### Expected

Step 2 finds the intake round and no write. Step 3 finds the playback and no write. Step 4 finds the gate and no write. Step 5 finds one `use_figma` call and lane counts that match the board

### Evidence

All four replies, the call arguments, the `get_figjam` read and the board URL

### Pass / Fail

- **Pass**: one `use_figma` call composes the board, each part sits in its lane as a column and the counts match
- **Fail**: a write precedes the gate's yes, the board is drawn by another route while `use_figma` is connected, a part sits in the wrong lane or the counts do not match. On the generated fallback a missing layout code is a secondary finding and the lane counts decide the verdict. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the composed route in `references/flow-mode.md` Section 6
2. Check `references/types/architecture.md` Sections 6 and 7

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
| [`references/types/architecture.md`](../../references/types/architecture.md) | Writing the board and read-back |
| [`references/flow-mode.md`](../../references/flow-mode.md) | The composed route and the generated fallback |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-019
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/architecture-write-lanes.md`

---
title: "FJ-019 -- An architecture written with its layout code"
description: "This scenario validates an architecture written with its layout code for `FJ-019`. It checks that with the hosted Figma MCP connected, the architecture call passes `useArchitectureLayoutCode` and the read-back counts its lanes."
version: 1.0.0.0
---

# FJ-019 -- An architecture written with its layout code

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-019`.

---

## 1. OVERVIEW

This scenario validates an architecture written with its layout code for `FJ-019`. It checks that with the hosted Figma MCP connected, the architecture call passes `useArchitectureLayoutCode` and the read-back counts its lanes.

### Why This Matters

The layout code is what places each part in its lane. A call without it draws a tangle the reader cannot fix, because generated nodes are never moved.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-019` and confirm the expected signals without contradictory evidence.

- Objective: Verify that with the hosted Figma MCP connected, the architecture call passes `useArchitectureLayoutCode` and the read-back counts its lanes
- Real user request: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`
- Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`
- Expected execution process: Run Turn 1 as `FJ-012`, then on the yes call `generate_diagram` with `useArchitectureLayoutCode` set to `FIGMA_DIAGRAM_2026`, read the board back and reply
- Expected signals: The one `generate_diagram` call carries `useArchitectureLayoutCode: "FIGMA_DIAGRAM_2026"`, and the reply's `Read-back:` line counts nodes, connectors and lanes
- Desired user-visible outcome: An architecture board in lanes with counts measured on it
- Pass/fail: PASS if the call passes the layout code, each part sits in its lane and the counts match. FAIL if the layout code is missing, a part sits in the wrong lane, or the counts do not match. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

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
| FJ-019 | An architecture written with its layout code | Verify that with the hosted Figma MCP connected, the architecture call passes `useArchitectureLayoutCode` and the read-back counts its lanes | `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service` | 1. `sandbox: confirm the hosted Figma MCP is connected -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the gate` -> 3. `user: Yes, go ahead. -> operator: read the call arguments and the reply, and count lanes on the board` | Step 3 finds the layout code in the call and lane counts that match the board | Both replies, the call arguments and the board URL | PASS if the call passes the layout code, each part sits in its lane and the counts match. FAIL if the layout code is missing, a part sits in the wrong lane, or the counts do not match. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. Check the hosted route in `references/flow-mode.md` Section 6 2. Check `references/types/architecture.md` Sections 6 and 7 |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the gate`
3. `user: Yes, go ahead. -> operator: read the call arguments and the reply, and count lanes on the board`

### Expected

Step 3 finds the layout code in the call and lane counts that match the board

### Evidence

Both replies, the call arguments and the board URL

### Pass / Fail

- **Pass**: the call passes the layout code, each part sits in its lane and the counts match
- **Fail**: the layout code is missing, a part sits in the wrong lane, or the counts do not match. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the hosted route in `references/flow-mode.md` Section 6
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
| [`references/types/architecture.md`](../../references/types/architecture.md) | Calling the tool and read-back |
| [`references/flow-mode.md`](../../references/flow-mode.md) | The hosted route |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-019
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/architecture-write-lanes.md`

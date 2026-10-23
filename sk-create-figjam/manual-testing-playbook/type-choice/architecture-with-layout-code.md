---
title: "FJ-012 -- An architecture through the six lanes"
description: "This scenario validates an architecture through the six lanes for `FJ-012`. It checks that a system request becomes an architecture in Figma's six lanes with no styling, cut to budget with the cut named, and a gate that names the layout code."
version: 1.0.0.0
---

# FJ-012 -- An architecture through the six lanes

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-012`.

---

## 1. OVERVIEW

This scenario validates an architecture through the six lanes for `FJ-012`. It checks that a system request becomes an architecture in Figma's six lanes with no styling, cut to budget with the cut named, and a gate that names the layout code.

### Why This Matters

Figma lays out an architecture on its own grid, only through `useArchitectureLayoutCode`. A model that styles nodes or skips the lanes draws as a plain flowchart.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-012` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a system request becomes an architecture in Figma's six lanes with no styling, cut to budget with the cut named, and a gate that names the layout code
- Real user request: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`
- Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`
- Expected execution process: Pick the architecture, start with `%% type: architecture`, assign every part to one of the six lane ids, cut file storage to stay inside 9 nodes and name it as left out, check it and end on a gate that names `useArchitectureLayoutCode`
- Expected signals: The model has at most 9 nodes, no `style` or `classDef`, dotted edges for async and external calls, a `Left out:` line naming file storage, the check prints `architecture: ok`, and the gate names the layout code and waits
- Desired user-visible outcome: A checked architecture with the cut named and a gate that waits
- Pass/fail: PASS if the model passes the check, a part beyond the budget is named under `Left out:`, the gate names the layout code and nothing is written. FAIL if the model sets styling, holds more than 9 nodes, drops a part with no `Left out:` entry, or the gate omits the layout code

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
| FJ-012 | An architecture through the six lanes | Verify that a system request becomes an architecture in Figma's six lanes with no styling, cut to budget with the cut named, and a gate that names the layout code | `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md` | Step 1 returns the gate naming `useArchitectureLayoutCode`. Step 2 prints `diagram 1, architecture: ok` with exit 0 | The reply, the model with its provenance table and `Left out:` line and the operator's check run | PASS if the model passes the check, a part beyond the budget is named under `Left out:`, the gate names the layout code and nothing is written. FAIL if the model sets styling, holds more than 9 nodes, drops a part with no `Left out:` entry, or the gate omits the layout code | 1. Check `references/types/architecture.md` Sections 2 and 3 for the lanes and allowed edges 2. Check the write call in `references/flow-mode.md` Section 6 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: copy the model into <scratch>/model.md and run python3 sk-create-figjam/scripts/flow_check.py <scratch>/model.md`

### Expected

Step 1 returns the gate naming `useArchitectureLayoutCode`. Step 2 prints `diagram 1, architecture: ok` with exit 0

### Evidence

The reply, the model with its provenance table and `Left out:` line and the operator's check run

### Pass / Fail

- **Pass**: the model passes the check, a part beyond the budget is named under `Left out:`, the gate names the layout code and nothing is written
- **Fail**: the model sets styling, holds more than 9 nodes, drops a part with no `Left out:` entry, or the gate omits the layout code

### Failure Triage

1. Check `references/types/architecture.md` Sections 2 and 3 for the lanes and allowed edges
2. Check the write call in `references/flow-mode.md` Section 6

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
| [`references/types/architecture.md`](../../references/types/architecture.md) | Lanes, allowed edges and budget |
| [`assets/templates/architecture.md`](../../assets/templates/architecture.md) | Architecture patterns |
| [`assets/examples/architecture-loomlist-sync.md`](../../assets/examples/architecture-loomlist-sync.md) | Worked example |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-012
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/architecture-with-layout-code.md`

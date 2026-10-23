---
title: "FJ-040 -- An over-broad brief is narrowed before a model"
description: "This scenario validates an over-broad brief is narrowed before a model for `FJ-040`. It checks that a brief that spans several flows is read back as one recommended scope with the parts left for a later board named, and only that scope is modelled and gated."
version: 1.0.0.0
---

# FJ-040 -- An over-broad brief is narrowed before a model

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-040`.

---

## 1. OVERVIEW

This scenario validates an over-broad brief is narrowed before a model for `FJ-040`. It checks that a brief that spans several flows is read back as one recommended scope with the parts left for a later board named, and only that scope is modelled and gated.

### Why This Matters

A brief that covers a whole product cannot fit one board. Reading the scope back lets the user move a part into this board before any model is written.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-040` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a brief that spans several flows is read back as one recommended scope with the parts left for a later board named, and only that scope is modelled and gated
- Real user request: `$figjam the whole Fernhouse product on a new board in our Fernhouse Product plan: signup, returns, refunds, the warehouse and billing`
- Prompt: `$figjam the whole Fernhouse product on a new board in our Fernhouse Product plan: signup, returns, refunds, the warehouse and billing`
- Expected execution process: Route to Flow Mode, find that the brief spans several flows, read it back as one recommended scope, name the parts left for a later board and model only that scope
- Expected signals: The first reply reads the brief back as one recommended scope and names the flows left for a later board, with no model. The second reply models that scope only, carries a `Left out:` line naming the rest and ends on a gate that waits
- Desired user-visible outcome: One board of the scope that was read back, with the rest named as later work
- Pass/fail: PASS if the reply names one recommended scope and the parts left for a later board, and only that scope is modelled. FAIL if every flow is drawn on one board, the run models with no scope read back, or a part outside the scope appears with no `Left out:` entry

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam the whole Fernhouse product on a new board in our Fernhouse Product plan: signup, returns, refunds, the warehouse and billing`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-040 | An over-broad brief is narrowed before a model | Verify that a brief that spans several flows is read back as one recommended scope with the parts left for a later board named, and only that scope is modelled and gated | `$figjam the whole Fernhouse product on a new board in our Fernhouse Product plan: signup, returns, refunds, the warehouse and billing` | 1. `session: start fresh -> user: submit the prompt exactly -> operator: read the reply and the tool calls` -> 2. `user: reply go ahead with that scope -> operator: read the model, the Left out: line and the gate` | Step 1 returns the recommended scope with the flows left out named. Step 2 finds a passing check on that scope, a `Left out:` line naming the rest and a gate that waits | Both replies, the tool calls with the check run and the model with its `Left out:` line | PASS if the reply names one recommended scope and the parts left for a later board, and only that scope is modelled. FAIL if every flow is drawn on one board, the run models with no scope read back, or a part outside the scope appears with no `Left out:` entry | 1. Check the draw-ready threshold in `references/flow-mode.md` Section 2 and the type table in Section 3 2. Check the budget rule in `references/flow-mode.md` Section 5 and the split pattern in `assets/flow-templates.md` Section 2 3. Check the `Left out:` line in `references/flow-mode.md` Section 8 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly -> operator: read the reply and the tool calls`
2. `user: reply go ahead with that scope -> operator: read the model, the Left out: line and the gate`

### Expected

Step 1 returns the recommended scope with the flows left out named. Step 2 finds a passing check on that scope, a `Left out:` line naming the rest and a gate that waits

### Evidence

Both replies, the tool calls with the check run and the model with its `Left out:` line

### Pass / Fail

- **Pass**: the reply names one recommended scope and the parts left for a later board, and only that scope is modelled
- **Fail**: every flow is drawn on one board, the run models with no scope read back, or a part outside the scope appears with no `Left out:` entry

### Failure Triage

1. Check the draw-ready threshold in `references/flow-mode.md` Section 2 and the type table in Section 3
2. Check the budget rule in `references/flow-mode.md` Section 5 and the split pattern in `assets/flow-templates.md` Section 2
3. Check the `Left out:` line in `references/flow-mode.md` Section 8

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Scope, the budget and the `Left out:` line |
| [`assets/flow-templates.md`](../../assets/flow-templates.md) | The split pattern |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-040
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/over-broad-brief-narrowed.md`

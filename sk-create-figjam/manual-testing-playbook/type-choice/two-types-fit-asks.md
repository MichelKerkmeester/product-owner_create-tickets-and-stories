---
title: "FJ-002 -- Two types fit, so one question"
description: "This scenario validates two types fit, so one question for `FJ-002`. It checks that a request that an architecture and a sequence both answer gets one question about the reader's question before any model is written."
version: 1.0.0.0
---

# FJ-002 -- Two types fit, so one question

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-002`.

---

## 1. OVERVIEW

This scenario validates two types fit, so one question for `FJ-002`. It checks that a request that an architecture and a sequence both answer gets one question about the reader's question before any model is written.

### Why This Matters

An architecture shows which parts connect and a sequence shows the order of one exchange. Guessing draws the wrong board for half the readers.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-002` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request that an architecture and a sequence both answer gets one question about the reader's question before any model is written
- Real user request: `make a FigJam diagram of how Loomlist block sync works`
- Prompt: `make a FigJam diagram of how Loomlist block sync works`
- Expected execution process: Route to Flow Mode on the FigJam wording, find that an architecture and a sequence both answer the request, and ask one question that names both reader questions
- Expected signals: The reply asks exactly one question, names the architecture and the sequence by the question each answers, writes no model, runs no check and calls no write tool
- Desired user-visible outcome: One plain question that lets the user pick the board they need
- Pass/fail: PASS if the reply asks one question naming both types and writes nothing. FAIL if the reply picks a type without asking, asks more than one question, writes a model before the answer or calls a write tool

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `make a FigJam diagram of how Loomlist block sync works`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-002 | Two types fit, so one question | Verify that a request that an architecture and a sequence both answer gets one question about the reader's question before any model is written | `make a FigJam diagram of how Loomlist block sync works` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply and the tool calls` | Step 1 returns one question naming both types. Step 2 finds no write tool, no `fj` verb and no model | The reply and the tool calls | PASS if the reply asks one question naming both types and writes nothing. FAIL if the reply picks a type without asking, asks more than one question, writes a model before the answer or calls a write tool | 1. Check the two-types rule in `references/flow-mode.md` Section 3 and Section 9 2. Check the type detection in `SKILL.md` Section 2 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply and the tool calls`

### Expected

Step 1 returns one question naming both types. Step 2 finds no write tool, no `fj` verb and no model

### Evidence

The reply and the tool calls

### Pass / Fail

- **Pass**: the reply asks one question naming both types and writes nothing
- **Fail**: the reply picks a type without asking, asks more than one question, writes a model before the answer or calls a write tool

### Failure Triage

1. Check the two-types rule in `references/flow-mode.md` Section 3 and Section 9
2. Check the type detection in `SKILL.md` Section 2

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Type table and recovery |
| [`SKILL.md`](../../SKILL.md) | Type detection |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/two-types-fit-asks.md`

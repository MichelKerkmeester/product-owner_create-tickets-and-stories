---
title: "FJ-021 -- FigJam as the subject of a task"
description: "This scenario validates figJam as the subject of a task for `FJ-021`. It checks that a task about a FigJam board stays a Task in the Product Owner packet and draws nothing."
version: 1.0.0.0
---

# FJ-021 -- FigJam as the subject of a task

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-021`.

---

## 1. OVERVIEW

This scenario validates figJam as the subject of a task for `FJ-021`. It checks that a task about a FigJam board stays a Task in the Product Owner packet and draws nothing.

### Why This Matters

Product Owner writes tickets about FigJam work. Reading every mention of FigJam as a drawing request would turn a ticket into an unwanted board.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-021` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a task about a FigJam board stays a Task in the Product Owner packet and draws nothing
- Real user request: `write a task to tidy the figjam board labels`
- Prompt: `write a task to tidy the figjam board labels`
- Expected execution process: Hub stage one keeps the request in the Product Owner packet, which routes it to Task Mode
- Expected signals: The reply is a Task, with no model, no check run and no Figma tool call
- Desired user-visible outcome: A task ticket, not a board
- Pass/fail: PASS if the reply is a Task and nothing is drawn. FAIL if Flow Mode runs, a model is written or a Figma tool is called

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `write a task to tidy the figjam board labels`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-021 | FigJam as the subject of a task | Verify that a task about a FigJam board stays a Task in the Product Owner packet and draws nothing | `write a task to tidy the figjam board labels` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply and the tool calls` | Step 1 returns a Task. Step 2 finds no Figma tool call | The reply and the tool calls | PASS if the reply is a Task and nothing is drawn. FAIL if Flow Mode runs, a model is written or a Figma tool is called | 1. Check the gold row `FigJam inside a task request` with `python3 benchmark/gates/check_hub.py` 2. Check the hand-back rule in `SKILL.md` Section 2 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply and the tool calls`

### Expected

Step 1 returns a Task. Step 2 finds no Figma tool call

### Evidence

The reply and the tool calls

### Pass / Fail

- **Pass**: the reply is a Task and nothing is drawn
- **Fail**: Flow Mode runs, a model is written or a Figma tool is called

### Failure Triage

1. Check the gold row `FigJam inside a task request` with `python3 benchmark/gates/check_hub.py`
2. Check the hand-back rule in `SKILL.md` Section 2

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
| [`SKILL.md`](../../SKILL.md) | Primary detection signal |
| [`../sk-product-owner/references/task-mode.md`](../../../sk-product-owner/references/task-mode.md) | Task Mode |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-021
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/figjam-as-task-subject.md`

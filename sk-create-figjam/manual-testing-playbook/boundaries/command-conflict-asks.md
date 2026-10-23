---
title: "FJ-020 -- Two artifact commands ask one question"
description: "This scenario validates two artifact commands ask one question for `FJ-020`. It checks that `$task $flow` names two artifacts, so the Product Owner packet asks one question that settles the artifact, later rounds ask only what the board needs and nothing is drawn or saved."
version: 1.0.0.0
---

# FJ-020 -- Two artifact commands ask one question

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-020`.

---

## 1. OVERVIEW

This scenario validates two artifact commands ask one question for `FJ-020`. It checks that `$task $flow` names two artifacts, so the Product Owner packet asks one question that settles the artifact, later rounds ask only what the board needs and nothing is drawn or saved.

### Why This Matters

The packet hands a conflict back rather than guessing, so the user decides whether they wanted a ticket or a board.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-020` and confirm the expected signals without contradictory evidence.

- Objective: Verify that `$task $flow` names two artifacts, so the Product Owner packet asks one question that settles the artifact, later rounds ask only what the board needs and nothing is drawn or saved
- Real user request: `$task $flow the Fernhouse onboarding checklist`
- Prompt: `$task $flow the Fernhouse onboarding checklist`
- Expected execution process: Hub stage one starts the request in the Product Owner packet, whose Interactive Mode asks one question naming a Task and a FigJam diagram
- Expected signals: The first reply asks one question naming both artifacts and nothing about the board, and a later round asks only the board facts the sources leave open. It writes no model, calls no Figma tool and saves nothing beyond the clarification the Product Owner contract allows
- Desired user-visible outcome: One question that settles the artifact
- Pass/fail: PASS if one question settles the artifact, later rounds ask only what the board needs and nothing is drawn until the artifact is settled. FAIL if a board or a model is produced before the artifact is settled, or a round that settles a board fact is refused as a second question

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$task $flow the Fernhouse onboarding checklist`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-020 | Two artifact commands ask one question | Verify that `$task $flow` names two artifacts, so the Product Owner packet asks one question that settles the artifact, later rounds ask only what the board needs and nothing is drawn or saved | `$task $flow the Fernhouse onboarding checklist` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply, the tool calls and export/` | Step 1 returns one question. Step 2 finds no Figma tool call and no model | The reply, the tool calls and the `export/` listing | PASS if one question settles the artifact, later rounds ask only what the board needs and nothing is drawn until the artifact is settled. FAIL if a board or a model is produced before the artifact is settled, or a round that settles a board fact is refused as a second question | 1. Check `$task $flow` in `benchmark/hub-routing-cases.json` and `python3 benchmark/gates/check_hub.py` 2. Check the conflict rule in `../sk-product-owner/references/interactive-mode.md` |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply, the tool calls and export/`

### Expected

Step 1 returns one question. Step 2 finds no Figma tool call and no model

### Evidence

The reply, the tool calls and the `export/` listing

### Pass / Fail

- **Pass**: one question settles the artifact, later rounds ask only what the board needs and nothing is drawn until the artifact is settled
- **Fail**: a board or a model is produced before the artifact is settled, or a round that settles a board fact is refused as a second question

### Failure Triage

1. Check `$task $flow` in `benchmark/hub-routing-cases.json` and `python3 benchmark/gates/check_hub.py`
2. Check the conflict rule in `../sk-product-owner/references/interactive-mode.md`

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
| [`../sk-product-owner/references/interactive-mode.md`](../../../sk-product-owner/references/interactive-mode.md) | Command conflicts |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-020
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/command-conflict-asks.md`

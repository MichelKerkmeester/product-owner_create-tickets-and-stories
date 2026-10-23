---
id: FJN-001
category: intra_routing_recall
stage: negative
title: "FJN-001 -- Negative control: a task about FigJam"
description: "This scenario validates negative control: a task about FigJam for `FJN-001`. It checks that a task request that names FigJam as its subject loads no packet leaf and hands back to the Product Owner packet."
expected_intent: UNKNOWN
expected_resources: []
expected_workflow_mode: UNKNOWN
expected_leaf_resources: []
version: 1.0.0.0
---

# FJN-001 -- Negative control: a task about FigJam

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJN-001`.

---

## 1. OVERVIEW

This scenario validates negative control: a task about FigJam for `FJN-001`. It checks that a task request that names FigJam as its subject loads no packet leaf and hands back to the Product Owner packet.

### Why This Matters

The packet must abstain on another artifact's framing. A leak here turns tickets about boards into boards.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJN-001` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a task request that names FigJam as its subject loads no packet leaf and hands back to the Product Owner packet
- Real user request: `write a task to tidy the figjam board labels`
- Prompt: `write a task to tidy the figjam board labels`
- Expected execution process: Hub stage one keeps the request in `sk-product-owner`, and a Flow route that still reached this packet would take the `UNKNOWN_FALLBACK` hand-back in `SKILL.md` Section 2
- Expected signals: The hub check passes with this prompt routed to `sk-product-owner`, and the topology gate accepts an empty leaf set
- Desired user-visible outcome: No FigJam leaf loads for a ticket about a board
- Pass/fail: PASS if the hub keeps the prompt in `sk-product-owner` and the packet declares no leaf for it. FAIL if the hub routes the prompt to `sk-create-figjam` or a leaf is declared

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
| FJN-001 | Negative control: a task about FigJam | Verify that a task request that names FigJam as its subject loads no packet leaf and hands back to the Product Owner packet | `write a task to tidy the figjam board labels` | 1. `bash: python3 benchmark/gates/check_hub.py` -> 2. `bash: grep -n "another artifact's framing" sk-create-figjam/SKILL.md` -> 3. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook` | Step 1 prints `PASSED the hub`. Step 2 prints the hand-back line. Step 3 prints `PASS  FJN-001` | The three command outputs with their exit status | PASS if the hub keeps the prompt in `sk-product-owner` and the packet declares no leaf for it. FAIL if the hub routes the prompt to `sk-create-figjam` or a leaf is declared | 1. Check the gold row `FigJam inside a task request` 2. Check the hand-back branch in `SKILL.md` Section 2 |

### Commands

1. `bash: python3 benchmark/gates/check_hub.py`
2. `bash: grep -n "another artifact's framing" sk-create-figjam/SKILL.md`
3. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook`

### Expected

Step 1 prints `PASSED the hub`. Step 2 prints the hand-back line. Step 3 prints `PASS  FJN-001`

### Evidence

The three command outputs with their exit status

### Pass / Fail

- **Pass**: the hub keeps the prompt in `sk-product-owner` and the packet declares no leaf for it
- **Fail**: the hub routes the prompt to `sk-create-figjam` or a leaf is declared

### Failure Triage

1. Check the gold row `FigJam inside a task request`
2. Check the hand-back branch in `SKILL.md` Section 2

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
| [`SKILL.md`](../../SKILL.md) | Hand-back rule |

---

## 5. SOURCE METADATA

- Group: Intra-routing recall
- Playbook ID: FJN-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `intra-routing-recall/negative-task-about-figjam.md`

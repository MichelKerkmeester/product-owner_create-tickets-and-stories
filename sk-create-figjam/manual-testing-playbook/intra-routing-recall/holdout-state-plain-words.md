---
id: FJH-001
category: intra_routing_recall
stage: holdout
title: "FJH-001 -- State routing in plain words"
description: "This scenario validates state routing in plain words for `FJH-001`. It checks that a request that never says state diagram, lifecycle or transition still reads as a state diagram through the word statuses."
expected_intent: sk-create-figjam
expected_resources:
  - sk-create-figjam/references/flow-mode.md
  - sk-create-figjam/assets/flow-templates.md
  - sk-create-figjam/references/types/state.md
  - sk-create-figjam/assets/templates/state.md
  - sk-create-figjam/references/quality-rubric.md
expected_workflow_mode: sk-create-figjam
expected_leaf_resources:
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/flow-mode.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/flow-templates.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/types/state.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/templates/state.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/quality-rubric.md
version: 1.0.1.0
---

# FJH-001 -- State routing in plain words

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJH-001`.

---

## 1. OVERVIEW

This scenario validates state routing in plain words for `FJH-001`. It checks that a request that never says state diagram, lifecycle or transition still reads as a state diagram through the word statuses.

### Why This Matters

Users describe what they want to see, not the diagram's name. This holdout decontaminates `FJR-005`, which uses the router's own words.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJH-001` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request that never says state diagram, lifecycle or transition still reads as a state diagram through the word statuses
- Real user request: `in FigJam, show which statuses an order can be in and what moves it between them`
- Prompt: `in FigJam, show which statuses an order can be in and what moves it between them`
- Expected execution process: Hub stage one starts the request in `sk-create-figjam` on the `figjam` signal, and `SKILL.md` `TYPE_SIGNALS` matches `status` to `state` alone
- Expected signals: The hub check passes with this prompt among its gold rows, and the resolved leaves match `FJR-005`
- Desired user-visible outcome: The state rules load from plain wording
- Pass/fail: PASS if the prompt routes to `sk-create-figjam` and resolves the same leaves as `FJR-005`. FAIL if the hub routes elsewhere or the leaves differ from `FJR-005` without a reason

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `in FigJam, show which statuses an order can be in and what moves it between them`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJH-001 | State routing in plain words | Verify that a request that never says state diagram, lifecycle or transition still reads as a state diagram through the word statuses | `in FigJam, show which statuses an order can be in and what moves it between them` | 1. `bash: python3 benchmark/gates/check_hub.py` -> 2. `bash: grep -n -e '"state": (.*"status"' sk-create-figjam/SKILL.md` -> 3. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook` | Step 1 prints `PASSED the hub`. Step 2 prints the `TYPE_SIGNALS` row for `state`, which carries the `status` cue the word statuses matches. Step 3 prints `PASS  FJH-001` | The three command outputs with their exit status | PASS if the prompt routes to `sk-create-figjam` and resolves the same leaves as `FJR-005`. FAIL if the hub routes elsewhere or the leaves differ from `FJR-005` without a reason | 1. Compare this file's leaves with `route-state.md` 2. Check the `status` cue in `SKILL.md` Section 2 |

### Commands

1. `bash: python3 benchmark/gates/check_hub.py`
2. `bash: grep -n -e '"state": (.*"status"' sk-create-figjam/SKILL.md`
3. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook`

### Expected

Step 1 prints `PASSED the hub`. Step 2 prints the `TYPE_SIGNALS` row for `state`, which carries the `status` cue the word statuses matches. Step 3 prints `PASS  FJH-001`

### Evidence

The three command outputs with their exit status

### Pass / Fail

- **Pass**: the prompt routes to `sk-create-figjam` and resolves the same leaves as `FJR-005`
- **Fail**: the hub routes elsewhere or the leaves differ from `FJR-005` without a reason

### Failure Triage

1. Compare this file's leaves with `route-state.md`
2. Check the `status` cue in `SKILL.md` Section 2

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
| [`SKILL.md`](../../SKILL.md) | Type detection |

---

## 5. SOURCE METADATA

- Group: Intra-routing recall
- Playbook ID: FJH-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `intra-routing-recall/holdout-state-plain-words.md`

---
title: "FJ-014 -- A ten-node user flow is refused"
description: "This scenario validates a ten-node user flow is refused for `FJ-014`. It checks that the check refuses a user flow of 10 nodes and tells the writer to split it."
version: 1.0.0.0
---

# FJ-014 -- A ten-node user flow is refused

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-014`.

---

## 1. OVERVIEW

This scenario validates a ten-node user flow is refused for `FJ-014`. It checks that the check refuses a user flow of 10 nodes and tells the writer to split it.

### Why This Matters

Nine nodes is the budget a reader can follow on one board. A longer flow must split or cut, and the cut must reach the reply as a `Left out:` line.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-014` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check refuses a user flow of 10 nodes and tells the writer to split it
- Real user request: `As the operator, run the sk-create-figjam check on a straight user flow of 10 nodes. Verify it fails on the node budget. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on a straight user flow of 10 nodes. Verify it fails on the node budget. Return the output and exit status.`
- Expected execution process: Write a 10-node linear `flowchart TD` to a scratch file and run the check on it
- Expected signals: The output reads `10 nodes, at most 9: split the flow` and exits 1
- Desired user-visible outcome: A refusal that names the budget
- Pass/fail: PASS if the budget failure is named and the exit status is 1. FAIL if the model passes or the exit status is not 1

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on a straight user flow of 10 nodes. Verify it fails on the node budget. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-014 | A ten-node user flow is refused | Verify that the check refuses a user flow of 10 nodes and tells the writer to split it | `As the operator, run the sk-create-figjam check on a straight user flow of 10 nodes. Verify it fails on the node budget. Return the output and exit status.` | 1. `bash: write a flowchart TD with a stadium start, eight steps and a stadium end to <scratch>/budget.md` -> 2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/budget.md; echo exit $?` | Step 2 prints the budget failure and `exit 1` | The scratch model and the command output with its exit status | PASS if the budget failure is named and the exit status is 1. FAIL if the model passes or the exit status is not 1 | 1. Check the budget in `scripts/figjam_checks/flowchart.py` 2. Check `references/types/user-flow.md` Section 4 |

### Commands

1. `bash: write a flowchart TD with a stadium start, eight steps and a stadium end to <scratch>/budget.md`
2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/budget.md; echo exit $?`

### Expected

Step 2 prints the budget failure and `exit 1`

### Evidence

The scratch model and the command output with its exit status

### Pass / Fail

- **Pass**: the budget failure is named and the exit status is 1
- **Fail**: the model passes or the exit status is not 1

### Failure Triage

1. Check the budget in `scripts/figjam_checks/flowchart.py`
2. Check `references/types/user-flow.md` Section 4

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
| [`scripts/figjam_checks/flowchart.py`](../../scripts/figjam_checks/flowchart.py) | Flowchart rules |
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | Budget and splitting |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-014
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/user-flow-over-budget.md`

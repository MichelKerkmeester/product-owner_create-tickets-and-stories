---
title: "FJ-043 -- A rank of five steps is refused"
description: "This scenario validates a rank of five steps is refused for `FJ-043`. It checks that the check measures the layout of a legal user flow and refuses one whose widest rank holds five steps."
version: 1.0.0.0
---

# FJ-043 -- A rank of five steps is refused

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-043`.

---

## 1. OVERVIEW

This scenario validates a rank of five steps is refused for `FJ-043`. It checks that the check measures the layout of a legal user flow and refuses one whose widest rank holds five steps.

### Why This Matters

A model can pass every count and still read badly. The generator owns the layout once the board exists, so a rank too wide to read at a glance is caught on the model, where a split costs nothing.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-043` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check measures the layout of a legal user flow and refuses one whose widest rank holds five steps
- Real user request: `As the operator, run the sk-create-figjam check on a user flow whose start branches into five parallel steps. Verify it fails on the layout measures. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on a user flow whose start branches into five parallel steps. Verify it fails on the layout measures. Return the output and exit status.`
- Expected execution process: Write a user flow whose start fans out to five steps that meet at one end to a scratch file and run the check
- Expected signals: The output reads `a rank holds 5 steps, at most 4: split the flow so a rank reads at a glance` and exits 1, and a passing model prints its widest rank, longest path, connectors per step, label average and crossing pairs beside the counts
- Desired user-visible outcome: A refusal that names the layout measure and its budget
- Pass/fail: PASS if the wide rank is refused with exit 1 and the shipped example passes with its five measures printed. FAIL if the wide model passes, the failure names no budget, or the passing line carries no measures

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on a user flow whose start branches into five parallel steps. Verify it fails on the layout measures. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-043 | A rank of five steps is refused | Verify that the check measures the layout of a legal user flow and refuses one whose widest rank holds five steps | `As the operator, run the sk-create-figjam check on a user flow whose start branches into five parallel steps. Verify it fails on the layout measures. Return the output and exit status.` | 1. `bash: write a flowchart TD whose stadium start links to five steps that each link to one stadium end to <scratch>/rank.md` -> 2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/rank.md; echo exit $?` -> 3. `bash: python3 sk-create-figjam/scripts/flow_check.py sk-create-figjam/assets/examples/user-flow-fernhouse-return.md; echo exit $?` | Step 2 prints the rank failure and `exit 1`. Step 3 prints the example's counts with the five measures and `exit 0` | The scratch model and both command outputs with their exit status | PASS if the wide rank is refused with exit 1 and the shipped example passes with its five measures printed. FAIL if the wide model passes, the failure names no budget, or the passing line carries no measures | 1. Check the budgets in `scripts/figjam_checks/layout.py` 2. Check the layout lines in `references/quality-rubric.md` Section 5 |

### Commands

1. `bash: write a flowchart TD whose stadium start links to five steps that each link to one stadium end to <scratch>/rank.md`
2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/rank.md; echo exit $?`
3. `bash: python3 sk-create-figjam/scripts/flow_check.py sk-create-figjam/assets/examples/user-flow-fernhouse-return.md; echo exit $?`

### Expected

Step 2 prints the rank failure and `exit 1`. Step 3 prints the example's counts with the five measures and `exit 0`

### Evidence

The scratch model and both command outputs with their exit status

### Pass / Fail

- **Pass**: the wide rank is refused with exit 1 and the shipped example passes with its five measures printed
- **Fail**: the wide model passes, the failure names no budget, or the passing line carries no measures

### Failure Triage

1. Check the budgets in `scripts/figjam_checks/layout.py`
2. Check the layout lines in `references/quality-rubric.md` Section 5

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
| [`scripts/figjam_checks/layout.py`](../../scripts/figjam_checks/layout.py) | Layout measures and budgets |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | Reading the measures before the gate |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-043
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/layout-measures-refuse-a-wide-rank.md`

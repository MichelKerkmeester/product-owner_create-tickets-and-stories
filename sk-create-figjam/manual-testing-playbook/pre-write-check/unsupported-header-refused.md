---
title: "FJ-006 -- A pie block is refused by the check"
description: "This scenario validates a pie block is refused by the check for `FJ-006`. It checks that the check refuses a Mermaid block whose kind Flow Mode does not draw."
version: 1.0.1.0
---

# FJ-006 -- A pie block is refused by the check

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-006`.

---

## 1. OVERVIEW

This scenario validates a pie block is refused by the check for `FJ-006`. It checks that the check refuses a Mermaid block whose kind Flow Mode does not draw.

### Why This Matters

A model that slips past the type choice must still be stopped before a board call.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-006` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check refuses a Mermaid block whose kind Flow Mode does not draw
- Real user request: `As the operator, run the sk-create-figjam check on a pie chart model. Verify it fails and points at the type table. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on a pie chart model. Verify it fails and points at the type table. Return the output and exit status.`
- Expected execution process: Write a pie block to a scratch file outside the repository and run the check on it
- Expected signals: The output names a pie block as undrawable, points at `references/flow-mode.md` Section 3 and exits 1
- Desired user-visible outcome: A refusal that points at the nearest drawable type
- Pass/fail: PASS if the pie block is refused with a pointer to Section 3 and exit 1. FAIL if the block passes or the exit status is not 1

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on a pie chart model. Verify it fails and points at the type table. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-006 | A pie block is refused by the check | Verify that the check refuses a Mermaid block whose kind Flow Mode does not draw | `As the operator, run the sk-create-figjam check on a pie chart model. Verify it fails and points at the type table. Return the output and exit status.` | 1. `bash: write a mermaid pie title Bookings block with two slices to <scratch>/pie.md` -> 2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/pie.md; echo exit $?` | Step 2 prints the undrawable-kind failure and `exit 1` | The scratch model and the command output with its exit status | PASS if the pie block is refused with a pointer to Section 3 and exit 1. FAIL if the block passes or the exit status is not 1 | 1. Check the header dispatch in `scripts/flow_check.py` 2. Check the undrawable list in `references/flow-mode.md` Section 3 |

### Commands

1. `bash: write a mermaid pie title Bookings block with two slices to <scratch>/pie.md`
2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/pie.md; echo exit $?`

### Expected

Step 2 prints the undrawable-kind failure and `exit 1`

### Evidence

The scratch model and the command output with its exit status

### Pass / Fail

- **Pass**: the pie block is refused with a pointer to Section 3 and exit 1
- **Fail**: the block passes or the exit status is not 1

### Failure Triage

1. Check the header dispatch in `scripts/flow_check.py`
2. Check the undrawable list in `references/flow-mode.md` Section 3

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
| [`scripts/flow_check.py`](../../scripts/flow_check.py) | Header dispatch and refusal |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-006
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/unsupported-header-refused.md`

---
title: "FJ-046 -- A status lane is checked and drawn"
description: "This scenario validates a status lane is checked and drawn for `FJ-046`. It checks that a laned process with a status lane passes the check and composes its statuses as chevrons moved by dotted lines, and that a solid status move is refused."
version: 1.0.0.0
---

# FJ-046 -- A status lane is checked and drawn

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-046`.

---

## 1. OVERVIEW

This scenario validates a status lane is checked and drawn for `FJ-046`. It checks that a laned process with a status lane passes the check and composes its statuses as chevrons moved by dotted lines, and that a solid status move is refused.

### Why This Matters

A status lane is a lane no actor works in. A status reached by a solid arrow reads as a step in the work, so the check refuses it on the model, before a board draws it wrong.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-046` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a laned process with a status lane passes the check and composes its statuses as chevrons moved by dotted lines, and that a solid status move is refused
- Real user request: `As the operator, run the sk-create-figjam check and composer on the worked status lane example, then on a copy whose first status move is solid. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check and composer on the worked status lane example, then on a copy whose first status move is solid. Return the output and exit status.`
- Expected execution process: Run the check on the worked example, print its composer model, then copy the example with its first status move written `-->` and run the check on the copy
- Expected signals: Step 1 prints `ok, 15 nodes and 20 connectors` and `exit 0`. Step 2 prints five nodes of kind `status` and the edge style `statusMove`. Step 4 prints `is solid: a step moves the status with -.->` and `exit 1`
- Desired user-visible outcome: A status lane that passes, composes as its own kind and line, and a solid move refused with the rule it breaks
- Pass/fail: PASS if the example passes with its counts, the model carries the status kind and the status move, and the solid move is refused with exit 1. FAIL if the example fails, the model draws a status as a step, or the solid move passes

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check and composer on the worked status lane example, then on a copy whose first status move is solid. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-046 | A status lane is checked and drawn | Verify that a laned process with a status lane passes the check and composes its statuses as chevrons moved by dotted lines, and that a solid status move is refused | `As the operator, run the sk-create-figjam check and composer on the worked status lane example, then on a copy whose first status move is solid. Return the output and exit status.` | 1. `bash: python3 sk-create-figjam/scripts/flow_check.py sk-create-figjam/assets/examples/process-fernhouse-commission.md; echo exit $?` -> 2. `bash: python3 sk-create-figjam/scripts/compose_board.py sk-create-figjam/assets/examples/process-fernhouse-commission.md --model` -> 3. `bash: copy the example to <scratch>/status.md with `order -.-> requested` written `order --> requested`` -> 4. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/status.md; echo exit $?` | Step 1 prints `ok, 15 nodes and 20 connectors` and `exit 0`. Step 2 prints five nodes of kind `status` and the edge style `statusMove`. Step 4 prints `is solid: a step moves the status with -.->` and `exit 1` | The four command outputs with their exit status | PASS if the example passes with its counts, the model carries the status kind and the status move, and the solid move is refused with exit 1. FAIL if the example fails, the model draws a status as a step, or the solid move passes | 1. Check `status_problems` in `scripts/figjam_checks/flowchart.py` 2. Check the status lane rules in `references/types/process.md` Section 3 |

### Commands

1. `bash: python3 sk-create-figjam/scripts/flow_check.py sk-create-figjam/assets/examples/process-fernhouse-commission.md; echo exit $?`
2. `bash: python3 sk-create-figjam/scripts/compose_board.py sk-create-figjam/assets/examples/process-fernhouse-commission.md --model`
3. `bash: copy the example to <scratch>/status.md with `order -.-> requested` written `order --> requested``
4. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/status.md; echo exit $?`

### Expected

Step 1 prints `ok, 15 nodes and 20 connectors` and `exit 0`. Step 2 prints five nodes of kind `status` and the edge style `statusMove`. Step 4 prints `is solid: a step moves the status with -.->` and `exit 1`

### Evidence

The four command outputs with their exit status

### Pass / Fail

- **Pass**: the example passes with its counts, the model carries the status kind and the status move, and the solid move is refused with exit 1
- **Fail**: the example fails, the model draws a status as a step, or the solid move passes

### Failure Triage

1. Check `status_problems` in `scripts/figjam_checks/flowchart.py`
2. Check the status lane rules in `references/types/process.md` Section 3

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
| [`scripts/figjam_checks/flowchart.py`](../../scripts/figjam_checks/flowchart.py) | Status lane rules |
| [`assets/compose-board.js`](../../assets/compose-board.js) | The chevron and the dotted status move |
| [`references/types/process.md`](../../references/types/process.md) | The status lane grammar and rules |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-046
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/status-lane-checked.md`

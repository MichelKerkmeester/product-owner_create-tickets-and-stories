---
title: "FJ-047 -- Detail cards only at the Faithful level"
description: "This scenario validates detail cards only at the Faithful level for `FJ-047`. It checks that a step's body passes at the Faithful detail level and is refused below it or over its line limit."
version: 1.0.0.0
---

# FJ-047 -- Detail cards only at the Faithful level

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-047`.

---

## 1. OVERVIEW

This scenario validates detail cards only at the Faithful level for `FJ-047`. It checks that a step's body passes at the Faithful detail level and is refused below it or over its line limit.

### Why This Matters

A body under a step keeps what a spec says about it, and it costs room. Below the Faithful level a label stays one line, so a body there is refused before the board grows to carry it.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-047` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a step's body passes at the Faithful detail level and is refused below it or over its line limit
- Real user request: `As the operator, run the sk-create-figjam check on the worked detail card example, on a copy at the Balanced level and on a copy with a 50-character body line. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on the worked detail card example, on a copy at the Balanced level and on a copy with a 50-character body line. Return the output and exit status.`
- Expected execution process: Run the check on the worked example, then on a copy whose `%% level:` line reads `balanced`, then on a copy whose first body line runs 50 characters
- Expected signals: Step 1 prints `ok` and `exit 0`. Step 3 prints `need %% level: faithful` and `exit 1`. Step 5 prints `at most 44: split it into two lines` and `exit 1`
- Desired user-visible outcome: Detail cards that pass at Faithful and a refusal that names the level or the line limit
- Pass/fail: PASS if the example passes and both copies are refused with exit 1 and the rule each breaks. FAIL if the example fails, or either copy passes

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on the worked detail card example, on a copy at the Balanced level and on a copy with a 50-character body line. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-047 | Detail cards only at the Faithful level | Verify that a step's body passes at the Faithful detail level and is refused below it or over its line limit | `As the operator, run the sk-create-figjam check on the worked detail card example, on a copy at the Balanced level and on a copy with a 50-character body line. Return the output and exit status.` | 1. `bash: python3 sk-create-figjam/scripts/flow_check.py sk-create-figjam/assets/examples/process-fernhouse-commission.md; echo exit $?` -> 2. `bash: copy the example to <scratch>/balanced.md with `%% level: faithful` written `%% level: balanced`` -> 3. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/balanced.md; echo exit $?` -> 4. `bash: copy the example to <scratch>/long.md with the first body line of `confirm` lengthened to 50 characters` -> 5. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/long.md; echo exit $?` | Step 1 prints `ok` and `exit 0`. Step 3 prints `need %% level: faithful` and `exit 1`. Step 5 prints `at most 44: split it into two lines` and `exit 1` | The scratch models and the three command outputs with their exit status | PASS if the example passes and both copies are refused with exit 1 and the rule each breaks. FAIL if the example fails, or either copy passes | 1. Check `detail_problems` in `scripts/figjam_checks/flowchart.py` 2. Check the detail level dial in `references/flow-mode.md` Section 4 |

### Commands

1. `bash: python3 sk-create-figjam/scripts/flow_check.py sk-create-figjam/assets/examples/process-fernhouse-commission.md; echo exit $?`
2. `bash: copy the example to <scratch>/balanced.md with `%% level: faithful` written `%% level: balanced``
3. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/balanced.md; echo exit $?`
4. `bash: copy the example to <scratch>/long.md with the first body line of `confirm` lengthened to 50 characters`
5. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/long.md; echo exit $?`

### Expected

Step 1 prints `ok` and `exit 0`. Step 3 prints `need %% level: faithful` and `exit 1`. Step 5 prints `at most 44: split it into two lines` and `exit 1`

### Evidence

The scratch models and the three command outputs with their exit status

### Pass / Fail

- **Pass**: the example passes and both copies are refused with exit 1 and the rule each breaks
- **Fail**: the example fails, or either copy passes

### Failure Triage

1. Check `detail_problems` in `scripts/figjam_checks/flowchart.py`
2. Check the detail level dial in `references/flow-mode.md` Section 4

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
| [`scripts/figjam_checks/flowchart.py`](../../scripts/figjam_checks/flowchart.py) | Detail card rules |
| [`references/flow-mode.md`](../../references/flow-mode.md) | The detail level dial |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-047
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/detail-cards-at-faithful.md`

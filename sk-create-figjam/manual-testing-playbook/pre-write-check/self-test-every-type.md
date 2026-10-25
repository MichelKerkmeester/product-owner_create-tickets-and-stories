---
title: "FJ-004 -- The self-test covers every type"
description: "This scenario validates the self-test covers every type for `FJ-004`. It checks that the check's self-test passes every planted defect and every template, example and Project mirror of all seven types."
version: 1.0.1.0
---

# FJ-004 -- The self-test covers every type

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-004`.

---

## 1. OVERVIEW

This scenario validates the self-test covers every type for `FJ-004`. It checks that the check's self-test passes every planted defect and every template, example and Project mirror of all seven types.

### Why This Matters

The check is the only thing standing between a model and a board the composer or the generated fallback would mangle. A rule whose planted defect passes is a rule that does nothing.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-004` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check's self-test passes every planted defect and every template, example and Project mirror of all seven types
- Real user request: `As the operator, run the sk-create-figjam self-test against the packet. Verify every check passes and every template and example is read. Return the summary line and exit status.`
- Prompt: `As the operator, run the sk-create-figjam self-test against the packet. Verify every check passes and every template and example is read. Return the summary line and exit status.`
- Expected execution process: Run the self-test from the Product Owner root, then the check on every template and example, and read each output and exit status
- Expected signals: The self-test ends `<n> of <n> self-test checks passed` with exit 0, and every template and example prints `PASSED`
- Desired user-visible outcome: A self-test that proves every rule fires
- Pass/fail: PASS if the self-test passes in full and every template and example passes. FAIL if any self-test check fails or any template or example fails

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam self-test against the packet. Verify every check passes and every template and example is read. Return the summary line and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-004 | The self-test covers every type | Verify that the check's self-test passes every planted defect and every template, example and Project mirror of all seven types | `As the operator, run the sk-create-figjam self-test against the packet. Verify every check passes and every template and example is read. Return the summary line and exit status.` | 1. `bash: python3 sk-create-figjam/scripts/flow_check.py --self-test` -> 2. `bash: for f in sk-create-figjam/assets/templates/*.md sk-create-figjam/assets/examples/*.md; do python3 sk-create-figjam/scripts/flow_check.py "$f"; done` | Step 1 prints all checks passed with exit 0. Step 2 prints `PASSED` for every file | Both command outputs with their exit status | PASS if the self-test passes in full and every template and example passes. FAIL if any self-test check fails or any template or example fails | 1. Read the failing line, which names the fixture or the file 2. Check the rule module under `scripts/figjam_checks/` for that type |

### Commands

1. `bash: python3 sk-create-figjam/scripts/flow_check.py --self-test`
2. `bash: for f in sk-create-figjam/assets/templates/*.md sk-create-figjam/assets/examples/*.md; do python3 sk-create-figjam/scripts/flow_check.py "$f"; done`

### Expected

Step 1 prints all checks passed with exit 0. Step 2 prints `PASSED` for every file

### Evidence

Both command outputs with their exit status

### Pass / Fail

- **Pass**: the self-test passes in full and every template and example passes
- **Fail**: any self-test check fails or any template or example fails

### Failure Triage

1. Read the failing line, which names the fixture or the file
2. Check the rule module under `scripts/figjam_checks/` for that type

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
| [`scripts/flow_check.py`](../../scripts/flow_check.py) | The check and its self-test |
| [`scripts/figjam_checks/fixtures.py`](../../scripts/figjam_checks/fixtures.py) | Good and planted fixtures |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-004
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/self-test-every-type.md`

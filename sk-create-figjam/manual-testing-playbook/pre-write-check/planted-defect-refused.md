---
title: "FJ-005 -- A sequence with an alias and a note is refused"
description: "This scenario validates a sequence with an alias and a note is refused for `FJ-005`. It checks that the check refuses a sequence model that uses an alias and a note, naming each rule."
version: 1.0.1.0
---

# FJ-005 -- A sequence with an alias and a note is refused

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-005`.

---

## 1. OVERVIEW

This scenario validates a sequence with an alias and a note is refused for `FJ-005`. It checks that the check refuses a sequence model that uses an alias and a note, naming each rule.

### Why This Matters

Neither the composer nor Figma's generated fallback draws aliases and notes, and the fallback drops them without an error, so a board drawn from this model would show a bare id and lose the note.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-005` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check refuses a sequence model that uses an alias and a note, naming each rule
- Real user request: `As the operator, run the sk-create-figjam check on a sequence model with an aliased participant and a note. Verify it fails and names both rules. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on a sequence model with an aliased participant and a note. Verify it fails and names both rules. Return the output and exit status.`
- Expected execution process: Write the planted model to a scratch file outside the repository and run the check on it
- Expected signals: The output names the alias, the note and the short id, ends `FAILED 1 of 1 diagram(s)` and exits 1
- Desired user-visible outcome: A refusal that says what to change
- Pass/fail: PASS if every planted defect is named and the exit status is 1. FAIL if the model passes, a defect goes unnamed or the exit status is not 1

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on a sequence model with an aliased participant and a note. Verify it fails and names both rules. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-005 | A sequence with an alias and a note is refused | Verify that the check refuses a sequence model that uses an alias and a note, naming each rule | `As the operator, run the sk-create-figjam check on a sequence model with an aliased participant and a note. Verify it fails and names both rules. Return the output and exit status.` | 1. `bash: write a sequence model to <scratch>/seq.md with participant G as GuestApp, a message from G and Note over BookingApi: holds the room` -> 2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/seq.md; echo exit $?` | Step 2 prints the alias, note and id failures and `exit 1` | The scratch model and the command output with its exit status | PASS if every planted defect is named and the exit status is 1. FAIL if the model passes, a defect goes unnamed or the exit status is not 1 | 1. Check `scripts/figjam_checks/sequence.py` for the alias and note rules 2. Check `references/types/sequence.md` Section 3 |

### Commands

1. `bash: write a sequence model to <scratch>/seq.md with participant G as GuestApp, a message from G and Note over BookingApi: holds the room`
2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/seq.md; echo exit $?`

### Expected

Step 2 prints the alias, note and id failures and `exit 1`

### Evidence

The scratch model and the command output with its exit status

### Pass / Fail

- **Pass**: every planted defect is named and the exit status is 1
- **Fail**: the model passes, a defect goes unnamed or the exit status is not 1

### Failure Triage

1. Check `scripts/figjam_checks/sequence.py` for the alias and note rules
2. Check `references/types/sequence.md` Section 3

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
| [`scripts/figjam_checks/sequence.py`](../../scripts/figjam_checks/sequence.py) | Sequence rules |
| [`references/types/sequence.md`](../../references/types/sequence.md) | What a sequence model cannot carry |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-005
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/planted-defect-refused.md`

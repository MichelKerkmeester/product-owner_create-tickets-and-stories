---
title: "FJ-015 -- An off-palette fill is refused"
description: "This scenario validates an off-palette fill is refused for `FJ-015`. It checks that the check refuses a fill that is not one of FigJam's light pairs and points at the style guide."
version: 1.0.0.0
---

# FJ-015 -- An off-palette fill is refused

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-015`.

---

## 1. OVERVIEW

This scenario validates an off-palette fill is refused for `FJ-015`. It checks that the check refuses a fill that is not one of FigJam's light pairs and points at the style guide.

### Why This Matters

A colour outside the palette fails the contrast record and becomes a custom swatch nobody can match from the FigJam picker.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-015` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check refuses a fill that is not one of FigJam's light pairs and points at the style guide
- Real user request: `As the operator, run the sk-create-figjam check on a user flow whose end node is filled #00FF00. Verify it fails on the palette. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on a user flow whose end node is filled #00FF00. Verify it fails on the palette. Return the output and exit status.`
- Expected execution process: Write a three-node user flow with `style c fill:#00FF00,stroke:#008800` to a scratch file and run the check
- Expected signals: The output reads `fill #00ff00 is not a FigJam light fill: pick a pair from references/style-guide.md` and exits 1
- Desired user-visible outcome: A refusal that points at the palette
- Pass/fail: PASS if the off-palette fill is named with the style guide pointer and the exit status is 1. FAIL if the model passes or the exit status is not 1

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on a user flow whose end node is filled #00FF00. Verify it fails on the palette. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-015 | An off-palette fill is refused | Verify that the check refuses a fill that is not one of FigJam's light pairs and points at the style guide | `As the operator, run the sk-create-figjam check on a user flow whose end node is filled #00FF00. Verify it fails on the palette. Return the output and exit status.` | 1. `bash: write a three-node flowchart TD with style c fill:#00FF00,stroke:#008800 to <scratch>/colour.md` -> 2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/colour.md; echo exit $?` | Step 2 prints the palette failure and `exit 1` | The scratch model and the command output with its exit status | PASS if the off-palette fill is named with the style guide pointer and the exit status is 1. FAIL if the model passes or the exit status is not 1 | 1. Check `ACCENT_PAIRS` in `scripts/figjam_checks/common.py` 2. Check the palette record in `references/style-guide.md` Section 3 |

### Commands

1. `bash: write a three-node flowchart TD with style c fill:#00FF00,stroke:#008800 to <scratch>/colour.md`
2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/colour.md; echo exit $?`

### Expected

Step 2 prints the palette failure and `exit 1`

### Evidence

The scratch model and the command output with its exit status

### Pass / Fail

- **Pass**: the off-palette fill is named with the style guide pointer and the exit status is 1
- **Fail**: the model passes or the exit status is not 1

### Failure Triage

1. Check `ACCENT_PAIRS` in `scripts/figjam_checks/common.py`
2. Check the palette record in `references/style-guide.md` Section 3

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
| [`scripts/figjam_checks/common.py`](../../scripts/figjam_checks/common.py) | The accepted pairs |
| [`references/style-guide.md`](../../references/style-guide.md) | The palette record |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-015
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/off-palette-colour-refused.md`

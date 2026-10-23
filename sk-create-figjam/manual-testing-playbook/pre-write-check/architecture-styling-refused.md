---
title: "FJ-016 -- A styled architecture is refused"
description: "This scenario validates a styled architecture is refused for `FJ-016`. It checks that the check refuses an otherwise valid architecture that carries one `style` line."
version: 1.0.0.0
---

# FJ-016 -- A styled architecture is refused

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-016`.

---

## 1. OVERVIEW

This scenario validates a styled architecture is refused for `FJ-016`. It checks that the check refuses an otherwise valid architecture that carries one `style` line.

### Why This Matters

Figma's architecture layout colours each lane itself. A styled node fights that layout and draws a colour the lane scheme did not choose.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-016` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the check refuses an otherwise valid architecture that carries one `style` line
- Real user request: `As the operator, run the sk-create-figjam check on the Loomlist architecture example with one style line added. Verify it fails on styling alone. Return the output and exit status.`
- Prompt: `As the operator, run the sk-create-figjam check on the Loomlist architecture example with one style line added. Verify it fails on styling alone. Return the output and exit status.`
- Expected execution process: Copy the architecture example's model to a scratch file, add `style sync fill:#CDF4D3,stroke:#66D575` and run the check
- Expected signals: The output reads `the block carries styling: the architecture layout colours each lane itself, drop it`, names no other rule and exits 1
- Desired user-visible outcome: A refusal that names styling as the one defect
- Pass/fail: PASS if the styling failure is the only finding and the exit status is 1. FAIL if the model passes, another rule fires on the unchanged example, or the exit status is not 1

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, run the sk-create-figjam check on the Loomlist architecture example with one style line added. Verify it fails on styling alone. Return the output and exit status.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-016 | A styled architecture is refused | Verify that the check refuses an otherwise valid architecture that carries one `style` line | `As the operator, run the sk-create-figjam check on the Loomlist architecture example with one style line added. Verify it fails on styling alone. Return the output and exit status.` | 1. `bash: copy the mermaid block of sk-create-figjam/assets/examples/architecture-loomlist-sync.md to <scratch>/arch.md and add style sync fill:#CDF4D3,stroke:#66D575` -> 2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/arch.md; echo exit $?` | Step 2 prints only the styling failure and `exit 1` | The scratch model and the command output with its exit status | PASS if the styling failure is the only finding and the exit status is 1. FAIL if the model passes, another rule fires on the unchanged example, or the exit status is not 1 | 1. Check the styling rule in `scripts/figjam_checks/flowchart.py` 2. Check `references/types/architecture.md` Section 5 |

### Commands

1. `bash: copy the mermaid block of sk-create-figjam/assets/examples/architecture-loomlist-sync.md to <scratch>/arch.md and add style sync fill:#CDF4D3,stroke:#66D575`
2. `bash: python3 sk-create-figjam/scripts/flow_check.py <scratch>/arch.md; echo exit $?`

### Expected

Step 2 prints only the styling failure and `exit 1`

### Evidence

The scratch model and the command output with its exit status

### Pass / Fail

- **Pass**: the styling failure is the only finding and the exit status is 1
- **Fail**: the model passes, another rule fires on the unchanged example, or the exit status is not 1

### Failure Triage

1. Check the styling rule in `scripts/figjam_checks/flowchart.py`
2. Check `references/types/architecture.md` Section 5

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
| [`scripts/figjam_checks/flowchart.py`](../../scripts/figjam_checks/flowchart.py) | Architecture rules |
| [`assets/examples/architecture-loomlist-sync.md`](../../assets/examples/architecture-loomlist-sync.md) | The unchanged model |

---

## 5. SOURCE METADATA

- Group: Pre-write check
- Playbook ID: FJ-016
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `pre-write-check/architecture-styling-refused.md`

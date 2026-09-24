---
title: "PBG-001 -- Bug report flow"
description: "Validates bug-command routing, the evidence context gate and the fixed bug-report Deliverable Block."
version: 1.0.0.0
---

# PBG-001 -- Bug report flow

This scenario validates the explicit `$bug` path from a one-line symptom to a rendered Bug Deliverable Block.

---

## 1. OVERVIEW

The command fixes Bug Mode. The Project should ask one evidence question, render it as a clarification block with an export-equivalent label, wait, then render the fixed bug structure with observed and expected behavior and the four-item QA checklist while claiming no file was written.

### Why this matters

The defect handoff depends on reproduction steps and honest missing values. A Project reply that invents a device or frequency sends QA after the wrong evidence.

---

## 2. SCENARIO CONTRACT

- Objective: Verify bug routing, the single evidence question, wait behavior and the fixed bug block
- Real user request: `The payout pause toggle silently reverts to off.`
- Prompt: `$bug The payout pause toggle silently reverts to off.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 and inspect the rendered bug block
- Expected signals: Turn 1 asks one evidence question, renders a clarification block with `Export-equivalent path: export/[NNN] - bug-payout-pause-toggle-clarification.md` and claims no file. Turn 2 renders the bug block with the field table, `1. Observed Behavior`, numbered steps, `2. Expected Behavior`, the four fixed checklist items and `Export-equivalent path: export/[NNN] - bug-payout-pause-toggle.md`
- Desired user-visible outcome: One evidence question followed by a compliant bug block
- Pass/fail: PASS if the runtime waits, missing environment values read `Not provided`, and the checklist keeps the four fixed items. FAIL if it invents a frequency, device, root cause or reproduction step, or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$bug The payout pause toggle silently reverts to off.` | Ask one evidence question for reproduction steps, environment, expected behavior and attachments, render it as a clarification block and wait. Create no bug draft | Bug Mode and the payout pause toggle remain selected | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `It happens every time on web. Steps: open a brand wallet with a pending payout, switch pause on, then refresh the page. The toggle shows off while the payout still shows paused. Expected: the toggle stays on until the brand resumes the payout. I used Chrome 126, no screenshot.` | Render the fixed bug structure from the supplied facts, use `Not provided` for missing fields and report the export-equivalent label | Frequency stays `Always`, the Chrome detail lands in the browser fields and no device or OS value is invented | Turn 2 reply, rendered bug block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$bug The payout pause toggle silently reverts to off.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered bug block -> operator: grade the field table, reproduction steps, checklist and labels`

### Expected

Step 1 fixes the panel baseline. Step 2 returns one evidence question as a Canvas Artifact. Step 3 proves the wait state. Step 4 finds `### About` with the field table, `1. Observed Behavior`, numbered steps, `2. Expected Behavior` and the exact four checklist items.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the field table values and the checklist.

### Pass / fail

- **Pass**: One evidence question, no early draft, and one rendered bug block with the fixed structure and honest missing values, under an export-equivalent label
- **Fail**: The runtime drafts before Turn 2, infers frequency from a count, invents environment data, alters the four checklist items or claims a local file

### Failure triage

1. Check the bug context question and fixed structure in the Templates - Bug Mode knowledge document
2. Compare the field table with the Bug Report Template knowledge document, especially the frequency and `Not provided` rules
3. Reconcile the reproduction steps with the supplied flow and remove any invented detail

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBG-001 | Bug report flow | Verify evidence intake and the fixed bug-report Deliverable Block | `$bug The payout pause toggle silently reverts to off.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the bug block | Step 1: baseline known. Step 2: one evidence question. Step 3: truthful missing values. Step 4: fixed structure with checklist and label | Both replies, rendered blocks, labels, field table and checklist | PASS if the question, the fixed structure and the honest fields all match. FAIL otherwise | 1. Check Bug Mode knowledge. 2. Check the field table rules. 3. Check reproduction steps and checklist |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Canvas Artifact and export-equivalent contract |
| [`Product Owner - Templates - Bug Mode - v0.203.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Bug%20Mode%20-%20v0.203.md) | Project bug workflow and evidence rules |
| [`Product Owner - Assets - Bug Report Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Bug%20Report%20Template%20-%20v0.100.md) | Field table, frequency rules and checklist |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBG-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/bug-report-flow.md`

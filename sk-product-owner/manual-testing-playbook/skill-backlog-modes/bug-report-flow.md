---
title: "SBG-001 -- Bug report flow"
description: "Validates bug-command routing, the evidence context gate and the fixed bug-report structure with its QA checklist."
version: 1.0.0.0
---

# SBG-001 -- Bug report flow

This scenario validates the explicit `$bug` path from a one-line symptom to a saved bug report.

---

## 1. OVERVIEW

The command fixes Bug Mode. The runtime should ask one evidence question for reproduction steps, environment and expected behavior, export that question as a clarification, wait, then export the fixed bug structure with observed and expected behavior and the four-item QA checklist.

### Why this matters

Bug reports hand a defect to QA. Missing reproduction steps or an invented frequency sends the wrong work downstream.

---

## 2. SCENARIO CONTRACT

- Objective: Verify bug routing, the single evidence question, wait behavior and fixed bug output
- Real user request: `The payout pause toggle silently reverts to off.`
- Prompt: `$bug The payout pause toggle silently reverts to off.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts
- Expected execution process: Start fresh, submit Turn 1, capture the evidence question and its clarification export, answer in Turn 2 and inspect the next bug export
- Expected signals: Turn 1 asks one evidence question, exports `export/[###] - bug-payout-pause-toggle-clarification.md`, reads it back and creates no draft. Turn 2 uses only supplied facts, writes `Not provided` where evidence is missing, saves `export/[###] - bug-payout-pause-toggle.md`, reads it back and replies path-first
- Desired user-visible outcome: One evidence question followed by a compliant bug export
- Pass/fail: PASS if the runtime waits, the bug carries observed and expected behavior and numbered reproduction steps, and the checklist holds the four fixed items. FAIL if it invents a frequency, a device, a root cause or a reproduction step
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$bug The payout pause toggle silently reverts to off.` | Ask one evidence question for reproduction steps, environment, expected behavior and attachments, export it as a clarification and wait. Create no bug draft | Bug Mode and the payout pause toggle remain selected | Turn 1 reply, clarification export, read-back result and clean draft ledger |
| 2 | `It happens every time on web. Steps: open a brand wallet with a pending payout, switch pause on, then refresh the page. The toggle shows off while the payout still shows paused. Expected: the toggle stays on until the brand resumes the payout. I used Chrome 126, no screenshot.` | Build the fixed bug structure from the supplied facts, use `Not provided` for missing fields, save the next bug export, read it back and reply path-first | Frequency stays `Always`, the Chrome detail lands in the browser fields and no device or OS value is invented | Turn 2 reply, exported bug and read-back result |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$bug The payout pause toggle silently reverts to off.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new bug export -> operator: grade the field table, reproduction steps and checklist`

### Expected

Step 1 fixes the baseline. Step 2 returns one evidence question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds `### About` with the field table, `1. Observed Behavior`, numbered steps, `2. Expected Behavior` and the exact four checklist items.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the field table values and the checklist.

### Pass / fail

- **Pass**: One evidence question, no early draft, and one readable bug export with the fixed structure and honest missing values
- **Fail**: The runtime drafts before Turn 2, infers frequency from a count, invents environment data or alters the four checklist items

### Failure triage

1. Check the bug context question and fixed structure in `bug-mode.md`
2. Compare the field table with `bug-report-template.md`, especially the frequency and `Not provided` rules
3. Reconcile the reproduction steps with the supplied flow and remove any invented detail

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBG-001 | Bug report flow | Verify evidence intake and the fixed bug-report structure | `$bug The payout pause toggle silently reverts to off.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the bug export | Step 1: baseline known. Step 2: one evidence question. Step 3: truthful missing values. Step 4: fixed structure with checklist | Both replies, ledger, clarification and bug export paths and artifact excerpts | PASS if the question, the fixed structure and the honest fields all match. FAIL otherwise | 1. Check Bug Mode. 2. Check the field table rules. 3. Check reproduction steps and checklist |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`bug-mode.md`](../../references/bug-mode.md) | Bug workflow, evidence rules and fixed structure |
| [`bug-report-template.md`](../../assets/bug-report-template.md) | Field table, frequency rules and checklist |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBG-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/bug-report-flow.md`

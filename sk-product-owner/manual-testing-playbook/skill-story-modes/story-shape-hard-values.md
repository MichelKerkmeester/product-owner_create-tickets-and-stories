---
title: "SST-001 -- Story shape hard values"
description: "Validates story-intake clarification, Story shape selection and verbatim hard values inside the Requirements section."
version: 1.0.0.0
---

# SST-001 -- Story shape hard values

This scenario validates a no-token PRD request from clarification through a house-format Story export.

---

## 1. OVERVIEW

The request says "Turn these notes into a PRD" and supplies none. The runtime should route to Story Mode, open the intake gate and ask one consolidated question. After the notes arrive, it must resolve the Story shape, name the kind, carry every hard value verbatim into Requirements and keep values out of the acceptance criteria.

### Why this matters

A generalized value is a different and false claim. `24 hours` must not become a short pause, and `Pause payout` must not become updated copy.

---

## 2. SCENARIO CONTRACT

- Objective: Verify Story intake, shape resolution and verbatim hard values in the exported Story
- Real user request: `Turn these notes into a PRD for the payout pause feature.`
- Prompt: `Turn these notes into a PRD for the payout pause feature.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts
- Expected execution process: Start fresh, submit Turn 1, capture the intake question and its clarification export, answer in Turn 2 and inspect the next Story export
- Expected signals: Turn 1 asks one consolidated question covering role, value, kind, requirements and evidence, exports `export/[###] - PRD-payout-pause-clarification.md`, reads it back, replies with its path, the read-back line and the HVR self-scan line (root section 5, Clarification turns) and creates no draft. Turn 2 names the Story kind in the reply, saves `export/[###] - PRD-payout-pause.md`, reads it back and carries `24 hours` and `Pause payout` verbatim in Requirements
- Desired user-visible outcome: One story-intake question followed by a house-format Story export naming its kind
- Pass/fail: PASS if the runtime waits, loads only the Story scaffold, keeps the supplied values in Requirements and names the kind. FAIL if it drafts early, generalizes a value, puts a value in an acceptance criterion or emits ticket fields and story points
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Turn these notes into a PRD for the payout pause feature.` | Route to Story Mode, run the intake gate, ask one consolidated question for operation, role, value, kind, requirements and evidence, export it as a clarification and wait. Create no draft | Story intent and the payout pause feature remain selected | Turn 1 reply, clarification export, read-back result and clean draft ledger |
| 2 | `Story for brands. A brand can pause a pending payout when it needs to hold it. Hard values: the pause lasts exactly 24 hours, the reason field is required, the toggle label reads Pause payout, and the payout row shows a paused badge. Acceptance: the pause releases automatically after the hold.` | Resolve the Story shape, load only the Story scaffold, build About, Problem, Solution, Expected outcomes and Requirements, save the next Story export, read it back and name the kind in the reply | `24 hours` and `Pause payout` appear verbatim in Requirements and no value appears in the acceptance criteria | Turn 2 reply, exported Story and read-back result |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Turn these notes into a PRD for the payout pause feature.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new Story export -> operator: check the kind, the house sections, the hard values and the acceptance criteria`

### Expected

Step 1 fixes the baseline. Step 2 returns one intake question and one clarification file. Step 3 proves the wait state. Step 4 finds the story preamble, `## About`, `### Problem`, `### Solution`, `#### **Expected outcomes**`, `## Requirements` with the supplied values in backticks, and numbered acceptance criteria closed by the Mark-as-done line.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the Requirements bullets with their backticked values and the acceptance criteria.

### Pass / fail

- **Pass**: One intake question, no early draft, and one house-format Story that carries every supplied value verbatim and names its kind
- **Fail**: The runtime drafts early, generalizes a value, duplicates a value into a criterion, loads both scaffolds, or adds ticket header fields, points or INVEST notes

### Failure triage

1. Check the intake gate and kind selection in `story-mode.md`
2. Check the Requirements and acceptance-criteria rules in `story-template.md`
3. Reconcile every supplied value against the Requirements bullets and restore any generalized value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SST-001 | Story shape hard values | Verify Story intake, house shape and verbatim hard values | `Turn these notes into a PRD for the payout pause feature.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story export | Step 1: baseline known. Step 2: one intake question. Step 3: kind and values supplied. Step 4: house Story with verbatim values | Both replies, ledger, clarification and Story export paths, Requirements bullets and criteria | PASS if intake, shape and verbatim values all match. FAIL otherwise | 1. Check the intake gate. 2. Check the house grammar. 3. Check the supplied values |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`story-mode.md`](../../references/story-mode.md) | Intake gate, shape selection and hard-value rules |
| [`story-template.md`](../../assets/story-template.md) | Story scaffold and acceptance-criteria grammar |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Story context question wording |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SST-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/story-shape-hard-values.md`

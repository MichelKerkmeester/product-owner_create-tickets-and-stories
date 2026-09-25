---
title: "PST-001 -- Story shape hard values"
description: "Validates Project story-intake clarification, Story shape selection and verbatim hard values inside the Requirements section."
version: 1.0.0.0
---

# PST-001 -- Story shape hard values

This scenario validates a no-token PRD request from clarification through a house-format Story Deliverable Block.

---

## 1. OVERVIEW

The request says "Turn these notes into a PRD" and supplies none. The Project should route to Story Mode, open the intake gate and ask one consolidated question. After the notes arrive, it must resolve the Story shape, name the kind, carry every hard value verbatim into Requirements and keep values out of the acceptance criteria.

### Why this matters

A generalized value is a different and false claim. `24 hours` must not become a short pause, and `Pause payout` must not become updated copy.

---

## 2. SCENARIO CONTRACT

- Objective: Verify Story intake, shape resolution and verbatim hard values in the rendered Story
- Real user request: `Turn these notes into a PRD for the payout pause feature.`
- Prompt: `Turn these notes into a PRD for the payout pause feature.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the intake question and its clarification block, answer in Turn 2 and inspect the rendered Story
- Expected signals: Turn 1 asks one consolidated question covering role, value, kind, requirements and evidence, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - Story-payout-pause-clarification.md` and the HVR self-scan line (root section 5, Clarification turns) and creates no draft. Turn 2 names the Story kind in the reply, renders the Story under `Export-equivalent path: export/[NNN] - Story-payout-pause.md`, claims no file and carries `24 hours` and `Pause payout` verbatim in Requirements
- Desired user-visible outcome: One story-intake question followed by a house-format Story block naming its kind
- Pass/fail: PASS if the runtime waits, consults only the Story scaffold where the transcript shows its reads (`Custom Instructions.md` lines 58 and 79), keeps the supplied values in Requirements, names the kind and claims no file. FAIL if it drafts early, opens both scaffolds, generalizes a value, puts a value in an acceptance criterion, emits ticket fields and story points, or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Turn these notes into a PRD for the payout pause feature.` | Route to Story Mode, run the intake gate, ask one consolidated question for operation, role, value, kind, requirements and evidence, render it as a clarification block and wait. Create no draft | Story intent and the payout pause feature remain selected | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Story for brands. A brand can pause a pending payout when it needs to hold it. Hard values: the pause lasts exactly 24 hours, the reason field is required, the toggle label reads Pause payout, and the payout row shows a paused badge. Acceptance: the pause releases automatically after the hold.` | Resolve the Story shape, render About, Problem, Solution, Expected outcomes and Requirements, name the kind in the reply and claim no file | `24 hours` and `Pause payout` appear verbatim in Requirements and no value appears in the acceptance criteria | Turn 2 reply, rendered Story block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Turn these notes into a PRD for the payout pause feature.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Story -> operator: check the kind, the house sections, the hard values and the acceptance criteria`

### Expected

Step 1 fixes the panel baseline. Step 2 returns one intake question as its own clarification block. Step 3 proves the wait state. Step 4 finds the story preamble, `## About`, `### Problem`, `### Solution`, `#### **Expected outcomes**`, `## Requirements` with the supplied values in backticks, and numbered acceptance criteria closed by the Mark-as-done line.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the Requirements bullets with their backticked values and the acceptance criteria.

### Pass / fail

- **Pass**: One intake question, no early draft, and one house-format Story that carries every supplied value verbatim, names its kind and claims no file
- **Fail**: The runtime drafts early, opens both scaffolds, generalizes a value, duplicates a value into a criterion, adds ticket header fields, points or INVEST notes, or claims a local save

### Failure triage

1. Check the intake gate and kind selection in `Product Owner - Templates - Story Mode`
2. Check the Requirements and acceptance-criteria rules in `Product Owner - Assets - Story Template`
3. Reconcile every supplied value against the Requirements bullets and restore any generalized value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PST-001 | Story shape hard values | Verify Project Story intake, house shape and verbatim hard values | `Turn these notes into a PRD for the payout pause feature.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story block | Step 1: baseline known. Step 2: one intake question. Step 3: kind and values supplied. Step 4: house Story with verbatim values and label | Both replies, rendered blocks, labels, Requirements bullets and criteria | PASS if intake, shape and verbatim values all match. FAIL otherwise | 1. Check the intake gate. 2. Check the house grammar. 3. Check the supplied values |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Canvas Artifact and export-equivalent contract |
| [`Product Owner - Templates - Story Mode - v0.402.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.402.md) | Project Story intake, shape selection and hard-value rules |
| [`Product Owner - Assets - Story Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Story%20Template%20-%20v0.100.md) | Project Story scaffold and acceptance-criteria grammar |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PST-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/story-shape-hard-values.md`

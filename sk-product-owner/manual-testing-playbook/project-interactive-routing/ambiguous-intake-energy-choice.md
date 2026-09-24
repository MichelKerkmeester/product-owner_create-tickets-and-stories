---
title: "PIR-001 -- Ambiguous intake energy choice"
description: "Validates the Project comprehensive intake question that opens with the energy choice and renders an intake clarification before any artifact."
version: 1.0.0.0
---

# PIR-001 -- Ambiguous intake energy choice

This scenario validates the no-command, low-confidence path into Interactive Mode in a Claude Project.

---

## 1. OVERVIEW

The user is unsure what to create. No artifact command is present and the request names no artifact shape. The Project must ask one comprehensive question whose first item is the energy choice, render that question as an intake clarification block, wait, then route the answer to Task Mode with Quick energy.

### Why this matters

An ambiguous request that guesses a shape renders the wrong artifact. The energy-first question is the whole routing decision for this path.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the energy-first comprehensive question, the intake clarification block and the routed quick task
- Real user request: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`
- Prompt: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the comprehensive question and its clarification block, answer in Turn 2 and inspect the rendered task
- Expected signals: Turn 1 asks one question that opens with the Quick or Deeper energy choice, renders it with `Export-equivalent path: export/[NNN] - intake-creator-payout-flow-clarification.md` and claims no file. Turn 2 keeps the chosen Quick energy, renders the task under `Export-equivalent path: export/[NNN] - task-payout-pause-visibility.md` and claims no file
- Desired user-visible outcome: One energy-first question labelled as an intake clarification, then a quick task block
- Pass/fail: PASS if the first question opens with the energy choice and renders intact, and the second turn produces one quick task block with no file claim. FAIL if the runtime picks a shape before the answer, skips the clarification block or treats energy as an artifact intent
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.` | Enter Interactive Mode, ask one comprehensive question with the energy choice as its first item, render it as an intake clarification block and wait. Create no artifact | No artifact shape is assumed and the payout flow context is retained | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Quick, please. It is a task. Creators need to see why a payout was paused, including the reason and the pause date, on the payout detail screen.` | Keep Quick energy and Task intent, render the task block with its export-equivalent label and the HVR self-scan line | The Quick choice survives and the reason and pause date facts land in the task | Turn 2 reply, rendered task block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm the energy choice is the first item -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered task -> operator: check Task Mode, Quick energy, the supplied facts and the label`

### Expected

Step 1 fixes the panel baseline. Step 2 returns one comprehensive question as a Canvas Artifact. Step 3 proves the wait state and the energy-first order. Step 4 finds a task with `### About`, `### Requirements` and the reason and pause date facts.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the question order and the task sections.

### Pass / fail

- **Pass**: One energy-first question, one intake clarification block and one quick task block carrying the supplied facts, with no file claim
- **Fail**: The runtime guesses a shape, asks a second round, omits the clarification block or lets energy replace the artifact intent

### Failure triage

1. Check the comprehensive question order and guidance rules in the Interactive Mode knowledge document
2. Compare the question with the Comprehensive Question template in the Interactive Response Templates knowledge document
3. Check the routed task against the Task Mode and Task Templates knowledge documents

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-001 | Ambiguous intake energy choice | Verify the Project energy-first question, the intake clarification and the routed quick task | `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the task block | Step 1: baseline known. Step 2: one energy-first question. Step 3: Quick and Task chosen. Step 4: one quick task with label | Both replies, rendered blocks, labels, question order and task sections | PASS if the question, the block and the route all match. FAIL otherwise | 1. Check Interactive Mode knowledge. 2. Check the question order. 3. Check the routed task |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Canvas Artifact and export-equivalent contract |
| [`Product Owner - System - Interactive Mode - v0.404.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.404.md) | Project comprehensive question and energy choice |
| [`Product Owner - Assets - Interactive Response Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.102.md) | Comprehensive Question template |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/ambiguous-intake-energy-choice.md`

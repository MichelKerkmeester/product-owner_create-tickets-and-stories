---
title: "SIR-001 -- Ambiguous intake energy choice"
description: "Validates the comprehensive intake question that opens with the energy choice and exports an intake clarification before any artifact."
version: 1.0.0.0
---

# SIR-001 -- Ambiguous intake energy choice

This scenario validates the no-command, low-confidence path into Interactive Mode.

---

## 1. OVERVIEW

The user is unsure what to create. No artifact command is present and the request names no artifact shape. The runtime must ask one comprehensive question whose first item is the energy choice, export that question as an intake clarification, wait, then route the answer to Task Mode with Quick energy.

### Why this matters

An ambiguous request that guesses a shape writes the wrong artifact. The energy-first question is the whole routing decision for this path.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the energy-first comprehensive question, the intake clarification export and the routed quick task
- Real user request: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`
- Prompt: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts
- Expected execution process: Start fresh, submit Turn 1, capture the comprehensive question and its clarification export, answer in Turn 2 and inspect the next task export
- Expected signals: Turn 1 asks one question that opens with the Quick or Deeper energy choice, exports `export/[###] - intake-creator-payout-flow-clarification.md`, reads it back and creates no artifact. Turn 2 keeps the chosen Quick energy, saves `export/[###] - task-payout-pause-visibility.md`, reads it back and replies path-first
- Desired user-visible outcome: One energy-first question saved as an intake clarification, then a quick task export
- Pass/fail: PASS if the first question opens with the energy choice and is exported intact, and the second turn produces one quick task. FAIL if the runtime picks a shape before the answer, skips the clarification export or treats energy as an artifact intent
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.` | Enter Interactive Mode, ask one comprehensive question with the energy choice as its first item, export it as an intake clarification and wait. Create no artifact | No artifact shape is assumed and the payout flow context is retained | Turn 1 reply, clarification export, read-back result and clean artifact ledger |
| 2 | `Quick, please. It is a task. Creators need to see why a payout was paused, including the reason and the pause date, on the payout detail screen.` | Keep Quick energy and Task intent, build the task, save the next task export, read it back and reply path-first with the HVR self-scan line | The Quick choice survives and the reason and pause date facts land in the task | Turn 2 reply, exported task and read-back result |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm the energy choice is the first item -> user: submit Turn 2 in the same session`
4. `filesystem: open the new task export -> operator: check Task Mode, Quick energy and the supplied facts`

### Expected

Step 1 fixes the baseline. Step 2 returns one comprehensive question and one clarification file. Step 3 proves the wait state and the energy-first order. Step 4 finds a task with `### About`, `### Requirements` and the reason and pause date facts.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the question order and the task sections.

### Pass / fail

- **Pass**: One energy-first question, one intake clarification export and one quick task carrying the supplied facts
- **Fail**: The runtime guesses a shape, asks a second round, omits the clarification export or lets energy replace the artifact intent

### Failure triage

1. Check the comprehensive question order and guidance rules in `interactive-mode.md`
2. Compare the question with the Comprehensive Question template in `interactive-response-templates.md`
3. Check the routed task against `task-mode.md` and the export numbering rule

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-001 | Ambiguous intake energy choice | Verify the energy-first question, the intake clarification and the routed quick task | `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the task export | Step 1: baseline known. Step 2: one energy-first question. Step 3: Quick and Task chosen. Step 4: one quick task | Both replies, ledger, clarification and task export paths, question order and task sections | PASS if the question, the export and the route all match. FAIL otherwise | 1. Check Interactive Mode. 2. Check the question order. 3. Check the routed task |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Comprehensive question, energy choice and clarification export |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Comprehensive Question template |
| [`task-mode.md`](../../references/task-mode.md) | Routed task workflow |
| [`task-templates.md`](../../assets/task-templates.md) | Routed task scaffold |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill interactive routing
- Playbook ID: SIR-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/ambiguous-intake-energy-choice.md`

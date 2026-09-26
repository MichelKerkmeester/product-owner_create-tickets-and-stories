---
title: "PIR-001 -- Vague intake, kind and energy"
description: "Validates a no-command Roamstay loyalty points request in a Claude Project: one energy-first intake question rendered in the intake lane, then the Epic Turn 2 picks, rendered as its own block."
version: 1.0.0.1
---

# PIR-001 -- Vague intake, kind and energy

This scenario validates the no-command, low-confidence path into Interactive Mode in a Claude Project, with a request that names no artifact kind.

---

## 1. OVERVIEW

A Roamstay product manager passes on a vague ask about loyalty points for guests, with no command and no artifact kind, and attaches the company context page. That page says Roamstay has no loyalty or points scheme today. The Project must ask one comprehensive question whose first item is the energy choice and which also asks for the deliverable type, render it as an `intake` lane clarification block and wait. Turn 2 picks Deeper and an Epic, and the Project must render that Epic from the answer, keep every number it supplies and invent no point value, funding source or existing scheme.

### Why this matters

A vague request that guesses a kind renders the wrong artifact, and a runtime that fills the gap from general knowledge describes a points scheme Roamstay does not have. The energy-first question is the whole routing decision on this path.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the energy-first comprehensive question, its intake-lane clarification block and the Epic Turn 2 selects
- Real user request: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`
- Prompt: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and `roamstay-context.md` is staged at `context/roamstay-context.md`
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the comprehensive question and its clarification block, answer in Turn 2 in the same conversation and inspect the rendered Epic
- Expected signals: Turn 1 carries no command, no framing and no scoring topic, so it enters Interactive Mode (`Product Owner - System - Router Contract` line 808) and asks one question that opens with the Quick or Deeper energy choice and asks for the deliverable type in the same prompt (`Product Owner - System - Interactive Mode` lines 36 and 79, `Product Owner - Assets - Interactive Response Templates` lines 32 and 36). It renders the question alone as its own block, then `Export-equivalent path: export/[NNN] - intake-loyalty-points-clarification.md` and the `HVR self-scan:` line, and claims no file (`Custom Instructions.md` lines 85 and 228, `Product Owner - System - Interactive Mode` lines 70 and 74). No artifact is rendered. Turn 2 routes to Story Mode in the Epic shape at Standard or Deep energy and renders the Epic as its own block, then `Export-equivalent path: export/[NNN] - Epic-guest-loyalty-points.md` and the `HVR self-scan:` line, naming the kind Epic and claiming no file (`Custom Instructions.md` lines 86 and 227, `Product Owner - Templates - Story Mode` line 115). The Epic carries About with Problem, Goal and Solution, a Scope naming the four child stories as plain text and release-level acceptance criteria (`Product Owner - Templates - Story Mode` line 182, `Product Owner - Assets - Epic Template` lines 21 to 94). It covers iOS, Android and web, its Goal keeps `19%`, `25%`, `12 months` and the end of 2027, spending stays on Pay now bookings, the point value and who pays for points stay undecided, and nothing describes points, tiers or member-only prices as existing today
- Desired user-visible outcome: One energy-first question rendered as an intake clarification, then an Epic block for guest loyalty points that keeps Roamstay's facts and the answer's numbers, with no file claim
- Size band (advisory): 60 to 120 lines for the Turn 2 Epic body
- Pass/fail: PASS if Turn 1 asks one question whose first item is the energy choice and which asks for the deliverable type, renders it alone as its own block with `Export-equivalent path:` under an `intake` `-clarification` name, and Turn 2 renders an `Epic` block with its label, About, Problem, Goal, Solution, Scope and Acceptance criteria, the four child stories, the answer's numbers verbatim, spending limited to Pay now and no invented fact or unfilled slot, with no file claim on either turn. FAIL if Turn 1 picks a kind or renders anything but the question before the answer, skips the clarification block, Turn 2 asks a second round, the label's artifact word is not `Epic`, either reply claims a saved file, or the Epic states a point value or funding source, or describes a points balance, member tiers or member-only prices as current
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md` | Enter Interactive Mode, ask one comprehensive question with the energy choice as its first item and the deliverable type among the rest, render it as an intake clarification block and wait. Render no artifact | No artifact kind is assumed, no file is claimed and `context/roamstay-context.md` is unchanged | Turn 1 reply, rendered clarification block and its labels |
| 2 | `Deeper, and write an epic for it. It covers guests on the Guest app, iOS, Android and web. The goal is repeat bookings: 19% of guests book a second stay within 12 months today and we want 25% by the end of 2027. The child stories are joining from Account, earning points on completed stays, a points balance and history under Account, and spending points at checkout on Pay now bookings only, since Pay at property guests pay the property directly. The point value and who pays for points are not decided yet, so do not put a number on either.` | Keep the Deeper energy, resolve the Epic shape, render the Epic as its own block, then report the export-equivalent label, the `HVR self-scan:` line and the kind named | The Deeper choice and the Epic kind survive, the numbers and the Pay now limit land in the Epic, and no file is claimed | Turn 2 reply, rendered Epic block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`

### Commands

1. `sandbox: stage context/roamstay-context.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm the energy choice is the first item and the deliverable type is asked -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Epic -> operator: check the Epic shape, the supplied numbers, the Pay now limit, the undecided point value and the label`

### Expected

Step 1 fixes the panel baseline with the attachment in place. Step 2 returns one comprehensive question as its own clarification block. Step 3 proves the wait state and the energy-first order. Step 4 finds an Epic with `## About`, `### Problem`, `### Goal`, `### Solution`, `## Scope` and `## Acceptance criteria`, the four child stories and the Turn 2 numbers.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the question order and the Epic sections. Note whether the Epic states that Roamstay has no loyalty or points scheme today, as `context/roamstay-context.md` says under Known constraints.

### Pass / fail

- **Pass**: One energy-first question that asks for the deliverable type, rendered alone as an intake clarification block, then one `Epic` block with its required sections, the four child stories, `19%`, `25%`, `12 months` and 2027 intact, spending limited to Pay now, no invented fact or unfilled slot and no file claim
- **Fail**: The runtime guesses a kind, renders an artifact before the answer, omits the clarification block, asks a second round, labels the Epic with another artifact word, claims a saved file, or invents a point value, a funding source or a points scheme that already exists

### Failure triage

1. Check the comprehensive question order and energy rules in `Product Owner - System - Interactive Mode` lines 36 and 79
2. Compare the question with the Comprehensive Question in `Product Owner - Assets - Interactive Response Templates` lines 23 to 65
3. Check the rendered Epic against `Product Owner - Templates - Story Mode` line 182, `Product Owner - Assets - Epic Template` and the Known constraints section of `roamstay-context.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-001 | Vague intake, kind and energy | Verify the Project energy-first question, the intake clarification block and the Epic Turn 2 selects | `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Epic block | Step 1: baseline known. Step 2: one energy-first question block. Step 3: Deeper and Epic chosen. Step 4: one Epic block with the supplied numbers and its label | Both replies, rendered blocks, labels, question order and Epic sections | PASS if the question, the block and the Epic all match, no fact is invented and no file is claimed. FAIL otherwise | 1. Check Interactive Mode knowledge. 2. Check the question order. 3. Check the Epic against Story Mode knowledge and the context page |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Deliverable Block and export-equivalent contract |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | Fallback routing into Interactive Mode |
| [`Product Owner - System - Interactive Mode - v0.406.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.406.md) | Comprehensive question, energy choice and clarification block |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Comprehensive Question template |
| [`Product Owner - Templates - Story Mode - v0.403.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.403.md) | Routed Story Mode workflow and Epic shape |
| [`Product Owner - Assets - Epic Template - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Epic%20Template%20-%20v0.101.md) | Routed Epic scaffold |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment, the Guest app surfaces, Pay now and Pay at property, and the absent loyalty scheme |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/vague-intake-kind-and-energy.md`

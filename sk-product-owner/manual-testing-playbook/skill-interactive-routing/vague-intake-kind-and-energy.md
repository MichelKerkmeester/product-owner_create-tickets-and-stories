---
title: "SIR-001 -- Vague intake, kind and energy"
description: "Validates a no-command Roamstay loyalty points request that names no artifact kind: one energy-first intake question exported in the intake lane, then the Epic Turn 2 picks at the energy it picks."
version: 1.0.0.0
---

# SIR-001 -- Vague intake, kind and energy

This scenario validates the no-command, low-confidence path into Interactive Mode with a request that names no artifact kind.

---

## 1. OVERVIEW

A Roamstay product manager passes on a vague ask about loyalty points for guests, with no command and no artifact kind, and attaches the company context page. That page says Roamstay has no loyalty or points scheme today. The runtime must ask one comprehensive question whose first item is the energy choice and which also asks for the deliverable type, export it in the `intake` lane and wait. Turn 2 picks Deeper and an Epic, and the runtime must write that Epic from the answer, keep every number it supplies and invent no point value, funding source or existing scheme.

### Why this matters

A vague request that guesses a kind writes the wrong artifact, and a runtime that fills the gap from general knowledge describes a points scheme Roamstay does not have. The energy-first question is the whole routing decision on this path.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the energy-first comprehensive question, its intake-lane export and the Epic Turn 2 selects
- Real user request: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`
- Prompt: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and `roamstay-context.md` is staged at `context/roamstay-context.md`
- Expected execution process: Start fresh, submit Turn 1, capture the comprehensive question and its clarification export, answer in Turn 2 in the same session and inspect the Epic export
- Expected signals: Turn 1 carries no command, no framing and no scoring topic, so it enters Interactive Mode (`SKILL.md` line 73) and asks one question that opens with the Quick or Deeper energy choice and asks for the deliverable type in the same prompt (`SKILL.md` line 252, `references/interactive-mode.md` lines 59 and 102, `assets/interactive-response-templates.md` lines 55 and 59). It saves `export/[###] - intake-loyalty-points-clarification.md` holding the question alone, reads it back and replies with its path, the `Verified: read-back succeeded` line and the `HVR self-scan:` line (`references/interactive-mode.md` lines 93 and 97). No artifact is drafted. Turn 2 routes to Story Mode in the Epic shape at Standard or Deep energy, saves `export/[###] - Epic-guest-loyalty-points.md` on the next number, reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line, naming the kind Epic (`references/story-mode.md` line 139). The Epic carries About with Problem, Goal and Solution, a Scope naming the four child stories as plain text and release-level acceptance criteria (`references/story-mode.md` line 206, `assets/epic-template.md` lines 40 to 113). It covers iOS, Android and web, its Goal keeps `19%`, `25%`, `12 months` and the end of 2027, spending stays on Pay now bookings, the point value and who pays for points stay undecided, and nothing describes points, tiers or member-only prices as existing today
- Desired user-visible outcome: One energy-first question saved in the intake lane, then an Epic for guest loyalty points that keeps Roamstay's facts and the answer's numbers
- Size band (advisory): 60 to 120 lines for the Turn 2 Epic body
- Pass/fail: PASS if Turn 1 asks one question whose first item is the energy choice and which asks for the deliverable type, saves it alone under an `intake` `-clarification` name and reads it back, and Turn 2 saves an `Epic` on the next number with About, Problem, Goal, Solution, Scope and Acceptance criteria, the four child stories, the answer's numbers verbatim, spending limited to Pay now and no invented fact or unfilled slot. FAIL if Turn 1 picks a kind or drafts anything before the answer, skips the export, Turn 2 asks a second round, the export word is not `Epic`, or the Epic states a point value or funding source, or describes a points balance, member tiers or member-only prices as current
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md` | Enter Interactive Mode, ask one comprehensive question with the energy choice as its first item and the deliverable type among the rest, export it in the intake lane and wait. Create no artifact | No artifact kind is assumed, one new export, the `-clarification` file, and `context/roamstay-context.md` unchanged | Turn 1 reply, clarification export, read-back result and side-effect ledger |
| 2 | `Deeper, and write an epic for it. It covers guests on the Guest app, iOS, Android and web. The goal is repeat bookings: 19% of guests book a second stay within 12 months today and we want 25% by the end of 2027. The child stories are joining from Account, earning points on completed stays, a points balance and history under Account, and spending points at checkout on Pay now bookings only, since Pay at property guests pay the property directly. The point value and who pays for points are not decided yet, so do not put a number on either.` | Keep the Deeper energy, resolve the Epic shape, write the Epic, save it on the next number, read it back and reply path first with the `Verified:` line, the `HVR self-scan:` line and the kind named | The Deeper choice and the Epic kind survive, the numbers and the Pay now limit land in the Epic, and the clarification file is untouched | Turn 2 reply, Epic export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`

### Commands

1. `sandbox: stage context/roamstay-context.md -> sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm the energy choice is the first item and the deliverable type is asked -> user: submit Turn 2 in the same session`
4. `filesystem: open the new Epic export -> operator: check the Epic shape, the supplied numbers, the Pay now limit and the undecided point value`

### Expected

Step 1 fixes the baseline with the attachment in place. Step 2 returns one comprehensive question and one clarification file. Step 3 proves the wait state and the energy-first order. Step 4 finds an Epic with `## About`, `### Problem`, `### Goal`, `### Solution`, `## Scope` and `## Acceptance criteria`, the four child stories and the Turn 2 numbers.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the question order and the Epic sections. Note whether the Epic states that Roamstay has no loyalty or points scheme today, as `context/roamstay-context.md` says under Known constraints.

### Pass / fail

- **Pass**: One energy-first question that asks for the deliverable type, saved alone in the intake lane, then one `Epic` on the next number with its required sections, the four child stories, `19%`, `25%`, `12 months` and 2027 intact, spending limited to Pay now and no invented fact or unfilled slot
- **Fail**: The runtime guesses a kind, drafts before the answer, omits the clarification export, asks a second round, exports under another artifact word, or invents a point value, a funding source or a points scheme that already exists

### Failure triage

1. Check the comprehensive question order and energy rules in `references/interactive-mode.md` lines 59 and 102
2. Compare the question with the Comprehensive Question in `assets/interactive-response-templates.md` lines 46 to 88
3. Check the routed Epic against `references/story-mode.md` line 206, `assets/epic-template.md` and the Known constraints section of `roamstay-context.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-001 | Vague intake, kind and energy | Verify the energy-first question, the intake clarification and the Epic Turn 2 selects | `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Epic export | Step 1: baseline known. Step 2: one energy-first question. Step 3: Deeper and Epic chosen. Step 4: one Epic with the supplied numbers | Both replies, ledger, clarification and Epic export paths, question order and Epic sections | PASS if the question, the export and the Epic all match and no fact is invented. FAIL otherwise | 1. Check Interactive Mode. 2. Check the question order. 3. Check the Epic against Story Mode and the context page |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`SKILL.md`](../../SKILL.md) | Fallback routing and the energy-first clarification protocol |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Comprehensive question, energy choice and clarification export |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Comprehensive Question template |
| [`story-mode.md`](../../references/story-mode.md) | Routed Story Mode workflow and Epic shape |
| [`epic-template.md`](../../assets/epic-template.md) | Routed Epic scaffold |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment, the Guest app surfaces, Pay now and Pay at property, and the absent loyalty scheme |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill interactive routing
- Playbook ID: SIR-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/vague-intake-kind-and-energy.md`

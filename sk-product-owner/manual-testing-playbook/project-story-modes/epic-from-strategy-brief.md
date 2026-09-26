---
title: "PEP-001 -- Epic from strategy brief"
description: "Validates an explicit $epic request built on a partner self-onboarding strategy brief in a Project: one Epic question block in the Epic lane, then a house-format Epic Deliverable Block whose child stories and numbers come from the brief verbatim."
version: 1.1.0.0
---

# PEP-001 -- Epic from strategy brief

This scenario validates an explicit `$epic` request at Roamstay, from the Epic question through a house-format Epic Deliverable Block built from a strategy brief.

---

## 1. OVERVIEW

A head of product types `$epic` for Partner Hub self-onboarding, points at Freya's strategy brief and the Roamstay context, and says the first release cut is not agreed. The command routes to Story Mode in the Epic shape without supplying that direction, so the Project asks one consolidated Epic question in the Epic lane and waits. Turn 2 settles the child-story set and the cut. The Epic that follows names the brief's six stages as its child stories, carries the brief's numbers verbatim, puts connecting a channel manager under Added Later and keeps every boundary the brief draws.

### Why this matters

A strategy brief carries the numbers a director will hold the squads to. `11 business days` written as about two weeks, `38%` as about a third or `2027-06-30` as mid-2027 is a different claim, and the squads would size against it. The brief also draws the line the first release depends on: independent properties with up to `40 rooms`, no chains and no property that uses a channel manager.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$epic` on a strategy brief asks one Epic question, then renders a house-format Epic whose child stories, numbers and boundaries come from the brief
- Real user request: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`
- Prompt: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-partner-self-onboarding-brief.md](../../../benchmark/fixtures/companies/roamstay/roamstay-partner-self-onboarding-brief.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit at `context/` before the Canvas baseline
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the Epic question and its clarification block, answer in Turn 2 in the same conversation and inspect the rendered Epic
- Expected signals: Turn 1 routes to Story Mode in the Epic shape, asks one consolidated question covering the first release cut and the child-story set, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - Epic-partner-self-onboarding-clarification.md` and the `HVR self-scan:` line (root section 5, Clarification turns) and creates no draft. Turn 2 names the Epic kind in the reply, renders the Epic as its Deliverable Block under `Export-equivalent path: export/[NNN] - Epic-partner-self-onboarding.md` with the `HVR self-scan:` line and claims no file. The Epic carries `11 business days` and `38%` in Problem, `3 business days`, `1,500` and `2027-06-30` in Goal, the six stage names in `## Scope` and connecting a `channel manager` under `#### Added Later`
- Desired user-visible outcome: One Epic question block, then one Roamstay Epic block the Partner, Ops Tools and Payments squads can plan from, with the brief's numbers intact
- Size band (advisory): 90 to 150 lines of Epic body
- Pass/fail: PASS if Turn 1 asks one Epic question in the Epic lane and drafts nothing, and Turn 2 renders one Epic in the house shape (a `# Epic - ` H1 with no story preamble, `## About` holding `### Problem`, `### Goal` and `### Solution` plus `#### **References**` only when a link is supplied, never empty and never with an invented link, `## Scope` naming exactly six first-release child stories as plain text, one per stage name verbatim, plus `#### Added Later` holding the channel manager connection, release-level `## Acceptance criteria` in numbered `1\.` blocks each closed by its Mark-as-done line, no `## Requirements`, no ticket header fields, story points or INVEST notes), consults only the Epic scaffold where the transcript shows its reads (`Custom Instructions.md` lines 58 and 79), names the kind, carries `11 business days`, `38%`, `3 business days`, `1,500` and `2027-06-30` verbatim, invents no link and claims no file. FAIL if it drafts in Turn 1, asks or labels under another artifact word, rounds or rewrites a brief value, adds, merges or drops a child story, brings chains, properties over `40 rooms` or channel manager properties into first-release scope, fills an estimate the brief never gave, leaves a template slot such as `{link}` unfilled or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.` | Route `$epic` to Story Mode in the Epic shape and consult only the Story Mode knowledge with the Epic Template. The command does not supply the open first release cut, so ask one consolidated Epic question covering the cut and whether the brief's six stages are the child stories, render it as an Epic-lane clarification block and wait. Create no draft | Epic intent, the brief and the Roamstay context stay selected, and no Epic block exists | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `One child story per stage in Freya's brief, all six in the first release. Connecting a channel manager goes under Added Later. The goal and target are Freya's, use them as she wrote them.` | Draft from the Epic Template: `## About` with Problem, Goal and Solution plus References only when a link is supplied, `## Scope` with the six stages as plain-text child stories and an Added Later group for connecting a channel manager, then release-level criteria. Render it as the Deliverable Block, name the Epic kind in the reply and claim no file | The brief's numbers, the six stage names and the up to `40 rooms` boundary survive verbatim | Turn 2 reply, rendered Epic block and its label |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`

### Commands

1. `sandbox: confirm both attachments sit at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Epic -> operator: check the kind, the house sections, the six child stories, the Added Later group and every brief value against the brief`

### Expected

Step 1 fixes the panel baseline with only `context/` populated. Step 2 returns one Epic question as its own clarification block in the Epic lane, and no Epic block. A question that also asks for a fact the brief states is the advisory reading in root section 5 and never fails the scenario. Step 3 proves the wait state.

Step 4 finds an Epic with no story preamble and an H1 such as `# Epic - Partner Hub - Self-onboarding`. `## About` opens with a narrative saying the work splits into child stories. `### Problem` carries `11 business days` and `38%`. `### Goal` carries `3 business days` for independent properties with up to `40 rooms`, and `1,500` properties by `2027-06-30`. `### Solution` follows, and `#### **References**` appears only when a link is supplied, never empty and never with an invented link.

`## Scope` names `Sign-up and verification`, `Property profile and photos`, `Rooms and rates setup`, `Policies and city tax`, `Payout details and identity checks` and `Go-live review queue` as plain-text child stories, and a `#### Added Later` group holds connecting a `channel manager`. Chains and properties over `40 rooms` stay out, as the brief says. A few release-level acceptance criteria close the Epic. Any other brief value it states, such as `8 photos`, `20 MB` or `1 business day`, matches the brief exactly.

`## Delivery` is optional here. The brief asks for an epic the squads can size, so a Delivery close with `TBD...` where the brief gives no figure is accepted, and so is an Epic that ends on Acceptance criteria.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the Epic's Problem, Goal and Scope sections and its acceptance criteria.

### Pass / fail

- **Pass**: One Epic question and no early draft, then one house-format Epic that names its kind, lists exactly the six stages verbatim as plain-text child stories with connecting a channel manager under Added Later, carries `11 business days`, `38%`, `3 business days`, `1,500` and `2027-06-30` verbatim, states every other brief value it uses exactly as the brief does, holds no `## Requirements`, invents no link or estimate and claims no file
- **Fail**: The runtime drafts in Turn 1, asks or labels under another artifact word, opens the Story scaffold, rounds or rewrites a brief value, adds, merges or drops a child story, brings chains, properties over `40 rooms` or channel manager properties into first-release scope, adds `## Requirements`, ticket header fields, story points or INVEST notes, invents a link, leaves a template slot unfilled or claims a local save

### Failure triage

1. Check the ESCALATE IF intake rule in `Custom Instructions.md` line 108 and the Epic clarification label at line 228
2. Check the Epic scaffold and its Notes For Use in `Product Owner - Assets - Epic Template` lines 22 to 102
3. Reconcile every number and stage name in the Epic against `roamstay-partner-self-onboarding-brief.md` and restore any rounded or renamed value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PEP-001 | Epic from strategy brief | Verify Project `$epic` on a strategy brief asks one Epic question, then renders an Epic built from the brief | `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.` | 1. Attachments and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Epic block | Step 1: baseline known. Step 2: one Epic question block in the Epic lane. Step 3: child stories and first release cut supplied. Step 4: house Epic with the six stages, the brief's values verbatim and its label | Both replies, rendered blocks, labels, Problem, Goal, Scope and criteria | PASS if the question, the Epic shape, the six child stories and the brief's values all match and no file is claimed. FAIL otherwise | 1. Check the command intake rule. 2. Check the Epic scaffold. 3. Check the brief's values |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | One scaffold at lines 58 and 79, rendering without a panel at line 85, the ESCALATE IF intake rule at line 108, the Epic shape at line 140 and the Epic and clarification labels at lines 227 and 228 |
| [`Product Owner - Templates - Story Mode - v0.403.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.403.md) | Clarification block at line 42, Epic kind at line 102, stated child-story set at line 110, Delivery opt-in at lines 131 and 132, Epic H1 at line 146 and Epic draft order at line 182 |
| [`Product Owner - Assets - Epic Template - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Epic%20Template%20-%20v0.101.md) | Epic scaffold at lines 22 to 93 and its Notes For Use at lines 98 to 102 |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Roamstay surfaces, squads and the epic title pattern |
| [`roamstay-partner-self-onboarding-brief.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-partner-self-onboarding-brief.md) | The six stages, the numbers and the boundaries the Epic carries |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PEP-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/epic-from-strategy-brief.md`

---
title: "SEP-001 -- Epic from strategy brief"
description: "Validates an explicit $epic request built on a partner self-onboarding strategy brief: one Epic question in the Epic lane, then a house-format Epic whose child stories and numbers come from the brief verbatim."
version: 1.0.0.0
---

# SEP-001 -- Epic from strategy brief

This scenario validates an explicit `$epic` request at Roamstay, from the Epic question through a house-format Epic export built from a strategy brief.

---

## 1. OVERVIEW

A head of product types `$epic` for Partner Hub self-onboarding, points at Freya's strategy brief and the Roamstay context, and says the first release cut is not agreed. The command routes to Story Mode in the Epic shape without supplying that direction, so the runtime asks one consolidated Epic question in the Epic lane and waits. Turn 2 settles the child-story set and the cut. The Epic that follows names the brief's six stages as its child stories, carries the brief's numbers verbatim, puts connecting a channel manager under Added Later and keeps every boundary the brief draws.

### Why this matters

A strategy brief carries the numbers a director will hold the squads to. `11 business days` written as about two weeks, `38%` as about a third or `2027-06-30` as mid-2027 is a different claim, and the squads would size against it. The brief also draws the line the first release depends on: independent properties with up to `40 rooms`, no chains and no property that uses a channel manager.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$epic` on a strategy brief asks one Epic question, then saves a house-format Epic whose child stories, numbers and boundaries come from the brief
- Real user request: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`
- Prompt: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-partner-self-onboarding-brief.md](../../../benchmark/fixtures/companies/roamstay/roamstay-partner-self-onboarding-brief.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/` before the export baseline
- Expected execution process: Start fresh, submit Turn 1, capture the Epic question and its clarification export, answer in Turn 2 in the same session and inspect the Epic export on the next number
- Expected signals: Turn 1 routes to Story Mode in the Epic shape, asks one consolidated question covering the first release cut and the child-story set, exports `export/[###] - Epic-partner-self-onboarding-clarification.md`, reads it back, replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns) and creates no draft. Turn 2 names the Epic kind in the reply, saves `export/[###] - Epic-partner-self-onboarding.md` on the next number, reads it back and replies with its path, the read-back line and the `HVR self-scan:` line. The Epic carries `11 business days` and `38%` in Problem, `3 business days`, `1,500` and `2027-06-30` in Goal, the six stage names in `## Scope` and connecting a `channel manager` under `#### Added Later`
- Desired user-visible outcome: One Epic question, then one Roamstay Epic the Partner, Ops Tools and Payments squads can plan from, with the brief's numbers intact
- Size band (advisory): 90 to 150 lines of Epic body
- Pass/fail: PASS if Turn 1 asks one Epic question in the Epic lane and drafts nothing, and Turn 2 saves one Epic in the house shape (a `# Epic - ` H1 with no story preamble, `## About` holding `### Problem`, `### Goal`, `### Solution` and `#### **References**`, `## Scope` naming exactly six first-release child stories as plain text, one per stage name verbatim, plus `#### Added Later` holding the channel manager connection, release-level `## Acceptance criteria` in numbered `1\.` blocks each closed by its Mark-as-done line, no `## Requirements`, no ticket header fields, story points or INVEST notes), names the kind, carries `11 business days`, `38%`, `3 business days`, `1,500` and `2027-06-30` verbatim and invents no link. FAIL if it drafts in Turn 1, asks or saves under another artifact word, rounds or rewrites a brief value, adds, merges or drops a child story, brings chains, properties over `40 rooms` or channel manager properties into first-release scope, fills an estimate the brief never gave or leaves a template slot such as `{link}` unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.` | Route `$epic` to Story Mode in the Epic shape and load only `story-mode.md` with `epic-template.md`. The command does not supply the open first release cut, so ask one consolidated Epic question covering the cut and whether the brief's six stages are the child stories, export it in the Epic lane, read it back and wait. Create no draft | Epic intent, the brief and the Roamstay context stay selected, and no Epic file exists | Turn 1 reply, clarification export, read-back result and clean draft ledger |
| 2 | `One child story per stage in Freya's brief, all six in the first release. Connecting a channel manager goes under Added Later. The goal and target are Freya's, use them as she wrote them.` | Draft from `epic-template.md`: `## About` with Problem, Goal, Solution and References, `## Scope` with the six stages as plain-text child stories and an Added Later group for connecting a channel manager, then release-level criteria. Save it on the next number, read it back and name the Epic kind in the reply | The brief's numbers, the six stage names and the up to `40 rooms` boundary survive verbatim, and the clarification file is untouched | Turn 2 reply, Epic export, read-back result and the unchanged clarification file |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`

### Commands

1. `sandbox: confirm both attachments sit at context/ -> sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new Epic export -> operator: check the kind, the house sections, the six child stories, the Added Later group and every brief value against the brief`

### Expected

Step 1 fixes the baseline with only `context/` populated. Step 2 returns one Epic question and one clarification file in the Epic lane, and no Epic file. A question that also asks for a fact the brief states is the advisory reading in root section 5 and never fails the scenario. Step 3 proves the wait state.

Step 4 finds an Epic with no story preamble and an H1 such as `# Epic - Partner Hub - Self-onboarding`. `## About` opens with a narrative saying the work splits into child stories. `### Problem` carries `11 business days` and `38%`. `### Goal` carries `3 business days` for independent properties with up to `40 rooms`, and `1,500` properties by `2027-06-30`. `### Solution` and `#### **References**` follow, with no invented link.

`## Scope` names `Sign-up and verification`, `Property profile and photos`, `Rooms and rates setup`, `Policies and city tax`, `Payout details and identity checks` and `Go-live review queue` as plain-text child stories, and a `#### Added Later` group holds connecting a `channel manager`. Chains and properties over `40 rooms` stay out, as the brief says. A few release-level acceptance criteria close the Epic. Any other brief value it states, such as `8 photos`, `20 MB` or `1 business day`, matches the brief exactly.

`## Delivery` is optional here. The brief asks for an epic the squads can size, so a Delivery close with `TBD...` where the brief gives no figure is accepted, and so is an Epic that ends on Acceptance criteria.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the clarification file, the Epic's Problem, Goal and Scope sections and its acceptance criteria.

### Pass / fail

- **Pass**: One Epic question and no early draft, then one house-format Epic that names its kind, lists exactly the six stages verbatim as plain-text child stories with connecting a channel manager under Added Later, carries `11 business days`, `38%`, `3 business days`, `1,500` and `2027-06-30` verbatim, states every other brief value it uses exactly as the brief does, holds no `## Requirements` and invents no link or estimate
- **Fail**: The runtime drafts in Turn 1, asks or saves under another artifact word, loads the Story scaffold, rounds or rewrites a brief value, adds, merges or drops a child story, brings chains, properties over `40 rooms` or channel manager properties into first-release scope, adds `## Requirements`, ticket header fields, story points or INVEST notes, invents a link or leaves a template slot unfilled

### Failure triage

1. Check the explicit-command intake rule in `AGENTS.md` line 287 and the Epic clarification lane in `SKILL.md` line 208
2. Check the Epic scaffold and its Notes For Use in `epic-template.md` lines 41 to 121
3. Reconcile every number and stage name in the Epic against `roamstay-partner-self-onboarding-brief.md` and restore any rounded or renamed value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SEP-001 | Epic from strategy brief | Verify `$epic` on a strategy brief asks one Epic question, then saves an Epic built from the brief | `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.` | 1. Attachments and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Epic export | Step 1: baseline known. Step 2: one Epic question in the Epic lane. Step 3: child stories and first release cut supplied. Step 4: house Epic with the six stages and the brief's values verbatim | Both replies, ledger, both export paths, Problem, Goal, Scope and criteria | PASS if the question, the Epic shape, the six child stories and the brief's values all match. FAIL otherwise | 1. Check the command intake rule. 2. Check the Epic scaffold. 3. Check the brief's values |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Epic-lane clarification at lines 79 and 82, and the explicit-command intake rule at line 287 |
| [`SKILL.md`](../../SKILL.md) | Epic export at line 207, clarification lane at line 208, Story-work clarification at line 252 and the Epic gate at lines 388 and 389 |
| [`story-mode.md`](../../references/story-mode.md) | Epic kind at line 126, stated child-story set at line 134, Delivery opt-in at lines 155 and 156, Epic H1 at line 170, Epic draft order at line 206 and Epic export at line 381 |
| [`epic-template.md`](../../assets/epic-template.md) | Epic scaffold at lines 41 to 112 and its Notes For Use at lines 117 to 121 |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Roamstay surfaces, squads and the epic title pattern |
| [`roamstay-partner-self-onboarding-brief.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-partner-self-onboarding-brief.md) | The six stages, the numbers and the boundaries the Epic carries |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SEP-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/epic-from-strategy-brief.md`

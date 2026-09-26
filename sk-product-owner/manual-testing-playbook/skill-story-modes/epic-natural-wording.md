---
title: "SEP-002 -- Epic natural wording"
description: "Validates a no-command request to write an epic for Loomlist offline mode: the Epic shape and lane from wording alone, one Epic question, then an Epic that keeps Web out of scope and the conflict decision open."
version: 1.1.0.0
---

# SEP-002 -- Epic natural wording

This scenario validates a natural-language epic request at Loomlist, from the Epic question through a house-format Epic export built from an epic brief.

---

## 1. OVERVIEW

A head of product asks in plain words for an epic for offline mode, points at Oskar's brief and the Loomlist context, and says the split into child stories is not settled. No command token is present, so the framing "write an epic for" alone has to select Story Mode, the Epic shape and the Epic lane. The runtime asks one consolidated Epic question and waits. Turn 2 fixes one child story per area across iOS, Android and Desktop and opens offline mode to every plan. The Epic keeps Web out of scope and leaves conflict handling as a dependency on the sync decision rather than choosing an answer.

### Why this matters

Natural wording is where a router most often falls back to a Story or a generic intake question. The brief also carries two facts a confident draft tends to smooth over: `Web is out of scope`, and how sync-service handles conflicting edits stays open until Joana decides on `2026-10-09`. An Epic that adds Web or picks a merge model states a decision nobody made.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a no-command request to write an epic resolves the Epic shape and lane, asks one Epic question, then saves an Epic that keeps the brief's scope, numbers and open dependency
- Real user request: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`
- Prompt: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-offline-mode-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/` before the export baseline
- Expected execution process: Start fresh, submit Turn 1, capture the Epic question and its clarification export, answer in Turn 2 in the same session and inspect the Epic export on the next number
- Expected signals: Turn 1 routes the framing to Story Mode in the Epic shape with no command token, asks one consolidated question covering the child-story split, exports `export/[###] - Epic-offline-mode-clarification.md`, reads it back, replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns) and creates no draft. Turn 2 names the Epic kind in the reply, saves `export/[###] - Epic-offline-mode.md` on the next number, reads it back and replies with its path, the read-back line and the `HVR self-scan:` line. The Epic carries `23%` and `31%` in Problem, names `Offline reading`, `Offline editing and creation`, `Sync on reconnect` and `Offline indicator and storage settings` as its four child stories, says Web is out of scope and leaves conflict handling open until the `2026-10-09` decision
- Desired user-visible outcome: One Epic question, then one Loomlist Epic the Sync and Mobile Platform teams can plan from, with Web out and the conflict decision still open
- Size band (advisory): 80 to 140 lines of Epic body
- Pass/fail: PASS if Turn 1 resolves the Epic kind from wording alone, asks one Epic question in the Epic lane and drafts nothing, and Turn 2 saves one Epic in the house shape (a `# Epic - ` H1 with no story preamble, `## About` holding `#### Problem`, `#### Goal` and `#### Solution` plus `#### **References**` only when a link is supplied, never empty and never with an invented link, `## Scope` naming exactly the four areas verbatim as plain-text child stories that each cover iOS, Android and Desktop, release-level `## Acceptance criteria` in numbered `1\.` blocks each closed by its Mark-as-done line, no `## Requirements`, no ticket header fields, story points or INVEST notes), names the kind, carries `23%` and `31%` verbatim, keeps Web out of every child story and criterion and names conflict handling as a dependency on the `2026-10-09` decision. FAIL if it asks in the intake or Story lane, drafts in Turn 1, splits a child story per platform, adds Web or an item the brief lists as out of scope, states a conflict-handling approach as decided, limits offline mode to a plan, alters a brief value or invents a link
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.` | Read "write an epic for" as Epic framing, route to Story Mode in the Epic shape and load only `story-mode.md` with `epic-template.md`. The child-story set is unsettled, so ask one consolidated Epic question covering the split, export it in the Epic lane, read it back and wait. Create no draft | Epic intent, the brief and the Loomlist context stay selected, and no Epic file exists | Turn 1 reply, clarification export, read-back result and clean draft ledger |
| 2 | `Follow his four areas, one child story each, and each story covers iOS, Android and Desktop together. Offline mode is for every plan, Free included.` | Draft from `epic-template.md`: `## About` with Problem, Goal and Solution plus References only when a link is supplied, `## Scope` with the four areas as plain-text child stories across iOS, Android and Desktop, then release-level criteria. State the open conflict-handling dependency without deciding it. Save it on the next number, read it back and name the Epic kind in the reply | Web stays out, no plan limit appears, the brief's numbers and the decision date survive verbatim, and the clarification file is untouched | Turn 2 reply, Epic export, read-back result and the unchanged clarification file |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`

### Commands

1. `sandbox: confirm both attachments sit at context/ -> sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new Epic export -> operator: check the kind, the house sections, the four child stories, the Web boundary, the dependency and every brief value against the brief`

### Expected

Step 1 fixes the baseline with only `context/` populated. Step 2 returns one Epic question and one clarification file in the Epic lane, and no Epic file. A question that also asks for a fact the brief states is the advisory reading in root section 5 and never fails the scenario. Step 3 proves the wait state.

Step 4 finds an Epic with no story preamble and an H1 such as `# Epic - Member - Offline mode`. `## About` opens with a narrative saying the work splits into child stories. `#### Problem` carries `23%` and `31%`. `#### Goal` covers opening, reading, editing and creating pages without a connection on iOS, Android and Desktop, on every plan. `#### Solution` follows, and `#### **References**` appears only when a link is supplied, never empty and never with an invented link.

`## Scope` names `Offline reading`, `Offline editing and creation`, `Sync on reconnect` and `Offline indicator and storage settings` as plain-text child stories, one per area and none per platform. The Epic says Web is out of scope and keeps the brief's other exclusions out. It names conflict handling as not settled, with offline editing and sync on reconnect depending on the sync decision due on `2026-10-09`, and it describes today's conflict behavior, if at all, only as `block-level last-writer-wins`. Any other brief value it states, such as `500 most recently opened pages`, `1 GB`, `30 seconds` or `Q1 2027`, matches the brief exactly. A few release-level acceptance criteria close the Epic, and none asserts how a conflict resolves.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the clarification file, the Epic's Problem, Goal and Scope sections, the dependency line and its acceptance criteria.

### Pass / fail

- **Pass**: One Epic question in the Epic lane from wording alone and no early draft, then one house-format Epic that names its kind, lists exactly the four areas verbatim as plain-text child stories across iOS, Android and Desktop, carries `23%` and `31%` verbatim, keeps Web out of scope, leaves conflict handling open on the `2026-10-09` decision, holds no `## Requirements` and invents no link
- **Fail**: The runtime asks in the intake or Story lane, drafts in Turn 1, loads the Story scaffold, splits a child story per platform, adds Web or another excluded item, picks a merge model or an option as decided, limits offline mode to a plan, alters a brief value, adds `## Requirements`, ticket header fields, story points or INVEST notes, invents a link or leaves a template slot unfilled

### Failure triage

1. Check the natural framing rule in `AGENTS.md` line 213 and `SKILL.md` line 142, and the Epic clarification lane in `SKILL.md` line 208
2. Check the Epic scaffold and its Notes For Use in `epic-template.md` lines 41 to 121
3. Reconcile Scope, Goal and the dependency against `loomlist-offline-mode-brief.md`, and strike any Web item or conflict-handling decision

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SEP-002 | Epic natural wording | Verify a no-command epic request resolves the Epic lane, asks one Epic question, then saves an Epic that keeps the brief's scope and open dependency | `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.` | 1. Attachments and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Epic export | Step 1: baseline known. Step 2: one Epic question in the Epic lane. Step 3: child-story split and plan scope supplied. Step 4: house Epic with the four areas, Web out and the dependency open | Both replies, ledger, both export paths, Problem, Goal, Scope, dependency and criteria | PASS if the lane, the Epic shape, the four child stories, the Web boundary and the open dependency all match. FAIL otherwise | 1. Check the framing rule. 2. Check the Epic scaffold. 3. Check the brief's scope |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Epic-lane clarification at lines 79 and 82, and the "write an epic for X" route at line 213 |
| [`SKILL.md`](../../SKILL.md) | Epic triggers at line 44, shape resolution by framing at line 142, Epic export at line 207, clarification lane at line 208 and the Epic gate at lines 388 and 389 |
| [`story-mode.md`](../../references/story-mode.md) | Epic kind at line 126, natural framing at line 131, stated child-story set at line 134, Epic H1 at line 170, Epic draft order at line 206 and Epic export at line 381 |
| [`epic-template.md`](../../assets/epic-template.md) | Epic scaffold at lines 41 to 112 and its Notes For Use at lines 117 to 121 |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Epic-lane clarification at line 93 and the Story intake gate at lines 169 to 173 |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Loomlist surfaces, plans, teams and the epic title pattern |
| [`loomlist-offline-mode-brief.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md) | The four areas, the numbers, the Web exclusion and the open conflict dependency |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SEP-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/epic-natural-wording.md`

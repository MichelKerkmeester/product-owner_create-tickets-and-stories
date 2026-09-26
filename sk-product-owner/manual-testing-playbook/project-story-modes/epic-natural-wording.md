---
title: "PEP-002 -- Epic natural wording"
description: "Validates a no-command request to write an epic for Loomlist offline mode in a Project: the Epic shape and lane from wording alone, one Epic question block, then an Epic Deliverable Block that keeps Web out of scope and the conflict decision open."
version: 1.1.0.1
---

# PEP-002 -- Epic natural wording

This scenario validates a natural-language epic request at Loomlist, from the Epic question through a house-format Epic Deliverable Block built from an epic brief.

---

## 1. OVERVIEW

A head of product asks in plain words for an epic for offline mode, points at Oskar's brief and the Loomlist context, and says the split into child stories is not settled. No command token is present, so the framing "write an epic for" alone has to select Story Mode, the Epic shape and the Epic lane. The Project asks one consolidated Epic question and waits. Turn 2 fixes one child story per area across iOS, Android and Desktop and opens offline mode to every plan. The Epic keeps Web out of scope and leaves conflict handling as a dependency on the sync decision rather than choosing an answer.

### Why this matters

Natural wording is where a router most often falls back to a Story or a generic intake question. The brief also carries two facts a confident draft tends to smooth over: `Web is out of scope`, and how sync-service handles conflicting edits stays open until Joana decides on `2026-10-09`. An Epic that adds Web or picks a merge model states a decision nobody made.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a no-command request to write an epic resolves the Epic shape and lane, asks one Epic question, then renders an Epic that keeps the brief's scope, numbers and open dependency
- Real user request: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`
- Prompt: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-offline-mode-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit at `context/` before the Canvas baseline
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the Epic question and its clarification block, answer in Turn 2 in the same conversation and inspect the rendered Epic
- Expected signals: Turn 1 routes the framing to Story Mode in the Epic shape with no command token, asks one consolidated question covering the child-story split, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - Epic-offline-mode-clarification.md` and the `HVR self-scan:` line (root section 5, Clarification turns) and creates no draft. Turn 2 names the Epic kind in the reply, renders the Epic as its Deliverable Block under `Export-equivalent path: export/[NNN] - Epic-offline-mode.md` with the `HVR self-scan:` line and claims no file. The Epic carries `23%` and `31%` in Problem, names `Offline reading`, `Offline editing and creation`, `Sync on reconnect` and `Offline indicator and storage settings` as its four child stories, says Web is out of scope and leaves conflict handling open until the `2026-10-09` decision
- Desired user-visible outcome: One Epic question block, then one Loomlist Epic block the Sync and Mobile Platform teams can plan from, with Web out and the conflict decision still open
- Size band (advisory): 80 to 140 lines of Epic body
- Pass/fail: PASS if Turn 1 resolves the Epic kind from wording alone, asks one Epic question in the Epic lane and drafts nothing, and Turn 2 renders one Epic in the house shape (a `# Epic - ` H1 with no story preamble, `## About` holding `### Problem`, `### Goal` and `### Solution` plus `#### **References**` only when a link is supplied, never empty and never with an invented link, `## Scope` naming exactly the four areas verbatim as plain-text child stories that each cover iOS, Android and Desktop, release-level `## Acceptance criteria` in numbered `1\.` blocks each closed by its Mark-as-done line, no `## Requirements`, no ticket header fields, story points or INVEST notes), consults only the Epic scaffold where the transcript shows its reads (`Custom Instructions.md` lines 58 and 79), names the kind, carries `23%` and `31%` verbatim, keeps Web out of every child story and criterion, names conflict handling as a dependency on the `2026-10-09` decision and claims no file. FAIL if it asks in the intake or Story lane, drafts in Turn 1, splits a child story per platform, adds Web or an item the brief lists as out of scope, states a conflict-handling approach as decided, limits offline mode to a plan, alters a brief value, invents a link or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.` | Read "write an epic for" as Epic framing, route to Story Mode in the Epic shape and consult only the Story Mode knowledge with the Epic Template. The child-story set is unsettled, so ask one consolidated Epic question covering the split, render it as an Epic-lane clarification block and wait. Create no draft | Epic intent, the brief and the Loomlist context stay selected, and no Epic block exists | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Follow his four areas, one child story each, and each story covers iOS, Android and Desktop together. Offline mode is for every plan, Free included.` | Draft from the Epic Template: `## About` with Problem, Goal and Solution plus References only when a link is supplied, `## Scope` with the four areas as plain-text child stories across iOS, Android and Desktop, then release-level criteria. State the open conflict-handling dependency without deciding it. Render it as the Deliverable Block, name the Epic kind in the reply and claim no file | Web stays out, no plan limit appears, and the brief's numbers and the decision date survive verbatim | Turn 2 reply, rendered Epic block and its label |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`

### Commands

1. `sandbox: confirm both attachments sit at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Epic -> operator: check the kind, the house sections, the four child stories, the Web boundary, the dependency and every brief value against the brief`

### Expected

Step 1 fixes the panel baseline with only `context/` populated. Step 2 returns one Epic question as its own clarification block in the Epic lane, and no Epic block. A question that also asks for a fact the brief states is the advisory reading in root section 5 and never fails the scenario. Step 3 proves the wait state.

Step 4 finds an Epic with no story preamble and an H1 such as `# Epic - Member - Offline mode`. `## About` opens with a narrative saying the work splits into child stories. `### Problem` carries `23%` and `31%`. `### Goal` covers opening, reading, editing and creating pages without a connection on iOS, Android and Desktop, on every plan. `### Solution` follows, and `#### **References**` appears only when a link is supplied, never empty and never with an invented link.

`## Scope` names `Offline reading`, `Offline editing and creation`, `Sync on reconnect` and `Offline indicator and storage settings` as plain-text child stories, one per area and none per platform. The Epic says Web is out of scope and keeps the brief's other exclusions out. It names conflict handling as not settled, with offline editing and sync on reconnect depending on the sync decision due on `2026-10-09`, and it describes today's conflict behavior, if at all, only as `block-level last-writer-wins`. Any other brief value it states, such as `500 most recently opened pages`, `1 GB`, `30 seconds` or `Q1 2027`, matches the brief exactly. A few release-level acceptance criteria close the Epic, and none asserts how a conflict resolves.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the Epic's Problem, Goal and Scope sections, the dependency line and its acceptance criteria.

### Pass / fail

- **Pass**: One Epic question block in the Epic lane from wording alone and no early draft, then one house-format Epic that names its kind, lists exactly the four areas verbatim as plain-text child stories across iOS, Android and Desktop, carries `23%` and `31%` verbatim, keeps Web out of scope, leaves conflict handling open on the `2026-10-09` decision, holds no `## Requirements`, invents no link and claims no file
- **Fail**: The runtime asks in the intake or Story lane, drafts in Turn 1, opens the Story scaffold, splits a child story per platform, adds Web or another excluded item, picks a merge model or an option as decided, limits offline mode to a plan, alters a brief value, adds `## Requirements`, ticket header fields, story points or INVEST notes, invents a link, leaves a template slot unfilled or claims a local save

### Failure triage

1. Check the natural framing rule in `Product Owner - Templates - Story Mode` line 107 and the Epic clarification label in `Custom Instructions.md` line 228
2. Check the Epic scaffold and its Notes For Use in `Product Owner - Assets - Epic Template` lines 22 to 102
3. Reconcile Scope, Goal and the dependency against `loomlist-offline-mode-brief.md`, and strike any Web item or conflict-handling decision

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PEP-002 | Epic natural wording | Verify a no-command Project epic request resolves the Epic lane, asks one Epic question, then renders an Epic that keeps the brief's scope and open dependency | `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.` | 1. Attachments and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Epic block | Step 1: baseline known. Step 2: one Epic question block in the Epic lane. Step 3: child-story split and plan scope supplied. Step 4: house Epic with the four areas, Web out, the dependency open and its label | Both replies, rendered blocks, labels, Problem, Goal, Scope, dependency and criteria | PASS if the lane, the Epic shape, the four child stories, the Web boundary and the open dependency all match and no file is claimed. FAIL otherwise | 1. Check the framing rule. 2. Check the Epic scaffold. 3. Check the brief's scope |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | One scaffold at lines 58 and 79, rendering without a panel at line 85, the Epic shape at line 140 and the Epic and clarification labels at lines 227 and 228 |
| [`Product Owner - Templates - Story Mode - v0.403.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.403.md) | Clarification block at line 42, Epic kind at line 102, natural framing at line 107, stated child-story set at line 110, Epic H1 at line 146 and Epic draft order at line 182 |
| [`Product Owner - Assets - Epic Template - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Epic%20Template%20-%20v0.101.md) | Epic scaffold at lines 22 to 93 and its Notes For Use at lines 98 to 102 |
| [`Product Owner - System - Interactive Mode - v0.407.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.407.md) | Epic-lane clarification at line 70 and the Story intake gate at lines 146 to 150 |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Loomlist surfaces, plans, teams and the epic title pattern |
| [`loomlist-offline-mode-brief.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md) | The four areas, the numbers, the Web exclusion and the open conflict dependency |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PEP-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/epic-natural-wording.md`

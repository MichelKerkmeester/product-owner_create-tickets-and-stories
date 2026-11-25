---
title: "PBR-002 -- Single app in plain words"
description: "Validates that a plain-words briefing request routes to Briefing Mode, asks only the gap and renders a single app briefing."
version: 1.0.0.0
---

# PBR-002 -- Single app in plain words

This scenario turns a Roamstay Search PM's plain-words request for a design briefing into one briefing and checks that it routes to Briefing Mode and keeps every copy value as the notes wrote it.

---

## 1. OVERVIEW

A Search squad PM asks in plain words, with no command, for a design briefing for the product designer from the free cancellation filter notes. Tomas's notes carry the filter rules, the result card badge, the empty state, the tracking and the release, and the request does not say whether a design system block belongs in it. The runtime should route to Briefing Mode on the briefing framing, ask one question that holds only that gap and wait. After Turn 2 it writes one briefing for the Guest app alone.

### Why this matters

The badge string, its date pattern and the empty-state copy are what a design review ticks. `Free cancellation until 14 Oct` rewritten as a deadline label, or the tracking event written into a design requirement, leaves the review ticking lines no frame can show.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a no-command briefing request routes to Briefing Mode, asks only for the gap the notes leave, then renders one single app briefing that keeps every copy value verbatim
- Real user request: `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.`
- Prompt: `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the briefing question, submit Turn 2 in the same conversation and inspect the rendered briefing
- Expected signals: With no command, the briefing framing routes to Briefing Mode (`Custom Instructions.md` line 92). The first question asks only for what the request leaves out among the apps, the area and the design system block (`Product Owner - Templates - Briefing Mode.md` line 34), here the design system block. It renders the question as its own block, then `Export-equivalent path: export/[NNN] - briefing-[description]-clarification.md` and the `HVR self-scan:` line, and renders no draft (`Custom Instructions.md` line 259). Turn 2 renders the briefing as its Deliverable Block, then `Export-equivalent path: export/[NNN] - briefing-[description].md` (`Custom Instructions.md` line 253), names the briefing kind, carries the `HVR self-scan:` line and claims no file was written. The structure follows `Product Owner - Templates - Briefing Mode.md` lines 82 to 89 and the scaffold in `Product Owner - Assets - Design Briefing Template.md` lines 27 to 96, with spacing as line 122 sets out. The title reads `Briefing - ` with no team lead and names the area in full, such as `Briefing - Guest App - Search - Free Cancellation Filter`. The briefing holds `## About`, `## Briefing` and `## Requirements` as H2 with a `* * *` divider directly under every heading and nowhere else. About keeps the evidence with its source and period, about one in six pre-booking chats and `44%` of August bookings, and states the decision. There is one audience, so Requirements carries no audience heading and starts straight on its first facet. Requirements carry `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates` and `Clear filter` in backticks as the notes wrote them and place the filter below `Price` and `Star rating`. Briefing says the map view, sorting by deadline and any Partner Hub change are out of scope for design. The tracking event `filter_applied` with `filter_name` set to `free_cancellation`, the cheapest free cancellation rate on the card and the search-service first release order sit under `## Dev Handover`, never in Requirements. No design system block is added. The briefing carries no table and no bullet ending in a full stop
- Desired user-visible outcome: One briefing question block about the design system block, then one single app briefing that keeps the badge, the empty state and the date pattern as the notes wrote them
- Size band (advisory): 45 to 90 lines of briefing body
- Pass/fail: PASS if Turn 1 routes to Briefing Mode, asks one consolidated question, renders it as its own block with a briefing-lane `Export-equivalent path:` and the `HVR self-scan:` line and renders no draft, and Turn 2 renders one briefing block with its `Export-equivalent path:` that holds the structure the signals above name and claims no file. FAIL if it drafts in Turn 1, asks again for the apps, the area or the decision the notes give, rewrites a value (`14 October`, `DD MMM`, `312 results`), writes an audience heading for a single audience, puts the tracking event or the release order in Requirements, adds a design system block, or writes a number the notes do not give. A claim of a local save also fails
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.` | Route to Briefing Mode on the briefing framing, read both attachments, ask one consolidated question that holds only the design system block gap, render it as a briefing-lane clarification block and wait. Create no draft | Briefing intent, the Guest app and the Search area stay selected, and only the design system answer is owed | Rendered clarification block, its label and the no-file-write statement |
| 2 | `No design system block, the filter is the only thing design needs to cover. Everything in Tomas's notes is settled.` | Draft the briefing from the notes and the answer, render it as its Deliverable Block with its export-equivalent label, name the briefing kind and claim no file | Every copy value sits in Requirements as written, the logic sits under Dev Handover | Turn 2 reply, rendered briefing block, its label and the audience, facet and Open Questions sections |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered briefing -> operator: check the title, the sections, the audiences and every value against the source and the answer`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one briefing question about the design system block and one clarification block. Step 3 proves the wait state. Step 4 finds the title, the three core sections, no audience heading, the copy values in backticks and the logic under Dev Handover.

### Evidence

Capture both replies, both rendered blocks and both export-equivalent labels, the copy values in Requirements and the Dev Handover section.

### Pass / fail

- **Pass**: One briefing question about the design system block, no early draft, and one single app briefing with no audience heading and every copy value verbatim, and no file claim
- **Fail**: The runtime drafts early, asks again for what the notes give, rewrites a value, adds an audience heading or puts the tracking logic in Requirements, or claims a local save

### Failure triage

1. Check the briefing framing rule in `Custom Instructions.md`
2. Check the title, section and facet rules in `Product Owner - Templates - Briefing Mode` and the scaffold in `Product Owner - Assets - Design Briefing Template`
3. Reconcile every value in the notes against Requirements and move any tracking or release line out of Requirements into Dev Handover

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBR-002 | Single app in plain words | Verify a no-command briefing request routes to Briefing Mode, asks only for the gap the notes leave, then renders one single app briefing that keeps every copy value verbatim | `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the briefing | Step 2: one question about the design system block. Step 3: gap answered. Step 4: single app briefing with verbatim copy | both replies, both rendered blocks and both export-equivalent labels, the copy values in Requirements and the Dev Handover section | PASS if the question, the single audience and every verbatim value match. FAIL otherwise | 1. Check the briefing framing rule. 2. Check the title, section and facet rules. 3. Reconcile every value in the notes against Requirements and move any tracking or release line out of Requirements into Dev Handover |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 92 briefing route, line 83 explicit commands ask first, line 69 title rule, line 259 clarification label, line 253 briefing label |
| [`Product Owner - Templates - Briefing Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Briefing%20Mode.md) | Line 34 critical rules, line 82 title, lines 85 and 86 audiences and facets, line 89 source wording, line 95 spacing, line 63 build work stays Task |
| [`Product Owner - Assets - Design Briefing Template.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Design%20Briefing%20Template.md) | Lines 27 to 96 briefing scaffold and its notes for use |
| [`Product Owner - System - Interactive Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode.md) | Line 276 Briefing Mode entry and flow |
| [`Product Owner - Assets - Interactive Response Templates.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates.md) | Line 87 briefing context question |
| [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Company context |
| [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md) | The source the request names |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBR-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/single-app-plain-words.md`

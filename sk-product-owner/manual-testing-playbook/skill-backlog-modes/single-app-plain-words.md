---
title: "SBR-002 -- Single app in plain words"
description: "Validates that a plain-words briefing request routes to Briefing Mode, asks only the gap and delivers a single app briefing."
version: 1.0.0.0
---

# SBR-002 -- Single app in plain words

This scenario turns a Roamstay Search PM's plain-words request for a design briefing into one briefing and checks that it routes to Briefing Mode and keeps every copy value as the notes wrote it.

---

## 1. OVERVIEW

A Search squad PM asks in plain words, with no command, for a design briefing for the product designer from the free cancellation filter notes. Tomas's notes carry the filter rules, the result card badge, the empty state, the tracking and the release, and the request does not say whether a design system block belongs in it. The runtime should route to Briefing Mode on the briefing framing, ask one question that holds only that gap and wait. After Turn 2 it writes one briefing for the Guest app alone.

### Why this matters

The badge string, its date pattern and the empty-state copy are what a design review ticks. `Free cancellation until 14 Oct` rewritten as a deadline label, or the tracking event written into a design requirement, leaves the review ticking lines no frame can show.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a no-command briefing request routes to Briefing Mode, asks only for the gap the notes leave, then exports one single app briefing that keeps every copy value verbatim
- Real user request: `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.`
- Prompt: `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1, capture the briefing question and its clarification export, submit Turn 2 in the same session and inspect the briefing export on the next number
- Expected signals: With no command, the briefing framing routes to Briefing Mode (`references/routing.md` line 34, `references/router-contract.md` line 143). The first question asks only for what the request leaves out among the apps, the area and the design system block (`references/briefing-mode.md` line 54), here the design system block. The question is saved as `export/[###] - briefing-[description]-clarification.md`, holds the question and nothing else, is read back, and the reply carries its path, its `Verified: read-back succeeded` line and the `HVR self-scan:` line (`AGENTS.md` line 84). Turn 2 saves `export/[###] - briefing-[description].md` on the next number (`AGENTS.md` line 98), reads it back and names the briefing kind. The structure follows `references/briefing-mode.md` lines 102 to 109 and the scaffold in `assets/design-briefing-template.md` lines 46 to 115, with spacing as line 141 sets out. The title reads `Briefing - ` with no team lead and names the area in full, such as `Briefing - Guest App - Search - Free Cancellation Filter`. The briefing holds `## About`, `## Briefing` and `## Requirements` as H2 with a `* * *` divider directly under every heading and nowhere else. About keeps the evidence with its source and period, about one in six pre-booking chats and `44%` of August bookings, and states the decision. There is one audience, so Requirements carries no audience heading and starts straight on its first facet. Requirements carry `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates` and `Clear filter` in backticks as the notes wrote them and place the filter below `Price` and `Star rating`. Briefing says the map view, sorting by deadline and any Partner Hub change are out of scope for design. The tracking event `filter_applied` with `filter_name` set to `free_cancellation`, the cheapest free cancellation rate on the card and the search-service first release order sit under `## Dev Handover`, never in Requirements. No design system block is added. The briefing carries no table and no bullet ending in a full stop
- Desired user-visible outcome: One briefing question about the design system block, then one single app briefing that keeps the badge, the empty state and the date pattern as the notes wrote them
- Size band (advisory): 45 to 90 lines of briefing body
- Pass/fail: PASS if Turn 1 routes to Briefing Mode, asks one consolidated question, saves it as a briefing-lane `-clarification` export reported with its path, its `Verified:` line and the `HVR self-scan:` line and drafts no briefing, and Turn 2 saves one briefing on the next number, read back and reported the same way, where the briefing holds the structure the signals above name. FAIL if it drafts in Turn 1, asks again for the apps, the area or the decision the notes give, rewrites a value (`14 October`, `DD MMM`, `312 results`), writes an audience heading for a single audience, puts the tracking event or the release order in Requirements, adds a design system block, or writes a number the notes do not give
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.` | Route to Briefing Mode on the briefing framing, read both attachments, ask one consolidated question that holds only the design system block gap, export it as a briefing-lane clarification, read it back and wait. Create no draft | Briefing intent, the Guest app and the Search area stay selected, and only the design system answer is owed | Clarification export, read-back line and a ledger holding only the clarification |
| 2 | `No design system block, the filter is the only thing design needs to cover. Everything in Tomas's notes is settled.` | Draft the briefing from the notes and the answer, save it on the next number, read it back and name the briefing kind in the reply | Every copy value sits in Requirements as written, the logic sits under Dev Handover, and the clarification file is unchanged | Turn 2 reply, briefing export, read-back line and the audience, facet and Open Questions sections |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the briefing export -> operator: check the title, the sections, the audiences and every value against the source and the answer`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one briefing question about the design system block and one clarification. Step 3 proves the wait state. Step 4 finds the title, the three core sections, no audience heading, the copy values in backticks and the logic under Dev Handover.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the copy values in Requirements and the Dev Handover section.

### Pass / fail

- **Pass**: One briefing question about the design system block, no early draft, and one single app briefing with no audience heading and every copy value verbatim
- **Fail**: The runtime drafts early, asks again for what the notes give, rewrites a value, adds an audience heading or puts the tracking logic in Requirements

### Failure triage

1. Check the briefing framing rule in `routing.md` and `router-contract.md`
2. Check the title, section and facet rules in `briefing-mode.md` and the scaffold in `design-briefing-template.md`
3. Reconcile every value in the notes against Requirements and move any tracking or release line out of Requirements into Dev Handover

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBR-002 | Single app in plain words | Verify a no-command briefing request routes to Briefing Mode, asks only for the gap the notes leave, then exports one single app briefing that keeps every copy value verbatim | `Turn Tomas's free cancellation filter notes into a design briefing for Ines. The notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the briefing | Step 2: one question about the design system block. Step 3: gap answered. Step 4: single app briefing with verbatim copy | both replies, the side-effect ledger, both export paths and read-back lines, the copy values in Requirements and the Dev Handover section | PASS if the question, the single audience and every verbatim value match. FAIL otherwise | 1. Check the briefing framing rule. 2. Check the title, section and facet rules. 3. Reconcile every value in the notes against Requirements and move any tracking or release line out of Requirements into Dev Handover |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Line 84 clarification export, line 98 briefing file name, line 129 briefing title, line 340 explicit commands ask first |
| [`briefing-mode.md`](../../references/briefing-mode.md) | Line 54 critical rules, line 102 title, lines 103 to 106 sections, audiences and facets, line 109 source wording, line 115 spacing, line 83 build work stays Task |
| [`design-briefing-template.md`](../../assets/design-briefing-template.md) | Lines 46 to 115 briefing scaffold and its notes for use |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Line 299 Briefing Mode entry and flow |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Line 111 briefing context question |
| [`routing.md`](../../references/routing.md) | Line 34 artifact framing without a command |
| [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Company context |
| [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md) | The source the request names |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBR-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/single-app-plain-words.md`

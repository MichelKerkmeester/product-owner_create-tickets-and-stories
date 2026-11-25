---
title: "PBR-001 -- Two audience briefing"
description: "Validates that `$briefing` asks one question and then renders a two audience briefing block for the wishlist."
version: 1.0.0.0
---

# PBR-001 -- Two audience briefing

This scenario turns a Fernhouse PM's request for a wishlist design briefing into one briefing and checks that the question, the audiences and the open decision all come out as the briefing rules set them.

---

## 1. OVERVIEW

A Storefront PM asks with `$briefing` for a design briefing on the wishlist, from the Customer Service lead's contact summary. The summary carries 412 contacts with their breakdown, the 50 item cap and a reply from Storefront that the apps save the wishlist on the device while web saves it to the account. The runtime should route to Briefing Mode, ask one consolidated question for what the summary leaves out and wait. After Turn 2 it writes one briefing for two audiences, with the decision settled and the lists already saved on a phone left open.

### Why this matters

A briefing is read by a design review that ticks lines off. A line it cannot tick, a number it cannot trace or a question already answered in Requirements sends the design team back to ask. The wishlist is also a decision the source calls open, so the one place it may sit is Open Questions with its owner.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$briefing` asks one question, then renders one briefing with two audience headings, source-dated numbers and the undecided phone lists left open
- Real user request: `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.`
- Prompt: `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-wishlist-feedback.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the briefing question, submit Turn 2 in the same conversation and inspect the rendered briefing
- Expected signals: `$briefing` routes to Briefing Mode and asks its context question before drafting (`Custom Instructions.md` line 83, `Product Owner - System - Interactive Mode.md` line 276, `Product Owner - Assets - Interactive Response Templates.md` line 87). It renders the question as its own block, then `Export-equivalent path: export/[NNN] - briefing-[description]-clarification.md` and the `HVR self-scan:` line, and renders no draft (`Custom Instructions.md` line 259). Turn 2 renders the briefing as its Deliverable Block, then `Export-equivalent path: export/[NNN] - briefing-[description].md` (`Custom Instructions.md` line 253), names the briefing kind, carries the `HVR self-scan:` line and claims no file was written. The structure follows `Product Owner - Templates - Briefing Mode.md` lines 82 to 89 and the scaffold in `Product Owner - Assets - Design Briefing Template.md` lines 27 to 96, with spacing as line 122 sets out. The title reads `Briefing - ` with no team lead, joins the two surfaces with `&` and names the area in full, such as `Briefing - Web & App - Wishlist - One List Everywhere`. The briefing holds `## About`, `## Briefing` and `## Requirements` as H2 with a `* * *` divider directly under every heading and nowhere else. About gives the contact numbers with their source and period, `412` contacts tagged wishlist from `2026-07-01` to `2026-09-20`, and states the decision in one or two sentences. Briefing holds the direction and restates no requirement. Requirements carries two ALL-CAPS H4 audience headings, one for Web and one for the apps, each with its divider and two blank lines before the second heading. Each facet is a bold Title Case lead line with `- []` items, such as `**Display**`, `**Validation**` and `**Existing Wishlists**`, and no prose or User Story sits under a facet. The `50 items` cap travels as the source wrote it. The lists already saved on a phone sit under `## Open Questions` with Lotte named as the decider and Requirements do not answer them. `## Success Signal` names the contact change we expect to see and invents no target number. The briefing carries no table, no `[Assumes: ...]` line and no bullet ending in a full stop
- Desired user-visible outcome: One briefing question block that collects the decision, the surfaces and the design system answer, then one briefing for Web and the app that a design review can tick line by line
- Size band (advisory): 60 to 110 lines of briefing body
- Pass/fail: PASS if Turn 1 routes to Briefing Mode, asks one consolidated question, renders it as its own block with a briefing-lane `Export-equivalent path:` and the `HVR self-scan:` line and renders no draft, and Turn 2 renders one briefing block with its `Export-equivalent path:` that holds the structure the signals above name and claims no file. FAIL if it drafts in Turn 1, leads the title with a team, abbreviates the area, writes audience headings as H3 or in Title Case or uses them for one audience, puts prose or a User Story under a facet, uses plain bullets in Requirements, answers the open phone-list question in Requirements, writes a number the source does not give such as a contact target or a sync time, or restates a requirement under Briefing. A claim of a local save also fails
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.` | Route to Briefing Mode on the exact `$briefing` token, read both attachments, ask one consolidated briefing question for what the summary leaves out, render it as a briefing-lane clarification block and wait. Create no draft | Briefing intent, the wishlist area and the Web and app surfaces stay selected, and the decision is still owed | Rendered clarification block, its label and the no-file-write statement |
| 2 | `Lotte decided that the app saves the wishlist to the account like web does, so it is one list everywhere, and the cap stays 50 items. What happens to the lists already saved on a phone is not decided yet and Lotte makes that call. The surfaces are Web and the apps, and no design system block belongs in it.` | Draft the briefing from the summary and the answer, render it as its Deliverable Block with its export-equivalent label, name the briefing kind and claim no file | Every number carries its source and period, the two audiences and the open phone-list question sit where the template puts them | Turn 2 reply, rendered briefing block, its label and the audience, facet and Open Questions sections |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered briefing -> operator: check the title, the sections, the audiences and every value against the source and the answer`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one briefing question and one clarification block. Step 3 proves the wait state. Step 4 finds the title, the three core sections, two ALL-CAPS H4 audience headings, facets of `- []` items, the open phone-list question and no number the source does not give.

### Evidence

Capture both replies, both rendered blocks and both export-equivalent labels, the audience headings, the facets and the Open Questions entry.

### Pass / fail

- **Pass**: One briefing question, no early draft, and one briefing with two ALL-CAPS H4 audience headings, source-dated numbers and the phone-list question left in Open Questions, and no file claim
- **Fail**: The runtime drafts early, leads the title with a team, mis-shapes the audience headings, writes prose under a facet, answers the open question or writes a number the source does not give, or claims a local save

### Failure triage

1. Check the explicit-command question rule in `Custom Instructions.md` and `Product Owner - System - Interactive Mode`
2. Check the title, section and facet rules in `Product Owner - Templates - Briefing Mode` and the scaffold in `Product Owner - Assets - Design Briefing Template`
3. Reconcile every number in the summary against About and Requirements, and move anything the source does not give to Open Questions

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBR-001 | Two audience briefing | Verify `$briefing` asks one question, then renders one briefing with two audience headings, source-dated numbers and the undecided phone lists left open | `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the briefing | Step 2: one briefing question. Step 3: decision supplied. Step 4: two audiences, dated numbers, open phone lists | both replies, both rendered blocks and both export-equivalent labels, the audience headings, the facets and the Open Questions entry | PASS if the wait, the audiences, the numbers and the open question all match. FAIL otherwise | 1. Check the explicit-command question rule. 2. Check the title, section and facet rules. 3. Reconcile every number in the summary against About and Requirements |

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
| [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Company context |
| [fernhouse-wishlist-feedback.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md) | The source the request names |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBR-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/two-audience-briefing.md`

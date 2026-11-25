---
title: "SBR-001 -- Two audience briefing"
description: "Validates that `$briefing` asks one question and then delivers a two audience briefing for the wishlist."
version: 1.0.0.0
---

# SBR-001 -- Two audience briefing

This scenario turns a Fernhouse PM's request for a wishlist design briefing into one briefing and checks that the question, the audiences and the open decision all come out as the briefing rules set them.

---

## 1. OVERVIEW

A Storefront PM asks with `$briefing` for a design briefing on the wishlist, from the Customer Service lead's contact summary. The summary carries 412 contacts with their breakdown, the 50 item cap and a reply from Storefront that the apps save the wishlist on the device while web saves it to the account. The runtime should route to Briefing Mode, ask one consolidated question for what the summary leaves out and wait. After Turn 2 it writes one briefing for two audiences, with the decision settled and the lists already saved on a phone left open.

### Why this matters

A briefing is read by a design review that ticks lines off. A line it cannot tick, a number it cannot trace or a question already answered in Requirements sends the design team back to ask. The wishlist is also a decision the source calls open, so the one place it may sit is Open Questions with its owner.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$briefing` asks one question, then exports one briefing with two audience headings, source-dated numbers and the undecided phone lists left open
- Real user request: `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.`
- Prompt: `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-wishlist-feedback.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1, capture the briefing question and its clarification export, submit Turn 2 in the same session and inspect the briefing export on the next number
- Expected signals: `$briefing` routes to Briefing Mode and asks its context question before drafting (`AGENTS.md` lines 233 and 340, `references/interactive-mode.md` line 299, `assets/interactive-response-templates.md` line 111). The question is saved as `export/[###] - briefing-[description]-clarification.md`, holds the question and nothing else, is read back, and the reply carries its path, its `Verified: read-back succeeded` line and the `HVR self-scan:` line (`AGENTS.md` line 84). Turn 2 saves `export/[###] - briefing-[description].md` on the next number (`AGENTS.md` line 98), reads it back and names the briefing kind. The structure follows `references/briefing-mode.md` lines 102 to 109 and the scaffold in `assets/design-briefing-template.md` lines 46 to 115, with spacing as line 141 sets out. The title reads `Briefing - ` with no team lead, joins the two surfaces with `&` and names the area in full, such as `Briefing - Web & App - Wishlist - One List Everywhere`. The briefing holds `## About`, `## Briefing` and `## Requirements` as H2 with a `* * *` divider directly under every heading and nowhere else. About gives the contact numbers with their source and period, `412` contacts tagged wishlist from `2026-07-01` to `2026-09-20`, and states the decision in one or two sentences. Briefing holds the direction and restates no requirement. Requirements carries two ALL-CAPS H4 audience headings, one for Web and one for the apps, each with its divider and two blank lines before the second heading. Each facet is a bold Title Case lead line with `- []` items, such as `**Display**`, `**Validation**` and `**Existing Wishlists**`, and no prose or User Story sits under a facet. The `50 items` cap travels as the source wrote it. The lists already saved on a phone sit under `## Open Questions` with Lotte named as the decider and Requirements do not answer them. `## Success Signal` names the contact change we expect to see and invents no target number. The briefing carries no table, no `[Assumes: ...]` line and no bullet ending in a full stop
- Desired user-visible outcome: One briefing question that collects the decision, the surfaces and the design system answer, then one briefing for Web and the app that a design review can tick line by line
- Size band (advisory): 60 to 110 lines of briefing body
- Pass/fail: PASS if Turn 1 routes to Briefing Mode, asks one consolidated question, saves it as a briefing-lane `-clarification` export reported with its path, its `Verified:` line and the `HVR self-scan:` line and drafts no briefing, and Turn 2 saves one briefing on the next number, read back and reported the same way, where the briefing holds the structure the signals above name. FAIL if it drafts in Turn 1, leads the title with a team, abbreviates the area, writes audience headings as H3 or in Title Case or uses them for one audience, puts prose or a User Story under a facet, uses plain bullets in Requirements, answers the open phone-list question in Requirements, writes a number the source does not give such as a contact target or a sync time, or restates a requirement under Briefing
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.` | Route to Briefing Mode on the exact `$briefing` token, read both attachments, ask one consolidated briefing question for what the summary leaves out, export it as a briefing-lane clarification, read it back and wait. Create no draft | Briefing intent, the wishlist area and the Web and app surfaces stay selected, and the decision is still owed | Clarification export, read-back line and a ledger holding only the clarification |
| 2 | `Lotte decided that the app saves the wishlist to the account like web does, so it is one list everywhere, and the cap stays 50 items. What happens to the lists already saved on a phone is not decided yet and Lotte makes that call. The surfaces are Web and the apps, and no design system block belongs in it.` | Draft the briefing from the summary and the answer, save it on the next number, read it back and name the briefing kind in the reply | Every number carries its source and period, the two audiences and the open phone-list question sit where the template puts them, and the clarification file is unchanged | Turn 2 reply, briefing export, read-back line and the audience, facet and Open Questions sections |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the briefing export -> operator: check the title, the sections, the audiences and every value against the source and the answer`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one briefing question and one clarification. Step 3 proves the wait state. Step 4 finds the title, the three core sections, two ALL-CAPS H4 audience headings, facets of `- []` items, the open phone-list question and no number the source does not give.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the audience headings, the facets and the Open Questions entry.

### Pass / fail

- **Pass**: One briefing question, no early draft, and one briefing with two ALL-CAPS H4 audience headings, source-dated numbers and the phone-list question left in Open Questions
- **Fail**: The runtime drafts early, leads the title with a team, mis-shapes the audience headings, writes prose under a facet, answers the open question or writes a number the source does not give

### Failure triage

1. Check the explicit-command question rule in `AGENTS.md` and `interactive-mode.md`
2. Check the title, section and facet rules in `briefing-mode.md` and the scaffold in `design-briefing-template.md`
3. Reconcile every number in the summary against About and Requirements, and move anything the source does not give to Open Questions

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBR-001 | Two audience briefing | Verify `$briefing` asks one question, then exports one briefing with two audience headings, source-dated numbers and the undecided phone lists left open | `$briefing Wishlist for Web and the app, from Maud's contact summary in context/fernhouse-wishlist-feedback.md. Company background is in context/fernhouse-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the briefing | Step 2: one briefing question. Step 3: decision supplied. Step 4: two audiences, dated numbers, open phone lists | both replies, the side-effect ledger, both export paths and read-back lines, the audience headings, the facets and the Open Questions entry | PASS if the wait, the audiences, the numbers and the open question all match. FAIL otherwise | 1. Check the explicit-command question rule. 2. Check the title, section and facet rules. 3. Reconcile every number in the summary against About and Requirements |

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
| [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Company context |
| [fernhouse-wishlist-feedback.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md) | The source the request names |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBR-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/two-audience-briefing.md`

---
title: "PST-003 -- Story refinement"
description: "Validates that a rough Fernhouse Story draft, refined in a Project with explicit leave to restructure, keeps its source file name, loses its PRD title prefix and build checklist, gains acceptance criteria and keeps every value it supplied."
version: 1.0.0.1
---

# PST-003 -- Story refinement

This scenario refines Priya's rough save card draft into the house Story shape as a Deliverable Block and checks that the restructure changes the shape without losing a single supplied value.

---

## 1. OVERVIEW

The Checkout PM sends `$s` with a draft that is deliberately rough: a `PRD -` title, a `**Checklist**` of build steps under Requirements, a `TBD...` line for the declined card copy and no acceptance criteria. Turn 1 gives explicit leave to restructure, which is what lets a refinement normalize a source (`Product Owner - Templates - Story Mode` line 210). The Project should ask its one Story question and wait. After Turn 2 supplies the declined card copy and a rule for the CVC limits, it renders the refined Story labelled with the draft's own file name, with a plain H1, the checklist's content carried as bold-lead constraint groups, an `## Acceptance criteria` section and every value the draft and the turns supplied.

### Why this matters

A refinement that drops `Expires 08/28` or writes `€150` as a rounded threshold hands the Checkout squad a Story that looks cleaner than the draft and says less. A refinement that keeps the checklist hands them build steps where the team expects constraints. Both happen quietly, so the label, the shape and the values are checked together.

---

## 2. SCENARIO CONTRACT

- Objective: Verify an authorized restructure of a rough Story draft into the house shape under the source file name label, with every supplied value intact
- Real user request: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`
- Prompt: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-save-card-draft.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-save-card-draft.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the Story question block, submit Turn 2 in the same conversation and inspect the rendered refinement
- Expected signals: Turn 1 routes to Story Mode on `$s`, reads both attachments and asks its one consolidated Story question, since an explicit command still asks before drafting (`Custom Instructions.md` line 108). It renders that question as its own block, then `Export-equivalent path: export/[NNN] - Story-save-card-clarification.md` and the `HVR self-scan:` line, and renders no draft. Turn 2 renders the refined Story as its Deliverable Block, then `Export-equivalent path: export/fernhouse-save-card-draft.md`, which keeps the source basename and takes no number (`Custom Instructions.md` line 229), names the Story kind, carries the `HVR self-scan:` line and claims no file was written. The refined Story sits under a plain H1 such as `Customer - Checkout - Save card for next time`, keeps the preamble, About, Problem, Solution and Expected outcomes with the draft's figures (17%, 9%, 68%) unaltered, and keeps the Saving a card, Paying with a saved card and Managing saved cards groups. The `**Checklist**` and its `- [ ]` build items are gone, and what they carried lands as constraints: only the payment provider's token, the brand, the last four digits and the expiry are stored, the checkbox is hidden in `guest checkout` on web, iOS and Android, a sixth card is refused, `Remove this card?` confirms a removal, the Turn 2 declined card copy replaces the `TBD...` line, and the three events (card saved, card removed, order paid with a saved card) are required with their names left to the Data team. The `€150` and `£130` limits apply to the order total including shipping. A new `## Acceptance criteria` section holds numbered Given/When/Then criteria for saving, paying with a saved card, removing one, guest checkout and a declined saved card, each closed by the Mark-as-done line. The export note above the draft's H1 is not graded either way
- Desired user-visible outcome: One Story question block, then one refined Story block labelled with the draft's own file name, in the house shape, with every value the draft and the turns supplied
- Size band (advisory): 70 to 130 lines of Story body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question, renders it as its own block with its `Export-equivalent path:` in the Story lane and the `HVR self-scan:` line and renders no draft, and Turn 2 renders one refined Story block with `Export-equivalent path: export/fernhouse-save-card-draft.md`, names the Story kind, carries the `HVR self-scan:` line and claims no file, where the refined Story has an H1 with no `PRD -` prefix, no `**Checklist**` and no `- [ ]` build item in Requirements, the checklist's content carried as bold-lead constraint groups, an `## Acceptance criteria` section of numbered Given/When/Then criteria each closed by the Mark-as-done line, and every supplied value verbatim: `Save this card for next time`, `unchecked by default`, `You can save up to 5 cards`, `Card ending 7031`, `Expires 08/28`, `CVC`, `€150`, `£130`, `Account > Payment methods`, `Remove this card?`, `guest checkout`, the Turn 2 copy `This card was declined. Choose another card or enter a new one.` and the order-total rule for the CVC limits. FAIL if it drafts in Turn 1, labels the refinement with a numbered `Story-` name, keeps the `PRD -` H1 or the build checklist, drops or rewrites a value (`€150.00`, `August 2028`, a card limit worded differently from `You can save up to 5 cards`), keeps `TBD...` for the declined card copy, invents event names, card brands or a stored field beyond the token, brand, last four and expiry, adds ticket header fields or story points, or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.` | Route to Story Mode on `$s`, read both attachments, record the leave to restructure, ask one consolidated Story question, render it as a Story-lane clarification block and wait. Create no draft | Story intent, the refinement of the save card draft and the leave to restructure stay selected | Turn 1 reply, rendered clarification block, its label and the no-file-write statement |
| 2 | `The declined card copy is agreed now: "This card was declined. Choose another card or enter a new one." The €150 and £130 CVC limits apply to the order total including shipping, and the Data team hasn't named the three events yet, so leave the names out.` | Refine the draft into the house Story shape, render it as its Deliverable Block labelled with the source basename, name the Story kind and claim no file | The refined Story carries every draft value and both Turn 2 facts | Turn 2 reply, rendered refinement block, its label and the Requirements and criteria |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered refinement -> operator: check the label, the H1, the Requirements groups, the criteria and every value against the draft and Turn 2`

### Expected

Step 1 fixes the panel baseline with `context/` holding the two attachments. Step 2 returns one Story question as its own clarification block. Step 3 proves the wait state. Step 4 finds the refined Story labelled `export/fernhouse-save-card-draft.md` with a plain H1, the preamble, `## About` with `### Problem`, `### Solution` and `#### **Expected outcomes**`, `## Requirements` as bold-lead groups with no `**Checklist**`, and `## Acceptance criteria` with numbered criteria each closed by the Mark-as-done line.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the refined H1, the Requirements groups with their backticked values and the acceptance criteria.

### Pass / fail

- **Pass**: One Story question block, no early draft, and one refined Story block labelled `export/fernhouse-save-card-draft.md` with a plain H1, no build checklist, bold-lead constraint groups, new acceptance criteria and every value from the draft and Turn 2 verbatim, claiming no file
- **Fail**: The runtime drafts early, labels the refinement with a numbered name, keeps the `PRD -` H1 or the checklist, drops or rewrites a value, keeps the `TBD...` copy line, invents event names, card brands or stored fields, adds ticket header fields or story points, or claims a local save

### Failure triage

1. Check the refinement rules and the authorization clause in `Product Owner - Templates - Story Mode` section 5
2. Check the Requirements and acceptance-criteria grammar in `Product Owner - Assets - Story Template`
3. Reconcile every value in the draft and Turn 2 against the refined block and restore any lost or rewritten value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PST-003 | Story refinement | Verify an authorized restructure of a rough draft keeps its file name label and every value in a Project | `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.` | 1. Stage and canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the refinement block | Step 1: baseline known. Step 2: one Story question block. Step 3: copy and rule supplied. Step 4: refined Story under the source name label with a plain H1, no checklist, criteria and every value | Both replies, rendered blocks, labels, H1, Requirements groups and criteria | PASS if the wait, the label, the H1, the groups, the criteria and every value all match. FAIL otherwise | 1. Check the refinement rules. 2. Check the house grammar. 3. Check each supplied value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 85 the block without a Canvas panel, line 108 an explicit command still asks, line 140 house format with no build checklist and no `PRD -` prefix, line 228 clarification label, line 229 the PRD refinement label, line 233 no `Path:`, `Saved:` or `Verified:` |
| [`Product Owner - Templates - Story Mode - v0.403.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.403.md) | Line 126 no `**Checklist**` in Requirements, line 143 the H1 with no `PRD -` prefix, lines 200 to 210 the refinement workflow, line 207 create-time checks only on request, line 209 the source basename, line 210 restructure needs explicit leave, lines 360 to 363 the refined label |
| [`Product Owner - Assets - Story Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Story%20Template%20-%20v0.100.md) | Lines 21 to 85 Story scaffold |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Lines 91 to 104 Story context question, including the refinement operation |
| [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Company context: stored card data limits, surfaces, story title pattern, tracking plan rule |
| [fernhouse-save-card-draft.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-save-card-draft.md) | The rough draft being refined |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PST-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/story-refinement.md`

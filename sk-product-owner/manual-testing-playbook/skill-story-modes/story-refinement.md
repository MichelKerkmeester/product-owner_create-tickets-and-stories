---
title: "SST-003 -- Story refinement"
description: "Validates that a rough Fernhouse Story draft, refined with explicit leave to restructure, keeps its source file name, loses its PRD title prefix and build checklist, gains acceptance criteria and keeps every value it supplied."
version: 1.0.0.0
---

# SST-003 -- Story refinement

This scenario refines Priya's rough save card draft into the house Story shape and checks that the restructure changes the shape without losing a single supplied value.

---

## 1. OVERVIEW

The Checkout PM sends `$s` with a draft that is deliberately rough: a `PRD -` title, a `**Checklist**` of build steps under Requirements, a `TBD...` line for the declined card copy and no acceptance criteria. Turn 1 gives explicit leave to restructure, which is what lets a refinement normalize a source (`story-mode.md` line 234). The runtime should ask its one Story question and wait. After Turn 2 supplies the declined card copy and a rule for the CVC limits, it saves the refined Story under the draft's own file name, with a plain H1, the checklist's content carried as `- []` constraint items under bold-lead groups, an `## Acceptance criteria` section and every value the draft and the turns supplied.

### Why this matters

A refinement that drops `Expires 08/28` or writes `€150` as a rounded threshold hands the Checkout squad a Story that looks cleaner than the draft and says less. A refinement that keeps the checklist hands them build steps where the team expects constraints. Both happen quietly, so the file name, the shape and the values are checked together.

---

## 2. SCENARIO CONTRACT

- Objective: Verify an authorized restructure of a rough Story draft into the house shape under the source file name, with every supplied value intact
- Real user request: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`
- Prompt: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-save-card-draft.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-save-card-draft.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1, capture the Story question and its clarification export, submit Turn 2 in the same session and inspect the refined export under the draft's file name
- Expected signals: Turn 1 routes to Story Mode on `$s`, reads both attachments and asks its one consolidated Story question, since an explicit command still asks before drafting (`AGENTS.md` line 287). It saves only that question as `export/[###] - Story-save-card-clarification.md`, reads it back, replies with its path, its `Verified:` read-back line and the `HVR self-scan:` line, and writes no draft. Turn 2 saves the refinement as `export/fernhouse-save-card-draft.md`, which keeps the source basename and takes no number (`AGENTS.md` line 45, `story-mode.md` line 233), reads it back, names the Story kind and carries the `HVR self-scan:` line, and `context/fernhouse-save-card-draft.md` stays byte for byte as supplied. The refined Story sits under a plain H1 such as `Customer - Checkout - Save card for next time`, keeps the preamble, About, Problem, Solution and Expected outcomes with the draft's figures (17%, 9%, 68%) unaltered, and keeps the Saving a card, Paying with a saved card and Managing saved cards groups. The `**Checklist**` and its `- [ ]` build items are gone, and what they carried lands as `- []` constraint items: only the payment provider's token, the brand, the last four digits and the expiry are stored, the checkbox is hidden in `guest checkout` on web, iOS and Android, a sixth card is refused, `Remove this card?` confirms a removal, the Turn 2 declined card copy replaces the `TBD...` line, and the three events (card saved, card removed, order paid with a saved card) are required with their names left to the Data team. The `€150` and `£130` limits apply to the order total including shipping. A new `## Acceptance criteria` section holds numbered Given/When/Then criteria for saving, paying with a saved card, removing one, guest checkout and a declined saved card, each closed by the Mark-as-done line. The export note above the draft's H1 is not graded either way
- Desired user-visible outcome: One Story question, then one refined Story saved under the draft's own file name, in the house shape, with every value the draft and the turns supplied
- Size band (advisory): 70 to 130 lines of Story body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question, saves only that question in the Story lane, reads it back and replies with its path, its `Verified:` line and the `HVR self-scan:` line with no draft, and Turn 2 saves the refinement as `export/fernhouse-save-card-draft.md`, reads it back, names the Story kind, carries the `HVR self-scan:` line and leaves `context/fernhouse-save-card-draft.md` unchanged, where the refined Story has an H1 with no `PRD -` prefix, no `**Checklist**` label and no build step in Requirements, the checklist's content carried as `- []` constraint items under bold-lead groups, with no `[ ]` box anywhere, an `## Acceptance criteria` section of numbered Given/When/Then criteria each closed by the Mark-as-done line, and every supplied value verbatim: `Save this card for next time`, `unchecked by default`, `You can save up to 5 cards`, `Card ending 7031`, `Expires 08/28`, `CVC`, `€150`, `£130`, `Account > Payment methods`, `Remove this card?`, `guest checkout`, the Turn 2 copy `This card was declined. Choose another card or enter a new one.` and the order-total rule for the CVC limits. FAIL if it drafts in Turn 1, saves the refinement under a numbered `Story-` name, overwrites the source, keeps the `PRD -` H1 or the build checklist, drops or rewrites a value (`€150.00`, `August 2028`, a card limit worded differently from `You can save up to 5 cards`), keeps `TBD...` for the declined card copy, invents event names, card brands or a stored field beyond the token, brand, last four and expiry, or adds ticket header fields or story points
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.` | Route to Story Mode on `$s`, read both attachments, record the leave to restructure, ask one consolidated Story question, export it as a Story-lane clarification, read it back and wait. Create no draft | Story intent, the refinement of the save card draft and the leave to restructure stay selected | Turn 1 reply, clarification export, read-back line and a ledger holding only the clarification |
| 2 | `The declined card copy is agreed now: "This card was declined. Choose another card or enter a new one." The €150 and £130 CVC limits apply to the order total including shipping, and the Data team hasn't named the three events yet, so leave the names out.` | Refine the draft into the house Story shape, save a copy under the source basename, read it back, confirm the source is unchanged and name the Story kind in the reply | The refined Story carries every draft value and both Turn 2 facts, the source draft is unchanged and the clarification file is unchanged | Turn 2 reply, refined export, read-back line, a hash of the source draft and the Requirements and criteria |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline and the draft's sha256`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open export/fernhouse-save-card-draft.md and hash context/fernhouse-save-card-draft.md -> operator: check the file name, the H1, the Requirements groups, the criteria and every value against the draft and Turn 2`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one Story question and one clarification file. Step 3 proves the wait state. Step 4 finds the refined Story at the draft's own file name with a plain H1, the preamble, `## About` with `#### Problem`, `#### Solution` and the `**Expected outcomes**` label, `## Requirements` as bold-lead groups of `- []` items with no `**Checklist**` label, and `## Acceptance criteria` with numbered criteria each closed by the Mark-as-done line, while the source draft hashes as it did in Step 1.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the source draft's hash before and after, the refined H1, the Requirements groups with their backticked values and the acceptance criteria.

### Pass / fail

- **Pass**: One Story question, no early draft, and one refined Story under `export/fernhouse-save-card-draft.md` with a plain H1, no build checklist, `- []` constraint items under bold-lead groups, new acceptance criteria and every value from the draft and Turn 2 verbatim, the source left unchanged
- **Fail**: The runtime drafts early, saves under a numbered name, overwrites the source, keeps the `PRD -` H1 or the checklist, drops or rewrites a value, keeps the `TBD...` copy line, invents event names, card brands or stored fields, or adds ticket header fields or story points

### Failure triage

1. Check the refinement rules and the authorization clause in `story-mode.md` section 5
2. Check the Requirements and acceptance-criteria grammar in `story-template.md`
3. Reconcile every value in the draft and Turn 2 against the refined file and restore any lost or rewritten value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SST-003 | Story refinement | Verify an authorized restructure of a rough draft keeps its file name and every value | `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.` | 1. Stage, baseline and hash -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the refined export and rehash the source | Step 1: baseline known. Step 2: one Story question. Step 3: copy and rule supplied. Step 4: refined Story under the source name with a plain H1, no checklist, criteria and every value | Both replies, ledger, both export paths, source hashes, H1, Requirements groups and criteria | PASS if the wait, the file name, the H1, the groups, the criteria, every value and the untouched source all match. FAIL otherwise | 1. Check the refinement rules. 2. Check the house grammar. 3. Check each supplied value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Line 45 a refined copy keeps the source file name, line 82 clarification export, line 287 an explicit command still asks |
| [`SKILL.md`](../../SKILL.md) | Line 208 clarification export name, line 209 refinement keeps the source basename, line 217 self-scan line, line 293 no build steps in a Story requirement |
| [`story-mode.md`](../../references/story-mode.md) | Line 150 no `**Checklist**` in Requirements, line 167 the H1 with no `PRD -` prefix, lines 224 to 234 the refinement workflow, line 231 create-time checks only on request, line 233 the source basename, line 234 restructure needs explicit leave |
| [`story-template.md`](../../assets/story-template.md) | Lines 40 to 104 Story scaffold, line 22 the refinement output path |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Lines 114 to 127 Story context question, including the refinement operation |
| [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Company context: stored card data limits, surfaces, story title pattern, tracking plan rule |
| [fernhouse-save-card-draft.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-save-card-draft.md) | The rough draft being refined |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SST-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/story-refinement.md`

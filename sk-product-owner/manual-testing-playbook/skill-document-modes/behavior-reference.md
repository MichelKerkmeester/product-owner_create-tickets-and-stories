---
title: "SDK-001 -- Behavior reference"
description: "Validates a no-command Doc request at Fernhouse that drafts a ClickUp behavior reference on discount stacking at once from its attachments, then applies a follow-up change that keeps the retired two-codes rule retired."
version: 2.0.0.0
---

# SDK-001 -- Behavior reference

This scenario validates natural-language Doc routing, a status-safe behavior reference drafted at once from Fernhouse's promotions rules and a follow-up change to the doc it delivered.

---

## 1. OVERVIEW

The request carries no command token. "Document how" routes it to Doc Mode (`AGENTS.md` line 211, `SKILL.md` line 110). With no command, the runtime asks one consolidated question only when purpose, audience, source authority, scope or source classification cannot be established safely (`doc-mode.md` line 67), and the attachments establish them. The rules note names its readers, CS, engineering and merchandisers checking a discount that looks wrong, and its authority: Colette owns it and promotions-service applies everything in it. Every rule sits under a Current rules or Retired rules heading, and the request names the scope. The notes are present, so the promised-source rule in `AGENTS.md` line 285 does not hold shape open, and "document how" reads as prediction, which picks Behavior reference without a preference question (`doc-mode.md` lines 258 and 260). Turn 1 therefore drafts at once and saves the doc in the doc lane on the first number.

The rules note mixes two statuses. Nine current rules sit beside one retired rule: two codes on one order were allowed until `2026-05-01` and are `retired` since. Turn 2 is a follow-up change to the delivered doc. It narrows the readers to CS agents and the Checkout engineers, names the rules note as the governing source and the context doc as background, asks for the two-codes rule to be in the doc with its retired label because CS still refunds those orders, and asks for how merchandisers set promotions up in Admin to be left out.

The rules settle most of Turn 2. The follow-up carries no command and leaves nothing unresolved, so the runtime revises without a question (`doc-mode.md` lines 67 and 196). The revision is a delivery with its own save, read-back and reply (`AGENTS.md` lines 44 to 47, `SKILL.md` line 213), and status labels travel with their claims (`doc-mode.md` line 154). The rules do not settle where the revision is saved. The refinement contract keeps the original file name (`AGENTS.md` lines 45 and 70 to 73, `SKILL.md` line 209, `doc-mode.md` line 324), and the new-document contract takes the next number (`AGENTS.md` line 44, `doc-mode.md` line 402). The refinement workflow is written for a document the user supplies (`doc-mode.md` line 294), and the Turn 1 doc is the runtime's own. Updating the Turn 1 export in place and saving the revision on the next number in the doc lane both pass, and that choice is not graded. For the same reason the grade reads the revised doc on its own terms, its shape, layout, values, status labels and the two requested changes, and not its diff from Turn 1 (`doc-mode.md` lines 298 to 314).

### Why this matters

A behavior reference that folds the retired two-codes rule into today's rules tells a CS agent a customer can still combine codes, and every refund call built on it is wrong. Status labels travel with their claims and are never normalized into current behavior (`doc-mode.md` line 154). A question the attachments already answer costs the requester a round and delivers nothing.

---

## 2. SCENARIO CONTRACT

- Objective: Verify no-command Doc routing that drafts a ClickUp behavior reference at once from the attachments, keeps Fernhouse's current and retired promotion rules apart and applies a follow-up change to the delivered doc
- Real user request: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-promotions-rules.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit unchanged at `context/fernhouse-context.md` and `context/fernhouse-promotions-rules.md` before the export baseline (root, Company context and attachments)
- Expected execution process: Start fresh, submit Turn 1, capture the doc export and its reply, submit the Turn 2 change in the same session, then inspect the revised doc export and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks no question and writes no clarification, saves `export/[###] - doc-discount-stacking.md` on the first number as a Behavior reference, reads it back and replies with the path, the `Verified: read-back succeeded` line with its line count, the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`doc-mode.md` line 412). Turn 2 asks no question, applies the change, saves the revised doc in the doc lane, over the Turn 1 export or on the next number, reads it back and replies with the path, the `Verified:` line, the `HVR self-scan:` line and the five summary lines. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: A behavior reference drafted straight from the attachments, then revised on request into the one CS agents and the Checkout engineers use to predict the discount on any cart
- Size band (advisory): 80 to 180 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Doc Mode and, with no question and no clarification, saves and reads back a Behavior reference in the doc lane on the first number with an Overview and a `## Behavior rules` body, `* * *` directly under every content heading, `*   ` bullets, sentence-case headings and no empty spacer heading in the file, stating the current rules with `one discount code per order`, `automatic promotions first`, `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap and `0.01` `half up` rounding verbatim, and Turn 2, with no question, delivers the revised doc in the doc lane with the same layout checks, every one of those values still verbatim, the two-codes rule in and labelled retired since `2026-05-01`, no account of how merchandisers set promotions up in Admin and nothing the two attachments do not state. Whether Turn 2 updates the Turn 1 export in place or saves on the next number is not graded. FAIL if Turn 1 asks a question or writes a clarification instead of drafting, routes to another mode or saves under another artifact word, or either doc presents the two-codes rule as current, alters a supplied value, invents a rule, number or example, or writes `---` dividers or hyphen bullets, or Turn 2 asks a question, drops the two-codes rule or its retired label, or keeps the merchandiser Admin setup in
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | Route to Doc Mode on the "document how" framing, read both attachments, take purpose, audience, authority, status and scope from the rules note and pick Behavior reference. Draft it from the rules note with its nine current rules as current behavior and their values verbatim, and any retired rule it carries under its own retired label. Apply the ClickUp layout, save it in the doc lane on the first number, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary. Ask no question and write no clarification | Doc Mode selected, one new doc export and no `-clarification` file, both `context/` files unchanged | Turn 1 reply, doc export and read-back line |
| 2 | `Thanks. A few changes: it's for CS agents and the Checkout engineers, so they can predict the discount on any cart, and it stays a behavior reference. Those two files are all there is, the rules note governs and the context doc is background only. Make sure the old two-codes rule is in there with its retired label, because CS still refunds those orders, and leave out how merchandisers set promotions up in Admin.` | Treat the message as a change to the delivered doc and ask nothing. Write it for CS agents and the Checkout engineers from the rules note, keep the nine current rules as current behavior with their values verbatim, keep the two-codes rule apart with its own retired label and its refund split, leave out how merchandisers set promotions up in Admin and keep the ClickUp layout. Save the revised doc in the doc lane, over the Turn 1 export or on the next number, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary | The retired label stays on the two-codes rule and no current rule loses its value or its exception. Where the revision saved is recorded but not graded | Turn 2 reply, revised doc export and read-back line |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> filesystem: record the export and context/ baselines`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the new doc export -> operator: confirm no clarification file exists and check the shape, the ClickUp layout and every promotion value against context/fernhouse-promotions-rules.md -> user: submit Turn 2 in the same session`
4. `filesystem: open the revised doc export -> operator: check the shape, the ClickUp layout, every promotion value, the retired label and the Admin exclusion against context/fernhouse-promotions-rules.md, and record whether the revision replaced the Turn 1 export or took the next number`
5. `filesystem: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one doc export on the first number and no clarification file. Step 3 finds a Behavior reference with an Overview and `## Behavior rules`, the two sections the shape cannot drop (`doc-templates.md` lines 115 and 400), `* * *` directly under each content heading, `*   ` bullets, sentence-case headings and no empty spacer heading, since a file export never carries one (`doc-mode.md` line 97), with every current rule's value exact. Step 4 finds the revised Behavior reference with the same layout checks and the current values unchanged. The two-codes rule sits apart, labelled retired since `2026-05-01` and never offered as something a customer can do today, and the doc gives no account of how merchandisers set promotions up in Admin. It sits at the Turn 1 path or on the next number in the doc lane, and either passes. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, the side-effect ledger with every export created or modified, both export paths and read-back lines, the doc headings with divider adjacency, the bullet markers, every promotion value in each doc, the status label on the two-codes rule, the Admin exclusion, both Doc quality summaries and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 drafts at once with no question, saving and reading back a Behavior reference in the doc lane on the first number that carries an Overview and `## Behavior rules`, passes the ClickUp layout gate and keeps every current rule's value verbatim, and Turn 2 delivers the revised doc with no question, the same layout and values, the two-codes rule in with its retired label and the merchandiser Admin setup left out, wherever in the doc lane it saved
- **Fail**: Turn 1 asks a question or writes a clarification instead of drafting, or routes outside Doc Mode, or either doc presents the two-codes rule as current, rounds or rewords a value such as `50%`, `0.01` or `STAFF-`, invents a rule, number or example, or writes `---` dividers, hyphen bullets or empty spacer headings into the file, or Turn 2 asks a question, drops the two-codes rule or its label, or keeps the merchandiser Admin setup

### Failure triage

1. Check the Doc routing phrase in `AGENTS.md` line 211, the no-command intake rule in `doc-mode.md` line 67 and the shape routing in `doc-mode.md` lines 258 and 260
2. Check each reply against the delivery sequence in `AGENTS.md` lines 44 to 47 and the Doc summary in `doc-mode.md` line 412
3. Re-read both docs against `context/fernhouse-promotions-rules.md`, restore any value that was rounded or reworded and put the retired label back on the two-codes rule (`doc-mode.md` lines 148 and 154)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-001 | Behavior reference | Verify no-command Doc routing that drafts a status-safe behavior reference on discount stacking at once, then applies a follow-up change | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the doc export and submit Turn 2 -> 4. Inspect the revised doc export -> 5. Compare context/ | Step 2: one doc export on the first number and no clarification. Step 3: behavior reference with the ClickUp layout and the rules' values. Step 4: revised doc with the values, the two-codes rule labelled retired and no Admin setup, saved anywhere in the doc lane. Step 5: attachments unchanged | Both replies, ledger, export paths, read-back lines, layout checks, promotion values and status labels | PASS if Turn 1 drafts with no question and both docs keep their sections, the layout and every value, with the revision keeping the retired label and dropping the Admin setup. FAIL otherwise | 1. Check Doc routing and no-command intake. 2. Check the delivery lines. 3. Check values and status labels |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Doc routing phrase, the promised-source rule, the delivery sequence and the new and refined export names |
| [`SKILL.md`](../../SKILL.md) | Documentation routing topic, Doc and refinement export names and the delivery reply |
| [`doc-mode.md`](../../references/doc-mode.md) | No-command intake rule, shape routing, source classification, refinement workflow, export contract and ClickUp output contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Behavior reference shape, status language and layout rules |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: Fernhouse company context |
| [`fernhouse-promotions-rules.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md) | Attachment: current promotion rules, worked examples and the retired two-codes rule |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/behavior-reference.md`

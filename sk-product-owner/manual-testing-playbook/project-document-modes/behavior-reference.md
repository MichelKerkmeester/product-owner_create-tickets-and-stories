---
title: "PDK-001 -- Behavior reference"
description: "Validates a no-command Doc request at Fernhouse that renders a ClickUp behavior reference Deliverable Block on discount stacking at once from its attachments, then applies a follow-up change that keeps the retired two-codes rule retired."
version: 2.0.0.1
---

# PDK-001 -- Behavior reference

This scenario validates natural-language Doc routing, a status-safe behavior reference drafted at once from Fernhouse's promotions rules and a follow-up change to the doc it delivered, in a Claude Project.

---

## 1. OVERVIEW

The request carries no command token. "Document how" routes it to Doc Mode (`Product Owner - System - Router Contract` line 899). With no command, the Project asks one consolidated question only when purpose, audience, source authority, scope or source classification cannot be established safely (`Product Owner - Templates - Doc Mode` line 43), and the attachments establish them. The rules note names its readers, CS, engineering and merchandisers checking a discount that looks wrong, and its authority: Colette owns it and promotions-service applies everything in it. Every rule sits under a Current rules or Retired rules heading, and the request names the scope. The notes are present, so the promised-source rule in `Custom Instructions.md` line 130 does not hold shape open, and "document how" reads as prediction, which picks Behavior reference without a preference question (`Product Owner - Templates - Doc Mode` lines 234 and 236). Turn 1 therefore renders the doc at once as its own block, labelled in the doc lane, with no file claim.

The rules note mixes two statuses. Nine current rules sit beside one retired rule: two codes on one order were allowed until `2026-05-01` and are `retired` since. Turn 2 is a follow-up change to the delivered doc. It narrows the readers to CS agents and the Checkout engineers, names the rules note as the governing source and the context doc as background, asks for the two-codes rule to be in the doc with its retired label because CS still refunds those orders, and asks for how merchandisers set promotions up in Admin to be left out.

The rules settle most of Turn 2. The follow-up carries no command and leaves nothing unresolved, so the Project revises without a question (`Product Owner - Templates - Doc Mode` lines 43 and 172). The revision is a delivery: the Deliverable Block comes first, then the export-equivalent path, the `HVR self-scan:` line and the quality status (`Custom Instructions.md` lines 85 and 86), with no claim or promise of a file (`Custom Instructions.md` line 101). Status labels travel with their claims (`Product Owner - Templates - Doc Mode` line 130). The rules do not settle which label the revision carries. A Doc refinement keeps the original file name (`Custom Instructions.md` line 231, `Product Owner - Templates - Doc Mode` lines 300 and 380), and a new Doc takes a new number (`Custom Instructions.md` line 225, `Product Owner - Templates - Doc Mode` line 378). The refinement workflow is written for a document the user supplies (`Product Owner - Templates - Doc Mode` line 270), and the Turn 1 doc is the Project's own. Reporting the Turn 1 label again and reporting a new `[NNN]` in the doc lane both pass, and that choice is not graded. For the same reason the grade reads the revised doc on its own terms, its shape, layout, values, status labels and the two requested changes, and not its diff from Turn 1 (`Product Owner - Templates - Doc Mode` lines 274 to 290).

### Why this matters

A behavior reference that folds the retired two-codes rule into today's rules tells a CS agent a customer can still combine codes, and every refund call built on it is wrong. Status labels travel with their claims and are never normalized into current behavior (`Product Owner - Templates - Doc Mode` line 130). A question the attachments already answer costs the requester a round and delivers nothing.

---

## 2. SCENARIO CONTRACT

- Objective: Verify no-command Doc routing that renders a ClickUp behavior reference at once from the attachments, keeps Fernhouse's current and retired promotion rules apart and applies a follow-up change to the delivered doc
- Real user request: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-promotions-rules.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit unchanged at `context/fernhouse-context.md` and `context/fernhouse-promotions-rules.md` before the Canvas panel baseline (root, Company context and attachments)
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the rendered reference and its reply, submit the Turn 2 change in the same conversation, then inspect the revised reference and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks no question and renders no clarification block, renders the Behavior reference as its own block under `Export-equivalent path: export/[NNN] - doc-discount-stacking.md`, then replies with the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`Custom Instructions.md` line 217) and claims no file. Turn 2 asks no question, applies the change, renders the revised reference as its own block under an `Export-equivalent path:` in the doc lane, the Turn 1 label or a new one, then replies with the `HVR self-scan:` line and the five summary lines and claims no file. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: A behavior reference block drafted straight from the attachments, then revised on request into the one CS agents and the Checkout engineers use to predict the discount on any cart
- Size band (advisory): 80 to 180 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Doc Mode and, with no question and no clarification block, renders a Behavior reference with a doc-lane export-equivalent label, an Overview and a `## Behavior rules` body, `* * *` directly under every content heading, `*   ` bullets and sentence-case headings, stating the current rules with `one discount code per order`, `automatic promotions first`, `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap and `0.01` `half up` rounding verbatim, and Turn 2, with no question, renders the revised reference with a doc-lane label, the same layout checks, every one of those values still verbatim, the two-codes rule in and labelled retired since `2026-05-01`, no account of how merchandisers set promotions up in Admin and nothing the two attachments do not state, with no file claim on either turn. Whether Turn 2 repeats the Turn 1 label or reports a new one is not graded. FAIL if Turn 1 asks a question or renders a clarification instead of drafting, routes to another mode or labels under another artifact word, or either doc presents the two-codes rule as current, alters a supplied value, invents a rule, number or example, or writes `---` dividers or hyphen bullets, or Turn 2 asks a question, drops the two-codes rule or its retired label, or keeps the merchandiser Admin setup in, or either reply prints `Path:`, `Saved:` or `Verified:` or claims or promises a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | Route to Doc Mode on the "document how" framing, read both attachments, take purpose, audience, authority, status and scope from the rules note and pick Behavior reference. Draft it from the rules note with its nine current rules as current behavior and their values verbatim, and any retired rule it carries under its own retired label. Apply the ClickUp layout, render it as its own block, then reply with the doc-lane export-equivalent label, the `HVR self-scan:` line and the five-line Doc summary. Ask no question, render no clarification and claim no file | Doc Mode selected, one reference block and no clarification block, both `context/` files unchanged | Turn 1 reply, rendered reference block and its label |
| 2 | `Thanks. A few changes: it's for CS agents and the Checkout engineers, so they can predict the discount on any cart, and it stays a behavior reference. Those two files are all there is, the rules note governs and the context doc is background only. Make sure the old two-codes rule is in there with its retired label, because CS still refunds those orders, and leave out how merchandisers set promotions up in Admin.` | Treat the message as a change to the delivered doc and ask nothing. Write it for CS agents and the Checkout engineers from the rules note, keep the nine current rules as current behavior with their values verbatim, keep the two-codes rule apart with its own retired label and its refund split, leave out how merchandisers set promotions up in Admin and keep the ClickUp layout. Render the revised reference as its own block, then reply with a doc-lane export-equivalent label, the Turn 1 label or a new one, the `HVR self-scan:` line and the five-line Doc summary. Claim no file | The retired label stays on the two-codes rule and no current rule loses its value or its exception. Which label the revision carries is recorded but not graded | Turn 2 reply, rendered revised reference block and its label |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered reference -> operator: confirm no clarification block exists and check the shape, the ClickUp layout, every promotion value and the export-equivalent label against context/fernhouse-promotions-rules.md -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the revised reference -> operator: check the shape, the ClickUp layout, every promotion value, the retired label, the Admin exclusion and the export-equivalent label against context/fernhouse-promotions-rules.md, and record which label the revision carries`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one reference block with a doc-lane label and no clarification block. Step 3 finds a Behavior reference with an Overview and `## Behavior rules`, the two sections the shape cannot drop (`Product Owner - Assets - Doc Templates` lines 94 and 379), `* * *` directly under each content heading, `*   ` bullets and sentence-case headings, with every current rule's value exact. Step 4 finds the revised Behavior reference with the same layout checks and the current values unchanged, under the Turn 1 label or a new one in the doc lane. The two-codes rule sits apart, labelled retired since `2026-05-01` and never offered as something a customer can do today, and the block gives no account of how merchandisers set promotions up in Admin. Spacer headings are not graded here. The skill twin fails them because a file export never carries one, and `Product Owner - Templates - Doc Mode` line 73 allows them in ClickUp-bound content, which the kernel does not say a rendered block is. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, both rendered blocks, both export-equivalent labels, the doc headings with divider adjacency, the bullet markers, every promotion value in each block, the status label on the two-codes rule, the Admin exclusion, both Doc quality summaries and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 renders at once with no question a Behavior reference with a doc-lane label that carries an Overview and `## Behavior rules`, passes the ClickUp layout gate and keeps every current rule's value verbatim, and Turn 2 renders the revised reference with no question, the same layout and values, the two-codes rule in with its retired label and the merchandiser Admin setup left out, under either label, and neither reply claims a file
- **Fail**: Turn 1 asks a question or renders a clarification instead of drafting, or routes outside Doc Mode, or either doc presents the two-codes rule as current, rounds or rewords a value such as `50%`, `0.01` or `STAFF-`, invents a rule, number or example, or writes `---` dividers or hyphen bullets, or Turn 2 asks a question, drops the two-codes rule or its label, or keeps the merchandiser Admin setup, or a reply claims or promises a local save

### Failure triage

1. Check the Doc routing phrase in `Product Owner - System - Router Contract` line 899, the no-command intake rule in `Product Owner - Templates - Doc Mode` line 43 and the shape routing in `Product Owner - Templates - Doc Mode` lines 234 and 236
2. Check each reply against the delivery order in `Custom Instructions.md` lines 85, 86 and 101 and the Doc summary in `Custom Instructions.md` line 217
3. Re-read both blocks against `context/fernhouse-promotions-rules.md`, restore any value that was rounded or reworded and put the retired label back on the two-codes rule (`Product Owner - Templates - Doc Mode` lines 124 and 130)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-001 | Behavior reference | Verify no-command Doc routing that renders a status-safe behavior reference on discount stacking at once in a Project, then applies a follow-up change | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | 1. Stage and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the reference block and submit Turn 2 -> 4. Inspect the revised reference block -> 5. Compare context/ | Step 2: one reference block with a doc-lane label and no clarification. Step 3: behavior reference with the ClickUp layout and the rules' values. Step 4: revised reference with the values, the two-codes rule labelled retired and no Admin setup, under either label. Step 5: attachments unchanged | Both replies, rendered blocks, labels, layout checks, promotion values and status labels | PASS if Turn 1 renders with no question and both blocks keep their sections, the layout and every value, with the revision keeping the retired label and dropping the Admin setup and no reply claiming a file. FAIL otherwise | 1. Check Doc routing and no-command intake. 2. Check the delivery order. 3. Check values and status labels |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project promised-source rule, Deliverable Block order, the no-file-claim rule and the new and refined export-equivalent labels |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | Project Doc routing phrase |
| [`Product Owner - Templates - Doc Mode - v0.112.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.112.md) | Project no-command intake rule, shape routing, source classification, refinement workflow, export contract and ClickUp output contract |
| [`Product Owner - Assets - Doc Templates - v0.109.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.109.md) | Project behavior reference shape, status language and layout rules |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: Fernhouse company context |
| [`fernhouse-promotions-rules.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md) | Attachment: current promotion rules, worked examples and the retired two-codes rule |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/behavior-reference.md`

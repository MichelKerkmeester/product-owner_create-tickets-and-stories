---
title: "PDK-001 -- Behavior reference"
description: "Validates a no-command Doc request at Fernhouse through the Project's five-field Doc intake question to a ClickUp behavior reference Deliverable Block that keeps the retired two-codes rule retired."
version: 1.0.0.0
---

# PDK-001 -- Behavior reference

This scenario validates natural-language Doc routing, the consolidated Doc intake question and a status-safe behavior reference built from Fernhouse's promotions rules in a Claude Project.

---

## 1. OVERVIEW

The request carries no command token. "Document how" routes it to Doc Mode (`Product Owner - System - Router Contract` line 899). Turn 1 names both attachments but states no reader, purpose, authority, status, shape or scope, so the Project must ask one consolidated question before drafting. `Custom Instructions.md` line 130 and `Product Owner - Templates - Doc Mode` line 174 set that question's minimum: source set, authority, status, shape and scope, each unless the user already stated it. Turn 1 names no reader, so the attachments cannot settle the reader's job and shape stays open. The question may propose Behavior reference for the user to confirm, which `Product Owner - Templates - Doc Mode` line 236 allows. The final reference renders as its own block with an export-equivalent label and no file claim.

The rules note mixes two statuses. Nine current rules sit beside one retired rule: two codes on one order were allowed until `2026-05-01` and are `retired` since. Turn 2 asks for today's behavior and also asks for the old rule to stay in for CS, so a correct doc carries both, each under its own status.

### Why this matters

A behavior reference that folds the retired two-codes rule into today's rules tells a CS agent a customer can still combine codes, and every refund call built on it is wrong. Status labels travel with their claims and are never normalized into current behavior (`Product Owner - Templates - Doc Mode` line 130).

---

## 2. SCENARIO CONTRACT

- Objective: Verify no-command Doc routing, the five-field Doc intake question and a ClickUp behavior reference that keeps Fernhouse's current and retired promotion rules apart
- Real user request: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-promotions-rules.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit unchanged at `context/fernhouse-context.md` and `context/fernhouse-promotions-rules.md` before the Canvas panel baseline (root, Company context and attachments)
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the consolidated question and its clarification block, answer in Turn 2, then inspect the rendered reference and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - doc-discount-stacking-clarification.md` and the `HVR self-scan:` line (root section 5, Clarification turns), claims no file and creates no draft. Turn 2 renders the Behavior reference as its own block under `Export-equivalent path: export/[NNN] - doc-discount-stacking.md`, then replies with the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`Custom Instructions.md` line 217), and claims no file. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: One question that settles the doc before any drafting, then a behavior reference block CS agents and the Checkout engineers can use to predict the discount on any cart
- Size band (advisory): 80 to 180 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, rendered as its own block with a doc-lane clarification label and no draft, and Turn 2 renders a Behavior reference with an Overview and a `## Behavior rules` body, `* * *` directly under every content heading, `*   ` bullets and sentence-case headings, states the current rules with `one discount code per order`, `automatic promotions first`, `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap and `0.01` `half up` rounding verbatim, keeps the two-codes rule in and labelled retired since `2026-05-01`, states nothing the two attachments do not and claims no file. FAIL if Turn 1 drafts, routes to another mode or leaves any of the five fields out of the question, or Turn 2 presents the two-codes rule as current, drops it or its retired label, alters a supplied value, invents a rule, number or example, writes `---` dividers or hyphen bullets, or prints `Path:`, `Saved:` or `Verified:` and claims a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | Route to Doc Mode, read both attachments, ask one consolidated question covering source set, authority, status, shape and scope, plus the purpose and audience the request left open, render it as a doc-lane clarification block with its export-equivalent label and wait. Create no draft | Doc Mode selected, no reader, shape or status assumed, both `context/` files unchanged | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Behavior reference for CS agents and the Checkout engineers, so they can predict the discount on any cart. Those two files are all there is, the rules note governs and the context doc is background only. Write up what promotions-service does today, keep the old two-codes rule in because CS still refunds those orders, and leave out how merchandisers set promotions up in Admin.` | Render the behavior reference from the rules note, state its nine current rules as current behavior with their values verbatim, keep the two-codes rule apart with its own retired label and its refund split, apply the ClickUp layout, then reply with the export-equivalent label, the `HVR self-scan:` line and the five-line Doc summary. Claim no file | The retired label stays on the two-codes rule, and no current rule loses its value or its exception | Turn 2 reply, rendered reference block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question and covers the five Doc fields -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered reference -> operator: check the shape, the ClickUp layout, every promotion value, the retired label and the export-equivalent label against context/fernhouse-promotions-rules.md`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one consolidated question as its own clarification block. Step 3 proves the wait state and that no draft exists. Step 4 finds a Behavior reference with an Overview and `## Behavior rules`, the two sections the shape cannot drop (`Product Owner - Assets - Doc Templates` lines 94 and 379), `* * *` directly under each content heading, `*   ` bullets and sentence-case headings. The current rules keep their exact values, and the two-codes rule sits apart, labelled retired since `2026-05-01` and never offered as something a customer can do today. Spacer headings are not graded here. The skill twin fails them because a file export never carries one, and `Product Owner - Templates - Doc Mode` line 73 allows them in ClickUp-bound content, which the kernel does not say a rendered block is. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the fields the question covers, the doc headings with divider adjacency, the bullet markers, every promotion value, the status label on the two-codes rule, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, rendered as a doc-lane clarification block, with no early draft, and the rendered reference carries an Overview and `## Behavior rules`, passes the ClickUp layout gate, keeps every current rule's value verbatim, keeps the two-codes rule in with its retired label and claims no file
- **Fail**: Turn 1 drafts, routes outside Doc Mode or leaves one of the five fields out, or the doc presents the two-codes rule as current, drops it or its label, rounds or rewords a value such as `50%`, `0.01` or `STAFF-`, invents a rule, number or example, writes `---` dividers or hyphen bullets, or the reply claims a local save

### Failure triage

1. Check the Doc intake minimum in `Custom Instructions.md` line 130 and `Product Owner - Templates - Doc Mode` line 174
2. Compare the block with the Doc Context and Clarification Question in `Product Owner - Assets - Interactive Response Templates` line 106
3. Re-read the rendered reference against `context/fernhouse-promotions-rules.md`, restore any value that was rounded or reworded and put the retired label back on the two-codes rule (`Product Owner - Templates - Doc Mode` lines 124 and 130)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-001 | Behavior reference | Verify no-command Doc routing, the five-field intake question and a status-safe behavior reference on discount stacking in a Project | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | 1. Stage and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the reference block -> 5. Compare context/ | Step 2: one five-field question as its own block. Step 3: no draft. Step 4: behavior reference with the ClickUp layout, the rules' values, the two-codes rule labelled retired and the label. Step 5: attachments unchanged | Both replies, rendered blocks, labels, layout checks, promotion values and status labels | PASS if the question covers all five fields with no draft and the block keeps its sections, the layout, every value and the retired label with no file claim. FAIL otherwise | 1. Check the Doc intake minimum. 2. Check the clarification block. 3. Check values and status labels |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project Doc intake minimum, Deliverable Block and export-equivalent contract |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | Project Doc routing phrase |
| [`Product Owner - Templates - Doc Mode - v0.110.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.110.md) | Project Doc intake minimum, source classification and ClickUp output contract |
| [`Product Owner - Assets - Doc Templates - v0.107.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.107.md) | Project behavior reference shape, status language and layout rules |
| [`Product Owner - Assets - Interactive Response Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.102.md) | Project Doc Context and Clarification Question wording |
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

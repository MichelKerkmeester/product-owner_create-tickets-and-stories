---
title: "SDK-001 -- Behavior reference"
description: "Validates a no-command Doc request at Fernhouse through the five-field Doc intake question to a ClickUp behavior reference on discount stacking that keeps the retired two-codes rule retired."
version: 1.0.0.0
---

# SDK-001 -- Behavior reference

This scenario validates natural-language Doc routing, the consolidated Doc intake question and a status-safe behavior reference built from Fernhouse's promotions rules.

---

## 1. OVERVIEW

The request carries no command token. "Document how" routes it to Doc Mode (`AGENTS.md` line 211, `SKILL.md` line 110). Turn 1 names both attachments but states no reader, purpose, authority, status, shape or scope, so the runtime must ask one consolidated question before drafting. `AGENTS.md` line 285 and `doc-mode.md` line 198 set that question's minimum: source set, authority, status, shape and scope, each unless the user already stated it. Turn 1 names no reader, so the attachments cannot settle the reader's job and shape stays open. The question may propose Behavior reference for the user to confirm, which `doc-mode.md` line 260 allows.

The rules note mixes two statuses. Nine current rules sit beside one retired rule: two codes on one order were allowed until `2026-05-01` and are `retired` since. Turn 2 asks for today's behavior and also asks for the old rule to stay in for CS, so a correct doc carries both, each under its own status.

### Why this matters

A behavior reference that folds the retired two-codes rule into today's rules tells a CS agent a customer can still combine codes, and every refund call built on it is wrong. Status labels travel with their claims and are never normalized into current behavior (`doc-mode.md` line 154).

---

## 2. SCENARIO CONTRACT

- Objective: Verify no-command Doc routing, the five-field Doc intake question and a ClickUp behavior reference that keeps Fernhouse's current and retired promotion rules apart
- Real user request: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-promotions-rules.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit unchanged at `context/fernhouse-context.md` and `context/fernhouse-promotions-rules.md` before the export baseline (root, Company context and attachments)
- Expected execution process: Start fresh, submit Turn 1, capture the consolidated question and its clarification export, answer in Turn 2, then inspect the next doc export and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, exports `export/[###] - doc-discount-stacking-clarification.md`, reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns), and creates no draft. Turn 2 saves `export/[###] - doc-discount-stacking.md` on the next number as a Behavior reference, reads it back and replies with the path, the `Verified:` line, the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`doc-mode.md` line 412). Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: One question that settles the doc before any drafting, then a behavior reference CS agents and the Checkout engineers can use to predict the discount on any cart
- Size band (advisory): 80 to 180 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, exports it in the doc lane and reads it back with no draft, and Turn 2 delivers a Behavior reference with an Overview and a `## Behavior rules` body, `* * *` directly under every content heading, `*   ` bullets, sentence-case headings and no empty spacer heading in the file, states the current rules with `one discount code per order`, `automatic promotions first`, `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap and `0.01` `half up` rounding verbatim, keeps the two-codes rule in and labelled retired since `2026-05-01`, and states nothing the two attachments do not. FAIL if Turn 1 drafts, routes to another mode or leaves any of the five fields out of the question, or Turn 2 presents the two-codes rule as current, drops it or its retired label, alters a supplied value, invents a rule, number or example, or writes `---` dividers or hyphen bullets
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | Route to Doc Mode, read both attachments, ask one consolidated question covering source set, authority, status, shape and scope, plus the purpose and audience the request left open, export it as a doc-lane clarification, read it back and wait. Create no draft | Doc Mode selected, no reader, shape or status assumed, both `context/` files unchanged | Turn 1 reply, clarification export, read-back line and clean draft ledger |
| 2 | `Behavior reference for CS agents and the Checkout engineers, so they can predict the discount on any cart. Those two files are all there is, the rules note governs and the context doc is background only. Write up what promotions-service does today, keep the old two-codes rule in because CS still refunds those orders, and leave out how merchandisers set promotions up in Admin.` | Build the behavior reference from the rules note, state its nine current rules as current behavior with their values verbatim, keep the two-codes rule apart with its own retired label and its refund split, apply the ClickUp layout, save the next doc export, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary | The retired label stays on the two-codes rule, and no current rule loses its value or its exception | Turn 2 reply, exported behavior reference and read-back line |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> filesystem: record the export and context/ baselines`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question and covers the five Doc fields -> user: submit Turn 2 in the same session`
4. `filesystem: open the new doc export -> operator: check the shape, the ClickUp layout, every promotion value and the retired label against context/fernhouse-promotions-rules.md`
5. `filesystem: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one consolidated question and one clarification file in the doc lane. Step 3 proves the wait state and that no draft exists. Step 4 finds a Behavior reference with an Overview and `## Behavior rules`, the two sections the shape cannot drop (`doc-templates.md` lines 115 and 400), `* * *` directly under each content heading, `*   ` bullets, sentence-case headings and no empty spacer heading, since a file export never carries one (`doc-mode.md` line 97). The current rules keep their exact values, and the two-codes rule sits apart, labelled retired since `2026-05-01` and never offered as something a customer can do today. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the fields the question covers, the doc headings with divider adjacency, the bullet markers, every promotion value, the status label on the two-codes rule, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, exported in the doc lane and read back, with no early draft, and the behavior reference carries an Overview and `## Behavior rules`, passes the ClickUp layout gate, keeps every current rule's value verbatim and keeps the two-codes rule in with its retired label
- **Fail**: Turn 1 drafts, routes outside Doc Mode or leaves one of the five fields out, or the doc presents the two-codes rule as current, drops it or its label, rounds or rewords a value such as `50%`, `0.01` or `STAFF-`, invents a rule, number or example, or writes `---` dividers, hyphen bullets or empty spacer headings into the file

### Failure triage

1. Check the Doc routing phrase in `AGENTS.md` line 211 and the minimum question fields in `AGENTS.md` line 285 and `doc-mode.md` line 198
2. Compare the question with the Doc Context and Clarification Question in `interactive-response-templates.md` line 129
3. Re-read the doc against `context/fernhouse-promotions-rules.md`, restore any value that was rounded or reworded and put the retired label back on the two-codes rule (`doc-mode.md` lines 148 and 154)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-001 | Behavior reference | Verify no-command Doc routing, the five-field intake question and a status-safe behavior reference on discount stacking | `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the doc export -> 5. Compare context/ | Step 2: one five-field question in the doc lane. Step 3: no draft. Step 4: behavior reference with the ClickUp layout, the rules' values and the two-codes rule labelled retired. Step 5: attachments unchanged | Both replies, ledger, export paths, read-back lines, layout checks, promotion values and status labels | PASS if the question covers all five fields with no draft and the doc keeps its sections, the layout, every value and the retired label. FAIL otherwise | 1. Check Doc routing and intake. 2. Check the question. 3. Check values and status labels |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Doc routing phrase, the Doc escalation question and the export protocol |
| [`SKILL.md`](../../SKILL.md) | Documentation routing topic, Doc export name and ClickUp contract |
| [`doc-mode.md`](../../references/doc-mode.md) | Doc intake minimum, source classification and ClickUp output contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Behavior reference shape, status language and layout rules |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Doc Context and Clarification Question wording |
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

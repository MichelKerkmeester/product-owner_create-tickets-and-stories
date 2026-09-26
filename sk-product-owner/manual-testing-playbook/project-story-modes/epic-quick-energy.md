---
title: "PEP-003 -- Epic quick energy"
description: "Validates a one-turn $quick $e request for Fernhouse self-serve returns in a Project: the Story gate passes on what the prompt supplies, so one lean house-format Epic Deliverable Block lands with no question."
version: 1.1.0.1
---

# PEP-003 -- Epic quick energy

This scenario validates a Quick Epic at Fernhouse, rendered in one turn from a prompt that carries the Goal, the child stories and the scope decisions.

---

## 1. OVERVIEW

A head of product types `$quick $e` for self-serve returns with the Goal, four child stories and two scope decisions in one line, and points at the Fernhouse context. Quick energy may skip routine intake while the Story gate still runs, and here nothing the gate needs is missing: the kind, the role, the Goal and the child-story set are all stated. The Project renders one lean Epic in the first turn, with no clarification. The Epic keeps the four named child stories, puts guest returns under Added Later, keeps pallet items with CS and carries the prompt's `60%` and `Q1 2027` as given.

### Why this matters

Quick is the energy most likely to cut a corner. It may skip a question the prompt already answers, and it never drops a section the Epic needs or adds scope nobody asked for. Fernhouse also has two facts a lean draft can trip on: a guest has no order history to start a return from, and a pallet item ships with a carrier that has no API, so neither belongs in the first release.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$quick $e` with the Goal and child stories in the prompt passes the Story gate and renders one lean house-format Epic in one turn, with its scope decisions intact
- Real user request: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`
- Prompt: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and the attachment sits at `context/` before the Canvas baseline
- Expected execution process: Start a fresh Project conversation, submit the single turn and inspect the rendered Epic, with no clarification block before it
- Expected signals: Turn 1 extracts Quick energy, routes `$e` to Story Mode in the Epic shape, passes the Story gate on what the prompt supplies, asks no question and renders no clarification block, renders the Epic as its Deliverable Block under `Export-equivalent path: export/[NNN] - Epic-self-serve-returns.md` with the `HVR self-scan:` line and the Epic kind, and claims no file. The Epic names the four child stories as plain text, puts guest returns under `#### Added Later`, keeps pallet items with CS, covers web, iOS and Android and carries `60%` and `Q1 2027` in Goal
- Desired user-visible outcome: One lean Fernhouse Epic block in the first reply, ready for the Post-purchase team to cut child stories from
- Size band (advisory): 60 to 110 lines of Epic body
- Pass/fail: PASS if the one turn asks nothing and renders one Epic in the house shape (a `# Epic - ` H1 with no story preamble, `## About` holding `### Problem`, `### Goal` and `### Solution` plus `#### **References**` only when a link is supplied, never empty and never with an invented link, `## Scope` naming exactly the four child stories the prompt lists as plain text plus `#### Added Later` holding guest returns, release-level `## Acceptance criteria` in numbered `1\.` blocks each closed by its Mark-as-done line, no `## Requirements`, no ticket header fields, story points or INVEST notes), consults only the Epic scaffold where the transcript shows its reads (`Custom Instructions.md` lines 58 and 79), names the kind, carries `60%` and `Q1 2027` verbatim, states any context number it uses exactly as `fernhouse-context.md` does and claims no file. FAIL if it asks a question or renders a clarification, drops a required section, adds a fifth first-release child story or drops one, puts guest returns or pallet items in first-release scope, invents a return fee, a carrier name or a link, alters a supplied value or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.` | Extract Quick energy, route `$e` to Story Mode in the Epic shape and consult only the Story Mode knowledge with the Epic Template. The Story gate runs and passes, because the prompt states the kind, the role, the Goal and the child-story set, so draft the lean Epic, render it as the Deliverable Block, name the kind in the reply and claim no file | Guest returns and pallet items stay outside first-release scope, and the only block is the Epic | Turn 1 reply, rendered Epic block and its label |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`

### Commands

1. `sandbox: confirm the attachment sits at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered Epic -> operator: check the kind, the house sections, the four child stories, the Added Later group, the pallet boundary and every supplied value`

### Expected

Step 1 fixes the panel baseline with only `context/` populated. Step 2 returns one Epic block and no question, Quick energy having skipped only the routine intake.

Step 3 finds an Epic with no story preamble and an H1 such as `# Epic - Customer - Self-serve returns`. `## About` opens with a narrative saying the work splits into child stories. `### Problem` rests on today's returns, which only a CS agent can create in Admin, and any number it quotes, such as `1,900` requests a month, `6 days` to a refund or the `30 days` window, matches `fernhouse-context.md` exactly. `### Goal` carries `60%` and `Q1 2027` for signed-in customers on web, iOS and Android. `### Solution` follows, and `#### **References**` appears only when a link is supplied, never empty and never with an invented link.

`## Scope` names the four child stories as plain text in the shape their Story H1s will take: starting a return from order history with items and a reason, the return label by email, return status on the order page and the refund after the warehouse check. `#### Added Later` holds guest returns. Pallet items stay with CS, and no child story or criterion gives them a return label. A few release-level acceptance criteria close the Epic. Nothing asked for `## Delivery` and Quick never opts it in, so the Epic ends on Acceptance criteria.

### Evidence

Capture the reply, the rendered Epic block, its export-equivalent label, the Epic's Problem, Goal and Scope sections and its acceptance criteria.

### Pass / fail

- **Pass**: No question and one lean house-format Epic that names its kind, lists exactly the four child stories as plain text with guest returns under Added Later, keeps pallet items with CS, carries `60%` and `Q1 2027` verbatim, states every context number it uses exactly as the context does, holds no `## Requirements`, invents no link and claims no file
- **Fail**: The runtime asks a question or renders a clarification, opens the Story scaffold, drops a required section, adds or drops a first-release child story, puts guest returns or pallet items in first-release scope, invents a return fee, a carrier name or a link, alters a supplied value, adds `## Requirements`, ticket header fields, story points or INVEST notes, leaves a template slot unfilled or claims a local save

### Failure triage

1. Check the Quick intake allowance in `Custom Instructions.md` line 108, the Quick row in `Product Owner - System - Interactive Mode` line 103 and the Story intake gate at lines 146 to 150
2. Check the Epic scaffold in `Product Owner - Assets - Epic Template` lines 22 to 93 and the stated child-story set rule in `Product Owner - Templates - Story Mode` line 110
3. Reconcile the child stories, the Added Later group and the pallet boundary against the prompt and `fernhouse-context.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PEP-003 | Epic quick energy | Verify Project `$quick $e` with the Goal and child stories supplied renders one lean Epic in one turn with its scope decisions intact | `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.` | 1. Attachment and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the Epic block | Step 1: baseline known. Step 2: no question, one Epic block. Step 3: lean house Epic with the four child stories, guest returns under Added Later, pallet items left with CS and its label | Reply, rendered block, label, Problem, Goal, Scope and criteria | PASS if no question is asked, the Epic shape, the four child stories, the scope decisions and the supplied values all match and no file is claimed. FAIL otherwise | 1. Check the Quick row and the Story gate. 2. Check the Epic scaffold. 3. Check the scope decisions |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | One scaffold at lines 58 and 79, rendering without a panel at line 85, the Quick intake allowance at line 108, the Epic shape at line 140 and the Epic label at line 227 |
| [`Product Owner - Templates - Story Mode - v0.403.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.403.md) | Every gate under Quick at line 60, Epic kind at line 102, stated child-story set at line 110, Quick keeps needed gates at line 113, Delivery opt-in at line 132, Epic H1 at line 146 and Epic draft order at line 182 |
| [`Product Owner - Assets - Epic Template - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Epic%20Template%20-%20v0.101.md) | Epic scaffold at lines 22 to 93 and its Notes For Use at lines 98 to 102 |
| [`Product Owner - System - Interactive Mode - v0.407.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.407.md) | The Quick energy row at line 103 and the Story intake gate at lines 146 to 150 |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Fernhouse surfaces, today's CS-only returns, guest orders, pallet items and the epic title pattern |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PEP-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/epic-quick-energy.md`

---
title: "SEP-003 -- Epic quick energy"
description: "Validates a one-turn $quick $e request for Fernhouse self-serve returns: the Story gate passes on what the prompt supplies, so one lean house-format Epic lands with no question."
version: 1.0.0.0
---

# SEP-003 -- Epic quick energy

This scenario validates a Quick Epic at Fernhouse, delivered in one turn from a prompt that carries the Goal, the child stories and the scope decisions.

---

## 1. OVERVIEW

A head of product types `$quick $e` for self-serve returns with the Goal, four child stories and two scope decisions in one line, and points at the Fernhouse context. Quick energy may skip routine intake while the Story gate still runs, and here nothing the gate needs is missing: the kind, the role, the Goal and the child-story set are all stated. The runtime saves one lean Epic in the first turn, with no clarification. The Epic keeps the four named child stories, puts guest returns under Added Later, keeps pallet items with CS and carries the prompt's `60%` and `Q1 2027` as given.

### Why this matters

Quick is the energy most likely to cut a corner. It may skip a question the prompt already answers, and it never drops a section the Epic needs or adds scope nobody asked for. Fernhouse also has two facts a lean draft can trip on: a guest has no order history to start a return from, and a pallet item ships with a carrier that has no API, so neither belongs in the first release.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$quick $e` with the Goal and child stories in the prompt passes the Story gate and saves one lean house-format Epic in one turn, with its scope decisions intact
- Real user request: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`
- Prompt: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and the attachment sits at `context/` before the export baseline
- Expected execution process: Start fresh, submit the single turn and inspect the Epic export, with no clarification before it
- Expected signals: Turn 1 extracts Quick energy, routes `$e` to Story Mode in the Epic shape, passes the Story gate on what the prompt supplies, asks no question and writes no clarification, saves `export/[###] - Epic-self-serve-returns.md` as the only new file, reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count, the `HVR self-scan:` line and the Epic kind. The Epic names the four child stories as plain text, puts guest returns under `#### Added Later`, keeps pallet items with CS, covers web, iOS and Android and carries `60%` and `Q1 2027` in Goal
- Desired user-visible outcome: One lean Fernhouse Epic in the first reply, ready for the Post-purchase team to cut child stories from
- Size band (advisory): 60 to 110 lines of Epic body
- Pass/fail: PASS if the one turn asks nothing and saves one Epic in the house shape (a `# Epic - ` H1 with no story preamble, `## About` holding `### Problem`, `### Goal`, `### Solution` and `#### **References**`, `## Scope` naming exactly the four child stories the prompt lists as plain text plus `#### Added Later` holding guest returns, release-level `## Acceptance criteria` in numbered `1\.` blocks each closed by its Mark-as-done line, no `## Requirements`, no ticket header fields, story points or INVEST notes), names the kind, carries `60%` and `Q1 2027` verbatim and states any context number it uses exactly as `fernhouse-context.md` does. FAIL if it asks a question or writes a clarification, drops a required section, adds a fifth first-release child story or drops one, puts guest returns or pallet items in first-release scope, invents a return fee, a carrier name or a link, or alters a supplied value
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.` | Extract Quick energy, route `$e` to Story Mode in the Epic shape and load only `story-mode.md` with `epic-template.md`. The Story gate runs and passes, because the prompt states the kind, the role, the Goal and the child-story set, so draft the lean Epic, save it, read it back and name the kind in the reply | Guest returns and pallet items stay outside first-release scope, and the only new file is the Epic | Turn 1 reply, Epic export, read-back result and the ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`

### Commands

1. `sandbox: confirm the attachment sits at context/ -> sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the new Epic export -> operator: check the kind, the house sections, the four child stories, the Added Later group, the pallet boundary and every supplied value`

### Expected

Step 1 fixes the baseline with only `context/` populated. Step 2 returns one Epic and no question, Quick energy having skipped only the routine intake, and the ledger shows one new file.

Step 3 finds an Epic with no story preamble and an H1 such as `# Epic - Customer - Self-serve returns`. `## About` opens with a narrative saying the work splits into child stories. `### Problem` rests on today's returns, which only a CS agent can create in Admin, and any number it quotes, such as `1,900` requests a month, `6 days` to a refund or the `30 days` window, matches `fernhouse-context.md` exactly. `### Goal` carries `60%` and `Q1 2027` for signed-in customers on web, iOS and Android. `### Solution` and `#### **References**` follow, with no invented link.

`## Scope` names the four child stories as plain text in the shape their Story H1s will take: starting a return from order history with items and a reason, the return label by email, return status on the order page and the refund after the warehouse check. `#### Added Later` holds guest returns. Pallet items stay with CS, and no child story or criterion gives them a return label. A few release-level acceptance criteria close the Epic. Nothing asked for `## Delivery` and Quick never opts it in, so the Epic ends on Acceptance criteria.

### Evidence

Capture the reply, the side-effect ledger, the export path and read-back result, the Epic's Problem, Goal and Scope sections and its acceptance criteria.

### Pass / fail

- **Pass**: No question and one lean house-format Epic that names its kind, lists exactly the four child stories as plain text with guest returns under Added Later, keeps pallet items with CS, carries `60%` and `Q1 2027` verbatim, states every context number it uses exactly as the context does, holds no `## Requirements` and invents no link
- **Fail**: The runtime asks a question or writes a clarification, loads the Story scaffold, drops a required section, adds or drops a first-release child story, puts guest returns or pallet items in first-release scope, invents a return fee, a carrier name or a link, alters a supplied value, adds `## Requirements`, ticket header fields, story points or INVEST notes or leaves a template slot unfilled

### Failure triage

1. Check the Quick energy row in `interactive-mode.md` line 126 and the Story intake gate at lines 169 to 173
2. Check the Epic scaffold in `epic-template.md` lines 41 to 112 and the stated child-story set rule in `story-mode.md` line 134
3. Reconcile the child stories, the Added Later group and the pallet boundary against the prompt and `fernhouse-context.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SEP-003 | Epic quick energy | Verify `$quick $e` with the Goal and child stories supplied saves one lean Epic in one turn with its scope decisions intact | `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.` | 1. Attachment and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the Epic export | Step 1: baseline known. Step 2: no question, one Epic file. Step 3: lean house Epic with the four child stories, guest returns under Added Later and pallet items left with CS | Reply, ledger, export path, Problem, Goal, Scope and criteria | PASS if no question is asked and the Epic shape, the four child stories, the scope decisions and the supplied values all match. FAIL otherwise | 1. Check the Quick row and the Story gate. 2. Check the Epic scaffold. 3. Check the scope decisions |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Quick energy may skip ordinary preference questions at line 289 |
| [`SKILL.md`](../../SKILL.md) | Epic export at line 207, the `$quick` allowance in Story-work clarification at line 252 and the Epic gate at lines 388 and 389 |
| [`story-mode.md`](../../references/story-mode.md) | Every gate under Quick at line 83, Epic kind at line 126, stated child-story set at line 134, Quick keeps needed gates at line 137, Delivery opt-in at line 156, Epic H1 at line 170 and Epic draft order at line 206 |
| [`epic-template.md`](../../assets/epic-template.md) | Epic scaffold at lines 41 to 112 and its Notes For Use at lines 117 to 121 |
| [`interactive-mode.md`](../../references/interactive-mode.md) | The Quick energy row at line 126 and the Story intake gate at lines 169 to 173 |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Fernhouse surfaces, today's CS-only returns, guest orders, pallet items and the epic title pattern |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SEP-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/epic-quick-energy.md`

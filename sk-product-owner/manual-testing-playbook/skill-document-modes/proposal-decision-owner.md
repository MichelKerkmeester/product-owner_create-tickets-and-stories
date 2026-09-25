---
title: "SDK-003 -- Proposal with a decision owner"
description: "Validates a $d request at Loomlist through the five-field Doc intake question to a ClickUp proposal on sync conflicts that stays proposed, names the decision owner and date and decides nothing."
version: 1.0.0.0
---

# SDK-003 -- Proposal with a decision owner

This scenario validates the short Doc command, the consolidated Doc intake question and a proposal that keeps an open engineering decision open.

---

## 1. OVERVIEW

`$d` is the short Doc command and does not supply the Doc context, so the runtime still asks its question and waits (`AGENTS.md` line 287). Turn 1 names both attachments but states no reader, authority, status, shape or scope. "Where we are" could fit a Narrative overview or a Proposal, so shape is genuinely open. `AGENTS.md` line 285 and `doc-mode.md` line 198 set the question's minimum: source set, authority, status, shape and scope, each unless the user already stated it. Turn 2 picks a Proposal.

The thread ends `not decided`. `Option B` has the most support and is never agreed, and `Joana`, `Engineering Manager, Sync`, decides on `2026-10-09`. Turn 2 says nothing is settled but names neither the owner nor the date, so both have to come from the thread. It also asks where people landed, which invites writing B up as the choice.

`Conflicting edit from {device name}` is the thread's own proposed copy for Option B, braces included. Keeping it verbatim is fidelity, not an unfilled template slot under root section 5, Ticket realism.

### Why this matters

A proposal that reads B as agreed lets engineers start building before the decision owner has seen the spike, and it tells Support something the Sync team never said. A proposal must not read like shipped or decided documentation (`doc-mode.md` line 355), and it keeps the decision owner and approval gap visible (`AGENTS.md` line 291).

---

## 2. SCENARIO CONTRACT

- Objective: Verify the Doc intake question under `$d` and a ClickUp proposal that lays out the three sync conflict options, attributes support and leaves the decision with its owner
- Real user request: `Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Prompt: `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-sync-conflict-thread.md](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit unchanged at `context/loomlist-context.md` and `context/loomlist-sync-conflict-thread.md` before the export baseline (root, Company context and attachments)
- Expected execution process: Start fresh, submit Turn 1, capture the consolidated question and its clarification export, answer in Turn 2, then inspect the next doc export and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, exports `export/[###] - doc-sync-conflicts-clarification.md`, reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns), and creates no draft. Turn 2 saves `export/[###] - doc-sync-conflicts.md` on the next number as a Proposal, reads it back and replies with the path, the `Verified:` line, the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`doc-mode.md` line 412). Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: One question that settles the doc before any drafting, then a proposal the Sync and Mobile engineers and the Support lead can read before the decision without mistaking any option for the chosen one
- Size band (advisory): 70 to 160 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, exports it in the doc lane and reads it back with no draft, and Turn 2 delivers a Proposal with the Proposal status notice directly below the title, an Overview and a proposed-design or options body, `* * *` directly under every content heading, `*   ` bullets, sentence-case headings and no empty spacer heading in the file, gives today's v3 `block-level last-writer-wins` as the current state, lays out `Option A` as `field-level` last-writer-wins, `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim and `Option C` as a `CRDT`, attributes support for B to the people who gave it, names `Joana` as decision owner and `2026-10-09` as decision date with the status `not decided`, calls no option chosen, agreed, approved or decided, and states nothing the two attachments do not. FAIL if Turn 1 drafts or leaves any of the five fields out of the question, or Turn 2 presents any option as decided or approved, drops the decision owner or date, drops the proposal status notice, changes a figure or estimate, fills `{device name}` with an invented device, invents evidence, or writes `---` dividers or hyphen bullets
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | Route to Doc Mode, read both attachments, ask one consolidated question covering source set, authority, status, shape and scope, plus the purpose and audience the request left open, export it as a doc-lane clarification, read it back and wait. Create no draft | Doc Mode selected, no reader, shape or status assumed, both `context/` files unchanged | Turn 1 reply, clarification export, read-back line and clean draft ledger |
| 2 | `A proposal for the Sync and Mobile engineers and the Support lead to read before the call is made. Those two files are all there is, the thread governs and the context doc is background on how v3 works today. Nothing is settled, so cover all three options with their cost and trade-offs and say where people in the thread landed. Keep the offline mode plans out of it.` | Build the proposal from the thread under a Proposal status notice, separate today's v3 behavior from the three candidate options, keep each option's mechanism, cost and trade-offs as the thread states them, attribute each position to its speaker, record the decision as not decided with its owner and date, apply the ClickUp layout, save the next doc export, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary | No option reads as chosen, and the decision owner and date come from the thread | Turn 2 reply, exported proposal and read-back line |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> filesystem: record the export and context/ baselines`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question and covers the five Doc fields -> user: submit Turn 2 in the same session`
4. `filesystem: open the new doc export -> operator: check the status notice, the shape, the ClickUp layout, the three options, the attributions and the decision block against context/loomlist-sync-conflict-thread.md`
5. `filesystem: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one consolidated question and one clarification file in the doc lane. Step 3 proves the wait state and that no draft exists. Step 4 finds a Proposal whose status notice sits directly below the title (`doc-templates.md` lines 486 and 575), then an Overview and a proposed-design or options body (lines 115 and 508), with `* * *` directly under each content heading, `*   ` bullets, sentence-case headings and no empty spacer heading, since a file export never carries one (`doc-mode.md` line 97). Today's v3 `block-level last-writer-wins` sits apart from the candidates. `Option A`, `Option B` and `Option C` keep the thread's mechanisms, and any figure the doc cites keeps its value: `0.8%` of sessions, `40` `lost-edit` tickets, the 58% and 42% split, about 3 weeks, 6 to 8 weeks and two quarters. Support for B is reported as what named people said, with Saskia's formatting fallback beside it. The decision reads `not decided`, owned by `Joana`, `Engineering Manager, Sync`, on `2026-10-09`, with Tomasz's two-week spike on B as the step before it, and it stays visible rather than being completed by assumption (`doc-templates.md` line 582). Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the fields the question covers, the status notice, the doc headings with divider adjacency, the bullet markers, each option with its figures, the attributions, the decision owner and date, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, exported in the doc lane and read back, with no early draft, and the proposal carries its status notice under the title, an Overview and an options body, passes the ClickUp layout gate, keeps the three options and every cited figure exact, names `Joana` and `2026-10-09` and leaves the decision open
- **Fail**: Turn 1 drafts or leaves one of the five fields out, or the proposal calls Option B, or any option, chosen, agreed, approved or decided, drops the status notice, the decision owner or the date, changes a figure or estimate, replaces `{device name}` with an invented device name, invents evidence or a position nobody in the thread took, or writes `---` dividers, hyphen bullets or empty spacer headings into the file

### Failure triage

1. Check the explicit-command rule in `AGENTS.md` line 287 and the minimum question fields in `AGENTS.md` line 285 and `doc-mode.md` line 198
2. Compare the question with the Doc Context and Clarification Question in `interactive-response-templates.md` line 129
3. Re-read the proposal against `context/loomlist-sync-conflict-thread.md`, restore the status notice and any figure that changed, and put the decision back to not decided with its owner and date (`doc-mode.md` line 355, `doc-templates.md` line 545)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-003 | Proposal with a decision owner | Verify the Doc intake question under the short command and a sync conflict proposal that decides nothing and names its owner | `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the doc export -> 5. Compare context/ | Step 2: one five-field question in the doc lane. Step 3: no draft. Step 4: proposal with its status notice, the ClickUp layout, three exact options, attributed support and an open decision with owner and date. Step 5: attachments unchanged | Both replies, ledger, export paths, read-back lines, layout checks, options, attributions and the decision block | PASS if the question covers all five fields with no draft and the proposal keeps its notice, sections, layout, options and figures and leaves the decision with its owner. FAIL otherwise | 1. Check the Doc intake. 2. Check the question. 3. Check status, options and the decision block |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Explicit-command intake rule, the Doc escalation question and the proposal boundary |
| [`doc-mode.md`](../../references/doc-mode.md) | Doc intake minimum, the Proposal shape and ClickUp output contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Proposal scaffold, status notice, decision block and layout rules |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Doc Context and Clarification Question wording |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: Loomlist company context |
| [`loomlist-sync-conflict-thread.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md) | Attachment: the three options, who supported what and the open decision with its owner and date |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/proposal-decision-owner.md`

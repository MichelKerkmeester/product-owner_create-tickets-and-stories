---
title: "PDK-003 -- Proposal with a decision owner"
description: "Validates a $d request at Loomlist through the Project's five-field Doc intake question to a ClickUp proposal Deliverable Block on sync conflicts that stays proposed, names the decision owner and date and decides nothing."
version: 1.1.0.0
---

# PDK-003 -- Proposal with a decision owner

This scenario validates the short Doc command, the consolidated Doc intake question and a proposal that keeps an open engineering decision open in a Claude Project.

---

## 1. OVERVIEW

`$d` is the short Doc command and does not supply the Doc context, so the Project still asks its question and waits (`Custom Instructions.md` line 108). Turn 1 names both attachments but states no reader, authority, status, shape or scope. "Where we are" could fit a Narrative overview or a Proposal, so shape is genuinely open. `Custom Instructions.md` line 130 and `Product Owner - Templates - Doc Mode` line 174 set the question's minimum: source set, authority, status, shape and scope, each unless the user already stated it. Turn 2 picks a Proposal. The final proposal renders as its own block with an export-equivalent label and no file claim.

The thread ends `not decided`. `Option B` has the most support and is never agreed, and `Joana`, `Engineering Manager, Sync`, decides on `2026-10-09`. Turn 2 says nothing is settled but names neither the owner nor the date, so both have to come from the thread. It also asks where people landed, which invites writing B up as the choice.

`Conflicting edit from {device name}` is the thread's own proposed copy for Option B, braces included. Keeping it verbatim is fidelity, not an unfilled template slot under root section 5, Ticket realism.

### Why this matters

A proposal that reads B as agreed lets engineers start building before the decision owner has seen the spike, and it tells Support something the Sync team never said. A proposal must not read like shipped or decided documentation (`Product Owner - Templates - Doc Mode` line 331), and it keeps decision ownership and approval status explicit (line 95).

---

## 2. SCENARIO CONTRACT

- Objective: Verify the Doc intake question under `$d` and a ClickUp proposal that lays out the three sync conflict options, attributes support and leaves the decision with its owner
- Real user request: `Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Prompt: `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-sync-conflict-thread.md](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit unchanged at `context/loomlist-context.md` and `context/loomlist-sync-conflict-thread.md` before the Canvas panel baseline (root, Company context and attachments)
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the consolidated question and its clarification block, answer in Turn 2, then inspect the rendered proposal and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - doc-sync-conflicts-clarification.md` and the `HVR self-scan:` line (root section 5, Clarification turns), claims no file and creates no draft. Turn 2 renders the Proposal as its own block under `Export-equivalent path: export/[NNN] - doc-sync-conflicts.md`, then replies with the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`Custom Instructions.md` line 217), and claims no file. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: One question that settles the doc before any drafting, then a proposal block the Sync and Mobile engineers and the Support lead can read before the decision without mistaking any option for the chosen one
- Size band (advisory): 70 to 160 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, rendered as its own block with a doc-lane clarification label and no draft, and Turn 2 renders a Proposal with the Proposal status notice directly below the title, an Overview and a proposed-design or options body, `* * *` directly under every content heading, `*   ` bullets and sentence-case headings, gives today's v3 block-level last-writer-wins as the current state, in the thread's words or as the same rule restated, lays out `Option A` as `field-level` last-writer-wins, `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim and `Option C` as a `CRDT`, attributes support for B to the people who gave it, names `Joana` as decision owner and `2026-10-09` as decision date with the status `not decided`, calls no option chosen, agreed, approved or decided, states nothing the two attachments do not and claims no file. FAIL if Turn 1 drafts or leaves any of the five fields out of the question, or Turn 2 presents any option as decided or approved, drops the decision owner or date, drops the proposal status notice, changes a figure or estimate, fills `{device name}` with an invented device, invents evidence, writes `---` dividers or hyphen bullets, or prints `Path:`, `Saved:` or `Verified:` and claims a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | Route to Doc Mode, read both attachments, ask one consolidated question covering source set, authority, status, shape and scope, plus the purpose and audience the request left open, render it as a doc-lane clarification block with its export-equivalent label and wait. Create no draft | Doc Mode selected, no reader, shape or status assumed, both `context/` files unchanged | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `A proposal for the Sync and Mobile engineers and the Support lead to read before the call is made. Those two files are all there is, the thread governs and the context doc is background on how v3 works today. Nothing is settled, so cover all three options with their cost and trade-offs and say where people in the thread landed. Keep the offline mode plans out of it.` | Render the proposal from the thread under a Proposal status notice, separate today's v3 behavior from the three candidate options, keep each option's mechanism, cost and trade-offs as the thread states them, attribute each position to its speaker, record the decision as not decided with its owner and date, apply the ClickUp layout, then reply with the export-equivalent label, the `HVR self-scan:` line and the five-line Doc summary. Claim no file | No option reads as chosen, and the decision owner and date come from the thread | Turn 2 reply, rendered proposal block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question and covers the five Doc fields -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered proposal -> operator: check the status notice, the shape, the ClickUp layout, the three options, the attributions, the decision block and the export-equivalent label against context/loomlist-sync-conflict-thread.md`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one consolidated question as its own clarification block. Step 3 proves the wait state and that no draft exists. Step 4 finds a Proposal whose status notice sits directly below the title (`Product Owner - Assets - Doc Templates` lines 465 and 554), then an Overview and a proposed-design or options body (lines 94 and 487), with `* * *` directly under each content heading, `*   ` bullets and sentence-case headings. Today's v3 block-level last-writer-wins sits apart from the candidates. `Option A`, `Option B` and `Option C` keep the thread's mechanisms, and any figure the doc cites keeps its value: `0.8%` of sessions, `40` `lost-edit` tickets, the 58% and 42% split, about 3 weeks, 6 to 8 weeks and two quarters. Support for B is reported as what named people said, with Saskia's formatting fallback beside it. The decision reads `not decided`, owned by `Joana`, `Engineering Manager, Sync`, on `2026-10-09`, with Tomasz's two-week spike on B as the step before it, and it stays visible rather than being completed by assumption (`Product Owner - Assets - Doc Templates` line 561). Spacer headings are not graded here. The skill twin fails them because a file export never carries one, and `Product Owner - Templates - Doc Mode` line 73 allows them in ClickUp-bound content, which the kernel does not say a rendered block is. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the fields the question covers, the status notice, the doc headings with divider adjacency, the bullet markers, each option with its figures, the attributions, the decision owner and date, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, rendered as a doc-lane clarification block, with no early draft, and the rendered proposal carries its status notice under the title, an Overview and an options body, passes the ClickUp layout gate, keeps the three options and every cited figure exact, names `Joana` and `2026-10-09`, leaves the decision open and claims no file
- **Fail**: Turn 1 drafts or leaves one of the five fields out, or the proposal calls Option B, or any option, chosen, agreed, approved or decided, drops the status notice, the decision owner or the date, changes a figure or estimate, replaces `{device name}` with an invented device name, invents evidence or a position nobody in the thread took, writes `---` dividers or hyphen bullets, or the reply claims a local save

### Failure triage

1. Check the explicit-command rule in `Custom Instructions.md` line 108 and the Doc intake minimum in `Custom Instructions.md` line 130 and `Product Owner - Templates - Doc Mode` line 174
2. Compare the block with the Doc Context and Clarification Question in `Product Owner - Assets - Interactive Response Templates` line 106
3. Re-read the rendered proposal against `context/loomlist-sync-conflict-thread.md`, restore the status notice and any figure that changed, and put the decision back to not decided with its owner and date (`Product Owner - Templates - Doc Mode` line 331, `Product Owner - Assets - Doc Templates` line 524)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-003 | Proposal with a decision owner | Verify the Doc intake question under the short command and a sync conflict proposal that decides nothing and names its owner in a Project | `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | 1. Stage and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the proposal block -> 5. Compare context/ | Step 2: one five-field question as its own block. Step 3: no draft. Step 4: proposal with its status notice, the ClickUp layout, three exact options, attributed support, an open decision with owner and date and the label. Step 5: attachments unchanged | Both replies, rendered blocks, labels, layout checks, options, attributions and the decision block | PASS if the question covers all five fields with no draft and the block keeps its notice, sections, layout, options and figures and leaves the decision with its owner, with no file claim. FAIL otherwise | 1. Check the Doc intake. 2. Check the clarification block. 3. Check status, options and the decision block |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project explicit-command rule, Doc intake minimum, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Doc Mode - v0.111.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.111.md) | Project Doc intake minimum, the Proposal shape and ClickUp output contract |
| [`Product Owner - Assets - Doc Templates - v0.108.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.108.md) | Project Proposal scaffold, status notice, decision block and layout rules |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Project Doc Context and Clarification Question wording |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: Loomlist company context |
| [`loomlist-sync-conflict-thread.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md) | Attachment: the three options, who supported what and the open decision with its owner and date |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/proposal-decision-owner.md`

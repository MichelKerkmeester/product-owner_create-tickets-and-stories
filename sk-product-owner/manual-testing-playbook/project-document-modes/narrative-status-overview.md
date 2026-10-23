---
title: "PDK-005 -- Narrative status overview"
description: "Validates a no-command Doc request at Loomlist that renders a ClickUp Narrative overview Deliverable Block on the lost edits at once for a newcomer, keeps every sync option proposed and the decision with its owner, then applies a follow-up change."
version: 1.0.0.0
---

# PDK-005 -- Narrative status overview

This scenario validates natural-language Doc routing, a prose-first Narrative overview that orients a newcomer on Loomlist's lost edits and a follow-up change that must leave the open decision open, in a Claude Project.

---

## 1. OVERVIEW

The request carries no command token. "Can you document" routes it to Doc Mode (`Custom Instructions.md` Section 10, Router Code, line 561). With no command, the Project asks one consolidated question only when purpose, audience, source authority, scope or source classification cannot be established safely (`Product Owner - Templates - Doc Mode` line 43), and the request and its attachments establish them. The request names the reader, Priya on her first day on the Sync team, the purpose, where things stand, and the scope, the lost edits between devices. The thread is the one governing source and the context doc is background. The thread is present, so the promised-source rule in `Custom Instructions.md` line 148 does not hold shape open, and the request asks for a status overview a newcomer reads for orientation, which picks Narrative overview without a preference question (`Product Owner - Templates - Doc Mode` lines 231, 236 and 335). Turn 1 therefore renders the doc at once as its own block, labelled in the doc lane, with no file claim.

`PDK-003` drafts a Proposal from the same thread for the people deciding. This scenario drafts the story for someone who has to understand it, so the doc is prose-first with a self-sufficient opening (`Product Owner - Assets - Doc Templates` lines 580 to 633). The thread mixes statuses. Protocol v3's block-level last-writer-wins is current behavior, Options A, B and C are proposals, and the pinned status is `not decided` with `Joana` deciding on `2026-10-09`. Option B has the most support in the thread, which invites a story that ends with B chosen.

Turn 2 is a follow-up change to the delivered doc, and "can you update the document" keeps it in Doc Mode on its own. It asks the doc to answer why the team has not simply gone with B and to say what Support tells members until the decision. Both answers sit in the thread, in Joana's closing message, so the follow-up carries no command and leaves nothing unresolved, and the Project revises without a question (`Product Owner - Templates - Doc Mode` lines 43 and 172). The revision is a delivery: the Deliverable Block comes first, then the export-equivalent path, the `HVR self-scan:` line and the quality status (`Custom Instructions.md` lines 91 and 92), with no claim or promise of a file (`Custom Instructions.md` line 107). Which label the revision carries is not graded, for the reason `PDK-001` section 1 gives, and the grade reads the revised doc on its own terms.

### Why this matters

A newcomer reads a status overview as the team's settled view. One that tells the story as "the team backed B" sends Priya into her first week building or defending a design nobody has chosen, before the spike has measured its storage cost or how often the merge falls back to a copy. Labels such as `proposal` must not be normalized into current behavior (`Product Owner - Templates - Doc Mode` line 130), and the Narrative overview keeps status discipline exactly as every other shape does (`Product Owner - Templates - Doc Mode` line 335).

---

## 2. SCENARIO CONTRACT

- Objective: Verify no-command Doc routing that renders a ClickUp Narrative overview at once from the attachments, orients a newcomer in prose, keeps every option proposed and the decision with its owner, and applies a follow-up change to the delivered doc
- Real user request: `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Prompt: `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-sync-conflict-thread.md](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit unchanged at `context/loomlist-context.md` and `context/loomlist-sync-conflict-thread.md` before the Canvas panel baseline (root, Company context and attachments)
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the rendered overview and its reply, submit the Turn 2 change in the same conversation, then inspect the revised overview and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks no question and renders no clarification block, renders the Narrative overview as its own block under `Export-equivalent path: export/[NNN] - doc-lost-edits-status.md` or a similar doc-lane name, then replies with the `HVR self-scan:` line and the quality line naming Source safety, Shape fit, ClickUp layout, Readability and Voice (`Product Owner - Templates - Doc Mode` line 388) and claims no file. Turn 2 asks no question, applies the change, renders the revised overview as its own block under an `Export-equivalent path:` in the doc lane, the Turn 1 label or a new one, then replies with the `HVR self-scan:` line and the quality line with its five Doc checks and claims no file. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: A status overview block Priya can read in one sitting to know what is going wrong, why, what the team is weighing and who decides when, then a revision that answers the question she is most likely to ask
- Size band (advisory): 40 to 110 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Doc Mode and, with no question and no clarification block, renders a Narrative overview with a doc-lane export-equivalent label whose title is followed by a `>` status notice that marks the options as proposals and the decision as open, whose opening paragraphs before the first section heading state the lost edits, why they matter and that nothing is decided, whose content sections open in prose paragraphs rather than bullet lists, with `* * *` directly under every content heading, `*   ` bullets where it uses any and sentence-case headings, that gives today's v3 block-level last-writer-wins as current behavior, keeps `lost-edit`, `40`, `22`, `0.8%`, `58%`, `42%`, `Option A`, `Option B`, `Option C`, their estimates `3 weeks`, `6 to 8 weeks` and `two quarters`, `Conflicting edit from {device name}`, `not decided`, `Joana` and `2026-10-09` verbatim, attributes support for B to the people who gave it and calls no option chosen, agreed, approved or decided, and Turn 2, with no question, renders the revised overview with a doc-lane label, the same shape and layout checks, every one of those values still verbatim, an answer to why B is not simply chosen drawn from Joana's message, the unknown mobile storage cost and how often the merge falls back to a copy, and what Support tells members until the decision, with nothing the two attachments do not state and no file claim on either turn. Whether Turn 2 repeats the Turn 1 label or reports a new one is not graded. FAIL if Turn 1 asks a question or renders a clarification instead of drafting, routes to another mode or picks another shape, or either doc presents any option as chosen or approved, drops the decision owner, date or status, drops the status notice, opens on a bullet list instead of prose, changes a figure or estimate, fills `{device name}` with an invented device, invents a person, date or fact, or writes `---` dividers or hyphen bullets, or Turn 2 asks a question or answers the B question with anything the thread does not say, or either reply prints `Path:`, `Saved:` or `Verified:` or claims or promises a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | Route to Doc Mode on the "can you document" framing, read both attachments, take purpose, audience, authority, status and scope from the request and the thread and pick Narrative overview. Draft it from the thread in prose, opening on the situation, the stakes and the open decision, with v3's behavior as current, Options A, B and C as proposals with their estimates verbatim and the pinned status, owner and date intact. Apply the ClickUp layout, render it as its own block, then reply with the doc-lane export-equivalent label, the `HVR self-scan:` line and the five-line Doc summary. Ask no question, render no clarification and claim no file | Doc Mode selected, one overview block and no clarification block, both `context/` files unchanged | Turn 1 reply, rendered overview block and its label |
| 2 | `Thanks. Can you update the document so it answers why we don't just go with B when most of the thread backs it, since Priya will ask? Also say what Support tells members until the decision, and keep it to what the thread says.` | Treat the message as a change to the delivered doc and ask nothing. Answer the B question from Joana's message, the unknown storage cost on mobile and how often the merge falls back to a copy, with the two-week spike that measures both and the decision still Joana's on `2026-10-09`. Add Support's line to members from the same message. Keep the shape, the prose opening, the status notice, every value and the ClickUp layout. Render the revised overview as its own block, then reply with a doc-lane export-equivalent label, the Turn 1 label or a new one, the `HVR self-scan:` line and the five-line Doc summary. Claim no file | No option becomes chosen, the status stays `not decided` and no figure changes. Which label the revision carries is recorded but not graded | Turn 2 reply, rendered revised overview block and its label |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered overview -> operator: confirm no clarification block exists and check the shape, the opening, the status notice, the ClickUp layout, every figure, estimate and decision field and the export-equivalent label against context/loomlist-sync-conflict-thread.md -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the revised overview -> operator: check the same items, the answer on B, Support's line and the export-equivalent label against context/loomlist-sync-conflict-thread.md, and record which label the revision carries`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one overview block with a doc-lane label and no clarification block. Step 3 finds a Narrative overview: the title, a `>` status notice between `* * *` lines because the material is not wholly current behavior (`Product Owner - Assets - Doc Templates` line 590), then two to four paragraphs a reader with no context understands alone (`Product Owner - Assets - Doc Templates` line 631), then sections whose names fit the story and that open in prose, each with `* * *` directly under its heading. Bullets appear only for enumerable content such as the three options, and open items may carry checklists. Every figure, estimate and decision field matches the thread. Step 4 finds the same checks passing under the Turn 1 label or a new one in the doc lane, plus an answer on B taken from Joana's message and Support's line to members. Spacer headings are not graded here, for the reason `PDK-001` section 3 gives. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, both rendered blocks, both export-equivalent labels, the status notice, the opening paragraphs, the doc headings with divider adjacency, the bullet markers, every figure, estimate and decision field in each block, the B answer, Support's line, both Doc quality summaries and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 renders at once with no question a Narrative overview with a doc-lane label, a status notice, a self-sufficient prose opening and prose-led sections, the ClickUp layout and every value verbatim, with every option proposed and the decision with `Joana` on `2026-10-09`, and Turn 2 renders the revised overview with no question, the same checks passing and the B answer and Support's line drawn from the thread, under either label, and neither reply claims a file
- **Fail**: Turn 1 asks a question or renders a clarification instead of drafting, or routes outside Doc Mode or picks another shape, or either doc presents an option as chosen, drops the status notice or a decision field, opens on bullets, alters a figure or estimate, invents a fact or fills `{device name}`, or writes `---` dividers or hyphen bullets, or Turn 2 asks a question or answers the B question beyond the thread, or a reply claims or promises a local save

### Failure triage

1. Check the Doc framing in `Custom Instructions.md` Section 10, Router Code, line 561, the no-command intake rule in `Product Owner - Templates - Doc Mode` line 43 and the shape routing in `Product Owner - Templates - Doc Mode` lines 231, 236 and 335
2. Check each reply against the delivery order in `Custom Instructions.md` lines 91, 92 and 107 and the Doc summary in `Product Owner - Templates - Doc Mode` line 388
3. Re-read both blocks against `context/loomlist-sync-conflict-thread.md`, restore any figure or estimate that was rounded or reworded, put the status notice and the decision fields back and reframe any option written as chosen (`Product Owner - Templates - Doc Mode` lines 123 and 130)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-005 | Narrative status overview | Verify no-command Doc routing that renders a prose-first status overview on the lost edits at once for a newcomer, then applies a follow-up change, with the decision kept open | `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the overview and submit Turn 2 -> 4. Inspect the revised overview -> 5. Compare context/ | Step 2: one overview block with a doc-lane label and no clarification. Step 3: Narrative overview with the status notice, a prose opening, the ClickUp layout and the thread's values. Step 4: revised overview with the B answer and Support's line from the thread and no option chosen, under either label. Step 5: attachments unchanged | Both replies, both blocks, labels, notice, opening, layout checks, values and decision fields | PASS if Turn 1 renders with no question and both blocks keep the shape, the layout, every value and the open decision, with the revision answering from the thread and no file claim. FAIL otherwise | 1. Check Doc framing and no-command intake. 2. Check the delivery order. 3. Check values, notice and decision fields |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project promised-source rule, Deliverable Block order, the no-file-claim rule and the export-equivalent labels |
| [`Custom Instructions.md` Section 10](../../../claude%20project/Custom%20Instructions.md) | Project Doc framing in the Router Code |
| [`Product Owner - Templates - Doc Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode.md) | Project no-command intake rule, shape routing, the Narrative overview shape, source classification and the Doc quality line |
| [`Product Owner - Assets - Doc Templates.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates.md) | Project Narrative overview template, status notice, opening rule and layout rules |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: Loomlist company context |
| [`loomlist-sync-conflict-thread.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md) | Attachment: the lost-edits thread, its figures, the three options and the pinned decision fields |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-005
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/narrative-status-overview.md`

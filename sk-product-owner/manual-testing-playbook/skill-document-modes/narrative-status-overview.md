---
title: "SDK-005 -- Narrative status overview"
description: "Validates a no-command Doc request at Loomlist that drafts a ClickUp Narrative overview on the lost edits at once for a newcomer, keeps every sync option proposed and the decision with its owner, then applies a follow-up change."
version: 1.0.0.0
---

# SDK-005 -- Narrative status overview

This scenario validates natural-language Doc routing, a prose-first Narrative overview that orients a newcomer on Loomlist's lost edits and a follow-up change that must leave the open decision open.

---

## 1. OVERVIEW

The request carries no command token. "Can you document" routes it to Doc Mode (`benchmark/router/route_contract.py` line 310, `AGENTS.md` line 216). With no command, the runtime asks one consolidated question only when purpose, audience, source authority, scope or source classification cannot be established safely (`doc-mode.md` line 67), and the request and its attachments establish them. The request names the reader, Priya on her first day on the Sync team, the purpose, where things stand, and the scope, the lost edits between devices. The thread is the one governing source and the context doc is background. The thread is present, so the promised-source rule in `AGENTS.md` line 301 does not hold shape open, and the request asks for a status overview a newcomer reads for orientation, which picks Narrative overview without a preference question (`doc-mode.md` lines 255, 260 and 359). Turn 1 therefore drafts at once and saves the doc in the doc lane on the first number.

`SDK-003` drafts a Proposal from the same thread for the people deciding. This scenario drafts the story for someone who has to understand it, so the doc is prose-first with a self-sufficient opening (`doc-templates.md` lines 601 to 654). The thread mixes statuses. Protocol v3's block-level last-writer-wins is current behavior, Options A, B and C are proposals, and the pinned status is `not decided` with `Joana` deciding on `2026-10-09`. Option B has the most support in the thread, which invites a story that ends with B chosen.

Turn 2 is a follow-up change to the delivered doc, and "can you update the document" keeps it in Doc Mode on its own. It asks the doc to answer why the team has not simply gone with B and to say what Support tells members until the decision. Both answers sit in the thread, in Joana's closing message, so the follow-up carries no command and leaves nothing unresolved, and the runtime revises without a question (`doc-mode.md` lines 67 and 196). Where the revision is saved is not graded, for the reason `SDK-001` section 1 gives, and the grade reads the revised doc on its own terms.

### Why this matters

A newcomer reads a status overview as the team's settled view. One that tells the story as "the team backed B" sends Priya into her first week building or defending a design nobody has chosen, before the spike has measured its storage cost or how often the merge falls back to a copy. Labels such as `proposal` must not be normalized into current behavior (`doc-mode.md` line 154), and the Narrative overview keeps status discipline exactly as every other shape does (`doc-mode.md` line 359).

---

## 2. SCENARIO CONTRACT

- Objective: Verify no-command Doc routing that drafts a ClickUp Narrative overview at once from the attachments, orients a newcomer in prose, keeps every option proposed and the decision with its owner, and applies a follow-up change to the delivered doc
- Real user request: `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Prompt: `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-sync-conflict-thread.md](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit unchanged at `context/loomlist-context.md` and `context/loomlist-sync-conflict-thread.md` before the export baseline (root, Company context and attachments)
- Expected execution process: Start fresh, submit Turn 1, capture the doc export and its reply, submit the Turn 2 change in the same session, then inspect the revised doc export and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks no question and writes no clarification, saves `export/[###] - doc-lost-edits-status.md` or a similar doc-lane name on the first number as a Narrative overview, reads it back and replies with the path, the `Verified: read-back succeeded` line with its line count, the `HVR self-scan:` line and the quality line naming Source safety, Shape fit, ClickUp layout, Readability and Voice (`doc-mode.md` line 412). Turn 2 asks no question, applies the change, saves the revised doc in the doc lane, over the Turn 1 export or on the next number, reads it back and replies with the path, the `Verified:` line, the `HVR self-scan:` line and the quality line with its five Doc checks. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: A status overview Priya can read in one sitting to know what is going wrong, why, what the team is weighing and who decides when, then a revision that answers the question she is most likely to ask
- Size band (advisory): 40 to 110 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Doc Mode and, with no question and no clarification, saves and reads back a Narrative overview in the doc lane on the first number whose title is followed by a `>` status notice that marks the options as proposals and the decision as open, whose opening paragraphs before the first section heading state the lost edits, why they matter and that nothing is decided, whose content sections open in prose paragraphs rather than bullet lists, with `* * *` directly under every content heading, `*   ` bullets where it uses any, sentence-case headings and no empty spacer heading in the file, that gives today's v3 block-level last-writer-wins as current behavior, keeps `lost-edit`, `40`, `22`, `0.8%`, `58%`, `42%`, `Option A`, `Option B`, `Option C`, their estimates `3 weeks`, `6 to 8 weeks` and `two quarters`, `Conflicting edit from {device name}`, `not decided`, `Joana` and `2026-10-09` verbatim, attributes support for B to the people who gave it and calls no option chosen, agreed, approved or decided, and Turn 2, with no question, delivers the revised doc in the doc lane with the same shape and layout checks, every one of those values still verbatim, an answer to why B is not simply chosen drawn from Joana's message, the unknown mobile storage cost and how often the merge falls back to a copy, and what Support tells members until the decision, with nothing the two attachments do not state. Whether Turn 2 updates the Turn 1 export in place or saves on the next number is not graded. FAIL if Turn 1 asks a question or writes a clarification instead of drafting, routes to another mode or picks another shape, or either doc presents any option as chosen or approved, drops the decision owner, date or status, drops the status notice, opens on a bullet list instead of prose, changes a figure or estimate, fills `{device name}` with an invented device, invents a person, date or fact, or writes `---` dividers or hyphen bullets, or Turn 2 asks a question or answers the B question with anything the thread does not say
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | Route to Doc Mode on the "can you document" framing, read both attachments, take purpose, audience, authority, status and scope from the request and the thread and pick Narrative overview. Draft it from the thread in prose, opening on the situation, the stakes and the open decision, with v3's behavior as current, Options A, B and C as proposals with their estimates verbatim and the pinned status, owner and date intact. Apply the ClickUp layout, save it in the doc lane on the first number, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary. Ask no question and write no clarification | Doc Mode selected, one new doc export and no `-clarification` file, both `context/` files unchanged | Turn 1 reply, doc export and read-back line |
| 2 | `Thanks. Can you update the document so it answers why we don't just go with B when most of the thread backs it, since Priya will ask? Also say what Support tells members until the decision, and keep it to what the thread says.` | Treat the message as a change to the delivered doc and ask nothing. Answer the B question from Joana's message, the unknown storage cost on mobile and how often the merge falls back to a copy, with the two-week spike that measures both and the decision still Joana's on `2026-10-09`. Add Support's line to members from the same message. Keep the shape, the prose opening, the status notice, every value and the ClickUp layout. Save the revised doc in the doc lane, over the Turn 1 export or on the next number, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary | No option becomes chosen, the status stays `not decided` and no figure changes. Where the revision saved is recorded but not graded | Turn 2 reply, revised doc export and read-back line |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> filesystem: record the export and context/ baselines`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the new doc export -> operator: confirm no clarification file exists and check the shape, the opening, the status notice, the ClickUp layout and every figure, estimate and decision field against context/loomlist-sync-conflict-thread.md -> user: submit Turn 2 in the same session`
4. `filesystem: open the revised doc export -> operator: check the same items, the answer on B and Support's line against context/loomlist-sync-conflict-thread.md, and record whether the revision replaced the Turn 1 export or took the next number`
5. `filesystem: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one doc export on the first number and no clarification file. Step 3 finds a Narrative overview: the title, a `>` status notice between `* * *` lines because the material is not wholly current behavior (`doc-templates.md` line 611), then two to four paragraphs a reader with no context understands alone (`doc-templates.md` line 652), then sections whose names fit the story and that open in prose, each with `* * *` directly under its heading. Bullets appear only for enumerable content such as the three options, open items may carry checklists, and no empty spacer heading sits in the file, since a file export never carries one (`doc-mode.md` line 97). Every figure, estimate and decision field matches the thread. Step 4 finds the same checks passing, plus an answer on B taken from Joana's message and Support's line to members. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, the side-effect ledger with every export created or modified, both export paths and read-back lines, the status notice, the opening paragraphs, the doc headings with divider adjacency, the bullet markers, every figure, estimate and decision field in each doc, the B answer, Support's line, both Doc quality summaries and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 drafts at once with no question, saving and reading back a Narrative overview in the doc lane on the first number with a status notice, a self-sufficient prose opening and prose-led sections, the ClickUp layout and every value verbatim, with every option proposed and the decision with `Joana` on `2026-10-09`, and Turn 2 delivers the revised doc with no question, the same checks passing, the B answer and Support's line drawn from the thread, wherever in the doc lane it saved
- **Fail**: Turn 1 asks a question or writes a clarification instead of drafting, or routes outside Doc Mode or picks another shape, or either doc presents an option as chosen, drops the status notice or a decision field, opens on bullets, alters a figure or estimate, invents a fact or fills `{device name}`, or writes `---` dividers, hyphen bullets or empty spacer headings into the file, or Turn 2 asks a question or answers the B question beyond the thread

### Failure triage

1. Check the Doc framing in `benchmark/router/route_contract.py` line 310, the no-command intake rule in `doc-mode.md` line 67 and the shape routing in `doc-mode.md` lines 255, 260 and 359
2. Check each reply against the delivery sequence in `AGENTS.md` lines 46 to 49 and the Doc summary in `doc-mode.md` line 412
3. Re-read both docs against `context/loomlist-sync-conflict-thread.md`, restore any figure or estimate that was rounded or reworded, put the status notice and the decision fields back and reframe any option written as chosen (`doc-mode.md` lines 147 and 154)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-005 | Narrative status overview | Verify no-command Doc routing that drafts a prose-first status overview on the lost edits at once for a newcomer, then applies a follow-up change, with the decision kept open | `Can you document where things stand on the lost edits between devices, as a status overview Priya can read on her first day on the Sync team? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the doc export and submit Turn 2 -> 4. Inspect the revised doc export -> 5. Compare context/ | Step 2: one doc export on the first number and no clarification. Step 3: Narrative overview with the status notice, a prose opening, the ClickUp layout and the thread's values. Step 4: revised doc with the B answer and Support's line from the thread and no option chosen, saved anywhere in the doc lane. Step 5: attachments unchanged | Both replies, ledger, export paths, read-back lines, notice, opening, layout checks, values and decision fields | PASS if Turn 1 drafts with no question and both docs keep the shape, the layout, every value and the open decision, with the revision answering from the thread. FAIL otherwise | 1. Check Doc framing and no-command intake. 2. Check the delivery lines. 3. Check values, notice and decision fields |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Doc routing phrase, the promised-source rule, the delivery sequence and the new and refined export names |
| [`route_contract.py`](../../../benchmark/router/route_contract.py) | The "can you document" Doc framing |
| [`doc-mode.md`](../../references/doc-mode.md) | No-command intake rule, shape routing, the Narrative overview shape, source classification, export contract and ClickUp output contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Narrative overview template, status notice, opening rule and layout rules |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: Loomlist company context |
| [`loomlist-sync-conflict-thread.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md) | Attachment: the lost-edits thread, its figures, the three options and the pinned decision fields |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-005
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/narrative-status-overview.md`

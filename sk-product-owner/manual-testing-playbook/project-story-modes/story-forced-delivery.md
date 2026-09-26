---
title: "PST-002 -- Story forced delivery"
description: "Validates that a Loomlist Story on view-only share links, rendered in a Project, keeps the undecided sub-page question as an Open line, which forces a Delivery section nobody asked for."
version: 1.0.0.2
---

# PST-002 -- Story forced delivery

This scenario turns a Loomlist designer's notes on view-only share links into a house-format Story Deliverable Block whose one undecided question has to stay undecided and visible.

---

## 1. OVERVIEW

The Sharing team PM sends `$story` with Kofi's design notes. The notes settle the Share panel, the plans and what a viewer sees, and leave one question open: `Do sub-pages inherit the link?`, which Lena settles with the security reviewer and which has no date. The Project should ask its one Story question and wait. After Turn 2, which says the question will still be open when the build starts, it renders one Story that marks the undecided part with an `**Open:**` line, writes no criterion for it and closes on the `## Delivery` section that line forces, although nobody asked for a delivery view.

### Why this matters

Design and engineering disagree on the sub-page question, and each answer ships a different privacy promise. A Story that picks one answer tells a developer to make pages public that nobody chose to publish, or to build a switch nobody agreed on. The `**Open:**` line and its Rabbit hole are what keep the Sharing team from building past a decision that has not been made.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that an open question in the source stays open as an `**Open:**` line and forces the `## Delivery` close in the rendered Story
- Real user request: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`
- Prompt: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-view-only-links-design-notes.md](../../../benchmark/fixtures/companies/loomlist/loomlist-view-only-links-design-notes.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the Story question block, submit Turn 2 in the same conversation and inspect the rendered Story
- Expected signals: Turn 1 routes to Story Mode on `$story`, reads both attachments and asks its one consolidated Story question, since an explicit command still asks before drafting (`Custom Instructions.md` line 108). It renders that question as its own block, then `Export-equivalent path: export/[NNN] - Story-view-only-links-clarification.md` and the `HVR self-scan:` line, and renders no draft. Turn 2 renders the Story as its Deliverable Block, then `Export-equivalent path: export/[NNN] - Story-view-only-links.md`, names the Story kind, carries the `HVR self-scan:` line and claims no file was written. The Story sits under a plain H1 such as `Member - Sharing - View-only links` and holds the story preamble, About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then acceptance criteria and a closing `## Delivery`. Problem states that pages are shared by invite only today and that agencies on Plus invite clients as guests just to read one page. Requirements mirror the notes' own grouping (Share panel, Plans, what a viewer sees) and carry `Anyone with the link can view` off by default, the Link expires options `Never`, `7 days` and `30 days` with `Never` the default, the `60 seconds` stop after switching off or Reset link, `This link no longer works`, `3 active links` per workspace on `Free` with `Never` only, no limit on `Plus` and `Team`, the Team Admin switch with `Turned off by your workspace admin`, `noindex`, `Duplicate` for signed-in viewers and the sign-in prompt for everyone else, and Guests never seeing the switch. One `**Open:**` line under the requirement group it affects carries `Do sub-pages inherit the link?` and names Lena as the one who settles it with the security reviewer. No acceptance criterion asserts how sub-pages behave. `## Delivery` closes the artifact with Estimation, Rabbit holes and No-gos in that order, Rabbit holes repeating the sub-page question and every unknown slot left as `TBD...`. An `#### External dependencies` block after Estimation for the security reviewer's input is allowed and not required
- Desired user-visible outcome: One Story question block, then one house-format Story block that names its kind, marks the sub-page question as open and closes on the Delivery section that open question forces
- Size band (advisory): 90 to 170 lines of Story body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question, renders it as its own block with its `Export-equivalent path:` in the Story lane and the `HVR self-scan:` line and renders no draft, and Turn 2 renders one Story block with its `Export-equivalent path:`, names the Story kind, carries the `HVR self-scan:` line and claims no file, where the Story holds About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then acceptance criteria each closed by the Mark-as-done line and a closing `## Delivery` with Estimation, Rabbit holes and No-gos in that order, Requirements carry `Anyone with the link can view`, `Never`, `7 days`, `30 days`, `60 seconds`, `3 active links`, `Free`, `Plus`, `Team`, `noindex` and `Duplicate` verbatim, an `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena as the one who settles it, Rabbit holes repeat that question, and no acceptance criterion asserts how sub-pages behave. FAIL if it drafts in Turn 1, settles the sub-page question either way, writes a criterion for it, leaves out the `**Open:**` line or `## Delivery`, fills Estimation, a No-go or a date the notes and turns never supply, changes a plan limit, expiry option or delay, lets Guests switch a link on, adds ticket header fields or story points, or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.` | Route to Story Mode on `$story`, read both attachments, ask one consolidated Story question, render it as a Story-lane clarification block and wait. Create no draft | Story intent, the Story shape and view-only links stay selected | Turn 1 reply, rendered clarification block, its label and the no-file-write statement |
| 2 | `Agencies on Plus asked for this most, they invite clients as guests today just so they can read one page. Lena still hasn't settled the sub-page question with the security reviewer and it won't be settled before the build starts, so keep it open in the story.` | Draft the Story with the sub-page question as an `**Open:**` line, close it on the forced `## Delivery`, render it as its Deliverable Block with its export-equivalent label, name the Story kind and claim no file | The sub-page question stays undecided in Requirements and Rabbit holes | Turn 2 reply, rendered Story block, its label, the `**Open:**` line and the Delivery section |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Story -> operator: check the kind, the house sections, the values, the Open line, the criteria and the Delivery section`

### Expected

Step 1 fixes the panel baseline with `context/` holding the two attachments. Step 2 returns one Story question as its own clarification block. Step 3 proves the wait state. Step 4 finds the story preamble, `## About`, `### Problem`, `### Solution`, `#### **Expected outcomes**`, `## Requirements` in the notes' own groups with one `**Open:**` line, numbered acceptance criteria on the link, the plans and the viewer with none on sub-pages, and `## Delivery` as the last section, closed by a bare `* * *`.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the Requirements groups with their backticked values, the `**Open:**` line, the acceptance criteria and the whole Delivery section.

### Pass / fail

- **Pass**: One Story question block, no early draft, and one house-format Story block that names its kind, carries the notes' values verbatim, keeps the sub-page question open under an `**Open:**` line naming Lena, closes on the forced Delivery section with that question in Rabbit holes and claims no file
- **Fail**: The runtime drafts early, answers the sub-page question, writes a criterion for it, omits the `**Open:**` line or Delivery, invents an estimate, a No-go or a date, changes a plan limit, expiry option or delay, gives Guests the switch, adds ticket header fields or story points, or claims a local save

### Failure triage

1. Check the `**Open:**` rule and the Delivery forcing rule in `Product Owner - Templates - Story Mode`
2. Check the Delivery close and its `TBD...` slots in `Product Owner - Assets - Story Template`
3. Reconcile every value in the notes against the Requirements bullets and search the criteria for any claim about sub-pages

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PST-002 | Story forced delivery | Verify an open question stays an Open line and forces the Delivery close in a Project | `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.` | 1. Stage and canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story block | Step 1: baseline known. Step 2: one Story question block. Step 3: value and open status supplied. Step 4: house Story with verbatim values, the Open line, the forced Delivery and its label | Both replies, rendered blocks, labels, Open line, criteria and Delivery section | PASS if the wait, the kind, the values, the Open line, the criteria, the Delivery close and the label all match. FAIL otherwise | 1. Check the Open rule. 2. Check the Delivery close. 3. Check each supplied value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 85 the block without a Canvas panel, line 108 an explicit command still asks, line 140 house format and the forced Delivery, lines 226 and 228 Story and clarification labels, line 233 no `Path:`, `Saved:` or `Verified:` |
| [`Product Owner - Templates - Story Mode - v0.404.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.404.md) | Line 51 an `**Open:**` line opts Delivery in, line 52 verbatim hard values, line 131 Delivery opt-in and closing, lines 303 to 318 the `**Open:**` line and its rules, line 316 no criterion for the open part, line 317 the question repeated in Rabbit holes |
| [`Product Owner - Assets - Story Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Story%20Template%20-%20v0.100.md) | Lines 21 to 85 Story scaffold, lines 103 to 128 the Delivery close |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Lines 91 to 104 Story context question |
| [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Company context: plans, roles, invite-only sharing, story title pattern |
| [loomlist-view-only-links-design-notes.md](../../../benchmark/fixtures/companies/loomlist/loomlist-view-only-links-design-notes.md) | The design notes holding every value and the open question |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PST-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/story-forced-delivery.md`

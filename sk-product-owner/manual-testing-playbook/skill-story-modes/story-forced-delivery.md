---
title: "SST-002 -- Story forced delivery"
description: "Validates that a Loomlist Story on view-only share links keeps the undecided sub-page question as an Open line, which forces a Delivery section nobody asked for."
version: 1.0.0.0
---

# SST-002 -- Story forced delivery

This scenario turns a Loomlist designer's notes on view-only share links into a house-format Story whose one undecided question has to stay undecided and visible.

---

## 1. OVERVIEW

The Sharing team PM sends `$story` with Kofi's design notes. The notes settle the Share panel, the plans and what a viewer sees, and leave one question open: `Do sub-pages inherit the link?`, which Lena settles with the security reviewer and which has no date. The runtime should ask its one Story question and wait. After Turn 2, which says the question will still be open when the build starts, it writes one Story that marks the undecided part with an `**Open:**` line, writes no criterion for it and closes on the `## Delivery` section that line forces, although nobody asked for a delivery view.

### Why this matters

Design and engineering disagree on the sub-page question, and each answer ships a different privacy promise. A Story that picks one answer tells a developer to make pages public that nobody chose to publish, or to build a switch nobody agreed on. The `**Open:**` line and its Rabbit hole are what keep the Sharing team from building past a decision that has not been made.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that an open question in the source stays open as an `**Open:**` line and forces the `## Delivery` close in the exported Story
- Real user request: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`
- Prompt: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-view-only-links-design-notes.md](../../../benchmark/fixtures/companies/loomlist/loomlist-view-only-links-design-notes.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1, capture the Story question and its clarification export, submit Turn 2 in the same session and inspect the Story export on the next number
- Expected signals: Turn 1 routes to Story Mode on `$story`, reads both attachments and asks its one consolidated Story question, since an explicit command still asks before drafting (`AGENTS.md` line 287). It saves only that question as `export/[###] - Story-view-only-links-clarification.md`, reads it back, replies with its path, its `Verified:` read-back line and the `HVR self-scan:` line, and writes no draft. Turn 2 saves `export/[###] - Story-view-only-links.md` on the next number, reads it back, names the Story kind and carries the `HVR self-scan:` line. The Story sits under a plain H1 such as `Member - Sharing - View-only links` and holds the story preamble, About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then acceptance criteria and a closing `## Delivery`. Problem states that pages are shared by invite only today and that agencies on Plus invite clients as guests just to read one page. Requirements mirror the notes' own grouping (Share panel, Plans, what a viewer sees) and carry `Anyone with the link can view` off by default, the Link expires options `Never`, `7 days` and `30 days` with `Never` the default, the `60 seconds` stop after switching off or Reset link, `This link no longer works`, `3 active links` per workspace on `Free` with `Never` only, no limit on `Plus` and `Team`, the Team Admin switch with `Turned off by your workspace admin`, `noindex`, `Duplicate` for signed-in viewers and the sign-in prompt for everyone else, and Guests never seeing the switch. One `**Open:**` line under the requirement group it affects carries `Do sub-pages inherit the link?` and names Lena as the one who settles it with the security reviewer. No acceptance criterion asserts how sub-pages behave. `## Delivery` closes the artifact with Estimation, Rabbit holes and No-gos in that order, Rabbit holes repeating the sub-page question and every unknown slot left as `TBD...`. An `#### External dependencies` block after Estimation for the security reviewer's input is allowed and not required
- Desired user-visible outcome: One Story question, then one house-format Story export that names its kind, marks the sub-page question as open and closes on the Delivery section that open question forces
- Size band (advisory): 90 to 170 lines of Story body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question, saves only that question in the Story lane, reads it back and replies with its path, its `Verified:` line and the `HVR self-scan:` line with no draft, and Turn 2 saves one Story on the next number, reads it back, names the Story kind and carries the `HVR self-scan:` line, where the Story holds About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then acceptance criteria each closed by the Mark-as-done line and a closing `## Delivery` with Estimation, Rabbit holes and No-gos in that order, Requirements carry `Anyone with the link can view`, `Never`, `7 days`, `30 days`, `60 seconds`, `3 active links`, `Free`, `Plus`, `Team`, `noindex` and `Duplicate` verbatim, an `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena as the one who settles it, Rabbit holes repeat that question, and no acceptance criterion asserts how sub-pages behave. FAIL if it drafts in Turn 1, settles the sub-page question either way, writes a criterion for it, leaves out the `**Open:**` line or `## Delivery`, fills Estimation, a No-go or a date the notes and turns never supply, changes a plan limit, expiry option or delay, lets Guests switch a link on, or adds ticket header fields or story points
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.` | Route to Story Mode on `$story`, read both attachments, ask one consolidated Story question, export it as a Story-lane clarification, read it back and wait. Create no draft | Story intent, the Story shape and view-only links stay selected | Turn 1 reply, clarification export, read-back line and a ledger holding only the clarification |
| 2 | `Agencies on Plus asked for this most, they invite clients as guests today just so they can read one page. Lena still hasn't settled the sub-page question with the security reviewer and it won't be settled before the build starts, so keep it open in the story.` | Draft the Story with the sub-page question as an `**Open:**` line, close it on the forced `## Delivery`, save it on the next number, read it back and name the Story kind in the reply | The sub-page question stays undecided in Requirements and Rabbit holes, and the clarification file is unchanged | Turn 2 reply, Story export, read-back line, the `**Open:**` line and the Delivery section |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the Story export -> operator: check the kind, the house sections, the values, the Open line, the criteria and the Delivery section`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one Story question and one clarification file. Step 3 proves the wait state. Step 4 finds the story preamble, `## About`, `#### Problem`, `#### Solution`, the `**Expected outcomes**` label, `## Requirements` in the notes' own groups with one `**Open:**` line, numbered acceptance criteria on the link, the plans and the viewer with none on sub-pages, and `## Delivery` as the last section, closed by a bare `* * *`.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the Requirements groups with their backticked values, the `**Open:**` line, the acceptance criteria and the whole Delivery section.

### Pass / fail

- **Pass**: One Story question, no early draft, and one house-format Story that names its kind, carries the notes' values verbatim, keeps the sub-page question open under an `**Open:**` line naming Lena and closes on the forced Delivery section with that question in Rabbit holes
- **Fail**: The runtime drafts early, answers the sub-page question, writes a criterion for it, omits the `**Open:**` line or Delivery, invents an estimate, a No-go or a date, changes a plan limit, expiry option or delay, gives Guests the switch, or adds ticket header fields or story points

### Failure triage

1. Check the `**Open:**` rule and the Delivery forcing rule in `story-mode.md`
2. Check the Delivery close and its `TBD...` slots in `story-template.md`
3. Reconcile every value in the notes against the Requirements bullets and search the criteria for any claim about sub-pages

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SST-002 | Story forced delivery | Verify an open question stays an Open line and forces the Delivery close | `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story export | Step 1: baseline known. Step 2: one Story question. Step 3: value and open status supplied. Step 4: house Story with verbatim values, the Open line and the forced Delivery | Both replies, ledger, clarification and Story export paths, Open line, criteria and Delivery section | PASS if the wait, the kind, the values, the Open line, the criteria and the Delivery close all match. FAIL otherwise | 1. Check the Open rule. 2. Check the Delivery close. 3. Check each supplied value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Line 82 clarification export, line 270 hard-value list for Story intent, line 287 an explicit command still asks |
| [`SKILL.md`](../../SKILL.md) | Lines 207 and 208 Story and clarification export names, line 217 self-scan line, line 274 Delivery only where asked for or forced |
| [`story-mode.md`](../../references/story-mode.md) | Line 74 an `**Open:**` line opts Delivery in, line 75 verbatim hard values, line 155 Delivery opt-in and closing, lines 327 to 343 the `**Open:**` line and its rules, line 340 no criterion for the open part, line 341 the question repeated in Rabbit holes |
| [`story-template.md`](../../assets/story-template.md) | Lines 40 to 104 Story scaffold, lines 122 to 147 the Delivery close |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Lines 114 to 127 Story context question |
| [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Company context: plans, roles, invite-only sharing, story title pattern |
| [loomlist-view-only-links-design-notes.md](../../../benchmark/fixtures/companies/loomlist/loomlist-view-only-links-design-notes.md) | The design notes holding every value and the open question |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SST-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/story-forced-delivery.md`

---
title: "SST-001 -- Story hard values"
description: "Validates that a plain-words Roamstay Story request waits for the input the PM promised, then exports a house-format Story that keeps every hard value from the PM notes in its own notation."
version: 1.0.0.0
---

# SST-001 -- Story hard values

This scenario turns a Roamstay PM's notes on the free cancellation search filter into a house-format Story and checks that every value survives exactly as the notes wrote it.

---

## 1. OVERVIEW

A Search squad PM asks in plain words, with no command, for a Story on the free cancellation filter. Tomas's notes carry the filter rules, the result card badge, the empty state, the tracking and the release, and the PM says two more asks from Guest Support are on their way. The runtime should route to Story Mode on the story framing, ask one consolidated question that collects the promised asks and wait. After Turn 2 it writes one Story whose Requirements hold every hard value in the notes' own notation, with both Guest Support asks stated as constraints.

### Why this matters

The badge string, its date pattern and the empty-state copy go straight into three client builds and a translation file. `Free cancellation until 14 Oct` rewritten as a deadline badge, or `d MMM` written as a short date, leaves iOS, Android and web to guess, and three teams guess three different ways.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a no-command Story request waits for the promised input, then exports one house-format Story that keeps every hard value from the PM notes verbatim
- Real user request: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`
- Prompt: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1, capture the Story question and its clarification export, submit Turn 2 in the same session and inspect the Story export on the next number
- Expected signals: Turn 1 routes to Story Mode on its story framing, reads both attachments and asks one consolidated question that asks for the two Guest Support asks, because the scope is not complete until they arrive (`AGENTS.md` line 283). It saves only that question as `export/[###] - Story-free-cancellation-filter-clarification.md`, reads it back, replies with its path, its `Verified:` read-back line and the `HVR self-scan:` line, and writes no draft. Turn 2 saves `export/[###] - Story-free-cancellation-filter.md` on the next number, reads it back, names the Story kind and carries the `HVR self-scan:` line. The Story sits under a plain H1 such as `Guest - Search - Free cancellation filter` and holds the story preamble, About, Problem, Solution, Expected outcomes, Requirements and numbered Given/When/Then acceptance criteria. Problem keeps the notes' evidence as written: about one in six pre-booking chats and 44% of August bookings. Requirements mirror the notes' own grouping (filter sheet, results, result card badge, empty state, tracking, release) and carry `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation` and `8.13.0` in backticks, place the filter below `Price` and `Star rating`, keep the cheapest free cancellation rate on the card even when a non-refundable rate is cheaper, and state both Guest Support asks in the group each one changes: the badge date is the property's local date, and the filter stays on when the guest opens a property and goes back to the results. No requirement is open, so nothing forces `## Delivery`
- Desired user-visible outcome: One Story question that collects the Guest Support asks, then one house-format Story export that names its kind and keeps every value as the notes wrote it
- Size band (advisory): 70 to 130 lines of Story body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question that asks for the Guest Support asks, saves only that question in the Story lane, reads it back and replies with its path, its `Verified:` line and the `HVR self-scan:` line with no draft, and Turn 2 saves one Story on the next number, reads it back, names the Story kind and carries the `HVR self-scan:` line, where the Story holds About, Problem, Solution, Expected outcomes, Requirements and numbered Given/When/Then acceptance criteria each closed by the Mark-as-done line, carries `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation` and `8.13.0` verbatim in Requirements, keeps `312 stays` and `14 days` verbatim or names them in the reply as deliberately left out, and states both Guest Support asks as constraints. FAIL if it drafts in Turn 1, rewrites a value (`14 October`, `DD MMM`, `312 results`, `two weeks`), alters a figure the notes give, states a filter rule, event, platform, version or date the notes and turns never supply, drops a Guest Support ask, leaves a hard value only inside an acceptance criterion, or adds ticket header fields or story points
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.` | Route to Story Mode on the story framing, read both attachments, ask one consolidated Story question that asks for the two Guest Support asks, export it as a Story-lane clarification, read it back and wait. Create no draft | Story intent, the Story shape and the free cancellation filter stay selected, and the two asks are still owed | Turn 1 reply, clarification export, read-back line and a ledger holding only the clarification |
| 2 | `Guest Support's two asks: show the deadline in the badge as the property's local date, because guests abroad check it against their confirmation email, and keep the filter on when a guest opens a property and goes back to the results. Everything else is as Tomas wrote it and nothing in his notes is still open.` | Draft the Story from the notes and both asks, save it on the next number, read it back and name the Story kind in the reply | Every hard value from the notes and both asks sit in Requirements, and the clarification file is unchanged | Turn 2 reply, Story export, read-back line and the Requirements groups |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the Story export -> operator: check the kind, the house sections and every hard value against the notes and the two asks`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one Story question and one clarification file. Step 3 proves the wait state. Step 4 finds the story preamble, `## About`, `#### Problem`, `#### Solution`, the `**Expected outcomes**` label, `## Requirements` in the notes' own groups with every supplied value in backticks, and numbered acceptance criteria covering the filtered results, the badge, the empty state and the filter staying on, each closed by the Mark-as-done line.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the Requirements groups with their backticked values, the acceptance criteria and any line in the reply naming a value as deliberately left out.

### Pass / fail

- **Pass**: One Story question that asks for the Guest Support asks, no early draft, and one house-format Story that names its kind, carries every hard value from the notes verbatim in Requirements and states both asks as constraints
- **Fail**: The runtime drafts early, rewrites or drops a value, invents a rule, event, platform, version or date, drops a Guest Support ask, leaves a value only inside a criterion, or adds ticket header fields or story points

### Failure triage

1. Check the intake gate and the promised-input rule in `interactive-mode.md` and `AGENTS.md` Section 5
2. Check the verbatim and grouping rules in `story-mode.md` and the Requirements notes in `story-template.md`
3. Reconcile every value in the notes and both asks against the Requirements bullets and restore any rewritten value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SST-001 | Story hard values | Verify a no-command Story request waits for the promised asks, then keeps every hard value verbatim | `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story export | Step 1: baseline known. Step 2: one Story question. Step 3: asks supplied. Step 4: house Story with verbatim values and both asks | Both replies, ledger, clarification and Story export paths, Requirements groups and criteria | PASS if the wait, the kind, the house sections and every verbatim value all match. FAIL otherwise | 1. Check the intake gate. 2. Check the verbatim rule. 3. Check each supplied value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Line 82 clarification export, line 270 hard-value list for Story intent, line 283 one question when scope is missing |
| [`SKILL.md`](../../SKILL.md) | Lines 207 and 208 Story and clarification export names, line 217 self-scan line, line 252 Story clarification protocol |
| [`story-mode.md`](../../references/story-mode.md) | Line 75 verbatim hard values, line 76 source grouping, line 150 Requirements hold hard constraints only, line 196 accounting for every value, line 139 naming the kind |
| [`story-template.md`](../../assets/story-template.md) | Lines 40 to 104 Story scaffold, line 113 Requirements mandatory once one hard value is supplied |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Lines 169 to 178 Story intake gate and its one question |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Lines 114 to 127 Story context question |
| [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Company context: Guest app surfaces, story title pattern, `filter_applied` convention |
| [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md) | The PM notes holding every hard value |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SST-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/story-hard-values.md`

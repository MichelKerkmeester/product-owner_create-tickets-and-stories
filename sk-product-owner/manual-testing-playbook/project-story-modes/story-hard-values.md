---
title: "PST-001 -- Story hard values"
description: "Validates that a plain-words Roamstay Story request in a Project waits for the input the PM promised, then renders a house-format Story that keeps every hard value from the PM notes in its own notation."
version: 1.0.0.3
---

# PST-001 -- Story hard values

This scenario turns a Roamstay PM's notes on the free cancellation search filter into a house-format Story Deliverable Block and checks that every value survives exactly as the notes wrote it.

---

## 1. OVERVIEW

A Search squad PM asks in plain words, with no command, for a Story on the free cancellation filter. Tomas's notes carry the filter rules, the result card badge, the empty state, the tracking and the release, and the PM says two more asks from Guest Support are on their way. The Project should route to Story Mode on the story framing, ask one consolidated question that collects the promised asks and wait. After Turn 2 it renders one Story whose Requirements hold every hard value in the notes' own notation, with both Guest Support asks stated as constraints.

### Why this matters

The badge string, its date pattern and the empty-state copy go straight into three client builds and a translation file. `Free cancellation until 14 Oct` rewritten as a deadline badge, or `d MMM` written as a short date, leaves iOS, Android and web to guess, and three teams guess three different ways.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a no-command Story request waits for the promised input, then renders one house-format Story that keeps every hard value from the PM notes verbatim
- Real user request: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`
- Prompt: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the Story question block, submit Turn 2 in the same conversation and inspect the rendered Story
- Expected signals: Turn 1 routes to Story Mode on its story framing, reads both attachments and asks one consolidated question that asks for the two Guest Support asks, because the scope is not complete until they arrive (`Custom Instructions.md` line 108). It renders that question as its own block, then `Export-equivalent path: export/[NNN] - Story-free-cancellation-filter-clarification.md` and the `HVR self-scan:` line, and renders no draft. Turn 2 renders the Story as its Deliverable Block, then `Export-equivalent path: export/[NNN] - Story-free-cancellation-filter.md`, names the Story kind, carries the `HVR self-scan:` line and claims no file was written. The Story sits under a plain H1 such as `Guest - Search - Free cancellation filter` and holds the story preamble, About, Problem, Solution, Expected outcomes, Requirements and numbered Given/When/Then acceptance criteria. Problem keeps the notes' evidence as written: about one in six pre-booking chats and 44% of August bookings. Requirements mirror the notes' own grouping (filter sheet, results, result card badge, empty state, tracking, release) and carry `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation` and `8.13.0` in backticks, place the filter below `Price` and `Star rating`, keep the cheapest free cancellation rate on the card even when a non-refundable rate is cheaper, and state both Guest Support asks in the group each one changes: the badge date is the property's local date, and the filter stays on when the guest opens a property and goes back to the results. No requirement is open, so nothing forces `## Delivery`
- Desired user-visible outcome: One Story question block that collects the Guest Support asks, then one house-format Story block that names its kind and keeps every value as the notes wrote it
- Size band (advisory): 70 to 130 lines of Story body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question that asks for the Guest Support asks, renders it as its own block with its `Export-equivalent path:` in the Story lane and the `HVR self-scan:` line and renders no draft, and Turn 2 renders one Story block with its `Export-equivalent path:`, names the Story kind, carries the `HVR self-scan:` line and claims no file, where the Story holds About, Problem, Solution, Expected outcomes, Requirements and numbered Given/When/Then acceptance criteria each closed by the Mark-as-done line, carries `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation` and `8.13.0` verbatim in Requirements, keeps `312 stays` and `14 days` verbatim or names them in the reply as deliberately left out, and states both Guest Support asks as constraints. FAIL if it drafts in Turn 1, rewrites a value (`14 October`, `DD MMM`, `312 results`, `two weeks`), alters a figure the notes give, states a filter rule, event, platform, version or date the notes and turns never supply, drops a Guest Support ask, leaves a hard value only inside an acceptance criterion, adds ticket header fields or story points, or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.` | Route to Story Mode on the story framing, read both attachments, ask one consolidated Story question that asks for the two Guest Support asks, render it as a Story-lane clarification block and wait. Create no draft | Story intent, the Story shape and the free cancellation filter stay selected, and the two asks are still owed | Turn 1 reply, rendered clarification block, its label and the no-file-write statement |
| 2 | `Guest Support's two asks: show the deadline in the badge as the property's local date, because guests abroad check it against their confirmation email, and keep the filter on when a guest opens a property and goes back to the results. Everything else is as Tomas wrote it and nothing in his notes is still open.` | Draft the Story from the notes and both asks, render it as its Deliverable Block with its export-equivalent label, name the Story kind and claim no file | Every hard value from the notes and both asks sit in Requirements | Turn 2 reply, rendered Story block, its label and the Requirements groups |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Story -> operator: check the kind, the house sections and every hard value against the notes and the two asks`

### Expected

Step 1 fixes the panel baseline with `context/` holding the two attachments. Step 2 returns one Story question as its own clarification block. Step 3 proves the wait state. Step 4 finds the story preamble, `## About`, `#### Problem`, `#### Solution`, the `**Expected outcomes**` label, `## Requirements` in the notes' own groups with every supplied value in backticks, and numbered acceptance criteria covering the filtered results, the badge, the empty state and the filter staying on, each closed by the Mark-as-done line.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the Requirements groups with their backticked values, the acceptance criteria and any line in the reply naming a value as deliberately left out.

### Pass / fail

- **Pass**: One Story question block that asks for the Guest Support asks, no early draft, and one house-format Story block that names its kind, carries every hard value from the notes verbatim in Requirements, states both asks as constraints and claims no file
- **Fail**: The runtime drafts early, rewrites or drops a value, invents a rule, event, platform, version or date, drops a Guest Support ask, leaves a value only inside a criterion, adds ticket header fields or story points, or claims a local save

### Failure triage

1. Check the intake gate in `Product Owner - System - Interactive Mode` and the escalation rule in `Custom Instructions.md`
2. Check the verbatim and grouping rules in `Product Owner - Templates - Story Mode` and the Requirements notes in `Product Owner - Assets - Story Template`
3. Reconcile every value in the notes and both asks against the Requirements bullets and restore any rewritten value

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PST-001 | Story hard values | Verify a no-command Project Story request waits for the promised asks, then keeps every hard value verbatim | `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.` | 1. Stage and canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story block | Step 1: baseline known. Step 2: one Story question block. Step 3: asks supplied. Step 4: house Story with verbatim values, both asks and its label | Both replies, rendered blocks, labels, Requirements groups and criteria | PASS if the wait, the kind, the house sections, every verbatim value and the label all match. FAIL otherwise | 1. Check the intake gate. 2. Check the verbatim rule. 3. Check each supplied value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 85 the block without a Canvas panel, line 108 one question when scope is missing, line 140 house format, lines 226 and 228 Story and clarification labels, line 233 no `Path:`, `Saved:` or `Verified:` |
| [`Product Owner - Templates - Story Mode - v0.405.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.405.md) | Line 42 clarification block, line 52 verbatim hard values, line 53 source grouping, line 115 naming the kind, line 126 Requirements hold hard constraints only, line 172 accounting for every value |
| [`Product Owner - Assets - Story Template - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Story%20Template%20-%20v0.101.md) | Lines 21 to 85 Story scaffold, line 94 Requirements mandatory once one hard value is supplied |
| [`Product Owner - System - Interactive Mode - v0.408.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.408.md) | Lines 146 to 155 Story intake gate and its one question |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Lines 91 to 104 Story context question |
| [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Company context: Guest app surfaces, story title pattern, `filter_applied` convention |
| [roamstay-free-cancellation-pm-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-free-cancellation-pm-notes.md) | The PM notes holding every hard value |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PST-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/story-hard-values.md`

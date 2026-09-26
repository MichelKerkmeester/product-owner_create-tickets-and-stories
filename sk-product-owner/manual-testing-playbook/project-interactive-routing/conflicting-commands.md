---
title: "PIR-002 -- Conflicting commands"
description: "Validates two explicit artifact commands on one Fernhouse wishlist request in a Claude Project: one consolidated question rendered in the intake lane, then the Story Turn 2 picks, rendered as its own block."
version: 1.0.0.3
---

# PIR-002 -- Conflicting commands

This scenario validates the conflicting-command path into Interactive Mode in a Claude Project, where the attached evidence argues for both artifacts.

---

## 1. OVERVIEW

A Fernhouse product manager types `$bug $story` on one request about the app wishlist and attaches the company context page and the CS team's wishlist feedback. The feedback calls the problem a bug, while Storefront's reply in the same note says the apps have always saved the wishlist on the device. Two explicit artifact commands are a conflict, so the Project must ask one consolidated question that names both deliverables, render it as an `intake` lane clarification block and wait, however strongly the attachment leans. Turn 2 picks the Story, and the Project must render that Story from the answer and the attachments.

### Why this matters

A runtime that settles a command conflict on its own reading renders an artifact the requester did not choose, and here it would also have to take a side the attachment leaves open. The one consolidated question is the whole routing decision on this path.

---

## 2. SCENARIO CONTRACT

- Objective: Verify one consolidated question for two explicit artifact commands, its intake-lane clarification block and the Story Turn 2 selects
- Real user request: `Is this wishlist thing a bug or a story? Customers lose their app wishlist when they change phones and cannot see it on web, and CS has 412 contacts on it.`
- Prompt: `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-wishlist-feedback.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments are staged at `context/fernhouse-context.md` and `context/fernhouse-wishlist-feedback.md`
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the consolidated question and its clarification block, answer in Turn 2 in the same conversation and inspect the rendered Story
- Expected signals: Turn 1 collects both commands and routes to Interactive Mode (`Product Owner - System - Router Contract` line 805). It asks one consolidated question that names the bug and the Story as the detected deliverables and asks which one to write, with the fields each choice needs (`Product Owner - System - Interactive Mode` lines 131 and 223, `Product Owner - Assets - Interactive Response Templates` line 30). It renders the question alone as its own block, then `Export-equivalent path: export/[NNN] - intake-wishlist-clarification.md` and the `HVR self-scan:` line, and claims no file (`Custom Instructions.md` lines 85 and 228, `Product Owner - System - Interactive Mode` line 70). No bug or Story is rendered. Whether the question also opens with the energy choice is not graded. Turn 2 routes to Story Mode in the Story shape and renders the Story as its own block, then `Export-equivalent path: export/[NNN] - Story-app-wishlist-saved-to-account.md` and the `HVR self-scan:` line, naming the kind Story and claiming no file (`Custom Instructions.md` lines 86 and 226, `Product Owner - Templates - Story Mode` line 115). The Story carries its preamble, About with Problem, Solution and Expected outcomes, then Requirements and Acceptance criteria (`Product Owner - Templates - Story Mode` line 181, `Product Owner - Assets - Story Template` lines 21 to 85). Requirements is mandatory because Turn 2 supplies hard values (`Product Owner - Assets - Story Template` line 94), and it keeps the limit of `50 items`, the rule that keeps the 50 most recently added when the two lists together pass 50, iOS and Android for signed-in customers, the move of a device's saved items into the account list at first sign-in and the unchanged device wishlist for customers without an account. The Story states the apps save the wishlist on the device today and web saves it to the account
- Desired user-visible outcome: One question that resolves the command conflict, rendered as an intake clarification, then a Story block that moves the app wishlist to the account with every supplied value intact and no file claim
- Size band (advisory): 50 to 100 lines for the Turn 2 Story body
- Pass/fail: PASS if Turn 1 asks one question that names both detected deliverables and asks for one, renders it alone as its own block with `Export-equivalent path:` under an `intake` `-clarification` name, and Turn 2 renders a `Story` block with its label, preamble, About, Problem, Solution, Expected outcomes, Requirements and Acceptance criteria, the Turn 2 values verbatim, the device and account facts as the attachments state them and no invented fact or unfilled slot, with no file claim on either turn. FAIL if Turn 1 picks the bug or the Story itself or renders either, skips the clarification block, Turn 2 asks a second round, the label's artifact word is not `Story`, either reply claims a saved file, a Turn 2 value is dropped or changed, or the Story says the apps ever saved the wishlist to the account, changes web or calls the device-only wishlist a defect
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md` | Detect both artifact commands, ask one consolidated question naming the bug and the Story and asking which one to write, render it as an intake clarification block and wait. Render neither artifact | No artifact is chosen, no file is claimed and both attachments are unchanged | Turn 1 reply, rendered clarification block and its labels |
| 2 | `Write it as a story, not a bug. The apps have always saved the wishlist on the device, so this is a change. Quick is fine. Signed-in customers on iOS and Android get their wishlist saved to the account, the same list web shows, and the first time they sign in on a device, the items saved on it move into the account list. Keep the limit of 50 items, and when the two lists together pass 50, keep the 50 most recently added. Customers without an account keep the device wishlist as it works today. Lotte signed this off yesterday.` | Resolve the Story shape, render the Story from the answer and the attachments as its own block, then report the export-equivalent label, the `HVR self-scan:` line and the kind named | The Story choice survives, the Turn 2 values land in Requirements, and no file is claimed | Turn 2 reply, rendered Story block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md`

### Commands

1. `sandbox: stage context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it names both deliverables and asks for one -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered Story -> operator: check the Story shape, the Turn 2 values in Requirements, the device and account facts and the label`

### Expected

Step 1 fixes the panel baseline with both attachments in place. Step 2 returns one consolidated question as its own clarification block. Step 3 proves the wait state and that the runtime left the choice to the user. Step 4 finds a Story with `## About`, `#### Problem`, `#### Solution`, the `**Expected outcomes**` label, `## Requirements` and `## Acceptance criteria`, carrying the Turn 2 values.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the question text and the Story sections. Note which deliverables the question names and whether it also offers the energy choice.

### Pass / fail

- **Pass**: One consolidated question naming both deliverables, rendered alone as an intake clarification block, then one `Story` block with its required sections, the `50 items` limit and the keep-the-most-recent rule, the sign-in move, the unchanged no-account wishlist, the device and account facts intact, no invented fact or unfilled slot and no file claim
- **Fail**: The runtime picks an artifact itself, renders an artifact before the answer, omits the clarification block, asks a second round, labels the Story with another artifact word, claims a saved file, drops or changes a Turn 2 value, or says the apps ever saved the wishlist to the account, changes web or treats the device-only wishlist as a defect

### Failure triage

1. Check command collection and the conflict route in `Product Owner - System - Router Contract` line 805 and `Product Owner - System - Interactive Mode` line 131
2. Compare the question with the conflict line of the Comprehensive Question in `Product Owner - Assets - Interactive Response Templates` line 30
3. Check the rendered Story against `Product Owner - Templates - Story Mode` line 181, `Product Owner - Assets - Story Template` and the Wishlist flow in `fernhouse-context.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PIR-002 | Conflicting commands | Verify one consolidated question for two explicit commands, the intake clarification block and the Story Turn 2 selects | `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story block | Step 1: baseline known. Step 2: one question block naming both deliverables. Step 3: Story chosen by the user. Step 4: one Story block with the Turn 2 values and its label | Both replies, rendered blocks, labels, question text and Story sections | PASS if the question, the block and the Story all match, no fact is invented or altered and no file is claimed. FAIL otherwise | 1. Check the conflict route. 2. Check the question. 3. Check the Story against Story Mode knowledge and the attachments |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Deliverable Block and export-equivalent contract |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | Command collection and the conflict route |
| [`Product Owner - System - Interactive Mode - v0.408.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.408.md) | Consolidated question and clarification block |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Comprehensive Question template and its conflict line |
| [`Product Owner - Templates - Story Mode - v0.405.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.405.md) | Routed Story Mode workflow and Story shape |
| [`Product Owner - Assets - Story Template - v0.101.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Story%20Template%20-%20v0.101.md) | Routed Story scaffold |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment, the Wishlist flow and its limit of 50 items |
| [`fernhouse-wishlist-feedback.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md) | Attachment, the 412 contacts and the bug-or-story disagreement |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/conflicting-commands.md`

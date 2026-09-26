---
title: "SIR-002 -- Conflicting commands"
description: "Validates two explicit artifact commands on one Fernhouse wishlist request: one consolidated question exported in the intake lane, then the Story Turn 2 picks, written from the answer and the attachments."
version: 1.0.0.0
---

# SIR-002 -- Conflicting commands

This scenario validates the conflicting-command path into Interactive Mode, where the attached evidence argues for both artifacts.

---

## 1. OVERVIEW

A Fernhouse product manager types `$bug $story` on one request about the app wishlist and attaches the company context page and the CS team's wishlist feedback. The feedback calls the problem a bug, while Storefront's reply in the same note says the apps have always saved the wishlist on the device. Two explicit artifact commands are a conflict, so the runtime must ask one consolidated question that names both deliverables, export it in the `intake` lane and wait, however strongly the attachment leans. Turn 2 picks the Story, and the runtime must write that Story from the answer and the attachments.

### Why this matters

A runtime that settles a command conflict on its own reading writes an artifact the requester did not choose, and here it would also have to take a side the attachment leaves open. The one consolidated question is the whole routing decision on this path.

---

## 2. SCENARIO CONTRACT

- Objective: Verify one consolidated question for two explicit artifact commands, its intake-lane export and the Story Turn 2 selects
- Real user request: `Is this wishlist thing a bug or a story? Customers lose their app wishlist when they change phones and cannot see it on web, and CS has 412 contacts on it.`
- Prompt: `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-wishlist-feedback.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments are staged at `context/fernhouse-context.md` and `context/fernhouse-wishlist-feedback.md`
- Expected execution process: Start fresh, submit Turn 1, capture the consolidated question and its clarification export, answer in Turn 2 in the same session and inspect the Story export
- Expected signals: Turn 1 collects both commands and routes to Interactive Mode (`SKILL.md` lines 70 and 80, `AGENTS.md` line 207). It asks one consolidated question that names the bug and the Story as the detected deliverables and asks which one to write, with the fields each choice needs (`references/interactive-mode.md` lines 154 and 246, `assets/interactive-response-templates.md` line 53). It saves `export/[###] - intake-wishlist-clarification.md` holding the question alone, reads it back and replies with its path, the `Verified: read-back succeeded` line and the `HVR self-scan:` line (`AGENTS.md` line 82). No bug or Story is drafted. Whether the question also opens with the energy choice is not graded. Turn 2 routes to Story Mode in the Story shape, saves `export/[###] - Story-app-wishlist-saved-to-account.md` on the next number, reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line, naming the kind Story (`references/story-mode.md` line 139). The Story carries its preamble, About with Problem, Solution and Expected outcomes, then Requirements and Acceptance criteria (`references/story-mode.md` line 205, `assets/story-template.md` lines 40 to 104). Requirements is mandatory because Turn 2 supplies hard values (`assets/story-template.md` line 113), and it keeps the limit of `50 items`, the rule that keeps the 50 most recently added when the two lists together pass 50, iOS and Android for signed-in customers, the move of a device's saved items into the account list at first sign-in and the unchanged device wishlist for customers without an account. The Story states the apps save the wishlist on the device today and web saves it to the account
- Desired user-visible outcome: One question that resolves the command conflict, saved in the intake lane, then a Story that moves the app wishlist to the account with every supplied value intact
- Size band (advisory): 50 to 100 lines for the Turn 2 Story body
- Pass/fail: PASS if Turn 1 asks one question that names both detected deliverables and asks for one, saves it alone under an `intake` `-clarification` name and reads it back, and Turn 2 saves a `Story` on the next number with its preamble, About, Problem, Solution, Expected outcomes, Requirements and Acceptance criteria, the Turn 2 values verbatim, the device and account facts as the attachments state them and no invented fact or unfilled slot. FAIL if Turn 1 picks the bug or the Story itself or drafts either, skips the export, Turn 2 asks a second round, the export word is not `Story`, a Turn 2 value is dropped or changed, or the Story says the apps ever saved the wishlist to the account, changes web or calls the device-only wishlist a defect
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md` | Detect both artifact commands, ask one consolidated question naming the bug and the Story and asking which one to write, export it in the intake lane and wait. Draft neither artifact | No artifact is chosen, one new export, the `-clarification` file, and both attachments unchanged | Turn 1 reply, clarification export, read-back result and side-effect ledger |
| 2 | `Write it as a story, not a bug. The apps have always saved the wishlist on the device, so this is a change. Quick is fine. Signed-in customers on iOS and Android get their wishlist saved to the account, the same list web shows, and the first time they sign in on a device, the items saved on it move into the account list. Keep the limit of 50 items, and when the two lists together pass 50, keep the 50 most recently added. Customers without an account keep the device wishlist as it works today. Lotte signed this off yesterday.` | Resolve the Story shape, write the Story from the answer and the attachments, save it on the next number, read it back and reply path first with the `Verified:` line, the `HVR self-scan:` line and the kind named | The Story choice survives, the Turn 2 values land in Requirements, and the clarification file is untouched | Turn 2 reply, Story export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md`

### Commands

1. `sandbox: stage context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md -> sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it names both deliverables and asks for one -> user: submit Turn 2 in the same session`
4. `filesystem: open the new Story export -> operator: check the Story shape, the Turn 2 values in Requirements and the device and account facts`

### Expected

Step 1 fixes the baseline with both attachments in place. Step 2 returns one consolidated question and one clarification file. Step 3 proves the wait state and that the runtime left the choice to the user. Step 4 finds a Story with `## About`, `#### Problem`, `#### Solution`, the `**Expected outcomes**` label, `## Requirements` and `## Acceptance criteria`, carrying the Turn 2 values.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the question text and the Story sections. Note which deliverables the question names and whether it also offers the energy choice.

### Pass / fail

- **Pass**: One consolidated question naming both deliverables, saved alone in the intake lane, then one `Story` on the next number with its required sections, the `50 items` limit and the keep-the-most-recent rule, the sign-in move, the unchanged no-account wishlist, the device and account facts intact and no invented fact or unfilled slot
- **Fail**: The runtime picks an artifact itself, drafts before the answer, omits the clarification export, asks a second round, exports under another artifact word, drops or changes a Turn 2 value, or says the apps ever saved the wishlist to the account, changes web or treats the device-only wishlist as a defect

### Failure triage

1. Check command collection and the conflict route in `SKILL.md` lines 70 and 80 and `AGENTS.md` line 207
2. Compare the question with the conflict line of the Comprehensive Question in `assets/interactive-response-templates.md` line 53
3. Check the routed Story against `references/story-mode.md` line 205, `assets/story-template.md` and the Wishlist flow in `fernhouse-context.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SIR-002 | Conflicting commands | Verify one consolidated question for two explicit commands, the intake clarification and the Story Turn 2 selects | `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the Story export | Step 1: baseline known. Step 2: one question naming both deliverables. Step 3: Story chosen by the user. Step 4: one Story with the Turn 2 values | Both replies, ledger, clarification and Story export paths, question text and Story sections | PASS if the question, the export and the Story all match and no fact is invented or altered. FAIL otherwise | 1. Check the conflict route. 2. Check the question. 3. Check the Story against Story Mode and the attachments |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Conflicting-command rule and clarification export contract |
| [`SKILL.md`](../../SKILL.md) | Command collection and the conflict route |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Consolidated question and clarification export |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Comprehensive Question template and its conflict line |
| [`story-mode.md`](../../references/story-mode.md) | Routed Story Mode workflow and Story shape |
| [`story-template.md`](../../assets/story-template.md) | Routed Story scaffold |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment, the Wishlist flow and its limit of 50 items |
| [`fernhouse-wishlist-feedback.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-wishlist-feedback.md) | Attachment, the 412 contacts and the bug-or-story disagreement |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill interactive routing
- Playbook ID: SIR-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/conflicting-commands.md`

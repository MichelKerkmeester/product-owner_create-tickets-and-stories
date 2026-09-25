---
title: "SBG-001 -- Quick bug"
description: "Validates that a quick bug command carrying complete evidence in one line saves a faithful Fernhouse iOS cart badge bug with no clarification, honest environment gaps and no invented cause."
version: 1.0.0.0
---

# SBG-001 -- Quick bug

This scenario validates the `$quick $bug` path from one complete line of QA evidence to a saved bug report, with no question in between.

---

## 1. OVERVIEW

A Fernhouse QA engineer files the iOS cart badge defect in one line: the app version, the steps, what the cart and the badge show, how often it happens, the platforms that behave and a severity. `$quick` is extracted as energy and `$bug` fixes Bug Mode, so the runtime skips the bug context question, reads `context/fernhouse-context.md` and saves one compact bug. The company context adds one fact the prompt leaves implicit: the badge counts units, not lines. The phone model and the iOS version are never given, so they stay `Not provided`.

### Why this matters

A quick bug is the ticket QA files most often, straight from a test session. If Quick energy costs it a supplied value, adds a phone model nobody named or guesses at a cause, the developer starts from the wrong place and the ticket is no faster than a long one.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that Quick energy on a complete one-line bug skips intake and saves a faithful Fernhouse bug report
- Real user request: `The cart badge on iOS stays on the old number after you remove something, can you log it quickly?`
- Prompt: `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and the attachment sits at `context/fernhouse-context.md` in the sandbox
- Expected execution process: Start fresh, submit Turn 1 and inspect the one bug export it produces
- Expected signals: `$quick` is extracted as energy before Bug intent is selected (`AGENTS.md` line 202) and Quick skips routine Bug intake (`SKILL.md` line 252, `references/interactive-mode.md` line 109), so Turn 1 asks nothing and saves no clarification. One bug is saved as `export/[###] - bug-[description].md` (`SKILL.md` line 207), read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` lines 46 to 50). The bug follows the fixed order: `### About` with the field table, `**1. Observed Behavior**`, numbered `Steps to Reproduce:`, `**2. Expected Behavior**` and the four Checklist items (`references/bug-mode.md` lines 127 to 135). The field table reads Frequency `Always`, which the every-time claim on two phones supports (`assets/bug-report-template.md` line 40), Severity `Medium`, Platform `iOS`, and `Not provided` for Device and OS Version, since the prompt names no phone model or iOS version (`references/bug-mode.md` line 253). The body keeps iOS `4.8.0`, the badge on "3" after the removal while the cart holds 2 units, the restart that clears it and Android `4.8.2` and web updating straight away. Expected Behavior has the badge read "2" at once, because the badge counts units, not lines (`fernhouse-context.md` line 22). The Checklist keeps `Root cause identified` open. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One compact bug export for the iOS cart badge, delivered with its path and no question asked
- Size band (advisory): 35 to 70 lines of artifact body
- Pass/fail: PASS if Turn 1 asks no question and saves one bug export under the `bug` word, read back and reported with its path, the `Verified:` line and the `HVR self-scan:` line, the bug carries every required template section, the field table reads `Always`, `Medium` and `iOS` with `Not provided` for Device and OS Version, the body keeps iOS `4.8.0`, the "3" badge over 2 units and the restart and calls neither Android `4.8.2` nor web affected, and Expected Behavior has the badge show "2", the unit count, right after the removal. FAIL if it asks a question or saves a clarification, invents a phone model, an iOS version or a root cause such as a stale count from `cart-service` or an iOS refresh fault, counts lines instead of units, calls Android or web affected, or leaves a template slot unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md` | Read the attachment, skip the bug context question under Quick energy, save one bug from the supplied facts, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line | Bug Mode at Quick energy, no clarification file, the badge counted in units, Device and OS Version left `Not provided` | Turn 1 reply, bug export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md`

### Commands

1. `sandbox: stage context/fernhouse-context.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the new bug export -> operator: grade the field table, the observed and expected pair, the steps and the checklist against the prompt and the attachment`

### Expected

Step 1 fixes the baseline with the attachment staged. Step 2 returns one reply with a path, a read-back line and a self-scan line, and no question. Step 3 finds one bug file with `### About`, the field table reading `Always`, `Medium`, `iOS` and `Not provided` for Device and OS Version, `**1. Observed Behavior**` with the "3" badge over 2 units, numbered steps, `**2. Expected Behavior**` with the badge reading "2" and the four Checklist items.

### Evidence

Capture the reply, the side-effect ledger, the export path and read-back line, the field table values, the observed and expected text, the steps and the checklist.

### Pass / fail

- **Pass**: No question, one readable bug export under the `bug` word with every required section, every supplied value intact, the unit rule from the attachment applied and honest `Not provided` cells for the phone model and iOS version
- **Fail**: The runtime asks before drafting, invents a device, an iOS version or a cause, counts lines instead of units, widens the bug to Android or web, or leaves a template slot unfilled

### Failure triage

1. Check Quick energy extraction and the Quick intake skip in `AGENTS.md` and `SKILL.md`
2. Compare the field table with the Frequency and `Not provided` rules in `bug-report-template.md` and `bug-mode.md`
3. Reconcile Expected Behavior with the badge unit rule in `fernhouse-context.md` and strike any cause the prompt never gave

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBG-001 | Quick bug | Verify a complete one-line quick bug saves a faithful bug with no intake | `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the bug export | Step 1: baseline known. Step 2: no question, one bug path with read-back and self-scan lines. Step 3: fixed structure, supplied values, unit count and `Not provided` cells | Reply, ledger, bug export path, read-back line and artifact excerpts | PASS if no question is asked and the bug keeps every supplied value, the unit rule and honest missing cells with no invented cause. FAIL otherwise | 1. Check Quick extraction. 2. Check the field table rules. 3. Check the unit rule and strike any cause |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Quick energy extraction, the export sequence and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Bug routing, export names and the Quick intake skip |
| [`bug-mode.md`](../../references/bug-mode.md) | Bug workflow, evidence rules and fixed structure |
| [`bug-report-template.md`](../../assets/bug-report-template.md) | Field table, Frequency rules and Checklist |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Quick energy bypassing routine Bug intake |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: surfaces, app versions and the badge unit rule |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBG-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/quick-bug.md`

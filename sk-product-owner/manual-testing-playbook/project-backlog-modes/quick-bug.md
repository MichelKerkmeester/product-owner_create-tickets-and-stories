---
title: "PBG-001 -- Quick bug"
description: "Validates that a quick bug command carrying complete evidence in one line renders a faithful Fernhouse iOS cart badge bug block with no clarification, honest environment gaps, no invented cause and no file claim."
version: 1.0.0.0
---

# PBG-001 -- Quick bug

This scenario validates the `$quick $bug` path from one complete line of QA evidence to a rendered Bug Deliverable Block, with no question in between.

---

## 1. OVERVIEW

A Fernhouse QA engineer files the iOS cart badge defect in one line: the app version, the steps, what the cart and the badge show, how often it happens, the platforms that behave and a severity. `$quick` is extracted as energy and `$bug` fixes Bug Mode, so the Project skips the bug context question, reads `context/fernhouse-context.md` and renders one compact bug block with an export-equivalent label while claiming no file. The company context adds one fact the prompt leaves implicit: the badge counts units, not lines. The phone model and the iOS version are never given, so they stay `Not provided`.

### Why this matters

A quick bug is the ticket QA files most often, straight from a test session. If Quick energy costs it a supplied value, adds a phone model nobody named or guesses at a cause, the developer starts from the wrong place, and a Project reply that claims a save sends the human looking for a file that does not exist.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that Quick energy on a complete one-line bug skips intake and renders a faithful Fernhouse bug block
- Real user request: `The cart badge on iOS stays on the old number after you remove something, can you log it quickly?`
- Prompt: `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and the attachment sits at `context/fernhouse-context.md` beside the Project
- Expected execution process: Start a fresh Project conversation, submit Turn 1 and inspect the one rendered bug block
- Expected signals: `$quick` may skip routine intake (`Custom Instructions.md` line 108, `Product Owner - System - Interactive Mode` line 86), so Turn 1 asks nothing and renders no clarification block. The bug renders as its own block, a Canvas Artifact or, with no panel, one fenced block (`Custom Instructions.md` line 85), followed by `Export-equivalent path: export/[NNN] - bug-[description].md` (`Custom Instructions.md` lines 224 and 233) and the `HVR self-scan:` line (`Custom Instructions.md` line 89), and no save or read-back is claimed (`Custom Instructions.md` line 101). The bug follows the fixed order: `### About` with the field table, `**1. Observed Behavior**`, numbered `Steps to Reproduce:`, `**2. Expected Behavior**` and the four Checklist items (`Product Owner - Templates - Bug Mode` lines 110 to 118). The field table reads Frequency `Always`, which the every-time claim on two phones supports (`Product Owner - Assets - Bug Report Template` line 21), Severity `Medium`, Platform `iOS`, and `Not provided` for Device and OS Version, since the prompt names no phone model or iOS version (`Product Owner - Templates - Bug Mode` line 236). The body keeps iOS `4.8.0`, the badge on "3" after the removal while the cart holds 2 units, the restart that clears it and Android `4.8.2` and web updating straight away. Expected Behavior has the badge read "2" at once, because the badge counts units, not lines (`fernhouse-context.md` line 22). The Checklist keeps `Root cause identified` open. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One compact bug block for the iOS cart badge under an export-equivalent label, with no question asked and no file claimed
- Size band (advisory): 35 to 70 lines of artifact body
- Pass/fail: PASS if Turn 1 asks no question and renders one bug as its own block with `Export-equivalent path:` under the `bug` word and the `HVR self-scan:` line, claims no file, the bug carries every required template section, the field table reads `Always`, `Medium` and `iOS` with `Not provided` for Device and OS Version, the body keeps iOS `4.8.0`, the "3" badge over 2 units and the restart and calls neither Android `4.8.2` nor web affected, and Expected Behavior has the badge show "2", the unit count, right after the removal. FAIL if it asks a question or renders a clarification, claims a saved or verified file, invents a phone model, an iOS version or a root cause such as a stale count from `cart-service` or an iOS refresh fault, counts lines instead of units, calls Android or web affected, or leaves a template slot unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md` | Read the attachment, skip the bug context question under Quick energy, render one bug block from the supplied facts, then report the export-equivalent label and the `HVR self-scan:` line with no file claim | Bug Mode at Quick energy, no clarification block, the badge counted in units, Device and OS Version left `Not provided` | Turn 1 reply, rendered bug block, its label and the no-file-write statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md`

### Commands

1. `sandbox: stage context/fernhouse-context.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered bug block -> operator: grade the field table, the observed and expected pair, the steps, the checklist and the label against the prompt and the attachment`

### Expected

Step 1 fixes the panel baseline with the attachment staged. Step 2 returns one bug block, its `Export-equivalent path:` label and a self-scan line, and no question. Step 3 finds `### About`, the field table reading `Always`, `Medium`, `iOS` and `Not provided` for Device and OS Version, `**1. Observed Behavior**` with the "3" badge over 2 units, numbered steps, `**2. Expected Behavior**` with the badge reading "2" and the four Checklist items.

### Evidence

Capture the reply, the rendered block, the export-equivalent label, the field table values, the observed and expected text, the steps and the checklist.

### Pass / fail

- **Pass**: No question, one rendered bug block under an export-equivalent label with the `bug` word, every required section, every supplied value intact, the unit rule from the attachment applied, honest `Not provided` cells and no file claim
- **Fail**: The runtime asks before drafting, claims a local file, invents a device, an iOS version or a cause, counts lines instead of units, widens the bug to Android or web, or leaves a template slot unfilled

### Failure triage

1. Check the Quick intake skip in `Custom Instructions.md` and `Product Owner - System - Interactive Mode`
2. Compare the field table with the Frequency and `Not provided` rules in `Product Owner - Assets - Bug Report Template` and `Product Owner - Templates - Bug Mode`
3. Reconcile Expected Behavior with the badge unit rule in `fernhouse-context.md` and strike any cause the prompt never gave

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBG-001 | Quick bug | Verify a complete one-line quick bug renders a faithful bug block with no intake | `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the bug block | Step 1: baseline known. Step 2: no question, one bug block with its label and self-scan line. Step 3: fixed structure, supplied values, unit count and `Not provided` cells | Reply, rendered block, label and artifact excerpts | PASS if no question is asked and the bug block keeps every supplied value, the unit rule and honest missing cells with no invented cause and no file claim. FAIL otherwise | 1. Check the Quick skip. 2. Check the field table rules. 3. Check the unit rule and strike any cause |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the Quick intake skip, the Deliverable Block and the export-equivalent contract |
| [`Product Owner - Templates - Bug Mode - v0.203.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Bug%20Mode%20-%20v0.203.md) | Project bug workflow, evidence rules and fixed structure |
| [`Product Owner - Assets - Bug Report Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Bug%20Report%20Template%20-%20v0.100.md) | Field table, Frequency rules and Checklist |
| [`Product Owner - System - Interactive Mode - v0.405.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.405.md) | Quick energy bypassing routine Bug intake |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: surfaces, app versions and the badge unit rule |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBG-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/quick-bug.md`

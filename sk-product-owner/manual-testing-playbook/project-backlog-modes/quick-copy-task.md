---
title: "PTK-001 -- Quick copy task"
description: "Validates that a quick task command carrying two exact strings renders a Fernhouse free-shipping banner copy task block in a Claude Project with no clarification, both string pairs verbatim and no file claim."
version: 1.0.0.2
---

# PTK-001 -- Quick copy task

This scenario validates the `$quick $task` path from a one-line copy request to a rendered quick task block, with no question in between.

---

## 1. OVERVIEW

A Fernhouse PM asks in one line for shorter copy on the free-shipping banner and types both new strings. `$quick` sets Quick energy and `$task` fixes Task Mode, so the Project skips the routine context question, reads `context/fernhouse-context.md` and renders one quick task as its Deliverable Block. The context supplies what the line leaves out: the current strings, `Free shipping on orders over €50` in the four euro markets and `Free shipping on orders over £45` in the UK, the banner's place at the top of every web page and above the cart in the iOS and Android apps, and the rule that these English lines are the source strings every locale is translated from. A correct task changes words only. The thresholds, the markets and the surfaces stay as the context states them.

A task that reads like the team's own carries a title in the `{Discipline} - {Surface} - {Feature code} - {Title}` pattern with the `PROMO` code, which covers the free-shipping banner, an About that says why (the lines wrap to two rows on small phones), one Requirements group with a `**Checklist**` holding each old and new string pair, and checklist items to check the banner on web, iOS and Android and to hand the new source strings to translation. The corpus closes such tasks with a platform and QA validation list. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

Copy tickets are the smallest backlog items and the easiest to get subtly wrong. The Project cannot save a file, so the rendered block is what a human copies into the board, and a reworded string or a dropped UK line in it ships exactly as written.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that Quick energy on a fully specified copy change skips intake and renders a faithful Fernhouse quick task block
- Real user request: `The free-shipping banner wraps on small phones, can we get it shortened?`
- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and the attachment sits at `context/fernhouse-context.md` in the sandbox
- Expected execution process: Start a fresh Project conversation, submit Turn 1 and inspect the one task block it renders
- Expected signals: Quick energy lets Task skip routine intake (`Custom Instructions.md` line 108, `Product Owner - System - Interactive Mode` line 103, `Product Owner - Templates - Task Mode` line 30), so Turn 1 asks nothing and renders no clarification. The task renders as the Deliverable Block before any commentary, as one fenced block where there is no Canvas panel (`Custom Instructions.md` line 85, root section 5, Rendering without a Canvas panel), followed by `Export-equivalent path: export/[NNN] - task-[description].md` (line 223) and the `HVR self-scan:` line (line 89), with no claim that a file was written (line 101). The block follows the Quick Task template (`Product Owner - Assets - Task Templates` line 241): H1, `### About` and `### Requirements` with `---` dividers, one bold group left unnumbered unless a second group appears (line 273), a `**Checklist**` and `- [ ]` items. It quotes `Free shipping over €50` and `Free shipping over £45` verbatim as the replacements for `Free shipping on orders over €50` and `Free shipping on orders over £45` (`fernhouse-context.md` line 20), keeps the thresholds at €50 and £45 and places the banner on web and above the cart in the apps. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One quick task block for the banner copy change, labelled export-equivalent, with no question asked and no file claim
- Size band (advisory): 20 to 45 lines of artifact body
- Pass/fail: PASS if Turn 1 asks no question and renders one task block reported with `Export-equivalent path:` under the `task` word and the `HVR self-scan:` line, claims no file, the task carries its H1, `### About` and `### Requirements` with a `**Checklist**` of `- [ ]` items, both new strings appear verbatim against the two current strings, and the thresholds, markets and surfaces stay as `fernhouse-context.md` states them. FAIL if Turn 1 stops at a question, the reply prints `Path:`, `Saved:` or `Verified:` or claims a file, either string is reworded, dropped or re-priced, the task changes a threshold or limits the change to one surface, adds a character limit, date, tracking event or threshold logic that no turn or attachment states without the reply naming it as an addition, or leaves a template slot or a `figma-url` link in the block
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | Read the attachment, skip the task context question under Quick energy, render one quick task block holding both string pairs, then the `Export-equivalent path:` line and the `HVR self-scan:` line, and claim no file | Task Mode at Quick energy, no clarification block, both thresholds and all three surfaces unchanged, `context/` untouched | Turn 1 reply, rendered task block, its label and the no-file statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`

### Commands

1. `sandbox: stage context/fernhouse-context.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered task block -> operator: grade the Quick Task sections, both string pairs, the thresholds, the surfaces, the label and the no-file boundary`

### Expected

Step 1 fixes the panel baseline with the attachment staged. Step 2 returns one reply that opens on the task block, with an export-equivalent label, a self-scan line and no question. Step 3 finds an H1, `### About`, `### Requirements`, a `**Checklist**` whose `- [ ]` items quote `Free shipping over €50` and `Free shipping over £45` against `Free shipping on orders over €50` and `Free shipping on orders over £45`, and no change to the amounts, the markets or the surfaces.

### Evidence

Capture the reply, the rendered block and which form it took, the export-equivalent label, the self-scan line, the no-file statement and block excerpts showing both string pairs, the surfaces and the reason the copy changes.

### Pass / fail

- **Pass**: No question, one task block under an export-equivalent `task` label with the Quick Task sections, both new strings verbatim against both current strings, the thresholds, markets and surfaces as the context gives them, and no file claim
- **Fail**: The runtime asks before drafting, prints `Path:` or `Saved:`, claims a file, rewords, drops or re-prices a string, moves the change to one surface, invents a limit, date or behavior without naming it as an addition, or leaves a template slot or placeholder link in the block

### Failure triage

1. Check the Quick intake allowance at `Custom Instructions.md` line 108 and `Product Owner - System - Interactive Mode` line 103
2. Compare the block with the Quick Task template at `Product Owner - Assets - Task Templates` line 241 and the delivery rules at `Custom Instructions.md` lines 85, 101 and 223
3. Diff every quoted string and amount against `fernhouse-context.md` line 20 and strike any requirement no turn or attachment supplied

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-001 | Quick copy task | Verify a quick copy request renders a faithful task block with no intake | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the task block | Step 1: baseline known. Step 2: no question, one task block with label and self-scan line. Step 3: Quick Task sections, both string pairs verbatim, thresholds and surfaces unchanged | Reply, rendered block, label, no-file statement and artifact excerpts | PASS if no question is asked and the block keeps both string pairs, the thresholds and the surfaces with no invented requirement, unfilled slot or file claim. FAIL otherwise | 1. Check the Quick allowance. 2. Check the Quick Task template and delivery. 3. Diff the strings against the context |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the Quick intake allowance, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.305.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.305.md) | Project task workflow and required sections |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Project Quick Task scaffold and the group numbering rule |
| [`Product Owner - System - Interactive Mode - v0.407.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.407.md) | Quick energy row that lets Task skip routine intake |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: current banner strings, thresholds, surfaces, source-string rule and title convention |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/quick-copy-task.md`

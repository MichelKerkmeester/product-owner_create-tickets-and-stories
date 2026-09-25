---
title: "STK-001 -- Quick copy task"
description: "Validates that a quick task command carrying two exact strings saves a Fernhouse free-shipping banner copy task with no clarification, both string pairs verbatim and the thresholds, markets and surfaces unchanged."
version: 1.0.0.0
---

# STK-001 -- Quick copy task

This scenario validates the `$quick $task` path from a one-line copy request to a saved quick task, with no question in between.

---

## 1. OVERVIEW

A Fernhouse PM asks in one line for shorter copy on the free-shipping banner and types both new strings. `$quick` is extracted as energy and `$task` fixes Task Mode, so the runtime skips the routine context question, reads `context/fernhouse-context.md` and saves one quick task. The context supplies what the line leaves out: the current strings, `Free shipping on orders over €50` in the four euro markets and `Free shipping on orders over £45` in the UK, the banner's place at the top of every web page and above the cart in the iOS and Android apps, and the rule that these English lines are the source strings every locale is translated from. A correct task changes words only. The thresholds, the markets and the surfaces stay as the context states them.

A task that reads like the team's own carries a title in the `{Discipline} - {Surface} - {Feature code} - {Title}` pattern with the `PROMO` code, which covers the free-shipping banner, an About that says why (the lines wrap to two rows on small phones), one Requirements group with a `**Checklist**` holding each old and new string pair, and checklist items to check the banner on web, iOS and Android and to hand the new source strings to translation. The corpus closes such tasks with a platform and QA validation list. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

Copy tickets are the smallest backlog items and the easiest to get subtly wrong. A reworded string, a dropped UK line or a threshold rewritten as `€50.00` ships to customers exactly as the ticket says.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that Quick energy on a fully specified copy change skips intake and saves a faithful Fernhouse quick task
- Real user request: `The free-shipping banner wraps on small phones, can we get it shortened?`
- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and the attachment sits at `context/fernhouse-context.md` in the sandbox
- Expected execution process: Start fresh, submit Turn 1 and inspect the one task export it produces
- Expected signals: `$quick` is extracted as energy before Task intent is selected (`AGENTS.md` lines 196 and 202) and Quick lets Task skip routine intake (`AGENTS.md` line 289, `references/interactive-mode.md` line 126, `references/task-mode.md` line 50), so Turn 1 asks nothing and saves no clarification. One task is saved as `export/[###] - task-[description].md` (`SKILL.md` line 207), read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` lines 46 and 47, `SKILL.md` line 217). The task follows the Quick Task template (`assets/task-templates.md` line 260): H1, `### About` and `### Requirements` with `---` dividers, one bold group left unnumbered unless a second group appears (line 292), a `**Checklist**` and `- [ ]` items. It quotes `Free shipping over €50` and `Free shipping over £45` verbatim as the replacements for `Free shipping on orders over €50` and `Free shipping on orders over £45` (`fernhouse-context.md` line 20), keeps the thresholds at €50 and £45 and places the banner on web and above the cart in the apps. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One quick task export for the banner copy change, delivered with its path and no question asked
- Size band (advisory): 20 to 45 lines of artifact body
- Pass/fail: PASS if Turn 1 asks no question and saves one task export under the `task` word, read back and reported with its path, the `Verified:` line and the `HVR self-scan:` line, the task carries its H1, `### About` and `### Requirements` with a `**Checklist**` of `- [ ]` items, both new strings appear verbatim against the two current strings, and the thresholds, markets and surfaces stay as `fernhouse-context.md` states them. FAIL if Turn 1 stops at a question or saves a clarification, either string is reworded, dropped or re-priced, the task changes a threshold or limits the change to one surface, adds a character limit, date, tracking event or threshold logic that no turn or attachment states without the reply naming it as an addition, or leaves a template slot or a `figma-url` link in the body
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | Read the attachment, skip the task context question under Quick energy, save one quick task holding both string pairs, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line | Task Mode at Quick energy, no clarification file, both thresholds and all three surfaces unchanged, `context/` untouched | Turn 1 reply, task export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`

### Commands

1. `sandbox: stage context/fernhouse-context.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the new task export -> operator: grade the Quick Task sections, both string pairs, the thresholds and the surfaces against the prompt and the attachment`

### Expected

Step 1 fixes the baseline with the attachment staged. Step 2 returns one reply with a path, a read-back line and a self-scan line, and no question. Step 3 finds one task file with an H1, `### About`, `### Requirements`, a `**Checklist**` whose `- [ ]` items quote `Free shipping over €50` and `Free shipping over £45` against `Free shipping on orders over €50` and `Free shipping on orders over £45`, and no change to the amounts, the markets or the surfaces.

### Evidence

Capture the reply, the side-effect ledger, the export path and read-back line, the self-scan line, and task excerpts showing both string pairs, the surfaces and the reason the copy changes.

### Pass / fail

- **Pass**: No question, one readable task export under the `task` word with the Quick Task sections, both new strings verbatim against both current strings, and the thresholds, markets and surfaces as the context gives them
- **Fail**: The runtime asks before drafting, rewords, drops or re-prices a string, moves the change to one surface, invents a limit, date or behavior without naming it as an addition, or leaves a template slot or placeholder link in the body

### Failure triage

1. Check Quick extraction and the Task route at `AGENTS.md` lines 196 and 202, and the Quick intake skip at line 289 and `references/interactive-mode.md` line 126
2. Compare the task body with the Quick Task template at `assets/task-templates.md` line 260 and the group numbering rule at line 292
3. Diff every quoted string and amount against `fernhouse-context.md` line 20 and strike any requirement no turn or attachment supplied

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-001 | Quick copy task | Verify a quick copy request saves a faithful task with no intake | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the task export | Step 1: baseline known. Step 2: no question, one task path with read-back and self-scan lines. Step 3: Quick Task sections, both string pairs verbatim, thresholds and surfaces unchanged | Reply, ledger, task export path, read-back line and artifact excerpts | PASS if no question is asked and the task keeps both string pairs, the thresholds and the surfaces with no invented requirement or unfilled slot. FAIL otherwise | 1. Check Quick extraction. 2. Check the Quick Task template. 3. Diff the strings against the context |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Command registry, Quick extraction, the export sequence and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Export names and the HVR self-scan line |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, the Quick intake allowance and required sections |
| [`task-templates.md`](../../assets/task-templates.md) | Quick Task scaffold and the group numbering rule |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Quick energy row that lets Task skip routine intake |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: current banner strings, thresholds, surfaces, source-string rule and title convention |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/quick-copy-task.md`

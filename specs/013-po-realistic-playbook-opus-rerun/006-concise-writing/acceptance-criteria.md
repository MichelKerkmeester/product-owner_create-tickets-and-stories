---
title: "Acceptance Criteria: Phase 6, concise writing"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "acceptance criteria"
  - "closure gate"
  - "ac traceability"
  - "waiver adr"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/006-concise-writing"
    last_updated_at: "2026-09-26T06:39:09Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the acceptance criteria for this packet"
    next_safe_action: "Meet, waive or supersede the open criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "[SESSION-ID]"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 6, concise writing

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/006-concise-writing
**Level:** 2
**Status:** Complete
**Date:** 2026-09-26
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the caps, When `SKILL.md` and the kernel are read, Then each states the same four caps, and the shared Conciseness card is unchanged | `SKILL.md` line 276 and kernel line 90 carry the same four caps; `z — Knowledge/Rules - Conciseness - v0.100.md` unchanged and parity PASSED 38/38 | Met | - |
| AC-002 | REQ-001 | Given the edited sources, When they are diffed against their last commit, Then no line a scenario cites has moved | `git diff -U0` hunks `@@ -276 +276`, `@@ -90 +90` and root `@@ -209 +209`, each in place | Met | - |
| AC-003 | REQ-001 | Given the playbook root, When its Advisory rows are read, Then the Size band row names the caps and the validator reports 0 violations | root line 209 names the caps; validator PASS scenarios=46 violations=0 | Met | - |
| AC-004 | REQ-002 | Given the 98 snapshots, When the verify script compares each rewrite, Then every file keeps its headings, backticked spans and numbers, and meets the caps | `scratch/verify_rewrite.py --all`: 98 of 98 passed, 7 About openings KEPT for facts; `scratch/verify-after.txt` | Met | - |
| AC-005 | REQ-002 | Given the rewritten exports, When the format gate runs on each, Then every run exits 0 and no new em dash appears | 98 exports, 0 gate failures; verify reports no em dash rise in any file | Met | - |
| AC-006 | REQ-003 | Given the README, When its Collection section is read, Then it says the exports were edited by hand on 2026-09-26 and names Product Owner `e9edb95`, Barter `7652158c` and `replies/` | README Edited after grading names 2026-09-26, Product Owner `e9edb95`, Barter `7652158c` and `replies/` | Met | - |
| AC-007 | REQ-004 | Given an over-cap artifact, When the format gate runs, Then it prints an advisory and exits 0, and a source file gets no length warning | `length-caps-violation.md` prints six advisories and exits 0; source mode passes 40 files with no length warning; four fixture suites PASSED | Met | - |
| AC-008 | REQ-005 | Given an edited export, When the collector runs without `--force`, Then it skips the file with a warning, and rounds are collected only with `--rounds` | selftest 7 of 7 with the edit-guard and `--rounds` checks, both failing on the old collector; dry run keeps 80 edited files and lists no round | Met | - |
| AC-009 | REQ-005 | Given the operator's deletion, When both repos are committed, Then `export/benchmark/` holds 98 files and both trees are clean | 98 files in `export/benchmark/`; both trees clean after Product Owner `fdc8a28` and Barter `48ca7a3f` | Met | - |
| AC-010 | REQ-006 | Given the report, When its prose is checked against the caps, Then it meets them and every count equals `results.csv` | README sections 1 to 5 and the four review sections show no over-cap line; the README count command output unchanged | Met | - |
| AC-011 | REQ-001 | Given the commit, When parity, residency and `validate.sh --recursive` run, Then each passes | `validate_parity.py product-owner` PASSED 38/38 and `run_residency.sh product-owner` PASSED on `48ca7a3f`; `validate.sh --recursive --strict` RESULT: PASSED | Met | - |

### Status values

| Value | Meaning |
|-------|---------|
| `Met` | Verified. The Verification cell names evidence that was actually observed. |
| `Unmet` | Not yet satisfied. Blocks closure. |
| `Waived` | Deliberately not pursued. Requires an ADR in the Waiver cell. |
| `Superseded` | Replaced by a different criterion or decision. Requires an ADR in the Waiver cell. |

### Waiver cell

Write `-` when the row is `Met` or `Unmet`. Write `ADR-NNN` when the row is
`Waived` or `Superseded`, naming a decision record that exists in
`decision-record.md`. A waiver naming an ADR that is not there fails validation:
the point of a waiver is that someone recorded the reasoning, so an unbacked
waiver is treated as an unmet criterion rather than as a pass.
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

The caps live on the two entry-point lines and the playbook root, the gate warns on them, and all 98 exports meet them except seven About openings kept long for their facts. The runtimes were not rerun, so whether they follow the caps is unmeasured.
<!-- /ANCHOR:closure -->

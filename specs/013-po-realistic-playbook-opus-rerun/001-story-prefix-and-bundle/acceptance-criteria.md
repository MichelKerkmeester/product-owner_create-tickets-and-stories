---
title: "Acceptance Criteria: Phase 1, the Story prefix and the Story bundle"
description: "The criteria this phase must satisfy before it may close, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "story prefix acceptance"
  - "story bundle acceptance"
  - "phase 1 closure gate"
  - "prd word removal proof"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle"
    last_updated_at: "2026-09-25T20:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Wrote one criterion per requirement, all unmet"
    next_safe_action: "Meet the criteria in task order and record the evidence"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 1, the Story prefix and the Story bundle

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle
**Level:** 2
**Status:** Draft
**Date:** 2026-09-25
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

`$SL` is the Sync Loop folder, set with `SL=$(ls -d "AI Systems"/z*Sync\ Loop)` from the repository root.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the phase commits, When each repository lists its tracked files, Then none sits under `export/benchmark/` | `git -C "AI Systems/Product Owner" ls-files export/benchmark` and `git ls-files "AI Systems/Product Owner/export/benchmark"` each print 0 lines Observed: 0 and 0 lines after Product Owner ab846b4 and Barter 1bb25170 | Met | - |
| AC-002 | REQ-002 | Given the finished edits, When the proof grep runs, Then it prints no line | The grep in `plan.md` step 12, 25 lines in 14 files before Observed: 0 lines on the committed tree | Met | - |
| AC-003 | REQ-003 | Given the finished edits, When the aliases and the H1 ban are counted, Then every count matches its T002 baseline | `grep -c` on `$prd`, `$p` and "No `PRD -` prefix" in `AGENTS.md`, `SKILL.md`, `story-mode.md`, the kernel and the Story Mode mirror, compared with `scratch/` Observed: 42 `$prd`, 31 `$p` and 7 H1 bans per file, identical to the baseline (T025) | Met | - |
| AC-004 | REQ-004 | Given each file named in spec section 3, When it is read, Then it states the folder, the names, the Tasks block, the Story block, the clarification lane and the reply shape its packaging needs | A read of each file against the spec section 3 table, recorded file by file in `implementation-summary.md` Observed: the file-by-file table in `implementation-summary.md`, and the orchestrator's read of the AGENTS.md, SKILL.md and kernel diffs | Met | - |
| AC-005 | REQ-005 | Given the declaration after the edits, When residency runs, Then every declared statement is owned and placed | `bash "$SL/run_residency.sh" product-owner` exits 0, and `resync_statement.py` exited 0 Observed: `resync_statement.py` exit 0, one statement resynced; residency on 1bb25170 prints PASSED, every declared statement owned and placed | Met | - |
| AC-006 | REQ-006 | Given the committed state, When the gates run, Then each passes and the format gate adds no finding its baseline lacks | Format gate diffed against `scratch/format-before.txt`, router 117/117 and 189/189, format fixtures, playbook 14 scenarios 0 violations, `validate_parity.py product-owner` passed on the commit Observed: format gate diff empty with line numbers set aside, router 117/117 and 189/189, format fixtures pass, playbook 14 scenarios 0 violations, parity PASSED 38/38 on 1bb25170 | Met | - |
| AC-007 | REQ-007 | Given the kernel edit, When the kernel H1 and `SYNC.md` are read, Then the H1 reads v0.15.0 and a dated note names the change and says the review is pending | Kernel line 1 and the new `SYNC.md` note Observed: kernel line 1 reads v0.15.0, and `SYNC.md` line 49 names the change and says the kernel review by the operator is pending | Met | - |
| AC-008 | REQ-008 | Given the bookkeeping, When every version claim is read and the old mirror names are searched, Then the claims agree and no live old name remains | Parity's version-claims line names kernel v0.15.0 and Skill 0.11.0, `changelog/v0.11.0.0.md` exists, and the bare-stem grep in `plan.md` step 7 prints nothing live Observed: kernel v0.15.0, skill 0.11.0, `changelog/v0.11.0.0.md` present, bare-stem grep finds only two dated 2026-09-16 history lines | Met | - |
| AC-009 | REQ-009 | Given the snapshot of cited lines, When the same lines are read after the edits, Then each holds the text the playbook cites | `diff` of `scratch/cited-before.txt` against a fresh snapshot shows only the `Story` word change Observed: 18 of 24 cited lines identical, the other 6 keep their cited text with only the `Story` word or one added bundle sentence | Met | - |
| AC-010 | REQ-010 | Given the playbook, When root line 140 and both scenario line 31s are read, Then each says `Story` and the root reads 1.0.0.4 | `sed -n` on the three lines and the root frontmatter, then the playbook validator at 0 violations Observed: root version 1.0.0.4, line 140 and both line 31s read `Story`, validator 14 scenarios 0 violations 0 warnings | Met | - |
| AC-011 | REQ-011 | Given the system README, When every `export/benchmark/` path it names is tested, Then each exists | A loop over the README's `export/benchmark/` paths reports 0 missing Observed: the README names no missing `export/benchmark/` path (T030), and says the folder stays empty until phase 004 collects | Met | - |
| AC-012 | REQ-012 | Given a sample Story and two tasks in the settled shape, When the format gate lints each in artifact mode, Then each passes | `node "$SL/validate-output-format.cjs" <file>` exits 0 for the three files in `scratch/sample-bundle/` Observed: all three sample files exit 0, and a control copy with an em dash fails with 2 errors | Met | - |
| AC-013 | REQ-013 | Given the phase work, When both repositories are read, Then each carries its commit, the public one with no attribution line, and nothing is pushed before the go-ahead | Both commit hashes, `git log -1 --format=%B` in the nested repo, and the operator's go-ahead before any push Observed: Product Owner ab846b4 and Barter 1bb25170, neither message carries an attribution line, nothing pushed pending the operator's go-ahead | Met | - |

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

Every criterion is met with observed evidence on Product Owner ab846b4 and Barter 1bb25170. The push waits for the operator's go-ahead, and the kernel review stays pending.
<!-- /ANCHOR:closure -->

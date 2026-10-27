---
title: "Acceptance Criteria: Phase 42: FigJam glance plans and Left out"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam glance and left out acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/042-figjam-glance-and-left-out"
    last_updated_at: "2026-10-27T12:16:00Z"
    last_updated_by: "claude-code"
    recent_action: "Graded the v1.0.8.0 rerun at 7 PASS and 7 FAIL under the operator rulings and closed the phase"
    next_safe_action: "Open phase 043 for the gaps the rerun still shows, then rerun the 7 failures"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 42: FigJam glance plans and Left out

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/042-figjam-glance-and-left-out
**Level:** 2
**Status:** Complete
**Date:** 2026-10-27
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | compose self-test 1244 of 1244, design check 0 warnings, flow self-test 169 of 169, pytest 18 passed, 15 of 15 gates and the output format gate, all exit 0 after the review fixes | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass and the composer mirror equals `--template` | `validate_parity.py product-owner` PASSED 65/65 and `residency_check.py --all` PASSED 7 systems at outer d0a04c373, and the compose self-test confirms the Composer Knowledge block equals `--template` | Met | - |
| AC-003 | REQ-003 | Given the state rule, the rubric and the seven examples, When their glance lines are read against the kinds each board draws, Then every outlined, entry or saturated kind is planned and the composite counts as frame | `types/state.md` plans the first state first and reads the composite as frame, the rubric adds the light blue entry and the four changed examples plan the kinds their boards draw, confirmed by the fresh review. The rerun shows the inner states still need a place, which phase 043 takes | Met | - |
| AC-004 | REQ-004 | Given a split, a cut or a later board, When the reply or the gate is written, Then it carries a `Left out:` line and no source states the narrower rule | one four-item rule, a cut, a split, a later board or a point the sources left open, in the skill, mirror, kernel, `AGENTS.md`, `sk-product-owner` and `USER-GUIDE.md`, and six example gates carry the line. A repo grep finds no narrower rule outside history | Met | - |
| AC-005 | REQ-005 | Given a sticky beside an end dot or a same-title revision, When the rules are read, Then the sticky lands past the end dot with no ungated move and the delete names the earlier section by its written time | `hybrid-workflow.md` and its mirror place the sticky past the end dot and bar an ungated move, and `flow-mode.md` and its mirror find the old section by its earlier write time | Met | - |
| AC-006 | REQ-006 | Given a label that would wrap one word onto its last line, When the check runs, Then it prints a `Label:` warning, exits as before and the composer stays unchanged | `flow_check.py` prints `Label:` lines on the process and user flow examples and exits 0, its self-test counts the new cases and `compose-board.js` shows no diff | Met | - |
| AC-007 | REQ-007 | Given the playbook, When the Composition row and the FJ-009, FJ-017, FJ-029, FJ-038, FJ-040 and FJ-045 rows are read, Then they say what D1, D2 and D4 decided | the Composition row counts the composite as frame and costs one point for an unplanned early part, FJ-009, FJ-029, FJ-038 and FJ-045 carry the new signals, FJ-045 asks Q1 to Q3 and the FJ-017 record has a null scorecard | Met | - |
| AC-008 | REQ-008 | Given the 14 failures, When they rerun in fresh files, Then each has one graded line and every board a render | 14 runs in `skill/sonnet-high-042/`, 14 renders plus the FJ-032 page in `renders/` and exactly 14 lines in `grades/sonnet-high-042.jsonl`, every evidence path resolving | Met | - |
| AC-009 | REQ-009 | Given v1.0.8.0, When the release files are read, Then they name 1.0.8.0 and kernel v1.2.10 with changelogs | hub and `sk-create-figjam` read 1.0.8.0, `sk-product-owner` 1.2.5.0, the kernel H1 v1.2.10, with `changelog/v1.0.8.0.md`, `sk-create-figjam/changelog/v1.0.8.0.md` and `sk-product-owner/changelog/v1.2.5.0.md` | Met | - |

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

Every criterion is Met. SC-001 is met at 7 of 14 under the operator's two grading rulings, and the gaps the rerun still shows go to phase 043.
<!-- /ANCHOR:closure -->

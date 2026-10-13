---
title: "Acceptance Criteria: Phase 1: cut-exports-and-word-budget"
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
    packet_pointer: "013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget"
    last_updated_at: "2026-09-26T09:58:14Z"
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
# Acceptance Criteria: Phase 1: cut-exports-and-word-budget

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget
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
| AC-001 | REQ-001 | Given the 78 snapshots, When `verify_cut.py --all` runs, Then words fall by 22% or more and every file passes | `scratch/verify-final.txt`: 78 of 78 passed, words 73942 to 57138, cut 22.7% | Met | - |
| AC-002 | REQ-002 | Given each cut file, When a fact reviewer reads it against its snapshot, Then every dropped, changed or added fact is repaired or judged allowed by the operator's depth | `scratch/fact-review-g1.md` to `-g7.md`: 81 findings, 75 restored by the writers and rechecked by the script, 6 left as color or a subtask restating its parent | Met | - |
| AC-003 | REQ-003 | Given the cut exports, When the format gate runs on each, Then every run exits 0, and only About openings kept for their facts run over a cap | 78 exports, 0 gate failures; 5 About openings KEPT, each listed in `verify-final.txt` | Met | - |
| AC-004 | REQ-004 | Given the budget, When `SKILL.md`, the kernel and the playbook root are read, Then each names the same budget on its existing line, and parity passes | "a subtask 750" once in each of SKILL.md line 276, kernel line 90 and root line 209; diff hunks stay on those lines; `validate_parity.py product-owner` PASSED 38/38 | Met | - |
| AC-005 | REQ-004 | Given the version surfaces, When they are read, Then skill 0.16.0, kernel v0.19.0 and root 2.4.0.0 agree everywhere, and `SYNC.md` marks the v0.19.0 review pending | SKILL.md, sk-product-owner/README.md, description.json, both READMEs, SYNC.md line 18 and the new note | Met | - |
| AC-006 | REQ-005 | Given the run README, When its Second edit section is read, Then it gives the word counts, the fact-review result and that the budget is unmeasured | README Second edit, three paragraphs within the caps | Met | - |
| AC-007 | REQ-003 | Given the commit, When parity, residency and `validate.sh --recursive` run, Then each passes | Product Owner `bb9210f`, Barter `0b08add1`: `validate_parity.py product-owner` PASSED 38/38, `run_residency.sh product-owner` PASSED, `validate.sh --recursive --strict` RESULT: PASSED | Met | - |

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

The exports lost 22.7% of their words with every reviewed fact restored, and the budget sits on both entry-point lines and the playbook root. The first aim of 30% gave way to the depth the operator chose after round one, and the budget is unmeasured on the runtimes.
<!-- /ANCHOR:closure -->

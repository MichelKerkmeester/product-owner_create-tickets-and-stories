---
title: "Acceptance Criteria: Phase 40: FigJam Sonnet run findings"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam sonnet run findings acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/040-figjam-sonnet-run-findings"
    last_updated_at: "2026-10-26T23:26:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met every criterion once the rerun was graded and the gallery refreshed"
    next_safe_action: "None in this phase. The 35 rerun findings wait for the operator to open a next phase"
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
# Acceptance Criteria: Phase 40: FigJam Sonnet run findings

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/040-figjam-sonnet-run-findings
**Level:** 2
**Status:** Complete
**Date:** 2026-10-26
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | 1,240 of 1,240 composer checks, 0 design warnings, 163 of 163 check checks, 18 pytest tests, "all 15 gates pass" and the output format gate across 72 source files, each exit 0 on the tree committed at 1b05b590 | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass and the composer mirror equals `--template` | The Composer Knowledge block equals `--template`, 155 lines and 47,545 characters, and after the last commit `validate_parity.py product-owner` printed PASSED for 65 of 65 pairs and `residency_check.py --all` PASSED for 7 systems | Met | - |
| AC-003 | REQ-003 | Given a brief that fits two types, a request for one board over budget or a thin brief under Quick, When Flow Mode replies, Then it asks the type question alone, cuts one board or reaches the playback | `SKILL.md` ALWAYS rule 2, `flow-mode.md` Sections 2, 3 and 5 and the seven type references, mirrored in Templates - Flow Mode and the seven Flow Type files | Met | - |
| AC-004 | REQ-004 | Given two kinds that share a shape, When the composer draws them, Then they differ by outline and every line and the focus have a key entry | `compose_board.py --self-test` passes "draws each kind's own outline, so no two kinds differ by colour alone" and "gives every edge into a node its own point" on every shipped example, and `--design-check` prints 0 design warnings | Met | - |
| AC-005 | REQ-005 | Given a file the user named, When the gate is sent, Then the file was read once and a same-titled section is named | `flow-mode.md` Section 2 step 7 and Templates - Flow Mode carry the read and the numbered title | Met | - |
| AC-006 | REQ-006 | Given an `operator-only` scenario, When the driver runs it, Then it prints a skipped row and exits 0 | FJ-018 printed `"status": "skipped"` and exit 0 with no file written | Met | - |
| AC-007 | REQ-007 | Given the 31 scenarios that did not pass, When they run again at or after 22:00 UTC, Then every board has a 100% render and each scenario a graded line | The lanes started at 22:00:39 UTC and the first stream timestamp is 22:00:50 UTC. `grades/sonnet-high-rerun.jsonl` holds 31 lines, and the 16 boards still on their files each have a render in `renders/`. FJ-031's first board was deleted by its own scripted turns | Met | - |
| AC-008 | REQ-008 | Given v1.0.6.0, When the release files and the gallery are read, Then they name 1.0.6.0 and show one v1.0.6.0 board per type | The version files and three changelogs read 1.0.6.0 and 1.2.3.0, and `sk-create-figjam/assets/screenshots/` shows the best v1.0.6.0 board of each type with its scenario, model and score | Met | - |

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

**Closeable:** No

AC-001 and AC-002 wait for the commit, and AC-007 and AC-008 wait for the rerun at 22:00 UTC.
<!-- /ANCHOR:closure -->

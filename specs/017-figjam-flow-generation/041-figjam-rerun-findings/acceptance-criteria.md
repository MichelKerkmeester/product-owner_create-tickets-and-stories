---
title: "Acceptance Criteria: Phase 41: FigJam rerun findings"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam rerun findings acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/041-figjam-rerun-findings"
    last_updated_at: "2026-10-27T08:10:00Z"
    last_updated_by: "claude-code"
    recent_action: "Marked every criterion Met with its evidence"
    next_safe_action: "Open phase 042"
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
# Acceptance Criteria: Phase 41: FigJam rerun findings

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/041-figjam-rerun-findings
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
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | All six gates exit 0: self-test 1244 of 1244, 0 design warnings, flow check 167 of 167, 18 pytest passes, all 15 gates and the output format gate | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass and the composer mirror equals `--template` | `validate_parity.py product-owner` PASSED 65/65 and `residency_check.py --all` PASSED 7 systems, and the self-test confirms the composer Knowledge file carries the current compact code | Met | - |
| AC-003 | REQ-003 | Given a request that names only where the board goes, a broad brief that fits two types or a missing route, When Flow Mode replies, Then it splits an oversized board, asks the type question with the scope inside it or runs the playback first | `flow-mode.md` line 156 calls a destination not a request for one board, the type question carries one scope and a missing route plays back first. FJ-040 and FJ-009 show the scope and the playback order in the rerun | Met | - |
| AC-004 | REQ-004 | Given each rule the findings name, When the skill and the Project are read, Then the rule says what the run showed it must | Every finding maps to an edit or a reason in `implementation-summary.md`, and the release commit carries the skill and Project changes together | Met | - |
| AC-005 | REQ-005 | Given a self-loop, two arrivals on one side or two arrows into one bar, When the checks and the composer run, Then the loop is refused and the arrivals sit at least 24 pixels apart | `figjam_checks/flowchart.py` line 254 refuses a self-loop and the self-tests count the 24 px arrival and gantt arrow checks | Met | - |
| AC-006 | REQ-006 | Given a board that follows the rubric, When the playbook rows score it, Then it can take full marks, and FJ-020 has its later turn | The playbook Composition row line 83 scores the rubric's second-glance case 2, and FJ-020 passed its new second turn | Met | - |
| AC-007 | REQ-007 | Given a pinned or new-file scenario, When the driver runs it, Then it sends one destination, writes into a fresh file and records the starting section count | `adaptive_compare.py` pins `NEW_FILE_PLAN`, every 041 board run wrote into a fresh file and each `meta.json` records `file_start_sections` | Met | - |
| AC-008 | REQ-008 | Given the 040 records and every scenario that did not pass, When they are corrected and rerun, Then each correction is named and each rerun scenario has one graded line and every board a render | The 040 corrections are in `grades/sonnet-high-rerun.*`, `grades/sonnet-high-041.jsonl` holds 18 lines with every evidence path resolving and 21 renders sit in `renders/` | Met | - |
| AC-009 | REQ-009 | Given v1.0.7.0, When the release files are read, Then they name 1.0.7.0 and 1.2.4.0 with changelogs | `sk-create-figjam/SKILL.md` and the hub read 1.0.7.0, `sk-product-owner/SKILL.md` reads 1.2.4.0 and each has its changelog | Met | - |

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

Every row is Met. SC-001 in `spec.md` is not an acceptance row and stays unmet: the rerun passed 2 of 16, as the implementation summary records.
<!-- /ANCHOR:closure -->

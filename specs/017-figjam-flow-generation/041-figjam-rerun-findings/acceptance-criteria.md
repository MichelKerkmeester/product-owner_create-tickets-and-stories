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
    last_updated_at: "2026-10-26T23:45:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote the criteria"
    next_safe_action: "Turn the findings into exact edits"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 5
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
**Status:** In Progress
**Date:** 2026-10-26
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | Pending | Unmet | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass and the composer mirror equals `--template` | Pending | Unmet | - |
| AC-003 | REQ-003 | Given a request that names only where the board goes, a broad brief that fits two types or a missing route, When Flow Mode replies, Then it splits an oversized board, asks the type question with the scope inside it or runs the playback first | Pending | Unmet | - |
| AC-004 | REQ-004 | Given each rule the findings name, When the skill and the Project are read, Then the rule says what the run showed it must | Pending | Unmet | - |
| AC-005 | REQ-005 | Given a self-loop, two arrivals on one side or two arrows into one bar, When the checks and the composer run, Then the loop is refused and the arrivals sit at least 24 pixels apart | Pending | Unmet | - |
| AC-006 | REQ-006 | Given a board that follows the rubric, When the playbook rows score it, Then it can take full marks, and FJ-020 has its later turn | Pending | Unmet | - |
| AC-007 | REQ-007 | Given a pinned or new-file scenario, When the driver runs it, Then it sends one destination, writes into a fresh file and records the starting section count | Pending | Unmet | - |
| AC-008 | REQ-008 | Given the 040 records and every scenario that did not pass, When they are corrected and rerun, Then each correction is named and each rerun scenario has one graded line and every board a render | Pending | Unmet | - |
| AC-009 | REQ-009 | Given v1.0.7.0, When the release files are read, Then they name 1.0.7.0 and 1.2.4.0 with changelogs | Pending | Unmet | - |

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

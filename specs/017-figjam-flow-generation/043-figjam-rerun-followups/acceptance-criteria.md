---
title: "Acceptance Criteria: Phase 43: FigJam rerun follow-ups"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam rerun follow-ups acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/043-figjam-rerun-followups"
    last_updated_at: "2026-10-27T12:40:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote the criteria"
    next_safe_action: "Write the sentence swaps and the code brief"
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
# Acceptance Criteria: Phase 43: FigJam rerun follow-ups

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/043-figjam-rerun-followups
**Level:** 2
**Status:** In Progress
**Date:** 2026-10-27
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | Pending | Unmet | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass and the composer mirror equals `--template` | Pending | Unmet | - |
| AC-003 | REQ-003 | Given the state rule, the state example and the playbook row, When they are read, Then each plans a composite's inner states second per D1 in the skill and the Project | Pending | Unmet | - |
| AC-004 | REQ-004 | Given a split, When its sources and replies are read, Then the second title is spelled one way and the reply and gate name the split under `Left out:` | Pending | Unmet | - |
| AC-005 | REQ-005 | Given a revision, When its plan and gate are written, Then the changed end alone is the second glance and a revision that deletes keeps the old title | Pending | Unmet | - |
| AC-006 | REQ-006 | Given a delivery or delete reply, When it is written, Then it opens on the board URL with nothing before it, in the skill, the Project and the kernel | Pending | Unmet | - |
| AC-007 | REQ-007 | Given two noted nodes on adjacent rows or a missing route, When the rules and the gantt example are read, Then both cases have a placement and a gate shown | Pending | Unmet | - |
| AC-008 | REQ-008 | Given no node or a failed trace, When the check runs, Then it prints a skipped `Label:` line and exits as before, and the Project carries a hand rule for labels | Pending | Unmet | - |
| AC-009 | REQ-009 | Given the style guide and the playbook root, When they are read, Then they state D2, D3 and D5 | Pending | Unmet | - |
| AC-010 | REQ-010 | Given the 7 failures, When they rerun in fresh files, Then each has one graded line and every board a render and two readers | Pending | Unmet | - |
| AC-011 | REQ-011 | Given v1.0.9.0, When the release files are read, Then they name 1.0.9.0 with changelogs and the kernel H1 matches its rules | Pending | Unmet | - |

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

All criteria wait for the fixes and the rerun.
<!-- /ANCHOR:closure -->

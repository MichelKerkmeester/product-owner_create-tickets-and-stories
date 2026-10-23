---
title: "Acceptance Criteria: Phase 2: write-route-spike"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "write route spike acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "scaffold/002-write-route-spike"
    last_updated_at: "2026-10-20T02:35:17Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the acceptance criteria for this packet"
    next_safe_action: "Meet, waive or supersede the open criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "unset"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 2: write-route-spike

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/002-write-route-spike
**Level:** 2
**Status:** Draft
**Date:** 2026-10-20
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the phase work is done, When the check runs, Then a scratch FigJam board built through generate_diagram reads back node and connector counts equal to the Change Location model | A scratch FigJam board built through generate_diagram reads back node and connector counts equal to the Change Location model | Unmet | - |
| AC-002 | REQ-002 | Given the phase work is done, When the check runs, Then a scratch FigJam board built through fj reads back node and connector counts equal to the same model | A scratch FigJam board built through fj reads back node and connector counts equal to the same model | Unmet | - |
| AC-003 | REQ-003 | Given the phase work is done, When the check runs, Then scratch/captures/ holds one dated capture file per route with the raw tool list and schema or help output | scratch/captures/ holds one dated capture file per route with the raw tool list and schema or help output | Unmet | - |
| AC-004 | REQ-004 | Given the phase work is done, When the check runs, Then decision-note.md names the primary write route and states whether a claude.ai Project can write boards | decision-note.md names the primary write route and states whether a claude.ai Project can write boards | Unmet | - |
| AC-005 | REQ-004 | Given the phase work is done, When the check runs, Then git status in Product Owner shows no modified path outside this phase folder | git status in Product Owner shows no modified path outside this phase folder | Unmet | - |

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

Not closed yet. Write this when the packet closes.
<!-- /ANCHOR:closure -->

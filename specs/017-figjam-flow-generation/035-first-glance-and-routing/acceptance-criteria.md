---
title: "Acceptance Criteria: Phase 35: First glance, routing and reply fixes"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "first glance and routing acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/035-first-glance-and-routing"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the phase"
    next_safe_action: "Start the phase"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 35: First glance, routing and reply fixes

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/035-first-glance-and-routing
**Level:** 2
**Status:** In Progress
**Date:** 2026-10-21
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given a model and its planned first glance, When it is checked and composed, Then the accent sits on that node in a hue no kind uses | Pending | Unmet | - |
| AC-002 | REQ-002 | Given an architecture or ER model, When it is composed, Then no edge runs along a zone border and no two edges share a stub or corridor | Pending | Unmet | - |
| AC-003 | REQ-003 | Given a Flow delivery, When the reply is read, Then the HVR self-scan is its last line | Pending | Unmet | - |
| AC-004 | REQ-004 | Given the rerun, When the failed scenarios are graded, Then Composition scores 2 on every scored board | Pending | Unmet | - |

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

The fixes have not landed.
<!-- /ANCHOR:closure -->

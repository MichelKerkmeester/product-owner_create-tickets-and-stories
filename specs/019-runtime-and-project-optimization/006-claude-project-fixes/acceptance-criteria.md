---
title: "Acceptance Criteria: Phase 6: Claude Project review fixes and user guide"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "claude project fixes acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/019-runtime-and-project-optimization/006-claude-project-fixes"
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
# Acceptance Criteria: Phase 6: Claude Project review fixes and user guide

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/019-runtime-and-project-optimization/006-claude-project-fixes
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
| AC-001 | REQ-001 | Given USER-GUIDE.md, When a Claude Desktop user follows it, Then each step names where to click and what to see | USER-GUIDE.md written with steps, expected replies and troubleshooting, linked from both READMEs, implementation-summary.md:55 | Met | - |
| AC-002 | REQ-002 | Given the kernel and its mirror, When the private doc recipe is read, Then it is two calls with name and parent | Kernel Section 9 now two calls with name and parent, residency passes, implementation-summary.md:56 and implementation-summary.md:108 | Met | - |
| AC-003 | REQ-003 | Given a just do it request, When the router runs, Then it selects Quick in every copy | QUICK with the phrase and STANDARD without, differential 220/220, implementation-summary.md:105 and implementation-summary.md:106 | Met | - |
| AC-004 | REQ-004 | Given each P2, When the phase closes, Then it is fixed or recorded with a reason | Every P2 fixed or recorded with its reason, gates pass, implementation-summary.md:107 | Met | - |

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

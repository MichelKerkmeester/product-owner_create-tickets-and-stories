---
title: "Acceptance Criteria: Phase 5: flow-mode"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "flow mode acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "scaffold/005-flow-mode"
    last_updated_at: "2026-10-20T02:35:20Z"
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
# Acceptance Criteria: Phase 5: flow-mode

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/005-flow-mode
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
| AC-001 | REQ-001 | Given the phase work is done, When the check runs, Then the pre-write check fails a four-exit decision, an unlabelled decision exit, an unknown shape and a 10-node diagram, and passes the Change Location model | flow_check.py --self-test 8 of 8 on 2026-10-20: a four-exit decision, an unlabelled exit, an unknown shape and a 10-node diagram each fail, and the Change Location model passes (implementation-summary.md, Verification) | Met | - |
| AC-002 | REQ-002 | Given the phase work is done, When the check runs, Then router fixtures pass for the Flow command and for "make a FigJam flow from these screenshots" | Router fixtures 123/123 on 2026-10-20, with `$flow the location change from these screenshots` and `make a FigJam flow from these screenshots` both routed to FLOW (benchmark/router/fixtures.json) | Met | - |
| AC-003 | REQ-003 | Given the phase work is done, When the check runs, Then one board built from the 7 Change Location screenshots lands in a scratch FigJam file, with read-back counts equal to the model and every decision exit labelled | Blocked: the hosted Figma MCP is not connected, so no board exists to read back | Unmet | - |
| AC-004 | REQ-004 | Given the phase work is done, When the check runs, Then the Flow Mode reply carries the board URL, a read-back line and the HVR self-scan line, and find export/ shows no new file | Blocked: the reply contract is written in flow-mode.md Section 6, but no board reply has been observed | Unmet | - |
| AC-005 | REQ-004 | Given the phase work is done, When the check runs, Then git status shows no HTML, SVG, PNG or Mermaid file created | git status on 2026-10-20 lists 0 HTML, SVG, PNG or Mermaid files outside the spec tree | Met | - |

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

AC-001, AC-002 and AC-005 were met by observed runs on 2026-10-20. AC-003 and AC-004 need a real board, which waits on the hosted Figma MCP and a scratch FigJam file the operator names.
<!-- /ANCHOR:closure -->

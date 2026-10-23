---
title: "Acceptance Criteria: Phase 7: project-mirror"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "project mirror acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "scaffold/007-project-mirror"
    last_updated_at: "2026-10-20T02:35:22Z"
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
# Acceptance Criteria: Phase 7: project-mirror

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/007-project-mirror
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
| AC-001 | REQ-001 | Given the phase work is done, When the check runs, Then run_parity.sh, run_receipts.sh, run_residency.sh and run_gates.sh each exit 0 | Scratch clone 2026-10-20: run_parity.sh exit 0 (39/39), run_residency.sh exit 0, run_gates.sh exit 0 (10 of 10). run_receipts.sh exit 1: SYNC.md carries no dated upload receipt | Unmet | - |
| AC-002 | REQ-002 | Given the phase work is done, When the check runs, Then validate-output-format.cjs --system product-owner passes | validate-output-format.cjs --system product-owner exit 0, 44 source files, 2026-10-20 | Met | - |
| AC-003 | REQ-003 | Given the phase work is done, When the check runs, Then a deliberate rule-span drift makes the parity gate fail | A planted "at most 4 exits" in the Flow Mode mirror made rule_parity.py, gate 3 of run_gates.sh, exit 1 naming the phrase; validate_parity.py alone passed it, so the Flow rule was added to rule parity | Met | - |
| AC-004 | REQ-003 | Given the phase work is done, When the check runs, Then the kernel names the Flow command and states the connector-conditional write or refusal | Kernel v1.2.2 Section 4 names `$flow` and `$figjam`, and Section 9 Flow Mode Delivery states the write with a connector and the refusal without one | Met | - |
| AC-005 | REQ-003 | Given the phase work is done, When the check runs, Then no review sentence is added to SYNC.md until the named human confirms the review | SYNC.md gained one maintenance record that says it is not a review and that the operator's review of v1.2.2 is pending | Met | - |

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

AC-002 to AC-005 were met by observed runs on 2026-10-20. AC-001 waits on run_receipts.sh, which needs the operator's upload and its receipt.
<!-- /ANCHOR:closure -->

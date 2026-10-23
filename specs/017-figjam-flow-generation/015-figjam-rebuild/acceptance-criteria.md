---
title: "Acceptance Criteria: Phase 15: figjam-rebuild"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "figjam rebuild acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/015-figjam-rebuild"
    last_updated_at: "2026-10-20T20:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met every criterion"
    next_safe_action: "Commit on the operator's go-ahead"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 15: figjam-rebuild

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/015-figjam-rebuild
**Level:** 2
**Status:** Complete
**Date:** 2026-10-20
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the seven types, When the packet is listed, Then each has a reference, a template past the user flow and an example that passes the check | 7 files in `references/types/`, 6 in `assets/templates/`, 7 in `assets/examples/`, each example printing `PASSED 1 diagram(s)` with exit 0 | Met | - |
| AC-002 | REQ-002 | Given the check, When its self-test runs, Then every planted defect fails and every shipped model passes | `148 of 148 self-test checks passed` in the repository and `134 of 134` inside the built plugin | Met | - |
| AC-003 | REQ-003 | Given the final tree, When every gate runs, Then each passes | parent-skill-check 0 failures 0 warnings. validate_skill_package --strict exit 0 on the root and four packets. run_gates.sh all 12 gates pass. Format gate exit 0 on four systems, reference parity identical. Packet playbook 45 scenarios 0 violations, packet topology 9 of 9, Product Owner playbook 48 scenarios 0 violations, hub topology 7 of 7. Plugin built 368 files and `claude plugin validate` passed | Met | - |
| AC-004 | REQ-004 | Given the Project mirror, When the Sync Loop gates run in a scratch clone, Then parity and residency pass | run_parity.sh 62 of 62, run_residency.sh pass. run_receipts.sh fails only on the missing upload receipt | Met | - |
| AC-005 | REQ-005 | Given a FigJam sequence, ER or gantt request, When the hub and the kernel router read it, Then both pick Flow | check_hub.py 33 gold rows pass, router fixtures 125 of 125 and differential 204 of 204 | Met | - |
| AC-006 | REQ-006 | Given a pie block or a mindmap request, When the check or the workflow reads it, Then it is refused with the nearest drawable type | A pie block exits 1 naming `references/flow-mode.md` Section 3, and that section lists every undrawable kind with its nearest type | Met | - |

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

The check carried the phase: every reference, template and example was written against rules a script enforces, so the docs and the check cannot drift apart unseen. Live board writes stay with phase 002, which waits for the hosted Figma MCP.
<!-- /ANCHOR:closure -->

---
title: "Acceptance Criteria: Phase 10: flow-mode-hardening"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "flow mode hardening acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/010-flow-mode-hardening"
    last_updated_at: "2026-10-20T09:38:56Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the acceptance criteria for this packet"
    next_safe_action: "Meet, waive or supersede the open criteria"
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
# Acceptance Criteria: Phase 10: Flow Mode hardening

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/010-flow-mode-hardening
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
| AC-001 | REQ-001 | Given the four Flow files and the kernel, When they are searched for page, Then no write targets or clears a page | grep -i page on the four files and the kernel's Flow Mode Delivery section, 2026-10-20: only pattern labels and lines that say a page is never the target | Met | - |
| AC-002 | REQ-002 | Given the check, When its self-test runs, Then every planted model fails and the good model passes | flow_check.py --self-test: 35 of 35 PASS, each planted model matched to its own message, both template files included | Met | - |
| AC-003 | REQ-003 | Given the shipped patterns and the real model, When the check runs, Then both pass | flow_check.py: flow-templates.md PASSED 6 diagrams, change-location-flow-model.md PASSED 1 | Met | - |
| AC-004 | REQ-004 | Given the final tree, When the gates run, Then each passes | run_gates.sh all 10 gates pass with rule_parity.py at 8 rules, format gate 44 files on both copies, playbook validator 48 scenarios and 0 violations, scratch clone run_parity.sh 39/39 and run_residency.sh pass | Met | - |
| AC-005 | REQ-005 | Given the kernel change, When SYNC.md is read, Then it carries a maintenance record that is not a review | SYNC.md line 73 ends "This is a maintenance record, not a review." | Met | - |

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

Every criterion is met by an observed run. A live board write stays with phase 002, because it needs the hosted Figma MCP.
<!-- /ANCHOR:closure -->

---
title: "Acceptance Criteria: Phase 14: hub-to-root"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "hub to root acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/014-hub-to-root"
    last_updated_at: "2026-10-20T18:30:00Z"
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
# Acceptance Criteria: Phase 14: hub-to-root

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/014-hub-to-root
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
| AC-001 | REQ-001 | Given the hub at the repository root, When parent-skill-check.cjs runs on it, Then it reports no failure and no warning | parent-skill-check.cjs on the absolute root path: 0 failures, 0 warnings | Met | - |
| AC-002 | REQ-002 | Given the root and its packets, When validate_skill_package.py --strict runs on each, Then each passes | Exit 0 on the root, sk-product-owner, sk-create-figjam, mcp-click-up and mcp-figma | Met | - |
| AC-003 | REQ-003 | Given the final tree, When every gate runs, Then each passes | run_gates.sh all 12 gates pass. differential.py 201 of 201. Format gate exit 0 on four systems, reference parity identical. Playbook 48 scenarios 0 violations, hub playbook 6 rows 0 violations. Plugin built 291 files with AGENTS.md and `claude plugin validate` passed. Scratch clone: run_parity.sh 39 of 39, run_residency.sh pass, residency_report.py exit 0 | Met | - |
| AC-004 | REQ-004 | Given the repository, When it is searched for the old folder, Then only specs and the dated SYNC.md record name it | Grep for a bare `product-owner/` prefix outside specs, the exports and the vendored copies finds the dated SYNC.md record and temporary sandbox paths inside old benchmark reports only | Met | - |

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

The two skilled checkers passing on the repository root carried the phase. The Claude Project mirror was left unchanged, since the move touches no Project-facing behavior.
<!-- /ANCHOR:closure -->

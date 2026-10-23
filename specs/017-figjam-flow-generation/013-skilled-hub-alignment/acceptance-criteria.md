---
title: "Acceptance Criteria: Phase 13: skilled-hub-alignment"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "skilled hub alignment acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/013-skilled-hub-alignment"
    last_updated_at: "2026-10-20T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met every criterion with an observed run"
    next_safe_action: "Commit both repositories on the operator's go-ahead"
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
# Acceptance Criteria: Phase 13: Skilled hub alignment

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/013-skilled-hub-alignment
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
| AC-001 | REQ-001 | Given the hub in `product-owner/`, When parent-skill-check.cjs runs on it, Then it reports no failure and no warning | parent-skill-check.cjs on the absolute hub path: "all hard invariants passed, 0 warnings", exit 0. Baseline was 39 failures | Met | - |
| AC-002 | REQ-002 | Given the hub and its packets, When validate_skill_package.py --strict runs on each, Then each passes | Exit 0 and PASS on product-owner/, sk-product-owner, sk-create-figjam, mcp-click-up and mcp-figma | Met | - |
| AC-003 | REQ-003 | Given the new schema, When the hub gold rows, router fixtures and differential rows replay, Then each routes as before | check_hub.py 24 gold rows pass, self-test 11 of 11. differential.py 201 of 201, 61 routing.md triggers. Router fixtures ok in run_gates.sh | Met | - |
| AC-004 | REQ-004 | Given the final tree, When every gate runs, Then each passes | run_gates.sh all 12 gates pass. Format gate exit 0 on four systems. Reference parity identical. Playbook 48 scenarios 0 violations, hub playbook 6 rows 0 violations. Plugin built 291 files and `claude plugin validate` passed. Scratch clone: run_parity.sh 39 of 39, run_residency.sh pass, residency_report.py exit 0 | Met | - |
| AC-005 | REQ-005 | Given the repository, When it is searched for retired paths, Then no packet holds a router or identity file and no doc names one | No ROUTER.md, graph-metadata.json or leaf-manifest file under any packet. Grep outside specs finds only the dated SYNC.md record. Link check finds no broken link outside the vendored copy and the doc example's sample links | Met | - |
| AC-006 | REQ-004 | Given a copy with no shared folders beside it, When run_gates.sh runs, Then the shared gates skip with a reason and the rest pass | Standalone copy: 8 of 12 gates pass, 4 skipped, exit 0 | Met | - |

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

Every criterion is met by an observed run. The hub sits in `product-owner/` on the operator's choice of 2026-10-20 and passes the skilled checker and validator with no exemption. `run_receipts.sh` still fails on the missing upload receipt, which is the operator's upload step and not this phase's.
<!-- /ANCHOR:closure -->

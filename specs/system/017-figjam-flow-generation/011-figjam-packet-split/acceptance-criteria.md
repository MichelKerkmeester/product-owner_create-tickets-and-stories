---
title: "Acceptance Criteria: Phase 11: figjam-packet-split"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "figjam packet split acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/011-figjam-packet-split"
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
# Acceptance Criteria: Phase 11: FigJam packet split

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/011-figjam-packet-split
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
| AC-001 | REQ-001 | Given the move, When the repository outside specs/ is searched for the old Flow paths, Then none remains | grep for sk-product-owner/references/flow-mode, sk-product-owner/assets/flow-templates and sk-product-owner/scripts, 2026-10-20: no hit outside specs/. The lane strings in router-contract.md and route_contract.py stay by decision D4 | Met | - |
| AC-002 | REQ-002 | Given the hub, When check_hub.py runs, Then the Flow gold rows route to sk-create-figjam and the self-test fails each planted defect | check_hub.py: PASSED the hub, 4 registry packets and 24 gold rows. --self-test: 11 of 11 PASS, among them a Flow command missing from packetCommands, a router without its loading section and a workflow packet registered as a tool | Met | - |
| AC-003 | REQ-003 | Given a Flow route in the Product Owner router, When it resolves, Then it hands off to the packet | ROUTER.md $flow row and CONDITIONAL row name the handoff, fixtures 123 of 123 with the three Flow rows loading no Flow file from sk-product-owner, differential 201 of 201 with kernel copy parity | Met | - |
| AC-004 | REQ-004 | Given the final tree, When the gates run, Then each passes | run_gates.sh all 10 gates pass, format gate 47 source files, shared validator exit 0 on four systems, reference parity byte-identical, playbook 48 scenarios 0 violations, scratch clone run_parity.sh 39/39 with 40 sources and run_residency.sh pass, a planted unmirrored packet file fails parity | Met | - |
| AC-005 | REQ-005 | Given the move, When SYNC.md and the plugin are read, Then SYNC.md carries a maintenance record and the plugin ships the packet | SYNC.md record ends "This is a maintenance record, not a review." build-plugin.py BUILT 292 files including sk-create-figjam, self-test 7 of 7, claude plugin validate passed | Met | - |

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

Every criterion is met by an observed run. The kernel is unchanged, so nothing new waits on a Project upload.
<!-- /ANCHOR:closure -->

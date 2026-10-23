---
title: "Acceptance Criteria: Phase 3: vendored-figma-and-sync"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "vendored figma and sync acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "scaffold/003-vendored-figma-and-sync"
    last_updated_at: "2026-10-20T02:35:18Z"
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
# Acceptance Criteria: Phase 3: vendored-figma-and-sync

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/003-vendored-figma-and-sync
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
| AC-001 | REQ-001 | Given the phase work is done, When the check runs, Then sha256 of every file under mcp-figma/ equals upstream at the base commit in vendor.json | implementation-summary.md:95 (58 of 58 files match git show 293caa90 for the upstream path, 0 mismatches) | Met | - |
| AC-002 | REQ-002 | Given the phase work is done, When the check runs, Then vendor-sync.py status exits 0 right after pull, and exits 1 after a one-byte local edit while pull refuses | implementation-summary.md:99 (status exited 0 after pull; a one-byte edit gave local-ahead and exit 1 and pull refused (test and live run)) | Met | - |
| AC-003 | REQ-003 | Given the phase work is done, When the check runs, Then vendor-sync.py refuses a planted symlink | implementation-summary.md:96 (test_planted_symlink_is_refused: exit 2, symlink refused) | Met | - |
| AC-004 | REQ-004 | Given the phase work is done, When the check runs, Then vendor-sync.py push against a scratch upstream produces a diff that git diff --stat shows there | implementation-summary.md:96 (test_push_writes_a_diff_upstream: git diff --stat lists guide.md) | Met | - |
| AC-005 | REQ-004 | Given the phase work is done, When the check runs, Then run_gates.sh and run_parity.sh exit 0 with the vendored copy in place | implementation-summary.md:97 (run_gates.sh: all 7 gates pass, exit 0; run_parity.sh: PASSED 37/37, exit 0) | Met | - |

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

All five criteria were met by observed runs on 2026-10-20. The one real push to upstream is left to phase 008.
<!-- /ANCHOR:closure -->

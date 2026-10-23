---
title: "Acceptance Criteria: Phase 6: claude-code-plugin"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "claude code plugin acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "scaffold/006-claude-code-plugin"
    last_updated_at: "2026-10-20T02:35:21Z"
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
# Acceptance Criteria: Phase 6: claude-code-plugin

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/006-claude-code-plugin
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
| AC-001 | REQ-001 | Given the phase work is done, When the check runs, Then claude plugin validate exits 0 on the built plugin | claude plugin validate exits 0 on the built plugin | Unmet | - |
| AC-002 | REQ-002 | Given the phase work is done, When the check runs, Then two consecutive builds produce identical hash trees | Two consecutive builds produce identical hash trees | Unmet | - |
| AC-003 | REQ-003 | Given the phase work is done, When the check runs, Then a planted divergence and a planted symlink each make the build fail | A planted divergence and a planted symlink each make the build fail | Unmet | - |
| AC-004 | REQ-003 | Given the phase work is done, When the check runs, Then a claude --plugin-dir session lists the Product Owner skill and routes the Flow command to Flow Mode | A claude --plugin-dir session lists the Product Owner skill and routes the Flow command to Flow Mode | Unmet | - |
| AC-005 | REQ-003 | Given the phase work is done, When the check runs, Then the built plugin has no bin/ folder and no mcpServers entry | The built plugin has no bin/ folder and no mcpServers entry | Unmet | - |

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

Not closed yet. Write this when the packet closes.
<!-- /ANCHOR:closure -->

---
title: "Acceptance Criteria: Phase 12: vendored-clickup"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "vendored clickup acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/012-vendored-clickup"
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
# Acceptance Criteria: Phase 12: Vendored ClickUp packet

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/012-vendored-clickup
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
| AC-001 | REQ-001 | Given the copy, When it is compared with upstream, Then it matches byte for byte and holds no symlink | vendor-sync.py pull: 178 files at 325ebb22. diff -rq against upstream printed nothing. find -type l: 0 | Met | - |
| AC-002 | REQ-002 | Given vendor.json, When status runs, Then every package is in step | vendor-sync.py status: mcp-figma 58 files, mcp-click-up 178 files and mermaid-extract 1 file in step, exit 0 | Met | - |
| AC-003 | REQ-003 | Given the hub, When the ClickUp gold rows replay, Then each routes as the rules state | check_hub.py 24 gold rows pass, among them cupt list my open tasks to mcp-click-up, search the clickup mcp to mcp-click-up, a bare clickup mention to product-owner and a doc request naming cupt to product-owner | Met | - |
| AC-004 | REQ-004 | Given the final tree, When run_gates.sh and the hub self-test run, Then both pass | run_gates.sh all 10 gates pass. check_hub.py --self-test 11 of 11 | Met | - |
| AC-005 | REQ-005 | Given the plugin and the docs, When they are read, Then the plugin ships the packet and the hub counts four packets | build-plugin.py ships mcp-click-up among 292 files. Hub SKILL.md names four packets, README tree lists mcp-click-up | Met | - |

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

Every criterion is met by an observed run. Product Owner's ClickUp parameters now follow the vendored contract, on the operator's ruling of 2026-10-20.
<!-- /ANCHOR:closure -->

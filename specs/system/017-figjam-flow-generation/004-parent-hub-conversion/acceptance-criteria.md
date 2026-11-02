---
title: "Acceptance Criteria: Phase 4: parent-hub-conversion"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "parent hub conversion acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "scaffold/004-parent-hub-conversion"
    last_updated_at: "2026-10-20T02:35:19Z"
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
# Acceptance Criteria: Phase 4: parent-hub-conversion

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/004-parent-hub-conversion
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
| AC-001 | REQ-001 | Given the phase work is done, When the check runs, Then router and format fixtures pass with the same counts as the baseline captured before the change | implementation-summary.md:97, implementation-summary.md:98 (router 117/117 and 189/189, format 59 cases plus 155 on each other system, equal to the baseline) | Met | - |
| AC-002 | REQ-002 | Given the phase work is done, When the check runs, Then the hub check passes, and fails on each of three planted defects: an unregistered packet folder, a wrong default and a missing router pointer | implementation-summary.md:99 (check passes; unregistered folder, wrong defaultMode and missing pointer each fail with their own message, plus two vendored-exemption defects) | Met | - |
| AC-003 | REQ-003 | Given the phase work is done, When the check runs, Then gold rows pass for a bare request, the existing figma Task fixture, a figma-ds-cli-only request and a negated Figma mention | implementation-summary.md:99 (11 gold rows pass, among them the bare request, the fixtures.json figma Task row, `figma-ds-cli fj nodes` and three negated mentions) | Met | - |
| AC-004 | REQ-004 | Given the phase work is done, When the check runs, Then the default Task request's token count, measured with one tokenizer before and after, rises by no more than the hub SKILL.md plus 286 tokens of hub overhead (operator amendment, 2026-10-20) | implementation-summary.md:100 (o200k rise 1,327 against 1,049 + 286 = 1,335) | Met | - |
| AC-005 | REQ-004 | Given the phase work is done, When the check runs, Then a fresh reviewer has read the diff and its findings are recorded in this phase's log | implementation-summary.md:105 (fresh Sonnet review: no P0, three P1 and the P2 set fixed, recorded in goal.md) | Met | - |

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

All five criteria were met by observed runs on 2026-10-20. AC-004 is held to the allowance the operator amended that day.
<!-- /ANCHOR:closure -->

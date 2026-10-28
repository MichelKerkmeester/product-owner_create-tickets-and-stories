---
title: "Acceptance Criteria: Phase 49: FigJam reading order and reply lead"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam reading order and reply lead acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 49: FigJam reading order and reply lead

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/049-figjam-reading-order-and-reply-lead
**Level:** 2
**Status:** In Progress
**Date:** 2026-10-28
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | Not yet run | Unmet | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then parity, residency and divergence pass | Not yet run | Unmet | - |
| AC-003 | REQ-003 | Given a flow, When the check prints its `Glance:` line, Then the accent comes first and the rest follow column by column | Not yet run | Unmet | - |
| AC-004 | REQ-004 | Given a delivery, When its reply is read, Then its first characters are the board URL, and the harness flags one that is not | Not yet run | Unmet | - |
| AC-005 | REQ-005 | Given FJ-023, When it runs, Then turn 1 is the intake round and a handoff queue is drawn as a label | Not yet run | Unmet | - |
| AC-006 | REQ-006 | Given the shipped examples, When a request names no reader, Then the example shows an intake round | Not yet run | Unmet | - |
| AC-007 | REQ-007 | Given a diamond label FigJam strands, When the check reads it, Then it prints a `leaves` line | Not yet run | Unmet | - |
| AC-008 | REQ-008 | Given an unstated dial, When the turn 1 rule counts assumed rows, Then the dial does not count | Not yet run | Unmet | - |
| AC-009 | REQ-009 | Given two reader notes, When the Composition script runs, Then it reproduces the corrected 047 and 048 scores | Not yet run | Unmet | - |
| AC-010 | REQ-010 | Given v1.0.15.0, When the release files are read, Then they name 1.0.15.0, the kernel H1 reads v1.2.15 and the mirror carries every change | Not yet run | Unmet | - |
| AC-011 | REQ-011 | Given v1.0.15.0, When FJ-022 and FJ-023 are rerun and graded, Then each has a recorded verdict, section 8.15 states the result and the gallery takes each passing board | Not yet run | Unmet | - |

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

Every criterion is Unmet. The fixes, the release and the rerun come next.
<!-- /ANCHOR:closure -->

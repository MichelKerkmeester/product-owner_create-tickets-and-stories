---
title: "Acceptance Criteria: Phase 48: FigJam neighbour and closing fixes"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam neighbour and closing fixes acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 48: FigJam neighbour and closing fixes

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/048-figjam-neighbour-and-closing-fixes
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
| AC-003 | REQ-003 | Given a decision joined to the accent on its row, When the check reads it, Then the `Glance:` line puts it right after the accent unless a node stands between | Not yet run | Unmet | - |
| AC-004 | REQ-004 | Given an intake round, When it ends, Then its last line is one closing question after its last block | Not yet run | Unmet | - |
| AC-005 | REQ-005 | Given FJ-017, When its stickies land where their `Sides:` lines named, Then no `Finding:` line is asked for | Not yet run | Unmet | - |
| AC-006 | REQ-006 | Given a 26-character decision, When the trace draws it, Then the diamond is 336 px wide and its text box reads 160 px | Not yet run | Unmet | - |
| AC-007 | REQ-007 | Given a playback, When it is scored, Then it names the three dials and the gate need not | Not yet run | Unmet | - |
| AC-008 | REQ-008 | Given a swapped pair, When Composition is scored, Then only the part read early costs the point | Not yet run | Unmet | - |
| AC-009 | REQ-009 | Given unsettled sources under Standard energy, When turn 1 runs, Then it is an intake round with no model or check before the playback's answer | Not yet run | Unmet | - |
| AC-010 | REQ-010 | Given v1.0.14.0, When the release files are read, Then they name 1.0.14.0 with changelogs and the mirror carries every change | Not yet run | Unmet | - |
| AC-011 | REQ-011 | Given v1.0.14.0, When FJ-017, FJ-022, FJ-023 and FJ-036 are rerun and graded, Then each has a recorded verdict, section 8.14 states the result and the gallery takes each passing board | Not yet run | Unmet | - |

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

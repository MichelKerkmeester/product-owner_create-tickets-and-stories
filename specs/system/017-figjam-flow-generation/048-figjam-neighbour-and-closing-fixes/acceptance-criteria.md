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
**Status:** Complete
**Date:** 2026-10-28
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | On the release tree e0a082d5 the self-tests, the design check, pytest and the gates pass, see tasks T013 | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then parity, residency and divergence pass | Parity PASSED 65 of 65, residency PASSED 7 systems and divergence PASSED 208 pairs after outer commit 8bc6d1014 | Met | - |
| AC-003 | REQ-003 | Given a decision joined to the accent on its row, When the check reads it, Then the `Glance:` line puts it right after the accent unless a node stands between | The cases "a decision beside the accent on its row reads right after it" and "a decision joined to the accent with a node between them on the row keeps its column place" pass in `flow_check.py`, and rubric Section 3 states the exception | Met | - |
| AC-004 | REQ-004 | Given an intake round, When it ends, Then its last line is one closing question after its last block | Flow templates Section 5, flow-mode Section 8, playbook Section 5 and the kernel state the closing question, and every intake round of the 048 rerun ended on it | Met | - |
| AC-005 | REQ-005 | Given FJ-017, When its stickies land where their `Sides:` lines named, Then no `Finding:` line is asked for | `hybrid-extension-written.md` 1.0.7.0 asks for the Finding only for a moved sticky, and the 048 FJ-017 run passed with none owed | Met | - |
| AC-006 | REQ-006 | Given a 26-character decision, When the trace draws it, Then the diamond is 336 px wide and its text box reads 160 px | `compose_board.py` holds a 26-character decision to 336 by 216 and `_text_width` reads a diamond at half its width less 8 px | Met | - |
| AC-007 | REQ-007 | Given a playback, When it is scored, Then it names the three dials and the gate need not | Flow-mode Section 4 and the playback sentence name the dials, playbook Section 5 checks them and all four 048 playbacks named them | Met | - |
| AC-008 | REQ-008 | Given a swapped pair, When Composition is scored, Then only the part read early costs the point | The playbook Composition row carries the levels and the swapped-pair sentence | Met | - |
| AC-009 | REQ-009 | Given unsettled sources under Standard energy, When turn 1 runs, Then it is an intake round with no model or check before the playback's answer | Playbook Section 5 states the turn 1 rule, FJ-022 scripts its intake turn and the 048 FJ-022 and FJ-036 streams show no model before the playback's answer | Met | - |
| AC-010 | REQ-010 | Given v1.0.14.0, When the release files are read, Then they name 1.0.14.0 with changelogs and the mirror carries every change | The hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.14.0, both changelogs exist and the kernel H1 reads v1.2.14 | Met | - |
| AC-011 | REQ-011 | Given v1.0.14.0, When FJ-017, FJ-022, FJ-023 and FJ-036 are rerun and graded, Then each has a recorded verdict, section 8.14 states the result and the gallery takes each passing board | `grades/sonnet-high-048.jsonl` holds a verdict for each, section 8.14 records 2 of 4 and the gallery took FJ-023's board | Met | - |

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

Every criterion is Met. SC-003 in `spec.md` is a success measure, not a criterion here, and the rerun passed 2 of 4, so it is recorded as not met and phase 049 takes the causes.
<!-- /ANCHOR:closure -->

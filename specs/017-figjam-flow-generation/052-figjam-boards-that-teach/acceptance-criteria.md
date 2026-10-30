---
title: "Acceptance Criteria: Phase 52: FigJam boards that teach the reader something"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam boards that teach acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 52: FigJam boards that teach the reader something

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/052-figjam-boards-that-teach
**Level:** 2
**Status:** Draft
**Date:** 2026-10-30
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given a zoned flow with `%% about:` lines, When it is checked and composed, Then it passes and each zone shows its notes, and the same flow at Balanced without them is refused | Fixtures and a scratch board | Unmet | - |
| AC-002 | REQ-002 | Given a body on a user flow, a process, an architecture and a state step, When each is checked at Balanced, Faithful and Simplified, Then the first two pass within their line limits and Simplified refuses | Fixtures | Unmet | - |
| AC-003 | REQ-003 | Given a flow with a style accent and no `%% focus: ... because ...`, When it is checked, Then it is refused | Fixture | Unmet | - |
| AC-004 | REQ-004 | Given every committed file, When the scan runs, Then nothing is found | Scan | Unmet | - |
| AC-005 | REQ-005 | Given the committed tree, When the gates run, Then they pass | run_gates.sh and parity | Unmet | - |
| AC-006 | REQ-006 | Given a composed board, When its key is read, Then the key band is one row at most 104 pixels tall | Scratch board read-back | Unmet | - |
| AC-007 | REQ-007 | Given the playbook root and rubric, When read, Then Substance is defined and a board totals 24 and passes at 20 | The root and rubric | Unmet | - |
| AC-008 | REQ-008 | Given the ten runs, When their records are read, Then each names `glm-5-3-flash-max` and has two reader notes and a scorecard row | meta.json files and grades | Unmet | - |
| AC-009 | REQ-009 | Given each gallery image, When its caption is read, Then it names a run of this phase and its score | Both READMEs | Unmet | - |

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

Every criterion is Unmet.
<!-- /ANCHOR:closure -->

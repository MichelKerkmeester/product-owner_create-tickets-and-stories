---
title: "Acceptance Criteria: Phase 50: FigJam lessons from a hand-built spec board"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam spec board learnings acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 50: FigJam lessons from a hand-built spec board

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/050-figjam-spec-board-learnings
**Level:** 2
**Status:** In progress
**Date:** 2026-10-29
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | flow_check 227 of 227, compose_board 1302 of 1302, design check 0, pytest 18 passed, run_gates.sh 15 of 15. The output format gate fails only on sk-product-owner/SKILL.md:46, a line from before this packet | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then parity, residency and divergence pass | Not yet run | Unmet | - |
| AC-003 | REQ-003 | Given every changed file, When the anonymity scan runs on the local term list, Then it prints nothing | The scan on every added line matches only the generic word deal in this packet's own spec text, and no line carries a board URL, file key or email | Met | - |
| AC-004 | REQ-004 | Given a write followed by a read-back, When the view still shows the board before the write, Then the read-back reports it stale and counts only a fresh view | flow-mode.md step 10 and Section 7, quality-rubric.md and hybrid-workflow.md Section 6 state the rule, FJ-048 tests it, and the scratch board was read back with node.screenshot() after its last write | Met | - |
| AC-005 | REQ-005 | Given every shipped example, When its subtitle line is read, Then it names where the flow starts and where it ends | Every shipped process, state, sequence, gantt and architecture subtitle names a start and an end. The ER example names what it covers, as the rule allows | Met | - |
| AC-006 | REQ-006 | Given a laned process with a status lane, When it is checked and composed, Then the status lane is drawn first with its line, dotted moves and key entry, and a broken status lane fails a self-test | The composer self-test draws the chevrons, the status line and the key entry, and 11 planted status cases fail with their named message | Met | - |
| AC-007 | REQ-007 | Given a node with a body at `Faithful`, When it is composed, Then its label sits on one line above a spacer and the body, and a body below `Faithful` or over its limits fails the check | The composer self-test sets label, spacer and body, and the planted below-Faithful, over-length and budget cases fail | Met | - |
| AC-008 | REQ-008 | Given the worked example, When it is composed on a scratch board and read back, Then the counts match its model and the view was rendered after the write | Scratch board: 15 of 15 nodes, 20 of 20 connectors, 0 warnings, read back from a fresh view after the card resize | Met | - |
| AC-009 | REQ-009 | Given the playbook, When its root is read, Then it lists one scenario each for the status lane, the detail cards and the fresh read-back | The root playbook lists FJ-046, FJ-047 and FJ-048 | Met | - |
| AC-010 | REQ-010 | Given the release, When the version files are read, Then the hub reads 1.0.17.0, `sk-create-figjam` reads 1.0.16.0 and the mirror and SYNC note carry every change | The hub files read 1.0.17.0, sk-create-figjam reads 1.0.16.0, 13 knowledge files changed and one added, and SYNC.md holds the 2026-10-29 note | Met | - |

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

Nine of ten criteria are Met. AC-002 waits for the release commit, after which the flow-mode review record moves to that commit and the parity check runs again.
<!-- /ANCHOR:closure -->

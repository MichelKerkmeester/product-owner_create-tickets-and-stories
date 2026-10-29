---
title: "Acceptance Criteria: Phase 51: FigJam gallery rerun on v1.0.16.0"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam gallery rerun acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 51: FigJam gallery rerun on v1.0.16.0

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/051-figjam-gallery-rerun
**Level:** 2
**Status:** Complete
**Date:** 2026-10-29
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the ten runs, When each meta.json is read, Then its model is `claude:claude-sonnet-5-5:medium` | Each of the ten meta.json files names claude:claude-sonnet-5-5:medium | Met | - |
| AC-002 | REQ-002 | Given every committed file, When the scan runs, Then no board URL, file key, plan name or email is found | A scan of every changed path for the ten draft keys, board URLs, plan names, plan keys and emails prints nothing | Met | - |
| AC-003 | REQ-003 | Given the committed tree, When the gates run, Then 15 of 15 pass | run_gates.sh passes 15 of 15 after the vendor pull | Met | - |
| AC-004 | REQ-004 | Given each board, When its records are read, Then it has two reader notes and a scorecard row | Twenty reader notes in grades/sonnet-medium-051/readers and ten rows in grades/sonnet-medium-051.jsonl | Met | - |
| AC-005 | REQ-005 | Given each gallery image, When its caption is read, Then it names a graded run and that run scores at least as high as any other board of its type | The five swapped images score 22, 22, 20, 22 and 19 against 22, 21, 20, 22 and ungraded, and the five kept images beat their new boards | Met | - |
| AC-006 | REQ-006 | Given the playbook root, When it is read, Then it lists FJ-049 with a prompt, signals and pass criteria | Section 10 and wave 4 of the root playbook list FJ-049, whose file holds the prompt, signals, Q1 to Q3 and the PASS line | Met | - |

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

Every criterion is Met.
<!-- /ANCHOR:closure -->

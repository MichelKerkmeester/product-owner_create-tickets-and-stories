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
**Status:** Complete
**Date:** 2026-10-28
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | compose 1251/1251, design check exit 0, flow check 201/201, pytest 18, 15 of 15 gates and the format gate on PO 0000184 | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then parity, residency and divergence pass | `validate_parity.py product-owner` PASSED 65/65, `residency_check.py --all` and `pair_divergence.py --all` PASSED after outer 0001124 | Met | - |
| AC-003 | REQ-003 | Given a flow, When the check prints its `Glance:` line, Then the accent comes first and the rest follow column by column | self-test case on FJ-023's shape and both rerun `Glance:` lines read the accent then column by column | Met | - |
| AC-004 | REQ-004 | Given a delivery, When its reply is read, Then its first characters are the board URL, and the harness flags one that is not | both rerun replies open on the redacted URL and `lead_is_url` rejects a sentence before it | Met | - |
| AC-005 | REQ-005 | Given FJ-023, When it runs, Then turn 1 is the intake round and a handoff queue is drawn as a label | FJ-023 turn 1 is the intake round, and its board draws Claim queued as a line label with 8 of 8 nodes | Met | - |
| AC-006 | REQ-006 | Given the shipped examples, When a request names no reader, Then the example shows an intake round | the process and user flow examples show an intake round and the other three name their reader | Met | - |
| AC-007 | REQ-007 | Given a diamond label FigJam strands, When the check reads it, Then it prints a `leaves` line | self-tests flag `New price compared to old?` and `Drop-off point or courier?` with `leaves` | Met | - |
| AC-008 | REQ-008 | Given an unstated dial, When the turn 1 rule counts assumed rows, Then the dial does not count | flow-mode Section 2 and playbook Section 5 say the dials are not rows, and both rerun intake rounds ask them as their own question | Met | - |
| AC-009 | REQ-009 | Given two reader notes, When the Composition script runs, Then it reproduces the corrected 047 and 048 scores | six of six stored boards match the corrected records and `--self-test` passes 5 of 5 | Met | - |
| AC-010 | REQ-010 | Given v1.0.15.0, When the release files are read, Then they name 1.0.15.0, the kernel H1 reads v1.2.15 and the mirror carries every change | six version files at 1.0.15.0, kernel H1 v1.2.15, SYNC note and parity PASSED | Met | - |
| AC-011 | REQ-011 | Given v1.0.15.0, When FJ-022 and FJ-023 are rerun and graded, Then each has a recorded verdict, section 8.15 states the result and the gallery takes each passing board | `grades/sonnet-high-049.*` records both verdicts, README section 8.15 states 0 of 2 with both boards at 22 and the 22-point FJ-023 board is the process gallery image | Met | - |

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

Every criterion is Met. SC-003 asked for both scenarios to pass, and neither did: each fails one expected signal while its board scores 22 of 22. The operator ended testing at this rerun, so both failures stand as known limitations.
<!-- /ANCHOR:closure -->

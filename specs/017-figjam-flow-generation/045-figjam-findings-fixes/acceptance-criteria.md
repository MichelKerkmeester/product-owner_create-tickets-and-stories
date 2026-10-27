---
title: "Acceptance Criteria: Phase 45: FigJam findings fixes"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam composite and path order acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/045-figjam-findings-fixes"
    last_updated_at: "2026-10-27T14:20:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Write the composer brief and the sentence swaps"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 5
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 45: FigJam findings fixes

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/045-figjam-findings-fixes
**Level:** 2
**Status:** Complete
**Date:** 2026-10-27
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. A new row takes the highest AC-ID plus one.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | Composer self-test 1245 of 1245, design check exit 0, flow check 172 of 172, pytest 18, 15 of 15 gates and the output format gate passed | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass | Parity PASSED 65/65 and residency PASSED 7 after outer commit 0001095, with the flow-mode review recorded at the source commit | Met | - |
| AC-003 | REQ-003 | Given a state board, When its glance lines are planned, Then the skill and the Project plan it as drawn with the named state leading its line | `references/types/state.md` Section 5, the rubric's first-glance line, Flow Mode's gate step, the style guide, the state example and their mirrors plan the state board as drawn | Met | - |
| AC-004 | REQ-004 | Given a user flow or a process, When its glance lines are planned, Then the main row as drawn is the second glance and the nodes off it the last, and no source keeps "two decisions share a line" | The rubric and both flow examples plan the drawn main row second and the nodes off it last, in the skill and the mirror, and no live file keeps the old phrase | Met | - |
| AC-005 | REQ-005 | Given a noted node with every side taken, When the gate is written, Then it says so and offers the pin and legend form or a recompose, and the sticky's size is stated | `references/hybrid-workflow.md` Section 3 and its mirror carry the gate question, the 240 pixel size and the in-call probe | Met | - |
| AC-006 | REQ-006 | Given the intake rules and the board scenarios, When they are read, Then no source states the narrower rule or expects at most one round | Both Flow Mode intake sentences name the last round, and every board scenario allows the rounds a run opens | Met | - |
| AC-007 | REQ-007 | Given a revision and a read-back, When Flow Mode is read, Then the playback reads the board first, the revision read-back names the changed end and the connector-label read is stated | Flow Mode Sections 6, 7 and 8 and their mirror carry the read, the second-glance clause and the connector-label count | Met | - |
| AC-008 | REQ-008 | Given the playbook, When it is read, Then the Composition and Shared trunks rows carry the D7 conventions and FJ-031's delete signal names the write time | The playbook root rows carry the conventions, and FJ-031 names the write time in both its copies | Met | - |
| AC-009 | REQ-009 | Given v1.0.11.0, When the release files are read, Then they name 1.0.11.0 with changelogs and the kernel H1 matches its rules | The hub and `sk-create-figjam` read 1.0.11.0 with changelogs, and the kernel stays v1.2.11 with its reason in SYNC.md | Met | - |
| AC-010 | REQ-002 | Given every declared pair, When the rule-content divergence check reads both sides, Then no shared anchor states one rule two ways | `pair_divergence.py product-owner` printed PASSED, 65 declared pairs compared, after five mirror lines were brought in line | Met | - |

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

All ten rows are Met with observed evidence. No rerun tested the new rules, because the operator closed testing on 2026-10-27.
<!-- /ANCHOR:closure -->

---
title: "Acceptance Criteria: Phase 44: FigJam composite placement and path order"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam composite and path order acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/044-figjam-composite-and-path-order"
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
# Acceptance Criteria: Phase 44: FigJam composite placement and path order

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/044-figjam-composite-and-path-order
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
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | Composer self-test 1245 of 1245, design check exit 0, flow check 172 of 172, pytest 18 passed, 15 of 15 gates and the output format gate passed on the committed tree | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then both pass and the composer mirror equals `--template` | Parity PASSED 65/65 and residency PASSED 7 after outer commit 0001092, and the Composer Knowledge block equals `--template` at 47,600 bytes | Met | - |
| AC-003 | REQ-003 | Given a state model with a composite, When it is composed, Then the first state sits left of the composite even when a label line is declared first, and every existing model traces to the same geometry | The label-line self-test case passes, the 38-model trace moved only the two composite fixtures, and the FJ-026, FJ-032 and FJ-017 renders draw Confirmed right of Pending | Met | - |
| AC-004 | REQ-004 | Given the rubric, the playbook row and the Project, When they are read, Then each states the path-order glance rule | The path-order sentence reads in `references/quality-rubric.md`, its Knowledge file and playbook row 83 | Met | - |
| AC-005 | REQ-005 | Given a revision, When its Composition is graded, Then every main-row node planned last is exempt when it reads before the changed end | Playbook row 83 and the rubric's revision line exempt the entry, the decisions and the main row planned last, and FJ-031 scored Composition 2 under it | Met | - |
| AC-006 | REQ-006 | Given the launcher, When the fixture runs through its PATH, Then a `Label:` line prints | The pin held in a direct probe, but every run printed `Label: skipped` because the Bash tool rebuilds PATH from the shell profile. The operator chose a Homebrew node reinstall instead | Superseded | ADR-001 |
| AC-007 | REQ-007 | Given the 6 failures, When they rerun in fresh files, Then each has one graded line and every board a render and two readers | `grades/sonnet-high-044.jsonl` holds 6 lines, 10 renders sit in `renders/` and two reader notes per scored board sit in `grades/sonnet-high-044/readers/` | Met | - |
| AC-008 | REQ-008 | Given v1.0.10.0, When the release files are read, Then they name 1.0.10.0 with changelogs and the kernel H1 matches its rules | The hub, its three JSON files and `sk-create-figjam/SKILL.md` read 1.0.10.0 with both changelogs, and the kernel stays v1.2.11 since no kernel rule changed | Met | - |

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

Seven rows are Met with observed evidence and AC-006 is Superseded by ADR-001. The success criteria are not met: the rerun passed 2 of 6 against SC-001's 4, and FJ-026 misses SC-002. The operator closed testing on 2026-10-27 and sent the findings to the skills.
<!-- /ANCHOR:closure -->

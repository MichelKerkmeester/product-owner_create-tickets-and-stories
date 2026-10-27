---
title: "Acceptance Criteria: Phase 46: FigJam gate and accent fixes"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam gate and accent fixes acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/046-figjam-gate-and-accent-fixes"
    last_updated_at: "2026-10-27T22:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Review the diff and commit"
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
# Acceptance Criteria: Phase 46: FigJam gate and accent fixes

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/046-figjam-gate-and-accent-fixes
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
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | On the committed tree: composer 1250 of 1250, flow check 177 of 177, pytest 18, 15 of 15 gates and the output format gate passed | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then parity, residency and divergence pass | After outer commit f5d8f2360: parity PASSED 65 of 65, residency PASSED 7 systems, divergence PASSED 208 pairs | Met | - |
| AC-003 | REQ-003 | Given a model with a notes line, When the composer and the check read it, Then the key moves down, a missing node is refused and a `Sides:` line names each node's side, and FJ-017 and the hybrid workflow use it | Composer self-test 1250 of 1250 with the key-gap and missing-node cases, flow check 175 of 175 with the sides cases, and `references/hybrid-workflow.md` Section 3, its mirror and both FJ-017 copies state the gate's use | Met | - |
| AC-004 | REQ-004 | Given a user flow or a process, When its accent is chosen, Then it never sits on the goal and a goal line names the goal, in every rule and shipped model | The rubric, style guide, both flow types, Flow Mode and the templates say so in the skill and the mirror, and the nine re-accented models pass the check with their goal drawn as the goal | Met | - |
| AC-005 | REQ-005 | Given a stop, When its reply is read, Then it ends on its question with no self-scan line | Flow Mode's stop paragraph, its mirror, `AGENTS.md` and the playbook acceptance rules state it | Met | - |
| AC-006 | REQ-006 | Given a group the request names as one, When a board is scored, Then the order of its members is not scored | The playbook Composition row states it | Met | - |
| AC-007 | REQ-007 | Given the gate, When it is written, Then it shows the sketch with the check result and answers four named critique questions unless the user settled them | Flow Mode step 7 and the look bullet, the rubric Section 5 and their mirrors, and the playbook acceptance rules state it | Met | - |
| AC-008 | REQ-008 | Given a label FigJam wraps to one last word, When the trace reads it, Then it prints a `Label:` line | The flow check self-test's "Editor with welcome tip" case passes | Met | - |
| AC-009 | REQ-009 | Given v1.0.12.0, When the release files are read, Then they name 1.0.12.0 with changelogs and the kernel H1 matches its rules | The hub and `sk-create-figjam` read 1.0.12.0 with changelogs, and the kernel moves to v1.2.12 for its gate sentence, with the declared residency row resynced and the reason in SYNC.md | Met | - |
| AC-010 | REQ-010 | Given v1.0.12.0, When FJ-017, FJ-036, FJ-022 and FJ-023 are rerun and graded, Then each has a recorded verdict, section 8.12 states the result and the gallery takes each passing board | `grades/sonnet-high-046.jsonl` records four FAIL verdicts, run README section 8.12 states 0 of 4 and no board passed, so the gallery is unchanged | Met | - |

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

Every criterion is met. The rerun did not reach SC-003: 0 of 4 passed, and phase 047 takes every cause run README section 8.12 names.
<!-- /ANCHOR:closure -->

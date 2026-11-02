---
title: "Acceptance Criteria: Phase 47: FigJam glance and row fixes"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam glance and row fixes acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/047-figjam-glance-and-row-fixes"
    last_updated_at: "2026-10-27T23:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase with D1 to D9 implemented"
    next_safe_action: "Write the Project mirror and the v1.0.13.0 release"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 40
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.3 -->
# Acceptance Criteria: Phase 47: FigJam glance and row fixes

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 017-figjam-flow-generation/047-figjam-glance-and-row-fixes
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
| AC-001 | REQ-001 | Given the changed sources, When every gate runs, Then each exits 0 | On the committed tree at f0c0ba95 the self-tests, the design check, pytest and the gates pass, see tasks T015 | Met | - |
| AC-002 | REQ-002 | Given the last commit, When the Sync Loop checks run, Then parity, residency and divergence pass | Parity PASSED 65 of 65, residency PASSED 7 systems and divergence PASSED 208 pairs after outer commit 3fe1a442e | Met | - |
| AC-003 | REQ-003 | Given a user flow or a process, When the check reads it, Then a `Glance:` line prints the drawn reading order and the rubric and the playbook plan and score from it | The reading-order case passes in the flow check self-test, 186 of 186, the process example prints its `Glance:` line, rubric Section 3 plans from it with path order as the fallback and the playbook Composition row scores against it | Met | - |
| AC-004 | REQ-004 | Given a main-row line that bends off the row, When the check reads it, Then a non-failing `Row:` line names the node between and the zone move, and the composer is unchanged | Both row cases pass in the flow check self-test and `git diff` shows no change to `compose_board.py` or `assets/compose-board.js` | Met | - |
| AC-005 | REQ-005 | Given a noted node, When the sides check reads it, Then its `Sides:` line names the side and the alignment, no square past one sticky width is offered and the notes call places the sticky there | The sides case with an end dot 76 px and 276 px past the node passes, `STICKY_REACH` equals one sticky and hybrid-workflow Section 3 states the side and alignment | Met | - |
| AC-006 | REQ-006 | Given the gate, When it shows its sketch, Then the sketch is the checked model with every `%%` and `style` line and the `PASSED` line as printed | Flow-mode step 7, rubric Section 5, the kernel, all seven examples' Sketch line and playbook Section 5 state it, and the Flow Mode, rubric and seven example Knowledge files carry the same wording | Met | - |
| AC-007 | REQ-007 | Given a label wrap, When the check and the rules read it, Then `may leave` marks a one-measure strand, step 5 offers a reworded or longer label or naming at the gate, the Legibility row covers several wraps and every example's Check block matches the check | The lone `tip` case reads `may leave`, both relabelled examples pass with no `Label:` line and the Check block case passes for all seven examples | Met | - |
| AC-008 | REQ-008 | Given parts a reader names in one reading step, When Composition is scored, Then their order against each other costs no point | The playbook Composition row states it | Met | - |
| AC-009 | REQ-009 | Given a Flow run, When intake round One asks, Then it asks the three dials | Flow templates Section 5 round One and the flow-mode Section 4 distance paragraph state it | Met | - |
| AC-010 | REQ-010 | Given an intake round the scenario does not name, When it ends, Then text after its question misses the playback signal | Playbook Section 5 states it | Met | - |
| AC-011 | REQ-011 | Given a scenario run, When the harness redacts and logs it, Then only its own output is redacted, each run-log row is redacted and a counted read-back or a `use_figma` call reads as a delivery | `run_full.sh` names each scenario's own paths, `adaptive_compare.py` writes rows through `log_line` and classifies through `classify` and the three `redact_run.py` copies hash alike | Met | - |
| AC-012 | REQ-012 | Given v1.0.13.0, When the release files are read, Then they name 1.0.13.0 with changelogs and the kernel H1 reads v1.2.13 | The hub, its three JSON files and `sk-create-figjam/SKILL.md` read 1.0.13.0, both v1.0.13.0 changelogs exist and the kernel H1 reads v1.2.13 | Met | - |
| AC-013 | REQ-013 | Given v1.0.13.0, When FJ-017, FJ-022, FJ-023 and FJ-036 are rerun and graded, Then each has a recorded verdict, section 8.13 states the result and the gallery takes each passing board | `grades/sonnet-high-047.jsonl` holds a verdict for each, section 8.13 records 1 of 4 and the gallery took FJ-022's board | Met | - |

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

Every criterion is Met. SC-003 in `spec.md` is a success measure, not a criterion here, and the rerun passed 1 of 4, so it is recorded as not met and phase 048 takes the causes.
<!-- /ANCHOR:closure -->

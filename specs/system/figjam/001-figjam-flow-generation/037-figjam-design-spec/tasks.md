---
title: "Tasks: Phase 37: figjam-design-spec"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "figjam design spec tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 37: figjam-design-spec

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path)`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Write the spec folder and add row 37 to the parent phase table (spec.md)
- [x] T002 Record the baseline: self-test count, pytest count, gate results and the compact template's character count (43,623)
- [x] T003 List every literal colour, size and connector look in the composer by grep (sk-create-figjam/assets/compose-board.js)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Compact the constants and add the built-in design and `const THEME = __THEME__` merge (sk-create-figjam/assets/compose-board.js)
- [x] T005 Rank 4: write the design file with prose sections, the token block and the read-only swatch and tint reference (sk-create-figjam/assets/figjam-design.md)
- [x] T006 Rank 4: read the built-in design, resolve and validate the file, print `DESIGN` warnings, count them on the `COMPOSED` line, fill `__THEME__` and count it in the 50,000-character check (sk-create-figjam/scripts/compose_board.py)
- [x] T007 Rank 4: add `--design-check` with the resolved design, differing tokens, measured ratios, warnings and theme cost (sk-create-figjam/scripts/compose_board.py)
- [x] T008 Rank 1: take pink out of the zone tint cycle and add a self-test tint check (compose-board.js, compose_board.py)
- [x] T009 Rank 2: pick zone and gantt band tints that skip member hues and differ from the neighbouring zone (compose-board.js)
- [x] T010 Rank 3: draw participants white with the neutral stroke and name the gateway and in progress roles (compose-board.js, style-guide.md)
- [x] T011 Rank 5: sort key entries in a canonical order per type (compose-board.js)
- [x] T012 Rank 6: align zone tops for zones that share a row in group mode (compose-board.js)
- [x] T013 Rank 7: edge label, key and source text at 18 px and a `small` 14 px step for bar text and pins (compose-board.js)
- [x] T014 Rank 8: keep routes clear of the subtitle band and the board margin by growing the diagram's box to hold every route, in place of pricing the band in the router (compose-board.js)
- [x] T015 Rank 9: span the key across the diagram's width and wrap it (compose-board.js)
- [x] T016 Rank 10: define connector looks once and give sequence requests the default gray with a closed head (compose-board.js)
- [x] T017 Rank 11: smaller participant feet, step pins beside the sender's lifeline and row height from the label size (compose-board.js)
- [x] T018 Rank 12: give gantt planned bars the line gray stroke (compose-board.js)
- [x] T019 Rank 13: top-align ER cards that share a row (compose-board.js)
- [x] T020 Rank 14: wrap the subtitle balanced with no one-word last line (compose-board.js)
- [x] T021 Rank 17: add the `marker` role for sequence step pins (compose-board.js, figjam-design.md)
- [x] T022 Rank 18: measure gantt section names at the size they are drawn (compose-board.js)
- [x] T023 Stop counting the design file as a shipped model (sk-create-figjam/scripts/flow_check.py)
- [x] T024 Point the style guide at the design file (sk-create-figjam/references/style-guide.md)
- [x] T025 Rank 15: add the ninth rubric criterion with the total at 18, point the scorecard Signal at the design file and its tint cycle with the total at 22 and add a family scenario and a broken-design scenario (references/quality-rubric.md, manual-testing-playbook/)
- [x] T026 [P] Rank 16: cut colour prose in the seven type references to role names and a pointer (sk-create-figjam/references/types/)
- [x] T027 Write the design Knowledge file, add the `__THEME__` line to the composer Knowledge steps, update the type mirrors and add the kernel clause at v1.2.4 (claude project/)
- [x] T028 Add the new asset and Knowledge pair to the Sync Loop declaration (systems.py and systems.cjs in the Sync Loop folder)
- [x] T029 Regenerate the manifest and write the v1.0.3.0 changelogs with the version bumps (leaf-manifest.json, sk-create-figjam/changelog/, changelog/)
- [x] T030 Rank 18: recompose the gallery boards on the fictional test FigJam file and update the screenshots, including the gantt board (moved to phase 038 by ADR-010, which composes every type on three models)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T031 Run `compose_board.py --self-test`, `flow_check.py --self-test` and `python3 -m pytest -q scripts/tests` and compare with the baseline
- [x] T032 Run `bash benchmark/gates/run_gates.sh` with `VENDOR_UPSTREAM_ROOT` set to the scratch clone and read all 15 results
- [x] T033 Run the Sync Loop residency, parity, output format and reference parity gates in a scratch clone
- [x] T034 Run `--design-check` on the shipped file and on a broken copy and read the warnings
- [x] T035 Get a fresh Opus high review of the finished work and close every finding before any commit (15 findings fixed, a second review closed them and its four new findings were fixed)
- [x] T036 Run validate.sh --strict on this folder and the parent (RESULT: PASSED on both)
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
- **Decisions**: See `decision-record.md`
<!-- /ANCHOR:cross-refs -->

---

## Verification Checklist

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|----------|----------|-------------------|
| **[P0]** | HARD BLOCKER | Cannot claim done until complete |
| **[P1]** | Required | Must complete OR get user approval |
| **[P2]** | Optional | Can defer with documented reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-007 in spec.md, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md phases and the nine decision records]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: node for the trace, the upstream root for the vendor gate and a scratch clone for the Sync Loop gates]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The filled template stays under 50,000 characters with the theme counted [EVIDENCE: every shipped model fits one call in the self-test, and the design check leaves 3,447 characters]
- [x] CHK-011 [P1] No comment carries a phase number, rank number or spec path [EVIDENCE: a scan of the added code lines finds none, and the review confirmed it]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-006 and AC-008 Met, AC-007 Superseded by ADR-010]
- [x] CHK-021 [P1] The broken-design scenario prints named warnings and still draws the board [EVIDENCE: FJ-045's design replays to three named warnings, and the self-test composes under 23 planted broken designs]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets, board URLs, Figma file keys, plan names or Barter flows in any changed file [EVIDENCE: a key, URL and plan-name scan over every changed file finds none]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan, tasks and decision record synchronized [EVIDENCE: ADR-010 records the gallery move, and tasks and acceptance rows point at it]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: every changed path matches a row of the files table, which now names the design reader, the trace and the release files]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 5 | 5/5 |
| P1 Items | 5 | 5/5 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-25
<!-- /ANCHOR:summary -->

---
title: "Acceptance Criteria: Phase 37: figjam-design-spec"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam design spec acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 37: figjam-design-spec

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/037-figjam-design-spec
**Level:** 2
**Status:** Complete
**Date:** 2026-10-25
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the shipped `figjam-design.md`, When `compose_board.py --design-check` reads it, Then it finds one token block, no warning and no token that differs from the built-in design, so the theme is `{}` | `compose_board.py --design-check` on the shipped file: `THEME {}`, `0 design warnings`, exit 0, 3,447 characters left for the model | Met | - |
| AC-002 | REQ-002 | Given a copy of the design file with one bad token and one with a broken block, When a model is composed under each, Then the first falls back for that token alone and the second for the whole design, each prints named `DESIGN` lines, the `COMPOSED` line counts them and the filled code stays under 50,000 characters | A copy with `type.small` 10 falls back for that token alone, a broken block falls back whole, both compose the ER board at 48,229 characters with named `DESIGN` lines. FJ-045's three-way break replays to exactly three warnings. The self-test also proves a nested tint cycle, an unreadable text and Windows line endings | Met | - |
| AC-003 | REQ-003 | Given the composer, When the self-test runs, Then it checks that no zone tint is pink or a member hue, that neighbouring zones differ, that the swatch pairs match the design file and that each type's key follows its canonical order, and ranks 1 to 3, 5 to 14, 17 and 18 are the only behaviour | Self-test 1,015 of 1,015: tints checked against member hues and every zone beside them, swatch pairs against the design file, key order per type, plus 23 planted broken designs, the largest and smallest legal sizes and both font fallbacks | Met | - |
| AC-004 | REQ-004 | Given the final state, When the packet gates run, Then `compose_board.py --self-test`, `flow_check.py --self-test`, `python3 -m pytest -q scripts/tests` and all 15 benchmark gates pass | `run_gates.sh` with the upstream root: all 15 gates pass. Composer self-test 1,015 of 1,015, flow check 158 of 158, pytest 18 passed | Met | - |
| AC-005 | REQ-005 | Given the Project mirror and the Sync Loop declaration, When the residency, parity, output format and reference parity gates run in a scratch clone, Then all pass, the new Knowledge file mirrors the design file and the kernel reads v1.2.4 with the `__THEME__` clause | Scratch clone at the change set plus the review record: residency PASSED, parity 65 of 65, output format passed across 72 files, reference parity byte-identical. Kernel H1 v1.2.4, the Project design file carries the skill's json block and `{}`, both proved by the self-test | Met | - |
| AC-006 | REQ-006 | Given the references, When they are read, Then the rubric has nine criteria totalling 18, the scorecard Signal reads the design file with its total at 22, the two new scenarios exist, the type references name roles and point at the design file, `flow_check.py` skips the design file, `leaf-manifest.json` is current and both changelogs read v1.0.3.0 | Rubric 9 criteria for 18, scorecard Signal reads the design file at 22, FJ-044 and FJ-045 exist, the seven type references name roles, `flow_check.py` skips the design file, `leaf-manifest.json` passes the leaf map gate, both changelogs read v1.0.3.0 | Met | - |
| AC-007 | REQ-007 | Given the recomposed gallery and the finished diff, When the screenshots and the review are read, Then each changed screenshot shows what the composer now draws and a fresh Opus high review has no open finding | The gallery recompose moved to phase 038, which composes every type on three models and keeps the best board of each. The review half is AC-008 | Superseded | ADR-010 |
| AC-008 | REQ-007 | Given the finished diff and the fixes of the first review, When a second fresh Opus high review reads them, Then each of the first review's 15 findings is closed and no new finding is open | A second fresh Opus high review closed F1 to F15, each with a probe or a file and line. Its four new P2 findings and the F11 residual were fixed and replayed on its own probes (the stage-zone top, the tint fallback, the surrogate compose), and the self-test passes 1,015 of 1,015 | Met | - |

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

AC-001 to AC-006 and AC-008 are met with the evidence above, and AC-007 is superseded by ADR-010, which moves the gallery to phase 038.
<!-- /ANCHOR:closure -->

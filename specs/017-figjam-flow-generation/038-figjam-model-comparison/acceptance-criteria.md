---
title: "Acceptance Criteria: Phase 38: figjam-model-comparison"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam model comparison acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 38: figjam-model-comparison

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/038-figjam-model-comparison
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
| AC-001 | REQ-001 | Given the driver and the three models, When the batch finishes, Then each of the 21 runs has its replies, tool calls and `meta.json` in the run folder and ran alone on the fictional test file | 21 `meta.json` files with `completed: true` under `skill/`, every turn's `response_models` naming the model asked for, and `batch.log` showing one run at a time | Met | - |
| AC-002 | REQ-002 | Given every written board, When it is graded, Then it has an overview, a 100% and a greyscale render and a 22-point scorecard from a grader that is none of the three models, with Clarity from a fresh reader | 23 overview, 23 full and 23 greyscale renders, seven Sonnet 5.5 grader files in `grades/` and three reader answer files scored against `grades/reader-key.md` | Met | - |
| AC-003 | REQ-003 | Given the run folder and every changed file, When they are scanned, Then no board URL, Figma file key, plan name or email appears | The leak scan read 0 hits on each scenario commit, on `grades/` and `results.jsonl` and on every changed file, apart from the repository owner's name in the root README's existing badges | Met | - |
| AC-004 | REQ-004 | Given `results.jsonl`, When the gallery rule picks the best board per type, Then each of the seven type images is that board and its caption names the scenario, the model and the score | The seven images are the `gallery: true` rows of `results.jsonl`, and `assets/screenshots/README.md` names the scenario, the model and the score for each | Met | - |
| AC-005 | REQ-005 | Given the graded runs, When the run README is read, Then it says which model draws boards best per type and overall, with the losses that decided it | The run README's Verdict and Results sections, with the deciding losses per model and per type | Met | - |
| AC-006 | REQ-006 | Given a Flow Mode run that offers a delete, When the user answers with a bare yes or a gate's answer, Then no board is deleted until a reply names the boards | `references/flow-mode.md` Section 6 runs a delete only on a reply that names the boards or a yes to a question naming exactly them, and Sections 6 and 9 name the old board in the delete question, mirrored in Templates - Flow Mode | Met | - |
| AC-007 | REQ-007 | Given `use_figma` answers "Failed to connect to MCP server", When the model recovers, Then it checks the call for a `fileKey` and retries with the gate's key before it falls back | `references/flow-mode.md` Section 9 `use_figma` fails to connect, mirrored in Templates - Flow Mode | Met | - |
| AC-008 | REQ-008 | Given a board-quality scenario, When its scorecard passes but an expected signal is missing, Then the scenario fails | Each of the nine board-quality PASS lines, the eight board-creation PASS lines that share the scorecard and the root playbook Section 3 say so | Met | - |
| AC-009 | REQ-009 | Given `results.jsonl`, When `run/aggregate.py` rebuilds it, Then the gallery rows follow the board points first and the gallery images and captions match them | `aggregate.py` rebuilds `results.jsonl` with only FJ-023's gallery row moved, to SWE 114:4602, and `process-board.png` has the SHA-1 of `renders/swe-FJ-023-114-4602.png` | Met | - |
| AC-010 | REQ-010 | Given a `use_figma` result that returns a board id, When the driver reads the run, Then the board is recorded whether or not the call held `const MODEL` | `run/adaptive_compare.py` `boards()` returns 134:5211 for DeepSeek's FJ-027 from its committed exports | Met | - |
| AC-011 | REQ-011 | Given a gantt with `after` and an ER model, When the composer draws them, Then each dependency is an arrow and each relationship end carries its cardinality mark, the state reference says where an exit from a composite starts and the Project mirror matches | `compose_board.py --self-test` 1029 of 1029, live gantt 147:5390 (5 arrows) and ER 148:5423 (6 marked relationships) with 0 warnings on the test file, and `validate_parity.py product-owner` PASSED 65/65 at Barter e79cfbe86 | Met | - |

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

AC-001 to AC-011 are Met. The operator reopened the phase on 2026-10-26 to fix the run's six findings, and the fixes passed their self-tests, a live render and the parity gate.
<!-- /ANCHOR:closure -->

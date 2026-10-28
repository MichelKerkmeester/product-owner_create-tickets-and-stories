---
title: "Feature Specification: Phase 48: FigJam neighbour and closing fixes"
description: "The v1.0.13.0 rerun passed 1 of 4. FJ-023's readers met a decision beside the accent before the entry, FJ-036's intake round ended on a Why line, FJ-017's scenario asked for a Finding the skill does not and the label trace drew diamonds wider than FigJam does. This phase fixes every cause as v1.0.14.0 with the Claude Project in step, then reruns FJ-017, FJ-022, FJ-023 and FJ-036."
trigger_phrases:
  - "figjam neighbour and closing fixes"
  - "phase 48 figjam fixes"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 48: FigJam neighbour and closing fixes

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-28 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 48 of 48 |
| **Predecessor** | 047-figjam-glance-and-row-fixes |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 48** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: every cause the v1.0.13.0 rerun names in `sk-create-figjam`, its scripts, its shipped models, the playbook and the Claude Project mirror, then a rerun of FJ-017, FJ-022, FJ-023 and FJ-036.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-047.*`, README section 8.13).
- `sk-create-figjam` v1.0.13.0 as phase 047 left it.

**Deliverables**:
- The script, skill, model and playbook fixes, released as hub and `sk-create-figjam` v1.0.14.0.
- The hand-written Project mirror in the same commit.
- The graded rerun and the gallery boards it earns.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.13.0 and 1 of 4 passed: FJ-022 PASS at 21, FJ-023 FAIL at 21, FJ-036 FAIL at 22 and FJ-017 FAIL with no scorecard. On FJ-023 both readers read the decision beside the accent on its row before the entry the `Glance:` line put second, so Composition scored 1. FJ-036's first intake round ended on a `Why:` line after its last question, because the question template puts the reason last. FJ-017's scenario asked for a `Finding:` line naming any sticky below or left of its node, while the skill asks for one only when a sticky leaves its named side. The label trace drew decision diamonds 24 px wider than FigJam does and read their text box narrower than FigJam fits it, so it passed `Drop-off point or courier?`, whose last word FigJam stranded. FJ-022 ran the check before its playback with the reader and the dials assumed, which the draw threshold does not allow under Standard energy but no playbook signal scored. Flow-mode asked the gate to name the dials, which no example gate does, and the Composition row charged both parts of a swapped pair.

### Purpose
Let the glance plan read a decision beside the accent where readers meet it, end each intake round on one closing question, ask FJ-017 for the Finding the skill gives, trace diamond labels at FigJam's size and box, keep the dials at the playback, charge one point for a swapped pair and score a turn 1 that models before its intake, in the skill and the Project alike.

### Decisions
Taken from the fresh Opus recommendation of 2026-10-28, which checked each cause against the files, the run streams and the renders, under the operator's standing instruction to proceed on it.

- **D1**: Accent neighbour. `reading_order` puts a decision joined to the accent by one line, set on the accent's own row with no node between them on that row, right after the accent. `references/quality-rubric.md` Section 3 states the same exception, the process example's `Glance:` line and second glance are regenerated and a self-test holds the FJ-036 shape, where a node stands between, to the plain order.
- **D2**: Closing question. Every intake round ends on one closing question after its last block, such as `Take the recommended answers, or correct any of them?`, so each `Why:` line stays inside its block: `assets/flow-templates.md` Section 5, `references/flow-mode.md` Section 8 and playbook Section 5, where a round whose last line is anything else misses its signal. The template's block order stays.
- **D3**: Finding on a moved sticky. FJ-017 and the root playbook ask for a `Finding:` line only for a sticky that left the side its `Sides:` line named, and none for a sticky placed where its line said. `references/hybrid-workflow.md` Section 3 says the check gives the second sticky the side below or to the left and names it on its `Sides:` line, so the gate shows it. The Project hybrid mirror, which has no check, says the notes call chooses the side from the returned boxes and a reply names every sticky placed below or left of its node on a `Finding:` line.
- **D4**: Diamond label trace. `compose-trace.mjs` measures whole-pixel line heights, so the trace draws diamonds at the size FigJam draws them, and `board_geometry._text_width` reads a diamond's text box as half its width less 8 px. A self-test holds a 26-character decision to a 336 px diamond, and the user flow example's `Drop-off point or pickup?` is reworded in the skill and the Project.
- **D5**: Dials at the playback. The playback names the three dials by their words and the gate need not repeat them, in flow-mode and its mirror, and playbook Section 5 fails a playback that leaves one out.
- **D6**: Composition levels. The playbook Composition row scores 2 when the planned order holds with the requested element first, 1 when one part reads out of its planned place or one unplanned part reads at or before the second glance, and 0 for two or more or a requested element not first. When two parts swap, only the part read earlier than its place costs the point.
- **D7**: Turn 1 intake. Playbook Section 5: under Standard energy, when the sources leave the reader unsettled or more than two rows assumed, turn 1 is an intake round, and no model is written and no check runs before the playback's answer, read from the tool stream.
- **D8**: Release. Every change lands in the skill and its hand-written Project mirror in the same commit as hub and `sk-create-figjam` v1.0.14.0, with a kernel bump only if a kernel sentence changes.

FJ-022's 047 PASS stands: its scenario's signals and PASS line held when it was graded, and D7 scores later runs on the rule it broke.

Three calls made while implementing, kept on review: the composer keeps edge labels 4 px clear of a zone title as the check asks, the user flow example's 30-day label reads `Within 30 days after delivery?` in the returns doc's words so its check prints no `Label:` line, and FJ-022 states turn 1 is an intake round because D7 makes it binding.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Lift the accent's row decision per D1, with a self-test, the rubric sentence and the regenerated process example.
- Write the closing question per D2, the FJ-017 Finding per D3, the playback dials per D5, the Composition levels per D6 and the turn 1 intake rule per D7.
- Fix the diamond trace per D4, with a self-test and the reworded user flow label.
- Write the Project mirror and release v1.0.14.0 per D8.
- Rerun FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.14.0 with Claude Sonnet 5.5 high, each in a fresh draft file in the operator's team drafts, grade them as phase 047 graded its rerun and refresh the gallery boards the passing runs earn.

### Out of Scope
- The composer's layout and geometry beyond the trace's line height and the edge label's clearance from a zone title, which moves to the check's 4 px because the whole-pixel line height left one planted label 1 px into a title and REQ-001 needs the composer self-test to pass.
- A rerun of scenarios that passed on v1.0.13.0 or earlier and are untouched by these rules.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/scripts/flow_check.py, scripts/figjam_checks/board_geometry.py, scripts/compose-trace.mjs, scripts/compose_board.py, assets/compose-board.js | Modify | The accent neighbour, the diamond text box, the whole-pixel line height and their self-tests |
| sk-create-figjam/references/, assets/ | Modify | Flow Mode, rubric, hybrid workflow, flow templates and the user flow and process examples |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Composition row, the Section 5 rules and FJ-017 |
| claude project/, SYNC.md, README.md | Modify | The mirror and the release notes |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.14.0 |
| benchmark/reports/.../, sk-create-figjam/assets/screenshots/ | Create, Modify | The rerun records and the gallery |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity, residency and divergence checks print PASSED after the last commit. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | The `Glance:` line puts a decision joined to the accent on its row with no node between right after the accent, the rubric states it and a self-test holds the case with a node between per D1. |
| REQ-004 | Flow templates Section 5, flow-mode Section 8 and playbook Section 5 end each intake round on one closing question per D2. |
| REQ-005 | FJ-017, the root playbook, hybrid-workflow Section 3 and the Project hybrid mirror state the Finding rule per D3. |
| REQ-006 | The trace draws a 26-character decision at 336 px, a diamond's text box reads half its width less 8 px and the user flow example's label no longer strands a word per D4. |
| REQ-007 | Flow-mode and its mirror name the dials at the playback and playbook Section 5 checks them per D5. |
| REQ-008 | The playbook Composition row carries the D6 levels and the swapped-pair sentence. |
| REQ-009 | Playbook Section 5 states the turn 1 intake rule per D7. |
| REQ-010 | `sk-create-figjam` and the hub read 1.0.14.0 with a changelog, and the mirror and the SYNC note carry every change per D8. |
| REQ-011 | FJ-017, FJ-022, FJ-023 and FJ-036 are rerun on v1.0.14.0, graded by one Opus grader with two readers per board and recorded in the run README as section 8.14, and the gallery takes each passing board. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Each cause of README section 8.13 that names a skill, script, playbook or mirror cause has a change in this phase or a recorded reason it needs none.
- **SC-002**: The skill and the Project state each changed rule in the same words, as the Sync Loop parity and divergence checks show.
- **SC-003**: At least 3 of FJ-017, FJ-022, FJ-023 and FJ-036 pass on v1.0.14.0.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The diamond text box is measured on one diamond size | Med | It applies to diamonds alone, other round shapes keep their reading, and the `may leave` line stays advice |
| Risk | The turn 1 rule fails a run that would have passed before | Med | It follows the draw threshold flow-mode already states, so it scores a rule the skill holds |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No board URL, Figma file key, plan name or email in any committed file. PO is a public repository.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A decision joined to the accent on its row with a step between them: it keeps its place in the column order.
- A diamond label whose last word fits by a few pixels: the check prints `may leave`, which is advice.

### Error Scenarios
- A board the check cannot trace: the `Glance:` line says it was skipped and the plan falls back to path order.
- A sticky the notes call moved off its named side: the reply names it on a `Finding:` line.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 13/25 | About 25 files across the scripts, skill, examples, playbook and mirror, plus a four-scenario rerun |
| Risk | 7/25 | A reading-order exception and a trace measure, each self-tested |
| Research | 3/20 | The causes were checked by a fresh Opus reviewer against the files, the streams and the renders |
| **Total** | **23/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. D1 to D8 were settled on 2026-10-28 from the fresh Opus recommendation under the operator's standing instruction.
<!-- /ANCHOR:questions -->

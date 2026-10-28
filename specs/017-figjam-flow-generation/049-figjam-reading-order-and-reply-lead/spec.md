---
title: "Feature Specification: Phase 49: FigJam reading order and reply lead"
description: "The v1.0.14.0 rerun passed 2 of 4. The glance order lifted a decision readers did not take second, a delivery reply opened on a sentence above the URL, FJ-023 still expected a turn 1 playback and 8 nodes against the rules, the examples modelled no intake round and the label trace counted characters where FigJam measures glyphs. This phase fixes each as v1.0.15.0 with the Claude Project in step, then reruns FJ-022 and FJ-023."
trigger_phrases:
  - "figjam reading order and reply lead"
  - "phase 49 figjam fixes"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 49: FigJam reading order and reply lead

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
| **Phase** | 49 of 49 |
| **Predecessor** | 048-figjam-neighbour-and-closing-fixes |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 49** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: every cause the v1.0.14.0 rerun names in `sk-create-figjam`, its scripts, its shipped models, the playbook, the run harness and the Claude Project mirror, then a rerun of FJ-022 and FJ-023.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-048.*`, README section 8.14).
- `sk-create-figjam` v1.0.14.0 as phase 048 left it.

**Deliverables**:
- The script, skill, model, playbook and harness fixes, released as hub and `sk-create-figjam` v1.0.15.0 with kernel v1.2.15.
- The hand-written Project mirror in the same commit.
- The graded rerun and the gallery boards it earns.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.14.0 and 2 of 4 passed: FJ-017 PASS, FJ-036 PASS at 21, FJ-022 FAIL at 20 and FJ-023 FAIL at 21. On FJ-023 both readers read the lane entry before the decision the `Glance:` line lifted beside the accent, and across the 18 reader orders of three runs that lift fit the minority. FJ-022 opened its delivery reply on a sentence announcing itself above the board URL, a slip seen in six earlier runs, because the rule names a heading, a summary and a note but not an announcement. FJ-023 skipped its turn 1 intake round and drew the runbook's queue as a ninth node, while its scenario still expects a turn 1 playback and 8 nodes and the process reference allows a queue as a store. Five of the seven shipped examples leave the reader unnamed and open on a playback, which the FJ-023 run copied. The label trace counted characters, so it passed `New price compared to old?`, whose last word FigJam stranded on FJ-036. Two grade records misread reader orders, caught only by a later check.

### Purpose
Plan the glance order readers actually take, put the board URL first in every delivery, make FJ-023 and the examples agree with the turn 1 rule, measure diamond labels as FigJam does and score Composition mechanically, in the skill and the Project alike.

### Decisions
Taken from a fresh Claude Sonnet 5.5 high recommendation of 2026-10-28, which checked each cause against the files, all 18 reader orders and the renders, under the operator's standing instruction to proceed on it.

- **D1**: Plain reading order. `reading_order` drops the lift that put a decision beside the accent second: the accent comes first, then column by column along the flow. Across all 18 reader orders of the 046 to 048 runs the lift fit the minority on FJ-023 and cost more boards than the plain order. `references/quality-rubric.md` Section 3 drops the exception and says the printed order is the majority read, the process example's `Glance:` line and second glance follow and phase 048's D1 is superseded.
- **D2**: Reply lead. Everything written after the last tool call is the reply and its first characters are the board URL, with no sentence before it, not a status line or a sentence announcing the reply. `references/flow-mode.md` Section 8 and step 11, `SKILL.md`, the rubric, `assets/flow-templates.md` with a wrong and a right first line, the kernel and the mirrors state it, and the harness flags a delivery whose first line is not the URL.
- **D3**: FJ-023 turns and the queue. FJ-023 scripts the turn 1 intake round its prompt calls for, as FJ-022 does, and keeps 8 of 8 nodes. `references/types/process.md` draws a queue that only carries work between two lanes as the crossing connector's label, and a queue is a store only when steps read and write it on their own.
- **D4**: Examples model the intake. The gantt, ER and sequence example requests name their reader, and the process and user flow examples show an intake round before the playback, in the skill and the Project.
- **D5**: Diamond wrap by glyph width. The label check wraps a diamond's label by Inter Medium advance widths at half its width less 4 px and reports a stranded last word as `leaves`, with a self-test on the labels FigJam stranded.
- **D6**: Dials are not rows. The detail level, the audience and the reading distance are dials, never Brief rows, so an unstated dial takes its default and never counts toward the two assumed rows, while a reader no source names stays unsettled. Flow-mode Section 2, playbook Section 5 and the mirror state it.
- **D7**: Mechanical Composition. Each reader's notes end on an `Order:` line and `run/composition_check.py` scores Composition from the plan's `Glance:` line and the two readers' orders, so the grader no longer reads the order by eye.
- **D8**: Release. Every change lands in the skill and its hand-written Project mirror in the same commit as hub and `sk-create-figjam` v1.0.15.0, with kernel v1.2.15 for the reply lead.

The operator's call the recommendation left open, charging only parts read earlier than planned, is not taken: it would loosen the rubric to fit one run, and FJ-022 would still fail on its reply.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Return the reading order to the plain order per D1, with self-tests, the rubric sentence and the regenerated process example.
- Write the reply lead per D2, the FJ-023 turns and the queue rule per D3, the examples per D4 and the dials rule per D6.
- Measure diamond labels by glyph width per D5, with self-tests.
- Add the `Order:` line and the Composition script per D7.
- Write the Project mirror and release v1.0.15.0 per D8.
- Rerun FJ-022 and FJ-023, the two that failed, on v1.0.15.0 with Claude Sonnet 5.5 high one after the other, grade them as phase 048 graded its rerun and refresh the gallery boards the passing runs earn.

### Out of Scope
- The composer's layout and geometry.
- A rerun of FJ-017 and FJ-036, which passed on v1.0.14.0 and which these rules touch only in wording.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/scripts/flow_check.py, scripts/figjam_checks/board_geometry.py | Modify | The plain reading order and the glyph-width diamond wrap with their self-tests |
| sk-create-figjam/SKILL.md, references/, assets/ | Modify | Flow Mode, rubric, the process type, flow templates and the examples |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Section 5 rules and FJ-023 |
| claude project/, SYNC.md, README.md | Modify | The mirror, kernel v1.2.15 and the release notes |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.15.0 |
| benchmark/reports/.../run/ and grades/ | Create, Modify | The reader brief, the Composition script and the delivery check |
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
| REQ-003 | `reading_order` prints the accent first and then column by column, the rubric says the order is the majority read and the process example follows per D1. |
| REQ-004 | Flow-mode, `SKILL.md`, the rubric, the flow templates, the kernel and the mirrors put the board URL first per D2, and the harness flags a delivery that does not. |
| REQ-005 | FJ-023 and its root playbook section script the turn 1 intake round and `references/types/process.md` and its mirror draw a handoff queue as a label per D3. |
| REQ-006 | The gantt, ER and sequence examples name their reader and the process and user flow examples show an intake round, with their mirrors, per D4. |
| REQ-007 | The diamond label check wraps by Inter Medium advance widths and a self-test holds the stranded labels per D5. |
| REQ-008 | Flow-mode Section 2, playbook Section 5 and the mirror state that dials are not rows per D6. |
| REQ-009 | The reader brief ends on an `Order:` line and `run/composition_check.py` scores Composition per D7. |
| REQ-010 | `sk-create-figjam` and the hub read 1.0.15.0 with a changelog, the kernel H1 reads v1.2.15 and the mirror and the SYNC note carry every change per D8. |
| REQ-011 | FJ-022 and FJ-023 are rerun on v1.0.15.0, graded with two readers per board and the Composition script and recorded in the run README as section 8.15, and the gallery takes each passing board. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Each cause of README section 8.14 that names a skill, script, playbook, harness or mirror cause has a change in this phase or a recorded reason it needs none.
- **SC-002**: The skill and the Project state each changed rule in the same words, as the Sync Loop parity and divergence checks show.
- **SC-003**: FJ-022 and FJ-023 both pass on v1.0.15.0.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Readers differ on the goal, an exit below the row and the entry against a decision in the accent's lane | High | The order is the majority read, a part costs a point only when both readers misplace it and the rerun may still lose Composition on reader variance alone |
| Risk | The glyph widths are measured on 336 px diamonds only | Med | Other shapes keep their character measures until a render measures them |
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
- A decision in the accent's lane to the right of the entry: it reads in its column, after the entry.
- A delivery that ends a clean-up call: the next text is the reply and opens on the URL.

### Error Scenarios
- A board the check cannot trace: the `Glance:` line says it was skipped and the plan falls back to path order.
- A reader note with no `Order:` line: the Composition script names the note and stops.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | About 30 files across the scripts, skill, seven examples, playbook, harness and mirror, plus a two-scenario rerun |
| Risk | 7/25 | A reading-order revert and a glyph-width measure, each self-tested |
| Research | 3/20 | The causes were checked against the files, 18 reader orders and the renders |
| **Total** | **24/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. D1 to D8 were settled on 2026-10-28 from the fresh Sonnet recommendation under the operator's standing instruction.
<!-- /ANCHOR:questions -->

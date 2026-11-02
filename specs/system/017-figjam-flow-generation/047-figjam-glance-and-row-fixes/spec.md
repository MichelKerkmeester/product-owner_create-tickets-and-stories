---
title: "Feature Specification: Phase 47: FigJam glance and row fixes"
description: "The v1.0.12.0 rerun passed 0 of 4. Three gates showed a sketch that dropped lines of the checked model, the glance plan put off-row nodes last where the composer draws them early, a past-the-dot sticky sat 328 px from its node, label wraps the sources' words could not clear cost Legibility and an intake round ended after its stop line. This phase fixes every cause as v1.0.13.0 with the Claude Project in step, then reruns FJ-017, FJ-022, FJ-023 and FJ-036."
trigger_phrases:
  - "figjam glance and row fixes"
  - "phase 47 figjam fixes"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 47: FigJam glance and row fixes

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-28 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 47 of 48 |
| **Predecessor** | 046-figjam-gate-and-accent-fixes |
| **Successor** | 048-figjam-neighbour-and-closing-fixes |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 47** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: every cause the v1.0.12.0 rerun names in `sk-create-figjam`, its scripts, its shipped models, the playbook, the run harness and the Claude Project mirror, then a rerun of FJ-017, FJ-022, FJ-023 and FJ-036.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-046.*`, README section 8.12).
- `sk-create-figjam` v1.0.12.0 as phase 046 left it.

**Deliverables**:
- The script, skill, model, playbook and harness fixes, released as hub and `sk-create-figjam` v1.0.13.0.
- The hand-written Project mirror in the same commit, with kernel v1.2.13.
- The graded rerun and the gallery boards it earns.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran FJ-017 and FJ-036, which failed on v1.0.11.0, and the board-quality scenarios FJ-022 and FJ-023 on v1.0.12.0, and 0 of 4 pass: FJ-017 FAIL with no scorecard, FJ-022 20, FJ-023 19 and FJ-036 19. Three gates showed a sketch that dropped lines of the checked model, `%%` lines on FJ-017 and FJ-036 and lane style lines on FJ-023. The glance plan put every off-row node last, while the composer draws Contact support (FJ-022), Send a second photo and the Claims table (FJ-023) and Get credit (FJ-036) where both readers meet them early, so Composition scored 1, 0 and 0. FJ-017's No-show sticky sat 328 px from its node, past the one sticky width rule, and the Cancelled sticky went below instead of the side its line named, since the `Sides:` line named no alignment. Label wraps cost Legibility on all three scored boards, on FJ-022 and FJ-036 no label in the sources' words cleared the check and the Legibility row set no level for several wraps. FJ-022's intake round ended on a sentence after its stop line, promising a dials round no rule placed. The harness rewrote committed records in a whole-folder redaction pass.

### Purpose
Let the glance plan follow the drawn board, flag a main row that bends, pin each sticky's side and alignment within reach, make the gate show the checked model line for line, give labels a way past a wrap the sources' words cannot clear, place the dials in intake round one and keep the harness to each scenario's own output, in the skill and the Project alike.

### Decisions
Taken under the operator's standing instruction of 2026-10-28 to settle open work autonomously.

- **D1**: Glance follows the drawing. `flow_check.py` prints a `Glance:` line on a user flow or a process, the order a reader meets the nodes: the accent first, then column by column along the flow and down each column, with the goal marked. `references/quality-rubric.md` Section 3 plans the second glance as the nodes up to and including the goal in that order and the last glance as the rest, or the key and the source line when the goal comes last, with path order as the fallback when the line is skipped. The playbook Composition row scores against that order.
- **D2**: Row advisory. A non-failing `Row:` line names a line between two main-row steps that bends off the row, the node between them and, on a zoned flow, the move into the next step's zone. The composer's layout is unchanged.
- **D3**: Sticky reach and alignment. `Sides:` lines name the alignment, top aligned or centred beside and left aligned or centred below or above, and no square further than one sticky width (240 px) from its node is offered. `references/hybrid-workflow.md` says the notes call places each sticky on the named side and alignment.
- **D4**: Verbatim gate sketch. The gate shows the checked model exactly as the check read it, every `%%` and `style` line, with the `PASSED` line as printed, in flow-mode step 7, rubric Section 5, the kernel, the mirror, all seven examples' Sketch line and playbook Section 5.
- **D5**: Label measures. A word only one measure strands prints `may leave`, step 5 allows a reworded or longer label in the source's words and naming an unclearable label at the gate, the Legibility row's 1 covers one or more awkward wraps and the user flow and process examples were relabelled so the check prints no `Label:` line. A new self-test checks each worked example's Check block equals the real check output.
- **D6**: Composition. Parts a reader names together in one step of their reading order read as a set.
- **D7**: Intake dials. `assets/flow-templates.md` Section 5 round One asks the three dials and flow-mode Section 4 names that round.
- **D8**: Playbook Section 5. An intake round a run opens beyond those its scenario names ends on its question, and trailing text misses the playback signal.
- **D9**: Harness. `run/run_full.sh` redacts each scenario's own output, `run/adaptive_compare.py` redacts run-log rows and reads a counted `Read-back:` line or a `use_figma` call as a delivery and `run/redact_run.py` takes single files with its two sibling copies matching.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Print the `Glance:` line and the `Row:` advisory per D1 and D2, with self-tests, and plan and score the glance lines from it.
- Name each sticky's alignment and cap its reach per D3, with self-tests.
- Make the gate sketch verbatim per D4 in every source, example and mirror that states it.
- Add the `may leave` measure, the label branches, the Legibility level and the Check block self-test per D5, and relabel the user flow and process examples.
- Write the Composition set reading per D6, the round One dials per D7 and the extra intake round rule per D8.
- Fix the harness per D9.
- Rerun FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.13.0 with Claude Sonnet 5.5 high, each in a fresh draft file in the operator's team drafts, grade them as phase 046 graded its rerun and refresh the gallery boards the passing runs earn.

### Out of Scope
- The composer's layout and geometry.
- A rerun of scenarios that passed on v1.0.12.0 or earlier and are untouched by these rules.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/scripts/flow_check.py, scripts/figjam_checks/board_geometry.py | Modify | The glance, row, sides and label lines and the Check block self-test |
| sk-create-figjam/references/, assets/ | Modify | Flow Mode, rubric, hybrid workflow, flow templates and the seven worked examples |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Composition and Legibility rows and the Section 5 stop rules |
| claude project/, SYNC.md, README.md | Modify | The mirror, kernel v1.2.13 and the release notes |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.13.0 |
| benchmark/reports/.../run/ | Modify | The harness redaction and delivery reading |
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
| REQ-003 | `flow_check.py` prints a `Glance:` line on a user flow or a process, the rubric plans the glance lines from it with path order as the fallback and the playbook Composition row scores against it per D1. |
| REQ-004 | `flow_check.py` prints a non-failing `Row:` line for a main-row line that bends off the row, naming the node between and the zone move on a zoned flow, with the composer unchanged per D2. |
| REQ-005 | Each `Sides:` line names its alignment, no square past one sticky width is offered and the hybrid workflow places each sticky on the named side and alignment per D3. |
| REQ-006 | Flow-mode step 7, rubric Section 5, the kernel, the mirror, all seven examples and playbook Section 5 require the checked model verbatim with the `PASSED` line as printed per D4. |
| REQ-007 | The label trace prints `may leave`, step 5 allows a reworded or longer label and names an unclearable one at the gate, the Legibility row covers several wraps, the relabelled examples print no `Label:` line and a self-test compares each example's Check block with the check per D5. |
| REQ-008 | The playbook Composition row reads parts named together in one reading step as a set per D6. |
| REQ-009 | Flow templates Section 5 round One asks the three dials and flow-mode Section 4 names that round per D7. |
| REQ-010 | Playbook Section 5 states the extra intake round rule per D8. |
| REQ-011 | `run_full.sh`, `adaptive_compare.py` and the three `redact_run.py` copies behave per D9. |
| REQ-012 | `sk-create-figjam` and the hub read 1.0.13.0 with a changelog, and the kernel H1 reads v1.2.13. |
| REQ-013 | FJ-017, FJ-022, FJ-023 and FJ-036 are rerun on v1.0.13.0, graded by one Opus grader with two readers per board and recorded in the run README as section 8.13, and the gallery takes each passing board. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Each cause of README section 8.12 that names a skill, script, playbook, harness or mirror cause has a change in this phase or a recorded reason it needs none.
- **SC-002**: The skill and the Project state each changed rule in the same words, as the Sync Loop parity and divergence checks show.
- **SC-003**: At least 3 of FJ-017, FJ-022, FJ-023 and FJ-036 pass on v1.0.13.0.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A reading order the check prints that readers do not follow | Med | The order comes from the drawn columns readers met in the 046 renders, and the rerun scores it with two readers per board |
| Risk | Rules no rerun has tested | Med | A fresh Opus reviewer reads the whole diff before the commit, and the rerun follows |
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
- A flow whose goal comes last in the drawn order: the last glance names the key and the source line.
- An end dot more than one sticky width past its node: the right side is not offered and the sticky takes another side.

### Error Scenarios
- A board the check cannot trace: the `Glance:` line says it was skipped and the plan falls back to path order.
- A label no wording in the source's words clears: it is kept and named at the gate.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 15/25 | About 30 files across the scripts, skill, examples, playbook, harness and mirror, plus a four-scenario rerun |
| Risk | 8/25 | Two new check lines and a reach cap on the sides search, each self-tested, with the composer unchanged |
| Research | 2/20 | The findings were graded and challenged before this phase |
| **Total** | **25/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. D1 to D9 were settled on 2026-10-28 under the operator's standing instruction.
<!-- /ANCHOR:questions -->

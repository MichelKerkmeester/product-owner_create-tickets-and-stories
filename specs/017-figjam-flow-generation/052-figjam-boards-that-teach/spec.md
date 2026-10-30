---
title: "Feature Specification: Phase 52: FigJam boards that teach the reader something"
description: "The gallery boards are tidy but say little: one-line labels, zones with only a name, a large key and a highlight with no reason. This phase lets cards and sections carry what the source says, makes the key compact, asks every highlight for its reason, adds a Substance score, gives each gallery test a spec-sized source and reruns the gallery with Sonnet 5.5 medium."
trigger_phrases:
  - "figjam boards that teach"
  - "phase 52 figjam"
  - "figjam substance score"
  - "figjam section notes"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 52: FigJam boards that teach the reader something

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-30 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 52 of 52 |
| **Predecessor** | 051-figjam-gallery-rerun |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 52** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: `sk-create-figjam`'s checker, composer, docs, examples and board-quality scenarios, its Claude Project mirror, the model comparison run folder and the gallery.

**Dependencies**:
- `sk-create-figjam` v1.0.16.0 and the phase 051 gallery.
- Claude Code serving `claude-sonnet-5-5` at medium effort with Figma's hosted MCP, and a draft file per run in the operator's team plan.

**Deliverables**:
- Section notes, detail cards at Balanced and Faithful on four types, a compact key and a required focus reason.
- A Substance dimension on the board quality scorecard.
- Ten gallery scenarios with spec-sized sources, rerun and graded, and a gallery drawn from them.
- Release sk-create-figjam 1.0.17.0 and hub 1.0.18.0, with the Claude Project mirror.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement

Michel found the gallery boards tidy but empty next to the collab chat prompt board. Each card holds one short line, so "Pick a reason" never says which reasons exist. A zone holds only a name such as "Done". The key takes about a fifth of the board and explains shapes. One node is marked "In focus" without a reason. The scorecard rewards tidiness and a match with the brief, and the test briefs are three sentences, so an empty board scores 22 of 22.

### Purpose

A board that teaches the reader what its source says: what a step asks, where a section starts and ends, and why one thing is marked.

### Decisions

- **D1**: GLM 5.3 Flash max draws every board, through Devin as `glm-5-3-flash-max`. Michel chose GLM on Pi first. Pi has no Figma write route, since its only MCP server is Code Mode, whose Figma manual is read-only, so Michel chose the Devin route on 2026-10-30. Devin's weekly quota was spent on the first run, so Michel amended D1 the same day: Sonnet 5.5 medium on Claude Code draws every board, the model the 051 gallery used.
- **D2**: A `%% about: <zone label or lane id> | line | line` line gives a zone or lane up to three note lines of at most 56 characters, drawn under its title. A user flow or process at Balanced or Faithful with two or more zones gives every zone one. The docs show Starts, Ends and Good to know as the lines a stage zone takes.
- **D3**: Detail cards are allowed at Balanced, up to 4 body lines, and at Faithful, up to 10, on a user flow, a process with or without lanes, an architecture and a state diagram. Simplified keeps one-line labels. A sequence, an ER model and a gantt have no card to describe, since an ER entity already lists its fields.
- **D4**: The key draws on one compact band, with smaller samples and small type. Every accent needs its reason, so a user flow or process with a `style` accent also needs `%% focus: <id> because <reason>`.
- **D5**: The scorecard gains Substance in the reading zoom: each scored scenario names two source questions whose answers are in its source and in no one-line label. 2: both readers answer both. 1: one question. 0: none. A board totals 24 and passes at 20.
- **D6**: The ten gallery scenarios, FJ-022 to FJ-028, FJ-032, FJ-036 and FJ-049, each give a spec-sized fictional source with screens, rules and edge cases in the prompt, and name the two source questions.
- **D7**: Every gallery image comes from this run. A failing board is rerun once and the better of its two runs takes the image, and its caption names the failure. The old images are not kept, because none of them could answer a source question. Amended on 2026-10-30: the status lane image keeps its v1.0.16.0 board on Michel's choice, because the graded FJ-049 run drew no status lane, and the seven boards with body cards ran again after the composer fixes for card corners, key samples and cylinder cards, which Michel chose.
- **D8**: Grading follows phase 051: two fresh readers per board, `run/composition_check.py` and one Claude Sonnet 5.5 high grader.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Checker, composer and model changes for D2 to D4, with fixtures.
- Docs, templates and examples that teach section notes, detail cards and the focus reason.
- The scorecard change in the playbook root and the quality rubric, and the ten scenarios.
- The release, the Claude Project mirror, the rerun, the grades and the gallery.

### Out of Scope
- The Composition rule and the reading-order gaps phase 051 found.
- Sequence, ER and gantt cards.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/scripts/ | Modify | `%% about:`, detail levels on more types, the focus reason |
| sk-create-figjam/assets/compose-board.js, assets/figjam-design.md | Modify | Section notes and the compact key |
| sk-create-figjam/references/, assets/templates/, assets/examples/ | Modify | The new lines and their rules |
| sk-create-figjam/manual-testing-playbook/ | Modify | Substance, the ten scenarios |
| sk-create-figjam/assets/screenshots/, README.md | Modify | Gallery and captions |
| sk-create-figjam/changelog/, SKILL.md, hub version files | Modify | Release 1.0.17.0 and hub 1.0.18.0 |
| claude project/ | Modify | The hand-written mirror |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify | Runs, grades and report section 8.17 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Zones and lanes carry notes | A model with `%% about:` lines checks clean and composes with the notes under each title, and a Balanced zoned flow without them is refused |
| REQ-002 | Detail cards on four types at Balanced and Faithful | The fixtures pass for each type and level, and Simplified refuses a body |
| REQ-003 | Every accent has a reason | A flow with a style accent and no focus reason is refused |
| REQ-004 | No board URL, file key, plan name or email in a committed file | The scan prints nothing |
| REQ-005 | The gates pass | `run_gates.sh` passes, the Sync Loop parity passes |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-006 | The key is compact | A composed board's key band is at most 104 pixels tall on one row |
| REQ-007 | The scorecard scores Substance | The playbook root and rubric define it, and every scored scenario totals 24 |
| REQ-008 | Ten graded runs on Sonnet 5.5 medium | Each meta.json names `claude-sonnet-5-5` at medium effort, with two reader notes and a scorecard row |
| REQ-009 | The gallery comes from this run, the status lane image excepted by D7 | Every caption names its run, model, version and score |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A reader of any gallery board answers a question the request's first sentence does not answer.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The composer grows past the Claude Project's room | High | Measure the compact code before and after, and cut elsewhere if it does |
| Risk | The board maker writes before the gate or deletes boards, as GLM did on 2026-10-25 | Med | Each run gets its own draft file, and the delete rule from that run is in Flow Mode |
| Risk | A long reply is cut off | Low | The run log records the stop reason, and a failed run is rerun once |
| Dependency | Claude Code usage | Med | The batch resumes where it stopped |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: Product Owner is a public repository, so no board URL, Figma file key, plan name or email is committed, and the test sources use fictional brands only.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A zone whose notes are wider than its nodes: the zone widens to its notes.
- A lane's notes: drawn under the lane title, and the lane's steps move down to clear them.

### Error Scenarios
- A run that writes no board is recorded and rerun once.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | Checker, composer, docs, playbook, mirror and a rerun |
| Risk | 12/25 | Composer geometry and the Project's room |
| Research | 8/20 | The Substance measure |
| **Total** | **38/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->

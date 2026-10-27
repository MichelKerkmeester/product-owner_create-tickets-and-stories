---
title: "Feature Specification: Phase 44: FigJam composite placement and path order"
description: "The v1.0.9.0 rerun passed 1 of 7, and every remaining failure has Composition at 0. The composer draws a composite across the top row, plans order a flow by fill while readers take its main row in path order and the revision exemption is too narrow. This phase fixes them as v1.0.10.0 and reruns the 6 failures with a working node."
trigger_phrases:
  - "figjam composite and path order"
  - "phase 44 figjam composite placement"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 44: FigJam composite placement and path order

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-27 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 44 of 44 |
| **Predecessor** | 043-figjam-rerun-followups |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 44** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the causes the v1.0.9.0 rerun found in `sk-create-figjam`, its composer, its glance rules, the playbook, the Claude Project mirror and the run's launcher, then a rerun of the 6 failures. No Barter board is read or written.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-043.*`, README section 8.9).
- `sk-create-figjam` v1.0.9.0 as phase 043 left it.

**Deliverables**:
- The composer placement, the path-order glance rule and the wider revision exemption, released as hub and `sk-create-figjam` v1.0.10.0, with the kernel moved only if its rules change.
- The hand-written Project mirror, including the composer code block read off `--template`.
- A graded rerun of the 6 failures with a working node, its renders and README section 8.10.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran the 7 failures of v1.0.8.0 on v1.0.9.0 and 1 passes. Every scored board has Composition at 0. The composer's `layered()` gives each zone its own lane and puts every node outside a zone in the last lane, so on FJ-026 and FJ-032 the Confirmed composite spans the top row above the first state and both readers read Upcoming and In stay first, a pink focus outline included. On FJ-029, FJ-031 and FJ-036 readers take a flow's main row in path order after the accent, while the plans order nodes by fill and outline: FJ-031's plain screens read before its changed end, which the revision exemption does not cover, FJ-029 puts one kind of diamond in two glance lines and FJ-036 leaves two nodes out of every line. FJ-017's second sticky sits right of its node, and no check traced a label because Homebrew's node on the run machine cannot load its `simdutf` library.

### Purpose
Make the board draw what the plan says reads first, make the plan follow the order readers take, and prove it by rerunning the 6 failures on the same model with a working node.

### Decisions
- **D1**: The composer places a composite after the state that enters it in reading order, to its right on a left-to-right board and below it on a top-to-bottom one, so the first state keeps the top-left place. A board with no composite composes byte-identical, and the composer keeps the Project's room.
- **D2**: After the accent and the entry, readers follow a flow's main row in path order. A plan names every node the board draws in some glance line, names the main row in path order and keeps nodes of one kind in one line.
- **D3**: On a revision whose changed end holds the planned second glance, every main-row node the rubric plans last costs no Composition point when it reads before the changed end, not only the entry and the decisions.
- **D4**: The launcher puts the working nvm node first on PATH, and a fixture that prints a `Label:` line proves it before any lane starts.
- **D5**: The rerun covers FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036. FJ-017 is graded on the reading of beside the v1.0.8.0 grade used, as the operator ruled for phase 043.
- **D6**: Exact sentence swaps whose wording this phase sets are applied by script and byte-checked in the skill and the mirror alike. DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the code changes, one change per brief. A fresh Opus reviewer verifies the whole diff. GPT 6 Luna max fast on cli-codex is the only fallback.
- **D7**: Every skill change reaches its Project file in the same commit, and the Flow Board Composer Knowledge code block is read off `compose_board.py --template` again.
- **D8**: Each rerun board scenario writes into a fresh draft file in the Barter team plan with its starting section count recorded, and each run has its own temp folder. No board URL, file key, plan name or email reaches a committed file.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Place a composite after the state that enters it in `assets/compose-board.js`, with a self-test case and the state example recomposed.
- Write the path-order glance rule and the wider revision exemption into the rubric, the playbook Composition row and the Project.
- Pin a working node in the run launcher and prove the label trace runs.
- Rerun the 6 failures with two readers per scored board, grade them and write README section 8.10.

### Out of Scope
- The composer's colours, type sizes and router.
- Running FJ-018 and FJ-035, which need Figma Desktop and the figma-ds-cli daemon.
- Rerunning FJ-009, which passed on v1.0.9.0.
- The machine's Homebrew node install.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/assets/compose-board.js, scripts/ | Modify | Composite placement and its self-test |
| sk-create-figjam/references/, assets/examples/ | Modify | The path-order glance rule, the revision exemption and the plans the examples show |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Composition row and FJ-017's sticky signal |
| claude project/, SYNC.md, README.md | Modify | Mirror, composer code block and release notes |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify, Create | The grader brief, the rerun records and README |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.10.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity and residency checks print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | A state board with a composite composes with the first state at the top left and the composite after the state that enters it, proved by a self-test case, and a board with no composite composes byte-identical. |
| REQ-004 | The rubric, the playbook Composition row and the Project state the path-order glance rule per D2. |
| REQ-005 | The rubric, the playbook Composition row and the Project state the wider revision exemption per D3. |
| REQ-006 | The launcher pins a working node, and a fixture prints a `Label:` line through it before the lanes start. |
| REQ-007 | The 6 failures run again on Claude Sonnet 5.5 high in fresh files, every board is rendered and read by two readers and each scenario is graded on one line. |
| REQ-008 | `sk-create-figjam` and the hub read 1.0.10.0 with a changelog, and the kernel H1 moves only when its rules change. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: At least 4 of the 6 rerun scenarios pass, and every remaining failure is named with its cause in the run README.
- **SC-002**: No rerun state board has a composite state in both readers' orders ahead of the planned first glance.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Draft files in the Barter team plan for every board scenario | High | Files are created before the lanes start and their keys stay in the scratchpad |
| Risk | The composer's room in the Project | High | `--design-check` measures the room after the change and the Composer Knowledge file names it |
| Risk | A layout change moves boards with zones on other types | Med | The self-test composes every shipped example and the change is limited to composites |
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
- A state board with no composite: it composes byte-identical to v1.0.9.0.
- A composite entered from two states: it sits after the first of them in reading order.

### Error Scenarios
- A node fixture that prints no `Label:` line: no lane starts until the pinned node traces it.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | About 20 files across composer, rubric, examples, mirror, playbook, launcher and records |
| Risk | 12/25 | The composer layout every state board uses and a live rerun |
| Research | 3/20 | The findings were graded and criticised before this phase |
| **Total** | **27/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose the composer fix, the 042 reading for FJ-017 and the pinned node on 2026-10-27.
<!-- /ANCHOR:questions -->

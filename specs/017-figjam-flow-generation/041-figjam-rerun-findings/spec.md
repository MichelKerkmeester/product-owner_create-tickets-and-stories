---
title: "Feature Specification: Phase 41: FigJam rerun findings"
description: "The v1.0.6.0 rerun of the 31 scenarios that did not pass closed at 14 PASS, 13 FAIL and 4 SKIP, and a findings pass and a critic named 35 findings across the skill, the composer, the playbook, the driver and the run records. This phase fixes them as v1.0.7.0, mirrors them to the Project and reruns every scenario that did not pass."
trigger_phrases:
  - "figjam rerun findings"
  - "phase 41 figjam rerun findings"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 41: FigJam rerun findings

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-26 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 41 of 41 |
| **Predecessor** | 040-figjam-sonnet-run-findings |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 41** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the 24 findings and the 11 critic findings of the v1.0.6.0 rerun in `sk-create-figjam`, the Interactive Mode reference, the playbook, the Claude Project mirror and the run folder's driver and records, then a rerun of every scenario that did not pass. No Barter board is read or written.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-rerun.*`, README section 8.6).
- `sk-create-figjam` v1.0.6.0 as phase 040 left it.

**Deliverables**:
- The skill, composer, playbook and driver fixes, released as hub and `sk-create-figjam` v1.0.7.0 and `sk-product-owner` v1.2.4.0.
- The hand-written Project mirror.
- The corrected 040 records, then a graded rerun with its renders and README section.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran the 31 scenarios v1.0.5.0 did not pass on v1.0.6.0 and passed 14. Six of the 13 failures are model slips alone. The rest trace to the skill or the playbook: the skill never says when a user asked for one board, a state board cannot lead with the group of end states a request names, the heavier goal outline reads before a planned second glance and the No route reply skips the playback. Two playbook rows give no full mark to a board that follows the rubric, the driver hands a pinned run three destinations and lane files fill with earlier boards. The critic also found records that score one claim two ways.

### Purpose
Remove every gap the findings name, correct the records and prove the fixes by rerunning every scenario that did not pass on the same model.

### Decisions
- **D1**: A user asked for one board only when the request says one board, a single board or one diagram. Naming where the board goes, such as on a new board or in this file, is a destination and not a request for one board.
- **D2**: DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the edits, Opus agents plan and verify them and GPT 6 Luna max fast on cli-codex is the only fallback.
- **D3**: One Opus grader scores every rerun board on one scale, then skeptics and adjudicators check each verdict.
- **D4**: Every skill change reaches its Project file in the same commit.
- **D5**: Each rerun scenario that writes a board gets a fresh draft file in the Barter team plan, created before its first turn, with its starting section count recorded. No board URL, file key, plan name or email reaches a committed file.
- **D6**: The greyscale outline weights stay. The glance order they cost is fixed in the planning rules, so the Signal gains of v1.0.6.0 hold.
- **D7**: The critic's record findings are applied to the 040 records as adjudications, with each change named in the grade summary.
- **D8**: FJ-018 and FJ-035 stay operator-only because they need Figma Desktop. FJ-044 is run by the operator through the hosted server, and FJ-045 runs alone after the other lanes because it edits the shared design file and restores it.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Define a request for one board, settle the first reply when a broad brief also fits two types and keep the playback and the gate before a missing-route reply.
- Plan a state board's composite and first state against the request, plan the outlined kinds right after the accent and map a leadership reader to the Executive and Simplified dials.
- Give a single sticky a place when its preferred sides are taken, a logged process a writer, a state guard its label and a read-back its honest source.
- Refuse a self-loop on a user flow or process, space gantt and graph arrivals at least 24 pixels apart and warn on a guard that names a model id.
- Give the Composition, Signal, Fidelity and Hygiene rows a full mark for a board that follows the rubric, and give FJ-020 its second turn.
- Send each pinned run one destination, give each board scenario a fresh file and script the operator steps the driver can perform.
- Correct the 040 rerun records the critic named, then rerun every scenario that did not pass and grade it.

### Out of Scope
- A router change for the composite state exit that crosses one edge - still recorded as an open failure in the self-test.
- Running FJ-018 and FJ-035, which need Figma Desktop and the figma-ds-cli daemon.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/SKILL.md, references/, assets/ | Modify | Flow Mode, rubric, hybrid workflow, the type references, the design and the templates |
| sk-create-figjam/assets/compose-board.js, scripts/ | Modify | Arrival spacing, gantt arrows, the self-loop refusal, the guard warning and their checks |
| sk-create-figjam/manual-testing-playbook/ | Modify | Scorecard rows, FJ-020, FJ-029 and the Hygiene exception |
| sk-product-owner/references/interactive-mode.md | Modify | Open items carry no board fact in a command conflict |
| claude project/, SYNC.md, README.md | Modify | Mirror and release notes |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify, Create | Driver, the 040 record corrections, the rerun records and README |
| changelog/, sk-create-figjam/changelog/, sk-product-owner/changelog/, version files | Create, Modify | v1.0.7.0 and v1.2.4.0 |
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
| REQ-003 | Flow Mode in the skill and the Project defines a request for one board as D1 sets out, settles the first reply when a broad brief fits two types and runs the playback and the gate before a missing-route reply. |
| REQ-004 | The state, rubric, dial, sticky, process log, guard and read-back rules the findings name say what the run showed they must, in the skill and the Project. |
| REQ-005 | `flow_check.py` refuses a self-loop on a user flow or process, and the composer self-test proves arrivals on one side and gantt arrows into one bar land at least 24 pixels apart where the side holds them. |
| REQ-006 | The playbook's Composition, Signal, Fidelity and Hygiene rows score a board that follows the rubric at full marks, and FJ-020 has the turn its later-round signal needs. |
| REQ-007 | The driver sends a pinned run one destination, each board scenario writes into a fresh file with its starting section count recorded and the operator steps the driver can perform are scripted. |
| REQ-008 | The 040 rerun records carry the critic's corrections, and every scenario that did not pass runs again on Claude Sonnet 5.5 high with every board rendered and each scenario graded on one line. |
| REQ-009 | `sk-create-figjam` and the hub read 1.0.7.0 and `sk-product-owner` 1.2.4.0, each with a changelog. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The rerun passes more of the scenarios it runs than the 14 of 27 the v1.0.6.0 rerun passed, and every remaining failure is named with its cause in the run README.
- **SC-002**: No rerun board loses a Signal point in greyscale, so the v1.0.6.0 outlines still hold.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Draft files in the Barter team plan for every board scenario | High | Files are created before the lanes start and their keys stay in the scratchpad |
| Risk | FJ-045 edits the shared design file | High | It runs alone after the other lanes, and its last step restores the file and checks `git diff --exit-code` |
| Risk | The composer call's room in the Project, about 2,470 characters | Med | Any composer change is measured with `--design-check` and the Composer Knowledge file names the new room |
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
- A side too short for its arrivals at 24 pixels apart: the points space out to fit the side, as a short gantt bar already does.

### Error Scenarios
- A scenario whose fresh file cannot be created: the lane stops before its first turn and the scenario is recorded as a harness failure.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | About 60 files across skill, mirror, composer, playbook, driver and records |
| Risk | 10/25 | The composer every board write sends, the shared design file and a live rerun |
| Research | 4/20 | The findings were graded and criticised before this phase |
| **Total** | **32/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose to fix all 35 findings on 2026-10-26.
<!-- /ANCHOR:questions -->

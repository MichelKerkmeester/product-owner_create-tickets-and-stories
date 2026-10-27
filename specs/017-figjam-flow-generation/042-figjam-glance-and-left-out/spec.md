---
title: "Feature Specification: Phase 42: FigJam glance plans and Left out"
description: "The v1.0.7.0 rerun passed 2 of the 16 scenarios it ran. Composition decided most failures, because the glance rules and the shipped examples disagree with what the composer draws, and the Left out line, the single sticky and the router spacing each left a gap. This phase fixes them as v1.0.8.0, mirrors them to the Project and reruns the 14 failures."
trigger_phrases:
  - "figjam glance and left out"
  - "phase 42 figjam glance plans"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 42: FigJam glance plans and Left out

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
| **Phase** | 42 of 42 |
| **Predecessor** | 041-figjam-rerun-findings |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 42** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the 25 findings and the 10 critic gaps of the v1.0.7.0 rerun in `sk-create-figjam`, its examples, the playbook, the composer, the Claude Project mirror and kernel, and the run folder's driver and records, then a rerun of the 14 scenarios that failed. No Barter board is read or written.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-041.*`, README section 8.7).
- `sk-create-figjam` v1.0.7.0 as phase 041 left it.

**Deliverables**:
- The skill, example, composer, playbook and driver fixes, released as hub and `sk-create-figjam` v1.0.8.0 with kernel v1.2.10.
- The hand-written Project mirror.
- A graded rerun of the 14 failures with its renders and README section 8.8.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran every scenario that did not pass on v1.0.6.0 and passed 2 of 16. Composition is below full marks on 8 of the 9 scored boards. The models copy the shipped examples, and the process, architecture and user flow examples leave the goal, the gateway or the light blue entry out of their glance lines, while the rubric omits the entry from the kinds that read early. `references/types/state.md` plans the composite first, but readers read the saturated first state first. The `Left out:` rule contradicts itself on a split and no rule puts one on a gate. The single sticky has no free side next to an end-dot connector, and the router lets two runs lie 24 pixels apart.

### Purpose
Make the glance rules and examples match the board the composer draws, close the Left out, sticky, router and playbook gaps and prove it by rerunning the 14 failures on the same model.

### Decisions
- **D1**: State boards. The rule follows the board: with no state named, the first state is planned first, and the composite section reads as part of the frame like the title block and never counts in the glance order. The composer and the design stay unchanged.
- **D2**: FJ-045 tests the design fallback, so its signals change to a goal that is light green and not pink and a first glance that is the accented node. The rubric's accent candidates stay.
- **D3**: A `Left out:` line appears whenever the board does not hold something the request or sources named: a cut, a split or a later board. The gate carries one too.
- **D4**: FJ-017 is a board-write scenario, so its record drops the scorecard and the two signals the grader added, and it passes or fails on its own signals.
- **D5**: Exact sentence swaps whose wording this phase sets are applied by script and byte-checked in the skill and the mirror alike. DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the code changes, one change per brief. A fresh Opus reviewer verifies the whole diff. GPT 6 Luna max fast on cli-codex is the only fallback.
- **D6**: Every skill change reaches its Project file in the same commit.
- **D7**: Each rerun board scenario writes into a fresh draft file in the Barter team plan with its starting section count recorded. No board URL, file key, plan name or email reaches a committed file.
- **D8**: Defaults taken without a question. A same-title revision finds its old section by the earlier written time. A label that would leave one word alone on its last line gets a `Label:` warning from `flow_check.py` before the gate, and the composer is not changed, because the Project sends the whole composer in every call and its largest shipped example already uses all but about 55 characters of the room (the operator chose this on 2026-10-27). The router is not changed either: recomposed today, FJ-026's model keeps check-out and missed check-in 72 pixels apart on the composer's own path estimate, which already rejects two runs closer than 56 pixels, so the 24 pixels readers saw is FigJam's own elbow routing and a cost change cannot reach it. The first split title is spelled `1. Sign up`. The reader brief carries the scenario's persona and Q1 to Q3 and gives one reader every board of a split. Each run gets its own temp folder.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Rewrite the state glance rule per D1 and treat the composite like the title block in the playbook's Composition row.
- Add the light blue entry to the rubric's early kinds, and bring the glance lines of all seven examples in line with the rubric.
- Score an unplanned part that reads before the planned second glance at 1 in the Composition row.
- Name every cut, split and later board in `Left out:`, in the reply and the gate, in the skill, the Project, `AGENTS.md` and the kernel.
- Give the single sticky a place past its node's end dot and bar moving a sticky without a new yes.
- Find a same-title revision's old section by its earlier written time, and spell the first split title one way.
- Warn before the gate about a label that would leave one word alone on its last line, with a self-test case.
- Fix the FJ-045, FJ-009, FJ-038, FJ-029 and FJ-040 scenario rows, drop the FJ-017 scorecard and add reader questions to FJ-045.
- Give the reader brief the persona and Q1 to Q3, and each run its own temp folder.
- Rerun the 14 failures, grade them and write README section 8.8.

### Out of Scope
- Running FJ-018 and FJ-035, which need Figma Desktop and the figma-ds-cli daemon.
- Rerunning FJ-020 and FJ-044, which passed on v1.0.7.0.
- Changing the accent candidates in the rubric or the composer's colours.
- The router. FigJam routes an elbowed connector itself, and the composer's path estimate already keeps the FJ-017 and FJ-026 runs apart.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/SKILL.md, references/, assets/ | Modify | Flow Mode, rubric, hybrid workflow, state reference, flow templates and the seven examples |
| sk-create-figjam/scripts/ | Modify | The label warning in the pre-write check and its self-test |
| sk-create-figjam/manual-testing-playbook/ | Modify | Composition row and the FJ-009, FJ-029, FJ-038, FJ-040 and FJ-045 scenarios |
| AGENTS.md, claude project/, SYNC.md, README.md | Modify | Reply contract, mirror, kernel and release notes |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify, Create | Driver, the FJ-017 record, the rerun records and README |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.8.0 |
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
| REQ-003 | The state rule, the rubric's early kinds and the glance lines of all seven examples agree with what the composer draws, in the skill and the Project. |
| REQ-004 | Every reply and gate that leaves something out carries a `Left out:` line, and no file states the narrower rule. |
| REQ-005 | The single sticky rule places a note past its node's end dot and bars an ungated move, and a same-title revision's delete finds the earlier section by its written time. |
| REQ-006 | `flow_check.py` prints a `Label:` warning for a label the board would wrap with one word alone on its last line, never fails on it and leaves the composer byte-identical, proved by a self-test case. |
| REQ-007 | The playbook's Composition row and the named scenario rows say what D1, D2 and D4 decided, and FJ-045 names three reader questions. |
| REQ-008 | The 14 failures run again on Claude Sonnet 5.5 high in fresh files, every board is rendered and each scenario is graded on one line. |
| REQ-009 | `sk-create-figjam` and the hub read 1.0.8.0 with a changelog, and the kernel reads v1.2.10. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: At least 7 of the 14 rerun scenarios pass, and every remaining failure is named with its cause in the run README.
- **SC-002**: No rerun board loses a Composition point because a glance line copied from a shipped example left out a kind the rubric names.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Draft files in the Barter team plan for every board scenario | High | Files are created before the lanes start and their keys stay in the scratchpad |
| Risk | FJ-045 edits the shared design file | High | It runs alone after the other lanes, and its last step restores the file and checks `git diff --exit-code` |
| Risk | The composer call's room in the Project | Med | Any composer change is measured with `--design-check` and the Composer Knowledge file names the new room |
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
- A state board whose request names a state: the focus line marks that state first, the first state is planned second and the composite stays part of the frame.
- A sticky whose node has no end dot and every side taken: it takes the side with the shortest clear line and the reply says so on a `Finding:` line.

### Error Scenarios
- A scenario whose fresh file cannot be created: the lane stops before its first turn and the scenario is recorded as a harness failure.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 16/25 | About 40 files across skill, examples, mirror, kernel, composer, playbook, driver and records |
| Risk | 10/25 | The composer router every board write sends, the kernel and a live rerun |
| Research | 3/20 | The findings were graded and criticised before this phase |
| **Total** | **29/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator settled D1 to D4 on 2026-10-27.
<!-- /ANCHOR:questions -->

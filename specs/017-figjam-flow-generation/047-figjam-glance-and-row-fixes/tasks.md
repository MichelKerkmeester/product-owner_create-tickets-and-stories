---
title: "Tasks: Phase 47: FigJam glance and row fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam glance and row fixes tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 47: FigJam glance and row fixes

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

**Task Format**: `T### [P?] Description (file path). Verify: <command> prints <expected output>`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/047-figjam-glance-and-row-fixes/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.12 cause to a change or a reason it needs none. Verify: each maps to D1 to D9 or is named in the implementation summary. [EVIDENCE: the off-row nodes read early map to D1 and D2, the 328 px sticky and the Cancelled side to D3, the three sketches that drop lines to D4, the wraps the sources' words could not clear, the flagged wrap FJ-023's board did not draw and the missing Legibility level to D5, parts read in one step to D6, FJ-022's promised dials round to D7 and D8 and the whole-folder redaction to D9]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Print the `Glance:` line and plan and score the glance lines from it (`scripts/flow_check.py`, `scripts/figjam_checks/board_geometry.py`, `references/quality-rubric.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: the flow check self-test passes the reading-order case. [EVIDENCE: `glance_lines` in `flow_check.py` and `reading_order` in `board_geometry.py`, the case "a flow prints the order a reader meets it, and a node between two row steps is met there and named on a Row line" passes, the process example prints `Glance: Approve the claim (accent) > ... > Refund released (goal)`, rubric Section 3 plans the second glance up to the goal and the last glance after it or the key and the source line with path order as the fallback and the playbook Composition row plans every node "in the order the check's `Glance:` line prints"]
- [x] T004 Print the non-failing `Row:` advisory (`scripts/flow_check.py`, `scripts/figjam_checks/board_geometry.py`, `references/flow-mode.md`). Verify: the self-test prints a Row line for the split zone and none once the node joins the next zone, and the composer has no diff. [EVIDENCE: `row_breaks` in `board_geometry.py`, the case naming "Row: the line from Within 30 days? to Start a return bends off its row round Contact support, so move Contact support into the zone Start a return sits in" and the case "the same node in the next step's zone shares its column and leaves the row straight" pass, flow-mode step 5 names the line and `git diff` shows no change to `compose_board.py` or `assets/compose-board.js`]
- [x] T005 Name each sticky's alignment and cap its reach at one sticky width (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`, `references/hybrid-workflow.md`). Verify: the sides self-test passes with a near and a far end dot. [EVIDENCE: `STICKY_REACH = STICKY` and `sticky_sides` returning top aligned, centred or left aligned, `Sides:` lines read "takes its sticky right, top aligned", the case ending "no sticky stands further than one sticky's width from its node" passes with an end dot 76 px and 276 px past the node and hybrid-workflow Section 3 says the notes call places each sticky "on the side and in the alignment its line named"]
- [x] T006 Make the gate sketch verbatim (`references/flow-mode.md`, `references/quality-rubric.md`, `assets/examples/`, `manual-testing-playbook/manual-testing-playbook.md`, `claude project/Custom Instructions.md`). Verify: each source names every `%%` and `style` line with the `PASSED` line as printed. [EVIDENCE: flow-mode step 7 shows "the checked model exactly as the check read it, every `%%` line and every `style` line included", the rubric Section 5 checklist line, the kernel's Flow write bullet, all seven examples' Sketch line and the playbook Section 5 paragraph now failing "a sketch that drops a line of the checked model such as a `%%` line or a `style` line"]
- [x] T007 Read labels for `may leave`, give step 5 its branches, widen the Legibility row and relabel the two examples (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`, `references/flow-mode.md`, `assets/examples/user-flow-fernhouse-return.md`, `assets/examples/process-fernhouse-refund.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: both examples pass with no `Label:` line and every example's Check block matches the check. [EVIDENCE: the expected case reads "Label: Editor with welcome tip may leave 'tip' alone", step 5 allows a reworded or longer label in the source's words and names an unclearable one at the gate, the Legibility row's 1 reads "one or more labels wrap awkwardly", `flow_check.py` prints PASSED with no `Label:` line for both relabelled examples and the new case "shows the output the check prints" passes for all seven examples]
- [x] T008 Read parts named in one reading step as a set (`manual-testing-playbook/manual-testing-playbook.md`). Verify: the Composition row states it. [EVIDENCE: "Parts a reader names together in one step of their reading order read as a set the same way, so their order against each other costs no point"]
- [x] T009 Ask the three dials in intake round One (`assets/flow-templates.md`, `references/flow-mode.md`). Verify: the round One row and flow-mode Section 4 name it. [EVIDENCE: flow templates Section 5 round One asks "The reader, the question, the outcome and the three dials" and the Section 4 distance paragraph says the dials are asked "in intake round one"]
- [x] T010 Hold an extra intake round to its question (`manual-testing-playbook/manual-testing-playbook.md`). Verify: playbook Section 5 states it. [EVIDENCE: "An intake round a run opens beyond those its scenario names ends on its question too, and text after that question misses the playback signal"]
- [x] T011 Keep the harness to each scenario's own output (`benchmark/reports/.../run/run_full.sh`, `run/adaptive_compare.py`, the three `run/redact_run.py` copies). Verify: the three copies hash alike. [EVIDENCE: `run_full.sh` passes only the scenario's own skill, reply, failed-attempt and stdout paths to `redact_run.py` when `RUN_REDACT_FILE` is set, `adaptive_compare.py` writes each row through `log_line` and `classify` reads a counted `Read-back:` line or a `use_figma` call as DELIVERY, `redact_run.py` redacts a named file alone and all three copies hash to `f44bfdd0`]
- [x] T012 Write the Project mirror for every changed skill file (`claude project/knowledge/`, `SYNC.md`). Verify: `validate_parity.py product-owner` and `pair_divergence.py product-owner` print PASSED. [EVIDENCE: 12 Knowledge files and the kernel carry the changes, the SYNC.md note of 2026-10-28 records each, and parity is read after the commit]
- [x] T013 Release v1.0.13.0 with kernel v1.2.13 (`SYNC.md`, `README.md`, version files, changelogs, `claude project/Custom Instructions.md`). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.13.0 and the kernel H1 reads v1.2.13. [EVIDENCE: `SKILL.md`, `description.json`, `hub-router.json`, `mode-registry.json` and `sk-create-figjam/SKILL.md` read 1.0.13.0, both v1.0.13.0 changelogs exist and the kernel H1 reads v1.2.13]
- [x] T014 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: the reviewer found 1 P1 and 11 P2 and no P0, all confirmed and repaired: a skip edge read as a bent row, an accented goal unmarked, a Check-block test that could skip silently, the dials in four first-round sentences, the top-down order, the revision exemption, a past-the-dot sticky out of reach, a taken side at the write, two labels outside the source's words, the README, two harness gaps and a serial comma, with 194 of 194 self-test checks after]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T015 Run the self-tests and gates on the committed tree. Verify: both self-tests, the design check, pytest, 15 of 15 gates and the output format gate pass.
- [ ] T016 Commit and push both repositories. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED.
- [ ] T017 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both after the closing edits.
- [ ] T018 Rerun FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.13.0, each in a fresh draft file (`benchmark/reports/.../skill/sonnet-high-047/`). Verify: each run has a `meta.json` and every turn exited 0.
- [ ] T019 Grade the four runs with two readers per board and one Opus grader (`grades/sonnet-high-047.*`). Verify: every scenario has a verdict with its signals.
- [ ] T020 Record the rerun as run README section 8.13, refresh the gallery with each passing board and commit both repositories. Verify: `validate_parity.py product-owner` prints PASSED.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [ ] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [ ] Manual verification passed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-013, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the nine decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-046.*` and README section 8.12]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and check self-tests pass with the new cases [EVIDENCE: on the working tree on 2026-10-28, `flow_check.py --self-test` printed 186 of 186 and `compose_board.py --self-test` 1250 of 1250, each exit 0]
- [ ] CHK-011 [P1] pytest passes
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [ ] CHK-020 [P0] All acceptance criteria met
- [ ] CHK-021 [P0] Gates pass
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each 8.12 cause is classed as script, skill, playbook, harness or model slip in the implementation summary]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: the verbatim sketch rule reaches flow-mode step 7, rubric Section 5, the kernel, all seven examples and playbook Section 5, and a search of `claude project/` on 2026-10-28 finds the new wording in the kernel, the Flow Mode and rubric Knowledge files and the seven example files]
- [ ] CHK-FIX-003 [P0] Consumer inventory completed
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: the row cases cover a node in its own zone and the same node moved into the next zone, the sides case covers an end dot inside and past one sticky width and the label case covers a word only the narrow measure strands]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: the sketch rule over seven examples, three rule files, the kernel and the playbook, and the relabel over the two flow examples whose checks printed a `Label:` line]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the spec tools run with the PO links created only for each run and removed after, as the operator asked]
- [ ] CHK-FIX-007 [P1] Evidence pinned to a diff range
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [ ] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [ ] CHK-040 [P1] Spec, plan and tasks synchronized
- [ ] CHK-041 [P1] Project mirror and SYNC note
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [ ] CHK-050 [P1] No change outside the files named in spec.md Section 3
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: this phase has no scratch folder]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 6 |
| P1 Items | 9 | 4 |
| P2 Items | 0 | 0 |

**Verification Date**: Pending
<!-- /ANCHOR:summary -->

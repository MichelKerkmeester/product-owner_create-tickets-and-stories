---
title: "Implementation Plan: Phase 50: FigJam lessons from a hand-built spec board"
description: "Trust only a read-back view rendered after the write, make the subtitle name the start and the end, add an optional status lane to a laned process, add detail cards at the Faithful detail level, ship one anonymized worked example of that board, check it all with the gates and release v1.0.16.0 with the Project in step."
trigger_phrases:
  - "figjam spec board learnings plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 50: FigJam lessons from a hand-built spec board

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

Five changes to `sk-create-figjam`, built in order of risk: the two wording changes first (D1, D2), then the status lane (D3), then detail cards (D4), then the worked example that exercises both (D5), then the mirror and the release (D6). The composer and the checker are read before D3 and D4 are written, because both add layout the composer does not draw today.

### Values the operator confirmed on 2026-10-29

| Item | Proposal |
|------|----------|
| Detail card level | Only at the `Faithful` detail level. `Balanced` and `Simplified` keep one-line labels |
| Detail card budget | A laned process at `Faithful` with detail cards: at most 18 nodes and 24 connectors per diagram, status states included |
| Body length | At most 10 body lines per card, each at most 44 characters, after a label of at most 40 characters on one line |
| Body type | A `body` token, 16 by default, Regular, line height 145%, with a 10 pixel spacer under the label. Floor: from `small` up to `node` |
| Status state | A chevron in the `neutral` role inside the status lane, so it differs from a step by shape, and a key entry `Status`. The operator chose the chevron on 2026-10-29, because a step is already a rounded rectangle |
| Status move line | A dotted connector in `line.lifeline` gray, key entry `Moves the status`, distinct from the dashed `Optional or proposed` line |
| Example brand | Fernhouse, as a commissioned planter: a client and a maker moving one commission through its statuses |
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

- `python3 sk-create-figjam/scripts/compose_board.py --self-test` and `--design-check` exit 0.
- `python3 sk-create-figjam/scripts/flow_check.py --self-test` exits 0, with new cases for the status lane and detail cards.
- `pytest sk-create-figjam/scripts/tests` passes.
- The repository gates run by the repository's gate runner all pass.
- `node "z — Claude Project Sync Loop/validate-output-format.cjs" --system product-owner` exits 0.
- The Sync Loop's `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` print PASSED after the last commit.
- The anonymity scan exits 0: `rg -i -f <local term list> sk-create-figjam "claude project" SYNC.md README.md changelog specs/017-figjam-flow-generation/050-figjam-spec-board-learnings` prints nothing. The term list lives outside the repository, so the source product's terms are never committed.
- `validate.sh --strict` on this phase and the parent prints `RESULT: PASSED`.
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

| Decision | Where it lands | How |
|----------|----------------|-----|
| D1 Fresh read-back | `references/flow-mode.md` step 10 and Section 7, `references/quality-rubric.md`, `references/hybrid-workflow.md` | A view counts only when it shows the write's change. The default read is `node.screenshot()` inside the `use_figma` call that wrote or a later one. A `get_screenshot` that matches the board before the write is reported `stale` and taken again |
| D2 Subtitle | `assets/flow-templates.md` Section 1, every `%% subtitle:` line in `assets/examples/` and `assets/templates/` | One sentence that names where the flow starts and where it ends, and the reader where the brief names one |
| D3 Status lane | `references/types/process.md`, `assets/templates/process.md`, `assets/compose-board.js`, `scripts/compose_board.py`, `scripts/figjam_checks/flowchart.py`, `assets/figjam-design.md` | A `%% status: <lane id>` line marks one lane as the status lane. The composer draws it first, joins its states in order by the status line and routes each `-.->` from a step to a state as the dotted status move. The checker holds: one status lane at most, states only inside it, states joined in a single chain, a move only from a step to a state |
| D4 Detail cards | `references/flow-mode.md` Section 4, `references/types/process.md`, `assets/figjam-design.md`, `assets/compose-board.js`, `scripts/compose_board.py`, `scripts/figjam_checks/` | A `%% detail: <node id> \| <line> \| <line>` line gives a node its body. The composer sets the label in `node` Bold on one line, the spacer and the body in the `body` token, left-aligned, and sizes the card to the wider of the label and the body. The checker refuses a body below `Faithful` and holds the budget in Section 1 |
| D5 Worked example | `assets/examples/process-fernhouse-commission.md`, `assets/templates/process.md` | The hand-built board's shape, rewritten for Fernhouse: a status lane, a client lane and a maker lane, one branch for a delivery and one for an in-person fitting, and a review loop of changes until approval |
| D6 Release | Version files, both changelogs, `SYNC.md`, `README.md`, `claude project/knowledge/`, `claude project/Custom Instructions.md` | Patch steps: hub 1.0.17.0, `sk-create-figjam` 1.0.16.0. Each changed skill file gets its Project counterpart written by hand in the same commit |

### Project counterparts

| Skill file | Project knowledge file |
|------------|------------------------|
| `references/flow-mode.md` | Flow Mode material in the kernel and the matching knowledge file |
| `references/quality-rubric.md` | `Product Owner - Rules - Flow Quality Rubric.md` |
| `references/style-guide.md`, `references/types/process.md` | `Product Owner - Rules - Flow Style Guide.md` |
| `assets/figjam-design.md` | `Product Owner - Assets - Flow Board Design.md` |
| `assets/compose-board.js` | `Product Owner - Assets - Flow Board Composer.md` |
| `assets/flow-templates.md` | `Product Owner - Assets - Flow Templates.md` |
| `assets/templates/process.md` | `Product Owner - Assets - Flow Templates - Process.md` |
| `assets/examples/process-fernhouse-commission.md` | A new `Product Owner - Examples - Flow - Process Commission.md` |
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

1. **Read.** Read `assets/compose-board.js` lane and node layout, `scripts/compose_board.py` model parsing and `scripts/figjam_checks/flowchart.py` process rules, and confirm or revise the proposals in Section 1 with the operator.
2. **Wording.** D1 and D2, with every shipped subtitle line rewritten and each example's Check block still matching the check.
3. **Status lane.** D3 in the checker first with failing self-tests, then the composer, then the design key and the process type and template.
4. **Detail cards.** D4 in the same order: checker, composer, design token and floor, then the references.
5. **Worked example.** D5, composed once on a scratch board, read back under D1 and checked against its own Check block.
6. **Playbook.** One scenario each for the status lane, the detail cards and the fresh read-back.
7. **Mirror and release.** D6, the SYNC note and the release notes, then a fresh review of the whole diff.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

- **Self-tests**: each new checker rule gets a passing and a failing case, and the composer self-test gets a status lane board and a detail card board.
- **Design check**: the `body` token below `small` or above `node` falls back and warns.
- **Live board**: the worked example composed once in a scratch draft file, with its read-back taken by `node.screenshot()` after the write.
- **Anonymity**: the scan in Section 2 on every changed file before each commit.
- **Regression**: every shipped example's Check block still matches, and the composer self-test count rises only by the new cases.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| A Figma connection with `use_figma` | External | Available on 2026-10-29 | The worked example's board cannot be composed or read back |
| The operator's confirmation of the Section 1 proposals | Internal | Confirmed on 2026-10-29 | The checker cannot enforce the detail budget |
| The outer repository's Sync Loop | Internal | Available | Parity cannot be shown |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: a gate fails after the release commit, or the operator rejects the status lane or the detail cards on the composed example.
- **Procedure**: revert the release commit in Product Owner and the mirror commit in the outer repository with `git revert`, then rerun the Sync Loop checks. The scratch board is deleted only on the operator's yes.
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Read | None | Status lane, Detail cards |
| Wording | None | Mirror and release |
| Status lane | Read | Worked example |
| Detail cards | Read | Worked example |
| Worked example | Status lane, Detail cards | Playbook |
| Playbook | Worked example | Mirror and release |
| Mirror and release | All | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Read | Low | 1 hour |
| Wording | Low | 1 hour |
| Status lane | High | 4 to 6 hours |
| Detail cards | High | 4 to 6 hours |
| Worked example | Medium | 2 hours |
| Playbook | Low | 1 hour |
| Mirror and release | Medium | 2 hours |
| **Total** | | **15 to 19 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] The anonymity scan prints nothing
- [ ] Every gate in Section 2 exits 0 on the tree to be committed

### Rollback Procedure
1. `git revert` the Product Owner release commit and push after the operator's go-ahead.
2. `git revert` the outer mirror commit and push after the operator's go-ahead.
3. Rerun `validate_parity.py product-owner` and confirm PASSED.

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: None needed. The only external state is the scratch board, removed on the operator's yes.
<!-- /ANCHOR:enhanced-rollback -->

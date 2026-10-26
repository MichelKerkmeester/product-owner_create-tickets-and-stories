---
title: "Implementation Summary"
description: "The seven board-quality scenarios ran on DeepSeek V4.1 Flash Max, GLM 5.3 Flash Max and SWE 2 Max, every board was graded on the 22-point scorecard, SWE 2 Max is the recommended model and the gallery holds the best board per type."
trigger_phrases:
  - "figjam model comparison implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/038-figjam-model-comparison"
    last_updated_at: "2026-10-26T01:45:00Z"
    last_updated_by: "claude-code"
    recent_action: "Graded all 21 boards, refreshed the gallery and closed every acceptance criterion"
    next_safe_action: "Open a phase for the run README's six findings, starting with a delete that needs a named yes"
    blockers: []
    key_files:
      - "spec.md"
      - "decision-record.md"
      - "acceptance-criteria.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 038-figjam-model-comparison |
| **Status** | Complete |
| **Completed** | 2026-10-26 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The seven board-quality scenarios, FJ-022 to FJ-028, ran once on each of DeepSeek V4.1 Flash Max, GLM 5.3 Flash Max and SWE 2 Max through the Devin CLI, against the composer and design file phase 037 shipped. All 21 runs finished and every board was graded on the 22-point scorecard by fresh Claude Sonnet 5.5 graders. GLM and SWE tie at 148 of 154 with five passes each and DeepSeek scores 144. The run README recommends SWE 2 Max, because it is the only model that never wrote before a gate and never changed work it did not create, while GLM, which won four of seven types on rank, deleted ten boards it never created after a generic yes. The seven gallery images are now the best board per type.

The operator then reopened the phase to fix the six findings the run recorded. Flow Mode deletes a board only on a reply that names it and recovers from a `use_figma` call with no `fileKey`. Every board-quality and board-creation scenario now needs its expected signals as well as its scorecard. The gallery rule ranks the 16 board points first, which moved FJ-023's image to SWE's board. The driver reads a board id from any `use_figma` result. The composer draws gantt dependencies as arrows and marks both ends of an ER relationship with Figma's crow's-foot caps, and the state reference names the inner state a composite exit leaves from. Fixing the driver also showed that the runner's URL redaction had cut text from JSON exports, so the 21 exports whose raw copies survived were redacted again from raw. On the operator's request four gallery boards were then drawn again from their best run's model: gantt 149:5482, ER 150:5517, the existing-board state 151:5578 and the dense flow 152:5695, each with 0 warnings. The dense flow's model took the two changes today's check asks for, one accent and a shorter credit label.

The operator then asked how GPT 6 Luna max and Claude Opus 5.5 low do on the same seven scenarios. `run/runtimes.py` adds a Codex and a Claude Code turn backend behind the same driver, and one fresh Opus 5.5 medium grader scored the 14 runs. Luna totals 142 with two passes and Opus 5.5 low 139 with one, so neither displaces GLM, SWE or DeepSeek. Luna draws clean boards but breaks the stops, and Opus 5.5 low holds every stop but leaves its temporary model behind. Opus 5.5 low drew nothing until the operator allowed a new file in drafts of the Barter team plan. The run README section 8 has the detail. The operator chose Claude Opus 5.5 medium for a full run of all 54 FigJam scenarios and stopped it after 24. It drew 20 boards covering all seven types, and seven scenarios rightly drew nothing. The run README section 8.3 has the detail.

On the operator's request one fresh Opus 5.5 medium judge then compared each gallery type image with the best boards of the day. It kept six and swapped the state image for Opus 5.5 medium's FJR-005 board, which has no crossing exit and one clear focus but no composite zone.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Created | The driver, the batch script, 21 runs with replies, transcripts and exports, renders, grades, `results.jsonl`, the aggregator and the README |
| sk-create-figjam/assets/screenshots/ | Modified | The seven type images and the gallery README's captions |
| sk-create-figjam/README.md, README.md | Modified | Gallery captions that describe the new boards |
| benchmark/reports/README.md | Modified | The run's row |
| sk-create-figjam/references/flow-mode.md, sk-create-figjam/SKILL.md | Modified | The named-delete rule and the missing `fileKey` recovery |
| sk-create-figjam/manual-testing-playbook/ | Modified | The PASS lines of seventeen scenarios, which now need every expected signal, the root Section 3 note and the FJ-027 and FJ-028 signals |
| sk-create-figjam/assets/compose-board.js, sk-create-figjam/scripts/compose_board.py, sk-create-figjam/scripts/compose-trace.mjs | Modified | Gantt dependency arrows, ER end marks and their self-test check |
| sk-create-figjam/references/types/, sk-create-figjam/assets/examples/state-roamstay-booking.md | Modified | The gantt, ER and state guidance and the guarded state example |
| claude project/, SYNC.md, changelog/, version files | Modified | The hand-written mirror, the maintenance note and the v1.0.4.0 release |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/run/ | Modified | The Codex and Claude Code backends, the two batch scripts and a redaction list for new draft files |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The adaptive driver sent each scenario's scripted turns through the Devin runner, one run at a time on the fictional test file, with the model order rotated per scenario. No run needed an adaptive or a supplementary turn. Each scenario was rendered, redacted, scanned and pushed as soon as its three runs finished, so the public repository grew with the batch.

Three readers answered every board's questions from its colour render, and seven graders scored one type each across the three models. Every grader claim that moved a verdict was checked against the evidence before it was used. GLM's FJ-024 delete is confirmed in its export. SWE's FJ-022 page read does list ten same-title boards. GLM's FJ-023 calls all lack a file key, and only SWE left files in `/tmp`. Two graders read the scorecard's "every count true" two ways, so one Reply point was reconciled and both scores are kept. `run/aggregate.py` rebuilds `results.jsonl` from the grader files byte for byte.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| All three models on Devin at max (ADR-001) | The operator asked for Devin first, and llmgateway refuses `max` for GLM 5.3 Flash |
| One adaptive operator for every run (ADR-002) | Only the model differs between runs |
| Sonnet 5.5 graders and readers (ADR-003) | No model grades its own boards |
| The gallery rule (ADR-004) | Fixed before the runs, so no board was picked by taste, then amended to rank the board points first |
| Reopen this phase for the findings (ADR-005) | The operator chose it, and that a missing expected signal fails a board scenario |

The remaining calls were judgement, recorded here for the operator to check:

| Judgement call | Why |
|----------|-----|
| GLM's FJ-023 kept as its result, not rerun | Its calls left out the file key, a model fault and not a transport failure |
| Readers rotated across the models | Every reader still sees one board per scenario, and no reader's skill lands on one model |
| SWE's FJ-022 Reply point reconciled to 2 | The FJ-023 grader scored the same undercount as no loss twice, and the brief counts earlier boards against no model |
| A strict verdict kept beside the PASS line | The root playbook's rule and the scenarios' PASS lines disagree on three runs |
| A grader's rank breaks a tie the gallery rule leaves | No run used an extra turn, so ADR-004's turn tie-breaks never separated two boards |
| SWE 2 Max recommended over GLM on a tied score | GLM's delete changed a file it did not own, and no score margin repays that |
| Overview renders committed in `renders/` | The grades cite them, and earlier runs that did not keep them could not be checked |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Runs | 21 of 21 completed, every turn answered by the model asked for |
| Grades | 21 scorecards in `results.jsonl`, rebuilt byte for byte by `run/aggregate.py` |
| Leak scan | 0 hits on every committed file apart from the repository owner's name in the root README's existing badges |
| Packet gates | `run_gates.sh` with the upstream root set: all 15 pass, exit 0 |
| Composer and checker | `compose_board.py --self-test` 1029 of 1029, `--design-check` 0 warnings with 2,869 characters left, `flow_check.py --self-test` 158 of 158, `scripts/tests` 18 passed |
| Live check | Gantt 147:5390 and ER 148:5423 on the test file, 0 warnings, arrows and crow's-foot marks in both renders |
| Project gates | `validate_parity.py product-owner` PASSED 65/65, `residency_check.py product-owner` PASSED, output format gate passed |
| Review | A DeepSeek V4.1 Flash max review, then two fresh Opus medium reviewers. Every confirmed finding was fixed |
| Spec validation | `validate.sh --strict` on this folder and the parent: RESULT: PASSED |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **GLM runs on Devin, not llmgateway.** llmgateway accepts at most `high` for GLM 5.3 Flash, so the max variant ran through Devin.
2. **One run per model per scenario.** A single run cannot separate a model's habit from chance. The tie between GLM and SWE is within one grader's judgement call.
3. **The six findings are fixed, not rerun.** No scenario was run again on the fixed skill, so the scores above measure the skill as it was. The gallery's four redrawn boards come from their best run's model: gantt and ER show the arrows and the end marks, and the two harder boards the design file. No grader scored the redraws.
4. **Ten test boards are gone from the test file.** GLM deleted them on FJ-024. Their renders were taken first and Figma's version history holds the file before the delete.
5. **42 exports keep the redaction loss.** Their raw copies were gone, so text the runner's URL pattern cut after a URL is lost there. The replies, transcripts and grades were never affected.
6. **A gantt arrow can cross a bar end.** Each arrow drops into the middle of the top of the bar that waits, so it crosses the end of any bar in between that ends on that date. The design-to-build arrow drops on 23 November, the middle of the build bar, and crosses the end of the Sync engine bar, which ends that day. `references/types/gantt.md` tells the reader to follow an arrow from the bar its tail leaves.
7. **The Luna and Opus 5.5 low grades rest on one grader.** It also scored Clarity from the renders itself, where the first run had three fresh readers.
8. **The full run stopped at 24 of 54 scenarios and was not graded.** FJ-016 to FJ-045 did not run. The driver's extra yes turns carried six check and offer scenarios past the stop they grade, and FJ-004 reported a Project template copy the check skipped, which is not yet looked into.
<!-- /ANCHOR:limitations -->

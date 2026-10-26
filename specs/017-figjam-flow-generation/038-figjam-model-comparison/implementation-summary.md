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

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Created | The driver, the batch script, 21 runs with replies, transcripts and exports, renders, grades, `results.jsonl`, the aggregator and the README |
| sk-create-figjam/assets/screenshots/ | Modified | The seven type images and the gallery README's captions |
| sk-create-figjam/README.md, README.md | Modified | Gallery captions that describe the new boards |
| benchmark/reports/README.md | Modified | The run's row |
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
| The gallery rule (ADR-004) | Fixed before the runs, so no board was picked by taste |

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
| Spec validation | `validate.sh --strict` on this folder and the parent |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **GLM runs on Devin, not llmgateway.** llmgateway accepts at most `high` for GLM 5.3 Flash, so the max variant ran through Devin.
2. **One run per model per scenario.** A single run cannot separate a model's habit from chance. The tie between GLM and SWE is within one grader's judgement call.
3. **Six findings wait for a later phase.** The run README's Section 7 records them: a delete that needs a named yes, the two verdict rules, a gallery rule that ranks on more than the board, the driver's compose check, the misleading missing-key error and three composer limits every reader met.
4. **Ten test boards are gone from the test file.** GLM deleted them on FJ-024. Their renders were taken first and Figma's version history holds the file before the delete.
<!-- /ANCHOR:limitations -->

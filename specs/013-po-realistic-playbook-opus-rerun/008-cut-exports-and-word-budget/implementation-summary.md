---
title: "Implementation Summary: Phase 8, cut the exports and set a word budget"
description: "The 78 benchmark exports lost 22.7% of their words with every protected fact kept, and the rules now give each artifact kind a word budget taken from them."
trigger_phrases:
  - "implementation summary"
  - "cut exports word budget"
  - "second conciseness pass"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget"
    last_updated_at: "2026-09-26T12:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Committed Product Owner bb9210f and Barter 0b08add1, pushed Product Owner"
    next_safe_action: "None for this phase; the kernel v0.19.0 review and deployment stay with the operator"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-008-cut-exports-and-word-budget"
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
| **Spec Folder** | 008-cut-exports-and-word-budget |
| **Completed** | 2026-09-26 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The benchmark exports now read 22.7% shorter, from 73,942 words to 57,138, and nothing a reader acts on was lost. The rules give each artifact kind a word budget, so a new run has a length to aim at rather than only a line cap.

### Phase 8: cut the exports and set a word budget

A bundle task runs at most 500 words, a subtask 750, any other task 900, a bug 800, an Epic 1,000, and a Story or a Doc 1,400, counted outside code. An artifact goes over only when supplied values, requirements or criteria need the room. 68 of the 78 cut exports fit.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `export/benchmark/**` | Modify | 78 exports cut in two rounds |
| `sk-product-owner/SKILL.md`, `claude project/Custom Instructions.md` | Modify | The budget on line 276 and line 90, skill 0.16.0, kernel v0.19.0 |
| `sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` | Modify | The budget in the Size band row, root 2.4.0.0 |
| `sk-product-owner/changelog/v0.16.0.0.md`, `SYNC.md`, both READMEs, `description.json`, `sk-product-owner/README.md` | Create, Modify | Versions and the pending kernel review |
| The run's `README.md` | Modify | Second edit section and next steps |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Seven Opus 5.5 writers cut the files in balanced groups against a snapshot. Round one reached 14.9%, so the operator chose a second round at the depth one group had shown. Seven fact reviewers then read every file against its snapshot, and the writers repaired each finding.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| A second round at 22 to 25%, not a push to 30% | Round one showed six of seven writers stopping near 12%, and one reaching 25% by tightening requirement wording. The operator chose that depth over merging conditions or trimming template sections |
| Table body rows open to tightening, headers and row counts fixed | Tables held 5% of the words, and every value in them stays under the script's value checks |
| Doc label and Status dashes kept | The Doc template prescribes them at `doc-templates.md` lines 69 and 136 to 140, and the operator chose to match it |
| Six review findings left as cut | Color, such as which users complained most, and a subtask restating context its parent still carries fall inside the operator's depth |
| A separate subtask budget of 750 | Subtasks written from a supplied parent run 686 to 733 words, while tasks inside a Story bundle stay under 460 |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `scratch/verify_cut.py` identity run and planted faults | 78 of 78 pass at 0%; dropped Given/When/Then, dropped number and changed heading caught |
| `scratch/verify_cut.py --all`, final | 78 of 78 passed, 73942 to 57138 words, 22.7%, 5 About openings KEPT |
| Fact reviews, `scratch/fact-review-g1.md` to `-g7.md` | 81 findings: 75 restored, 6 allowed |
| Format gate on sources and each export | 40 sources pass, 78 exports 0 failures |
| `validate_parity.py product-owner`, `run_residency.sh product-owner` | PASSED 38/38, PASSED |
| Playbook validator | PASS, 46 scenarios, 0 violations |
| `run/selftest.py`, collector dry run | 7 of 7; all 78 edited files kept |
| Commits and pushes | Product Owner `e042272..bb9210f`; Barter `c6493c1b..0b08add1`, its commit skipping mirror-parity once on the operator's approval for a parallel session's drift in Code_Environment, its push passing every hook |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The budget is unmeasured.** No scenario reran, so nothing shows the runtimes write to it.
2. **Ten exports run over their budget.** Eight run 6% or less over. The partner onboarding Epic and the promotion stacking Doc run about 23% over, and were also the longest of their kind before the cut.
3. **The kernel review is stale.** The operator reviewed v0.18.0, and v0.19.0 adds the budget, so `validate_parity.py --reviews` fails until the operator confirms the new text.
<!-- /ANCHOR:limitations -->

---

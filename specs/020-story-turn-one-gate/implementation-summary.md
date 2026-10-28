---
title: "Implementation Summary"
description: "An explicit Story command now asks first on turn 1 however complete the sources look: 4 of 4 Pi reruns of PST-003 and PST-004 asked, where the earlier runs drafted. The reply linters in five systems now report only real blockers."
trigger_phrases:
  - "story turn one gate implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "020-story-turn-one-gate"
    last_updated_at: "2026-10-28T09:07:55Z"
    last_updated_by: "template-author"
    recent_action: "Initialize continuity block"
    next_safe_action: "Replace template defaults on first save"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-020-story-turn-one-gate"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.4 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 1 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 020-story-turn-one-gate |
| **Completed** | 2026-10-28 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

An explicit `$s` or `$story` now asks its question on turn 1 even when the sources answer everything. In four Pi reruns of PST-003 and PST-004 on DeepSeek V4.1 Flash high, every turn 1 asked and drafted nothing, where both scenarios drafted on turn 1 before on both Devin and Pi.

### Story turn-one gate and reply linter fixes

You no longer get a finished Story before you have had a chance to correct the reading. The question an explicit command asks always keeps its Validation field, what the model is likely to assume wrongly, because no source can answer that. So the question never collapses to nothing when the sources look complete. The same rule now sits in the kernel, `AGENTS.md`, `SKILL.md`, the Story and Doc question templates and Story Mode, in the skill and in its Project mirror.

The reply linters now report only real blockers. The Product Owner linter skips the `TBD...` Delivery placeholder the Human Voice card grants, and all five systems' linters match a phrase as whole words, so "acts as" no longer fires inside "contacts as" and "bij deze" no longer fires inside "bij dezelfde".

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `claude project/Custom Instructions.md`, `AGENTS.md`, `sk-product-owner/SKILL.md` | Modified | The rule, kernel v1.2.16 |
| `sk-product-owner/assets/interactive-response-templates.md`, `sk-product-owner/references/story-mode.md` and their two Project mirrors | Modified | Validation field kept, Step 1 closed |
| `benchmark/grader/hvr_lint.py` | Modified | `TBD...` exemption, bounded phrases |
| Copywriter, Deal Templates, Sales HubSpot and Sales Direct Communication linters, Sales `export_blockers.py` | Modified | Bounded phrases |
| Version files, `changelog/v1.0.16.0.md`, `sk-product-owner/changelog/v1.2.6.0.md`, `SYNC.md`, both READMEs | Modified, Created | Release |
| `mcp-figma/`, `mcp-click-up/`, `vendor.json` | Modified | Vendor pull the vendor sync gate asked for |
| `sk-create-figjam/assets/screenshots/README.md` | Modified | A bullet the format gate failed on |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The cause came from the model's own reasoning in the earlier Pi run of PST-004, which quoted the template's "Populate only unresolved fields" and concluded the question collapses when every field is resolved. The fix gives the question a field no source settles. The gates ran in all five systems, then PST-003 and PST-004 ran twice each on Pi from the release tree, and a deterministic check read each turn. Product Owner shipped in commits 0000187 to 0000189.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Keep the Validation field rather than add a playback | A playback of the settled facts is the recap the grader already flagged, while the Validation field is a real question no source answers |
| Rule PST-002 a FAIL under the existing rule | Story Mode already keeps unknown Delivery values as `TBD...` rather than an inferred exclusion, so a new rule would only restate it |
| Fix the substring defect in all five linters | The same matching sat in every copy and in the Sales export gate, and one fix ships for the whole class |
| Shorten the `SKILL.md` sentence | The full sentence pushed `SKILL.md` to 5,026 words against the 5,000 cap of the packet contract |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `bash benchmark/gates/run_gates.sh` | PASS, all 15 gates pass |
| Output format gate `--system product-owner` | PASS across 72 source files |
| Sync Loop residency and pair divergence | PASS, 7 systems and 208 pairs |
| Sibling gates | PASS, Copywriter all 4, Deal Templates all 7, Sales HubSpot exit 0, Sales Direct Communication gates and export blocker check |
| `validate_parity.py product-owner` | PASS, 65 of 65 declared pairs after the outer mirror commit |
| Pi rerun, PST-003 and PST-004 twice | PASS, 4 of 4 turn 1 replies ask with a Validation line and no `## Problem`, 4 of 4 turn 2 replies draft Problem and Acceptance criteria, 8 of 8 replies lint clean |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Turn 1 only was proven.** The rerun checks that turn 1 asks and turn 2 drafts, with no full grade of the turn 2 Stories. Their fidelity slips from the earlier runs, such as the reworded `5 attempts`, are not rechecked.
2. **Some questions still carry a recap.** Three of the four turn 1 replies open with a sentence on what the sources settle before the questions, which the kernel's "the question and nothing else" rule discourages.
3. **The live claude.ai Project is not updated.** Kernel v1.2.16 and the two changed Knowledge files wait for the operator's paste.
4. **The continuity block keeps its scaffold defaults.** The save writer requires a packet pointer with a track and a packet segment, and this repository's specs root is flat, so `020-story-turn-one-gate` is refused with MEMORY_003. `validate.sh --strict` therefore reports one error, SCAFFOLD_NEVER_TOUCHED, which the operator chose to record here rather than hand-write the block or change the writer.
<!-- /ANCHOR:limitations -->

---

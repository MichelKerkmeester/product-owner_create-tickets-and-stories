---
title: "Implementation Summary"
description: "Add the draw-ready threshold, the ordered stop rule and the energy cap."
trigger_phrases:
  - "draw ready stop rule implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/031-round-three-apply/002-draw-ready-stop-rule"
    last_updated_at: "2026-10-21T10:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Applied the change and ran every gate"
    next_safe_action: "The operator gives the commit go-ahead"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
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
| **Spec Folder** | 002-draw-ready-stop-rule |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Add the draw-ready threshold, the ordered stop rule and the energy cap. Draw when no row is unasked, the reader and question are settled, at most two rows are assumed and each names its settlement. Stop asking on the first of: complete and confirmed, two consecutive rounds that change no row, a user stop, or the energy cap. Quick is zero rounds, Standard three, Deep five. At the cap the packet draws with the assumed rows named or takes the no-route branch and offers a table. The cap counts rounds, not questions, which is why a per-call width limit is not it.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| sk-create-figjam/references/flow-mode.md | Modified | Add the draw-ready threshold, the ordered stop rule and the energy cap |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

A read-only DeepSeek V4.1 Flash worker at max through cli-pi on llmgateway proposed exact edits as JSON. The orchestrator reviewed them, applied them with a script that refuses missing or repeated old text and hand-mirrored or regenerated the Project files. Nothing is committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Apply the ranked change as the synthesis words it | The operator adopted all thirty-two changes |
| Every question states a reading and a recommendation | The operator's rule for this phase outranks the research's rule that the reader and the question are never assumed |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| The change | Applied to sk-create-figjam/references/flow-mode.md: draw when no row is unasked, the reader and question are settled, at most two rows are assumed and each names its settlement. Stop asking on the first of: complete and confirmed, two consecutive rounds that change no row, a user stop, or the energy cap. Quick is zero rounds, Standard three, Deep five. At the cap the packet draws with the assumed rows named or takes the no-route branch and offers a table. The cap counts rounds, not questions, which is why a per-call width limit is not it |
| Review of the worker's edits | Reviewed against the operator's rule that every question carries the AI's reading and a recommended answer and never dead-ends. The Thinking line was merged by hand with phase 8's Quick energy wording, because both rewrote it |
| Gates on the final tree | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the playbooks passed at 51 scenarios with 0 warnings and 48 scenarios at the 37 baseline warnings, the topology check passed, the three skill packages validated, the plugin rebuilt to 375 files and validates, the flow_check self-test passed 154 of 154, the router passed 141 of 141 fixtures and 219 of 219 differential inputs, check_hub passed 37 gold rows, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. No live board has been written, so the change is untested against the hosted Figma MCP until it is connected.
<!-- /ANCHOR:limitations -->

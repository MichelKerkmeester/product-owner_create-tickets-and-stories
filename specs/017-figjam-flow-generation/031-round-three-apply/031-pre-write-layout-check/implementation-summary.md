---
title: "Implementation Summary"
description: "Measure the graph before the write, not after."
trigger_phrases:
  - "pre write layout check implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/031-round-three-apply/031-pre-write-layout-check"
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
| **Spec Folder** | 031-pre-write-layout-check |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Measure the graph before the write, not after. The same parse also reports rank width, edges per node, longest path, total label characters against the 40 character cap already held in `MAX_LABEL_CHARS`, and an estimate of edge pairs that must cross. A number out of band is fixed in the model before a write is spent.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| sk-create-figjam/scripts/figjam_checks/layout.py | Modified | Measure the graph before the write, not after |
| sk-create-figjam/scripts/flow_check.py | Modified | Measure the graph before the write, not after |
| sk-create-figjam/scripts/figjam_checks/fixtures.py | Modified | Measure the graph before the write, not after |
| sk-create-figjam/references/quality-rubric.md | Modified | Measure the graph before the write, not after |
| sk-create-figjam/assets/examples/ (three quoted check lines) | Modified | Measure the graph before the write, not after |
| sk-create-figjam/SKILL.md | Modified | Measure the graph before the write, not after |
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
| The change | Applied to sk-create-figjam/scripts/figjam_checks/layout.py, sk-create-figjam/scripts/flow_check.py, sk-create-figjam/scripts/figjam_checks/fixtures.py, sk-create-figjam/references/quality-rubric.md, sk-create-figjam/assets/examples/ (three quoted check lines), sk-create-figjam/SKILL.md: the same parse also reports rank width, edges per node, longest path, total label characters against the 40 character cap already held in `MAX_LABEL_CHARS`, and an estimate of edge pairs that must cross. A number out of band is fixed in the model before a write is spent |
| Review of the worker's edits | Reviewed against the operator's rule that every question carries the AI's reading and a recommended answer and never dead-ends. The three examples' quoted check output and the packet SKILL.md module list were refreshed to carry the layout measures |
| Gates on the final tree | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the playbooks passed at 51 scenarios with 0 warnings and 48 scenarios at the 37 baseline warnings, the topology check passed, the three skill packages validated, the plugin rebuilt to 375 files and validates, the flow_check self-test passed 154 of 154, the router passed 141 of 141 fixtures and 219 of 219 differential inputs, check_hub passed 37 gold rows, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. No live board has been written, so the change is untested against the hosted Figma MCP until it is connected.
<!-- /ANCHOR:limitations -->

---
title: "Implementation Summary"
description: "Common pair phrasings now keep the board beside the artifact, and write a doc or write a bug now frames its artifact, so a Doc or Bug asked for with a board no longer loses the artifact to FLOW."
trigger_phrases:
  - "pair phrasing and framing implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/029-extension-fixes/002-pair-phrasing-and-framing"
    last_updated_at: "2026-10-21T09:30:00Z"
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
| **Spec Folder** | 002-pair-phrasing-and-framing |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Common pair phrasings now keep the board beside the artifact, and write a doc or write a bug now frames its artifact, so a Doc or Bug asked for with a board no longer loses the artifact to FLOW.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| benchmark/router/route_contract.py, fixtures.json | Modified | The second-output opener and joiners, the doc noun and the bug frame, twelve fixtures |
| benchmark/hub-routing-cases.json | Modified | Two gold rows |
| sk-product-owner/references/router-contract.md, routing.md | Modified | The contract copy and step 5 prose |
| claude project/Custom Instructions.md | Modified | The kernel router copy |
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
| One phase for two findings | Both change the same three router copies |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| The change | route_contract.py forms the pair after then, and then, also and a sentence break and for a board joined with plus or and, frames a bare doc and write, file or log a bug about or for. Twelve fixtures were added and pass 141 of 141, the differential passes 219 of 219 so the three router copies agree, and check_hub.py passes 37 gold rows including a Doc pair and a Bug pair |
| Review of the worker's edits | The worker changed the oracle, fixtures and gold rows only. The orchestrator ported the three pattern changes into router-contract.md and the kernel and updated routing.md step 5 and the contract's comment. A task about FigJam board export still routes TASK with no then |
| Gates on the final tree | run_gates.sh all 12 gates pass. The format gate passes on 70 source files with 38 advisory warnings, the baseline count, and reference-parity.cjs is byte-identical. Router fixtures pass 141 of 141, the differential 219 of 219 and check_hub.py 37 gold rows, and the flow_check self-test passes 149 of 149. The playbook validator passes sk-create-figjam with 47 scenarios and 0 violations, and sk-product-owner with 48 scenarios and the baseline 37 warnings. validate_skill_package.py --strict passes on the hub and both packets, and the plugin rebuilds to 370 files and validates. In the scratch clone run_parity passes 62 of 62 pairs and run_residency passes for Product Owner |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. A board asked for before the artifact, as in make a figjam flow and then write a story, still routes to the artifact first, as it did before.
<!-- /ANCHOR:limitations -->

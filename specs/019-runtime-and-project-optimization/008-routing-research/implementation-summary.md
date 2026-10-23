---
title: "Implementation Summary"
description: "Ten DeepSeek iterations on routing, mode links, README currency, dead files and sk-code-skilled alignment, with the key claims spot-checked."
trigger_phrases:
  - "routing research implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/008-routing-research"
    last_updated_at: "2026-10-21T17:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Ran and checked the routing research"
    next_safe_action: "The operator picks which findings a fix phase takes"
    blockers: []
    key_files:
      - "research/lineages/deepseek/research.md"
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
| **Spec Folder** | 008-routing-research |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

One cli-pi DeepSeek V4.1 Flash max lineage ran ten iterations, one question each, and wrote `research/lineages/deepseek/research.md` with 88 findings. The verdict: the routing code is sound and gated, but three stage-one sources state routing with no precedence, two leaf maps are never compared, seven mode hand-offs are undefined or contradictory, no dead code or dead document exists, and the code lints clean with documentation-level deviations from sk-code-skilled.

### Spot checks

| Claim | Result |
|-------|--------|
| The plugin build copy of `router-contract.md` lacks the just do it branch | Confirmed, 3 matches against 4 in the source |
| `benchmark/gates/README.md` says 33 gold rows | Confirmed, the file holds 37 |
| `README.md` and `benchmark/router/README.md` say four guards | Confirmed, `differential.py` runs four checks plus the per-input comparison |
| `DEFAULT_RESOURCE` in `router-contract.md` is read by nothing | Confirmed for `route_contract.py` |
| The resolver never emits Deep or Raw | Confirmed, `route_contract.py` emits only QUICK besides the default |
| Kernel Section 10 is empty | Confirmed, six lines |
| `sk-product-owner/README.md` miscounts examples as 20 | Partly. The table counts the 20 on fictional products and line 472 states 21 with 20 fictional |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The run was staged in the outer repository at `specs/z-staging-po-019s`, as the earlier reviews were, and ran through `fanout-run.cjs` with the stop policy at max-iterations and convergence off. It was copied here without the containment snapshots, home-directory path prefixes were removed and the staging folder was deleted.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Read only | Fixes wait for the operator to pick them |
| Seven claims checked by hand | A lineage verdict is a claim until a check confirms it |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Runner exit | `fanout exit 0`, 1 lineage succeeded, 0 failed |
| Iterations | 10 of 10 written and verified by `verify-iteration.cjs` |
| Private paths | Only the staging path and the exclusion rule named outside paths, and the home prefix was removed |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The P0 hand-off table and the kernel trim estimate were not checked line by line.** They are the lineage's claims.
2. **Which stage-one source should be the authority is an owner decision.**
<!-- /ANCHOR:limitations -->

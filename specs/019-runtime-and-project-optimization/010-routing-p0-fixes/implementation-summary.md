---
title: "Implementation Summary"
description: "hub-router.json as the executed stage-one authority, artifact requests winning over an opening tool word, and every P0 finding of the 008 research fixed and verified."
trigger_phrases:
  - "routing p0 fixes implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/010-routing-p0-fixes"
    last_updated_at: "2026-10-21T17:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Fixed and verified the P0 findings"
    next_safe_action: "The operator reviews kernel-changes.md and approves the commit"
    blockers: []
    key_files:
      - "hub-router.json"
      - "benchmark/gates/check_hub.py"
      - "kernel-changes.md"
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
| **Spec Folder** | 010-routing-p0-fixes |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

### Findings

| Finding | Outcome |
|---------|---------|
| Stage-one authority | Fixed. `hub-router.json` holds six ordered rule entries that `check_hub.py` executes, first match wins, and the self-test fails a reordered or missing rule. The hub `SKILL.md` summarizes and points to it |
| Tool word plus artifact request | Fixed. An artifact request rule runs before the opening-signal rule. 41 gold rows, `cupt list my open tasks` still routes to `mcp-click-up` |
| `DEFAULT_RESOURCE` | Fixed, the router copies match `ROUTER.md` |
| Unloadable ALWAYS entry | Fixed, removed from all three router copies |
| Seven hand-offs | Fixed. One owner per contract, pointers elsewhere, eight paired playbook scenarios per runtime. The resolver now emits Deep and Raw |
| Leaf maps | Fixed. A lane crosswalk and `check_leaf_map_parity.py` cover every lane including FLOW. 15 gates |
| Kernel Section 4 drift | Fixed, `differential.py` compares the kernel's commands and energy signals with the contract both ways. 234 inputs |
| Section numbering | Fixed, Router Code is Section 10 |

### Corrections made here after the dispatch

- The Flow pairing sequence (artifact first, the reply ending on the board gate with no ClickUp offer, Flow running on the artifact under its own check and yes) had been reduced to a pointer whose target did not carry it. It now opens Section 8 Delivery in `sk-create-figjam/references/flow-mode.md` and its Project mirror
- Two historical changelog entries, `v0.17.1.0` and `v0.17.2.0`, were restored, because they record the kernel as it was
- The Sync Loop declaration followed the moved and reworded text: the router row names Section 10, the Processing statement follows its mirror, and two omission entries whose lines the mirrors now carry were removed
- Mirror references to kernel section numbers now name the Router Code and the Delivery Protocol, since `ClickUp Handoff` named no kernel heading

### The add verb

On 2026-10-22 the owner chose that add counts as a creation verb only when an indefinite opener follows it: a, an, new or another. `hub-router.json` holds add in `artifact-request-indefinite-verbs` and the openers in `artifact-request-indefinite-openers`, and `check_hub.py` reads both. `cupt add the task to the sprint` routes to `mcp-click-up`, `cupt add a task for the login bug` to `sk-product-owner`, and both are gold rows, now 41. A request that names a task without opening on a tool, such as `add the task to the sprint with cupt`, still starts in `sk-product-owner` through the older artifact-word rule.
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

`codex exec --model gpt-6-luna -c model_reasoning_effort="max" -c service_tier="fast"` ran in the Product Owner root with the child-dispatch preamble, the code persona and the two owner decisions. A snapshot taken first scoped the diff, and every removed source line was checked for a surviving owner.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| `hub-router.json` is the stage-one authority | The owner chose it on 2026-10-21. The gate executes it, so prose cannot drift from it |
| An artifact request wins over an opening tool word | The owner chose it, so a request never loses the artifact it asks for |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `differential.py` | PASSED 234/234 |
| `run_gates.sh` | All 15 gates pass |
| Stage-one probes | Both new gold cases route to `sk-product-owner`, the cupt and figma-ds-cli tool rows keep their packets |
| Stage-two probes | Story with `then: FLOW`, Deep, Raw, Quick and just do it resolve as documented |
| Format gate | Pass across 70 source files |
| `residency_check.py product-owner` in the scratch clone | PASSED |
| `validate_parity.py product-owner` in the scratch clone | Only the `quality-scoring.md` review open since 018 |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No live Project or CLI run.** The playbook scenarios are written, not run.
2. **The consolidation leans on Knowledge pointers** for the Story bundle reply and the Flow pairing, each read only in its own routed mode.
<!-- /ANCHOR:limitations -->

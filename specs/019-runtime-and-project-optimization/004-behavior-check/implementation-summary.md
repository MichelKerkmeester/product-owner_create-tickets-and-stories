---
title: "Implementation Summary"
description: "The optimized Project package held every baseline verdict, and the one Flow failure it exposed got a one-clause kernel fix."
trigger_phrases:
  - "behavior check implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/004-behavior-check"
    last_updated_at: "2026-10-21T23:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Ran the Project playbook on the optimized kernel and fixed the Flow no-connector reply"
    next_safe_action: "The operator reviews the kernel and approves the Product Owner commit"
    blockers: []
    key_files:
      - "benchmark/reports/2026-10-21--kernel-dedupe--deepseek-v4-1-flash-high/README.md"
      - "claude project/Custom Instructions.md"
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
| **Spec Folder** | 004-behavior-check |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The baseline is the 2026-10-01 kernel-diet run, the last Project run on a changed kernel. Its scenario set ran again on the optimized kernel with the same model and thinking level, plus `PFL-001`, which that run predates. The report is `benchmark/reports/2026-10-21--kernel-dedupe--deepseek-v4-1-flash-high/README.md`.

- **Ask-first:** 12 of 12, the same as the baseline, across `PTK-006`, `PST-001` and `PEP-002` four times each, with every turn 2 carrying its required values.
- **Other baseline scenarios:** `PID-001`, `PBG-001`, `PIR-001`, `PIR-002` and `PDK-001` pass, as in the baseline.
- **PFL-001:** failed on turn 1 with a `Read-back:` line and nothing written. The pre-phase kernel failed it too, 0 of 3, by asking intake questions, so the cut changed the failure's form rather than causing it. One clause in the kernel's no-connector bullet took it to 2 of 3.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `benchmark/reports/2026-10-21--kernel-dedupe--deepseek-v4-1-flash-high/` | Created | The runner copy, the replies and the report |
| `claude project/Custom Instructions.md` | Modified | The no-connector clause, 56 bytes |
| `SYNC.md` | Modified | A dated note for the clause |
| `z — Claude Project Sync Loop/systems.py`, in the outer repository | Modified | The Section 9 residency statement resynced |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Each runner process ran alone, since parallel processes share one sandbox path. The first pass met a spent `opencode-go` quota, a 429 on every call, so the run moved to `llmgateway` for the same model, and the refused attempts are kept in `transport-429/`. The runner copy needed one harness fix, because it took the first `sk-` folder in a root that now holds two packets. The pre-phase kernel ran from a scratch copy of the system, so the live tree never held it again.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Same model and thinking level as the baseline, on another provider | It keeps the comparison on the kernel, and only the route to the model changed |
| Run PFL-001 on both kernels before fixing | A single failing sample cannot tell a regression from an old defect |
| Fix the kernel only | The skill reaches Figma through Code Mode and has no no-connector case |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Ask-first samples, four runs of three scenarios | 12 of 12 ask on turn 1, 12 of 12 drafts carry the required values |
| The five other baseline scenarios | 5 of 5 PASS |
| PFL-001 on the old, cut and fixed kernels, three samples each | 0 of 3, 0 of 3 and 2 of 3, every fixed-kernel model passing `flow_check.py` |
| `differential.py`, `run_gates.sh`, format gate | 219/219, all 12 gates, 70 source files |
| `residency_check.py product-owner` in the scratch clone | PASSED after resyncing the one statement |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **PFL-001 still fails one sample in three.** It asks the reader question on turn 1. The pre-phase kernel did so in every sample, because Flow Mode Delivery opens a run with intake rounds, and the scenario's no-question line and that rule pull against each other.
2. **One model and one grader.** No second grader read the replies.
<!-- /ANCHOR:limitations -->

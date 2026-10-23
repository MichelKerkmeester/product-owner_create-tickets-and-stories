---
title: "Implementation Summary"
description: "Every P1 and P2 finding of the 008 routing research fixed through cli-codex GPT 6 Luna max fast and verified here."
trigger_phrases:
  - "routing research fixes implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/009-routing-research-fixes"
    last_updated_at: "2026-10-21T17:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Fixed and verified the P1 and P2 findings"
    next_safe_action: "The operator reviews the kernel trim ledger and decides the P0 stage-one authority"
    blockers: []
    key_files:
      - "kernel-trim-ledger.md"
      - "benchmark/gates/check_markdown_links.py"
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
| **Spec Folder** | 009-routing-research-fixes |
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
| Gold rows stated as 33 | Fixed to 37 in the gates README and the playbook |
| Four guards | Fixed, both READMEs describe the five checks `differential.py` runs |
| Stale plugin build | Rebuilt, and a plugin build freshness gate added to `run_gates.sh` |
| No link check | A markdown link integrity gate, `benchmark/gates/check_markdown_links.py`, added. Placeholder targets such as `figma-url` are skipped, so the worked examples keep their placeholder links |
| Kernel size | Trimmed from 70,010 to 67,971 bytes, Section 11 unchanged, ledger in `kernel-trim-ledger.md` |
| Remaining README counts and the corpus group name | Fixed, the group is now `quick-energy-and-false-prefixes` and the example count reads 20 Fictional Worked Examples |
| Unread config entries | `toolSurface.workspaceWrites` removed. The other three stay because code reads them or the parent-hub schema requires them, and `mode-registry.json` says so |
| `routing.md` with no lane | Marked detail-only in the packet `SKILL.md`, and the hub release note is linked from the root README |
| sk-code-skilled deviations | Strict mode in the format validator, 59 long Python lines wrapped, return types in `hvr_lint.py`, a comment in each shell script that omits `set -e` |
| The P0 findings | Not changed, the stage-one authority is the owner's decision |

### Corrections made here after the dispatch

- Codex wrapped the example placeholder links in code formatting, which would teach the model to print backticked links. The 16 example files were restored and the link gate learned to skip placeholder targets instead
- The new link checker carried a doubled shebang line, removed
- The upstream `mcp-figma` change committed at 96b3395920 was pulled with `vendor-sync.py`, and the plugin copy was rebuilt
- Residency row for the removed Section 10 now names Section 6, where the Quality Scoring pointer lives
- The format validator has no byte twin: the shared Sync Loop validator is a different file that already carries strict mode, so nothing was mirrored
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

`codex exec --model gpt-6-luna -c model_reasoning_effort="max" -c service_tier="fast"` ran in the Product Owner root with workspace-write, the child-dispatch preamble and the code persona inline. A snapshot taken before the dispatch scoped the diff, and every change outside the rebuilt plugin was listed and read.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Skip placeholder link targets in the gate | Examples teach the artifact shape, so their placeholders stay links |
| Leave the P0 findings | They wait on the owner's stage-one authority decision |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `differential.py` | PASSED 220/220 |
| `run_gates.sh` | All 14 gates pass |
| Link gate on a planted broken link | Flags it and skips the placeholder |
| Format gate and format fixtures | Pass across 70 source files, all fixtures pass |
| `scripts/tests` | 18 passed |
| `residency_check.py product-owner` in the scratch clone | PASSED |
| `validate_parity.py product-owner` in the scratch clone | Only the `quality-scoring.md` review open since 018 |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The kernel trim has no retention gate.** The ledger is the record, and a human review of it is the check.
2. **Section numbers jump from 9 to 11**, because the router gate finds Section 11 by its heading.
<!-- /ANCHOR:limitations -->

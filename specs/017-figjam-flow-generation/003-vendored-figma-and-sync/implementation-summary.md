---
title: "Implementation Summary"
description: "Product Owner now carries a byte-identical vendored copy of mcp-figma with a manifest and a sync tool that detects drift both ways and moves changes with one command."
trigger_phrases:
  - "vendored figma and sync implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/003-vendored-figma-and-sync"
    last_updated_at: "2026-10-20T02:35:18Z"
    last_updated_by: "claude-code"
    recent_action: "Vendored mcp-figma and added vendor-sync.py with tests and a gate"
    next_safe_action: "Start phase 004 parent hub conversion"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-003-vendored-figma-and-sync"
      parent_session_id: null
    completion_pct: 0
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
| **Spec Folder** | 003-vendored-figma-and-sync |
| **Completed** | 2026-10-20 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Product Owner now carries its own copy of the shared figma skill, and a gate fails the moment that copy and the shared one disagree. Before this, the only way to embed the skill was to copy it by hand and hope nobody edited either side.

### Phase 3: vendored-figma-and-sync

You run `python3 scripts/vendor-sync.py status` to see whether `mcp-figma/` matches the shared skill at the commit recorded in `vendor.json`. It names every changed, added or removed file on the side that moved. `pull` takes upstream changes and refuses when you have local edits upstream does not carry. `push` writes your local edits into the shared skill's working tree and stops there, so you commit upstream yourself and run `pull` to re-baseline.

The gate runner calls `status` on every run, so drift turns a gate red instead of going unnoticed. A standalone clone of the public repo has no shared skill folder beside it, and there the gate reports SKIPPED and counts it, never as a pass.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| mcp-figma/ | Created | Vendored copy, 58 files, pulled at 293caa90 |
| vendor.json | Created | Upstream path, base commit and a sha256 per file |
| scripts/vendor-sync.py | Created | status, pull and push |
| scripts/tests/test_vendor_sync.py | Created | 7 tests against a scratch upstream repo |
| benchmark/gates/run_gates.sh | Modified | Vendor sync gate and its tests, with a counted skip |
| benchmark/gates/README.md | Modified | Documents the new gate |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The gate baseline was captured first (5 of 5 gates, parity 37/37). The copy was made by the tool's own `pull`, then checked file by file against `git show` at the base commit. The tests drive the script as a subprocess against a throwaway git repository, so the shared skill repo was never written. A one-byte edit was planted in the real copy to prove the gate goes red, then restored. Nothing is committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Push stops at the upstream working tree | Committing in the shared repo is the operator's step, and pull afterwards records the new base commit |
| Symlinks are refused on both sides | A link copies as a pointer that does not exist in a clone, so its hash would claim an equality the clone cannot reproduce |
| The upstream root is found by walking up for .skilled | Keeps any personal path out of a public repo, and VENDOR_UPSTREAM_ROOT covers other layouts |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Base-commit hash check | PASS, 58 of 58 files, 0 mismatches |
| test_vendor_sync.py | PASS, 7 of 7 |
| run_gates.sh | PASS, 7 of 7 gates, exit 0 |
| run_parity.sh | PASS, 37/37 declared pairs, exit 0 |
| Planted one-byte drift | Gate FAILED as intended, status exit 0 after restore |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No real upstream push yet.** Only the scratch upstream has received a push. Phase 008 does the first real one.
2. **Status compares working trees.** An uncommitted upstream edit shows as upstream-ahead even before it is committed, which is the intended warning.
<!-- /ANCHOR:limitations -->

---



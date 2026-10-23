---
title: "Implementation Summary"
description: "mcp-click-up is vendored into the Product Owner hub as a byte copy at 325ebb22, kept in step with .skilled by vendor-sync.py and routed at stage one by its own signals."
trigger_phrases:
  - "vendored clickup implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/012-vendored-clickup"
    last_updated_at: "2026-10-20T17:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Vendored mcp-click-up and registered it in the hub"
    next_safe_action: "Commit both repositories on the operator's go-ahead"
    blockers: []
    key_files:
      - "mcp-click-up/SKILL.md"
      - "vendor.json"
      - "mode-registry.json"
      - "hub-router.json"
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
| **Spec Folder** | 012-vendored-clickup |
| **Status** | Complete |
| **Completed** | 2026-10-20 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Product Owner now carries the ClickUp skill it pushes through, so a clone or the plugin has the transport contract with it.

### Phase 12: vendored-clickup

`mcp-click-up/` is a byte copy of `.skilled/skills/mcp-tooling/mcp-click-up`, 178 files at `325ebb22`. `vendor.json` records it and `scripts/vendor-sync.py status`, `pull` and `push` keep it in step, the same way `mcp-figma/` is kept. The hub registers it as a vendored tool packet and routes `mcp-click-up`, `cupt` and `clickup mcp` to it. Bare "clickup" is no signal, because Product Owner writes ClickUp-native artifacts.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| mcp-click-up/ | Created | Byte copy of the upstream skill |
| vendor.json | Modified | The package and its 178 file hashes |
| mode-registry.json, hub-router.json, SKILL.md | Modified | The fourth packet and its signals |
| benchmark/gates/check_hub.py | Modified | Five ClickUp gold rows |
| scripts/build-plugin.py | Modified | The plugin ships the packet |
| AGENTS.md, sk-product-owner/SKILL.md, README.md, SYNC.md | Modified | ClickUp delivery names the vendored packet |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The upstream was scanned for tokens, workspace ids and Barter text before the copy, and it already lives in a public GitHub repository. One manifest entry and one `pull` vendored it, and `diff -rq` against upstream printed nothing.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Folder named `mcp-click-up` | The upstream name, so the copy and the sync stay one to one |
| No Project mirror | A Project reaches ClickUp through its own connector |
| No edit inside the copy | It is upstream-owned, so a change goes through `push` |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| vendor-sync.py status | PASS, three packages in step |
| diff -rq against upstream | No difference, 0 symlinks |
| check_hub.py | PASS, 24 gold rows, five of them ClickUp |
| run_gates.sh | PASS, all 10 gates |
| Plugin | mcp-click-up shipped among 292 files |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The claude.ai connector was not re-checked.** The operator ruled on 2026-10-20 that the vendored skill is the truth, so Product Owner and the kernel now use its parameters: `markdown_description` for create and update, `content_format: "text/md"` for document pages and `include: ["description"]` on `clickup_get_task` for a read-back. The vendored skill checked them against the `clickup_official` schema on 2026-10-08 and says the claude.ai connector was not re-checked, so a first Project push should confirm the read-back.
<!-- /ANCHOR:limitations -->

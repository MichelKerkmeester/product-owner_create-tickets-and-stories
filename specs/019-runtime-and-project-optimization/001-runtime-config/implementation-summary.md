---
title: "Implementation Summary"
description: "The public Product Owner repo now starts Code Mode from its own configs, with the forked server and its launcher vendored and a fresh install proven."
trigger_phrases:
  - "runtime config implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/001-runtime-config"
    last_updated_at: "2026-10-21T20:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Vendored Code Mode, added the runtime configs and proved a fresh start"
    next_safe_action: "Start phase 002, kernel size"
    blockers: []
    key_files:
      - ".utcp_config.json"
      - ".mcp.json"
      - "opencode.json"
      - "scripts/code-mode.cjs"
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
| **Spec Folder** | 001-runtime-config |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A clone of the public repository now carries everything Code Mode needs. The operator chose to vendor the forked `@utcp/code-mode-mcp` server, which adds a stdout guard, a session-end exit, idle transport release and a watchdog that the npm package lacks.

- **Vendored server:** `mcp-code-mode/`, 73 files at upstream `cd30de6395`, kept in step by `vendor.json`. Its `exclude` list keeps `node_modules`, `dist` and the `mcp-server/README.md` symlink out.
- **Vendored launcher:** `scripts/vendored/code-mode/`, the upstream launcher and its Node resolver, byte for byte. `scripts/code-mode.cjs` hands them this repo's server path. The server needs Node 24, since `isolated-vm` has no later build, and the resolver finds one through nvm, fnm, volta or `PATH`.
- **Runtime configs:** `.utcp_config.json` with the `clickup_official` and `figma` manuals, and `.mcp.json` and `opencode.json`, which both run `node scripts/code-mode.cjs`.
- **Keys and ignores:** `.env.example` lists `figma_FIGMA_API_KEY`, in the prefixed form Code Mode reads. `.gitignore` keeps the build local and overrides the global ignore of the two config files.
- **`vendor-sync.py`:** a per-package `exclude` list. A plain name matches at any depth and a path matches one entry. An excluded entry is never hashed or copied, and a local build carries across a pull.
- **Gates:** `check_hub.py` lets a folder that `repoPaths` declares carry a `SKILL.md`, and `build-plugin.py` checks a vendored package with its exclude rule. The plugin still ships without Code Mode.
- **Upstream defect fixed on the way:** a fresh install crashed on start-up, because a global `js-yaml` override forced `json-schema-ref-parser` onto the wrong major. It is fixed upstream in `mcp-tooling/024`, commit `cd30de6395`.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `.utcp_config.json`, `.mcp.json`, `opencode.json` | Created | Runtime configs |
| `.env.example`, `.gitignore` | Modified | Credential key and ignore rules |
| `mcp-code-mode/`, `scripts/vendored/code-mode/`, `vendor.json` | Created, Modified | The vendored server and launcher |
| `scripts/code-mode.cjs` | Created | The repository launcher |
| `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py` | Modified | The exclude field and three tests |
| `scripts/build-plugin.py`, `benchmark/gates/check_hub.py` | Modified | Exclude-aware drift check and the repoPaths exemption, each with a self-test case |
| `mode-registry.json`, `README.md` | Modified | repoPaths entries, setup steps and the tree |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The first build came up against the upstream lockfile and crashed. The cause was traced to the override, and a scoped override was proven in a scratch copy before the operator approved the upstream commit. The approved install ran `npm ci` and the build under Node 24, and the rollback is `rm -rf mcp-code-mode/mcp-server/node_modules mcp-code-mode/mcp-server/dist`. Nothing in Product Owner is committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Vendor the fork and not the npm package | The operator chose it, because the fork's stdout guard keeps a stray log line from corrupting the MCP stream |
| Vendor the upstream launcher and add a thin repo launcher | The upstream launcher computes its server path from its own location, so a byte copy cannot point here alone |
| Prove start-up with an empty manual list | Loading the real config starts `mcp-remote`, which opens a ClickUp OAuth sign-in in the browser |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `vendor-sync.py status` | All five packages in step, mcp-code-mode 73 files at cd30de6395 |
| `node scripts/code-mode.cjs` under default Node 26, stdio `initialize` then `tools/list` | serverInfo CodeMode-MCP, and the seven tools call_tool_chain, deregister_manual, get_required_keys_for_tool, list_tools, register_manual, search_tools and tool_info |
| `.utcp_config.json` through the server's `UtcpClientConfigSerializer` | manuals clickup_official:mcp and figma:mcp, loader dotenv |
| `grep .skilled .mcp.json opencode.json` | No match |
| `.env.example` against `.utcp_config.json` | The one variable, `FIGMA_API_KEY`, appears as `figma_FIGMA_API_KEY` |
| `test_vendor_sync.py`, `check_hub.py --self-test`, `build-plugin.py --self-test` | 18 of 18, 15 of 15, 10 of 10 |
| `bash benchmark/gates/run_gates.sh`, format gate | All 12 gates pass, format passed across 70 source files |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No live ClickUp or Figma call was made.** The first ClickUp call opens an OAuth sign-in, and the figma manual needs a token in `.env`, so both are the operator's first-run steps.
2. **The launch pins are still unpinned.** `mcp-remote` and `figma-developer-mcp@latest` follow the packets' documented arguments, as phase 006 of packet 018 recorded.
<!-- /ANCHOR:limitations -->

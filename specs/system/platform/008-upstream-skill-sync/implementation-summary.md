---
title: "Implementation Summary"
description: "vendor-sync.py fetches vendored skills from the public Skilled repository, adds a new skill, mode or hub by its upstream path, flags rebuilds on source changes and runs as one update command."
trigger_phrases:
  - "upstream skill sync implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/platform/008-upstream-skill-sync"
    last_updated_at: "2026-11-24T19:30:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Added remote sync, the add command, source rebuild lines and the one-command update"
    next_safe_action: "Regenerate leaf-manifest.json once the peer session's task examples settle, then commit in the Product Owner repository"
    blockers: []
    key_files:
      - "scripts/vendor-sync.py"
      - "scripts/update-vendored.sh"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "762fe814-d3a3-49eb-a70b-1f8e7c37cf68"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "The spec lives in the platform sub-track and covers all four parts: remote fetch, add, one-command update and source rebuilds"
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.4 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 008-upstream-skill-sync |
| **Completed** | 2026-11-24 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Anyone with this repository can now update the vendored skills from the public Skilled repository and add a new one by its upstream path.

### Upstream skill sync

`--remote` reads a cached partial clone of Skilled, `add` writes and pulls a new `vendor.json` entry, and a changed server source file now prints its rebuild line. `bash scripts/update-vendored.sh` runs the sync and the gates, and `/vendor-update` runs it for an agent.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `scripts/vendor-sync.py` | Modified | Remote source, `add`, source rebuild lines |
| `scripts/tests/test_vendor_sync.py` | Modified | Five new cases |
| `scripts/update-vendored.sh`, `.claude/commands/vendor-update.md` | Created | The one-command update |
| `scripts/README.md`, `README.md`, `changelog/v1.0.38.0.md` | Modified | Document the commands |
| `scripts/tests/README.md`, `scripts/vendored/README.md` and its two `code-mode` READMEs | Modified | Current commands, test coverage and the standalone-clone check |
| `sk-create-figjam/assets/README.md`, `sk-create-figjam/scripts/README.md`, `scripts/figjam_checks/README.md`, `scripts/vendored/README.md` | Created | Code-folder READMEs where none existed |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

DeepSeek V4.1 Flash at max effort wrote the change through one Vibe build run, and every check below was rerun outside that run. The wrapper then got one fix: it hands the gates the same clone the sync read. A later pass aligned the code with the sk-code Python and shell checklists. The wrapper now runs under `set -euo pipefail` with numbered sections, and the usage block names `--remote` and `--ref`.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| `--remote` sets `VENDOR_UPSTREAM_ROOT` to the clone | Every command already reads upstream from there |
| `add` leaves out `graph-metadata.json` by default | The hub keeps one advisor identity |
| Only a Claude Code command | The repository has no other runtime command folder |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `python3 scripts/tests/test_vendor_sync.py` | 41 tests, OK |
| `vendor-sync.py status --remote` against GitHub | All six entries in step |
| `shellcheck scripts/update-vendored.sh` and the sk-code quality gate | Clean, no blocker found |
| sk-doc `validate_document.py` on all nine code READMEs | VALID, 0 issues each |
| `run_gates.sh` with `VENDOR_UPSTREAM_ROOT` set to the Skilled checkout | 4 of 19 fail: the identifier scan that failed before, the hub contract on a stale `leaf-manifest.json`, and the format fixtures and packet contract on another session's uncommitted `sk-product-owner` and `benchmark/format` edits |
| `bash scripts/update-vendored.sh --remote` | 2 of 19 gates fail, the identifier scan and skilled packet contract that failed before |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

- `--remote` needs network access to GitHub, and `VENDOR_UPSTREAM_URL` is the route when that repository moves
- `leaf-manifest.json` must be regenerated before the commit, because `sk-create-figjam/assets/README.md` is a new leaf. The regeneration waits for another session's new task examples to settle, so the manifest lists only finished files
<!-- /ANCHOR:limitations -->

---

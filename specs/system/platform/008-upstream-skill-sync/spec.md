---
title: "Feature Specification: Upstream skill sync"
description: "vendor-sync.py fetches vendored skills from the public Skilled repository, adds a new skill, mode or hub by its upstream path, flags rebuilds on source changes and runs as one update command."
trigger_phrases:
  - "upstream skill sync"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Upstream skill sync

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-24 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
`scripts/vendor-sync.py` reads upstream only from a local Skilled checkout above the repository, so an external user of this public repository cannot update the vendored skills at all. It has no way to vendor a new skill, mode or hub, so each new package means a hand-written `vendor.json` entry. It prints a rebuild step only when a dependency file changes, so a changed server source file leaves a stale build, as happened to `mcp-code-mode/mcp-server/index.ts`.

### Purpose
Anyone with this repository can update every vendored skill from the public Skilled repository with one command, add a new one by its upstream path, and see every rebuild a change needs.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A `--remote` option that fetches the selected upstream paths from the public Skilled repository into a cache, with `VENDOR_UPSTREAM_URL` and a ref override
- An `add` command that writes a new `vendor.json` entry from an upstream path and pulls it, leaving out `graph-metadata.json` by default
- A rebuild line when a vendored server's source file changes, beside the existing dependency-file trigger
- `scripts/update-vendored.sh`, one command that syncs and runs the gates, and a Claude Code `/vendor-update` command that runs it
- Tests for all three script changes, and the docs that describe the commands
- Code-folder READMEs: refresh the five under `scripts/` and add the four missing under `sk-create-figjam/` (`assets/`, `scripts/`, `scripts/figjam_checks/`, `scripts/vendored/`), added at the operator's request

### Out of Scope
- Changing what any vendored copy contains
- Pushing local edits upstream over the network
- OpenCode, Codex or other runtime command folders
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | A remote sync works with no local Skilled checkout | A test against a local bare repository passed through `VENDOR_UPSTREAM_URL` pulls a package |
| REQ-002 | `add` vendors a new package | A test adds a package, and `status` then prints `in step` for it |
| REQ-003 | The existing behavior is unchanged | `python3 scripts/tests/test_vendor_sync.py` passes every old case |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | A changed server source file prints a rebuild line | A test changes a `.ts` file under a package that excludes build output |
| REQ-005 | The change adds no gate failure | `run_gates.sh` fails no gate that passed in the baseline |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: An external user runs `bash scripts/update-vendored.sh` and gets every vendored skill in step with Skilled `main`
- **SC-002**: `scripts/README.md` documents remote sync, `add` and the update command
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The Skilled repository stays public on GitHub | High | `VENDOR_UPSTREAM_URL` points the fetch at a mirror |
| Risk | A partial clone needs network and git 2.25 or later | Low | The local checkout route stays the default when one is found |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None
<!-- /ANCHOR:questions -->

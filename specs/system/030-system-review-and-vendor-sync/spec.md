---
title: "Feature Specification: Whole-system review and vendor sync"
description: "Fixes the confirmed findings of a ten-iteration review of the whole Product Owner system, checks alignment with Skilled sk-doc and sk-code, and makes syncing the vendored packets one command."
trigger_phrases:
  - "system review and vendor sync"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Whole-system review and vendor sync

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-10 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Michel asked for a ten-iteration review of the whole system and its nested skills, a check that it still follows Skilled sk-doc and sk-code, and an easy way to sync the mcp and browser packets taken from Skilled, with a look at whether the Skilled overlay and repin support could do that. The review returned CONDITIONAL with 4 P1 and 21 P2 findings. The hub prose forbade a file its own gate requires. The vendored browser docs taught capture exports into the working tree with no rule against committing them. Syncing a vendored packet took a package name, an environment variable and a manual read of seven status lines. A short `_Mark as done_` line also stayed white in a pushed page.

### Purpose
Every confirmed finding is fixed at its source, the alignment checks are on record, and one command syncs every vendored entry.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Review: AI Systems root specs/054-po-system-deep-review/review/review-report.md
  verdict CONDITIONAL, filed P0 0, P1 4, P2 21, ten iterations, seven of them in parallel
  after adjudication: 3 P1 confirmed, 1 downgraded, 1 P2 refuted, 1 declined, 1 by design, 2 owner decisions
Alignment before the fix:
  package_skill.py --check --strict: valid for the hub, sk-product-owner and sk-create-figjam
  quality-gate.cjs over 42 code files: clean, one heuristic false positive
Vendor state before the fix:
  6 of 7 entries in step, mcp-code-mode 3 files behind, run_gates.sh 1 of 15 failing
Overlay engine on a two-packet scratch tree: staged repin exit 2, 809 refusals
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Hub `SKILL.md`, `ROUTER.md` and `AGENTS.md` drift
- Browser capture rules in the two vendored browser packets, fixed upstream in Skilled and pulled
- `benchmark/` gate wiring, the format harness, the parity wrappers, `.gitignore` and `.utcp_config.json`
- The Claude Project kernel and its README
- `scripts/vendor-sync.py`: `sync`, `status --local`, `diff`, the override root check, tests and docs
- The Mark-as-done match in the `mcp-click-up` page writer, upstream then pulled
- The `mcp-code-mode` pull that was pending

### Out of Scope
- A token diet for the always-loaded files. It changes behaviour and needs a benchmark run
- A restructure of `SYNC.md`
- Adopting the Skilled overlay engine. The review rules it out for this layout
- Live deployment of the Claude Project

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `SKILL.md`, `ROUTER.md`, `AGENTS.md` | Modify | Rules match the hub gate, true references, manual names |
| Skilled `mcp-chrome-devtools/`, `mcp-aside-devtools/`, `mcp-click-up/` (vendored) | Modify | Capture rules, Mark-as-done match |
| `mcp-code-mode/`, `vendor.json` | Modify | Vendor pulls |
| `benchmark/gates/`, `benchmark/format/`, `benchmark/parity/`, `.gitignore`, `.utcp_config.json` | Modify | Gate wiring, reference parity, ignore patterns |
| `claude project/` | Modify | Kernel v1.2.19, counts, upload guide |
| `scripts/vendor-sync.py`, `scripts/tests/`, `scripts/README.md` | Modify | Sync conveniences and tests |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The hub rules state what the hub gate enforces | `check_hub.py` passes and no hub sentence forbids a packet `ROUTER.md` |
| REQ-002 | A browser capture cannot be committed by accident | The chrome packet carries a capture rule and `.gitignore` covers the capture file names |
| REQ-003 | Every vendored entry is in step | `vendor-sync.py status` exits 0 |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | One command syncs every entry | `vendor-sync.py sync` pulls each upstream-ahead entry and prints one line per entry, proven by tests |
| REQ-005 | A standalone clone checks its vendored copies | `vendor-sync.py status --local` needs no upstream and the gate runs it where it skipped |
| REQ-006 | Every confirmed P2 is fixed or carries a recorded reason | Each row of the review registry maps to a change or a verdict |
| REQ-007 | No gate regresses | `run_gates.sh` passes all gates and the Sync Loop parity and residency checks pass |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `run_gates.sh` reports every gate passing, up from 1 of 15 failing
- **SC-002**: A rerun of the review finds none of the confirmed findings
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Where | Mitigation |
|------|------|--------|--------|------------|
| Risk | A reworded hub or kernel sentence breaks a declared residency row | Medium | Sync Loop | Run `validate_parity.py` and `residency_check.py` after the edits |
| Risk | Five agents edit one tree at once | Medium | Working tree | Each agent owns a separate file set and one full gate run closes the work |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the always-loaded files go on a token diet? About 11,800 words load before task work
- Should `SYNC.md` get an index or a split?
- Should an upstream-ahead vendored entry keep failing the release gate, or only warn?
<!-- /ANCHOR:questions -->

---

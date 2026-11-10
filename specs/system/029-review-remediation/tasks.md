---
title: "Tasks: Review remediation for the ClickUp session work"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "review remediation tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Review remediation for the ClickUp session work

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path). Verify: <command> prints <expected output>`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Read the review report and the 15 active findings. Verify: every registry row maps to a task below.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Contain local image uploads, allow only http, https and mailto links, add `- - -` as a divider, add expected counts and one normalizer and marker list, and unify `gapsLeft` (Skilled `mcp-tools.md`). Verify: offline converter run refuses `../../etc/passwd` and `sub/x.png`, all five programs parse.
- [x] T003 Release mcp-click-up 1.2.20.0 and hub 1.9.12.0 upstream and vendor-pull it (`mcp-click-up/`, `vendor.json`). Verify: `vendor-sync.py pull` prints `pulled`.
- [x] T004 [P] Fix `--write` divider inserts in both validators, give the checkbox near-miss its own silent fixture and align both harnesses (`benchmark/format/`, Sync Loop). Verify: both `run_fixtures.sh` pass.
- [x] T005 Correct 027 and 028 evidence, `SYNC.md` and the skill README version and count. Verify: `rg -n validate_parity specs/system/028-feedback-ticket-template/spec.md` prints REQ-003.
- [x] T006 Release hub 1.0.28.0 and `sk-product-owner` 1.2.16.0 with changelogs and a SYNC note. Verify: `check_changelog_shape.py` passes both.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Live push through the vendored page writer on scratch page 2kyq4d0p-123435. Verify: `mismatch` and `importDiff` empty, gaps 0.
- [x] T008 Run the system gates, format gate, parity and residency checks. Verify: 1 of 15 gates fails, vendor sync on `mcp-code-mode`, and the rest pass.
- [x] T009 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---

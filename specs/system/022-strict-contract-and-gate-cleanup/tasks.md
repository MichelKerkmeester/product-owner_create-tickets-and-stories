---
title: "Tasks: Strict skill contract and gate cleanup"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "strict contract and gate cleanup tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Strict skill contract and gate cleanup

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

`G` is `bash benchmark/gates/run_gates.sh`, run from the system root.
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Measure the gates (`benchmark/gates/`). Verify: `G` printed `4 of 15 gates failed`.
- [x] T002 Measure the strict findings (`sk-product-owner/`). Verify: `package_skill.py --check --strict` listed 105.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Prefix the bold label lines in 14 reference and asset files (`sk-product-owner/`). Verify: the strict check no longer names them.
- [x] T004 Add the setext blank lines in three references and two knowledge copies (`claude project/knowledge/`). Verify: `rule parity` prints `ok`.
- [x] T005 Skip git-ignored files in the link gate (`benchmark/gates/check_markdown_links.py`). Verify: `markdown link integrity` prints `ok`.
- [x] T006 Pull `mcp-figma` and `mcp-code-mode` (`vendor.json`). Verify: `vendor sync` prints `ok`.
- [x] T007 Bump to 1.2.9.0 and 1.0.21.0 with changelogs (`sk-product-owner/changelog/v1.2.9.0.md`, `changelog/v1.0.21.0.md`). Verify: `skilled hub contract` prints `ok`.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T008 Rerun every gate (`benchmark/gates/run_gates.sh`). Verify: `G` prints `1 of 15 gates failed`, naming only the three shared cards.
- [x] T009 Record the change (`SYNC.md`). Verify: `rg -n '1.2.9.0' SYNC.md` prints the line.
- [x] T010 Run the first-use readiness check before the first ClickUp write (`sk-product-owner/SKILL.md` Section 7 at 1.2.12.0, `AGENTS.md`, hub 1.0.24.0, `.utcp_config.json` gains `aside` and `chrome_devtools_live`, vendored `mcp-click-up` 1.2.14.0). Verify: `G` prints `all 15 gates pass`, and `rg -n 'readiness check' sk-product-owner/SKILL.md AGENTS.md` prints both lines.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed: `G` prints `1 of 15 gates failed`, and the failure is the shared cards this packet leaves out
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---

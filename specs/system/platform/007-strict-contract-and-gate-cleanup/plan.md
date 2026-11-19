---
title: "Implementation Plan: Strict skill contract and gate cleanup"
description: "Fix the render findings sk-product-owner owns with mechanical list and blank-line edits, teach the link gate to skip ignored files, and pull the vendored packages, then prove it with run_gates.sh."
trigger_phrases:
  - "strict contract and gate cleanup plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Strict skill contract and gate cleanup

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, Python 3 |
| **Framework** | Skilled skill package format |
| **Storage** | None |
| **Testing** | `benchmark/gates/run_gates.sh`, `package_skill.py --check --strict` |

### Overview
The render findings get a mechanical fix: a `- ` prefix on each bold label line and a blank line before each setext underline. The link gate skips what git ignores, and the vendor pull brings the two stale packages up to upstream. `run_gates.sh` proves the result.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] `bash benchmark/gates/run_gates.sh` prints `1 of 15 gates failed`, naming only the shared cards
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Source edits, then gates.

### Key Components
- **`sk-product-owner` references and assets**: the skill source the strict check reads
- **`benchmark/gates/check_markdown_links.py`**: the link gate, which now asks `git check-ignore` which files to skip

### Data Flow
Skill sources change first, the Project knowledge copies follow by hand, and the gates read both.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. Setup measures the findings, Implementation fixes them, Verification reruns the gates.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

`bash benchmark/gates/run_gates.sh` from the system root, and `benchmark/parity/run_parity.sh` in the Sync Loop after commit.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

The Skilled checkout for the vendor pull and `package_skill.py`. No new package.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Trigger: a gate that passed before now fails. Revert the one commit in the nested repo and the matching Barter commit.
<!-- /ANCHOR:rollback -->

---

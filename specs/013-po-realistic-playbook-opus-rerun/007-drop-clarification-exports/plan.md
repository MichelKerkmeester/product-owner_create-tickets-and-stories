---
title: "Implementation Plan: Phase 7, drop clarification exports"
description: "Delete the 20 published clarification files, make the collector skip the clarification suffix on both sides, prove it in the selftest, and bring the run README up to date."
trigger_phrases:
  - "drop clarification exports plan"
  - "collector clarification skip"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 7, drop clarification exports

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Python 3 standard library, Markdown |
| **Framework** | None |
| **Storage** | Files in `export/benchmark/` |
| **Testing** | The run's `selftest.py`, a collector dry run over the real run folder |

### Overview
The collector decides by file name, since the Product Owner naming rule gives every clarification the `-clarification.md` suffix. A skipped file prints one `skip` line, so the dry run shows what was left out.
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
- [x] Tests passing (if applicable)
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Other

### Key Components
- **`collect_exports.py`**: skips a clarification on the skill side before copying and on the Project side before writing
- **`selftest.py`**: the synthetic run already plants one clarification per side, so the expected set drops both and a new check asks for their skip lines

### Data Flow
Run folder exports and Project replies go through the collector into `export/benchmark/`, minus any clarification.
<!-- /ANCHOR:architecture -->


---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

Run the selftest against the old collector first, to show the new check fails there, then against the new one. Then run a dry run over the real run folder after the deletion.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

N/A. The change touches only this run's own tooling.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the commit in both repos. The removed files come back with it.
<!-- /ANCHOR:rollback -->

---

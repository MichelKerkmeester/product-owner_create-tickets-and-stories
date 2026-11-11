---
title: "Implementation Plan: Fresh review fixes"
description: "Fixes the chosen findings of a fresh review in four workstreams, redacts private identifiers in place and leaves the history rewrite as a separate confirmed step."
trigger_phrases:
  - "fresh review fixes plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Fresh review fixes

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, Python, Bash, Node |
| **Framework** | Product Owner hub, its gates and the Skilled sk-doc checkers |
| **Storage** | None |
| **Testing** | `run_gates.sh`, `test_vendor_sync.py`, the format gate, parity, residency and strict packet validation |

### Overview
Three workers fix separate file sets at once: the skill docs with their Project mirror, the gates and scripts, and the upstream items in Skilled. The identifiers are redacted in place by one script. The history rewrite of the two public repositories runs last and only on Michel's confirmation.
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
- [x] `run_gates.sh` passes every gate
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Fix each finding at its source, then add the gate that would have caught it

### Key Components
- **Skill docs and mirror**: scaffolds, the spacer rule, the feedback path and the stale counts
- **Gates**: the source format lint, the scaffold lint and the identifier scan
- **Vendor script**: exit 2 on a malformed manifest
- **Skilled**: four checker repairs, one playbook and the workspace id in two packets
- **Redaction**: one script over `specs/` and `benchmark/reports/`

### Data Flow
Skilled commit and publish, vendor sync, Product Owner commit, then the outer commit.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

Each new gate is shown red on a scratch copy before it is trusted. `run_gates.sh`, the vendor tests, parity and residency in a scratch clone, and `validate.sh --strict` close the work.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

The Skilled sk-doc checkers under `.skilled/skills/sk-doc`, and a published Skilled commit before the vendor sync.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the Product Owner commit, the outer repository commit and the Skilled commits. A history rewrite has no revert: the pre-rewrite refs are kept in a local bundle until Michel says to drop it.
<!-- /ANCHOR:rollback -->

---

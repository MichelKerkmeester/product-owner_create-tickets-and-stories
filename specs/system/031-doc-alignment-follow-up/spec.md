---
title: "Feature Specification: Doc alignment follow-up"
description: "Fixes the drift a hand-run of the Skilled sk-doc checkers found in the Product Owner docs and records what was left alone and why."
trigger_phrases:
  - "doc alignment follow-up"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Doc alignment follow-up

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P2 |
| **Status** | Complete |
| **Created** | 2026-11-11 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Michel asked for the Skilled alignment command on the whole system, to check each skill doc against sk-create-skill and the playbooks and READMEs against reality. The command scopes from a git diff and its surface map fires only on paths under `.skilled/skills`, so it resolved this system to 0 files. Its checkers were run by hand instead. They found one stale version line, three benchmark READMEs outside the README shape and a set of failures that need a decision or an upstream fix.

### Purpose
The drift that is safe to fix is fixed, and every other failure carries a reason.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
validate_skill_package.py --strict and quick_validate.py: pass for the hub and all seven packets
validate-playbook-topology.cjs: PASS, 7 of 7
validate_catalog_package.py: the four live catalogs pass
audit_readmes.py: exit 0
validate_document.py over 288 own docs: 229 pass, 59 fail
  57 fail on a missing overview section, 2 READMEs on heading case
check_changelog_shape.py over 93 own changelogs: 5 pass, 88 fail, 485 of the hits are sentence length
validate-playbook-package.cjs: mcp-code-mode fails with 10 real violations
sk-create-figjam/README.md says version 1.0.16.0, SKILL.md says 1.0.18.0
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The `sk-create-figjam/README.md` version line
- The README shape of `benchmark/gates/README.md`, `benchmark/format/README.md` and `benchmark/router/README.md`
- A record of the failures left alone and of the upstream items
- The pre-push wording left in the packet 030 summary

### Out of Scope
- Adding an overview section to agent-loaded references, templates and worked examples. It changes what the agent reads and what the Claude Project mirrors, so it needs a benchmark run
- Rewriting 88 older changelogs for sentence length
- Fixing the `mcp-code-mode` playbook, which is vendored and belongs upstream
- Changing the Skilled checkers

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-create-figjam/README.md` | Modify | Version 1.0.18.0 |
| `benchmark/gates/README.md`, `benchmark/format/README.md` | Modify | Upper-case numbered headings with `---` separators |
| `benchmark/router/README.md` | Modify | Overview heading, numbered sections |
| `specs/system/030-system-review-and-vendor-sync/implementation-summary.md` | Modify | Post-push wording |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The FigJam README states the packet version | Its frontmatter version equals the `SKILL.md` version |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-002 | The three benchmark READMEs pass the document validator | `validate_document.py` prints VALID for each |
| REQ-003 | No gate regresses | `run_gates.sh` passes every gate |
| REQ-004 | Every failure left alone has a reason on record | The implementation summary lists each group |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The four edited READMEs pass `validate_document.py`
- **SC-002**: `run_gates.sh` reports every gate passing
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Where | Mitigation |
|------|------|--------|--------|------------|
| Risk | A renumbered README section breaks a line citation | Low | `benchmark/format/README.md` | Search for citations into the three files and update them |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the overview rule apply to type references, templates and playbook scenarios, or do they get an exemption in the checker?
- Should the older changelogs be rewritten to the sentence ceiling?
<!-- /ANCHOR:questions -->

---

---
title: "Feature Specification: Product Owner Story and Epic template changes requested by the PM"
description: "The PM asked for four Story and Epic template changes: split each joined outcome in an acceptance criterion onto its own bold And line, drop the Story intro, merge About into a 3-5 sentence Problem, and drop the Delivery helper sentences."
trigger_phrases:
  - "product owner story feedback"
  - "product owner story and epic template changes requested"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Product Owner Story and Epic template changes requested by the PM

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-08 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The PM finds three things in generated Stories that slow them down. A Then line joins two outcomes with ", and" where the PM wants each outcome on its own bold **And** line. Every Story opens with a two-line intro the PM does not want, and About and Problem split the problem statement across two sections. Every Delivery sub-heading carries a helper sentence the PM deletes by hand.

### Purpose
The next Story the PM creates needs no hand edits for these four points, in the CLI skill and the claude.ai Project alike.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Story and Epic acceptance criteria: one outcome per Then or And line, a second outcome joined by "and" goes on its own `*   **And**` line, noun pairs stay intact
- Story only: no intro lines, `## About` and `#### Problem` merge into `## Problem` (3-5 sentences on the business problem), `## Solution` moves to H2
- Story and Epic: every Delivery helper sentence removed (Estimation, Rabbit holes, No-gos, External dependencies), `TBD...` placeholders kept
- Both format validators (Product Owner and the shared Sync Loop copy, byte-identical): Problem paragraph caps and an advisory for ", and" inside a Then or And line
- Skill and kernel minor bumps, changelog, dated `SYNC.md` note, playbook pass lines

### Out of Scope
- Task and Bug acceptance criteria - operator chose Stories and Epics only
- Epic About and Problem structure - operator chose Story only
- Benchmark reports, exports, changelogs and fixture source drafts - they are records or inputs
- Uploading the kernel and knowledge files to the claude.ai Project - operator step

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/story-template.md`, `epic-template.md` | Modify | New Story opening, And rule, no helper sentences |
| `sk-product-owner/references/story-mode.md` | Modify | Same rules in the mode workflow and checklist |
| `sk-product-owner/assets/examples/story/*.md` | Modify | Examples follow the new shape |
| `claude project/Custom Instructions.md`, `claude project/knowledge/*` Story and Epic files | Modify | Project mirrors of the same changes, kernel bump |
| `SKILL.md`, `AGENTS.md`, READMEs, playbook Story scenarios | Modify | Statements of the Story shape |
| `benchmark/format/validate-output-format.cjs`, shared Sync Loop copy, fixtures | Modify | Problem caps and the ", and" advisory |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | No Story or Epic source or mirror teaches a Then or And line that joins two outcomes | Template rule present on both sides, examples carry no ", and" in a Then or And line |
| REQ-002 | No new Story carries the intro lines or `## About` | Template, examples and kernel open on `## Problem` |
| REQ-003 | No Delivery helper sentence remains in a template, example or mirror | grep finds the four sentences only in records |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | Gates hold | Router, format fixtures, rule parity, project parity and reference parity pass |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A Story generated from the PM's sort example puts "the sort control shows..." on its own **And** line
- **SC-002**: Every system gate passes after the change, as it did before
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | claude.ai Project upload | The PM sees the change only after upload | Operator uploads the kernel and changed knowledge files |
| Risk | Validator twin drift | Med | Same edit in both copies, reference parity run |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None. Scope decisions were made by the operator on 2026-10-08
<!-- /ANCHOR:questions -->

---



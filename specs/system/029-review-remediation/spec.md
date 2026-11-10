---
title: "Feature Specification: Review remediation for the ClickUp session work"
description: "Fixes the 15 active findings a five-iteration deep review raised against the browser-first page writer, the Mark-as-done divider rule and the feedback ticket template."
trigger_phrases:
  - "review remediation"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Review remediation for the ClickUp session work

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
A five-iteration deep review of packets 026 to 028 returned CONDITIONAL with 2 P1 and 13 P2 findings. The page writer read any local file named by an image marker and uploaded it. The 028 spec cited a phrase-count gate as proof of mirror equality. The rest were converter edge cases, a validator `--write` bug, duplicated logic, fixture placement and version or count drift.

### Purpose
Every active finding is fixed at its source. The page writer is fixed upstream in Skilled and vendored back.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Review report: AI Systems root specs/053-po-clickup-session-review/review/review-report.md
  verdict CONDITIONAL, P0 0, P1 2, P2 13
Page writer before the fix:
  ![](../../x.png) read path.join(pwd, file) with no containment, sent as image/png
  [x](javascript:...) kept its href, "- - -" became a bullet
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Page writer and columns program in `mcp-click-up/references/mcp-tools.md`, upstream then vendored
- The two twin format validators, both fixture corpora and both fixture harnesses
- Spec evidence in 027 and 028, `SYNC.md` and the `sk-product-owner/README.md` version and count

### Out of Scope
- Kernel and Claude Project knowledge changes. No finding touches a Project-facing rule
- Live deployment of the Claude Project

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `mcp-click-up/references/mcp-tools.md` (Skilled, vendored) | Modify | Upload containment, link allowlist, divider spelling, expected counts, one normalizer |
| `benchmark/format/validate-output-format.cjs` and its Sync Loop twin | Modify | `--write` divider inserts |
| `benchmark/format/fixtures/`, Sync Loop `fixtures/`, both `run_fixtures.sh` | Modify | Silent near-miss fixture, equal expectations |
| `specs/system/027-*/spec.md`, `specs/system/028-*/` | Modify | Evidence corrections |
| `SYNC.md`, `sk-product-owner/README.md` | Modify | Version and count drift |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | A local upload reads only an image file name in the Aside session folder | Offline run refuses `../../x` and `sub/x.png`, accepts `shot.png` and `a.PNG` with the right type |
| REQ-002 | 028 cites a check that can fail on its claim | REQ-003 in 028 names `validate_parity.py` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | Every P2 finding is fixed | Each row in the review registry maps to a change |
| REQ-004 | No gate regresses | `run_gates.sh` fails only vendor sync on `mcp-code-mode`, both fixture harnesses pass |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A rerun of the review finds none of the 15 findings
- **SC-002**: A live push through the page writer reports an empty `mismatch`
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The gray count on a saved page can differ from the pasted HTML | Medium | Live push on a scratch page before release |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None
<!-- /ANCHOR:questions -->

---

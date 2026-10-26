---
title: "Tasks: Phase 38: figjam-model-comparison"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "figjam model comparison tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 38: figjam-model-comparison

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path)`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Write the spec folder and add row 38 to the parent phase table (spec.md)
- [x] T002 Copy the Devin runner into the run folder and write the adaptive driver and batch script (run/)
- [x] T003 Probe Figma's whoami on each of the three models through Devin
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Run FJ-022 to FJ-028 on DeepSeek V4.1 Flash max through Devin (skill/deepseek/)
- [x] T005 Run FJ-022 to FJ-028 on SWE 2 Max through Devin (skill/swe/)
- [x] T006 Run FJ-022 to FJ-028 on GLM 5.3 Flash max through Devin (skill/glm/)
- [x] T007 Render every written board at overview, 100% and greyscale (23 renders each, the overview set kept in renders/)
- [x] T008 [P] Give fresh readers the colour renders and the questions (grades/), three readers rotated across the models as the ADR-003 note records
- [x] T009 [P] Grade each type's three boards on the 22-point scorecard (grades/)
- [x] T010 Write results.jsonl and the run README with the per-type and per-model result
- [x] T011 Replace the seven type images with the best board per type and update the captions (sk-create-figjam/assets/screenshots/, README.md, sk-create-figjam/README.md)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T012 Redact the run folder and scan it and every changed file for the file key, board URLs, plan names and emails
- [x] T013 Run the benchmark gates and validate.sh --strict on this folder and the parent
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
- **Decisions**: See `decision-record.md`
<!-- /ANCHOR:cross-refs -->

---

## Verification Checklist

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|----------|----------|-------------------|
| **[P0]** | HARD BLOCKER | Cannot claim done until complete |
| **[P1]** | Required | Must complete OR get user approval |
| **[P2]** | Optional | Can defer with documented reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-005 in spec.md, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md and the four decision records]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: Devin 3000.11.205 with Figma's hosted server, Figma whoami answered on all three models, Code Mode for the renders]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P1] The driver reuses the runners' sandbox, isolation proof and redaction unchanged [EVIDENCE: cmp finds run/devin_playbook_runner.py identical to the 2026-10-24 copy and run/redact_run.py identical to the first-glance run's copy]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-005 Met in acceptance-criteria.md]
- [x] CHK-021 [P1] Every written board has its three renders and a scorecard [EVIDENCE: 23 overview, 23 full and 23 greyscale renders, and 21 rows in results.jsonl each with a scorecard]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets, board URLs, Figma file keys, plan names or emails in any changed file [EVIDENCE: the leak scan reads 0 hits on every scenario commit and on the grades, and the one README hit is the repository owner's name in the existing badges]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan, tasks and decision record synchronized [EVIDENCE: ADR-003 carries the as-run reader note, and T008 points at it]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: the commits touch the run folder, sk-create-figjam/assets/screenshots/, the two READMEs, the reports index and this folder]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 4 | 4/4 |
| P1 Items | 5 | 5/5 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-26
<!-- /ANCHOR:summary -->

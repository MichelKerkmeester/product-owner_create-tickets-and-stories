---
title: "Goal: Phase 8: Upstream round-trip and release"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "upstream roundtrip and release goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/008-upstream-roundtrip-and-release"
    last_updated_at: "2026-10-20T00:00:00Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "unset"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 8: Upstream round-trip and release

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Prove the sync path end to end by pushing one real optimization from Product Owner's vendored copy to .skilled, re-baselining, and releasing the upgrade with a clean-clone test.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | No push to any git remote without the operator's explicit go-ahead. |
| D2 | Release numbers move by patch steps only. |
| D3 | The hosted FigJam route documentation is pushed upstream into the shared mcp-figma skill for the operator's commit (operator, 2026-10-20). |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] vendor.json's base commit equals Code_Environment/Public HEAD for the mcp-figma path, and vendor-sync.py status exits 0
- [ ] A fresh git clone of Product Owner into a scratch folder has no dangling links and run_gates.sh exits 0 there
- [ ] Every gate named in phases 003 to 007 is rerun from the final state and each exit status is recorded in this phase's log
- [ ] validate.sh --recursive --strict on the parent prints RESULT: PASSED
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase opened | Pending | |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->

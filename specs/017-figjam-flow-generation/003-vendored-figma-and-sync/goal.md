---
title: "Goal: Phase 3: Vendored figma skill and sync"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "vendored figma and sync goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/003-vendored-figma-and-sync"
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
# Goal: Phase 3: Vendored figma skill and sync

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Give Product Owner a byte-identical vendored copy of the mcp-figma skill with a manifest and a vendor-sync.py tool whose status, pull and push keep it in step with .skilled.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The vendored copy stays byte-identical to upstream at the recorded base commit. Local changes leave only through push. |
| D2 | Tests use a scratch upstream. Nothing is written into Code_Environment/Public in this phase. |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] sha256 of every file under mcp-figma/ equals upstream at the base commit in vendor.json
- [x] vendor-sync.py status exits 0 right after pull, and exits 1 after a one-byte local edit while pull refuses
- [x] vendor-sync.py refuses a planted symlink
- [x] vendor-sync.py push against a scratch upstream produces a diff that git diff --stat shows there
- [x] run_gates.sh and run_parity.sh exit 0 with the vendored copy in place
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
| Vendored copy | Done | 58 files, 0 mismatches against 293caa90 |
| vendor-sync.py and tests | Done | 7 of 7 tests pass |
| Gates | Done | run_gates.sh 7 of 7, run_parity.sh PASSED 37/37 |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->

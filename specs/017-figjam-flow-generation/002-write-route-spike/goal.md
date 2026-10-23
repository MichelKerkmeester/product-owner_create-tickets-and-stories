---
title: "Goal: Phase 2: Write-route spike"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "write route spike goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/002-write-route-spike"
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
# Goal: Phase 2: Write-route spike

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Prove which FigJam write routes work from Claude Code and a claude.ai Project by building one scratch board through the hosted generate_diagram tool and one through figma-ds-cli fj, and record each route's tools, schema and limits.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Boards are written only to scratch Figma files. |
| D2 | No Product Owner source file changes in this phase. |
| D3 | The hosted generate_diagram route is the expected primary and fj the fallback, per the operator's 2026-10-20 choice. The spike confirms or refutes it with evidence. |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] A scratch FigJam board built through generate_diagram reads back node and connector counts equal to the Change Location model
- [ ] A scratch FigJam board built through fj reads back node and connector counts equal to the same model
- [ ] scratch/captures/ holds one dated capture file per route with the raw tool list and schema or help output
- [ ] decision-note.md names the primary write route and states whether a claude.ai Project can write boards
- [ ] git status in Product Owner shows no modified path outside this phase folder
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

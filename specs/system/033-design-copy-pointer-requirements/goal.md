---
title: "Goal: Design copy pointer requirements"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "design copy pointer requirements goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "system/033-design-copy-pointer-requirements"
    last_updated_at: "2026-11-12T15:10:00Z"
    last_updated_by: "claude-code"
    recent_action: "Changed the Story design copy rule in the skill and the Project mirrors"
    next_safe_action: "Upload the two changed knowledge files to the Claude Project"
    blockers: []
    key_files:
      - "sk-product-owner/references/story-mode.md"
      - "sk-product-owner/assets/story-template.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "ea1d6c8f-a3bd-4c7e-aa69-94dcca4ee626"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Design copy pointer requirements

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** A Story points at the design for the copy of a designed screen instead of listing every visible string.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Typed values and a shown string that is itself the change still travel verbatim |
| D2 | A new screen or component supplied as a design gets one pointer item plus the rules a design cannot show |
| D3 | No edit lands inside a statement the shared Sync Loop declaration pins |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] `rg -c 'Never write one item per visible string'` prints 1 for both sources and both mirrors
- [x] `bash benchmark/gates/run_gates.sh` prints `all 19 gates pass`
- [x] `bash benchmark/parity/run_residency.sh` prints `PASSED 1 system(s)`
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
| Rule edits in two sources and two mirrors | Done | New rule count 1 in each of the four files |
| Release files | Done | Hub 1.0.34.0, skill 1.2.19.0, two changelog files, one `SYNC.md` note |
| Gates | Done | `all 19 gates pass`, residency `PASSED 1 system(s)` |

### Deviations and findings

| Item | Note |
|------|------|
| Kernel clause and quality-scoring edit | Both were written, failed the residency check with 3 findings and were backed out, because each sat inside a pinned statement |
<!-- /ANCHOR:log -->

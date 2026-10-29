---
title: "Goal: Phase 51: FigJam gallery rerun on v1.0.16.0"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/051-figjam-gallery-rerun"
    last_updated_at: "2026-10-29T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Write FJ-049 and prepare the draft files"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "cb7f5c8f-ad61-46e0-8985-4b3286150879"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
# Goal: Phase 51: FigJam gallery rerun on v1.0.16.0

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Rerun the nine `sk-create-figjam` gallery scenarios and one new status lane scenario on v1.0.16.0 with Claude Sonnet 5.5 medium as the board maker, grade every board as the last reruns did, and give each gallery image to the higher-scoring of its old and new board, with no board URL, file key, plan name or email in any committed file.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Board maker: `claude:claude-sonnet-5-5:medium` for every run. |
| D2 | Scenarios: FJ-022 to FJ-028, FJ-032, FJ-036 and the new FJ-049. |
| D3 | Grading: two fresh readers per board, `run/composition_check.py` and one Claude Sonnet 5.5 high grader. |
| D4 | Judge: a new board takes the image when it scores at least as high as the old one. |
| D5 | One push of both repositories after the gallery lands. |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] Ten runs exist, each with a meta.json naming the medium model and one board
- [ ] Every board has two reader notes and one scorecard row
- [ ] Every gallery image and caption follows D4
- [ ] The redaction scan prints nothing and `run_gates.sh` passes 15 of 15
- [ ] `validate.sh --strict` on this phase prints RESULT: PASSED
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
| Phase scaffolded | Done | spec, plan, tasks, acceptance criteria and this goal |
| Runs, grading, gallery | Done | ten runs, twenty reader notes, 3 PASS and 7 FAIL, five images replaced |

### Deviations

| Item | Note |
|------|------|
| Readers | Reader a and reader b each read all ten boards in one session, allowed because no two boards share a request |
| FJ-032 start sections | The launch did not set FILE_START_SECTIONS, so the run log has none and the grader took the prepared section from the brief |
| Vendor sync gate | Code_Environment commits from another session moved the vendored mcp-figma and mcp-click-up after the first green run |
<!-- /ANCHOR:log -->

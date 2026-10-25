---
title: "Goal: Phase 37: FigJam design spec"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam design spec goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/037-figjam-design-spec"
    last_updated_at: "2026-10-25T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote the spec folder"
    next_safe_action: "Record the baseline and start task T002"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 3
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 37: FigJam design spec

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Build the user-editable FigJam design file inside sk-create-figjam and the 18 ranked fixes from phase 036, so editing one file restyles every composed board, a bad edit falls back with a named warning and every diagram type reads as one family, then mirror it to the claude.ai Project.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | One design file at `sk-create-figjam/assets/figjam-design.md`, with no override layer or flag |
| D2 | The composer keeps the built-in design and `compose_board.py` sends only differing tokens through `__THEME__`. The shipped theme is `{}` |
| D3 | A bad design falls back with a warning, whole or per token, as `DESIGN` lines that reach the reply as findings |
| D4 | Plain JSON tokens with swatch names. No off-palette hex |
| D5 | Style tokens only. Spacing, rhythm, router and layout stay in the composer |
| D6 | No layout switches. The fixed behaviour is the only behaviour |
| D7 | Sequence participants are white with the neutral stroke |
| D8 | The Project gets a design Knowledge file and the kernel moves to v1.2.4 |
| D9 | The theme counts toward the 50,000-character limit of one call |
| D10 | No board URL, Figma file key, plan name or Barter board in any file. Gallery boards use the fictional test file |
| D11 | The operator approved the plan. Run the build autonomously until everything is perfected, tested and verified. Decide on best judgement, record the decision and verify it at the end. Never pause mid-build for a question |
| D12 | A fresh Opus high review of the finished work comes before any commit, and every finding is closed first |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `--design-check` on the shipped design file prints no warning and an empty theme
- [ ] A broken design copy still draws the board with named `DESIGN` warnings counted on the `COMPOSED` line
- [ ] The self-test checks tints, swatch pins and key order, and the ranked fixes are the composer's only behaviour
- [ ] The composer and flow check self-tests, pytest and all 15 benchmark gates pass
- [ ] The Sync Loop residency, parity, output format and reference parity gates pass in a scratch clone
- [ ] The rubric, scorecard, scenarios, references, manifest and changelogs match the design file
- [ ] The gallery is recomposed and a fresh Opus high review has no open finding
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive. It is not
copied into the objective and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase opened | Done | 2026-10-25, a child of 017 after 036 |
| Spec folder | Done | spec, plan, tasks, acceptance criteria, decision record and goal written |
| Design file, ranked fixes, Project mirror and two review rounds | Done | self-test 1015/1015, 15 of 15 gates, Sync Loop gates pass in a scratch clone, validate.sh --strict PASSED. Gallery moved to 038 by ADR-010 |
<!-- /ANCHOR:log -->

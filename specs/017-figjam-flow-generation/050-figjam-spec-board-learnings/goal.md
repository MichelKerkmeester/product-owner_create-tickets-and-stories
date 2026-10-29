---
title: "Goal: Phase 50: FigJam lessons from a hand-built spec board"
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
    packet_pointer: "017-figjam-flow-generation/050-figjam-spec-board-learnings"
    last_updated_at: "2026-10-29T16:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Read the composer and confirm the plan.md Section 1 proposals with the operator"
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
# Goal: Phase 50: FigJam lessons from a hand-built spec board

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Close the five gaps a hand-built spec board showed in `sk-create-figjam`, as hub v1.0.17.0 and `sk-create-figjam` v1.0.16.0 with the Claude Project mirror in the same commits: a read-back trusts only a view rendered after its write, the subtitle names where a flow starts and ends, a laned process may carry one status lane, the `Faithful` detail level may give a step a body under a one-line label, and one anonymized worked example shows that board shape, with nothing of the source product in any committed file.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Fresh read-back: a view taken after a write counts only when it was rendered after that write, read by default through `node.screenshot()` inside a `use_figma` call, and a view that matches the board before the write is reported stale and taken again. |
| D2 | Subtitle: `%% subtitle:` stays one sentence and names where the flow starts and where it ends, with the reader where the brief names one. |
| D3 | Status lane: a laned process may declare one status lane, drawn first, holding the record's states in order, with a dotted `Moves the status` connector from each step whose move changes it. It is never an actor lane and its states count toward the budget. |
| D4 | Detail cards: at the `Faithful` detail level a step may carry a body of short lines under a one-line label, with a spacer and its own type token, held to the budget the checker prints. |
| D5 | Worked example: the board becomes one anonymized worked example and one process template pattern, written for a shipped fictional brand. |
| D6 | Release: hub v1.0.17.0 and `sk-create-figjam` v1.0.16.0 with the hand-written mirror in the same commit, and the kernel moves only when a kernel sentence changes. |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, the repository gates and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED after the last commit
- [ ] The anonymity scan on every changed file prints nothing
- [ ] The read-back, subtitle, status lane and detail card rules read the same in the skill and the Project
- [ ] The worked example is composed on a scratch board and its read-back matches its model from a view rendered after the write
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
| Checker, composer, docs, example, playbook | Done | flow_check 227 of 227 after the review repairs, composer 1302 of 1302, gates 15 of 15, pytest 18 |
| Project mirror and release | Done | divergence PASSED 66 pairs, residency PASSED 7 in a scratch clone |
| Live board | Done | 15 of 15 nodes, 20 of 20 connectors, 0 warnings, fresh view after the card fix |

### Deviations and findings

| Item | Note |
|------|------|
| Status shape | The confirmed proposal said a rounded rectangle differs from a step by shape, but a step is already one. The operator chose a chevron |
| Project room | The new composer code first left the Project 1,346 characters for a model, below the ER example's 2,225. The compactor now drops a lone arrow parameter's brackets and a semicolon or comma before a closing brace, so the room is 2,628, above the 2,404 before this phase |
| Example size | The commission example's body lines were shortened and the fitting step lost its body so its model, 2,610 characters, fits one Project call |
| Card height | The live board clipped a three-line body at 160 px. The card allowance moved from 8 to 32 px, and the three cards were resized in place rather than recomposed, then read back from a fresh view |
| Wrap advice | The check's stranded-word advice read a card's lines as one label, so it now skips text with a line break |
| Parity review record | `validate_parity.py` needs the flow-mode review record moved to the release commit, which can only be written after that commit exists |
| Format gate | `sk-product-owner/SKILL.md:46` fails the output format gate with a prose semicolon from an earlier commit, outside this phase's scope |
<!-- /ANCHOR:log -->

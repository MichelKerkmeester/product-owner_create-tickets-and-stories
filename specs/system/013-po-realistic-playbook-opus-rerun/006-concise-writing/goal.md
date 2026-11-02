---
title: "Goal: Phase 6, concise writing"
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
    packet_pointer: "013-po-realistic-playbook-opus-rerun/006-concise-writing"
    last_updated_at: "2026-09-26T06:39:09Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "[SESSION-ID]"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 6, concise writing

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> Everything between the frontmatter and the log is the DURABLE SLICE: it is
> what an operator sets as the session objective, and it must stay true for the
> life of the packet. The frontmatter above it is bookkeeping and never leaves
> this file: it is not sent in chat, not injected, not stored in an objective.
> Keep the slice short. A phase parent or top-level packet has one limit, 4000
> characters, measured from the frontmatter's closing fence to the log anchor.
> Up to 4000 passes and past it fails; the runtime goal surfaces cap what they
> hold, and a truncated objective loses its tail, which is where the criteria
> live.

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Write length caps for bullets and paragraphs into the Product Owner rules on both sides, warn on them in the format gate and the playbook, and edit the Opus run's 98 exports and its report to them by hand, without a rerun.

### Decisions

Parent decisions this phase honors. Changing one is an amendment to the parent.

| ID | Decision |
|----|----------|
| D4 | `export/benchmark/` holds only this run's deliverables, now the main run's 98 |
| D7 | A kernel review is recorded only after the operator confirms it |
| D8 | The caps go into the rules without a rerun, and the exports are edited by hand after grading, with verdicts still citing the graded originals |

### Operator copy

The operator holds the parent directive as the session objective, not this
file. A change here that alters a parent decision or criterion is applied to
the parent `goal.md` first, and the parent's chat slice is resent.
<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] A bullet is one sentence of 25 words or fewer, a paragraph at most 3 sentences and 60 words, and an About or Overview opening at most 2 paragraphs, in `SKILL.md`, the kernel and the playbook root, with the shared Conciseness card unchanged
- [ ] The format gate warns on over-cap artifact lines, exits 0, and its fixtures pass
- [ ] All 98 exports keep their headings, backticked values and numbers and meet the caps, checked file by file against a snapshot
- [ ] The README says the exports were edited by hand on 2026-09-26 and names the graded originals
- [ ] The collector skips an edited export unless forced and collects rounds only on request
- [ ] `validate.sh --recursive` passes, and both repos are committed with the 102 deletions
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
| Phase docs | Done | spec, plan, tasks, criteria, goal written |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | - |
<!-- /ANCHOR:log -->

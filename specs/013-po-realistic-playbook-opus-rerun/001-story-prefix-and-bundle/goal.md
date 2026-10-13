---
title: "Goal: Story prefix and Story bundle"
description: "The durable directive this phase executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "story prefix goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle"
    last_updated_at: "2026-09-25T20:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Authored the phase directive and its criteria"
    next_safe_action: "Execute the tasks against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Story prefix and Story bundle

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

**Objective:** Make every Product Owner Story export use the `Story-` word and let a Story ship with its tasks as one linked folder, in both packagings, before the playbook rewrite starts.

### Decisions

Frozen choices, restated from the parent `goal.md`. Changing one is an amendment there first.

| ID | Decision |
|----|----------|
| D1 | Story exports use `Story-` and the clarification lane is `{task\|bug\|doc\|Story\|Epic}`. `$prd` and `$p` stay aliases, and the H1 ban on `PRD -` stays |
| D2 | A Story with its task breakdown saves as `export/[###] - Story-[description]/`, holding the Story and one linked `[###].[n] - task-[description].md` per task |
| D4 | The old Sonnet files in `export/benchmark/` are removed first |
| D5 | Product Owner only, both packagings |
| D7 | A kernel review is recorded only after the operator confirms it |

### Operator copy

The operator holds this directive as the session objective, and that copy is
what judges completion, not this file. Whenever anything above the log changes
(objective, a decision, the binding table, a criterion), resend this file's
chat slice so the operator can update their copy. The chat slice is the
durable slice without its frontmatter, HTML comments, anchor markers, `---`
dividers or heading section numbers, and `goal.cjs packet` prints it as
`chat_slice`. Never send more than 4000 characters: cut this file first. Keep
reminding while the copy stays unset, and never stop work for it. A child goal
change that alters a parent decision or criterion is an amendment to the
parent: apply it there first, then resend the parent.
<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

Three to seven bullets, each checkable without opening another file. Copy them
verbatim into the objective: nothing dereferences a path, so criteria left only
here are invisible to whatever judges completion.

- [ ] A grep for `PRD-` and `|PRD|` over the Product Owner system and the Sync Loop folder, leaving out changelog, reports, episodes, `export/` and dated log lines, prints 0 lines
- [ ] `validate-output-format.cjs --system product-owner` exits 0 with no finding its baseline lacks, and `run_residency.sh product-owner` exits 0
- [ ] `validate_parity.py product-owner` exits 0 on the phase commit
- [ ] `AGENTS.md`, `SKILL.md`, `story-mode.md` and `task-templates.md` state the Story bundle, and the kernel and its Story Mode, Task Templates and Interactive Mode mirrors state the same rule
- [ ] The playbook validator reports 0 violations, and `git ls-files` lists 0 files under `AI Systems/Product Owner/export/benchmark/` in both repositories
- [ ] `SYNC.md` holds a dated note for kernel v0.15.0 that says its review is pending
- [ ] `validate.sh --strict` on this phase folder reports 0 errors
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
| D4 clean-up | Done | 25 files removed with `git rm` in the nested repo: `git diff --cached --stat` reads 25 files changed, 1087 deletions. Not yet staged in Barter, committed in neither |
| D1, D2 and bookkeeping | Pending | Planned in `plan.md` steps 1 to 15 |

### Deviations and findings

| Item | Note |
|------|------|
| System README | Lines 477, 492 and 737 name Sonnet and GLM files that D4 removed, so this phase rewrites them. The parent plan listed only lines 306, 570 and 572 |
<!-- /ANCHOR:log -->

---
title: "Goal: Phase 3, the playbook rewrite and the approval gate"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "playbook rewrite goal"
  - "003 completion criteria"
  - "scenario plan approval"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/003-playbook-rewrite"
    last_updated_at: "2026-09-25T18:45:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Authored the durable directive"
    next_safe_action: "Start T001 once phases 001 and 002 are committed"
    blockers:
      - "Phases 001 and 002 are not committed yet"
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
# Goal: Phase 3, the playbook rewrite and the approval gate

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

**Objective:** Replace the Product Owner playbook's 14 scenarios with 46 realistic ones set at Roamstay, Loomlist and Fernhouse, add the Ticket realism rubric and the attachment and bundle support in a new run folder and stop for the operator's approval before any scenario runs.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Story exports use `Story-` and the clarification lane is `{task\|bug\|doc\|Story\|Epic}` |
| D2 | A Story with its task breakdown is one subfolder, and the collector keeps it whole on both runtimes |
| D3 | Each scenario's attachments are copied into both sandboxes at `context/` before the baseline |
| D5 | Product Owner only, both packagings |
| D6 | No scenario runs before the operator approves the scenario plan |
| R1 | Ticket realism Blocking: wrong artifact word, a required template section missing, an invented fact, placeholder or toy content, context facts ignored or altered. Advisory: size band, commentary, asking for a fact an attachment states, a Task or Bug title with no discipline code. No Story or Epic H1 is expected to carry a code |

### Operator copy

The operator holds this directive as the session objective, and that copy is
what judges completion, not this file. Whenever anything above the log changes
(objective, a decision, a criterion), resend this file's chat slice so the
operator can update their copy. The chat slice is the durable slice without its
frontmatter, HTML comments, anchor markers, `---` dividers or heading section
numbers, and `goal.cjs packet` prints it as `chat_slice`. Never send more than
4000 characters: cut this file first. A child goal change that alters a parent
decision or criterion is an amendment to the parent: apply it there first, then
resend the parent.
<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] The playbook validator prints `scenarios=46 categories=10 operator=46` with `violations=0 warnings=0` and exits 0
- [ ] `run/selftest.py` in the claude-opus-5-5-medium report folder exits 0 after asserting 46 rows, 86 turns, identical twins, every attachment staged and checked and a bundle collected into its subfolder on both runtimes
- [ ] Root section 5 holds one `### Ticket realism` subsection with 5 Blocking and 4 Advisory items, and the six existing advisory readings are unchanged apart from line numbers
- [ ] A `PRD-` search over the playbook package and an em dash search over the package and the new report folder both print nothing
- [ ] The phase is committed in the Barter repo and the Product Owner repo, the latter with no attribution line
- [ ] The operator approved the scenario plan through AskUserQuestion, recorded below with its date and both SHAs, while the new report folder held no `manifest.json`, `run-status.json` or `run-log.jsonl`
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
| Phase 003 | Pending | Scoped. Waits on phases 001 and 002 |
| Phase 003 | Done | Rubric (T003) before group writers (T007-T012); validator 46/0/0, selftest 7/7, dry run 46 rows 86 turns; Product Owner 3023c5e, Barter c15c05e9; 18/18 AC met |
| Operator approval | Recorded | 2026-09-25 19:31 UTC, AskUserQuestion answer Approve and run, against 3023c5e and c15c05e9, report folder held only .gitignore and run/ scripts; plan page https://claude.ai/artifact/YE9rqVDigYxfRXTs8u3NR8 |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->

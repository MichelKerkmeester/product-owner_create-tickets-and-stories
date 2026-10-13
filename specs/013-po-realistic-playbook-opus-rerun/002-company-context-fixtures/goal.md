---
title: "Goal: Phase 2, company context fixtures"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "company fixtures goal"
  - "002 completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/002-company-context-fixtures"
    last_updated_at: "2026-09-25T18:45:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Authored the durable directive"
    next_safe_action: "Write the values check and the three writer briefs"
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
# Goal: Phase 2, company context fixtures

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

**Objective:** Write the three company context documents and the 22 source attachments the new Product Owner scenarios cite, under `AI Systems/Product Owner/benchmark/fixtures/companies/`, each file named and valued exactly as this phase's manifest states.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Parent D3: fixtures are attached files the runner copies into both sandboxes at `context/<basename>`, so every name carries its company slug and is unique |
| D2 | Parent D5: Product Owner only. This phase adds fixture files and changes no skill, kernel, knowledge, playbook or runner file |
| D3 | Every scenario attaches its company's context document, and 18 of the 23 also attach the sources the manifest lists |
| D4 | Third-party vendors appear by role, never by a real brand, and people appear by fictional first name and role |
| D5 | The manifest in `spec.md` is the contract for names and values. Phase 003 cites those names exactly, and any change goes into the manifest first |

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

- [ ] `find` counts exactly 25 files under `AI Systems/Product Owner/benchmark/fixtures/companies/`, and `scratch/check_manifest_values.py` exits 0 with every manifest file in place and every hard value found
- [ ] The em dash grep (U+2014) on the fixtures prints nothing, and `lint_replies.py --brief` reads `clean` for all 25 files
- [ ] `roamstay-context.md`, `loomlist-context.md` and `fernhouse-context.md` are each 150 to 250 lines with the eleven named H2 sections
- [ ] The link, brand and test-vocabulary greps print nothing, and the template-marker grep lists no file beyond the two given inputs
- [ ] In the digest pair, `07:00` is absent from the spec, `08:00` is absent from the inventory, and neither holds an authority word
- [ ] The fixtures are committed in the Barter repo and the Product Owner public repo, the public commit has no attribution line, and nothing is pushed before the operator's go-ahead
- [ ] `validate.sh --strict` on this phase reports 0 errors and `acceptance-criteria.md` reads `Closeable: Yes`
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
| Fixtures | Pending | Scoped in `spec.md`, no file written |
| Fixtures | Done | 25 files, 512 values 0 misses; Product Owner ff5c80f, Barter 37591a16; 12/12 AC met |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->

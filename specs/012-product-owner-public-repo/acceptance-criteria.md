---
title: "Acceptance Criteria: Publish Product Owner as its own public repo"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "acceptance criteria"
  - "product owner public repo closure"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "012-product-owner-public-repo"
    last_updated_at: "2026-09-24T12:00:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Verified the follow-up criteria on b86e6ed and monorepo 6f49fabb"
    next_safe_action: "None required. Follow-ups are listed in implementation-summary.md"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/README.md"
      - "AI Systems/Product Owner/.gitignore"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "57a20eaa-0fc8-4c05-99d5-39e79963f536"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "README placement: a real root README, the skill README unchanged"
      - "The four z — Knowledge symlinks: replaced with byte copies"
      - "The follow-ups: keep the copies and teach the sync loop about them"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Publish Product Owner as its own public repo

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 012-product-owner-public-repo
**Level:** 2
**Status:** Complete
**Date:** 2026-09-24
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the public repo, When GitHub renders its root, Then it shows a regular `README.md` in the Skilled style whose local links all resolve | `gh api repos/MichelKerkmeester/product-owner_create-tickets-and-stories/readme` returns `README.md` opening `# Product Owner - Create Tickets & Stories`. Link scan: 17 local links, 0 broken | Met | - |
| AC-002 | REQ-002 | Given the `.gitignore`, When `export/` holds drafts, Then only `.gitkeep` and `export/benchmark/` are tracked | `git check-ignore -v` names `.gitignore:5` for the four task files and `Story Drafts/`. The contents API lists `.gitkeep, benchmark` under `export/` | Met | - |
| AC-003 | REQ-003 | Given the pushed tree, When symlinks are listed, Then none exist | `git ls-files -s` shows 0 entries with mode `120000`. `cmp` confirmed each copy matches its source | Met | - |
| AC-004 | REQ-004 | Given the staged set, When scanned, Then it holds no credentials and no raw logs | Pattern scan for tokens, keys and `.env` values returned no hits. 0 `.jsonl` or `stderr.txt` files staged | Met | - |
| AC-005 | REQ-005 | Given the README counts, When compared with the files, Then they match | 21 examples (5 task, 4 bug, 7 doc, 5 story), 38 knowledge files, 6 templates, 117 fixtures and 189 differential inputs, each counted on disk or from command output | Met | - |
| AC-006 | REQ-006 | Given the README, When validated, Then it passes sk-doc and HVR | `validate_document.py` VALID with 0 issues. `hvr_lint.py` clean. No em dash, en dash, prose semicolon or Oxford comma | Met | - |
| AC-007 | REQ-007 | Given the commit, When inspected, Then it follows sk-git | `0da0a05 feat(product-owner): add the skill, Project package and front-page README`, staged by explicit paths, hooks ran, no bypass | Met | - |
| AC-008 | Follow-up | Given the skill sources, When searched for the old layout, Then none calls the four files symlinks | `SKILL.md` lines 121, 317, 318 and 405 and the skill README, Project README and benchmark notes describe copies. Pushed as `b86e6ed` | Met | - |
| AC-009 | Follow-up | Given a card in `z — Knowledge/` or a copy changes, When the parity gate runs, Then it reports the copy or the mirror that no longer matches | Red proof: a changed copy gives 1 finding, a changed card gives copy and mirror findings. Clean tree: 38/38, 4 shared sources checked as vendored copies. Pushed as monorepo `6f49fabb` | Met | - |

### Status values

| Value | Meaning |
|-------|---------|
| `Met` | Verified. The Verification cell names evidence that was actually observed. |
| `Unmet` | Not yet satisfied. Blocks closure. |
| `Waived` | Deliberately not pursued. Requires an ADR in the Waiver cell. |
| `Superseded` | Replaced by a different criterion or decision. Requires an ADR in the Waiver cell. |

### Waiver cell

Write `-` when the row is `Met` or `Unmet`. Write `ADR-NNN` when the row is
`Waived` or `Superseded`, naming a decision record that exists in
`decision-record.md`. A waiver naming an ADR that is not there fails validation:
the point of a waiver is that someone recorded the reasoning, so an unbacked
waiver is treated as an unmet criterion rather than as a pass.
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

All nine criteria are met. The first seven hold on `0da0a05`, the follow-up criteria on `b86e6ed` and monorepo `6f49fabb`. The monorepo carries the front page, the ignore rules and the `LICENSE` as `5ae0494e` and the benchmark deliverables as `859dad08`, and the benchmark parity scripts still need the monorepo.
<!-- /ANCHOR:closure -->

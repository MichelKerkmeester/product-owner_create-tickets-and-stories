---
title: "Implementation Summary: Publish Product Owner as its own public repo"
description: "Product Owner now opens on GitHub with its own front-page README, keeps drafts out of git and loads every rule file from a plain clone."
trigger_phrases:
  - "implementation summary"
  - "product owner public repo shipped"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "012-product-owner-public-repo"
    last_updated_at: "2026-09-24T12:00:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Pushed the follow-up b86e6ed and monorepo 6f49fabb"
    next_safe_action: "None required"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/README.md"
      - "AI Systems/Product Owner/.gitignore"
      - "AI Systems/Product Owner/sk-product-owner/references/hvr-core.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "57a20eaa-0fc8-4c05-99d5-39e79963f536"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 012-product-owner-public-repo |
| **Completed** | 2026-09-24 |
| **Level** | 2 |
| **Commit** | `0da0a05` and follow-up `b86e6ed` on `main` of https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories |
| **Monorepo commits** | `a183e88a`, `98e14d27`, `6f49fabb`, `5ae0494e` and `859dad08` on `main` of `Barter-BV/marketing-ai-systems` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The Product Owner repository now opens on a real front page and carries the whole system in one commit. A clone routes requests, loads every always-on rule file and runs its router and format checks without the monorepo.

### Publish Product Owner as its own public repo

The root `README.md` was a symlink to the skill README, so GitHub would have shown skill frontmatter as a table and links that break from the root. It is now a 684-line front page in the style of the Skilled README: summary, overview with a flow diagram, quick start, routing, output shapes, delivery, templates, checks, a repository map, FAQ, troubleshooting and related documents. GPT-6 Luna drafted it at max effort on the fast tier, then the session checked every claim against the files and tuned it.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `README.md` | Symlink replaced with a file | Public front page |
| `.gitignore` | Created | Ignores `.DS_Store` and `export/` except `.gitkeep` and `export/benchmark/` |
| `sk-product-owner/references/hvr-core.md` | Symlink replaced with a byte copy | Always-loaded rule file resolves in a clone |
| `sk-product-owner/references/conciseness.md` | Symlink replaced with a byte copy | Always-loaded rule file resolves in a clone |
| `sk-product-owner/references/conciseness-rationale.md` | Symlink replaced with a byte copy | On-demand rule file resolves in a clone |
| `sk-product-owner/references/human-voice-rules.md` | Symlink replaced with a byte copy | On-demand rule file resolves in a clone |

### Follow-up: copies the sync loop knows about

The operator asked to fix the follow-ups and chose to keep the copies and teach the sync loop about them. `SKILL.md`, the skill README, the Project README and the benchmark notes now call the four files copies. The standalone format lint leaves the copies out of its walk and still names the two always-loaded cards. In the monorepo, `systems.py` declares the four as `vendored_shared_copies`, each naming its card. The parity gate holds each copy and its Project mirror to the card byte for byte. The carrier query, the reading brief and the shared format core treat a declared copy exactly as they treat a symlink.

| File | Action | Purpose |
|------|--------|---------|
| `sk-product-owner/SKILL.md`, `sk-product-owner/README.md`, `claude project/README.md` | Modified | Describe the copy layout |
| `benchmark/gates/*`, `benchmark/router/*` | Modified | Notes and comments describe the copy layout |
| `benchmark/format/validate-output-format.cjs` | Modified | Copies stay out of the source lint walk |
| `SYNC.md` | Modified | Dated note, kernel and Skill versions unchanged |
| `z — Claude Project Sync Loop/systems.py`, `validate_parity.py`, `carrier_query.py`, `reading_brief.py`, `systems.cjs`, `validate-output-format.cjs` | Modified in the monorepo | Declare and check vendored shared copies |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The ignore rules, the byte copies and the remote repoint landed before the draft, so the first commit could only carry a public-safe tree. After the Luna draft, the session fixed four defects it found against the sources: a Story template missing its dividers and spacers, a Task template missing its group divider, parity scripts listed as runnable when they need the monorepo, and missing inline code for every command and path. The README then passed the sk-doc validator, the repo's own HVR linter and a link scan. The session staged the repo by explicit paths, committed through the normal hooks and pushed to `origin/main`.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| A real root README, the skill README left as it was | The operator chose it. The skill README carries version frontmatter that tooling reads |
| Byte copies for the four shared rule files | The operator chose it. A symlink into `z — Knowledge/` points at nothing in the public repo |
| Last Commit badge in place of Latest Release | The repo has no release, so a release badge would read "no releases" |
| No `Co-Authored-By` trailer | The `commit-msg` hook rejects attribution lines, and the hook was not bypassed |
| The README calls the parity and gates scripts maintainer tooling | They exec scripts in `z — Claude Project Sync Loop/`, so they fail from a clone |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `bash benchmark/router/run_fixtures.sh` | PASS, 117/117 fixtures and 189/189 differential inputs |
| `bash benchmark/format/run_fixtures.sh` | PASS, all format-validator fixtures |
| sk-doc `validate_document.py README.md` | PASS, VALID with 0 issues |
| `benchmark/grader/hvr_lint.py README.md` | PASS, clean |
| Link, dash, semicolon and Oxford-comma scan | PASS, 17 local links resolve, 0 findings |
| Staged set scan | PASS, 584 files, 0 symlinks, 0 credentials, 0 raw logs, `export/` holds `.gitkeep` and 60 benchmark deliverables |
| `git rev-parse HEAD origin/main` after fetch | PASS, both `0da0a05` |
| GitHub README API | PASS, serves the new `README.md` |
| Follow-up: `validate_parity.py product-owner` | PASS, 38/38 pairs, 4 shared sources checked as vendored copies |
| Follow-up: red proof | PASS, a changed copy gives 1 finding, a changed card gives copy and mirror findings, both restored with no residue |
| Follow-up: `validate-output-format.cjs --system product-owner` and reference parity | PASS, 40 source files, shared core identical to the standalone validator |
| Follow-up: router and format fixtures | PASS, 117/117 fixtures, 189/189 inputs, all format fixtures |
| Follow-up: carrier query fan-out and duplicates | PASS, 41 reached pairs as before the change, 37 with the declaration removed. The copies add 0 duplicate sentences |
| Follow-up: `carrier_query_evidence.py` against the pre-change tree | Same results. Checks 1 to 5 fail on both trees, the only other difference is the untracked `export/` drafts in the live discovery count |
| Follow-up: `residency_check.py --all`, `check_criteria.sh` | 5 residency findings and 6 criteria fail, all present before this work: the removed Barter Blog Posts system and residency rows in other systems |
| Follow-up: `git rev-parse` after fetch | PASS, public repo `b86e6ed` and monorepo `6f49fabb` match their remotes |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Maintainer scripts do not run from a clone.** `benchmark/parity/*.sh` and `benchmark/gates/rule_parity.py` call `z — Claude Project Sync Loop/`, which lives only in the monorepo. The README says so and points readers at the two checks that run standalone.
2. **A card change turns this system red until it is copied over.** The parity gate now catches it, but the copy is still made by hand: copy the card over its file under `references/` and over the Project mirror.
3. **Both repos carry the same public files.** The monorepo holds the front page, the ignore rules and the `LICENSE` as `5ae0494e` and the 60 benchmark deliverables as `859dad08`, byte-identical to the public repo.
4. **The pushed tree carries local paths and one real example.** 42 benchmark report files name `/Users/michelkerkmeester/...` paths, and `task/task-example-ds-variables.md` is a real Barter design token release.
<!-- /ANCHOR:limitations -->

---

---
title: "Feature Specification: Publish Product Owner as its own public repo"
description: "Product Owner now has its own git repository and a public GitHub remote, but its front page is a symlink to the skill README, its export folder would publish real Barter drafts, and four reference files are symlinks that point outside the repo. This packet gives the repo a real front-page README, ignore rules for export and self-contained references, then makes the first push."
trigger_phrases:
  - "product owner public repo"
  - "product-owner_create-tickets-and-stories"
  - "front-page readme"
  - "export gitignore"
importance_tier: "normal"
contextType: "specification"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Publish Product Owner as its own public repo

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete, pushed |
| **Created** | 2026-09-24 |
| **Branch** | `main` of the nested repo (packet only, no monorepo branch created) |
| **Systems touched** | Product Owner, plus the sync loop in the follow-up |
| **Public repo** | https://github.com/MichelKerkmeester/product-owner_create-tickets-and-stories |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
`AI Systems/Product Owner/` now holds its own `.git` with a public GitHub remote, and its only commit is the GitHub-generated `LICENSE`. The root `README.md` is a symlink to `sk-product-owner/README.md`, so GitHub would show the skill README with its frontmatter as a table and with links that break from the repo root. Nothing ignores `export/`, which holds real Barter tasks and story drafts. Four ALWAYS and ON_DEMAND references in `sk-product-owner/references/` are symlinks into `z — Knowledge/`, which the public repo does not contain.

### Purpose
The public repo opens on a front-page README in the style of the Skilled repo README, carries every file its skill loads, keeps generated exports local apart from the benchmark deliverables, and holds the whole system in its first pushed commit.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A real root `README.md` in the style of `Code_Environment/Public/README.md`, drafted by GPT-6 Luna at max effort on the fast tier through cli-codex, then verified and tuned
- A root `.gitignore` that ignores `.DS_Store` and all of `export/` except `export/.gitkeep` and `export/benchmark/`
- Byte copies in place of the four `z — Knowledge/` symlinks in `sk-product-owner/references/`
- The `origin` remote pointed at the renamed repo
- One Conventional Commit of the system and a push to `origin/main`

### Out of Scope
- Editing `sk-product-owner/README.md`, `SKILL.md`, `AGENTS.md` or `SYNC.md`: the operator asked for the front page only. `SKILL.md` still calls the four copied files symlinks, which is recorded as a follow-up
- Committing anything in the monorepo: the operator asked for commits in the public repo
- Removing the other monorepo references the system files carry: a larger clean-up the operator has not asked for

### Follow-up Scope

The operator asked on 2026-09-24 to fix the follow-ups this packet recorded, and chose to keep the copies and teach the sync loop about them. That lifts two of the exclusions above:

- `SKILL.md`, the skill README, the Project README and the benchmark docs now describe the four files as copies
- The monorepo gets a commit: the sync loop declares the four files as vendored shared copies, so its gates hold each copy and its Project mirror to the card byte for byte

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/README.md` | Replace symlink with file | Public front page |
| `AI Systems/Product Owner/.gitignore` | Create | Export and OS-file ignore rules |
| `AI Systems/Product Owner/sk-product-owner/references/hvr-core.md` | Replace symlink with file | Byte copy of `Rules - Human Voice Core - v0.100.md` |
| `AI Systems/Product Owner/sk-product-owner/references/conciseness.md` | Replace symlink with file | Byte copy of `Rules - Conciseness - v0.100.md` |
| `AI Systems/Product Owner/sk-product-owner/references/conciseness-rationale.md` | Replace symlink with file | Byte copy of `Rules - Conciseness - On Demand Rationale - v0.100.md` |
| `AI Systems/Product Owner/sk-product-owner/references/human-voice-rules.md` | Replace symlink with file | Byte copy of `Rules - Human Voice - EN - v0.210.md` |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The root `README.md` is a regular file that follows the Skilled README style and every local link in it resolves inside the repo |
| REQ-002 | `git check-ignore` ignores every `export/` entry except `export/.gitkeep` and `export/benchmark/` |
| REQ-003 | No committed symlink points outside the repo |
| REQ-004 | The pushed commit holds no credentials and no ignored raw benchmark logs |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | Every count the README publishes matches the files |
| REQ-006 | The README passes the sk-doc validator and carries no em dash, en dash, prose semicolon or Oxford comma |
| REQ-007 | The commit follows sk-git: Conventional Commit subject, scoped staging, no hook bypass |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: GitHub shows the new front page on the repo root
- **SC-002**: `origin/main` equals the local commit and holds no file from `export/` apart from `.gitkeep` and `benchmark/`
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | codex CLI with `gpt-6-luna` | No draft if the dispatch fails | Write the README in session from the same sources |
| Risk | Public exposure of internal material | High | Keep `export/` ignored, scan the staged set for credentials before the commit |
| Risk | The four copied references drift from `z — Knowledge/` | Low | Operator chose copies over symlinks. Recorded as a follow-up |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The pushed tree stays small. Raw benchmark event logs stay ignored by the report folder's own `.gitignore`
- **NFR-P02**: No single committed file approaches the GitHub 50 MB warning size

### Security
- **NFR-S01**: No token, key or `.env` value in the staged set
- **NFR-S02**: Real Barter exports stay local

### Reliability
- **NFR-R01**: The router fixtures and the format fixtures still pass after the change
- **NFR-R02**: The push goes through the normal hooks
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- Empty input: `export/` with only `.gitkeep` still keeps the folder in git
- Maximum length: none
- Invalid format: a symlinked `README.md` is removed before the writer runs so a write cannot land in the skill README

### Error Scenarios
- External service failure: a failed push leaves the local commit in place for a retry
- Network timeout: retry the push
- Concurrent access: the monorepo tree is shared, so only the nested repo is staged

### State Transitions
- Partial completion: the spec records which step stopped
- Session expiry: this packet carries the state
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 10/25 | Six files, one repo |
| Risk | 12/25 | First public push |
| Research | 6/20 | Style source, skill sources, ignore rules |
| **Total** | **28/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None open. The operator chose a real root README, byte copies for the four symlinks and one packet per repo on 2026-09-24
<!-- /ANCHOR:questions -->

---

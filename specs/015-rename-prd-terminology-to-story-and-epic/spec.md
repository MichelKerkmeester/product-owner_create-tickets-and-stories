---
title: "Feature Specification: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration"
description: "Product Owner ships Story and Epic artifacts, but its skill, kernel and Project knowledge still called them PRDs and printed a **PRD:** label into generated Stories. This packet renames the artifact everywhere it is meant, keeping $prd/$p and PRD input wording as back-compat routes."
trigger_phrases:
  - "rename prd terminology to story and epic"
  - "rename leftover prd terminology to story and epic"
  - "story value line label"
  - "story-example rename"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-17 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner produces two artifact kinds, Story and Epic, yet about fifty lines across the skill, the kernel, the Project knowledge and the READMEs still name the artifact a PRD or a product requirements document. The optional Connextra value line printed `**PRD:**` into every Story that used it, and the router topic and the five Story examples still carried the `prd` name.

### Purpose
Every place that names the artifact says Story or Epic, while the `$prd`/`$p` aliases and PRD wording in user input keep routing to Story.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The `**PRD:**` value-line label becomes `**Story:**` in the Story Mode template and the maximal example, on both packagings
- Prose that names the artifact a PRD, in the skill, kernel, Project knowledge, `AGENTS.md` and both READMEs
- `assets/examples/story/prd-example-*.md` renamed to `story-example-*.md`, with every live reference repointed
- The router semantic topic key `prd` renamed to `story` in the router contract, the kernel copy, the benchmark copy and the `SKILL.md` topic table
- Version bumps, a changelog entry, a `SYNC.md` change record and the resync of declared statements in `systems.py`

### Out of Scope
- `$prd` and `$p` aliases, the `$prds` false-match lists and router patterns that match "prd" in user input - they are deliberate back-compat
- The ban on the old `PRD -` title prefix and the playbook scenarios that test it - the old prefix is still what they remove
- Changelogs, `SYNC.md` history, `kernel-review.json`, benchmark reports, episode records and earlier spec packets - they are history
- Pre-existing sk-doc structural findings in five edited files - present at HEAD with the same counts

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/SKILL.md`, `README.md`, `references/*.md`, `assets/*.md` | Modify | Artifact naming, topic table, version |
| `sk-product-owner/assets/examples/story/prd-example-*.md` | Rename | To `story-example-*.md` |
| `sk-product-owner/leaf-manifest.json`, `leaf-aliases.json`, `graph-metadata.json` | Modify | New example paths and description |
| `claude project/Custom Instructions.md`, `README.md`, seven `knowledge/` files | Modify | Mirrors of the skill edits, kernel v1.2.0 |
| `AGENTS.md`, `README.md`, `SYNC.md` | Modify | Naming, version claims, change record |
| `benchmark/router/route_contract.py`, `differential_corpus.json` | Modify | Topic key and group labels |
| `sk-product-owner/changelog/v1.2.0.0.md` | Create | Release note |
| `z — Claude Project Sync Loop/systems.py` | Modify | Pair paths and resynced statements |
| `z — Claude Project Sync Loop/validate_parity.py` | Modify | Review-due diff follows renames |
| `z — Claude Project Sync Loop/prove_rename_drift.py`, `README.md`, feature catalog | Create, Modify | Proof and its registration |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | No Story or Epic produced from the templates or examples carries a `**PRD:**` label |
| REQ-002 | The router still routes every existing fixture, including `$prd`, `$p` and PRD wording, to the same intent |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | Prose that names the artifact says Story or Epic on both packagings, with each skill edit mirrored |
| REQ-004 | The examples and the router topic carry the story name, and no live reference points at an old name |
| REQ-005 | The Sync Loop gates show no finding beyond the baseline at HEAD |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Zero `**PRD:**` lines outside history, and router fixtures 117/117 plus differential 189/189 pass
- **SC-002**: Residency and parity findings equal the HEAD baseline
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Sync Loop gates read committed `systems.py` | Cannot verify on the live tree | Scratch clone with one throwaway commit |
| Risk | Statement resync rewrites every system's rows | Med | Diff against a backup, changed rows confined to the Product Owner block |
| Risk | Parity drift check did not follow renames | Med | Gate taught to follow renames, on the operator's decision |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: N/A, documentation and routing data only

### Security
- **NFR-S01**: No secrets or environment values enter any file

### Reliability
- **NFR-R01**: Router behaviour is unchanged for every fixture input
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- User input that says "PRD": still routes to Story through the unchanged patterns and synonyms
- `$prds`: still a false match that does not route

### Error Scenarios
- A refinement whose source carries an old `PRD -` title: keeps it unless restructuring is authorized, as before

### State Transitions
- Existing Stories that carry `**PRD:**`: a source-preserving refinement keeps the label, as with any unasked normalization
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | About 40 files across two repos, mostly line edits |
| Risk | 9/25 | Router key and declaration statements are contract surfaces |
| Research | 6/20 | Classify each mention as artifact name or input wording |
| **Total** | **29/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None open. The rename drift findings cleared through a rename-aware drift check, on the operator's decision
<!-- /ANCHOR:questions -->

---

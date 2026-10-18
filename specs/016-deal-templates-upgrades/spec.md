---
title: "Feature Specification: Deal Templates upgrades for Product Owner"
description: "Product Owner replies came in ten shapes, asked a second question round, and six Doc examples broke the format gate they model. This packet sets one Delivery Reply Shape with numbered Open items, one question round, fixed Doc examples with an example lint and gate runner, and a narrow Catalog em-dash grant."
trigger_phrases:
  - "deal templates upgrades"
  - "delivery reply shape"
  - "one question round"
  - "example lint"
  - "catalog em dash grant"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Deal Templates upgrades for Product Owner

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-18 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
In the 2026-10-08 Haiku 5.5 run the 43 skill replies opened in ten different ways, three with a sentence before the path, and 19 carried bullets ending in a full stop. Three scenarios asked a second question on Turn 2 instead of drafting. Six of the seven Doc worked examples failed the output-format gate they model, and no check read the examples.

### Purpose
Every reply follows one shape described once, the draft comes after one question round with leftover gaps listed as Open items, and every worked example and worked reply passes a gate that runs from one command.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- One Delivery Reply Shape in Interactive Response Templates Section 3, with a wrong and a right first line, one quality line, a numbered Open items block, one closing line and worked replies, on both packagings
- `AGENTS.md`, `SKILL.md`, Doc Mode, Story Mode, Interactive Mode, Quality Scoring and the kernel pointing at that shape
- One question round: after the answer the next reply drafts, and only a source conflict, a missing promised source or an unsettled decision may ask again
- The six failing Doc examples fixed on both packagings
- `benchmark/gates/example_lint.py` and `benchmark/gates/run_gates.sh`
- A Catalog entry em-dash grant in Doc Mode, Doc Templates and both validator twins, with fixtures
- Version bumps, changelog, `SYNC.md` record, READMEs and the playbook lines whose expectations changed

### Out of Scope
- Explicit commands asking first - kept as v0.12.0.0 set it, on the operator's decision
- The shared Human Voice card and this system's copy of it - shared fleet-wide, so the card owner adds the Catalog grant
- `systems.py` - another process owns it, so the resync pairs are handed over instead
- Bare-fence fallback, semantic read-back and the version-bump rule text - not in the approved scope

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/interactive-response-templates.md` and mirror | Modify | Delivery Reply Shape, Section 3 |
| `AGENTS.md`, `sk-product-owner/SKILL.md` | Modify | Pointers, one question round, Open items |
| `sk-product-owner/references/{doc,story,interactive}-mode.md`, `quality-scoring.md` and mirrors | Modify | Pointers, Doc quality line, Catalog grant |
| `sk-product-owner/assets/doc-templates.md` and mirror | Modify | Catalog grant |
| Seven Doc examples and mirrors | Modify | Em dashes and semicolons removed |
| `claude project/Custom Instructions.md` | Modify | Kernel v1.2.1 |
| `benchmark/format/validate-output-format.cjs` and its shared Sync Loop twin | Modify | Catalog grant, same edit in both |
| `benchmark/format/run_fixtures.sh`, three fixtures | Modify, Create | Catalog cases |
| `benchmark/gates/example_lint.py`, `run_gates.sh` | Create | Example lint and gate runner |
| READMEs, `SYNC.md`, changelog, playbook | Modify, Create | Records and expectations |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Every worked example and Project example mirror passes the system validator in artifact mode |
| REQ-002 | The Catalog entry heading and its link pass inside a Catalog with an Index heading, and an em dash anywhere else still fails, with both validator twins in reference parity |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | The reply shape is described once, with worked replies, and every other surface points at it |
| REQ-004 | After the one question round the next reply drafts, and Open items carries each addition and safe default in the Situation and Open bullet shape |
| REQ-005 | One gate runner runs every system gate, and the example lint provably fails on a broken example and a broken reply |
| REQ-006 | No line the playbook cites moves, and every playbook expectation that changed is rewritten |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `run_gates.sh` prints `all 5 gates pass`, and the example lint passes 42 files and the worked replies
- **SC-002**: Reference parity stays identical and the Deal Templates, Copywriter and Sales Direct format fixtures still pass
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | `systems.py` owned elsewhere | Residency and one adapted pair stay red until resynced | Resync pairs handed over and simulated against the files |
| Dependency | Shared Human Voice card | Card grant list omits the Catalog shape | Named in the changelog and the hand-off |
| Risk | Shared validator used by four systems | Med | Same edit in both twins, reference parity, every system's fixtures rerun |
| Risk | Playbook cites lines by number | Med | Every edit kept on its own line, line counts asserted |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The example lint runs in seconds over 42 files

### Security
- **NFR-S01**: No secrets or environment values enter any file

### Reliability
- **NFR-R01**: A lint that finds no file fails rather than passing
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A Catalog heading with no stable ID, a second dash, an H2 or a title: still blocked
- The entry shape in a document with no Index heading: still blocked

### Error Scenarios
- A standalone clone with no Sync Loop folder: rule parity reports SKIPPED and the summary names it
- A blocked export: the reply opens on `Export blocked:` and prints no path line

### State Transitions
- A source conflict after the first answer: the one sanctioned second question
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 15/25 | About 55 files, mostly line edits on both packagings |
| Risk | 11/25 | Shared validator and declared kernel statements are contract surfaces |
| Research | 7/20 | Read of Deal Templates and of the last run's replies |
| **Total** | **33/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- The shared Human Voice card needs the Catalog grant line, outside this packet's write scope
<!-- /ANCHOR:questions -->

---

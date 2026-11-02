---
title: "Implementation Plan: Publish Product Owner as its own public repo"
description: "Replace the README symlink with a Luna-drafted front page, add export ignore rules, copy the four shared references into the repo, then commit and push the whole system as the first real commit."
trigger_phrases:
  - "product owner public repo plan"
  - "front-page readme plan"
  - "first push plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Publish Product Owner as its own public repo

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, gitignore, git |
| **Framework** | sk-doc create-readme rules, sk-git commit workflow |
| **Storage** | None |
| **Testing** | sk-doc `validate_document.py`, `benchmark/router/run_fixtures.sh`, `benchmark/format/run_fixtures.sh`, link and dash scans |

### Overview
The front page is drafted by GPT-6 Luna at max effort on the fast tier through cli-codex, from the skill sources and in the style of the Skilled README, then verified against the files and tuned in session. Ignore rules and self-contained references land first so the first commit carries a public-safe tree.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [ ] All acceptance criteria met
- [ ] Router and format fixtures passing
- [ ] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Other: a documentation and repository-hygiene change

### Key Components
- **Root `README.md`**: the public front page, separate from the skill README
- **Root `.gitignore`**: keeps generated exports local
- **`sk-product-owner/references/`**: now self-contained

### Data Flow
Skill sources and the style source feed the Luna draft. The session verifies the draft against the files, tunes it, then stages the repo and pushes it.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `README.md` | Symlink to the skill README | Replace with a real front page | `test -f` and not `-L`, validator, link scan |
| `sk-product-owner/references/*` symlinks | Shared rules from `z — Knowledge/` | Byte copies | `cmp` against each target |
| `SKILL.md` wording about symlinks | Describes the old layout | Unchanged, follow-up | Recorded in the implementation summary |
| `z — Claude Project Sync Loop/systems.cjs` | Reads the rule files by path | Unchanged | Content is byte-identical |
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Unit | Router contract and format validator | `benchmark/router/run_fixtures.sh`, `benchmark/format/run_fixtures.sh` |
| Integration | Ignore rules and staged set | `git check-ignore`, `git ls-files --others --exclude-standard` |
| Manual | README read-back against the files | Validator, dash scan, link scan, count checks |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| codex CLI 0.156.1 with `gpt-6-luna` | External | Green | Draft in session instead |
| GitHub account `MichelKerkmeester` | External | Green | No push |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: sensitive content found on the remote, or a broken front page
- **Procedure**: commit a fix on top. The remote is new, so the operator may also reset it to the `LICENSE` commit with their approval
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Phase 1 (Setup) ──────┐
                      ├──► Phase 2 (Core) ──► Phase 3 (Verify)
Phase 1.5 (Config) ───┘
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core, Config |
| Config | Setup | Core |
| Core | Setup, Config | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | 15 minutes |
| Core Implementation | Medium | 45 minutes including the Luna draft |
| Verification | Medium | 30 minutes |
| **Total** | | **About 1.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the original symlink targets stay in `z — Knowledge/` and the old README stays in `sk-product-owner/README.md`
- [x] Feature flag configured: not applicable
- [x] Monitoring alerts set: not applicable

### Rollback Procedure
1. Commit a corrective change on top of the pushed commit
2. Restore a symlink with `ln -s` if the operator reverses the copy decision
3. Read the repo page on GitHub after the fix
4. Tell the operator what changed

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---

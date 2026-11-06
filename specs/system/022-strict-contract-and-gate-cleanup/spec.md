---
title: "Feature Specification: Strict skill contract and gate cleanup"
description: "sk-product-owner failed its strict package check on 105 render findings, and four Product Owner gates failed. This packet fixes the 85 findings the skill owns and brings the gates to 14 of 15."
trigger_phrases:
  - "strict contract and gate cleanup"
  - "strict skill contract and gate cleanup"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Strict skill contract and gate cleanup

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-05 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
`package_skill.py --check --strict` failed `sk-product-owner` on 105 render findings: bold label lines that join into one paragraph, and setext underlines that turn a line into a heading. Four Product Owner gates failed as well: vendor sync, markdown link integrity, skilled hub contract and skilled packet contract.

### Purpose
Every finding the skill owns is fixed and every gate the skill owns passes, so the one failure left is the shared cards, which belong to `z — Knowledge`.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
$ bash benchmark/gates/run_gates.sh   (before)
4 of 15 gates failed
$ bash benchmark/gates/run_gates.sh   (after)
  skilled packet contract  FAILED
  Strict mode: 20 contract requirement(s) unmet (references/conciseness-rationale.md, references/conciseness.md, references/hvr-core.md)
1 of 15 gates failed
$ bash benchmark/gates/run_gates.sh   (2026-11-06, after the shared-card fix and the readiness release)
all 15 gates pass
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Turn the bold label lines in 14 `sk-product-owner` reference and asset files into list items
- Add the blank line that stops a setext heading in `quality-scoring.md`, `router-contract.md`, `story-mode.md` and their two Project knowledge copies
- Make `check_markdown_links.py` skip files git ignores, so the private `context/` folder no longer fails the link gate
- Pull the vendored `mcp-figma` and `mcp-code-mode` copies to upstream, so vendor sync passes
- Fix the 20 findings in the three shared cards at their source in `z — Knowledge/`, on Michel's decision, and copy the new bytes into all 15 copies across five systems, re-freezing the Sales Direct Communication snapshot
- Fix the 23 findings the new Skilled render checks raised on 2026-11-05: renumber the Conciseness card 1 to 8 on Michel's decision, with every citation and kernel v1.2.17, rewrite the card and template intros, add the When to Use sections, open the README with its Overview, and leave `assets/examples/` out of the render scan in Skilled `package_skill.py`
- Fix the 45 `sk-create-figjam` findings under the same checks, on Michel's decision, and move that packet to 1.0.18.0
- Bump `sk-product-owner` to 1.2.9.0, then 1.2.10.0 and 1.2.11.0, and the hub to 1.0.21.0 with changelogs, and record the change in `SYNC.md`
- Run the vendored `mcp-click-up` first-use readiness check after a push is approved and before the first ClickUp write, add the `aside` and `chrome_devtools_live` manuals to `.utcp_config.json`, and pull `mcp-click-up` 1.2.14.0 and 1.2.15.0 (`sk-product-owner` 1.2.12.0, hub 1.0.24.0)

### Out of Scope
- The `mcp-code-mode` vendor pull. Upstream holds a peer session's uncommitted `ROUTER.md` edit, so the pull waits for that commit
- The SKILL.md word count warning. It is advisory and does not fail the gate

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/references/*.md`, `sk-product-owner/assets/*.md` | Modify | Bold labels as list items, setext blank lines |
| `claude project/knowledge/Product Owner - Rules - Quality Scoring.md`, `Product Owner - Templates - Story Mode.md` | Modify | Same setext fix as the skill sources |
| `benchmark/gates/check_markdown_links.py` | Modify | Skip git-ignored files |
| `mode-registry.json` | Modify | List `context` in repoPaths |
| `mcp-figma/`, `mcp-code-mode/`, `vendor.json` | Modify | Vendor pull |
| `SKILL.md`, `hub-router.json`, `description.json`, `README.md`, `SYNC.md`, `changelog/`, `sk-product-owner/changelog/` | Modify/Create | Versions and notes |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Every strict finding outside the shared cards is fixed | `package_skill.py --check --strict` lists only `hvr-core.md`, `conciseness.md` and `conciseness-rationale.md` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-002 | Vendor sync and link integrity pass | `run_gates.sh` prints `ok` for both |
| REQ-003 | The Project knowledge copies carry the same fix | `rule_parity` prints `ok` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `run_gates.sh` prints `1 of 15 gates failed`, and the failure names only the three shared cards. After the shared cards were fixed at their source, it prints `all 15 gates pass`
- **SC-002**: The strict count falls from 105 to 20
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Upstream Skilled commits for the vendor pull | Pull refuses while upstream is dirty | Commit Skilled first, then pull |
| Risk | A list prefix changes text a Project copy mirrors | Med | `rule_parity` and the Sync Loop parity run after commit |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the shared cards be fixed in `z — Knowledge` and spread to every system that copies them? Decision: yes, by Michel on 2026-11-05. The Conciseness card is renumbered rather than exempted, also his decision
<!-- /ANCHOR:questions -->

---

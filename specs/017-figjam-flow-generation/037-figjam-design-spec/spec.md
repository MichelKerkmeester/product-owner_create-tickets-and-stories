---
title: "Feature Specification: Phase 37: FigJam design spec"
description: "Phase 036 ranked 18 design changes for composed FigJam boards and recommended a user-editable design spec file. This phase builds both in sk-create-figjam: one design file inside the skill that restyles every board, theme plumbing that falls back with a warning on a bad edit, the ranked fixes, the rubric and playbook checks and the claude.ai Project mirror."
trigger_phrases:
  - "figjam design spec"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 37: FigJam design spec

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-25 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 37 of 37 |
| **Predecessor** | 036-figjam-design-system |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met and a fresh Opus high review of the finished work has no open finding |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 37** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: sk-create-figjam, its Project mirror and kernel, the Sync Loop declaration for the new file pair, the hub manifest and changelogs. No Barter board.

**Dependencies**:
- `036-figjam-design-system/research/research.md` Section 4 for the ranked fixes, Section 6 for the design spec, Section 7 for what stays out and Section 9 for the questions the operator answered.
- sk-create-figjam as it stands after phase 036, whose compact template measured 43,623 characters.

**Deliverables**:
- `sk-create-figjam/assets/figjam-design.md`, the one design file.
- The composer and `compose_board.py` changes for the theme, the fallback warnings, `--design-check` and the ranked fixes.
- The rubric, scorecard, playbook scenarios, style guide and type references brought in line.
- The Project Knowledge file, the composer Knowledge step and the kernel clause at v1.2.4.
- The gallery boards recomposed and their screenshots updated.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
A composed board's style lives in literals across the composer, the style guide, the type references and the check. A user who wants boards in another style has no one place to change it. Phase 036 also found boards that break the packet's own rules: pink in the zone tints, light blue with five meanings, keys that order one type two ways and routes that run under the subtitle.

### Purpose
Ship one design file inside the skill that restyles every board when edited, keep a bad edit from breaking a board and apply the ranked fixes so every diagram type reads as one family.

### Decisions
The full records are in `decision-record.md`.

- **D1 (ADR-001)**: One design file at `sk-create-figjam/assets/figjam-design.md`, with no system-root override and no per-run flag. It is a smaller FigJam form of the DESIGN.md Style Reference: prose sections, then one fenced `json` token block.
- **D2 (ADR-002)**: The composer keeps the factory design built in. `compose_board.py` reads it from the composer source, resolves the design file over it and sends only the tokens that differ through a new `__THEME__` placeholder. The shipped file equals the built-in design, so the shipped theme is `{}`.
- **D3 (ADR-003)**: A bad design falls back with a warning. A broken block or an unknown schema version drops the whole design. A bad token drops that token alone. Each warning prints as a `DESIGN` line, is counted on the `COMPOSED` line and becomes a `Finding:` line in the Flow reply.
- **D4 (ADR-004)**: Plain JSON tokens with swatch names, not the DTCG `$value` shape. FigJam's swatch pairs and section tints are read-only reference in the block and pinned by the self-test. Off-palette hex is deferred.
- **D5 (ADR-005)**: Tokens carry style values only. Spacing, rhythm, the router's constants and the layout stay in the composer.
- **D6 (ADR-006)**: No layout switches. The improved behaviour from the ranked fixes is the only behaviour.
- **D7 (ADR-007)**: Sequence participants are drawn white with the neutral stroke.
- **D8 (ADR-008)**: The claude.ai Project gets the design in this phase, with the kernel moving to v1.2.4.
- **D9 (ADR-009)**: The theme counts toward the 50,000-character limit of one `use_figma` call, and the constants are compacted to pay for it.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
The ranked fixes from research Section 4, by rank:

1. Pink out of the zone tint cycle, plus a self-test tint check.
2. Zone and gantt band tints skip any hue a member kind draws and always differ from the neighbouring zone.
3. One meaning per colour: participants white, with gateway and in progress recorded as named roles.
4. The design spec and the theme plumbing, plus `compose_board.py --design-check`. This read-only command prints the resolved design, the tokens that differ from the built-in ones, the measured ratios, the warnings and the theme's character cost.
5. Canonical key order per type.
6. Zone tops aligned for zones that share a row in group mode.
7. Edge label, key and source text from 16 to 18 px, plus a `small` 14 px step for bar text and pins.
8. Routes priced to stay inside the diagram's box, clear of the subtitle band and the board margin.
9. The key spans the diagram's width and wraps.
10. Connector looks defined once. Sequence requests take the default gray with a closed head.
11. A lighter sequence board: smaller participant feet, step pins beside the sender's lifeline and row height from the label size.
12. Gantt planned bars get the line gray as their stroke.
13. ER cards that share a row are top-aligned.
14. The subtitle wrapped balanced, so no last line holds one word.
15. A ninth rubric criterion "Matches the active design" with the total moving from 16 to 18. The scorecard Signal reads the design file and its tint cycle, and its total stays 22. Two new playbook scenarios: a family scenario and a broken-design scenario.
16. Type references cut their colour prose to role names and a pointer to the design file, with their Project mirrors.
17. A `marker` role for sequence step pins.
18. Gantt section names measured at the size they are drawn, and the gantt screenshot re-rendered.

Also in scope:
- `flow_check.py` stops counting `figjam-design.md` as a shipped model.
- The Sync Loop declaration in `systems.py` and `systems.cjs`, in the Claude Project Sync Loop folder beside the systems, learns the new asset and Knowledge pair.
- `leaf-manifest.json` regenerated.
- The style guide points at the design file.
- Changelogs for sk-create-figjam v1.0.3.0 and the hub v1.0.3.0, with their version bumps.
- The gallery boards recomposed on the fictional test FigJam file, with the screenshots updated honestly.
- A fresh Opus high review of the finished work before any commit.

### Out of Scope
- Brand skins and off-palette hex.
- Per-type themes.
- Router or spacing tokens.
- A numeric corner radius.
- ER header bands and crow's-foot ends.
- Any Barter board, board URL or Figma file key.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/assets/figjam-design.md | Create | The one design file |
| sk-create-figjam/assets/compose-board.js | Modify | Built-in design, `__THEME__`, compacted constants and the ranked fixes |
| sk-create-figjam/scripts/compose_board.py | Modify | Design resolution, fallback warnings, `--design-check`, the budget and self-test checks |
| sk-create-figjam/scripts/flow_check.py | Modify | Skip the design file as a model |
| sk-create-figjam/scripts/figjam_checks/design.py | Create | Read the design file over the built-in design and hold it to the floors |
| sk-create-figjam/scripts/figjam_checks/board_geometry.py, sk-create-figjam/scripts/compose-trace.mjs | Modify | Measure boards in the active design, and prove the font fallbacks in the trace |
| SKILL.md, README.md, USER-GUIDE.md, SYNC.md, mode-registry.json, description.json, hub-router.json and the packet's SKILL.md and README.md | Modify | Release versions, file maps, a dated note and the README order the operator asked for on 2026-10-25 |
| sk-create-figjam/references/ | Modify | Style guide, quality rubric and the seven type references |
| sk-create-figjam/manual-testing-playbook/ | Modify | Scorecard Signal and two new scenarios |
| sk-create-figjam/assets/screenshots/ | Modify | Recomposed gallery boards, moved to phase 038 by ADR-010 |
| sk-create-figjam/changelog/, changelog/ | Create | v1.0.3.0 for the packet and the hub |
| leaf-manifest.json | Modify | Regenerated |
| claude project/ | Modify | New design Knowledge file, composer steps, type mirrors and the kernel at v1.2.4 |
| Sync Loop folder: systems.py, systems.cjs | Modify | The new asset and Knowledge pair |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | `sk-create-figjam/assets/figjam-design.md` holds prose sections that say what each token means and which floors apply, then one fenced `json` block of style tokens per D4 and D5, and its values equal the composer's built-in design. |
| REQ-002 | `compose_board.py` resolves the design file over the built-in design, validates it, falls back per D3 and fills `__THEME__` with only the tokens that differ. `--design-check` prints the resolved design, the differing tokens, the measured ratios, the warnings and the theme's character cost. The filled code stays under 50,000 characters. |
| REQ-003 | The composer applies ranked fixes 1 to 3, 5 to 14, 17 and 18 as its only behaviour, and the self-test checks the tints, the swatch pins and the key order. |
| REQ-004 | The packet gates pass from the final state: the composer self-test, the flow check self-test, the pytest suite and the 15 benchmark gates. |
| REQ-005 | The Project carries the design: the new Knowledge file, the `__THEME__` step in the composer Knowledge file, the type mirrors and one kernel clause at v1.2.4. The Sync Loop declaration names the new pair and its residency, parity, output format and reference parity gates pass in a scratch clone. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-006 | The rubric, scorecard, playbook scenarios, style guide and type references match the design file, `flow_check.py` skips it, `leaf-manifest.json` is regenerated and both changelogs exist at v1.0.3.0. |
| REQ-007 | The gallery boards are recomposed on the fictional test FigJam file and every changed screenshot shows what the composer now draws. A fresh Opus high review of the finished work has no open finding before any commit. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Editing one token in `figjam-design.md` restyles every composed board, and a bad edit draws the built-in style for that token with a named warning.
- **SC-002**: The shipped design file sends an empty theme, and every gate that owns a changed file passes from the final state.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Phase 036 research | Defines the fixes | Each task names its rank |
| Risk | The template passes 50,000 characters with the theme and the fixes | High | Compact the constants first and count the theme in the same check |
| Risk | Larger labels and aligned zones widen dense boards | Med | Recompose every gallery board and rerun the layout budgets |
| Risk | A Project mirror drifts from its skill source | Med | Sync Loop parity and reference parity gates in a scratch clone |
| Risk | A design edit breaks a board silently | Med | Each fallback prints a named `DESIGN` warning that reaches the reply |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs, Figma file keys, plan names or Barter flows in any changed file. PO is a public repository.

### Reliability
- **NFR-R01**: An empty or missing theme draws the default board, so the Project's copy works without a script.
- **NFR-R02**: Each change is a working-tree edit to a tracked file, reverted with `git checkout -- <path>` on the operator's approval.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- The token block is missing, duplicated or unparseable: the built-in design draws the board with one warning.
- A token names an unknown swatch or misses a floor: that token falls back and its warning names it.
- A board with more zones than tints: neighbouring zones still differ and no tint matches a member hue.

### State Transitions
- Partial completion: resume from the first unchecked task in tasks.md.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | Composer, script, references, playbook, Project mirror and Sync Loop |
| Risk | 12/25 | Every board's look changes under a tight character budget |
| Research | 4/20 | Done in phase 036 |
| **Total** | **34/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator answered the research's open questions before this phase opened. Off-palette hex stays deferred.
<!-- /ANCHOR:questions -->

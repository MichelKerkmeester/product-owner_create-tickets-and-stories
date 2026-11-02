---
title: "Implementation Plan: Phase 37: figjam-design-spec"
description: "Builds the user-editable FigJam design file inside sk-create-figjam, the theme plumbing that falls back with a warning, the 18 ranked fixes from phase 036 and the Project mirror, then recomposes the gallery and runs every owning gate."
trigger_phrases:
  - "figjam design spec plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 37: figjam-design-spec

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | JavaScript for the composer, Python for the scripts, Markdown for the design file and references |
| **Framework** | The FigJam plugin API through one `use_figma` call |
| **Storage** | `sk-create-figjam/assets/figjam-design.md`, one fenced `json` token block |
| **Testing** | `compose_board.py --self-test`, `flow_check.py --self-test`, pytest, the 15 benchmark gates, the Sync Loop gates and validate.sh --strict |

### Overview
The composer keeps its factory design built in and gains a `__THEME__` placeholder beside `__MODEL__`. `compose_board.py` reads the built-in design from the composer source, resolves `figjam-design.md` over it, validates each token against its floor and sends only the differences. A bad token falls back with a named `DESIGN` warning. The ranked fixes then land as the composer's only behaviour, and the constants are compacted so the theme and the fixes fit under 50,000 characters. The rubric, scorecard, playbook, references and Project mirror follow, and the gallery is recomposed on the fictional test file.
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
- [ ] validate.sh --strict passes
- [ ] Docs updated (spec, plan, tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
A built-in default with a validated overlay, sent as a difference

### Key Components
- **`figjam-design.md`**: prose that says what each token means and which floors apply, then one `json` block of style tokens and the read-only swatch and tint reference
- **`compose-board.js`**: the built-in design, `const THEME = __THEME__` merged over it and the ranked fixes
- **`compose_board.py`**: reads the built-in design, resolves and validates the file, prints `DESIGN` warnings, fills `__THEME__` and runs `--design-check`
- **The self-test**: pins the swatch pairs and tints to the composer, checks tint hues and the key order and counts the theme in the 50,000-character check

### Data Flow
`compose_board.py` reads the model and the design file. It parses the token block, checks each token and keeps the built-in value for any token that fails. It writes the differing tokens as compact JSON into `__THEME__` and the model into `__MODEL__`. The composer merges the theme over its built-in design and draws the board. The `COMPOSED` line counts the warnings and the Flow reply turns each into a `Finding:` line. In the claude.ai Project the agent fills `__THEME__` by hand from the design Knowledge file, and `{}` draws the default board.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `compose-board.js` | Draws the board | Built-in design, theme merge, ranked fixes | `compose_board.py --self-test` |
| `compose_board.py` | Fills and checks the template | Design resolution, warnings, `--design-check` | Self-test and pytest |
| `flow_check.py` | Checks shipped models | Skips the design file | `flow_check.py --self-test` |
| References and playbook | Rules, rubric and scenarios | Point at the design file, ninth criterion, two scenarios | Benchmark gates |
| Project mirror and kernel | Carry the packet to claude.ai | New Knowledge file, composer step, kernel v1.2.4 | Sync Loop gates in a scratch clone |
| Sync Loop declaration | Lists source and mirror pairs | Learns the new pair | Residency and parity gates |

Required inventories:
- Same-class producers: every literal colour, size and connector look in `compose-board.js`, found by grep before the built-in design is drawn up
- Consumers of changed paths: the Project composer Knowledge file, the playbook scenarios that compose boards, `leaf-manifest.json` and the Sync Loop declaration
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
| Unit | Design parsing, fallback warnings, theme difference, budget | `python3 sk-create-figjam/scripts/compose_board.py --self-test`, `python3 -m pytest -q scripts/tests` |
| Unit | Model checks | `python3 sk-create-figjam/scripts/flow_check.py --self-test` |
| Integration | The packet and its mirrors | `bash benchmark/gates/run_gates.sh` with `VENDOR_UPSTREAM_ROOT` set to the scratch clone named in the run notes, then the Sync Loop residency, parity, output format and reference parity gates in a scratch clone |
| Manual | Board look | The gallery recomposed on the fictional test file and read by eye, the two new playbook scenarios and a fresh Opus high review |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 036 research | Internal | Complete | None |
| Figma connector with `use_figma` | External | Needed for the gallery step | The gallery cannot be recomposed |
| A scratch clone for the Sync Loop and vendor gates | Internal | Named in the run notes | Gates cannot run against a committed declaration |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails and cannot be fixed in scope, or the operator rejects the new look
- **Procedure**: Revert the changed tracked files with `git checkout -- <path>` on the operator's approval and delete the new design file, Knowledge file and changelogs
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core |
| Core | Setup | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | 30 minutes |
| Core Implementation | High | 6 hours |
| Verification | Med | 3 hours |
| **Total** | | **9.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Backup created: the last commit holds every file this phase changes
- [ ] Feature flag: not applicable, D6 keeps one behaviour
- [ ] Monitoring: the self-test count and the template character count before and after

### Rollback Procedure
1. Stop the work
2. Revert the changed tracked files on the operator's approval
3. Delete the new files this phase created
4. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

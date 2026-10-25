---
title: "Decision Record: FigJam design spec"
description: "Nine decisions for the FigJam design spec build: one design file inside the skill, a built-in default with a theme of differences, fallback with a warning, plain JSON tokens, style tokens only, no layout switches, white participants, the Project mirror now and the character budget."
trigger_phrases:
  - "figjam design spec decision"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/037-figjam-design-spec"
    last_updated_at: "2026-10-25T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded the nine build decisions"
    next_safe_action: "Record the baseline and start task T002"
---
# Decision Record: FigJam design spec

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: One design file inside the skill

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The operator, who answered "Inside the skill ofc" on 2026-10-25 |

---

<!-- ANCHOR:adr-001-context -->
### Context

Research Section 6.1 proposed three layers: a packet default, an optional override beside the system `AGENTS.md` and a per-run `--design` flag, resolved token by token. Research question 1 asked whether the override should be tracked or local.

### Constraints
- One user restyles boards for the whole system, so a team choice and a personal one are the same file here.
- Every extra layer is another file the Project must mirror and another path the self-test must cover.

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: Ship one design file at `sk-create-figjam/assets/figjam-design.md`, with no system-root override and no per-run override flag.

**Details**: Editing that file restyles every board. It is written as a smaller FigJam form of the DESIGN.md Style Reference: prose sections that say what each token means and which floors apply, then one fenced `json` token block. Research Section 6.2 gives what is kept, replaced and dropped from the Style Reference.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **One file inside the skill** | One place to edit and one file to mirror | A change is a tracked edit to the skill | 9/10 |
| Three layers with precedence | A one-off restyle without touching the skill | Three paths to resolve, test and mirror | 5/10 |
| A file at the system root | Sits beside `AGENTS.md` | Splits the skill's assets across two folders | 4/10 |

**Why Chosen**: The operator chose it, and it keeps one source for the style.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- Every board, the Project mirror and the self-test read one file.

**Negative**:
- A one-off restyle edits the shipped file. Mitigation: the edit is a tracked change that git reverts.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: The new design file and the readers in `compose_board.py` that load it.

**How to roll back**: Delete the file. The composer's built-in design draws every board.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->

---

<!-- ANCHOR:adr-002 -->
## ADR-002: A built-in default and a theme of differences

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator in the phase brief of 2026-10-25, from research Section 6.5 |

---

<!-- ANCHOR:adr-002-context -->
### Context

The claude.ai Project runs no script, so its agent fills the template by hand. One `use_figma` call takes 50,000 characters of code and a full resolved theme would cost about 4,000 of them.

### Constraints
- An empty theme must draw the default board.
- The Project's copy of the composer must stay byte-equal to `--template`.

<!-- /ANCHOR:adr-002-context -->

---

<!-- ANCHOR:adr-002-decision -->
### Decision

**Summary**: The composer keeps a built-in default design, the factory values, and `compose_board.py` sends only the tokens that differ through a new `__THEME__` placeholder beside `__MODEL__`.

**Details**: `compose_board.py` reads the built-in design from the composer source, resolves the design file over it and validates it. The shipped design file equals the built-in design, so the shipped theme is `{}`.

<!-- /ANCHOR:adr-002-decision -->

---

<!-- ANCHOR:adr-002-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Built-in default plus differences** | Small theme, works with no script | Two copies of the factory values, pinned by the self-test | 9/10 |
| Send the whole resolved theme | One source at run time | Costs about 4,000 characters per call | 4/10 |
| Generate the composer from the file | No duplicate values | A build step and a Project copy that drifts | 3/10 |

**Why Chosen**: It fits the budget and keeps the Project working without a script.

<!-- /ANCHOR:adr-002-alternatives -->

---

<!-- ANCHOR:adr-002-consequences -->
### Consequences

**Positive**:
- The Project can paste `{}` and get the default board.

**Negative**:
- The factory values live in the composer and in the design file. Mitigation: the self-test fails when they differ.

**Risks**: A composer literal missed by the built-in design. Mitigation: the grep inventory in task T003.

<!-- /ANCHOR:adr-002-consequences -->

---

<!-- ANCHOR:adr-002-impl -->
### Implementation

**What changes**: `compose-board.js` gains the built-in design and the theme merge. `compose_board.py` gains the reader and the placeholder fill.

**How to roll back**: Revert both files. The placeholder disappears with them.

<!-- /ANCHOR:adr-002-impl -->
<!-- /ANCHOR:adr-002 -->

---

<!-- ANCHOR:adr-003 -->
## ADR-003: Fall back with a warning on a bad design

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The operator, who chose "Fall back with a warning" on 2026-10-25 |

---

<!-- ANCHOR:adr-003-context -->
### Context

Research Section 6.6 proposed refusing the board before the call on a structural error and reverting one token on a floor miss. Research question 2 asked which the operator wanted.

### Constraints
- A board drawn in defaults after a user edit must never look like a success.
- One bad token should not block a board the rest of the design draws well.

<!-- /ANCHOR:adr-003-context -->

---

<!-- ANCHOR:adr-003-decision -->
### Decision

**Summary**: A bad design falls back with a warning and the board is still drawn.

**Details**: A missing, duplicated or unparseable token block or an unknown schema version makes the whole design fall back to the built-in one with one warning. An unknown group or token, an unknown swatch or tint name, a wrong value type or a value that misses a floor makes that one token fall back, and the warning names it. Warnings print as `DESIGN` lines on stderr, the `COMPOSED` line counts them and each becomes a `Finding:` line in the Flow reply.

<!-- /ANCHOR:adr-003-decision -->

---

<!-- ANCHOR:adr-003-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Fall back with a warning** | The board always draws and the user sees each miss | A user who skips the reply misses the warning | 8/10 |
| Refuse before the call | No silent defaults | One typo blocks every board | 5/10 |

**Why Chosen**: The operator chose it. The warning reaching the reply keeps the fallback from passing as a success.

<!-- /ANCHOR:adr-003-alternatives -->

---

<!-- ANCHOR:adr-003-consequences -->
### Consequences

**Positive**:
- A design edit never stops a board from drawing.

**Negative**:
- A broken block draws default boards until the user reads the finding. Mitigation: the `COMPOSED` line and the reply both carry the count.

**Risks**: A warning dropped on its way to the reply. Mitigation: the broken-design playbook scenario expects the `Finding:` lines.

<!-- /ANCHOR:adr-003-consequences -->

---

<!-- ANCHOR:adr-003-impl -->
### Implementation

**What changes**: The validator and the warning output in `compose_board.py`, and the Flow reply rule that turns each warning into a finding.

**How to roll back**: Revert `compose_board.py` and the reply rule.

<!-- /ANCHOR:adr-003-impl -->
<!-- /ANCHOR:adr-003 -->

---

<!-- ANCHOR:adr-004 -->
## ADR-004: Plain JSON tokens with swatch names

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator in the phase brief of 2026-10-25 |

---

<!-- ANCHOR:adr-004-context -->
### Context

Research Section 6.2 proposed the Design Tokens Community Group shape, `$value` with optional `$type` and aliases in braces. Research question 5 asked whether off-palette hex should be allowed.

### Constraints
- The file is edited by hand.
- No tool in the packet consumes DTCG.
- A custom colour drops out of FigJam's colour picker.

<!-- /ANCHOR:adr-004-context -->

---

<!-- ANCHOR:adr-004-decision -->
### Decision

**Summary**: Write tokens as plain JSON with swatch names, so a role reads `"goal": "lightGreen"`.

**Details**: FigJam's swatch pairs and section tints are listed in the block as read-only reference and pinned to the composer by the self-test, so a board stays recolourable from FigJam's picker. Off-palette hex is not supported and stays deferred.

<!-- /ANCHOR:adr-004-decision -->

---

<!-- ANCHOR:adr-004-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Plain JSON with swatch names** | Short and easy to edit by hand | Not a standard shape | 9/10 |
| DTCG `$value` tokens | A published shape | Longer to type, no consumer gains from it | 4/10 |
| Raw hex per role | Any colour | Leaves FigJam's palette and its picker | 3/10 |

**Why Chosen**: It is the shortest correct form for a hand-edited file.

<!-- /ANCHOR:adr-004-alternatives -->

---

<!-- ANCHOR:adr-004-consequences -->
### Consequences

**Positive**:
- A role change is one word.

**Negative**:
- No brand colours. Mitigation: recorded as deferred, research open question 5.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-004-consequences -->

---

<!-- ANCHOR:adr-004-impl -->
### Implementation

**What changes**: The token block format in `figjam-design.md` and its parser in `compose_board.py`.

**How to roll back**: Revert the file and the parser.

<!-- /ANCHOR:adr-004-impl -->
<!-- /ANCHOR:adr-004 -->

---

<!-- ANCHOR:adr-005 -->
## ADR-005: Style tokens only

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator in the phase brief of 2026-10-25, from research Sections 6.3 and 7 |

---

<!-- ANCHOR:adr-005-context -->
### Context

Research Section 6.3 listed `space` and `rhythm` groups beside the style groups. The router's clearances are measured against the spacing, and the style guide says a cramped board is fixed in the model, not by changing the steps.

### Constraints
- A user cannot see the invariants the router and layout hold.

<!-- /ANCHOR:adr-005-context -->

---

<!-- ANCHOR:adr-005-decision -->
### Decision

**Summary**: Tokens carry style values only.

**Details**: The tokens are colour by role (17 roles), the accent pair and its two weights, each kind's role and key words, the type family and seven sizes, the connector colours and weight, the zone tint cycle and the key's words and tint. Spacing, rhythm, the router's constants and the layout stay the composer's.

<!-- /ANCHOR:adr-005-decision -->

---

<!-- ANCHOR:adr-005-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Style values only** | No token can break routing | Spacing cannot be restyled | 9/10 |
| Expose spacing and rhythm | More control | A user can break clearances they cannot see | 3/10 |

**Why Chosen**: It keeps every invariant the router depends on out of reach.

<!-- /ANCHOR:adr-005-alternatives -->

---

<!-- ANCHOR:adr-005-consequences -->
### Consequences

**Positive**:
- Any valid design draws a board the router can route.

**Negative**:
- A denser or looser board needs a composer change.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-005-consequences -->

---

<!-- ANCHOR:adr-005-impl -->
### Implementation

**What changes**: The token groups the design file and the validator accept.

**How to roll back**: Not needed, nothing outside the composer moves.

<!-- /ANCHOR:adr-005-impl -->
<!-- /ANCHOR:adr-005 -->

---

<!-- ANCHOR:adr-006 -->
## ADR-006: No layout switches

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator in the phase brief of 2026-10-25 |

---

<!-- ANCHOR:adr-006-context -->
### Context

The research proposed each layout fix as a token with today's behaviour as the default: `key.order`, `key.width`, `zone.align`, `zone.tintPolicy` and `titleBlock.noOrphan`.

### Constraints
- The template has little room under the 50,000-character limit.
- Nobody asked for the old look.

<!-- /ANCHOR:adr-006-context -->

---

<!-- ANCHOR:adr-006-decision -->
### Decision

**Summary**: The improved behaviour from the ranked fixes is the only behaviour.

**Details**: Canonical key order, the key at the diagram's width, zone tops aligned in a row, a balanced subtitle and tints that avoid member hues ship with no switch. Keeping both paths would double the code under a tight character budget.

<!-- /ANCHOR:adr-006-decision -->

---

<!-- ANCHOR:adr-006-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **One behaviour** | Half the code, one look to test | No way back to the old look | 9/10 |
| A token per fix | The old look on request | Two paths per fix inside the budget | 3/10 |

**Why Chosen**: It pays for the fixes inside the budget.

<!-- /ANCHOR:adr-006-alternatives -->

---

<!-- ANCHOR:adr-006-consequences -->
### Consequences

**Positive**:
- The self-test and the gallery check one behaviour.

**Negative**:
- Every existing board looks different when recomposed.

**Risks**: A fix that reads worse on one type. Mitigation: the gallery is recomposed and read by eye.

<!-- /ANCHOR:adr-006-consequences -->

---

<!-- ANCHOR:adr-006-impl -->
### Implementation

**What changes**: The ranked fixes land in `compose-board.js` with no token behind them.

**How to roll back**: Revert the composer.

<!-- /ANCHOR:adr-006-impl -->
<!-- /ANCHOR:adr-006 -->

---

<!-- ANCHOR:adr-007 -->
## ADR-007: White sequence participants

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The operator, who chose "White participants" on 2026-10-25 |

---

<!-- ANCHOR:adr-007-context -->
### Context

Five kinds draw light blue today. Research Rank 3 and question 4 asked whether participants should be drawn white or keep light blue as their own named role.

### Constraints
- The style guide says a colour means the same thing on every board.

<!-- /ANCHOR:adr-007-context -->

---

<!-- ANCHOR:adr-007-decision -->
### Decision

**Summary**: Sequence participants are drawn white with the neutral stroke.

**Details**: Light blue then means where a reader starts, plus the named gateway and in-progress roles.

<!-- /ANCHOR:adr-007-decision -->

---

<!-- ANCHOR:adr-007-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **White participants** | Light blue reads as start on every type | Every sequence board changes look | 8/10 |
| Keep light blue as a participant role | No change to sequence boards | Light blue keeps two meanings | 4/10 |

**Why Chosen**: The operator chose it, and it gives light blue one meaning.

<!-- /ANCHOR:adr-007-alternatives -->

---

<!-- ANCHOR:adr-007-consequences -->
### Consequences

**Positive**:
- The sequence board's first glance moves to the accent.

**Negative**:
- Every sequence board and the gallery change.

**Risks**: None beyond the recomposed gallery.

<!-- /ANCHOR:adr-007-consequences -->

---

<!-- ANCHOR:adr-007-impl -->
### Implementation

**What changes**: The participant kind's role in the composer, the design file and the sequence reference.

**How to roll back**: Set the participant role back in the design file.

<!-- /ANCHOR:adr-007-impl -->
<!-- /ANCHOR:adr-007 -->

---

<!-- ANCHOR:adr-008 -->
## ADR-008: The Project gets the design in this phase

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The operator, who said "Actually dont hold but add" on 2026-10-25 |

---

<!-- ANCHOR:adr-008-context -->
### Context

Research question 6 asked whether to accept the kernel change now or hold the Project at defaults until the kernel review.

### Constraints
- A Project cannot read a local file and runs no script.
- Kernel changes follow the manual parity method in `SYNC.md`.

<!-- /ANCHOR:adr-008-context -->

---

<!-- ANCHOR:adr-008-decision -->
### Decision

**Summary**: Add the design to the claude.ai Project in this phase.

**Details**: One new Knowledge file, `Product Owner - Assets - Flow Board Design.md`, mirrors the design file. The composer Knowledge steps gain the `__THEME__` line. One clause is added to `claude project/Custom Instructions.md` and the kernel version moves from v1.2.3 to v1.2.4.

<!-- /ANCHOR:adr-008-decision -->

---

<!-- ANCHOR:adr-008-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Add now** | The Project and the CLI draw the same boards | A kernel edit in this phase | 8/10 |
| Hold at defaults | No kernel edit | The Project cannot restyle and drifts from the skill | 4/10 |

**Why Chosen**: The operator chose it.

<!-- /ANCHOR:adr-008-alternatives -->

---

<!-- ANCHOR:adr-008-consequences -->
### Consequences

**Positive**:
- Both surfaces read one design.

**Negative**:
- The kernel review is still a human step. Mitigation: recorded in `SYNC.md` only after the operator confirms it.

**Risks**: Mirror drift. Mitigation: the Sync Loop parity and reference parity gates.

<!-- /ANCHOR:adr-008-consequences -->

---

<!-- ANCHOR:adr-008-impl -->
### Implementation

**What changes**: The new Knowledge file, the composer Knowledge steps, the kernel and the Sync Loop declaration.

**How to roll back**: Delete the Knowledge file and revert the kernel, the composer Knowledge file and the declaration.

<!-- /ANCHOR:adr-008-impl -->
<!-- /ANCHOR:adr-008 -->

---

<!-- ANCHOR:adr-009 -->
## ADR-009: Pay for the theme inside the 50,000-character budget

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator in the phase brief of 2026-10-25 |

---

<!-- ANCHOR:adr-009-context -->
### Context

One `use_figma` call takes 50,000 characters of code. The compact template measured 43,623 characters before this phase, and the theme plumbing and the fixes add code.

### Constraints
- The model and the theme share what the template leaves.

<!-- /ANCHOR:adr-009-context -->

---

<!-- ANCHOR:adr-009-decision -->
### Decision

**Summary**: Compact the constants to pay for the theme plumbing and the fixes, and count the theme toward the same 50,000-character check.

**Details**: The existing check runs on the filled code, so a large theme fails the same way a large model does.

<!-- /ANCHOR:adr-009-decision -->

---

<!-- ANCHOR:adr-009-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Compact and count the theme** | One limit, one check | Compaction work first | 9/10 |
| A separate theme cap | Simple to state | A second limit that can disagree with the first | 5/10 |

**Why Chosen**: The real limit is the call, so the check should measure the whole call.

<!-- /ANCHOR:adr-009-alternatives -->

---

<!-- ANCHOR:adr-009-consequences -->
### Consequences

**Positive**:
- No call fails at Figma for size.

**Negative**:
- Compact constants read less easily. Mitigation: the design file carries the meaning in prose.

**Risks**: The fixes outgrow the budget. Mitigation: task T002 records the baseline and each fix is measured.

<!-- /ANCHOR:adr-009-consequences -->

---

<!-- ANCHOR:adr-009-impl -->
### Implementation

**What changes**: The constants in `compose-board.js` and the size check in `compose_board.py`.

**How to roll back**: Revert both files.

<!-- /ANCHOR:adr-009-impl -->
<!-- /ANCHOR:adr-009 -->

---

<!-- ANCHOR:adr-010 -->
## ADR-010: Recompose the gallery in phase 038, as part of a model comparison

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The operator, in the session of 2026-10-25 |

---

<!-- ANCHOR:adr-010-context -->
### Context

Task T030 recomposes the gallery boards with the new composer. Figma was not connected in this session until the build and the review were done. Once it was, the operator asked for DeepSeek V4.1 Flash max, GLM 5.3 Flash max and SWE 2 Max to each run the seven board-quality scenarios, to see which model builds FigJam boards best.

<!-- /ANCHOR:adr-010-context -->

---

<!-- ANCHOR:adr-010-decision -->
### Decision

**We chose**: Phase 038 runs the seven board-quality scenarios on each of the three models and recomposes the gallery from the best board of each type. Phase 037 closes without the gallery.

**How it works**: Task T030 and the gallery half of AC-007 are superseded by phase 038. The review half of AC-007 stays here and is met.

<!-- /ANCHOR:adr-010-decision -->

---

<!-- ANCHOR:adr-010-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Gallery from the comparison in 038** | One pass makes the gallery and answers the model question | The gallery waits for the comparison | 9/10 |
| Recompose the gallery here first | 037 closes complete | The same boards are drawn twice | 5/10 |

**Why Chosen**: The comparison composes every type anyway, so its best boards are the gallery.

<!-- /ANCHOR:adr-010-alternatives -->

---

<!-- ANCHOR:adr-010-consequences -->
### Consequences

**Positive**:
- The design file ships now, and the gallery shows boards a graded run produced.

**Negative**:
- Until 038 lands, the screenshots show the composer before this phase. Mitigation: the implementation summary says so.

**Risks**: None beyond the comparison's own.

<!-- /ANCHOR:adr-010-consequences -->

---

<!-- ANCHOR:adr-010-impl -->
### Implementation

**What changes**: Task T030 and AC-007 point at phase 038.

**How to roll back**: Recompose the gallery here and mark T030 done.

<!-- /ANCHOR:adr-010-impl -->
<!-- /ANCHOR:adr-010 -->

---
title: Deep Research Strategy Template
description: Runtime template copied to research/ during initialization to track research progress, focus decisions, and outcomes across iterations.
trigger_phrases:
  - "deep research strategy"
  - "research strategy template"
  - "research session tracking"
  - "exhausted research approaches"
  - "research stop conditions"
  - "ruled out research directions"
importance_tier: normal
contextType: planning
version: 1.14.0.19
---

# Deep Research Strategy - Session Tracking Template

Runtime template copied to `{spec_folder}/research/` during initialization. Tracks research progress across iterations.

## 1. OVERVIEW

### Purpose

Serves as the "persistent brain" for a deep research session. Records what to investigate, what worked, what failed, and where to focus next. Read by the orchestrator and agents at every iteration.

### Usage

- **Init:** Orchestrator copies this template to `{spec_folder}/research/deep-research-strategy.md` and populates Topic, Key Questions, Known Context, and Research Boundaries from config and memory context.
- **Per iteration:** Agent reads Next Focus, writes iteration evidence, and the reducer refreshes What Worked/Failed, answered questions, carried-forward questions, ruled-out directions, and Next Focus.
- **Mutability:** Mutable — analyst-owned sections remain stable, while machine-owned sections are rewritten by the reducer after each iteration. Section 3 is a generated projection from the reducer registry.
- **Protection:** Shared state with explicit ownership boundaries. Orchestrator validates consistency on resume.

### Question Injection Surface

Use `{spec_folder}/research/inbox.jsonl` to append external questions during an active run. Each line is one JSON object with:

- `id`: stable inbox record identifier
- `text`: question text to promote
- `source`: concrete source label, such as an angle bank entry, analyst strategy, or operator note
- `origin`: one of `angle-bank`, `analyst-strategy`, `operator`, or `legacy-import`
- `injectedAtIteration`: iteration number when the question was introduced
- `promotedQuestionId`: promoted registry question id, or `null` until promotion

The reducer reads the inbox on every reduce step and carries `origin` into the question registry and dashboard badges. Direct edits to Section 3 still work as a compatibility path, but they are attributed as `legacy-import`.

Question ownership is explicit:

- Inbox rows are immutable input.
- The reducer registry is canonical question state.
- Section 3 is rendered only from the registry view.

When an inbox row targets an existing registry question but carries different text, the reducer keeps the registry value, records `operatorDecision: needs_decision`, and appends a `question_conflict` event with both `inboxValue` and `registryValue`.

---

## 2. TOPIC
How can the FigJam boards that Product Owner's sk-create-figjam packet composes look better and stay consistent across all seven diagram types, and should the packet read a user-editable design spec file (in the spirit of a DESIGN.md Style Reference) so a repository user can restyle every board to their own taste? The packet turns a checked Mermaid model into a framed FigJam board through one use_figma call. Audit its design surface, all under AI Systems/Product Owner/sk-create-figjam/: assets/compose-board.js (the composer that draws frame, title, subtitle, zones, shapes, connectors, key and source line, and holds the palette, type scale and grid), scripts/compose_board.py (fills the model and runs the self-test), assets/flow-templates.md, assets/templates/*.md, assets/examples/*.md, references/style-guide.md (the palette record and colour by kind), references/quality-rubric.md (the board design rubric in Section 7), references/types/*.md (each type's colour, zones and notes section), references/flow-mode.md (the gate and read-back) and the nine rendered boards in assets/screenshots/*.png with assets/screenshots/README.md naming each one's scenario and score. Open the PNGs when your tool can view images and judge them as a visual designer would: hierarchy and the first glance, alignment and spacing rhythm, type scale and weight, colour harmony and contrast, connector routing and label legibility, zone tints, the key, density, and how alike the seven types feel side by side. When you cannot view images, reason from the composer code and the captions. For the design spec idea, read how the sk-design hub's sk-design-md-generator mode defines a DESIGN.md Style Reference under .skilled/skills/sk-design/sk-design-md-generator/ (SKILL.md, references and assets), and look at public examples of design token files and DESIGN.md style guides for AI agents online. Decide where such a file would live (repository level, packet level or both), its schema (tokens for colour by kind, type, spacing and grid, shape radii and strokes, connector styles and arrowheads, zones, key, title block and source line, plus the first-glance accent), how compose_board.py, the composer and the claude.ai Project mirror would read it, how safe defaults hold when a user edits it badly (validation, contrast floors, fallbacks), and how the quality rubric and the board scorecard would check a board against it. Name what the current boards already do well so nothing good is removed. Every iteration either covers a new part of the design surface, a new diagram type or a new outside source, or deepens an earlier finding and names the iteration it builds on. Cite every claim as [SOURCE: path:line], and name the screenshot file for a visual finding. The synthesis ranks at least 10 design changes, at least 3 of them on consistency across diagram types, each naming the file it changes and its evidence, and ends with a concrete recommendation for the design spec file. Never open AI Systems/Product Context, any Barter board, board URL or Figma file key, and never quote Barter product flows.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] How does the shared composer establish hierarchy, alignment, color, spacing, and connector clarity across all seven types?
- [x] Which current visual strengths should remain, and which screenshot evidence points to the highest-value design changes?
- [x] Should the editable style spec live at packet scope, and what token schema can safely cover shared and type-specific board treatments?
- [x] How should the CLI composer, one-call JavaScript composer, Claude Project mirror, rubric, and scorecard validate the same spec?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS
This research recommends design and maintenance changes only; it does not modify packet sources, access live boards, evaluate Product Context, or quote product flows.

---

## 5. STOP CONDITIONS
Complete exactly two iterations, then synthesize with stopReason maxIterationsReached. Convergence is telemetry only because convergenceMode is off.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- How does the shared composer establish hierarchy, alignment, color, spacing, and connector clarity across all seven types?
- Which current visual strengths should remain, and which screenshot evidence points to the highest-value design changes?
- Should the editable style spec live at packet scope, and what token schema can safely cover shared and type-specific board treatments?
- How should the CLI composer, one-call JavaScript composer, Claude Project mirror, rubric, and scorecard validate the same spec?

<!-- /ANCHOR:answered-questions -->

---

<!-- MACHINE-OWNED: START -->
<!-- ANCHOR:what-worked -->
## 7. WHAT WORKED
[None yet]

<!-- /ANCHOR:what-worked -->

---

<!-- ANCHOR:what-failed -->
## 8. WHAT FAILED
[None yet]

<!-- /ANCHOR:what-failed -->

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
[No exhausted approach categories yet]

<!-- /ANCHOR:exhausted-approaches -->

---

<!-- ANCHOR:ruled-out-directions -->
## 10. RULED OUT DIRECTIONS
[None yet]

<!-- /ANCHOR:ruled-out-directions -->

---

<!-- ANCHOR:divergence-frontier -->
## 10A. SATURATED DIRECTIONS AND DIVERGENCE FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Saturated: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:divergence-frontier -->

---

<!-- ANCHOR:carried-forward-open-questions -->
## 11A. CARRIED-FORWARD OPEN QUESTIONS
- Should the editable style spec live at packet scope, and what token schema can safely cover shared and type-specific board treatments? (iteration 1)
- How should the CLI composer, one-call JavaScript composer, Claude Project mirror, rubric, and scorecard validate the same spec? (iteration 1)
- None for the stated scope; packet changes remain recommendations and would need implementation review. (iteration 2)

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT
Known context: the packet already has a semantic palette, type scale, 8 px grid, contrast gates, layout checks, and a high-scoring screenshot gallery. Inspect packet sources and rendered screenshots; keep the design system and all write activity inside this lineage.

### Bounded Context Snapshot

Populate during initialization when the target is codebase-scoped. Keep this pointer-based and small:

- Source pointers: paths, symbols, or resource-map entries relevant to the topic.
- Reuse candidates: existing utilities, patterns, docs, or agents worth extending.
- Integration points: files or contracts the research is likely to touch.
- Constraints and risks: scope limits, stale graph or memory gaps, and known non-goals.

Do not inline full source bodies. Do not dispatch the retired standalone context loop. Use `@context` for one-shot retrieval, and use this snapshot only to seed the research loop.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 0.05
- Convergence threshold: [from config]
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true (default)
- research/research.md ownership: workflow-owned canonical synthesis output
- Lifecycle branches: `resume`, `restart` (live); `fork`, `completed-continue` (deferred, not runtime-wired)
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A, including Section 10A pivot lineage
- Question injection surface: `{spec_folder}/research/inbox.jsonl`
- Question conflict owner: reducer registry; `question_conflict` events surface inbox/registry disagreements for operator decision
- Canonical pause sentinel: `research/.deep-research-pause`
- Capability matrix: `.skilled/skills/system-deep-loop/deep-research/assets/runtime-capabilities.json`
- Capability matrix doc: `.skilled/skills/system-deep-loop/deep-research/references/guides/capability-matrix.md`
- Capability resolver: `.skilled/skills/system-deep-loop/deep-research/scripts/runtime-capabilities.cjs`
- Current generation: 1
- Started: 2026-10-25T19:16:12Z

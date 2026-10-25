# Deep Research Strategy - Session Tracking

Lineage: `swe` (fan-out of `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system`, executor `cli-devin`, model `swe-2-max`).

## 1. OVERVIEW

### Purpose

Serves as the "persistent brain" for this deep research lineage. Records what to investigate, what worked, what failed, and where to focus next. Read by the executor at every iteration.

### Usage

- **Init:** Populated with Topic, Key Questions, Known Context, and Research Boundaries from the lineage config.
- **Per iteration:** The executor reads Next Focus, writes iteration evidence, and the reducer refreshes What Worked/Failed, answered questions, carried-forward questions, ruled-out directions, and Next Focus.
- **Mutability:** Mutable — analyst-owned sections remain stable, while machine-owned sections are rewritten by the reducer after each iteration. Section 3 is a generated projection from the reducer registry.

---

## 2. TOPIC

How can the FigJam boards that Product Owner's sk-create-figjam packet composes look better and stay consistent across all seven diagram types, and should the packet read a user-editable design spec file (in the spirit of a DESIGN.md Style Reference) so a repository user can restyle every board to their own taste? The audit covers `AI Systems/Product Owner/sk-create-figjam/`: `assets/compose-board.js` (composer: frame, title, subtitle, zones, shapes, connectors, key, source line; holds palette, type scale, grid), `scripts/compose_board.py`, `assets/flow-templates.md`, `assets/templates/*.md`, `assets/examples/*.md`, `references/style-guide.md`, `references/quality-rubric.md` (Section 7 board design rubric), `references/types/*.md`, `references/flow-mode.md`, and the nine rendered boards in `assets/screenshots/*.png` with `assets/screenshots/README.md`. The design-spec question reads `.skilled/skills/sk-design/sk-design-md-generator/` for its Style Reference model plus public design-token/DESIGN.md examples.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] What does the sk-create-figjam composer's design surface control today — palette, type scale, grid, zones, shapes, connectors, key, title block and source line — and where is each value set in compose-board.js and the packet references?
- [x] How well do the nine rendered boards in assets/screenshots hold up as visual design — first-glance hierarchy, alignment and spacing rhythm, type scale and weight, colour harmony and contrast, connector routing and label legibility, zone tints, the key, and density?
- [x] Where do the seven diagram types diverge in colour, zones and layout, which divergences are deliberate per-type identity and which are inconsistencies to unify?
- [x] Should the packet read a user-editable design spec file in the spirit of a DESIGN.md Style Reference, and if so where would it live, what schema would it carry, how would compose_board.py, the composer and the claude.ai Project mirror read it, and how would validation keep bad edits safe?
- [x] What do the current boards already do well that must be preserved, and how should the quality rubric and board scorecard check a board against a design spec?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS

- Implementation or code changes to sk-create-figjam — this run reports findings and a recommendation only.
- Any write outside `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/lineages/swe` (spec.md write-back, validate.sh, generate-context.js, coverage-graph upsert, git mutations are all out of lineage scope and are recorded as skips, not executed).
- Opening `AI Systems/Product Context`, any Barter board, board URL, or Figma file key, or quoting Barter product flows.
- Re-deciding the merge's job: this lineage produces its own registry, dashboard, strategy, resource-map and research.md; fanout-merge belongs to the parent run.

---

## 5. STOP CONDITIONS

- `config.maxIterations` reached (2 iterations; `stopPolicy: max-iterations`, `convergenceMode: off` — convergence signals are telemetry only).
- The terminal synthesis record must carry `stopReason: "maxIterationsReached"`.
- Lineage-scoped halt: gateway exit 2 (refusal), three failed calls on the same step, or unrecoverable state corruption.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- What does the sk-create-figjam composer's design surface control today — palette, type scale, grid, zones, shapes, connectors, key, title block and source line — and where is each value set in compose-board.js and the packet references?
- How well do the nine rendered boards in assets/screenshots hold up as visual design — first-glance hierarchy, alignment and spacing rhythm, type scale and weight, colour harmony and contrast, connector routing and label legibility, zone tints, the key, and density?
- Where do the seven diagram types diverge in colour, zones and layout, which divergences are deliberate per-type identity and which are inconsistencies to unify?
- Should the packet read a user-editable design spec file in the spirit of a DESIGN.md Style Reference, and if so where would it live, what schema would it carry, how would compose_board.py, the composer and the claude.ai Project mirror read it, and how would validation keep bad edits safe?
- What do the current boards already do well that must be preserved, and how should the quality rubric and board scorecard check a board against a design spec?

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
- Should the packet read a user-editable design spec file in the spirit of a DESIGN.md Style Reference, and if so where would it live, what schema would it carry, how would compose_board.py, the composer and the claude.ai Project mirror read it, and how would validation keep bad edits safe? (iteration 1)
- Where do the seven diagram types diverge in colour, zones and layout, which divergences are deliberate per-type identity and which are inconsistencies to unify? — partially answered by findings 2, 5-7, 13, 15; iteration 2 consolidates per-type divergence against `references/types/*.md` and names which deltas to unify. (iteration 1)
- What do the current boards already do well that must be preserved, and how should the quality rubric and board scorecard check a board against a design spec? — strengths are enumerated in findings 2-4, 8-11; the rubric-integration half remains for iteration 2. (iteration 1)
- None blocking — all five key questions are answered; synthesis ranks the changes. (iteration 2)

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT

### Bounded Context Snapshot

- Source pointers: `AI Systems/Product Owner/sk-create-figjam/` — `assets/compose-board.js`, `scripts/compose_board.py`, `assets/flow-templates.md`, `assets/templates/*.md`, `assets/examples/*.md`, `assets/screenshots/*.png` + `README.md`, `references/style-guide.md`, `references/quality-rubric.md`, `references/types/*.md`, `references/flow-mode.md`.
- Design-spec reference: `.skilled/skills/sk-design/sk-design-md-generator/` (SKILL.md, references, assets) defines the DESIGN.md Style Reference model this question borrows.
- Reuse candidates: the packet's existing palette/type/grid constants in `compose-board.js`, the per-type colour/zones records in `references/types/*.md`, and the Section 7 board rubric in `references/quality-rubric.md`.
- Integration points: `scripts/compose_board.py` (model fill + self-test), the one `use_figma` call the composer emits, and the claude.ai Project mirror that would also need to read a design spec file.
- Constraints and risks: reads only; nine PNGs may not be viewable if the image tool is unavailable (fall back to composer-code reasoning plus `screenshots/README.md` captions); lineage write scope excludes spec.md, coverage-graph DB and repo tooling.
- `resource-map.md` not present; skipping coverage gate.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 2
- Convergence threshold: 0.05 (telemetry only; `convergenceMode: off`, `stopPolicy: max-iterations`)
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true
- research.md ownership: workflow-owned canonical synthesis output at the lineage root
- Lifecycle branches: `new` (this run); `resume`, `restart` live; `fork`, `completed-continue` deferred
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A
- Canonical pause sentinel: `.deep-research-pause` (lineage-local)
- Current generation: 1
- Session: `fanout-swe-1792955293904-icey00`
- Started: 2026-10-25T19:14Z

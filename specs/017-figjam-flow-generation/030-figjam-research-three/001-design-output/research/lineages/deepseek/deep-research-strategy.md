---
title: "Deep Research Strategy - FigJam board legibility lineage (deepseek)"
description: "Strategy file for the deepseek fan-out lineage: how sk-create-figjam can produce FigJam boards that look and read better, and how that quality is measured."
trigger_phrases:
  - "figjam board legibility research"
  - "sk-create-figjam diagram design research"
  - "figjam board quality rubric"
importance_tier: important
contextType: planning
---

# Deep Research Strategy - FigJam Board Legibility (deepseek lineage)

## 1. OVERVIEW

### Purpose
Persistent brain for this lineage. Records what to investigate, what worked, what failed and where to focus next.

### Usage
- **Init:** topic, key questions, known context and boundaries are set here.
- **Per iteration:** the agent writes the iteration narrative and delta, and the reducer refreshes the machine-owned sections.

---

## 2. TOPIC

How can Product Owner's `sk-create-figjam` produce FigJam diagrams that look and read better? The finished board is the unit of study: layout direction and spacing, grouping and sections, visual hierarchy and first eye landing, colour roles/palette/contrast, shape vocabulary, connector routing and labels, density limits and split points, titles/legends/stickies/callouts, text size and label length, and how several diagrams sit on one board. The research separates what `generate_diagram` decides from what the Mermaid input can steer and what `use_figma` extensions add afterwards, compares the packet against the diagram design rules in `sk-design-diagram`/`sk-design-fundamentals` and against public diagram style guides and FigJam guidance, and judges how board quality is measured today.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] Which board qualities does sk-create-figjam decide today, and for each one, does generate_diagram own it, can the Mermaid model steer it, or does a use_figma extension add it afterwards?
- [x] Which diagram design rules in sk-design-diagram and sk-design-fundamentals have no counterpart in the FigJam packet, and which of those gaps can a FigJam board actually carry?
- [x] What layout, spacing, grouping, connector-routing, density and section behaviour do the 22-repo corpus and Figma's own published skills demonstrate that a Mermaid model or the generator can steer?
- [x] How should a board holding several diagrams be composed — titles, sections, legends, reading order and spacing between diagrams — so a reader meets it in the intended order?
- [x] How is board quality measured today across references/quality-rubric.md and the manual-testing-playbook scorecard, and what would measure it better?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS

- Re-proposing changes already implemented from `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/` and `.../016-figjam-improvement-research/`.
- Implementing any change. This lineage reports findings only.
- Editing any file outside `research/lineages/deepseek/`.
- Reading `AI Systems/Product Context`, any screenshot or image file, any figma.com board URL, or anything under a containment folder.
- Quoting Barter product flows. Examples use fictional companies (Fernhouse, Loomlist, Roamstay).

---

## 5. STOP CONDITIONS

- `config.stopPolicy` is `max-iterations`, so the loop runs all 5 iterations and stops with `maxIterationsReached`. Convergence before iteration 5 is telemetry only and broadens review angles instead of synthesizing early.
- A three-failure run on the same call is the only halt condition, per the dispatch contract.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- Which board qualities does sk-create-figjam decide today, and for each one, does generate_diagram own it, can the Mermaid model steer it, or does a use_figma extension add it afterwards?
- Which diagram design rules in sk-design-diagram and sk-design-fundamentals have no counterpart in the FigJam packet, and which of those gaps can a FigJam board actually carry?
- What layout, spacing, grouping, connector-routing, density and section behaviour do the 22-repo corpus and Figma's own published skills demonstrate that a Mermaid model or the generator can steer?
- How should a board holding several diagrams be composed — titles, sections, legends, reading order and spacing between diagrams — so a reader meets it in the intended order?
- How is board quality measured today across references/quality-rubric.md and the manual-testing-playbook scorecard, and what would measure it better?

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
- What layout, spacing, grouping, connector-routing, density and section behaviour do the 22-repo corpus and Figma's own published skills demonstrate that a Mermaid model or the generator can steer? (iteration 1)
- How should a board holding several diagrams be composed? (iteration 1)
- Which diagram design rules in `sk-design-diagram` and `sk-design-fundamentals` have no counterpart in the FigJam packet, and which of those gaps can a FigJam board actually carry? (iteration 1)
- How is board quality measured today, and what would measure it better? (iteration 1)
- How is board quality measured today across `references/quality-rubric.md` and the manual-testing-playbook scorecard, and what would measure it better? (iteration 4)

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT

- Packet under study: `AI Systems/Product Owner/sk-create-figjam/` (SKILL.md, references/flow-mode.md, references/style-guide.md, references/quality-rubric.md, references/hybrid-workflow.md, references/types/*, assets/flow-templates.md, assets/templates/*, assets/examples/*, scripts/flow_check.py, scripts/figjam_checks/*, manual-testing-playbook/).
- Design-rule comparators: `.skilled/skills/sk-design/sk-design-diagram/` (SKILL.md, references/foundations/, references/primitives/, references/types/, references/catalog.md) and `.skilled/skills/sk-design/sk-design-fundamentals/references/` (hierarchy.md, color-system.md, depth-and-detail.md, review-checklist.md, diagnosis-table.md).
- Corpus: 22 public repos under `research/corpus/`, including Figma's own `figma__mcp-server-guide` skills and `figma__architecture-diagram-components`.
- Prior research already implemented: `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md` and `.../016-figjam-improvement-research/research/research.md` sections 1-9.
- `resource-map.md not present; skipping coverage gate`.

### Bounded Context Snapshot
- Source pointers: the packet listed above; `AI Systems/Product Owner/SKILL.md`, `AGENTS.md`, `claude project/Custom Instructions.md`, vendored `mcp-figma/`.
- Integration points: the hosted Figma MCP (`generate_diagram`, `use_figma`, `get_figjam`, `get_screenshot`), the `fj` fallback through `figma-ds-cli`, and `scripts/flow_check.py` as the pre-write gate.
- Constraints and risks: no image or board URL may be read, so on-board appearance must be inferred from tool contracts, published skills and the packet's own read-back rules.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 5
- Convergence threshold: 0.05 (stop policy `max-iterations`)
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true
- `research.md` ownership: workflow-owned canonical synthesis output
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A
- Canonical pause sentinel: `research/lineages/deepseek/.deep-research-pause`
- Current generation: 1
- Started: 2026-10-21T06:24:59.000Z

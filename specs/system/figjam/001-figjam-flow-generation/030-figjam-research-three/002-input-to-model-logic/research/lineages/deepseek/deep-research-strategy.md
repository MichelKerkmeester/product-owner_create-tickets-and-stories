---
title: Deep Research Strategy - FigJam input-to-model extraction
description: Session tracking for the deepseek fan-out lineage that researches how screenshots, Figma flows and product logic become a correct FigJam model.
contextType: planning
version: 1.0.0.0
---

# Deep Research Strategy - Session Tracking

## 1. OVERVIEW

### Purpose

Tracks focus, answers and dead ends for the lineage that studies the input-to-model half of Flow Mode: extraction from screenshots, Figma flows, product docs, specs, Stories, Epics, acceptance criteria and support tickets; inference over that extraction; provenance; gap marking; type choice; chunking; and the pre-gate check against sources.

### Usage

- **Init:** populated from the dispatch prompt.
- **Per iteration:** the iteration file records evidence; the reducer rewrites the machine-owned sections.
- **Mutability:** analyst sections stay stable; section 3 and sections 6 to 11 are reducer-rendered.

---

## 2. TOPIC

How can the AI most reliably turn screenshots, Figma flows and product logic (product docs, specs, Stories, Epics, acceptance criteria, support tickets) into a correct FigJam model? Study extraction and inference: putting a set of screenshots in order, telling a screen from a state, finding the action that moves between screens, spotting error, empty and loading states, reading Figma prototype links and frame names, turning prose rules and acceptance criteria into decisions and branches, merging several sources and resolving conflicts, keeping a provenance trail per node, marking gaps rather than inventing, choosing the diagram type from what the input actually holds, chunking large inputs, and checking the model against its sources before the gate.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] What can a vision-capable model reliably read from a UI screenshot, and which reads must Flow Mode re-check or refuse?
- [x] How should a set of screenshots be ordered into a flow when the filenames carry no step number?
- [x] How should a screen be told apart from a state, and how should loading, empty and error states be modelled?
- [x] How should the action that moves between two screens be found, and what happens when it is only implied?
- [x] What should Flow Mode read from a Figma prototype link, frame name or prototype connection, and which Figma read tool returns it?
- [x] How should prose rules and acceptance criteria become decisions and branches without inventing either?
- [x] How should several sources be merged, conflicts resolved, provenance kept per node and gaps marked?
- [x] How should the diagram type be chosen from what the input actually holds, and how should a large input be chunked?
- [x] How should the model be checked against its sources before the write gate?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS

- Re-proposing the twelve ranks of phase 016 or the fifteen of phase 009. Those are implemented and are read as the baseline.
- The write path, the read-back and the reply shape, except where a read tool limits what the input side can know.
- Barter product flows. Examples use fictional companies such as Fernhouse, Loomlist and Roamstay.
- Any containment folder, screenshot or image file read, `figma.com` board URL, or Product Context material.

---

## 5. STOP CONDITIONS

- `maxIterations` reached (stopPolicy `max-iterations`). Convergence is telemetry only.
- Every iteration must either widen the source set or deepen an earlier finding and name the iteration it builds on.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- What can a vision-capable model reliably read from a UI screenshot, and which reads must Flow Mode re-check or refuse?
- How should a set of screenshots be ordered into a flow when the filenames carry no step number?
- How should a screen be told apart from a state, and how should loading, empty and error states be modelled?
- How should the action that moves between two screens be found, and what happens when it is only implied?
- What should Flow Mode read from a Figma prototype link, frame name or prototype connection, and which Figma read tool returns it?
- How should prose rules and acceptance criteria become decisions and branches without inventing either?
- How should several sources be merged, conflicts resolved, provenance kept per node and gaps marked?
- How should the diagram type be chosen from what the input actually holds, and how should a large input be chunked?
- How should the model be checked against its sources before the write gate?

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
- Figma prototype links, frame names and the read tools behind them. (iteration 1)
- Finding the action between two screens when it is only implied. (iteration 1)
- The pre-gate check of a model against its sources. (iteration 1)
- Screen versus state, and how loading, empty and error states enter a model. (iteration 1)
- Ordering a screenshot set that carries no step numbers. (iteration 1)
- Merging sources, resolving conflicts, provenance per node and marking gaps. (iteration 1)
- Type choice from what the input holds, and chunking a large input. (iteration 1)
- Prose rules and acceptance criteria into decisions and branches. (iteration 1)
- Finding the action between two screens when it is only implied, now that an edge has an actor. (iteration 2)
- What Flow Mode should read from a Figma prototype link, frame name or prototype connection, and which read tool returns it. (iteration 3)
- Merging sources, resolving conflicts, provenance per node and marking gaps in one stated procedure. (iteration 3)
- Whether a `figma.com/proto` URL carries navigation metadata the design URL does not. No corpus source describes its parameters, so this stays unverified and is not claimed. (iteration 4)
- None from the strategy's set. The open items are the claims this lineage could not verify, listed in the synthesis. (iteration 5)

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

- Baseline packet surfaces: `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 (intake), `assets/flow-templates.md` Section 3 (provenance table), `references/quality-rubric.md`, `scripts/flow_check.py`.
- Baseline research: phase 009 and phase 016 syntheses under `AI Systems/Product Owner/specs/017-figjam-flow-generation/`.
- Corpus: 22 public repos under `research/corpus/`, Figma's own `figma__mcp-server-guide` skills among them.
- Vision capability surface: `.skilled/skills/sk-vision/SKILL.md`.
- Read-tool surface: `AI Systems/Product Owner/mcp-figma/` and Figma's developer docs for the MCP server.

---

## 13. RESEARCH BOUNDARIES

- Max iterations: 5
- Convergence threshold: 0.05 (telemetry only; stopPolicy is `max-iterations`)
- Per-iteration budget: 24 tool calls, 20 minutes
- Progressive synthesis: true
- research.md ownership: workflow-owned canonical synthesis output
- Machine-owned sections: reducer controls Sections 3, 6, 7 to 11A
- Question injection surface: not used in this lineage
- Capability matrix: `.skilled/skills/system-deep-loop/deep-research/assets/runtime-capabilities.json`
- Current generation: 1
- Started: 2026-10-21T06:25:54Z

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
How Product Owner can turn screenshots, Figma flows and product docs into FigJam flows, with FigJam as the only output, using the local Figma MCP, transferable diagram rules, an embedded skill, a Claude Code plugin, cross-repository sync and a parent hub.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] What FigJam creation and editing capabilities and limits does the local Figma MCP expose?
- [x] How should Product Owner ingest screenshots, Figma flows, and product documentation into a FigJam-only output?
- [x] Which sk-design-diagram flowchart rules transfer to FigJam, and what must be adapted?
- [x] How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories?
- [x] What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS
[What this research session is NOT trying to answer -- populated during initialization]

---

## 5. STOP CONDITIONS
Complete all 8 iterations; convergence is telemetry only (mode off); terminal stop reason is maxIterationsReached.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- What FigJam creation and editing capabilities and limits does the local Figma MCP expose?
- How should Product Owner ingest screenshots, Figma flows, and product documentation into a FigJam-only output?
- Which sk-design-diagram flowchart rules transfer to FigJam, and what must be adapted?
- How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories?
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?

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
- Which sk-design-diagram flowchart rules transfer to FigJam, and what must be adapted? (iteration 1)
- How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories? (iteration 1)
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub? (iteration 1)
- How should Product Owner ingest screenshots, Figma flows, and product documentation into a FigJam-only output? (iteration 1)
- Which concrete risks should gate the build phases? (iteration 4)
- Which build risks should block or sequence the proposed phases? (iteration 5)
- What should Product Owner copy or avoid from Moneybird Accountant’s parent hub? (iteration 5)
- Which routing mistakes did Moneybird’s reviews uncover, and which of its controls should Product Owner adopt? (iteration 6)
- Which combined architecture risks should sequence the build phases? (iteration 6)
- What integrated risks and ordered implementation phases best fit the findings so far? (iteration 7)
- Whether the current installed figma-ds-cli build exposes the documented FigJam arguments and can safely create/read back a representative board; this run did not perform a live CLI or board check. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:165] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95] (iteration 8)

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT
Phase spec defines research-only scope and FigJam as the sole output. The staging phase spec identifies the local mcp-figma and sk-design-diagram packages, Media Editor plugin and Moneybird hub as required sources.

### Bounded Context Snapshot

Populate during initialization when the target is codebase-scoped. Keep this pointer-based and small:

- Source pointers: paths, symbols, or resource-map entries relevant to the topic.
- Reuse candidates: existing utilities, patterns, docs, or agents worth extending.
- Integration points: files or contracts the research is likely to touch.
- Constraints and risks: scope limits, stale graph or memory gaps, and known non-goals.

Do not inline full source bodies. Do not dispatch the retired standalone context loop. Use `@context` for one-shot retrieval, and use this snapshot only to seed the research loop.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: [from config]
- Convergence threshold: [from config]
- Per-iteration budget: [from config.maxToolCallsPerIteration] tool calls, [from config.maxMinutesPerIteration] minutes
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
- Current generation: [from config.lineage.generation]
- Started: 2026-10-19T21:03:48Z

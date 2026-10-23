---
title: Deep Research Dashboard
description: Auto-generated reducer view over the research packet.
---

# Deep Research Dashboard - Session Overview

Auto-generated from JSONL state log, iteration files, findings registry, and strategy state. Never manually edited.

<!-- ANCHOR:overview -->
## 1. OVERVIEW

Reducer-generated observability surface for the active research packet.

<!-- /ANCHOR:overview -->
<!-- ANCHOR:status -->
## 2. STATUS
- Topic: How can Product Owner's sk-create-figjam packet and its integration with sk-product-owner improve, judged against the public FigJam work online? The packet turns screenshots, Figma flows and product docs into a checked Mermaid model of one of seven types (user flow, process, architecture, sequence, state, ER, gantt) and writes it to FigJam through the hosted Figma MCP generate_diagram tool, with figma-ds-cli fj as the Figma Desktop fallback and use_figma extensions for pins, stickies, tints and legends. Packet sources: AI Systems/Product Owner/sk-create-figjam/SKILL.md, references/flow-mode.md, references/types/*.md, references/style-guide.md, references/quality-rubric.md, references/hybrid-workflow.md, assets/flow-templates.md, assets/templates/*.md, assets/examples/*.md, scripts/flow_check.py, scripts/figjam_checks/*.py and manual-testing-playbook/ (its board quality scorecard in manual-testing-playbook.md Section 3), all under AI Systems/Product Owner/sk-create-figjam/. Integration surfaces: the hub at AI Systems/Product Owner/SKILL.md, ROUTER.md, hub-router.json, mode-registry.json and AGENTS.md; AI Systems/Product Owner/sk-product-owner/SKILL.md, references/router-contract.md, references/interactive-mode.md and references/task-mode.md; the claude.ai kernel AI Systems/Product Owner/claude project/Custom Instructions.md and its Flow Knowledge files under AI Systems/Product Owner/claude project/knowledge/; the vendored AI Systems/Product Owner/mcp-figma/SKILL.md; AI Systems/Product Owner/benchmark/hub-routing-cases.json, benchmark/gates/check_hub.py and benchmark/router/route_contract.py. The corpus is 22 public repos pinned under specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/: figma__mcp-server-guide at a newer commit than phase 009 read (look for what changed, the skills-figquery folder, workflow-skills/generate-project-plan and figma-power), figma__community-resources, figma__architecture-diagram-components, openai__plugins (Figma's skills as OpenAI ships them), lightspeedwp__.github, adobe__spectrum-design-data (a design-system diagram skill), hferello__ai (arch-flow FigJam references), prasantloki__figjam-builder, rrichardsonv__parse-figjam, ecestnrkl__figjam-mcp (a board as LLM context), bluescaban__blueprints (FigJam to spec kit to Mermaid user flows), arinspunk__claude-talk-to-figma-mcp, ulasbilgen__mcp-skills-plugins (get_figjam), tmcw__figjam-mermaid, lauragalera__figjam-erd-plugin, plus the seven phase 009 repos IamTheLime__dotfiles, southleft__figma-console-mcp-skills, mkaralevich__pi-figma-labor, amo-tech-ai__rocket-path-ai, atezer__FMCP, ompug__diagram-codebase and memi-design__mermaid-jam. Half the work is the packet against the corpus: diagram types and kinds the packet lacks, model rules and checks, layout, colour and density, read-back and how a board's quality is measured, revision and fileKey reuse, extensions, failure and retry, and delivery. The other half is the integration: how a request reaches the packet and hands back, whether a Story, Epic, Doc, Task or Bug from sk-product-owner should carry or link a FigJam diagram and how, whether a board URL should reach ClickUp through the vendored mcp-click-up, how the claude.ai Project runs Flow without a Figma connector, and where the hub routing, the kernel router and the playbooks leave gaps. Name what the packet already does better than the corpus, so nothing good is removed. Never stop early: every iteration either widens the corpus (a new repo found with gh search, a new file or a new question) or deepens an earlier finding, and names the earlier iteration it builds on. Cite every claim as [SOURCE: path:line]. The synthesis ranks at least 10 improvements, at least 3 of them on the integration, each naming the Product Owner file it changes and the corpus or Product Owner file it comes from. Never open AI Systems/Product Context, any screenshot, any board URL or anything under a containment folder, and never quote Barter product flows.
- Started: 2026-10-20T20:13:00.419Z
- Status: COMPLETE
- Iteration: 10 of 10
- Session ID: fanout-deepseek-1792527089584-nrdj43
- Parent Session: none
- Lifecycle Mode: new
- Generation: 1
- continuedFromRun: none
- stopReason: maxIterationsReached

<!-- /ANCHOR:status -->
<!-- ANCHOR:progress -->
## 3. PROGRESS

| # | Focus | Track | Ratio | Findings | Status |
|---|-------|-------|-------|----------|--------|
| 1 | Packet baseline: what sk-create-figjam already enforces (SKILL.md, flow-mode, rubric, style guide, flow_check.py, playbook scorecard) | - | 1.00 | 10 | complete |
| 2 | figma__mcp-server-guide newer commit: mandatory pre-call skill, universal constraints, figma-use-figjam, generate-project-plan layout and diagram-section recipe | - | 0.88 | 12 | complete |
| 3 | Three public distributions of Figma diagram skill and the packet type grammar against Figma own flowchart rules | - | 0.85 | 11 | complete |
| 4 | Board read-back, snapshot diff and revision history across five public projects | - | 0.90 | 12 | complete |
| 5 | FigJam builders and converters: board-quality grammar, extra diagram kinds, reverse round trip | - | 0.86 | 11 | complete |
| 6 | Design-system diagram house style, independent architecture lanes, and a publish manifest | - | 0.92 | 13 | complete |
| 7 | Two-stage routing, the one-way Flow handoff, and where a board can legitimately land in an artifact | - | 0.88 | 12 | complete |
| 8 | Read-back, revision, fileKey reuse, retry and rollback, read directly | - | 0.85 | 13 | complete |
| 9 | The claude.ai Project without a Figma connector, and the ClickUp carrier for a board URL | - | 0.87 | 13 | complete |
| 10 | Synthesis: twelve ranked improvements, five of them integration changes | - | 0.42 | 12 | complete |

- iterationsCompleted: 10
- keyFindings: 119
- openQuestions: 0
- resolvedQuestions: 5

<!-- /ANCHOR:progress -->
<!-- ANCHOR:questions -->
## 4. QUESTIONS
- Answered: 5/5
- [x] Q1: Which diagram types, diagram kinds and model rules does the public FigJam/Figma corpus expose that the packet's seven types do not cover?
- [x] Q2: Which layout, colour, density and board-quality measurement practices in the corpus exceed the packet's style guide, quality rubric and manual-testing scorecard?
- [x] Q3: How do public projects handle board read-back, revision, fileKey reuse, failure and retry, and delivery, and what does the packet handle differently?
- [x] Q4: How does a Flow request reach sk-create-figjam through the Product Owner hub and sk-product-owner, and where does the handoff back to a Story, Epic, Doc, Task or Bug break?
- [x] Q5: What must the claude.ai kernel and knowledge files change so a Claude Project without a Figma connector can still run Flow, and should a board URL reach ClickUp through the vendored mcp-click-up?

<!-- /ANCHOR:questions -->
<!-- ANCHOR:uncovered-questions -->
## Uncovered Questions
- Count: 0
- None

<!-- /ANCHOR:uncovered-questions -->
<!-- ANCHOR:trend -->
## 5. TREND
- newInfoRatio sparkline: █▇▇▆▆▆▇▇▆▇▇▇▇▆▆▆▆▆▄▁
- score sparkline: █▇▇▆▆▆▇▇▆▇▇▇▇▆▆▆▆▆▄▁
- Last 3 ratios: 0.85 -> 0.87 -> 0.42
- Stuck count: 0
- Guard violations: none recorded by the reducer pass
- convergenceScore: 0.42
- coverageBySources: {"other":62}
- Advisory events: none

<!-- /ANCHOR:trend -->
<!-- ANCHOR:dead-ends -->
## 6. DEAD ENDS
- Judging board visual quality from screenshots or board URLs: the run's constraints forbid opening screenshots or board URLs, so every layout claim must come from documentation, code or the scorecard's written thresholds. Visual scoring is treated as an operator step the packet already defines. (iteration 1)
- No dead end yet; iteration 1 establishes the baseline. The `manual-testing-playbook` scenario files are numerous and were not needed for the baseline beyond Section 3. (iteration 1)
- Treating the packet's seven types as the corpus comparison unit alone: type names differ across projects (flowchart/workflow/architecture/state), so later iterations compare by capability and rule, not by label. (iteration 1)
- Copying the documented `mermaid`/`editorType` call shape into the packet: the corpus contradicts itself, and the packet's runtime schema check is the safer rule. (iteration 2)
- Looking for a new diagram type in the newer commit: the supported-type set is unchanged (`flowchart`, `sequenceDiagram`, `stateDiagram`, `gantt`, `erDiagram`), so any type-coverage improvement must come from another corpus repo, not from this commit. (iteration 2)
- Treating `skills-figquery/` as an independent second source: it is a byte-identical copy of `skills/` for the diagram skill, so citing both would double-count one source. (iteration 2)
- Adopting Figma's eighteen-shape vocabulary for a user flow: the packet's four-shape rule is what lets the check assign one meaning per shape, and the corpus itself warns that most Mermaid shapes silently fall back to rectangles. (iteration 3)
- Counting `openai__plugins` and `lightspeedwp__.github` as independent evidence: one is identical apart from the hybrid workflow reference, the other an older truncated copy, so citing all three as separate sources would inflate the evidence base. (iteration 3)
- Looking for a per-type read-back in the corpus's type references: none exists; the corpus validates before the call and stops at the tool call. (iteration 3)
- Building version history into the packet: it is REST-only, requires a personal access token, and therefore cannot be a claude.ai Project capability. (iteration 4)
- Nothing read this iteration was unusable. `atezer__FMCP` was listed but its skills are design-system and token workflows with no FigJam diagram or read-back surface worth citing here. (iteration 4)
- Treating `get_board_context`'s BM25 retrieval and vision clustering as a read-back model for the packet: those tools interpret a board the packet did not draw, while the packet's read-back has an expected model and exact counts. Their diff and evidence ideas transfer; the retrieval pipeline does not. (iteration 4)
- `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` were listed but not read; their ERD and flow-export surfaces are candidates for a later iteration, not dead ends. The iteration spent its remaining budget on the builder grammar because it bears directly on Q2. (iteration 5)
- Adopting `figjam-builder`'s vibrant palette tiers for diagram fills: its vibrant tier is for board signal sections and stickies, while the packet's diagram fills are governed by a measured contrast gate that the vibrant values would fail. (iteration 5)
- Treating `tmcw__figjam-mermaid` as a full read-back: it reads stickies and connectors only, so it cannot verify shapes, sections, tables or labels. (iteration 5)
- Adopting Adobe's full export-and-embed pipeline inside Flow Mode: it conflicts with the packet's no-file rule and needs a site build; it belongs to a Doc or publication route, not to the board reply. (iteration 6)
- No dead end. The component library was thin on rules but useful as a capability boundary. (iteration 6)
- Treating the architecture component library as a rule source: it is a manual asset library, and its variants cannot be generated. (iteration 6)
- No dead end. The routing files were long but each answered a specific question. (iteration 7)
- Proposing a file attachment pipeline into ClickUp: the templates forbid images and image paths in artifacts, so a link is the only legal carrier. (iteration 7)
- Treating the Flow lane in `router-contract.md` as loadable: the guard drops it by design and the lane exists only for Project knowledge naming. (iteration 7)
- Adopting a preserve-positions update model inside Flow Mode: the packet's generator owns layout, so preserved positions cannot be reconciled with its no-move rule without a hand-built route it does not have. (iteration 8)
- No dead end. The packet's Sections 5 to 9 answered the question directly and the corpus supplied only two genuine divergences. (iteration 8)
- Replacing the model-to-board read-back with a screenshot-only check: the packet's own rule states a picture cannot prove which nodes a connector joins. (iteration 8)
- Attaching a screenshot of the board to a ClickUp task as the carrier: the artifact rules forbid images and image paths, and a picture cannot prove joins. (iteration 9)
- Building a Project-side check script substitute beyond the rule-by-rule mirror: the mirror already converts the script's checks and a Project cannot execute one. (iteration 9)
- Mirroring `mcp-click-up` into the Project: a Project uses its own connector and the packet's CLI verbs do not exist there. (iteration 9)
- No dead end. The kernel and mirror were both explicit, and the only gap was a sentence. (iteration 9)
- No dead end. The ranking was constrained by evidence strength, not by missing material. (iteration 10)
- Proposing a new packet for diagrams. The hub already routes Flow to a sibling packet, and the integration findings are fixes inside existing files. (iteration 10)
- Ranking the source-coverage gaps above the delivery gaps. Coverage reporting is valuable, but the manifest (Rank 4) is what makes coverage trustworthy. (iteration 10)

<!-- /ANCHOR:dead-ends -->
<!-- ANCHOR:divergent-pivots -->
## 6A. DIVERGENT PIVOTS
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Saturated: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:divergent-pivots -->
<!-- ANCHOR:next-focus -->
## 7. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 8. ACTIVE RISKS
- None active beyond normal research uncertainty.

<!-- /ANCHOR:active-risks -->
<!-- ANCHOR:blocked-stops -->
## 9. BLOCKED STOPS
No blocked-stop events recorded.

<!-- /ANCHOR:blocked-stops -->
<!-- ANCHOR:graph-convergence -->
## 10. GRAPH CONVERGENCE
- graphConvergenceScore: 0.00
- graphDecision: [Not recorded]
- graphBlockers: none recorded

<!-- /ANCHOR:graph-convergence -->

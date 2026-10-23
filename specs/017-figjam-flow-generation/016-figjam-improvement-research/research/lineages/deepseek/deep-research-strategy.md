---
title: Deep Research Strategy - Product Owner FigJam Packet Review
importance_tier: normal
contextType: planning
---

# Deep Research Strategy - Session Tracking

## 1. OVERVIEW

Fan-out lineage `deepseek` of the Product Owner FigJam improvement review. The reducer owns Sections 3, 6, 7-11A; this analyst surface owns Topic, Non-Goals, Stop Conditions, Known Context and Boundaries.

---

## 2. TOPIC

How can Product Owner's sk-create-figjam packet and its integration with sk-product-owner improve, judged against the public FigJam work online? The packet turns screenshots, Figma flows and product docs into a checked Mermaid model of one of seven types (user flow, process, architecture, sequence, state, ER, gantt) and writes it to FigJam through the hosted Figma MCP generate_diagram tool, with figma-ds-cli fj as the Figma Desktop fallback and use_figma extensions for pins, stickies, tints and legends. Packet sources: AI Systems/Product Owner/sk-create-figjam/SKILL.md, references/flow-mode.md, references/types/*.md, references/style-guide.md, references/quality-rubric.md, references/hybrid-workflow.md, assets/flow-templates.md, assets/templates/*.md, assets/examples/*.md, scripts/flow_check.py, scripts/figjam_checks/*.py and manual-testing-playbook/ (its board quality scorecard in manual-testing-playbook.md Section 3), all under AI Systems/Product Owner/sk-create-figjam/. Integration surfaces: the hub at AI Systems/Product Owner/SKILL.md, ROUTER.md, hub-router.json, mode-registry.json and AGENTS.md; AI Systems/Product Owner/sk-product-owner/SKILL.md, references/router-contract.md, references/interactive-mode.md and references/task-mode.md; the claude.ai kernel AI Systems/Product Owner/claude project/Custom Instructions.md and its Flow Knowledge files under AI Systems/Product Owner/claude project/knowledge/; the vendored AI Systems/Product Owner/mcp-figma/SKILL.md; AI Systems/Product Owner/benchmark/hub-routing-cases.json, benchmark/gates/check_hub.py and benchmark/router/route_contract.py. The corpus is 22 public repos pinned under specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/: figma__mcp-server-guide at a newer commit than phase 009 read (look for what changed, the skills-figquery folder, workflow-skills/generate-project-plan and figma-power), figma__community-resources, figma__architecture-diagram-components, openai__plugins (Figma's skills as OpenAI ships them), lightspeedwp__.github, adobe__spectrum-design-data (a design-system diagram skill), hferello__ai (arch-flow FigJam references), prasantloki__figjam-builder, rrichardsonv__parse-figjam, ecestnrkl__figjam-mcp (a board as LLM context), bluescaban__blueprints (FigJam to spec kit to Mermaid user flows), arinspunk__claude-talk-to-figma-mcp, ulasbilgen__mcp-skills-plugins (get_figjam), tmcw__figjam-mermaid, lauragalera__figjam-erd-plugin, plus the seven phase 009 repos IamTheLime__dotfiles, southleft__figma-console-mcp-skills, mkaralevich__pi-figma-labor, amo-tech-ai__rocket-path-ai, atezer__FMCP, ompug__diagram-codebase and memi-design__mermaid-jam. Half the work is the packet against the corpus: diagram types and kinds the packet lacks, model rules and checks, layout, colour and density, read-back and how a board's quality is measured, revision and fileKey reuse, extensions, failure and retry, and delivery. The other half is the integration: how a request reaches the packet and hands back, whether a Story, Epic, Doc, Task or Bug from sk-product-owner should carry or link a FigJam diagram and how, whether a board URL should reach ClickUp through the vendored mcp-click-up, how the claude.ai Project runs Flow without a Figma connector, and where the hub routing, the kernel router and the playbooks leave gaps. Name what the packet already does better than the corpus, so nothing good is removed. Never stop early: every iteration either widens the corpus (a new repo found with gh search, a new file or a new question) or deepens an earlier finding, and names the earlier iteration it builds on. Cite every claim as [SOURCE: path:line]. The synthesis ranks at least 10 improvements, at least 3 of them on the integration, each naming the Product Owner file it changes and the corpus or Product Owner file it comes from. Never open AI Systems/Product Context, any screenshot, any board URL or anything under a containment folder, and never quote Barter product flows.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] Q1: Which diagram types, diagram kinds and model rules does the public FigJam/Figma corpus expose that the packet's seven types do not cover?
- [x] Q2: Which layout, colour, density and board-quality measurement practices in the corpus exceed the packet's style guide, quality rubric and manual-testing scorecard?
- [x] Q3: How do public projects handle board read-back, revision, fileKey reuse, failure and retry, and delivery, and what does the packet handle differently?
- [x] Q4: How does a Flow request reach sk-create-figjam through the Product Owner hub and sk-product-owner, and where does the handoff back to a Story, Epic, Doc, Task or Bug break?
- [x] Q5: What must the claude.ai kernel and knowledge files change so a Claude Project without a Figma connector can still run Flow, and should a board URL reach ClickUp through the vendored mcp-click-up?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS

- Never open `AI Systems/Product Context`, any screenshot, any board URL, or anything under a containment folder.
- Never quote or reconstruct Barter product flows.
- No implementation: this run reports ranked improvements and the file each one changes; it does not edit the packet.
- No judging the visual quality of boards that cannot be read as text; layout claims must come from documentation or code.

---

## 5. STOP CONDITIONS

- The run stops at `maxIterations` = 10; convergence is telemetry only (`convergenceMode: off`, `stopPolicy: max-iterations`).
- Every iteration must widen the corpus or deepen an earlier finding and name the iteration it builds on.
- The synthesis must rank at least 10 improvements, at least 3 of them integration, each naming the Product Owner file it changes and the corpus or Product Owner file it comes from.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- Q1: Which diagram types, diagram kinds and model rules does the public FigJam/Figma corpus expose that the packet's seven types do not cover?
- Q2: Which layout, colour, density and board-quality measurement practices in the corpus exceed the packet's style guide, quality rubric and manual-testing scorecard?
- Q3: How do public projects handle board read-back, revision, fileKey reuse, failure and retry, and delivery, and what does the packet handle differently?
- Q4: How does a Flow request reach sk-create-figjam through the Product Owner hub and sk-product-owner, and where does the handoff back to a Story, Epic, Doc, Task or Bug break?
- Q5: What must the claude.ai kernel and knowledge files change so a Claude Project without a Figma connector can still run Flow, and should a board URL reach ClickUp through the vendored mcp-click-up?

<!-- /ANCHOR:answered-questions -->

---

<!-- MACHINE-OWNED: START -->
<!-- ANCHOR:what-worked -->
## 7. WHAT WORKED
- reading the check script alongside the prose contract exposed the real gate boundaries — the script owns drawability, labels, ids, budget and palette, while the rubric owns taste and the playbook owns board scoring. Reading all three separately would have blurred that split. (iteration 1)
- diffing the two skill trees before reading separated a pure redistribution from genuinely new guidance, which prevented double-counting `skills-figquery/` as an independent source. Reading `blocks/diagram-section.md` next to `plan-board-content.md` exposed the one capability the packet structurally cannot do: place a generated diagram inside a board section. (iteration 2)
- diffing the three distributions first prevented a false sense of three independent sources. Reading the checker's constants (`BUDGET`, lane table, decision-exit cap) next to the corpus's prose checklist showed that the packet already automates six of Figma's eight pre-call checks, which reframed the density gap as the main open trade-off rather than a missing rule. (iteration 3)
- reading the source rather than the README for `figjam-context-mcp` produced the two transferable mechanisms — a content-hash snapshot diff and a `modelDerived` provenance flag — that the README only advertises. Reading `parse-figjam` and `connectorGraph.ts` together produced the concrete direction algorithm the packet's read-back assumes but never states. (iteration 4)
- reading `figjam-builder` whole was worth the budget because its audit pass supplied the missing post-write standard — trace every edge, not just count connectors — and its palette tiers gave the corpus's clearest account of why the packet's one-accent rule is a subset rather than a competitor. `mermaid-jam`'s supported-input list answered Q1 directly. (iteration 5)
- reading Adobe's house style and `diagram-codebase`'s design doc together produced the strongest single improvement of the run so far: the packet verifies counts but never traces edges, and both sources independently insist on clarity over counts. hferello's lane file then corroborated the packet's best machine-checked rule instead of adding a competitor. (iteration 6)
- reading the hub, the stage-two map, the packet router and the artifact templates in that order made the seam visible. Each file is internally consistent; the gap appears only when the Flow exemption, the Story image ban and the dropped Flow lane are read together. (iteration 7)
- reading the packet's own error-recovery section against the corpus's update sections produced two real divergences (all-or-nothing revision, no partial update) and one convergence worth keeping (the two-attempt stop). The packet is stronger than expected on failure honesty. (iteration 8)
- reading the kernel's Flow Mode Delivery beside the Flow Knowledge mirror exposed a real one-sentence parity gap that neither file shows alone. The ClickUp section then made the missing offer obvious, because the offer is attached to a Deliverable Block that Flow never renders. (iteration 9)
- ranking by durability and blast radius rather than by novelty surfaced the accent test and the artifact link-back as the two changes with the widest effect for the smallest edit. The integration items clustered naturally once each was tied to a file that already has a slot for it. (iteration 10)

<!-- /ANCHOR:what-worked -->

---

<!-- ANCHOR:what-failed -->
## 8. WHAT FAILED
- nothing failed. The scorecard's line numbers were not in the first `flow-mode` read and needed a targeted grep, which is cheaper than rereading the playbook. (iteration 1)
- the `generate-project-plan` SKILL is 494 lines and reading it whole would have consumed the iteration; targeted greps for approval and verification gates gave the gate structure at a fraction of the cost. (iteration 2)
- the first draft treated shape breadth as a packet weakness. The corpus's own warning that most Mermaid shapes fall back to rectangles shows the packet's four-shape rule is a deliberate defence, not an oversight. (iteration 3)
- `atezer__FMCP` looked promising by name but its skills are design-system and token workflows; a directory listing before reading prevented a wasted pass. (iteration 4)
- two repos were only listed. Their names promised diagram-specific rules, but the builder grammar was more directly relevant to the open questions, so the reads were deliberately deferred rather than skipped silently. (iteration 5)
- the component library had almost no textual rules; it cost one read to establish that the generated path cannot express ownership variants. (iteration 6)
- searching the packet for "figjam" produced forty hits that were mostly routing keywords; the decisive lines were the template Notes For Use and the router contract comment, neither of which mentions FigJam in its heading. (iteration 7)
- the rubric's board section is short and mostly repeats the read-back rule; the unique content was one line about overlaps, which needed the write routes to interpret. (iteration 8)
- grepping for "figjam" in the kernel returned mostly router regexes; the delivery sections were the only substantive content, and they sit far apart in the file. (iteration 9)
- the corpus repeatedly suggested a higher budget, but the packet's no-move rule makes those numbers non-transferable; the ranking had to resist the loudest evidence. (iteration 10)

<!-- /ANCHOR:what-failed -->

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` were listed but not read; their ERD and flow-export surfaces are candidates for a later iteration, not dead ends. The iteration spent its remaining budget on the builder grammar because it bears directly on Q2. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` were listed but not read; their ERD and flow-export surfaces are candidates for a later iteration, not dead ends. The iteration spent its remaining budget on the builder grammar because it bears directly on Q2.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` were listed but not read; their ERD and flow-export surfaces are candidates for a later iteration, not dead ends. The iteration spent its remaining budget on the builder grammar because it bears directly on Q2.

### Adopting `figjam-builder`'s vibrant palette tiers for diagram fills: its vibrant tier is for board signal sections and stickies, while the packet's diagram fills are governed by a measured contrast gate that the vibrant values would fail. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Adopting `figjam-builder`'s vibrant palette tiers for diagram fills: its vibrant tier is for board signal sections and stickies, while the packet's diagram fills are governed by a measured contrast gate that the vibrant values would fail.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting `figjam-builder`'s vibrant palette tiers for diagram fills: its vibrant tier is for board signal sections and stickies, while the packet's diagram fills are governed by a measured contrast gate that the vibrant values would fail.

### Adopting a preserve-positions update model inside Flow Mode: the packet's generator owns layout, so preserved positions cannot be reconciled with its no-move rule without a hand-built route it does not have. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Adopting a preserve-positions update model inside Flow Mode: the packet's generator owns layout, so preserved positions cannot be reconciled with its no-move rule without a hand-built route it does not have.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting a preserve-positions update model inside Flow Mode: the packet's generator owns layout, so preserved positions cannot be reconciled with its no-move rule without a hand-built route it does not have.

### Adopting Adobe's full export-and-embed pipeline inside Flow Mode: it conflicts with the packet's no-file rule and needs a site build; it belongs to a Doc or publication route, not to the board reply. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Adopting Adobe's full export-and-embed pipeline inside Flow Mode: it conflicts with the packet's no-file rule and needs a site build; it belongs to a Doc or publication route, not to the board reply.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting Adobe's full export-and-embed pipeline inside Flow Mode: it conflicts with the packet's no-file rule and needs a site build; it belongs to a Doc or publication route, not to the board reply.

### Adopting Figma's eighteen-shape vocabulary for a user flow: the packet's four-shape rule is what lets the check assign one meaning per shape, and the corpus itself warns that most Mermaid shapes silently fall back to rectangles. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Adopting Figma's eighteen-shape vocabulary for a user flow: the packet's four-shape rule is what lets the check assign one meaning per shape, and the corpus itself warns that most Mermaid shapes silently fall back to rectangles.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting Figma's eighteen-shape vocabulary for a user flow: the packet's four-shape rule is what lets the check assign one meaning per shape, and the corpus itself warns that most Mermaid shapes silently fall back to rectangles.

### Attaching a screenshot of the board to a ClickUp task as the carrier: the artifact rules forbid images and image paths, and a picture cannot prove joins. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Attaching a screenshot of the board to a ClickUp task as the carrier: the artifact rules forbid images and image paths, and a picture cannot prove joins.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Attaching a screenshot of the board to a ClickUp task as the carrier: the artifact rules forbid images and image paths, and a picture cannot prove joins.

### Building a Project-side check script substitute beyond the rule-by-rule mirror: the mirror already converts the script's checks and a Project cannot execute one. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Building a Project-side check script substitute beyond the rule-by-rule mirror: the mirror already converts the script's checks and a Project cannot execute one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Building a Project-side check script substitute beyond the rule-by-rule mirror: the mirror already converts the script's checks and a Project cannot execute one.

### Building version history into the packet: it is REST-only, requires a personal access token, and therefore cannot be a claude.ai Project capability. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Building version history into the packet: it is REST-only, requires a personal access token, and therefore cannot be a claude.ai Project capability.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Building version history into the packet: it is REST-only, requires a personal access token, and therefore cannot be a claude.ai Project capability.

### Copying the documented `mermaid`/`editorType` call shape into the packet: the corpus contradicts itself, and the packet's runtime schema check is the safer rule. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Copying the documented `mermaid`/`editorType` call shape into the packet: the corpus contradicts itself, and the packet's runtime schema check is the safer rule.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Copying the documented `mermaid`/`editorType` call shape into the packet: the corpus contradicts itself, and the packet's runtime schema check is the safer rule.

### Counting `openai__plugins` and `lightspeedwp__.github` as independent evidence: one is identical apart from the hybrid workflow reference, the other an older truncated copy, so citing all three as separate sources would inflate the evidence base. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Counting `openai__plugins` and `lightspeedwp__.github` as independent evidence: one is identical apart from the hybrid workflow reference, the other an older truncated copy, so citing all three as separate sources would inflate the evidence base.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Counting `openai__plugins` and `lightspeedwp__.github` as independent evidence: one is identical apart from the hybrid workflow reference, the other an older truncated copy, so citing all three as separate sources would inflate the evidence base.

### Judging board visual quality from screenshots or board URLs: the run's constraints forbid opening screenshots or board URLs, so every layout claim must come from documentation, code or the scorecard's written thresholds. Visual scoring is treated as an operator step the packet already defines. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Judging board visual quality from screenshots or board URLs: the run's constraints forbid opening screenshots or board URLs, so every layout claim must come from documentation, code or the scorecard's written thresholds. Visual scoring is treated as an operator step the packet already defines.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Judging board visual quality from screenshots or board URLs: the run's constraints forbid opening screenshots or board URLs, so every layout claim must come from documentation, code or the scorecard's written thresholds. Visual scoring is treated as an operator step the packet already defines.

### Looking for a new diagram type in the newer commit: the supported-type set is unchanged (`flowchart`, `sequenceDiagram`, `stateDiagram`, `gantt`, `erDiagram`), so any type-coverage improvement must come from another corpus repo, not from this commit. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Looking for a new diagram type in the newer commit: the supported-type set is unchanged (`flowchart`, `sequenceDiagram`, `stateDiagram`, `gantt`, `erDiagram`), so any type-coverage improvement must come from another corpus repo, not from this commit.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a new diagram type in the newer commit: the supported-type set is unchanged (`flowchart`, `sequenceDiagram`, `stateDiagram`, `gantt`, `erDiagram`), so any type-coverage improvement must come from another corpus repo, not from this commit.

### Looking for a per-type read-back in the corpus's type references: none exists; the corpus validates before the call and stops at the tool call. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Looking for a per-type read-back in the corpus's type references: none exists; the corpus validates before the call and stops at the tool call.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a per-type read-back in the corpus's type references: none exists; the corpus validates before the call and stops at the tool call.

### Mirroring `mcp-click-up` into the Project: a Project uses its own connector and the packet's CLI verbs do not exist there. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Mirroring `mcp-click-up` into the Project: a Project uses its own connector and the packet's CLI verbs do not exist there.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Mirroring `mcp-click-up` into the Project: a Project uses its own connector and the packet's CLI verbs do not exist there.

### No dead end yet; iteration 1 establishes the baseline. The `manual-testing-playbook` scenario files are numerous and were not needed for the baseline beyond Section 3. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: No dead end yet; iteration 1 establishes the baseline. The `manual-testing-playbook` scenario files are numerous and were not needed for the baseline beyond Section 3.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No dead end yet; iteration 1 establishes the baseline. The `manual-testing-playbook` scenario files are numerous and were not needed for the baseline beyond Section 3.

### No dead end. The component library was thin on rules but useful as a capability boundary. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: No dead end. The component library was thin on rules but useful as a capability boundary.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No dead end. The component library was thin on rules but useful as a capability boundary.

### No dead end. The kernel and mirror were both explicit, and the only gap was a sentence. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: No dead end. The kernel and mirror were both explicit, and the only gap was a sentence.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No dead end. The kernel and mirror were both explicit, and the only gap was a sentence.

### No dead end. The packet's Sections 5 to 9 answered the question directly and the corpus supplied only two genuine divergences. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: No dead end. The packet's Sections 5 to 9 answered the question directly and the corpus supplied only two genuine divergences.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No dead end. The packet's Sections 5 to 9 answered the question directly and the corpus supplied only two genuine divergences.

### No dead end. The ranking was constrained by evidence strength, not by missing material. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: No dead end. The ranking was constrained by evidence strength, not by missing material.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No dead end. The ranking was constrained by evidence strength, not by missing material.

### No dead end. The routing files were long but each answered a specific question. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: No dead end. The routing files were long but each answered a specific question.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No dead end. The routing files were long but each answered a specific question.

### Nothing read this iteration was unusable. `atezer__FMCP` was listed but its skills are design-system and token workflows with no FigJam diagram or read-back surface worth citing here. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Nothing read this iteration was unusable. `atezer__FMCP` was listed but its skills are design-system and token workflows with no FigJam diagram or read-back surface worth citing here.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Nothing read this iteration was unusable. `atezer__FMCP` was listed but its skills are design-system and token workflows with no FigJam diagram or read-back surface worth citing here.

### Proposing a file attachment pipeline into ClickUp: the templates forbid images and image paths in artifacts, so a link is the only legal carrier. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Proposing a file attachment pipeline into ClickUp: the templates forbid images and image paths in artifacts, so a link is the only legal carrier.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Proposing a file attachment pipeline into ClickUp: the templates forbid images and image paths in artifacts, so a link is the only legal carrier.

### Proposing a new packet for diagrams. The hub already routes Flow to a sibling packet, and the integration findings are fixes inside existing files. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Proposing a new packet for diagrams. The hub already routes Flow to a sibling packet, and the integration findings are fixes inside existing files.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Proposing a new packet for diagrams. The hub already routes Flow to a sibling packet, and the integration findings are fixes inside existing files.

### Ranking the source-coverage gaps above the delivery gaps. Coverage reporting is valuable, but the manifest (Rank 4) is what makes coverage trustworthy. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Ranking the source-coverage gaps above the delivery gaps. Coverage reporting is valuable, but the manifest (Rank 4) is what makes coverage trustworthy.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Ranking the source-coverage gaps above the delivery gaps. Coverage reporting is valuable, but the manifest (Rank 4) is what makes coverage trustworthy.

### Replacing the model-to-board read-back with a screenshot-only check: the packet's own rule states a picture cannot prove which nodes a connector joins. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Replacing the model-to-board read-back with a screenshot-only check: the packet's own rule states a picture cannot prove which nodes a connector joins.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Replacing the model-to-board read-back with a screenshot-only check: the packet's own rule states a picture cannot prove which nodes a connector joins.

### Treating `get_board_context`'s BM25 retrieval and vision clustering as a read-back model for the packet: those tools interpret a board the packet did not draw, while the packet's read-back has an expected model and exact counts. Their diff and evidence ideas transfer; the retrieval pipeline does not. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Treating `get_board_context`'s BM25 retrieval and vision clustering as a read-back model for the packet: those tools interpret a board the packet did not draw, while the packet's read-back has an expected model and exact counts. Their diff and evidence ideas transfer; the retrieval pipeline does not.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating `get_board_context`'s BM25 retrieval and vision clustering as a read-back model for the packet: those tools interpret a board the packet did not draw, while the packet's read-back has an expected model and exact counts. Their diff and evidence ideas transfer; the retrieval pipeline does not.

### Treating `skills-figquery/` as an independent second source: it is a byte-identical copy of `skills/` for the diagram skill, so citing both would double-count one source. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Treating `skills-figquery/` as an independent second source: it is a byte-identical copy of `skills/` for the diagram skill, so citing both would double-count one source.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating `skills-figquery/` as an independent second source: it is a byte-identical copy of `skills/` for the diagram skill, so citing both would double-count one source.

### Treating `tmcw__figjam-mermaid` as a full read-back: it reads stickies and connectors only, so it cannot verify shapes, sections, tables or labels. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Treating `tmcw__figjam-mermaid` as a full read-back: it reads stickies and connectors only, so it cannot verify shapes, sections, tables or labels.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating `tmcw__figjam-mermaid` as a full read-back: it reads stickies and connectors only, so it cannot verify shapes, sections, tables or labels.

### Treating the architecture component library as a rule source: it is a manual asset library, and its variants cannot be generated. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Treating the architecture component library as a rule source: it is a manual asset library, and its variants cannot be generated.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the architecture component library as a rule source: it is a manual asset library, and its variants cannot be generated.

### Treating the Flow lane in `router-contract.md` as loadable: the guard drops it by design and the lane exists only for Project knowledge naming. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Treating the Flow lane in `router-contract.md` as loadable: the guard drops it by design and the lane exists only for Project knowledge naming.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the Flow lane in `router-contract.md` as loadable: the guard drops it by design and the lane exists only for Project knowledge naming.

### Treating the packet's seven types as the corpus comparison unit alone: type names differ across projects (flowchart/workflow/architecture/state), so later iterations compare by capability and rule, not by label. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Treating the packet's seven types as the corpus comparison unit alone: type names differ across projects (flowchart/workflow/architecture/state), so later iterations compare by capability and rule, not by label.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the packet's seven types as the corpus comparison unit alone: type names differ across projects (flowchart/workflow/architecture/state), so later iterations compare by capability and rule, not by label.

<!-- /ANCHOR:exhausted-approaches -->

---

<!-- ANCHOR:ruled-out-directions -->
## 10. RULED OUT DIRECTIONS
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
- Q2: layout, colour, density and board-quality measurement. (iteration 2)
- Q3: read-back, revision, fileKey reuse, failure/retry, delivery. (iteration 2)
- Q1: type/kind and model-rule coverage. (iteration 2)
- Q4: request routing and artifact handoff. (iteration 2)
- Q5: claude.ai kernel without a Figma connector, and ClickUp. (iteration 2)
- Q3: read-back, revision, fileKey reuse, failure/retry, delivery (delivery now has corpus evidence; revision and retry still need the routing and execution surfaces). (iteration 6)
- Q3: read-back, revision, fileKey reuse, failure and retry (partly covered; the revision and retry surfaces still need a direct read). (iteration 7)
- Q5: the claude.ai kernel without a Figma connector, and ClickUp. (iteration 7)
- Q5: the claude.ai kernel without a Figma connector, and whether a board URL should reach ClickUp through the vendored transport. (iteration 8)
- None open. Q1 to Q5 are answered; iteration 10 turns the findings into ranked recommendations. (iteration 9)
- None. The ranking is the deliverable. (iteration 10)

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

- Packet under review: `AI Systems/Product Owner/sk-create-figjam/` (SKILL.md, references/flow-mode.md, references/types/{user-flow,process,architecture,sequence,state,er,gantt}.md, references/style-guide.md, references/quality-rubric.md, references/hybrid-workflow.md, assets/flow-templates.md, assets/templates/*.md, assets/examples/*.md, scripts/flow_check.py, scripts/figjam_checks/*.py, manual-testing-playbook/).
- Integration surfaces: `AI Systems/Product Owner/SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `AGENTS.md`, `sk-product-owner/SKILL.md` plus `references/router-contract.md`, `references/interactive-mode.md`, `references/task-mode.md`, `claude project/Custom Instructions.md` and `claude project/knowledge/`, `mcp-figma/SKILL.md`, `benchmark/hub-routing-cases.json`, `benchmark/gates/check_hub.py`, `benchmark/router/route_contract.py`.
- Corpus: 22 pinned public repos under `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/` (Figma MCP server guide at a newer commit than phase 009, community resources, architecture-diagram components, OpenAI plugins, lightspeedwp `.github`, Adobe spectrum design data, hferello/ai, prasantloki/figjam-builder, rrichardsonv/parse-figjam, ecestnrkl/figjam-mcp, bluescaban/blueprints, arinspunk/claude-talk-to-figma-mcp, ulasbilgen/mcp-skills-plugins, tmcw/figjam-mermaid, lauragalera/figjam-erd-plugin, plus seven phase 009 repos).
- Constraints: read-only outside the lineage; no screenshots, board URLs, containment folders, or Product Context.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 10
- Convergence threshold: 0.05 (telemetry only; `convergenceMode: off`)
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true
- research/research.md ownership: workflow-owned canonical synthesis output
- Lifecycle branches: `resume`, `restart` live; `fork`, `completed-continue` deferred
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A
- Canonical pause sentinel: `research/.deep-research-pause`
- Current generation: 1
- Started: 2026-10-20

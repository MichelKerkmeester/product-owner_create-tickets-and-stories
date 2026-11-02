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
- Topic: What should Product Owner's Flow Mode adopt from the strongest public FigJam diagram skills? Flow Mode turns screenshots, Figma flows and product docs into a checked Mermaid model and writes it to FigJam through the hosted Figma MCP generate_diagram tool, with figma-ds-cli fj as the Desktop fallback. Its sources: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md, AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md, AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py, AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md, AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Templates.md and the Flow Mode Delivery section of AI Systems/Product Owner/claude project/Custom Instructions.md. The corpus is eight public repos pinned under specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/: figma__mcp-server-guide (Figma's official figma-generate-diagram and figma-use-figjam skills and their references), IamTheLime__dotfiles (figjam-diagrams), southleft__figma-console-mcp-skills (figjam-create-content), mkaralevich__pi-figma-labor (figjam-create), amo-tech-ai__rocket-path-ai (figjam-diagrams), atezer__FMCP (figjam-diagram-builder), ompug__diagram-codebase and memi-design__mermaid-jam. Compare rules, checks, write routes, read-back and verification, failure and retry handling, file and page handling, layout, colour, shapes, density, label rules, iteration and fileKey reuse, hybrid generate_diagram plus use_figma extension, and delivery. Give an adopt or reject verdict, with reasons, on four known gaps: FigJam files have one implicit page and figma.createPage throws, so Flow Mode's new-page rule and page rollback; emojis in Mermaid; reserved node IDs end, subgraph and graph; underscores in node IDs. Also judge Flow Mode's deliberate limits against the corpus: top-to-bottom only, 9 nodes, 3 exits per decision, one accent colour, four shapes.
- Started: 2026-10-20T07:43:20Z
- Status: COMPLETE
- Iteration: 20 of 20
- Session ID: fanout-deepseek-1792482040367-nu2bmb
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
| 1 | Figma's official hosted-route contract (figma-generate-diagram + figma-use-figjam) | - | 0.90 | 10 | complete |
| 2 | IamTheLime__dotfiles figjam-diagrams: projector-readable board rules and FigJam API notes | - | 0.96 | 12 | complete |
| 3 | southleft figjam-create-content: console route, atomicity, and read-back queries | - | 0.89 | 10 | complete |
| 4 | mkaralevich pi-figma-labor: staged write, per-mutation undo, structural verification | - | 0.90 | 10 | complete |
| 5 | rocket-path figjam-diagrams: same-route rival playbook and examples | - | 0.85 | 11 | complete |
| 6 | atezer FMCP figjam-diagram-builder: response safety, deterministic coordinates, phased writes | - | 0.90 | 11 | complete |
| 7 | ompug diagram-codebase: Mermaid linter, sanitizer, deterministic ID builder | - | 0.91 | 12 | complete |
| 8 | memi-design mermaid-jam: parser diagnostics, ID normalization, revise pass | - | 0.91 | 11 | complete |
| 9 | Deepen iterations 2 and 7: ompug publish protocol, sections, idempotency, rollback, verification | - | 0.88 | 10 | complete |
| 10 | Five-limit verdicts plus widened corpus source parse-figjam | - | 0.77 | 13 | complete |
| 11 | Candidate improvement table tested against the actual Flow Mode files | - | 0.58 | 13 | complete |
| 12 | Stress-test the accent and subgraph rows and fit new rules into the checker self-test | - | 0.52 | 12 | complete |
| 13 | Extractor fields, unchecked edge operators and dead markup checks | - | 0.70 | 12 | complete |
| 14 | Replacement text for the checker and rule list plus planted models | - | 0.60 | 13 | complete |
| 15 | Write-route replacement text across skill, mirror and kernel | - | 0.55 | 13 | complete |
| 16 | Read-back format, direction counting and the eighth page statement | - | 0.62 | 13 | complete |
| 17 | Batching the changes against the real gate state | - | 0.66 | 13 | complete |
| 19 | Attacking the top rows and correcting four decisions | - | 0.68 | 12 | complete |
| 18 | The ranked table | - | 0.35 | 12 | complete |
| 20 | Consolidation of final decisions and ranking | - | 0.25 | 12 | complete |

- iterationsCompleted: 20
- keyFindings: 235
- openQuestions: 0
- resolvedQuestions: 5

<!-- /ANCHOR:progress -->
<!-- ANCHOR:questions -->
## 4. QUESTIONS
- Answered: 5/5
- [x] Which pre-write model check, rule set or validator does each corpus skill define before a FigJam write, and which of those rules are machine-enforced rather than advisory?
- [x] Which write route does each corpus skill use (hosted MCP `generate_diagram`, `use_figma` plugin API, console bridge, direct `fj`-style node script), and what read-back or verification follows the write?
- [x] How do the corpus skills handle FigJam's single implicit page, file creation, `fileKey` reuse and rollback, and what does that imply for Flow Mode's new-page rule?
- [x] How do the corpus skills handle Mermaid label and identifier hazards: emojis, reserved node IDs `end`/`subgraph`/`graph`, underscores in node IDs, and line breaks or markup?
- [x] Which layout, colour, shape, density and label limits does the corpus treat as enforceable versus advisory, and do they support or contradict Flow Mode's limits (TD only, 9 nodes, 3 decision exits, one accent colour, four shapes)?

<!-- /ANCHOR:questions -->
<!-- ANCHOR:uncovered-questions -->
## Uncovered Questions
- Count: 0
- None

<!-- /ANCHOR:uncovered-questions -->
<!-- ANCHOR:trend -->
## 5. TREND
- newInfoRatio sparkline: ▇█▇▇▇▇██▇▆▄▄▅▄▄▅▅▅▂▁
- score sparkline: ▇█▇▇▇▇██▇▆▄▄▅▄▄▅▅▅▂▁
- Last 3 ratios: 0.68 -> 0.35 -> 0.25
- Stuck count: 0
- Guard violations: none recorded by the reducer pass
- convergenceScore: 0.25
- coverageBySources: {"code":1,"github.com":1,"other":69}
- Advisory events: none

<!-- /ANCHOR:trend -->
<!-- ANCHOR:dead-ends -->
## 6. DEAD ENDS
- Reading the duplicate `skills-figquery/` tree as a separate source: it is a mirrored copy, not independent evidence. (iteration 1)
- Treating `figma-generate-diagram`'s workflow reference as primary for this iteration: it covers hybrid annotations/colour-coding, which belongs to the write-route iteration, not the rule baseline. (iteration 1)
- Adopting IamTheLime's shape list `SQUARE`/`DIAMOND`/dashed as Flow Mode's vocabulary: it removes stadium start/end and the merge-dot circle, both load-bearing in Flow Mode's patterns, without replacing their semantics. (iteration 2)
- Adopting the 120–160px band spacing into the hosted route: the generator owns layout, so the number has no lever there. (iteration 2)
- Searching for a `read-back` or verification helper inside this skill: verification is prose and screenshots, with no script. Recorded so later iterations do not re-scan for one. (iteration 2)
- Adopting the console bridge as a third Flow Mode route: it requires the same Desktop Plugin API as `fj` but adds a second tool surface, so it is redundant for Flow Mode's constraints. (iteration 3)
- Searching this repo for a Mermaid parser or pre-write validator: none exists; the skill validates by running the operation and reading back. (iteration 3)
- Treating the snippet file's broader shape list (`ROUNDED_RECTANGLE`, triangles, parallelograms) as a rule: it is an API capability list with no check attached. (iteration 3)
- Adopting Labor's `labor_*` tool surface into Flow Mode: Flow Mode's Desktop fallback is `figma-ds-cli fj`, and adding a third vendor CLI would double the connection and daemon surface without adding a capability. (iteration 4)
- Looking for a Mermaid parser or pre-write model check in this repo: the skill is node-level and has none. (iteration 4)
- Treating `labor_undo` as directly callable from Flow Mode: the principle transfers, the verb does not. (iteration 4)
- Adopting its LR default wholesale: Flow Mode's TD-only is a product decision about reading user flows on a board; the corpus shows LR is common, not that TD is wrong. (iteration 5)
- Adopting this repo's shape vocabulary: it conflicts with the official renderer behaviour and with Flow Mode's four-shape discipline. (iteration 5)
- Searching for a pre-write validator or a read-back in this repo: none exists. (iteration 5)
- Adopting the F-MCP bridge as a Flow Mode route: it requires a third-party plugin plus Desktop, and Flow Mode already has a Desktop fallback. (iteration 6)
- Adopting the swimlane pattern into Flow Mode's current model: it needs a lane primitive and a second layout axis, neither of which the Mermaid-to-FigJam route exposes. (iteration 6)
- No pre-write model check exists here; the skill is purely execution safety. Recorded so Q1 is not re-probed in this repo. (iteration 6)
- Adopting the 25-node density cap: it is 2.8× Flow Mode's 9 and belongs to codebase architecture diagrams, not product user flows. (iteration 7)
- Adopting the full lint rule set verbatim into `flow_check.py`: most rules are already there, and the additions must be split into errors (emoji, reserved IDs, underscores) versus warnings (camelCase, backticks) rather than imported wholesale. (iteration 7)
- Looking for a FigJam writer in this repo: the driver exists (`figma/driver.py`) but is outside the FigJam diagram-skill surface this run is comparing; the linter and builder are the transferable part. (iteration 7)
- Adopting ID rewriting into Flow Mode: the provenance table depends on stable authored IDs, so rewriting them would break node-to-source mapping [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33]. (iteration 8)
- Adopting Mermaid Jam's plugin as a Flow Mode route: it is a consumer-facing plugin with its own UI and no MCP surface, so Flow Mode cannot call it. (iteration 8)
- No emoji-specific handling was found in this repo; its label cleaning removes markdown syntax but not emoji. Recorded so Q4's emoji verdict rests on the three sources that address it directly. (iteration 8)
- Adopting the `pending_action` ledger as a Flow Mode mechanism: Flow Mode has no persistent run state of its own; the principle (record intent before the call, reconcile before retry) can still be stated as guidance. (iteration 9)
- Adopting the 60% label-ratio threshold into Flow Mode: at nine nodes, partial label coverage is a defect, not a pass. (iteration 9)
- Searching the driver for a page-based rollback: none exists; every cleanup path is section-scoped. Confirms iteration 2's conclusion rather than adding a new option. (iteration 9)
- Adopting a REST read-back as Flow Mode's primary verification: the hosted MCP route already returns a board link, and a REST token is a new dependency; it is a recommended complement, not a replacement. (iteration 10)
- Broader `gh search` queries ("figjam skill", "figma diagram skill") returned no additional skill repos; only `parse-figjam` had substance. Recorded so later iterations do not repeat the searches. (iteration 10)
- Pinning `parse-figjam` into the local corpus: it was read through the GitHub API, and adding files would write outside this lineage. (iteration 10)
- Adding a REST read-back implementation to Flow Mode: it needs a Figma token and a REST dependency, so it stays a recommendation rather than a change. (iteration 11)
- Adding the `fj` route to the Claude Project mirror: the mirror correctly states that the Desktop route is unavailable in a Project [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:99]. (iteration 11)
- Changing the 9-node or 3-exit caps: iteration 10 found both defensible. (iteration 11)
- Looking for a fourth Flow Mode surface: the skill, its asset, the two mirrors and the kernel are the full set; no further file repeats the page rule. (iteration 11)
- **A 120-character cap**: too loose for a board at this size; 80 chosen. (iteration 12)
- **Accent family** as a change: withdrawn for lack of a palette; replaced by a documentation line explaining why one hex is deliberate. (iteration 12)
- **Parsing subgraph nesting**: unnecessary once subgraphs are rejected. (iteration 12)
- **Subgraph support**: rejected explicitly, with the three-reason rationale above. (iteration 12)
- Trying to derive colour families from hue distance: every threshold was arbitrary, and the self-test could not distinguish a disciplined palette from a sloppy one. Recorded so a later iteration does not retry it. (iteration 12)
- Adding a parser change for edge rules: `Edge` already carries the needed fields. (iteration 13)
- Checking markup on `node.label`: two marks are dead there; raw text is the only honest surface. (iteration 13)
- Probing `parse_block` with a `subgraph` model returned no diagram, so subgraph structure is not modelled; this confirms the raw-text scan rather than a node-level check. Recorded so a later iteration does not look for subgraph nodes. (iteration 13)
- Treating a reserved word in a label as a defect: the generator only reserves IDs. (iteration 13)
- A bare `<`/`>` raw scan: collides with arrow operators. (iteration 14)
- A camelCase warning: needs a warning channel and a non-binary exit code. (iteration 14)
- A separate emoji helper module: one regex used twice is smaller. (iteration 14)
- Counting subgraph nesting: rejected outright, so counting is wasted work. (iteration 14)
- Trying to keep the "first six rules" sentence by appending new rules after the read-back bullet: that would put a model rule in the read-back half and misstate the gate. Reordering is the only coherent option. (iteration 14)
- **A new knowledge file for write safety**: the existing mirror already owns the section. (iteration 15)
- **Claiming the kernel review in the change**: only a named human can confirm it. (iteration 15)
- **Editing the kernel only**: leaves the skill and mirror stating the impossible page rule. (iteration 15)
- **Rewording the `fj` rollback**: route-specific and still valid. (iteration 15)
- Looking for a page-creation workaround: the vendor restriction is absolute for plugins, and every corpus source that writes through a plugin uses sections or existing pages instead. Recorded so no later iteration hunts for one. (iteration 15)
- **A fourth reply line for details**: violates the kernel's "and nothing else". (iteration 16)
- **Cap-only direction counting**: proves an arrowhead exists, not where it points. (iteration 16)
- **Changing the kernel line**: it does not prescribe the format. (iteration 16)
- **Screenshot-only read-back as the default**: cannot establish endpoints or containment. (iteration 16)
- Searching for a fifth page statement in `flow-templates.md`: the asset has none, so the surface set is the skill, the mirror and the kernel, with eight statements total. (iteration 16)
- **Applying the format gate to Flow Mode**: there is no artifact file. (iteration 17)
- **Committing the batch**: not requested and not authorised here. (iteration 17)
- **Recording a kernel review line**: the kernel is uncommitted and the reviewer is a human. (iteration 17)
- **Running the parity gate as proof now**: it refuses on the declaration state. (iteration 17)
- Looking for a git-tracked copy of `flow-mode.md` under another name: `git log` on the path is empty and `git status` shows it untracked, so no earlier revision exists to diff against. Recorded so a later iteration does not search. (iteration 17)
- **Combining the three ID rules into one row**: the synthesis needs distinct target changes, and each has its own planted model. (iteration 18)
- **Including withdrawn rows to reach a count**: the table has twelve real changes without them. (iteration 18)
- **Ranking by corpus frequency**: the page rule appears in more sources than the edge rule but fires less often. (iteration 18)
- **Dropping containment to preserve never-move**: loses the rollback boundary. (iteration 19)
- **Exact-match reserved IDs**: contradicted by the corpus linter. (iteration 19)
- **Keeping `fileKey` at rank 10**: contradicted by the draft-file count. (iteration 19)
- **Narrow emoji range**: contradicted by the corpus sanitizer. (iteration 19)
- Looking for a generator flag that targets a section directly: the official skill exposes `fileKey` and a separate `use_figma` step, not a section parameter. Recorded so the plan does not assume one. (iteration 19)
- Any change to the 9-node, 3-exit or four-shape rules: each survived the stress test. (iteration 20)
- Any claim that the parity gate passes today: it cannot run. (iteration 20)
- Any further corpus widening: twenty iterations reached saturation; the last three new sources changed details, not the ranking. (iteration 20)
- Searching for a generator parameter that targets a section directly: none exists; placement is a separate step. (iteration 20)
- Searching for a page-creation workaround in the plugin API: none exists; the restriction is absolute. (iteration 20)

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

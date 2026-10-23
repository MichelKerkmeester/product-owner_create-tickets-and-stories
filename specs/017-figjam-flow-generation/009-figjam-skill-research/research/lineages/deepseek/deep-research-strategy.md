# Deep Research Strategy - Flow Mode / FigJam corpus comparison

## 2. TOPIC

What should Product Owner's Flow Mode adopt from the strongest public FigJam diagram skills? Flow Mode turns screenshots, Figma flows and product docs into a checked Mermaid model and writes it to FigJam through the hosted Figma MCP `generate_diagram` tool, with `figma-ds-cli fj` as the Desktop fallback.

Corpus (pinned under `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/`): `figma__mcp-server-guide`, `IamTheLime__dotfiles`, `southleft__figma-console-mcp-skills`, `mkaralevich__pi-figma-labor`, `amo-tech-ai__rocket-path-ai`, `atezer__FMCP`, `ompug__diagram-codebase`, `memi-design__mermaid-jam`.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] Which pre-write model check, rule set or validator does each corpus skill define before a FigJam write, and which of those rules are machine-enforced rather than advisory?
- [x] Which write route does each corpus skill use (hosted MCP `generate_diagram`, `use_figma` plugin API, console bridge, direct `fj`-style node script), and what read-back or verification follows the write?
- [x] How do the corpus skills handle FigJam's single implicit page, file creation, `fileKey` reuse and rollback, and what does that imply for Flow Mode's new-page rule?
- [x] How do the corpus skills handle Mermaid label and identifier hazards: emojis, reserved node IDs `end`/`subgraph`/`graph`, underscores in node IDs, and line breaks or markup?
- [x] Which layout, colour, shape, density and label limits does the corpus treat as enforceable versus advisory, and do they support or contradict Flow Mode's limits (TD only, 9 nodes, 3 decision exits, one accent colour, four shapes)?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS

- Never open `AI Systems/Product Context`, any screenshot, any board URL or anything under a containment folder.
- Never quote Barter product flows.
- No implementation or edits to Flow Mode sources; this run reports findings only.
- No ranking of vendors or repos by popularity; only by transferable technique.

---

## 5. STOP CONDITIONS

- Stop at `maxIterations` (20) with stop reason `maxIterationsReached`.
- Convergence is telemetry only (`convergenceMode: off`, `stopPolicy: max-iterations`).
- Every iteration must widen the corpus (new repo/file/question) or deepen a named earlier iteration.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- Which pre-write model check, rule set or validator does each corpus skill define before a FigJam write, and which of those rules are machine-enforced rather than advisory?
- Which write route does each corpus skill use (hosted MCP `generate_diagram`, `use_figma` plugin API, console bridge, direct `fj`-style node script), and what read-back or verification follows the write?
- How do the corpus skills handle FigJam's single implicit page, file creation, `fileKey` reuse and rollback, and what does that imply for Flow Mode's new-page rule?
- How do the corpus skills handle Mermaid label and identifier hazards: emojis, reserved node IDs `end`/`subgraph`/`graph`, underscores in node IDs, and line breaks or markup?
- Which layout, colour, shape, density and label limits does the corpus treat as enforceable versus advisory, and do they support or contradict Flow Mode's limits (TD only, 9 nodes, 3 decision exits, one accent colour, four shapes)?

<!-- /ANCHOR:answered-questions -->

---

<!-- MACHINE-OWNED: START -->
<!-- ANCHOR:what-worked -->
## 7. WHAT WORKED
- reading the vendor skill first fixed the ground truth before community repos could muddy it. The vendor file names the four known gaps in plain text, so the gap analysis does not depend on inference. (iteration 1)
- reading the API notes alongside the design skill produced the mechanically useful half — the palette stays a design opinion, the API notes become an implementable checklist. (iteration 2)
- reading the snippet bodies rather than the prose produced the useful material — the two read queries and the atomicity note are not visible in the 42-line SKILL. (iteration 3)
- reading for lifecycle rather than rules produced the canary-write and scratch-node findings, which no earlier source had. (iteration 4)
- reading a same-route competitor produced the cleanest evidence so far, because route variables cancel out. (iteration 5)
- reading a scale-oriented skill produced operational constraints (timeouts, constants, return sizes) that design-oriented skills never state. (iteration 6)
- reading source code rather than skill prose produced the only implemented rule list in the corpus, including the severity choices that prose never states. (iteration 7)
- reading a real parser produced implemented policy on every hazard the topic names, including the ID-rewrite strategy no skill prose mentioned. (iteration 8)
- reading a publish protocol rather than a skill description produced the only crash-safety and idempotency model in the corpus. (iteration 9)
- combining synthesis with a genuinely new source kept the iteration from being a restatement; the read-back-only repo produced the direction and legend checks the write-oriented corpus lacked. (iteration 10)
- diffing the mirrors against the skill separated real drift from designed adaptation, which prevents a wrong "fix the mirror to match" recommendation. (iteration 11)
- reading the checker before recommending checker changes exposed that one recommendation was unimplementable; evidence from the target file beats evidence from the corpus. (iteration 12)
- probing the parser instead of reading only its dataclasses produced the edge-operator gap, which is the most consequential finding since iteration 7. (iteration 13)
- writing the actual conditions exposed two mistakes in the earlier recommendations — case-insensitive reserved matching and a bare-angle-bracket scan — before either reached a plan. (iteration 14)
- counting every statement of the page rule before drafting text prevented a one-file fix that would have left the kernel lying. (iteration 15)
- grepping every synonym for page found the recovery statement that iteration 15 missed; the count was only as good as the search terms. (iteration 16)
- running the gate instead of assuming it would pass produced the state facts that make the plan honest; a gate that cannot run is different from a gate that passes. (iteration 17)
- writing the impact scale before scoring kept the page rule from winning on drama alone; the edge rule fires more often and costs less to fix. (iteration 18)
- attacking the section rule found a direct contradiction with an existing Flow Mode rule, which no amount of corpus reading would have surfaced without the cross-check. (iteration 19)
- keeping a running table and attacking its top rows produced a final order that survived four reversals; the reversals are the evidence of rigour, not a weakness. (iteration 20)

<!-- /ANCHOR:what-worked -->

---

<!-- ANCHOR:what-failed -->
## 8. WHAT FAILED
- nothing failed; the mirrored `skills-figquery/` tree is a duplicate risk to avoid in later iterations. (iteration 1)
- no script exists in this repo, so it cannot answer Q1's "machine-enforced" half. (iteration 2)
- none failed; the skill has no model-level rules, so it cannot advance Q1. (iteration 3)
- nothing failed. (iteration 4)
- nothing failed; the examples file is long and only the densest examples were worth citing. (iteration 5)
- the Turkish source slows literal citation, so only structural claims were used. (iteration 6)
- the driver layer is large and not needed for this comparison; stopping at the linter/builder kept the iteration focused. (iteration 7)
- no emoji handling exists here, so the emoji verdict had to rest on the other three sources. (iteration 8)
- nothing failed; the driver is long but the publish order header made the target sections obvious. (iteration 9)
- three of four `gh search` queries returned nothing usable, so widening cost more calls than expected. (iteration 10)
- nothing failed, but the row count is larger than one iteration can rank well; ordering belongs in synthesis. (iteration 11)
- iteration 10's accent verdict was too quick — it treated a corpus pattern as a rule without asking what the check would compare. (iteration 12)
- the earlier iterations trusted `MARKUP_MARKS` at face value; only a probe showed three marks cannot fire. (iteration 13)
- the first draft appended new bullets at the end, which broke the check/read-back split; reordering fixed it. (iteration 14)
- the first draft changed the `fj` rollback too, until the route distinction showed it was still valid. (iteration 15)
- iteration 15 searched "new page" and "cleared the page" but not "cleared page", which is why the recovery pair slipped. (iteration 16)
- the first batch order put the kernel second, until the dependency on the mirror showed it had to be last. (iteration 17)
- the first ordering put read-back v2 at rank 3, until the missing/extra lists were recognised as an output change that needs the format work in rank 6. (iteration 18)
- the first emoji regex was invented rather than copied from the corpus sanitizer, and it was both too narrow and too wide in different ranges. (iteration 19)
- the early iterations trusted corpus patterns as rules before checking the target file; two recommendations had to be withdrawn as a result. (iteration 20)

<!-- /ANCHOR:what-failed -->

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### **A 120-character cap**: too loose for a board at this size; 80 chosen. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: **A 120-character cap**: too loose for a board at this size; 80 chosen.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A 120-character cap**: too loose for a board at this size; 80 chosen.

### **A fourth reply line for details**: violates the kernel's "and nothing else". -- BLOCKED (iteration 16, 1 attempts)
- What was tried: **A fourth reply line for details**: violates the kernel's "and nothing else".
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A fourth reply line for details**: violates the kernel's "and nothing else".

### **A new knowledge file for write safety**: the existing mirror already owns the section. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: **A new knowledge file for write safety**: the existing mirror already owns the section.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A new knowledge file for write safety**: the existing mirror already owns the section.

### **Accent family** as a change: withdrawn for lack of a palette; replaced by a documentation line explaining why one hex is deliberate. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: **Accent family** as a change: withdrawn for lack of a palette; replaced by a documentation line explaining why one hex is deliberate.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Accent family** as a change: withdrawn for lack of a palette; replaced by a documentation line explaining why one hex is deliberate.

### **Applying the format gate to Flow Mode**: there is no artifact file. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: **Applying the format gate to Flow Mode**: there is no artifact file.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Applying the format gate to Flow Mode**: there is no artifact file.

### **Cap-only direction counting**: proves an arrowhead exists, not where it points. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: **Cap-only direction counting**: proves an arrowhead exists, not where it points.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Cap-only direction counting**: proves an arrowhead exists, not where it points.

### **Changing the kernel line**: it does not prescribe the format. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: **Changing the kernel line**: it does not prescribe the format.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Changing the kernel line**: it does not prescribe the format.

### **Claiming the kernel review in the change**: only a named human can confirm it. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: **Claiming the kernel review in the change**: only a named human can confirm it.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Claiming the kernel review in the change**: only a named human can confirm it.

### **Combining the three ID rules into one row**: the synthesis needs distinct target changes, and each has its own planted model. -- BLOCKED (iteration 18, 1 attempts)
- What was tried: **Combining the three ID rules into one row**: the synthesis needs distinct target changes, and each has its own planted model.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Combining the three ID rules into one row**: the synthesis needs distinct target changes, and each has its own planted model.

### **Committing the batch**: not requested and not authorised here. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: **Committing the batch**: not requested and not authorised here.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Committing the batch**: not requested and not authorised here.

### **Dropping containment to preserve never-move**: loses the rollback boundary. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: **Dropping containment to preserve never-move**: loses the rollback boundary.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Dropping containment to preserve never-move**: loses the rollback boundary.

### **Editing the kernel only**: leaves the skill and mirror stating the impossible page rule. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: **Editing the kernel only**: leaves the skill and mirror stating the impossible page rule.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Editing the kernel only**: leaves the skill and mirror stating the impossible page rule.

### **Exact-match reserved IDs**: contradicted by the corpus linter. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: **Exact-match reserved IDs**: contradicted by the corpus linter.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Exact-match reserved IDs**: contradicted by the corpus linter.

### **Including withdrawn rows to reach a count**: the table has twelve real changes without them. -- BLOCKED (iteration 18, 1 attempts)
- What was tried: **Including withdrawn rows to reach a count**: the table has twelve real changes without them.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Including withdrawn rows to reach a count**: the table has twelve real changes without them.

### **Keeping `fileKey` at rank 10**: contradicted by the draft-file count. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: **Keeping `fileKey` at rank 10**: contradicted by the draft-file count.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Keeping `fileKey` at rank 10**: contradicted by the draft-file count.

### **Narrow emoji range**: contradicted by the corpus sanitizer. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: **Narrow emoji range**: contradicted by the corpus sanitizer.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Narrow emoji range**: contradicted by the corpus sanitizer.

### **Parsing subgraph nesting**: unnecessary once subgraphs are rejected. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: **Parsing subgraph nesting**: unnecessary once subgraphs are rejected.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Parsing subgraph nesting**: unnecessary once subgraphs are rejected.

### **Ranking by corpus frequency**: the page rule appears in more sources than the edge rule but fires less often. -- BLOCKED (iteration 18, 1 attempts)
- What was tried: **Ranking by corpus frequency**: the page rule appears in more sources than the edge rule but fires less often.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Ranking by corpus frequency**: the page rule appears in more sources than the edge rule but fires less often.

### **Recording a kernel review line**: the kernel is uncommitted and the reviewer is a human. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: **Recording a kernel review line**: the kernel is uncommitted and the reviewer is a human.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Recording a kernel review line**: the kernel is uncommitted and the reviewer is a human.

### **Rewording the `fj` rollback**: route-specific and still valid. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: **Rewording the `fj` rollback**: route-specific and still valid.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Rewording the `fj` rollback**: route-specific and still valid.

### **Running the parity gate as proof now**: it refuses on the declaration state. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: **Running the parity gate as proof now**: it refuses on the declaration state.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Running the parity gate as proof now**: it refuses on the declaration state.

### **Screenshot-only read-back as the default**: cannot establish endpoints or containment. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: **Screenshot-only read-back as the default**: cannot establish endpoints or containment.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Screenshot-only read-back as the default**: cannot establish endpoints or containment.

### **Subgraph support**: rejected explicitly, with the three-reason rationale above. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: **Subgraph support**: rejected explicitly, with the three-reason rationale above.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Subgraph support**: rejected explicitly, with the three-reason rationale above.

### A bare `<`/`>` raw scan: collides with arrow operators. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: A bare `<`/`>` raw scan: collides with arrow operators.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A bare `<`/`>` raw scan: collides with arrow operators.

### A camelCase warning: needs a warning channel and a non-binary exit code. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: A camelCase warning: needs a warning channel and a non-binary exit code.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A camelCase warning: needs a warning channel and a non-binary exit code.

### A separate emoji helper module: one regex used twice is smaller. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: A separate emoji helper module: one regex used twice is smaller.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A separate emoji helper module: one regex used twice is smaller.

### Adding a parser change for edge rules: `Edge` already carries the needed fields. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Adding a parser change for edge rules: `Edge` already carries the needed fields.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adding a parser change for edge rules: `Edge` already carries the needed fields.

### Adding a REST read-back implementation to Flow Mode: it needs a Figma token and a REST dependency, so it stays a recommendation rather than a change. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Adding a REST read-back implementation to Flow Mode: it needs a Figma token and a REST dependency, so it stays a recommendation rather than a change.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adding a REST read-back implementation to Flow Mode: it needs a Figma token and a REST dependency, so it stays a recommendation rather than a change.

### Adding the `fj` route to the Claude Project mirror: the mirror correctly states that the Desktop route is unavailable in a Project [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:99]. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Adding the `fj` route to the Claude Project mirror: the mirror correctly states that the Desktop route is unavailable in a Project [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:99].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adding the `fj` route to the Claude Project mirror: the mirror correctly states that the Desktop route is unavailable in a Project [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:99].

### Adopting a REST read-back as Flow Mode's primary verification: the hosted MCP route already returns a board link, and a REST token is a new dependency; it is a recommended complement, not a replacement. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Adopting a REST read-back as Flow Mode's primary verification: the hosted MCP route already returns a board link, and a REST token is a new dependency; it is a recommended complement, not a replacement.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting a REST read-back as Flow Mode's primary verification: the hosted MCP route already returns a board link, and a REST token is a new dependency; it is a recommended complement, not a replacement.

### Adopting IamTheLime's shape list `SQUARE`/`DIAMOND`/dashed as Flow Mode's vocabulary: it removes stadium start/end and the merge-dot circle, both load-bearing in Flow Mode's patterns, without replacing their semantics. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Adopting IamTheLime's shape list `SQUARE`/`DIAMOND`/dashed as Flow Mode's vocabulary: it removes stadium start/end and the merge-dot circle, both load-bearing in Flow Mode's patterns, without replacing their semantics.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting IamTheLime's shape list `SQUARE`/`DIAMOND`/dashed as Flow Mode's vocabulary: it removes stadium start/end and the merge-dot circle, both load-bearing in Flow Mode's patterns, without replacing their semantics.

### Adopting ID rewriting into Flow Mode: the provenance table depends on stable authored IDs, so rewriting them would break node-to-source mapping [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33]. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Adopting ID rewriting into Flow Mode: the provenance table depends on stable authored IDs, so rewriting them would break node-to-source mapping [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting ID rewriting into Flow Mode: the provenance table depends on stable authored IDs, so rewriting them would break node-to-source mapping [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33].

### Adopting its LR default wholesale: Flow Mode's TD-only is a product decision about reading user flows on a board; the corpus shows LR is common, not that TD is wrong. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Adopting its LR default wholesale: Flow Mode's TD-only is a product decision about reading user flows on a board; the corpus shows LR is common, not that TD is wrong.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting its LR default wholesale: Flow Mode's TD-only is a product decision about reading user flows on a board; the corpus shows LR is common, not that TD is wrong.

### Adopting Labor's `labor_*` tool surface into Flow Mode: Flow Mode's Desktop fallback is `figma-ds-cli fj`, and adding a third vendor CLI would double the connection and daemon surface without adding a capability. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Adopting Labor's `labor_*` tool surface into Flow Mode: Flow Mode's Desktop fallback is `figma-ds-cli fj`, and adding a third vendor CLI would double the connection and daemon surface without adding a capability.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting Labor's `labor_*` tool surface into Flow Mode: Flow Mode's Desktop fallback is `figma-ds-cli fj`, and adding a third vendor CLI would double the connection and daemon surface without adding a capability.

### Adopting Mermaid Jam's plugin as a Flow Mode route: it is a consumer-facing plugin with its own UI and no MCP surface, so Flow Mode cannot call it. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Adopting Mermaid Jam's plugin as a Flow Mode route: it is a consumer-facing plugin with its own UI and no MCP surface, so Flow Mode cannot call it.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting Mermaid Jam's plugin as a Flow Mode route: it is a consumer-facing plugin with its own UI and no MCP surface, so Flow Mode cannot call it.

### Adopting the `pending_action` ledger as a Flow Mode mechanism: Flow Mode has no persistent run state of its own; the principle (record intent before the call, reconcile before retry) can still be stated as guidance. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Adopting the `pending_action` ledger as a Flow Mode mechanism: Flow Mode has no persistent run state of its own; the principle (record intent before the call, reconcile before retry) can still be stated as guidance.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the `pending_action` ledger as a Flow Mode mechanism: Flow Mode has no persistent run state of its own; the principle (record intent before the call, reconcile before retry) can still be stated as guidance.

### Adopting the 120–160px band spacing into the hosted route: the generator owns layout, so the number has no lever there. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Adopting the 120–160px band spacing into the hosted route: the generator owns layout, so the number has no lever there.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the 120–160px band spacing into the hosted route: the generator owns layout, so the number has no lever there.

### Adopting the 25-node density cap: it is 2.8× Flow Mode's 9 and belongs to codebase architecture diagrams, not product user flows. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Adopting the 25-node density cap: it is 2.8× Flow Mode's 9 and belongs to codebase architecture diagrams, not product user flows.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the 25-node density cap: it is 2.8× Flow Mode's 9 and belongs to codebase architecture diagrams, not product user flows.

### Adopting the 60% label-ratio threshold into Flow Mode: at nine nodes, partial label coverage is a defect, not a pass. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Adopting the 60% label-ratio threshold into Flow Mode: at nine nodes, partial label coverage is a defect, not a pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the 60% label-ratio threshold into Flow Mode: at nine nodes, partial label coverage is a defect, not a pass.

### Adopting the console bridge as a third Flow Mode route: it requires the same Desktop Plugin API as `fj` but adds a second tool surface, so it is redundant for Flow Mode's constraints. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Adopting the console bridge as a third Flow Mode route: it requires the same Desktop Plugin API as `fj` but adds a second tool surface, so it is redundant for Flow Mode's constraints.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the console bridge as a third Flow Mode route: it requires the same Desktop Plugin API as `fj` but adds a second tool surface, so it is redundant for Flow Mode's constraints.

### Adopting the F-MCP bridge as a Flow Mode route: it requires a third-party plugin plus Desktop, and Flow Mode already has a Desktop fallback. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Adopting the F-MCP bridge as a Flow Mode route: it requires a third-party plugin plus Desktop, and Flow Mode already has a Desktop fallback.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the F-MCP bridge as a Flow Mode route: it requires a third-party plugin plus Desktop, and Flow Mode already has a Desktop fallback.

### Adopting the full lint rule set verbatim into `flow_check.py`: most rules are already there, and the additions must be split into errors (emoji, reserved IDs, underscores) versus warnings (camelCase, backticks) rather than imported wholesale. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Adopting the full lint rule set verbatim into `flow_check.py`: most rules are already there, and the additions must be split into errors (emoji, reserved IDs, underscores) versus warnings (camelCase, backticks) rather than imported wholesale.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the full lint rule set verbatim into `flow_check.py`: most rules are already there, and the additions must be split into errors (emoji, reserved IDs, underscores) versus warnings (camelCase, backticks) rather than imported wholesale.

### Adopting the swimlane pattern into Flow Mode's current model: it needs a lane primitive and a second layout axis, neither of which the Mermaid-to-FigJam route exposes. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Adopting the swimlane pattern into Flow Mode's current model: it needs a lane primitive and a second layout axis, neither of which the Mermaid-to-FigJam route exposes.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting the swimlane pattern into Flow Mode's current model: it needs a lane primitive and a second layout axis, neither of which the Mermaid-to-FigJam route exposes.

### Adopting this repo's shape vocabulary: it conflicts with the official renderer behaviour and with Flow Mode's four-shape discipline. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Adopting this repo's shape vocabulary: it conflicts with the official renderer behaviour and with Flow Mode's four-shape discipline.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adopting this repo's shape vocabulary: it conflicts with the official renderer behaviour and with Flow Mode's four-shape discipline.

### Any change to the 9-node, 3-exit or four-shape rules: each survived the stress test. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Any change to the 9-node, 3-exit or four-shape rules: each survived the stress test.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Any change to the 9-node, 3-exit or four-shape rules: each survived the stress test.

### Any claim that the parity gate passes today: it cannot run. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Any claim that the parity gate passes today: it cannot run.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Any claim that the parity gate passes today: it cannot run.

### Any further corpus widening: twenty iterations reached saturation; the last three new sources changed details, not the ranking. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Any further corpus widening: twenty iterations reached saturation; the last three new sources changed details, not the ranking.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Any further corpus widening: twenty iterations reached saturation; the last three new sources changed details, not the ranking.

### Broader `gh search` queries ("figjam skill", "figma diagram skill") returned no additional skill repos; only `parse-figjam` had substance. Recorded so later iterations do not repeat the searches. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Broader `gh search` queries ("figjam skill", "figma diagram skill") returned no additional skill repos; only `parse-figjam` had substance. Recorded so later iterations do not repeat the searches.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Broader `gh search` queries ("figjam skill", "figma diagram skill") returned no additional skill repos; only `parse-figjam` had substance. Recorded so later iterations do not repeat the searches.

### Changing the 9-node or 3-exit caps: iteration 10 found both defensible. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Changing the 9-node or 3-exit caps: iteration 10 found both defensible.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Changing the 9-node or 3-exit caps: iteration 10 found both defensible.

### Checking markup on `node.label`: two marks are dead there; raw text is the only honest surface. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Checking markup on `node.label`: two marks are dead there; raw text is the only honest surface.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Checking markup on `node.label`: two marks are dead there; raw text is the only honest surface.

### Counting subgraph nesting: rejected outright, so counting is wasted work. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: Counting subgraph nesting: rejected outright, so counting is wasted work.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Counting subgraph nesting: rejected outright, so counting is wasted work.

### Looking for a FigJam writer in this repo: the driver exists (`figma/driver.py`) but is outside the FigJam diagram-skill surface this run is comparing; the linter and builder are the transferable part. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Looking for a FigJam writer in this repo: the driver exists (`figma/driver.py`) but is outside the FigJam diagram-skill surface this run is comparing; the linter and builder are the transferable part.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a FigJam writer in this repo: the driver exists (`figma/driver.py`) but is outside the FigJam diagram-skill surface this run is comparing; the linter and builder are the transferable part.

### Looking for a fourth Flow Mode surface: the skill, its asset, the two mirrors and the kernel are the full set; no further file repeats the page rule. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Looking for a fourth Flow Mode surface: the skill, its asset, the two mirrors and the kernel are the full set; no further file repeats the page rule.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a fourth Flow Mode surface: the skill, its asset, the two mirrors and the kernel are the full set; no further file repeats the page rule.

### Looking for a generator flag that targets a section directly: the official skill exposes `fileKey` and a separate `use_figma` step, not a section parameter. Recorded so the plan does not assume one. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: Looking for a generator flag that targets a section directly: the official skill exposes `fileKey` and a separate `use_figma` step, not a section parameter. Recorded so the plan does not assume one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a generator flag that targets a section directly: the official skill exposes `fileKey` and a separate `use_figma` step, not a section parameter. Recorded so the plan does not assume one.

### Looking for a git-tracked copy of `flow-mode.md` under another name: `git log` on the path is empty and `git status` shows it untracked, so no earlier revision exists to diff against. Recorded so a later iteration does not search. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: Looking for a git-tracked copy of `flow-mode.md` under another name: `git log` on the path is empty and `git status` shows it untracked, so no earlier revision exists to diff against. Recorded so a later iteration does not search.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a git-tracked copy of `flow-mode.md` under another name: `git log` on the path is empty and `git status` shows it untracked, so no earlier revision exists to diff against. Recorded so a later iteration does not search.

### Looking for a Mermaid parser or pre-write model check in this repo: the skill is node-level and has none. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Looking for a Mermaid parser or pre-write model check in this repo: the skill is node-level and has none.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Mermaid parser or pre-write model check in this repo: the skill is node-level and has none.

### Looking for a page-creation workaround: the vendor restriction is absolute for plugins, and every corpus source that writes through a plugin uses sections or existing pages instead. Recorded so no later iteration hunts for one. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: Looking for a page-creation workaround: the vendor restriction is absolute for plugins, and every corpus source that writes through a plugin uses sections or existing pages instead. Recorded so no later iteration hunts for one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a page-creation workaround: the vendor restriction is absolute for plugins, and every corpus source that writes through a plugin uses sections or existing pages instead. Recorded so no later iteration hunts for one.

### No emoji-specific handling was found in this repo; its label cleaning removes markdown syntax but not emoji. Recorded so Q4's emoji verdict rests on the three sources that address it directly. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: No emoji-specific handling was found in this repo; its label cleaning removes markdown syntax but not emoji. Recorded so Q4's emoji verdict rests on the three sources that address it directly.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No emoji-specific handling was found in this repo; its label cleaning removes markdown syntax but not emoji. Recorded so Q4's emoji verdict rests on the three sources that address it directly.

### No pre-write model check exists here; the skill is purely execution safety. Recorded so Q1 is not re-probed in this repo. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: No pre-write model check exists here; the skill is purely execution safety. Recorded so Q1 is not re-probed in this repo.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: No pre-write model check exists here; the skill is purely execution safety. Recorded so Q1 is not re-probed in this repo.

### Pinning `parse-figjam` into the local corpus: it was read through the GitHub API, and adding files would write outside this lineage. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Pinning `parse-figjam` into the local corpus: it was read through the GitHub API, and adding files would write outside this lineage.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Pinning `parse-figjam` into the local corpus: it was read through the GitHub API, and adding files would write outside this lineage.

### Probing `parse_block` with a `subgraph` model returned no diagram, so subgraph structure is not modelled; this confirms the raw-text scan rather than a node-level check. Recorded so a later iteration does not look for subgraph nodes. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Probing `parse_block` with a `subgraph` model returned no diagram, so subgraph structure is not modelled; this confirms the raw-text scan rather than a node-level check. Recorded so a later iteration does not look for subgraph nodes.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Probing `parse_block` with a `subgraph` model returned no diagram, so subgraph structure is not modelled; this confirms the raw-text scan rather than a node-level check. Recorded so a later iteration does not look for subgraph nodes.

### Reading the duplicate `skills-figquery/` tree as a separate source: it is a mirrored copy, not independent evidence. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Reading the duplicate `skills-figquery/` tree as a separate source: it is a mirrored copy, not independent evidence.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Reading the duplicate `skills-figquery/` tree as a separate source: it is a mirrored copy, not independent evidence.

### Searching for a `read-back` or verification helper inside this skill: verification is prose and screenshots, with no script. Recorded so later iterations do not re-scan for one. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Searching for a `read-back` or verification helper inside this skill: verification is prose and screenshots, with no script. Recorded so later iterations do not re-scan for one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a `read-back` or verification helper inside this skill: verification is prose and screenshots, with no script. Recorded so later iterations do not re-scan for one.

### Searching for a fifth page statement in `flow-templates.md`: the asset has none, so the surface set is the skill, the mirror and the kernel, with eight statements total. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: Searching for a fifth page statement in `flow-templates.md`: the asset has none, so the surface set is the skill, the mirror and the kernel, with eight statements total.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a fifth page statement in `flow-templates.md`: the asset has none, so the surface set is the skill, the mirror and the kernel, with eight statements total.

### Searching for a generator parameter that targets a section directly: none exists; placement is a separate step. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Searching for a generator parameter that targets a section directly: none exists; placement is a separate step.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a generator parameter that targets a section directly: none exists; placement is a separate step.

### Searching for a page-creation workaround in the plugin API: none exists; the restriction is absolute. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Searching for a page-creation workaround in the plugin API: none exists; the restriction is absolute.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a page-creation workaround in the plugin API: none exists; the restriction is absolute.

### Searching for a pre-write validator or a read-back in this repo: none exists. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Searching for a pre-write validator or a read-back in this repo: none exists.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a pre-write validator or a read-back in this repo: none exists.

### Searching the driver for a page-based rollback: none exists; every cleanup path is section-scoped. Confirms iteration 2's conclusion rather than adding a new option. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Searching the driver for a page-based rollback: none exists; every cleanup path is section-scoped. Confirms iteration 2's conclusion rather than adding a new option.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching the driver for a page-based rollback: none exists; every cleanup path is section-scoped. Confirms iteration 2's conclusion rather than adding a new option.

### Searching this repo for a Mermaid parser or pre-write validator: none exists; the skill validates by running the operation and reading back. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Searching this repo for a Mermaid parser or pre-write validator: none exists; the skill validates by running the operation and reading back.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching this repo for a Mermaid parser or pre-write validator: none exists; the skill validates by running the operation and reading back.

### Treating `figma-generate-diagram`'s workflow reference as primary for this iteration: it covers hybrid annotations/colour-coding, which belongs to the write-route iteration, not the rule baseline. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Treating `figma-generate-diagram`'s workflow reference as primary for this iteration: it covers hybrid annotations/colour-coding, which belongs to the write-route iteration, not the rule baseline.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating `figma-generate-diagram`'s workflow reference as primary for this iteration: it covers hybrid annotations/colour-coding, which belongs to the write-route iteration, not the rule baseline.

### Treating `labor_undo` as directly callable from Flow Mode: the principle transfers, the verb does not. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Treating `labor_undo` as directly callable from Flow Mode: the principle transfers, the verb does not.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating `labor_undo` as directly callable from Flow Mode: the principle transfers, the verb does not.

### Treating a reserved word in a label as a defect: the generator only reserves IDs. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Treating a reserved word in a label as a defect: the generator only reserves IDs.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating a reserved word in a label as a defect: the generator only reserves IDs.

### Treating the snippet file's broader shape list (`ROUNDED_RECTANGLE`, triangles, parallelograms) as a rule: it is an API capability list with no check attached. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Treating the snippet file's broader shape list (`ROUNDED_RECTANGLE`, triangles, parallelograms) as a rule: it is an API capability list with no check attached.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the snippet file's broader shape list (`ROUNDED_RECTANGLE`, triangles, parallelograms) as a rule: it is an API capability list with no check attached.

### Trying to derive colour families from hue distance: every threshold was arbitrary, and the self-test could not distinguish a disciplined palette from a sloppy one. Recorded so a later iteration does not retry it. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: Trying to derive colour families from hue distance: every threshold was arbitrary, and the self-test could not distinguish a disciplined palette from a sloppy one. Recorded so a later iteration does not retry it.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Trying to derive colour families from hue distance: every threshold was arbitrary, and the self-test could not distinguish a disciplined palette from a sloppy one. Recorded so a later iteration does not retry it.

### Trying to keep the "first six rules" sentence by appending new rules after the read-back bullet: that would put a model rule in the read-back half and misstate the gate. Reordering is the only coherent option. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: Trying to keep the "first six rules" sentence by appending new rules after the read-back bullet: that would put a model rule in the read-back half and misstate the gate. Reordering is the only coherent option.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Trying to keep the "first six rules" sentence by appending new rules after the read-back bullet: that would put a model rule in the read-back half and misstate the gate. Reordering is the only coherent option.

<!-- /ANCHOR:exhausted-approaches -->

---

<!-- ANCHOR:ruled-out-directions -->
## 10. RULED OUT DIRECTIONS
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
- Q1 (per-skill checks), Q2 (write routes), Q4 (identifier hazards), Q5 (limits) remain open. (iteration 2)
- Q1, Q2, Q4, Q5 remain open. (iteration 3)
- Q1, Q2, Q4, Q5 remain open; two FigJam repos (FMCP, Ompug) and the Mermaid-side repos are unread. (iteration 5)
- Q1, Q2, Q4, Q5 remain formally open. (iteration 7)
- Q2 (full route/read-back matrix; ompug's driver unread) and Q5 (limits verdict) remain open. (iteration 8)
- Q5 (limits verdict) remains open; iterations 10–12 will test the five limits against the corpus and then broaden to new sources. (iteration 9)
- None of the five key questions remains open. Iterations 11–20 will deepen improvement candidates, test the synthesis ranking, and widen where new sources or files appear. (iteration 10)
- None. Iterations 12–20 will stress-test the ranking, deepen individual rows, and widen where new evidence appears. (iteration 11)
- None. Remaining iterations deepen the mechanical rows and prepare the synthesis ranking. (iteration 12)
- Whether a thick or dashed edge is ever useful in a Flow Mode diagram; the corpus treats dashed as a distinct relationship but Flow Mode has no need for one at nine nodes. (iteration 13)
- None for the checker. The remaining iterations test the ranking and the write-route rows. (iteration 14)
- Whether the section name should carry a run id, which affects idempotency on retries. Left for the write-safety iteration if evidence appears. (iteration 15)
- None for read-back. The remaining iterations rank the full set and test the write-route additions against the parity gate. (iteration 16)
- Whether the pending Product Owner batch should land before or with the Flow Mode batch; that is the operator's call, not the research's. (iteration 17)
- None. Iterations 19–20 test the table's weakest assumptions and prepare the synthesis. (iteration 18)
- None. Iteration 20 consolidates the decisions and prepares the synthesis. (iteration 19)
- None within the research scope. Implementation, commit and review are outside it. (iteration 20)

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->

## 12. KNOWN CONTEXT

Flow Mode baseline sources:

- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md` (163 lines): workflow, flowchart rules, hosted and `fj` write routes, read-back, delivery.
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md` (124 lines): five passing Mermaid patterns, provenance table, three-line reply.
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py` (180 lines): the pre-write check with seven planted failure models.
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md` and `.../Product Owner - Assets - Flow Templates.md`: Claude Project mirrors.
- `AI Systems/Product Owner/claude project/Custom Instructions.md`, Flow Mode Delivery section: the claude.ai kernel.

Corpus inventory: 656 files across eight repos; the FigJam-relevant surface is roughly a dozen skill files plus their references.

### Bounded Context Snapshot

- Source pointers: the eight corpus repos under `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/`.
- Reuse candidates: Figma's official FigJam skill references (`figjam-colors.md`, `position-figjam-nodes.md`, `plan-board-content.md`), community skill checklists, and any repo that encodes a Mermaid-to-FigJam translator.
- Integration points: `flow-mode.md` rules and write routes, `flow-templates.md` patterns, `flow_check.py` rule set.
- Constraints and risks: the corpus is public material of uneven depth; only claims with a file and line citation count.

---

## 13. RESEARCH BOUNDARIES

- Max iterations: 20
- Convergence threshold: 0.05 (telemetry only; convergence mode off)
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true
- research/research.md ownership: workflow-owned canonical synthesis output
- Lifecycle branches: `new` only for this lineage
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A
- Canonical pause sentinel: none used in this detached lineage
- Current generation: 1
- Started: 2026-10-20T07:43:20Z

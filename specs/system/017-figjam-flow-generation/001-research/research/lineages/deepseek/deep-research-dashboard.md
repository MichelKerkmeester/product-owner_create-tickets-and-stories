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
- Topic: How can Product Owner (AI Systems/Product Owner) turn screenshots, Figma flows and product docs into FigJam flows, with FigJam as the only output? Cover: FigJam capability and limits through the Figma MCP (.skilled/skills/mcp-tooling/mcp-figma); input handling per type; which sk-design-diagram flow chart rules (.skilled/skills/sk-design/sk-design-diagram) carry over to FigJam; embedding a duplicate of the mcp-figma skill in Product Owner; a Claude Code plugin following Media Editor (AI Systems/Media Editor/runtime/claude-plugin); a low-friction sync path from the embedded copy back to .skilled across two git repos; converting Product Owner to a parent hub following Moneybird Accountant (hub-router.json, mode-registry.json); lessons and mistakes from both precedents; risks. Each iteration opens a new question or deepens an earlier finding. Cite local file and line for every claim.
- Started: 2026-10-19T23:02:00Z
- Status: COMPLETE
- Iteration: 20 of 20
- Session ID: fanout-deepseek-1792443686484-iqx882
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
| 1 | FigJam write surface and its hard runtime limits | - | 1.00 | 6 | complete |
| 2 | Screenshots as a pre-structured flow model | - | 1.00 | 6 | complete |
| 3 | Figma frame flows as input, and the missing bridge into FigJam | - | 0.92 | 6 | complete |
| 4 | Product docs as input, and the output contract they collide with | - | 0.85 | 6 | complete |
| 5 | One intermediate flow model for three input types | - | 0.60 | 6 | insight |
| 6 | The flowchart rules sk-design-diagram actually enforces | - | 0.95 | 6 | complete |
| 7 | Which flowchart rules survive FigJam, and what replaces the rest | - | 0.70 | 6 | insight |
| 8 | How a Product Owner skill package is built | - | 1.00 | 6 | complete |
| 9 | The Media Editor plugin as a packaging precedent | - | 1.00 | 6 | complete |
| 10 | Mistakes the Media Editor plugin already paid for | - | 1.00 | 6 | complete |
| 11 | What a parent hub is, in files | - | 1.00 | 6 | complete |
| 12 | What the Moneybird hub conversion actually cost | - | 1.00 | 6 | complete |
| 13 | The sync reality that already exists between the two repositories | - | 1.00 | 6 | complete |
| 14 | Scoring the sync options against proven mechanics | - | 0.80 | 6 | insight |
| 15 | The Product Owner parent-hub change list | - | 0.85 | 6 | insight |
| 16 | The gates that will judge the embedded skill | - | 1.00 | 6 | complete |
| 17 | The risk register, ranked by what research can reduce | - | 0.90 | 7 | complete |
| 18 | What FigJam is the only output actually constrains | - | 0.85 | 6 | insight |
| 19 | What the claude.ai Project can do with a FigJam capability | - | 0.90 | 6 | complete |
| 20 | Closing the loop, separating what is known from what must be run | - | 0.45 | 6 | insight |

- iterationsCompleted: 20
- keyFindings: 121
- openQuestions: 1
- resolvedQuestions: 4

<!-- /ANCHOR:progress -->
<!-- ANCHOR:questions -->
## 4. QUESTIONS
- Answered: 4/5
- [x] How does each input type, screenshot or Figma frame flow or product doc, become a flow model before any FigJam write?
- [x] Which sk-design-diagram flow rules carry over to FigJam, and which need a FigJam-native replacement?
- [x] How should a Product Owner copy of mcp-figma be embedded, plugin-packaged and synced back to .skilled across two repositories?
- [x] What must Product Owner change to become a parent hub, and which Media Editor and Moneybird Accountant lessons and risks apply?
- [ ] What can the Figma MCP build, read and refuse inside FigJam, and what are its hard limits? [legacy-import]

<!-- /ANCHOR:questions -->
<!-- ANCHOR:uncovered-questions -->
## Uncovered Questions
- Count: 1
- [ ] What can the Figma MCP build, read and refuse inside FigJam, and what are its hard limits?

<!-- /ANCHOR:uncovered-questions -->
<!-- ANCHOR:trend -->
## 5. TREND
- newInfoRatio sparkline: ██▇▆▃▇▄██████▅▆█▇▆▇▁
- score sparkline: ██▇▆▃▇▄██████▅▆█▇▆▇▁
- Last 3 ratios: 0.85 -> 0.90 -> 0.45
- Stuck count: 0
- Guard violations: none recorded by the reducer pass
- convergenceScore: 0.45
- coverageBySources: {"code":67,"other":50}
- Advisory events: none

<!-- /ANCHOR:trend -->
<!-- ANCHOR:dead-ends -->
## 6. DEAD ENDS
- Assuming a headless server-side render step. There is no API-key path for authoring; closure of Desktop or a missing daemon stops the work. (iteration 1)
- Searching the mcp-figma skill for an official Figma Dev Mode MCP path. The reference explicitly places it out of scope for this skill, so it is not a fallback the Product Owner may rely on today. (iteration 1)
- Treating "Figma MCP" as the FigJam writer. The MCP is a read surface for design context, so a Product Owner flow that claims "the MCP builds the FigJam board" is describing a capability the wired server does not have. (iteration 1)
- Looking for a Product Owner documentation file that already describes the screenshot library. No PO doc in the skill or bootstrap mentions screenshots, so there is no existing contract to extend. (iteration 2)
- Reading every screenshot in the corpus. 341 images with a per-flow structure means the folder, not the library, is the unit of work. (iteration 2)
- Treating filenames as sufficient. Filenames give the step label and intent but not the on-screen control a step clicks, so OCR or detection is still needed for a grounded node. (iteration 2)
- Extracting whole files. The auto-split behavior makes a whole-file read a directory-producing operation, not a bounded input. (iteration 3)
- Searching the skill for an official Figma Dev Mode MCP bridge into FigJam. Iteration 1 already placed it out of scope; this iteration confirms nothing else bridges design files to FigJam boards. (iteration 3)
- Transporting design frames into FigJam as embedded objects. There is no documented verb for it, and inventing one from the Figma Plugin API would mean `fj eval`, which the skill classes as arbitrary mutation. (iteration 3)
- Looking for an existing diagram or canvas artifact type in the Product Owner skill. None exists in the lane list or in the export path pattern. (iteration 4)
- Reusing the doc lane to emit a FigJam board. The lane's contract is markdown plus read-back, and a canvas has no read-back equivalent. (iteration 4)
- Treating the existing "Figma feedback" trigger as diagram input. It consumes prose about Figma, not a Figma file. (iteration 4)
- A model that needs tables or embedded images. The six-verb surface cannot render either, so any such requirement would force `fj eval` and its arbitrary-mutation gate. (iteration 5)
- Looking for a layout verb in the FigJam group. There is none; positioning is manual through move or update. (iteration 5)
- Trusting creation output to return ids. That contract is undocumented; a read-back step is the only grounded option. (iteration 5)
- Keeping the arc-jump crossing rule. It is an SVG geometry trick with no FigJam equivalent in the six-verb surface. (iteration 6)
- Reusing the HTML/SVG renderer for FigJam. FigJam has no documented HTML or SVG import verb, and the skill explicitly excludes canvas deliverables. (iteration 6)
- Searching the ASCII validator for shape rules. It validates labels, arrows and nesting depth, not shape vocabulary, so shape semantics live only in the type reference. (iteration 6)
- Deferring layout to FigJam. No automatic layout verb exists, so a deferral would produce overlapping nodes. (iteration 7)
- Looking for a FigJam-native validator in either skill package. Neither the mcp-figma skill nor the diagram skill ships one. (iteration 7)
- Porting the HTML/SVG taste gate wholesale. Its palette, typography and spacing rules describe a rendered page, not a board whose colours and shapes are FigJam primitives. (iteration 7)
- Encoding the diagram capability as a route inside `sk-product-owner`. The manifest config declares one workflow mode, and the router contract maps commands to artifact lanes, not to a second capability. (iteration 8)
- Looking for a `mode-registry.json` in the Product Owner package. It is absent by design. (iteration 8)
- Treating the embedded skill as a folder copy. Three of its files are generated projections, so a plain copy drifts from its own schema on the first edit. (iteration 8)
- Copying the "no MCP server" choice for a FigJam plugin. Product Owner's writer is an external CLI binary rather than a bundled server, so the two cases do not share a transport. (iteration 9)
- Hand-maintaining the copy in the plugin directory. The build replaces it and fails on any divergence, so hand edits are rejected by design. (iteration 9)
- Looking for a tracked plugin payload in git. The three payload directories are untracked by design, which is why this precedent answers the drift question so cleanly. (iteration 9)
- Assuming the runtime supplies a Node runtime or expands bundle settings. The spike disproved both, and the manifest was rebuilt around that. (iteration 10)
- Looking for a plugin-specific parity tool in the PO repo. The parity lesson is transferable, but there is no shared checker to reuse. (iteration 10)
- Treating the development dependency as the shipped binary. The 45-failure run shows that shortcut fails silently. (iteration 10)
- Looking for a hub-level mode reference file. The hub has no mode docs of its own; all stage-two routing lives in packets. (iteration 11)
- Making a tool packet the default. The registry defaults to the workflow packet so a bare request cannot fall into a CLI execution. (iteration 11)
- Treating "parent hub" as a large single skill. The hub is a router plus independent packets, and the packet boundary is the unit of loading. (iteration 11)
- Declaring the conversion done once the files exist. Two review rounds found P1s and unmatched mutants after the first green build. (iteration 12)
- Looking for a hub conversion that avoided touching scripts. Every routing reader had to move; there is no compatibility shim in the record. (iteration 12)
- One shared router file for every packet. It was measured at +73 percent tokens on a default-path request and removed. (iteration 12)
- Assuming an automated mirror still exists. The compiler is retired and the generated regions are archived. (iteration 13)
- Looking for a checksum ledger to compare the two repositories. None is kept by design. (iteration 13)
- Treating the git submodule or symlink as a clean sharing mechanism. The vendoring decision exists precisely because links fail in a standalone clone. (iteration 13)
- A fully generated Project mirror. It would contradict the hand-parity contract and the review-recording rule. (iteration 14)
- A published-package route for a skill-only artifact. Neither precedent publishes a skill; the plugin publishes a compiled server, which is a different problem. (iteration 14)
- Symlinks or submodules for the embedded skill. Both fail the clone requirement, and the plugin build rejects links outright. (iteration 14)
- Adding the diagram capability as a seventh command inside the existing skill. The registry's five lanes are artifact modes with one workflow manifest; a canvas capability needs its own packet and router. (iteration 15)
- Editing the Project kernel before the skill side lands. The kernel would then point at a path that does not exist yet. (iteration 15)
- Looking for a PO-level route-table checker equivalent to Moneybird's `check-route-table.py`. The PO repo has fixtures but not a hub consistency checker, so that tool would be new. (iteration 15)
- Looking for a gate that reads the skill source and the Project mirror for semantic equivalence. Rule parity counts declared phrases only; everything else is a reviewer obligation. (iteration 16)
- Shipping examples for a new mode without the reply-shape lines the example linter reads. (iteration 16)
- Treating the PO repo as the whole verification surface. Two of the required declarations live in the shared Sync Loop folder outside it. (iteration 16)
- Planning against npm `latest`. It has no FigJam verbs, so a plan built on it would fail at the first write. (iteration 17)
- Searching for a documented rate limit. None exists in the skill; only the external API owner could supply it. (iteration 17)
- Using `fj eval` to fill a capability gap. It converts a bounded pipeline into arbitrary execution against a live board. (iteration 17)
- Exports as a fallback. A PNG or SVG export is exactly what "only output" excludes. (iteration 18)
- Looking for a FigJam export verb that could serve as read-back proof. The FigJam group has no export verb. (iteration 18)
- Treating the markdown receipt as a second output. It is verification evidence, not a deliverable, and calling it an output would contradict the topic. (iteration 18)
- Assuming a Figma connector exists for claude.ai. Nothing in the repository registers one, and the existing Figma MCP is not a connector. (iteration 19)
- Looking for a Project-side export path for a board. There is none; the Project cannot reach Figma at all. (iteration 19)
- Mirroring the FigJam write procedure into Project knowledge. It would instruct a runtime that cannot execute it, which the hand-parity method explicitly excludes. (iteration 19)
- Raising the confidence of any verb-level claim without a live run. The documentation gap is measured, not closable by more reading. (iteration 20)
- Searching for a local record of `fj` output formats. None exists, and the skill's own uncertainty list stands. (iteration 20)
- Treating the sibling Luna lineage as a source. It runs the same topic independently and is not evidence for this lineage's claims. (iteration 20)

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
Follow up on: The research format has a working precedent in this workspace: the Moneybird routing research lineage produced a fourteen-section `research.md` with a convergence appendix, so the synthesis can follow a house shape ra...

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

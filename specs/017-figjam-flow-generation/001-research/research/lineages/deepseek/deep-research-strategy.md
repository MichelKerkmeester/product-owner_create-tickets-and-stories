---
title: Deep Research Strategy - Product Owner FigJam flows
description: Session tracking for the Product Owner FigJam research lineage, listing key questions, known context, stop conditions and per-iteration focus.
trigger_phrases:
  - "figjam research strategy"
  - "product owner figjam"
importance_tier: normal
contextType: planning
---

# Deep Research Strategy - Product Owner FigJam flows

## 1. OVERVIEW

### Purpose

Persistent brain for the deepseek lineage of the Product Owner FigJam research run. Records what to investigate, what worked, what failed, and where to focus next for the twenty-iteration forced-depth run.

### Usage

- **Init:** seeded with the topic, five key questions, known context and stop conditions.
- **Per iteration:** the executor reads Next Focus, writes iteration evidence, and the workflow reducer refreshes machine-owned sections from the ledger.

---

## 2. TOPIC
How can Product Owner (AI Systems/Product Owner) turn screenshots, Figma flows and product docs into FigJam flows, with FigJam as the only output? Cover: FigJam capability and limits through the Figma MCP (.skilled/skills/mcp-tooling/mcp-figma); input handling per type; which sk-design-diagram flow chart rules (.skilled/skills/sk-design/sk-design-diagram) carry over to FigJam; embedding a duplicate of the mcp-figma skill in Product Owner; a Claude Code plugin following Media Editor (AI Systems/Media Editor/runtime/claude-plugin); a low-friction sync path from the embedded copy back to .skilled across two git repos; converting Product Owner to a parent hub following Moneybird Accountant (hub-router.json, mode-registry.json); lessons and mistakes from both precedents; risks. Each iteration opens a new question or deepens an earlier finding. Cite local file and line for every claim.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [ ] What can the Figma MCP build, read and refuse inside FigJam, and what are its hard limits?
- [x] How does each input type, screenshot or Figma frame flow or product doc, become a flow model before any FigJam write?
- [x] Which sk-design-diagram flow rules carry over to FigJam, and which need a FigJam-native replacement?
- [x] How should a Product Owner copy of mcp-figma be embedded, plugin-packaged and synced back to .skilled across two repositories?
- [x] What must Product Owner change to become a parent hub, and which Media Editor and Moneybird Accountant lessons and risks apply?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS
- Building or editing the Product Owner system, `.skilled` skills, or any plugin: this phase produces findings only.
- Commits, branches, pushes, or Figma account operations.
- Judging visual design taste of the resulting diagrams.

---

## 5. STOP CONDITIONS
- Forced depth: run all 20 iterations even if convergence telemetry drops below 0.05, then synthesize with stopReason maxIterationsReached.
- Stop early only for unrecoverable state corruption or a missing required control file.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- How does each input type, screenshot or Figma frame flow or product doc, become a flow model before any FigJam write?
- Which sk-design-diagram flow rules carry over to FigJam, and which need a FigJam-native replacement?
- How should a Product Owner copy of mcp-figma be embedded, plugin-packaged and synced back to .skilled across two repositories?
- What must Product Owner change to become a parent hub, and which Media Editor and Moneybird Accountant lessons and risks apply?

<!-- /ANCHOR:answered-questions -->

---

<!-- MACHINE-OWNED: START -->
<!-- ANCHOR:what-worked -->
## 7. WHAT WORKED
- reading the gating taxonomy before the feature catalogs gave the write/read split in one pass, because the skill classifies every verb exactly once. (iteration 1)
- reading the folder tree before the vision skill showed that the repo already solved step ordering through naming, which changes what the vision step is for. (iteration 2)
- comparing two verb families side by side exposed the absence of a bridge faster than searching for one, because an absence is only meaningful against a complete inventory. (iteration 3)
- reading the trigger list and the export protocol together exposed the contract collision, which a single-lane read would have missed. (iteration 4)
- deriving the model from the verb ceiling instead of from diagram theory kept it renderable, because the transport is the binding constraint. (iteration 5)
- separating grammar from rendering in the first read made the portability question tractable, because grammar rules survive a transport change while renderer rules do not. (iteration 6)
- splitting the rule set by layer (model versus renderer) produced a decision for every rule without needing new sources. (iteration 7)
- reading the manifest config before the manifest exposed the generator contract, which a file listing alone would have hidden. (iteration 8)
- reading the structure block after the quick start exposed the untracked-payload decision, which is the single most reusable idea in this precedent. (iteration 9)
- reading the acceptance criteria for the word "superseded" found the Node assumption faster than reading the plan, because a supersession marks a belief that failed in practice. (iteration 10)
- reading the 13-line router before the 291-line Product Owner bootstrap made the hub's minimality obvious, which reframes the conversion as a small registry plus packaging, not a rewrite. (iteration 11)
- reading the phase record's review paragraph instead of only its file table produced the token measurement and the P1 list, which are the transferable parts. (iteration 12)
- reading the parity note before the Project package made the three-hop chain visible, because the note names each hop in order. (iteration 13)
- scoring each option against the clone requirement eliminated two options without debate, because that constraint is absolute in this workspace. (iteration 14)
- deriving the change list from the bootstrap's own path tables kept it grounded, because those tables are the actual loading contract. (iteration 15)
- reading the gate READMEs by section (declaration, rules, receipts) produced a checklist in the order a change would hit it. (iteration 16)
- ranking by reducibility produced a different ordering than severity alone, because the version gap is both severe and fixable while the public-exposure risk is structural. (iteration 17)
- holding the topic and the protocol side by side produced the receipt distinction, which neither document states alone. (iteration 18)
- reading the kernel's own constraint lines first turned the mirror question into a split, which is a cheap rule the next phase can apply per file. (iteration 19)
- separating actionable from live-run findings produced a handoff list the synthesis can copy, which is the most useful output of a forced-depth run. (iteration 20)

<!-- /ANCHOR:what-worked -->

---

<!-- ANCHOR:what-failed -->
## 8. WHAT FAILED
- the topic's "Figma MCP" framing nearly steered the iteration into describing an authoring MCP; the repo's own routing line corrected it. (iteration 1)
- searching for a documenting markdown file wasted a step; the folder naming itself is the evidence. (iteration 2)
- the first pass assumed FigJam could hold an image; the six-verb list disproved it. (iteration 3)
- expecting a diagram lane in the skill wasted a search; the lane list is complete and short. (iteration 4)
- an early draft assumed tables for swimlanes; the six-verb list removed that option. (iteration 5)
- assuming the validator encoded shape rules was wrong; it encodes labels and depth. (iteration 6)
- an early attempt to keep the merge dot as a "small sticky" broke the grammar, because a sticky is a node, not a junction. (iteration 7)
- a first attempt to treat `leaf-manifest.json` as authored led to a wrong assumption about hand-editing. (iteration 8)
- an early expectation of a rich plugin schema was wrong; the manifest is five fields. (iteration 9)
- expecting the changelog to carry defects was wrong; the phase documents carry them and the changelog carries the propagation steps. (iteration 10)
- expecting a hub-level mode reference wasted a step; the hub intentionally owns no modes. (iteration 11)
- expecting the hub to be a two-file change was only half right; the files are small but the readers are many. (iteration 12)
- expecting a generated manifest wasted a step; its absence is the point. (iteration 13)
- trying to find a submodule precedent used two searches for a mechanism that does not exist here. (iteration 14)
- expecting a hub checker in the PO repo was wrong; the fixture runners are narrower. (iteration 15)
- assuming all parity logic lived in the PO repo was wrong; the wrappers are deliberately thin. (iteration 16)
- the rate-limit search produced an absence rather than a number, which is still a finding but not a budget. (iteration 17)
- the packet's plan and tasks are still template scaffolds, so they could not supply acceptance detail; the goal had to carry it. (iteration 18)
- an early attempt to design a Project-side write path contradicted line 2 and was discarded immediately. (iteration 19)
- no new external evidence was available without a Figma session, so the ratio is low by construction. (iteration 20)

<!-- /ANCHOR:what-failed -->

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### A fully generated Project mirror. It would contradict the hand-parity contract and the review-recording rule. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: A fully generated Project mirror. It would contradict the hand-parity contract and the review-recording rule.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A fully generated Project mirror. It would contradict the hand-parity contract and the review-recording rule.

### A model that needs tables or embedded images. The six-verb surface cannot render either, so any such requirement would force `fj eval` and its arbitrary-mutation gate. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: A model that needs tables or embedded images. The six-verb surface cannot render either, so any such requirement would force `fj eval` and its arbitrary-mutation gate.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A model that needs tables or embedded images. The six-verb surface cannot render either, so any such requirement would force `fj eval` and its arbitrary-mutation gate.

### A published-package route for a skill-only artifact. Neither precedent publishes a skill; the plugin publishes a compiled server, which is a different problem. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: A published-package route for a skill-only artifact. Neither precedent publishes a skill; the plugin publishes a compiled server, which is a different problem.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A published-package route for a skill-only artifact. Neither precedent publishes a skill; the plugin publishes a compiled server, which is a different problem.

### Adding the diagram capability as a seventh command inside the existing skill. The registry's five lanes are artifact modes with one workflow manifest; a canvas capability needs its own packet and router. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: Adding the diagram capability as a seventh command inside the existing skill. The registry's five lanes are artifact modes with one workflow manifest; a canvas capability needs its own packet and router.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adding the diagram capability as a seventh command inside the existing skill. The registry's five lanes are artifact modes with one workflow manifest; a canvas capability needs its own packet and router.

### Assuming a Figma connector exists for claude.ai. Nothing in the repository registers one, and the existing Figma MCP is not a connector. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: Assuming a Figma connector exists for claude.ai. Nothing in the repository registers one, and the existing Figma MCP is not a connector.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Assuming a Figma connector exists for claude.ai. Nothing in the repository registers one, and the existing Figma MCP is not a connector.

### Assuming a headless server-side render step. There is no API-key path for authoring; closure of Desktop or a missing daemon stops the work. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Assuming a headless server-side render step. There is no API-key path for authoring; closure of Desktop or a missing daemon stops the work.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Assuming a headless server-side render step. There is no API-key path for authoring; closure of Desktop or a missing daemon stops the work.

### Assuming an automated mirror still exists. The compiler is retired and the generated regions are archived. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Assuming an automated mirror still exists. The compiler is retired and the generated regions are archived.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Assuming an automated mirror still exists. The compiler is retired and the generated regions are archived.

### Assuming the runtime supplies a Node runtime or expands bundle settings. The spike disproved both, and the manifest was rebuilt around that. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Assuming the runtime supplies a Node runtime or expands bundle settings. The spike disproved both, and the manifest was rebuilt around that.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Assuming the runtime supplies a Node runtime or expands bundle settings. The spike disproved both, and the manifest was rebuilt around that.

### Copying the "no MCP server" choice for a FigJam plugin. Product Owner's writer is an external CLI binary rather than a bundled server, so the two cases do not share a transport. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Copying the "no MCP server" choice for a FigJam plugin. Product Owner's writer is an external CLI binary rather than a bundled server, so the two cases do not share a transport.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Copying the "no MCP server" choice for a FigJam plugin. Product Owner's writer is an external CLI binary rather than a bundled server, so the two cases do not share a transport.

### Declaring the conversion done once the files exist. Two review rounds found P1s and unmatched mutants after the first green build. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: Declaring the conversion done once the files exist. Two review rounds found P1s and unmatched mutants after the first green build.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Declaring the conversion done once the files exist. Two review rounds found P1s and unmatched mutants after the first green build.

### Deferring layout to FigJam. No automatic layout verb exists, so a deferral would produce overlapping nodes. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Deferring layout to FigJam. No automatic layout verb exists, so a deferral would produce overlapping nodes.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Deferring layout to FigJam. No automatic layout verb exists, so a deferral would produce overlapping nodes.

### Editing the Project kernel before the skill side lands. The kernel would then point at a path that does not exist yet. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: Editing the Project kernel before the skill side lands. The kernel would then point at a path that does not exist yet.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Editing the Project kernel before the skill side lands. The kernel would then point at a path that does not exist yet.

### Encoding the diagram capability as a route inside `sk-product-owner`. The manifest config declares one workflow mode, and the router contract maps commands to artifact lanes, not to a second capability. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Encoding the diagram capability as a route inside `sk-product-owner`. The manifest config declares one workflow mode, and the router contract maps commands to artifact lanes, not to a second capability.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Encoding the diagram capability as a route inside `sk-product-owner`. The manifest config declares one workflow mode, and the router contract maps commands to artifact lanes, not to a second capability.

### Exports as a fallback. A PNG or SVG export is exactly what "only output" excludes. -- BLOCKED (iteration 18, 1 attempts)
- What was tried: Exports as a fallback. A PNG or SVG export is exactly what "only output" excludes.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Exports as a fallback. A PNG or SVG export is exactly what "only output" excludes.

### Extracting whole files. The auto-split behavior makes a whole-file read a directory-producing operation, not a bounded input. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Extracting whole files. The auto-split behavior makes a whole-file read a directory-producing operation, not a bounded input.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Extracting whole files. The auto-split behavior makes a whole-file read a directory-producing operation, not a bounded input.

### Hand-maintaining the copy in the plugin directory. The build replaces it and fails on any divergence, so hand edits are rejected by design. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Hand-maintaining the copy in the plugin directory. The build replaces it and fails on any divergence, so hand edits are rejected by design.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Hand-maintaining the copy in the plugin directory. The build replaces it and fails on any divergence, so hand edits are rejected by design.

### Keeping the arc-jump crossing rule. It is an SVG geometry trick with no FigJam equivalent in the six-verb surface. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Keeping the arc-jump crossing rule. It is an SVG geometry trick with no FigJam equivalent in the six-verb surface.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Keeping the arc-jump crossing rule. It is an SVG geometry trick with no FigJam equivalent in the six-verb surface.

### Looking for a `mode-registry.json` in the Product Owner package. It is absent by design. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Looking for a `mode-registry.json` in the Product Owner package. It is absent by design.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a `mode-registry.json` in the Product Owner package. It is absent by design.

### Looking for a checksum ledger to compare the two repositories. None is kept by design. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Looking for a checksum ledger to compare the two repositories. None is kept by design.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a checksum ledger to compare the two repositories. None is kept by design.

### Looking for a FigJam export verb that could serve as read-back proof. The FigJam group has no export verb. -- BLOCKED (iteration 18, 1 attempts)
- What was tried: Looking for a FigJam export verb that could serve as read-back proof. The FigJam group has no export verb.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a FigJam export verb that could serve as read-back proof. The FigJam group has no export verb.

### Looking for a FigJam-native validator in either skill package. Neither the mcp-figma skill nor the diagram skill ships one. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Looking for a FigJam-native validator in either skill package. Neither the mcp-figma skill nor the diagram skill ships one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a FigJam-native validator in either skill package. Neither the mcp-figma skill nor the diagram skill ships one.

### Looking for a gate that reads the skill source and the Project mirror for semantic equivalence. Rule parity counts declared phrases only; everything else is a reviewer obligation. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: Looking for a gate that reads the skill source and the Project mirror for semantic equivalence. Rule parity counts declared phrases only; everything else is a reviewer obligation.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a gate that reads the skill source and the Project mirror for semantic equivalence. Rule parity counts declared phrases only; everything else is a reviewer obligation.

### Looking for a hub conversion that avoided touching scripts. Every routing reader had to move; there is no compatibility shim in the record. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: Looking for a hub conversion that avoided touching scripts. Every routing reader had to move; there is no compatibility shim in the record.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a hub conversion that avoided touching scripts. Every routing reader had to move; there is no compatibility shim in the record.

### Looking for a hub-level mode reference file. The hub has no mode docs of its own; all stage-two routing lives in packets. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Looking for a hub-level mode reference file. The hub has no mode docs of its own; all stage-two routing lives in packets.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a hub-level mode reference file. The hub has no mode docs of its own; all stage-two routing lives in packets.

### Looking for a layout verb in the FigJam group. There is none; positioning is manual through move or update. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Looking for a layout verb in the FigJam group. There is none; positioning is manual through move or update.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a layout verb in the FigJam group. There is none; positioning is manual through move or update.

### Looking for a plugin-specific parity tool in the PO repo. The parity lesson is transferable, but there is no shared checker to reuse. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Looking for a plugin-specific parity tool in the PO repo. The parity lesson is transferable, but there is no shared checker to reuse.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a plugin-specific parity tool in the PO repo. The parity lesson is transferable, but there is no shared checker to reuse.

### Looking for a PO-level route-table checker equivalent to Moneybird's `check-route-table.py`. The PO repo has fixtures but not a hub consistency checker, so that tool would be new. -- BLOCKED (iteration 15, 1 attempts)
- What was tried: Looking for a PO-level route-table checker equivalent to Moneybird's `check-route-table.py`. The PO repo has fixtures but not a hub consistency checker, so that tool would be new.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a PO-level route-table checker equivalent to Moneybird's `check-route-table.py`. The PO repo has fixtures but not a hub consistency checker, so that tool would be new.

### Looking for a Product Owner documentation file that already describes the screenshot library. No PO doc in the skill or bootstrap mentions screenshots, so there is no existing contract to extend. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Looking for a Product Owner documentation file that already describes the screenshot library. No PO doc in the skill or bootstrap mentions screenshots, so there is no existing contract to extend.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Product Owner documentation file that already describes the screenshot library. No PO doc in the skill or bootstrap mentions screenshots, so there is no existing contract to extend.

### Looking for a Project-side export path for a board. There is none; the Project cannot reach Figma at all. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: Looking for a Project-side export path for a board. There is none; the Project cannot reach Figma at all.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Project-side export path for a board. There is none; the Project cannot reach Figma at all.

### Looking for a tracked plugin payload in git. The three payload directories are untracked by design, which is why this precedent answers the drift question so cleanly. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Looking for a tracked plugin payload in git. The three payload directories are untracked by design, which is why this precedent answers the drift question so cleanly.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a tracked plugin payload in git. The three payload directories are untracked by design, which is why this precedent answers the drift question so cleanly.

### Looking for an existing diagram or canvas artifact type in the Product Owner skill. None exists in the lane list or in the export path pattern. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Looking for an existing diagram or canvas artifact type in the Product Owner skill. None exists in the lane list or in the export path pattern.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for an existing diagram or canvas artifact type in the Product Owner skill. None exists in the lane list or in the export path pattern.

### Making a tool packet the default. The registry defaults to the workflow packet so a bare request cannot fall into a CLI execution. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Making a tool packet the default. The registry defaults to the workflow packet so a bare request cannot fall into a CLI execution.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Making a tool packet the default. The registry defaults to the workflow packet so a bare request cannot fall into a CLI execution.

### Mirroring the FigJam write procedure into Project knowledge. It would instruct a runtime that cannot execute it, which the hand-parity method explicitly excludes. -- BLOCKED (iteration 19, 1 attempts)
- What was tried: Mirroring the FigJam write procedure into Project knowledge. It would instruct a runtime that cannot execute it, which the hand-parity method explicitly excludes.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Mirroring the FigJam write procedure into Project knowledge. It would instruct a runtime that cannot execute it, which the hand-parity method explicitly excludes.

### One shared router file for every packet. It was measured at +73 percent tokens on a default-path request and removed. -- BLOCKED (iteration 12, 1 attempts)
- What was tried: One shared router file for every packet. It was measured at +73 percent tokens on a default-path request and removed.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: One shared router file for every packet. It was measured at +73 percent tokens on a default-path request and removed.

### Planning against npm `latest`. It has no FigJam verbs, so a plan built on it would fail at the first write. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: Planning against npm `latest`. It has no FigJam verbs, so a plan built on it would fail at the first write.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Planning against npm `latest`. It has no FigJam verbs, so a plan built on it would fail at the first write.

### Porting the HTML/SVG taste gate wholesale. Its palette, typography and spacing rules describe a rendered page, not a board whose colours and shapes are FigJam primitives. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Porting the HTML/SVG taste gate wholesale. Its palette, typography and spacing rules describe a rendered page, not a board whose colours and shapes are FigJam primitives.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Porting the HTML/SVG taste gate wholesale. Its palette, typography and spacing rules describe a rendered page, not a board whose colours and shapes are FigJam primitives.

### Raising the confidence of any verb-level claim without a live run. The documentation gap is measured, not closable by more reading. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Raising the confidence of any verb-level claim without a live run. The documentation gap is measured, not closable by more reading.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Raising the confidence of any verb-level claim without a live run. The documentation gap is measured, not closable by more reading.

### Reading every screenshot in the corpus. 341 images with a per-flow structure means the folder, not the library, is the unit of work. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Reading every screenshot in the corpus. 341 images with a per-flow structure means the folder, not the library, is the unit of work.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Reading every screenshot in the corpus. 341 images with a per-flow structure means the folder, not the library, is the unit of work.

### Reusing the doc lane to emit a FigJam board. The lane's contract is markdown plus read-back, and a canvas has no read-back equivalent. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Reusing the doc lane to emit a FigJam board. The lane's contract is markdown plus read-back, and a canvas has no read-back equivalent.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Reusing the doc lane to emit a FigJam board. The lane's contract is markdown plus read-back, and a canvas has no read-back equivalent.

### Reusing the HTML/SVG renderer for FigJam. FigJam has no documented HTML or SVG import verb, and the skill explicitly excludes canvas deliverables. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Reusing the HTML/SVG renderer for FigJam. FigJam has no documented HTML or SVG import verb, and the skill explicitly excludes canvas deliverables.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Reusing the HTML/SVG renderer for FigJam. FigJam has no documented HTML or SVG import verb, and the skill explicitly excludes canvas deliverables.

### Searching for a documented rate limit. None exists in the skill; only the external API owner could supply it. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: Searching for a documented rate limit. None exists in the skill; only the external API owner could supply it.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a documented rate limit. None exists in the skill; only the external API owner could supply it.

### Searching for a local record of `fj` output formats. None exists, and the skill's own uncertainty list stands. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Searching for a local record of `fj` output formats. None exists, and the skill's own uncertainty list stands.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a local record of `fj` output formats. None exists, and the skill's own uncertainty list stands.

### Searching the ASCII validator for shape rules. It validates labels, arrows and nesting depth, not shape vocabulary, so shape semantics live only in the type reference. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Searching the ASCII validator for shape rules. It validates labels, arrows and nesting depth, not shape vocabulary, so shape semantics live only in the type reference.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching the ASCII validator for shape rules. It validates labels, arrows and nesting depth, not shape vocabulary, so shape semantics live only in the type reference.

### Searching the mcp-figma skill for an official Figma Dev Mode MCP path. The reference explicitly places it out of scope for this skill, so it is not a fallback the Product Owner may rely on today. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Searching the mcp-figma skill for an official Figma Dev Mode MCP path. The reference explicitly places it out of scope for this skill, so it is not a fallback the Product Owner may rely on today.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching the mcp-figma skill for an official Figma Dev Mode MCP path. The reference explicitly places it out of scope for this skill, so it is not a fallback the Product Owner may rely on today.

### Searching the skill for an official Figma Dev Mode MCP bridge into FigJam. Iteration 1 already placed it out of scope; this iteration confirms nothing else bridges design files to FigJam boards. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Searching the skill for an official Figma Dev Mode MCP bridge into FigJam. Iteration 1 already placed it out of scope; this iteration confirms nothing else bridges design files to FigJam boards.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching the skill for an official Figma Dev Mode MCP bridge into FigJam. Iteration 1 already placed it out of scope; this iteration confirms nothing else bridges design files to FigJam boards.

### Shipping examples for a new mode without the reply-shape lines the example linter reads. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: Shipping examples for a new mode without the reply-shape lines the example linter reads.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Shipping examples for a new mode without the reply-shape lines the example linter reads.

### Symlinks or submodules for the embedded skill. Both fail the clone requirement, and the plugin build rejects links outright. -- BLOCKED (iteration 14, 1 attempts)
- What was tried: Symlinks or submodules for the embedded skill. Both fail the clone requirement, and the plugin build rejects links outright.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Symlinks or submodules for the embedded skill. Both fail the clone requirement, and the plugin build rejects links outright.

### Transporting design frames into FigJam as embedded objects. There is no documented verb for it, and inventing one from the Figma Plugin API would mean `fj eval`, which the skill classes as arbitrary mutation. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Transporting design frames into FigJam as embedded objects. There is no documented verb for it, and inventing one from the Figma Plugin API would mean `fj eval`, which the skill classes as arbitrary mutation.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Transporting design frames into FigJam as embedded objects. There is no documented verb for it, and inventing one from the Figma Plugin API would mean `fj eval`, which the skill classes as arbitrary mutation.

### Treating "Figma MCP" as the FigJam writer. The MCP is a read surface for design context, so a Product Owner flow that claims "the MCP builds the FigJam board" is describing a capability the wired server does not have. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Treating "Figma MCP" as the FigJam writer. The MCP is a read surface for design context, so a Product Owner flow that claims "the MCP builds the FigJam board" is describing a capability the wired server does not have.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating "Figma MCP" as the FigJam writer. The MCP is a read surface for design context, so a Product Owner flow that claims "the MCP builds the FigJam board" is describing a capability the wired server does not have.

### Treating "parent hub" as a large single skill. The hub is a router plus independent packets, and the packet boundary is the unit of loading. -- BLOCKED (iteration 11, 1 attempts)
- What was tried: Treating "parent hub" as a large single skill. The hub is a router plus independent packets, and the packet boundary is the unit of loading.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating "parent hub" as a large single skill. The hub is a router plus independent packets, and the packet boundary is the unit of loading.

### Treating filenames as sufficient. Filenames give the step label and intent but not the on-screen control a step clicks, so OCR or detection is still needed for a grounded node. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Treating filenames as sufficient. Filenames give the step label and intent but not the on-screen control a step clicks, so OCR or detection is still needed for a grounded node.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating filenames as sufficient. Filenames give the step label and intent but not the on-screen control a step clicks, so OCR or detection is still needed for a grounded node.

### Treating the development dependency as the shipped binary. The 45-failure run shows that shortcut fails silently. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Treating the development dependency as the shipped binary. The 45-failure run shows that shortcut fails silently.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the development dependency as the shipped binary. The 45-failure run shows that shortcut fails silently.

### Treating the embedded skill as a folder copy. Three of its files are generated projections, so a plain copy drifts from its own schema on the first edit. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Treating the embedded skill as a folder copy. Three of its files are generated projections, so a plain copy drifts from its own schema on the first edit.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the embedded skill as a folder copy. Three of its files are generated projections, so a plain copy drifts from its own schema on the first edit.

### Treating the existing "Figma feedback" trigger as diagram input. It consumes prose about Figma, not a Figma file. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Treating the existing "Figma feedback" trigger as diagram input. It consumes prose about Figma, not a Figma file.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the existing "Figma feedback" trigger as diagram input. It consumes prose about Figma, not a Figma file.

### Treating the git submodule or symlink as a clean sharing mechanism. The vendoring decision exists precisely because links fail in a standalone clone. -- BLOCKED (iteration 13, 1 attempts)
- What was tried: Treating the git submodule or symlink as a clean sharing mechanism. The vendoring decision exists precisely because links fail in a standalone clone.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the git submodule or symlink as a clean sharing mechanism. The vendoring decision exists precisely because links fail in a standalone clone.

### Treating the markdown receipt as a second output. It is verification evidence, not a deliverable, and calling it an output would contradict the topic. -- BLOCKED (iteration 18, 1 attempts)
- What was tried: Treating the markdown receipt as a second output. It is verification evidence, not a deliverable, and calling it an output would contradict the topic.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the markdown receipt as a second output. It is verification evidence, not a deliverable, and calling it an output would contradict the topic.

### Treating the PO repo as the whole verification surface. Two of the required declarations live in the shared Sync Loop folder outside it. -- BLOCKED (iteration 16, 1 attempts)
- What was tried: Treating the PO repo as the whole verification surface. Two of the required declarations live in the shared Sync Loop folder outside it.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the PO repo as the whole verification surface. Two of the required declarations live in the shared Sync Loop folder outside it.

### Treating the sibling Luna lineage as a source. It runs the same topic independently and is not evidence for this lineage's claims. -- BLOCKED (iteration 20, 1 attempts)
- What was tried: Treating the sibling Luna lineage as a source. It runs the same topic independently and is not evidence for this lineage's claims.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the sibling Luna lineage as a source. It runs the same topic independently and is not evidence for this lineage's claims.

### Trusting creation output to return ids. That contract is undocumented; a read-back step is the only grounded option. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Trusting creation output to return ids. That contract is undocumented; a read-back step is the only grounded option.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Trusting creation output to return ids. That contract is undocumented; a read-back step is the only grounded option.

### Using `fj eval` to fill a capability gap. It converts a bounded pipeline into arbitrary execution against a live board. -- BLOCKED (iteration 17, 1 attempts)
- What was tried: Using `fj eval` to fill a capability gap. It converts a bounded pipeline into arbitrary execution against a live board.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Using `fj eval` to fill a capability gap. It converts a bounded pipeline into arbitrary execution against a live board.

<!-- /ANCHOR:exhausted-approaches -->

---

<!-- ANCHOR:ruled-out-directions -->
## 10. RULED OUT DIRECTIONS
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
[None yet]

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
Follow up on: The research format has a working precedent in this workspace: the Moneybird routing research lineage produced a fourteen-section `research.md` with a convergence appendix, so the synthesis can follow a house shape ra...

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT

### Bounded Context Snapshot

- Source pointers: `.skilled/skills/mcp-tooling/mcp-figma/` (tool surface, feature catalogs, changelog), `.skilled/skills/sk-design/sk-design-diagram/` (flow rules, references, benchmark reports), `AI Systems/Product Owner/` (AGENTS.md, sk-product-owner, claude project, SYNC.md, specs 001-016), `AI Systems/Media Editor/runtime/claude-plugin/` (plugin packaging precedent), `AI Systems/Moneybird Accountant/hub-router.json` and `mode-registry.json` (parent-hub precedent), `specs/z-staging-po-017-research/` (goal, spec, plan, tasks).
- Reuse candidates: mcp-figma skill package, sk-design-diagram flow-chart rule set, Media Editor plugin manifest and marketplace files, Moneybird hub-router and mode-registry JSON shapes.
- Integration points: Product Owner AGENTS.md bootstrap, its skill package, Claude Project knowledge/parity files, and the `.skilled` source of truth in this repository.
- Constraints and risks: FigJam-only output, public-repo privacy, Figma auth and rate limits, two-repository sync drift, parity and format gates.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 20
- Convergence threshold: 0.05 (mode off; telemetry only)
- Stop policy: max-iterations
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true
- research/research.md ownership: workflow-owned canonical synthesis output
- Lifecycle branches: resume, restart (live); fork, completed-continue (deferred)
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A
- Question injection surface: research/inbox.jsonl
- Canonical pause sentinel: research/.deep-research-pause
- Current generation: 1
- Started: 2026-10-19T21:03:00Z

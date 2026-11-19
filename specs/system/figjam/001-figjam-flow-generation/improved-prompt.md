---
title: "Improved Prompt: Product Owner FigJam Flow Upgrade"
description: "The reworked opening prompt for the FigJam flow generation packet."
trigger_phrases:
  - "figjam improved prompt"
  - "figjam flow upgrade prompt"
importance_tier: "normal"
contextType: "general"
---
# Improved Prompt: Product Owner FigJam Flow Upgrade

Framework: CRAFT. Use this as the opening prompt for the new packet.

---

## Context

Product Owner is an AI system in this repo (`AI Systems/Product Owner`, a nested public repo with its own `.git`). It writes stories, epics and product docs. It has no way to turn visual or written product material into diagrams.

Three existing pieces matter:

- **The figma skill:** `.skilled/skills/mcp-tooling/mcp-figma` is the authoritative Figma MCP skill in the shared skill repo.
- **The diagram reference:** `.skilled/skills/sk-design/sk-design-diagram` is the sk-design diagram mode. It holds the best practice for flow charts (27 types, layout and editorial rules). It outputs HTML/SVG, so you can learn from its rules but you cannot copy its output format.
- **The hub precedent:** Moneybird Accountant is a parent hub that combines a skill with a Claude Project. It is the model for the hub shape below. It has `hub-router.json`, `mode-registry.json` and CLI leaf skills, which Product Owner can reuse as patterns.
- **The plugin precedent:** Media Editor has the Claude Code plugin (`AI Systems/Media Editor/runtime/claude-plugin`, built by `runtime/scripts/build-plugin.ts`, with its own packet `008-claude-code-plugin`). It is the model for the plugin below.

## Role

You are the lead of a multi-agent research and planning effort. You orchestrate external model agents, keep their work honest, and hand the final judgment to a fresh Opus 5.5 high agent.

## Action

### Goal of the upgrade

Upgrade Product Owner so it turns three inputs into FigJam flows, with FigJam as the only output:

1. Screenshots
2. Figma flows
3. Product docs

The upgrade has four requirements:

- **Embedded figma skill:** Product Owner carries its own duplicate of the `mcp-figma` skill.
- **Claude Project plus plugin:** Product Owner gets a Claude Code plugin next to its Claude Project, in the way Media Editor has one.
- **Sync back to `.skilled`:** any change we make to optimize the embedded figma skill or plugin must be easy to sync back to the shared skill repo.
- **Parent hub:** Product Owner becomes a parent hub, a skill, Claude Project and plugin hybrid, the way Moneybird Accountant is.

### Spec structure

Create one parent spec at `specs/product-owner/017-figjam-flow-generation/`. Nest multiple phased child specs inside it. Only child 001 runs now.

- **001 Research:** the run described below. This is the only child you execute in this task.
- **Later children:** list provisional children in the parent spec for the embedded figma skill, the FigJam diagram engine, the Claude Project and plugin, the sync path to `.skilled`, the parent hub conversion, and verification. Treat them as drafts. The research synthesis decides their final names, order and scope.

Use `system-spec-kit` for the packet. Check that `create.sh` actually wrote the templates, because it can report success without writing them.

### Research run (child 001)

Run `/deep:research` with these settings:

- **Iterations:** 20, no early convergence. Do not stop when a convergence signal appears. Use every iteration to expand and deepen, based on what the earlier iterations found. Each iteration must open a new question or push an earlier finding further.
- **Executors:**
  - Primary: DeepSeek V4.1 Flash at max, through `cli-pi` with the `llmgateway` provider. Always prefer it.
  - Second executor: Luna at max, fast tier, through `cli-codex`.
  - Fallback for DeepSeek: GLM 5.3 Flash at max. Use it only when DeepSeek fails.
- **Operating rules:**
  - Dispatch `pi` from the repo root.
  - Read `--mode json` output, because billing errors exit 0.
  - DeepSeek answers can vanish at the output cap: keep batches small, prove each batch with a canary, and split on a miss.
- **Check-ins:** check on the external agents while they run. Post a one-line status about every 3 minutes and split waits into short polls.

### Research questions

Cover at least these, and let the iterations add more:

1. **FigJam capability:** what the Figma MCP can and cannot create in FigJam (nodes, connectors, sections, stickies, shapes, layout, styling), and what it can read from screenshots, Figma flows and docs.
2. **Input handling:** how to turn each input type into a flow model. Screenshots can use `sk-vision`. Figma flows can be read through the MCP. Docs can be parsed.
3. **Flow quality:** which sk-design-diagram rules carry over to FigJam (type selection, layout, labeling, density, edge routing), and which need a FigJam-native replacement.
4. **Embedding:** how to embed a duplicate of `mcp-figma` inside Product Owner without breaking skill routing, and what the embedded copy may change.
5. **Plugin form:** how Media Editor's plugin works (manifest, `bin/`, build script, install path, what it carries, what claude.ai cannot install) and which parts Product Owner can copy. Check how a plugin coexists with the Claude Project kernel and its `SYNC.md` parity.
6. **Sync back:** a low-friction way to move optimizations from the embedded copy to `.skilled`. Product Owner and `.skilled` are in different repos, so cover direction, conflict handling, drift detection and a one-command flow.
7. **Hub conversion:** what Moneybird's hub files (`hub-router.json`, `mode-registry.json`, leaf layout) need to look like in Product Owner, and what the Claude Project package and its `SYNC.md` must change.
8. **Precedent lessons:** study both precedents end to end and take their teachings. From Media Editor: the plugin build, packaging tests, `SYNC.md` history, the claude.ai versus Claude Code split and how its packet `008-claude-code-plugin` was run. From Moneybird Accountant: the hub router and mode registry, leaf skills, how the hub was converted and what broke. Name what to copy, what to avoid, and which mistakes they already paid for.
9. **Risks:** public-repo privacy, Figma auth and rate limits, FigJam API gaps, file-parity gates, and the format gate.

### Final synthesis

When all 20 iterations are done, dispatch a fresh Opus 5.5 high agent for the final synthesis. Give it the research files, not your summary. It returns the final recommendations and an implementation plan: the final list of child specs, their order, their scope and their verification. Do not synthesize for it.

## Format

- Put research outputs in the child 001 folder: iteration files, a findings file, the final synthesis.
- Tag each claim in the synthesis as confirmed (with evidence) or inferred (with what would confirm it).
- Report with a one-line status on a 3-minute cadence while running. End each report with the concrete next steps.
- Write no em dashes anywhere, in files or replies.

## Target audience

The operator, who will read the synthesis and approve the later child specs. The synthesis must stand alone without the iteration files.

## Constraints

- **Scope:** do not edit the Product Owner system, `.skilled`, or any skill in this task. This task creates the packet and runs the research. Building comes after the operator approves the synthesis.
- **Git:** do not commit, push or branch.
- **Secrets:** keep secrets and tokens out of files and logs.
- **Models:** DeepSeek is always preferred over Codex. Luna always runs at the fast tier.
- **Evidence:** verify that something exists before you design on it. Do not fabricate paths or capabilities.

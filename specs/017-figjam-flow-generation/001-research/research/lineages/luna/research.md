# Product Owner to FigJam Flow Generation — Research Synthesis

Research lineage: Luna, iterations 1–8. Prepared 2026-10-19T21:21:48Z. Terminal stop reason: maxIterationsReached. This report synthesizes the bounded Luna lineage and is not a live FigJam capability test. [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-config.json:3] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-strategy.md:78] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:6-10]

## 1. Executive Summary

- The local mcp-figma package makes the Figma Desktop CLI its primary authoring surface and treats Framelink MCP as an optional read-context path; its FigJam namespace documents reads and named create/edit operations, with delete and arbitrary eval kept out of the default path. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:14] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:46] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-152] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:186-191]
- Product Owner should own source classification, flow meaning, route selection, and the FigJam-only result; an embedded mcp-figma tool packet should own explicit board operations. This follows Moneybird’s workflow/tool packet split and the Product Owner requirement that FigJam be the only output. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-67] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-83] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30-35] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:5-19] [INFERENCE: retain Product Owner as the default workflow packet and make mcp-figma a non-default tool packet]
- The first implementation gate should verify the installed CLI, live help, screenshot intake, one isolated FigJam write, and board read-back. This research used static source review only; it did not inspect a live Figma tool schema, run CLI help, build a plugin, or write a FigJam board. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:165] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:75-79] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:6-10] [INFERENCE: a live feasibility gate should precede implementation]

## 2. Research Objective and Scope

The parent specification asks Product Owner to accept screenshots, Figma flows, and product documents, emit FigJam only, embed mcp-figma, add a Claude Code plugin, sync skill improvements back to the shared repository, convert into a parent hub, and verify the result. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-84]

The research phase includes input handling, diagram-rule transfer, plugin and hub precedents, cross-repository synchronization, privacy, Figma authentication and rate-limit risks, parity gates, and the format gate; it excludes implementation, edits to Product Owner or .skilled, and Git commits, pushes, or branches. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:74-83]

## 3. Evidence and Boundaries

The Luna registry records eight completed iterations, five resolved tracked questions, and zero registry-open questions. The strategy lists all five key questions as answered and sets the terminal stop condition to eight iterations with convergence disabled. [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/findings-registry.json:801-818] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-strategy.md:62-89] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-strategy.md:78-79]

The eight-iteration Luna lineage is narrower than the phase specification, which calls for a twenty-iteration DeepSeek lineage plus a fresh Opus 5.5 synthesis. This document therefore represents the requested Luna lineage only; it does not claim the parent phase’s multi-lineage handoff or Opus review is complete. [SOURCE: specs/z-staging-po-017-research/spec.md:48-51] [SOURCE: specs/z-staging-po-017-research/spec.md:101-104] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-config.json:3-8] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:55-56]

The run performed static repository inspection rather than live Figma or plugin execution. The mcp-figma reference itself says its Framelink package is @latest, its names and schemas are not pinned, and callers should rediscover tools and schemas before use. [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:6-10] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-112]

The phase risk list explicitly calls out public-repository privacy, Figma authentication, rate limits, parity gates, and format validation; it also prohibits secrets in research files and unreviewed transfer of private Product Owner context through external model prompts. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:79] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:143-145]

## 4. FigJam Capability Through the Local Figma Tooling

mcp-figma describes the CLI as its primary surface and Framelink MCP through Code Mode as an optional way to pull design data, variables, and screenshots into model context. The MCP manual’s confirmed list contains file/node design-data retrieval and referenced image/SVG downloads; the FigJam write operations are documented in the CLI namespace. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:14] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:46] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-150]

| FigJam surface | Documented operation | Role |
|---|---|---|
| Read | fj list, fj info, fj nodes | Inspect pages and nodes. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] |
| Write | fj sticky, fj shape, fj text, fj connect, fj move, fj update | Create or edit board content. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150] |
| Destructive | fj delete | Exclude from normal generation; require a specific request and stronger safeguards. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:151] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:186-190] |
| Arbitrary | fj eval | Keep out of the default route. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:152] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:191] |

The documented CLI needs Figma Desktop open with a file, Node.js 18 or newer, and the silships figma-ds-cli on PATH. The skill says the full documented command surface is version 1.2.0 from the silships repository; the npm 1.0.0 build is minimal and lacks documented features such as safe mode, daemon, and extract. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:54]

## 5. Limits and Safety Guarantees

The optional MCP runs through a changing @latest server, and its tool schemas are not pinned in this repository; live discovery and tool_info inspection are required before depending on a call signature. The Figma URL example exposes fileKey and nodeId, but that example is not a substitute for checking the current schema. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-114] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:129-135]

The mcp-figma policy requires an explicit target, a description of the effect, a rollback note, and confirmation before FigJam write verbs. Destructive deletes and arbitrary evaluation are omitted from the default flow. The Product Owner adapter should preserve these gates and narrow them to the selected FigJam board and node set. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:179-191] [INFERENCE: the Product Owner route should expose only the named FigJam verbs needed for generation]

The local manuals document screenshot-url for importing a website screenshot into Figma, but the reviewed MCP list is limited to Figma data and referenced image retrieval. They do not establish OCR or arbitrary local screenshot-file ingestion; that capability must be treated as unverified. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112] [INFERENCE: the consulted references provide no evidence for local screenshot OCR/import]

## 6. Input Handling by Type

| Input | Recommended handling | Evidence and unresolved point |
|---|---|---|
| Screenshot | Extract actors, visible steps, decisions, labels, and outcomes into a source-linked flow model; retain image/crop provenance for review. Verify which local vision/OCR path is available before promising automatic extraction. | The documented screenshot-url path is a website capture into Figma, and the MCP list does not establish local-image OCR. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112] [INFERENCE: source-linked extraction is the safest unverified-input design] |
| Figma flow | Parse fileKey and nodeId from the supplied design URL, discover the current MCP tools and schema, request the smallest useful node scope, and use downloaded referenced images only when needed. Convert the inspected flow into the shared semantic model before making FigJam writes. | The manual shows URL identifiers, node-scoped retrieval, and image download, and warns that names and schemas can change. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:129-148] [INFERENCE: a normalized model separates source inspection from board mutation] |
| Product document | Classify every material claim as current behavior, approved direction, proposal, retired material, or unknown; preserve labels at claim or section level; stop composition where authority does not resolve a contradiction. Map accepted claims and explicit branches into the semantic model. | Product Owner’s Doc Mode defines these classes and says unresolved conflicts stop composition rather than being blended. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-160] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:168-186] |
| Mixed sources | Keep the request in Product Owner while it establishes authority and reconciles the sources; hand off only the explicit board operation after the flow model and target are ready. | Product Owner uses one primary route/resource lane, and Moneybird keeps workflow work in its default packet before a concrete tool handoff. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:32-35] [INFERENCE: mixed-source FigJam work should stay in the Product Owner workflow packet] |

The public specification makes FigJam the sole output and explicitly excludes HTML and SVG deliverables. Internal classification and flow-model data may guide generation, but the user-facing artifact should be the FigJam board. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-84] [INFERENCE: treat internal models as implementation data, not an additional deliverable]

## 7. Recommended End-to-End Architecture

1. Intake chooses among screenshot, Figma URL/node, product document, or mixed sources and retains source identity and provenance. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-79] [INFERENCE: add a typed intake record with source and claim provenance]
2. A source adapter extracts candidate steps and decisions; Product Owner’s source authority and status rules resolve them before the diagram is generated. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-160] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:168-186]
3. A shared semantic flow model represents start/end, action, decision, merge, and labeled transitions independently of FigJam geometry. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-25] [INFERENCE: a format-independent flow model avoids duplicating meaning across source adapters]
4. A FigJam adapter maps those nodes and transitions to the current fj shape, text, and connect operations. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-150] [INFERENCE: use FigJam-native primitives and discover their live arguments]
5. Before mutation, name the target board and rollback; after the write, read the board back and verify its content and connector paths. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:179-184] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [INFERENCE: board read-back is the FigJam equivalent of Product Owner’s file read-back gate]

This boundary leaves product interpretation and output policy with Product Owner and board mechanics with the tool packet, consistent with Moneybird’s two-stage routing and with Product Owner’s own source-safe Doc Mode. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30-38] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:164-186] [INFERENCE: workflow and tool responsibilities should remain separate]

## 8. Flowchart Rules to Carry into FigJam

| Rule | Transfer decision |
|---|---|
| Node meaning | Carry the distinct start/end, action, decision, and merge semantics; use native FigJam shape equivalents after checking the live command options. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-24] [INFERENCE: map semantic types to the FigJam shape vocabulary] |
| Direction and branches | Keep the flow top-down, label every decision exit, limit a diamond to at most three exits, and refactor a larger branch into nested decisions. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:23-32] |
| Color | Use color as an accent rather than a code for node type; keep focal accents restrained. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:25-31] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:268] |
| Density and grid | Preserve one distinct idea per node, remove redundant links, and target readable density; validate the 9-node split heuristic and 4px grid in FigJam instead of assuming SVG coordinates transfer. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:260-266] [INFERENCE: these numeric layout thresholds need a FigJam prototype] |
| Connectors | Preserve orthogonal routes, labels with visible clearance, non-overlapping paths, distinct attach points, and routes around unrelated nodes; translate SVG-specific radii, masks, bridges, and pixel spacing into FigJam-native controls. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:291-295] [INFERENCE: FigJam-native equivalents need visual confirmation] |
| Delivery mechanics | Do not carry over HTML wrappers, SVG semantics, HTML/SVG validators, or SVG exports as deliverables; the Product Owner scope makes FigJam the only output. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:269-272] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79-83] |

## 9. Embedding the mcp-figma Skill

Product Owner’s parent specification says the current figma skill lives in the shared .skilled repository and asks for an embedded duplicate. The Product Owner manifest is currently a standalone single-mode manifest with leaf roots for references, assets, and the testing playbook; a copy must be made routable and inventoried rather than left as an unreferenced folder. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-67] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2-11] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:103-111]

Recommended layout: vendor the upstream mcp-figma subtree intact as a dedicated tool packet, then keep Product Owner-specific FigJam limits, output policy, and source behavior in a thin adapter or packet router. The upstream skill covers broad Figma authoring and export, while the Product Owner requirement is FigJam-only; separating the adapter reduces the risk of accidentally changing upstream Figma behavior. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:14] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-163] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-83] [INFERENCE: keep the vendored source and Product Owner wrapper as distinct layers]

Copying instructions does not add the required tools: Product Owner currently lists file-oriented tools, whereas mcp-figma requires Bash and Code Mode MCP; its CLI also requires Node and an open Figma Desktop file. The plugin or host setup must expose and preflight these runtime dependencies. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-5] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:54] [INFERENCE: skill vendoring alone cannot provide missing host capabilities]

## 10. Low-Friction Cross-Repository Sync

The phase research spec confirms that Product Owner’s vendored copy and the shared mcp-figma skill are in two Git repositories, and the parent spec says shared-skill changes should travel only through a sync path. Product Owner’s existing SYNC.md handles manual parity between its skill and claude.ai Project files; it has no manifest, lock, or checksum ledger for the separate vendor-copy problem. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:63] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:83] [SOURCE: AI Systems/Product Owner/SYNC.md:8-15]

Recommended round-trip:

1. Keep an upstream source path, accepted source revision, and vendored destination path in a small sync manifest owned by Product Owner. [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2-11] [INFERENCE: an explicit manifest makes the two roots and revision reviewable]
2. For upstream-to-vendor sync, compare the selected mcp-figma subtree, stop on local divergence, and update the vendored copy only from an accepted shared-source revision. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:83] [INFERENCE: this preserves the shared source as authority]
3. For a useful improvement discovered in Product Owner, export a patch from the embedded copy, review and accept the change in the shared .skilled repository, then refresh the embedded copy from that accepted source revision. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:63] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-83] [INFERENCE: a reviewed patch and re-vendor cycle avoids blind bidirectional overwrites]
4. Keep Claude Project manual parity as a separate process; it decides which skill paragraphs apply in that Project and records drift through read-only commit-timestamp comparison. [SOURCE: AI Systems/Product Owner/SYNC.md:8-15]

## 11. Parent Hub and Routing Design

Moneybird separates stage-one packet selection from packet-level routing. Its root SKILL.md selects a packet using hub-router.json and mode-registry.json; each packet’s router and skill own its own route rules and contract. The registry labels its default packet as a workflow and every non-default packet as a tool. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:10] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30-38] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:4-27] [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:2-12] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:201] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:903-905]

Recommended Product Owner mapping:

| Packet | Kind | Responsibility |
|---|---|---|
| Product Owner workflow | Default workflow | Keep backlog, Doc, source-authority, input normalization, flow meaning, and FigJam-only delivery rules. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:42-74] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [INFERENCE: preserve the existing workflow as the default packet] |
| mcp-figma FigJam adapter | Non-default tool | Expose only the named board reads/writes needed after flow meaning and target are resolved. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-191] [INFERENCE: the Figma CLI surface is a tool packet] |

Product Owner currently maps the word figma to UI-refinement Task Mode. Route FigJam by explicit output intent, such as a dedicated $figjam command or “make a FigJam flow,” and preserve ordinary Figma UI feedback in Task Mode. Mixed input requests should start in the Product Owner workflow; a mention of a CLI, FigJam, or Figma in negation, quotation, or explanation should not itself authorize a board write. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:66-73] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:97] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:32-35] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:179-191] [INFERENCE: use output intent for routing and require separate authorization for mutation]

A hub conversion should add a root hub contract, hub-router.json and mode-registry.json, and update Product Owner’s AGENTS.md bootstrap to load the hub before the selected packet. Preserve the current single-mode skill as the default workflow packet rather than treating its leaf manifest as the hub registry. [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2-11] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:44-55] [SOURCE: AI Systems/Moneybird Accountant/AGENTS.md:36-50] [INFERENCE: adapt Moneybird’s hub bootstrap and keep the current Product Owner workflow packet]

## Eliminated Alternatives

These are evidence-based design choices, not experiments run by this lineage.

| Approach | Reason excluded | Evidence | Status |
|---|---|---|---|
| Use Framelink MCP as the FigJam authoring surface | Its documented tools retrieve Figma file/node data and images; FigJam create/edit verbs are in the CLI surface. | [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-150] | Excluded by documented surface, not live-tested. |
| Deliver HTML or SVG alongside the board | The parent scope explicitly excludes both and names FigJam as the only output. | [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79-83] | Excluded by scope. |
| Route any request containing “Figma” directly to the FigJam tool | Product Owner already routes figma to Task Mode, and Moneybird’s recorded reviews found prefix and contextual-negation false routes. | [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:97] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-90] | Excluded by routing evidence. |
| Blindly copy changes in both directions between Git roots | The Product Owner copy and shared source are separate repositories, and current Claude Project parity has no vendor lock or checksum ledger. | [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:63] [SOURCE: AI Systems/Product Owner/SYNC.md:8-15] | Excluded by repository boundary; recommend reviewed patch flow. |
| Bundle Media Editor’s custom multi-platform runtime into the first PO plugin | Media Editor bundles its own server and platform dependencies; mcp-figma expects an installed Figma CLI and open Desktop. | [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:31-38] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-18] | Excluded unless a prototype demonstrates a missing capability. |

## Divergence Map

The lineage registry records zero completed pivots, failed pivots, overrides, or saturated directions, with an empty remaining frontier. This means no divergence pivots were recorded; it does not prove the live tool path or the broader topic is converged. [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/findings-registry.json:795-796] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/findings-registry.json:816-818] [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:2166-2167]

## 12. Open Questions

1. Which installed figma-ds-cli version is available, and what exact flags and shapes does its live fj help expose? The documented command inventory is a version snapshot and directs users to live help. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:165]
2. Can the host extract steps and branches from a local screenshot without sending private context externally, and what provenance should be kept for uncertain OCR? The CLI manual only documents website screenshot import, and the phase privacy requirement bars unreviewed external transfer. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:143-145]
3. Which FigJam board-selection, permission, and read-back operations are available in the installed environment? The current FigJam surface lists reads and writes but the tool documentation says to verify live commands. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-165]
4. What authentication and rate-limit behavior applies to this Figma environment? The phase spec explicitly lists both as risks but this static lineage did not test either. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:79] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:10]
5. Which host tools will a Claude Code plugin expose to the Product Owner skill, and what exact dependencies should its preflight enforce? The current Product Owner and mcp-figma tool declarations differ. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-5]

## 13. Risk Register

| Risk | Impact | Control | Evidence |
|---|---|---|---|
| CLI/MCP version or schema drift | The adapter could call unsupported commands or interpret source data incorrectly. | Check CLI version/help at startup, discover MCP tools/schema before use, and fail closed on unknown signatures. | [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:165] |
| Unauthorized or overly broad mutation | Wrong board or a broad delete/eval could change unrelated content. | Name the target board/node, show effect and rollback, confirm writes, and omit delete/eval from ordinary generation. | [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:179-191] |
| Screenshot extraction and source ambiguity | OCR or inferred branches may turn a visual guess into a false product fact. | Keep source provenance and uncertainty attached to extracted claims; use Product Owner’s status and conflict rules. | [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-160] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:168-186] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145] [INFERENCE: preserve uncertainty until a source owner resolves it] |
| Router false positives and false negatives | Figma mentions, negation, or mixed requests could reach the wrong packet or trigger a write. | Add whole-word and context guards, route by explicit FigJam output intent, use route gold cases and mutants, then perform live routing smoke. | [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-103] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:109-123] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:97] [INFERENCE: adapt the precedent’s gold-route and live-smoke separation] |
| Cross-repository drift | Vendor changes could silently diverge from the shared skill or overwrite unreviewed work. | Track source revision and explicit roots, compare before sync, review a patch in the shared source, and re-vendor only after acceptance. | [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:63] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:83] [SOURCE: AI Systems/Product Owner/SYNC.md:8-15] [INFERENCE: source revision plus review is a narrow drift control] |
| Secret or private-source leakage | Figma credentials or private Product Owner material could enter artifacts or external prompts. | Never write tokens to research/logs and review any external prompt containing private context. | [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:143-145] |
| Plugin/project boundary confusion | Users could expect Claude Code’s bin plugin to operate in claude.ai Project or Cowork. | Document plugin support as Claude Code only and keep its packaging separate from manual Project parity. | [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:15] [SOURCE: AI Systems/Product Owner/SYNC.md:8-15] |
| Diagram geometry copied literally | SVG-specific dimensions may not produce readable FigJam connectors. | Test representative routes on a FigJam board and inspect board read-back before expanding the adapter. | [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:291-295] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-150] [INFERENCE: validate layout values in the destination renderer] |

## 14. Risk-Ordered Implementation Plan

### Phase 0 — Feasibility spike

On an isolated test board, record the installed CLI version, inspect live FigJam help, verify the Figma Desktop connection and board selection, create a small sample using named fj operations, and read it back. Separately try a representative screenshot and document whether a local image extraction path is available. Gate further work on successful FigJam-only output and the documented mutation safeguards. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-5] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-184] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79-84] [INFERENCE: isolate the first live write and read-back before building on the API]

### Phase 1 — Vendor boundary and sync contract

Add the mcp-figma subtree as a dedicated embedded packet, record its upstream revision, document the Product Owner adapter boundary, and design a two-root drift/patch flow. Test conflict refusal and one accepted patch round-trip before allowing routine updates. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-67] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:63] [SOURCE: AI Systems/Product Owner/SYNC.md:8-15] [INFERENCE: prove the vendor update path before maintaining a long-lived duplicate]

### Phase 2 — Hub and route conversion

Add Product Owner root hub instructions, hub-router.json, and mode-registry.json; preserve its current backlog and documentation skill as the default workflow packet and register mcp-figma as a tool packet. Update AGENTS.md to bootstrap the hub and chosen packet. Route explicit FigJam output intent separately from ordinary Figma UI feedback, and create gold rows for mixed sources, negated/quoted mentions, and tool-only operations. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30-38] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:5-19] [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:2-12] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:903-952] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44-73] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:97] [INFERENCE: implement the hub’s packet contract around the existing Product Owner workflow]

### Phase 3 — Source adapters and semantic flow engine

Implement typed adapters for screenshots, Figma node URLs, and product documents, with provenance, source status, unresolved claims, and a flow graph that preserves actors, steps, decisions, merges, outcomes, and labeled transitions. Make the first screenshot adapter conditional on Phase 0 evidence. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:129-148] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-186] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-32] [INFERENCE: a shared semantic graph allows each source type to reach the same FigJam renderer]

### Phase 4 — FigJam layout and thin Claude Code plugin

Build a FigJam-native layout adapter for the verified fj commands; keep connectors readable and the allowed write surface narrow. Add a Claude Code bin shim that checks Node, Figma Desktop, CLI version, and command help, then invokes the Product Owner workflow. Do not bundle Media Editor’s custom server unless the feasibility phase finds a required capability missing from the external CLI. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-191] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-18] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9-15] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:31-38] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83] [INFERENCE: a thin shim fits the external CLI dependency better than a second custom server]

### Phase 5 — Integrated checks and release readiness

Run the Product Owner route corpus and mutants, compare the vendored subtree with its accepted source revision, verify plugin installation and host boundaries, test safe write/read-back on an isolated FigJam board, and confirm no HTML/SVG deliverable is created. Keep fixture scores separate from live model-routing evidence. [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/feature-catalog/reference-and-state/hub-and-packet-routers.md:32-57] [SOURCE: AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:418-439] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79-84] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:109-123] [INFERENCE: these gates cover the known packaging, routing, mutation, and output risks]

## 15. Verification Plan

| Gate | Evidence to collect |
|---|---|
| Source and adapter | Tests for each input type, status preservation, conflict handling, node/edge counts, and FigJam shape/connector mapping. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-186] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-32] [INFERENCE: exercise each adapter against its source contract] |
| Routing | Gold fixtures for $figjam, “make a FigJam flow,” ordinary Figma UI feedback, mixed inputs, Figma/CLI names in quotes or negation, and explicit board-tool commands; add mutants for prefix and raw-text guards. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:68-73] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:97] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-103] [INFERENCE: mirror the precedent’s route mutation tests] |
| Embedded copy and sync | Check source revision, drift output, refusal on divergence, reviewed patch application, and exact post-sync copy. Keep this separate from plugin packaging and Claude Project parity. [SOURCE: AI Systems/Product Owner/SYNC.md:8-15] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83] [INFERENCE: validate the two synchronization boundaries independently] |
| Plugin | Validate manifest, executable shim, preflight failures, Claude Code support, and no accidental claim of claude.ai execution. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9-15] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:70-83] |
| Live FigJam | On a test board, confirm target, safe named writes, readable connectors, and node/edge read-back; record CLI/MCP versions and schema observed. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-184] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-112] [INFERENCE: a live board check complements static route fixtures] |
| Output and privacy | Assert the result is a FigJam board with no HTML/SVG sidecar, no token in logs, and no unreviewed private context in an external prompt. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79-84] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:143-145] |

No plugin build, new route corpus, or live FigJam gate was run for this research lineage; these are proposed downstream verification steps. [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:6-10]

## 16. Precedent Lessons and Mistakes

### Moneybird Accountant hub

The first reviewed hub had a prefix false positive where “Jortt clients” matched a Jortt CLI signal, and a request naming a CLI could bypass the accountant workflow during migration. A raw-text refusal fix then dropped a valid invoice handoff containing “Don’t submit anything.” Later work added gold rows and cases for route fixes, but the documented corpus still reports misses and says resolver results do not prove the live model follows the route. Product Owner should use whole-word/context-sensitive signals, explicit output intent, regression rows, mutants, and live smoke as separate evidence. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-103] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:78-80] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:104-123] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/scratch/verification/review-parent.md:98] [INFERENCE: keep fixture and live-model evidence separate]

Moneybird’s reusable design is its packet split: root hub chooses a workflow/tool packet, each packet owns its route contract, and the checker verifies registry/router consistency and required tool packet roles. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30-38] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:4-27] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:903-952]

### Media Editor Claude Code plugin

Reuse the Claude Code plugin shape, bin shim, packaging checks, and source-to-shipped-skill equality check. The plugin uses a plugin folder with manifest, bin, server, and skill; its build replaces generated skill content, checks copied files, and refuses certain package mismatches. The plugin is expressly Claude Code-only because the bin-based plugin is not installed by claude.ai or Cowork. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9-15] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:70-83] [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:354-418] [SOURCE: AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:418-439]

Avoid copying its whole runtime without a need: Media Editor bundles a platform-specific server, while mcp-figma depends on an already installed CLI and Figma Desktop. The Media Editor delivery record also shows runtime-version behavior matters: a shipped ffmpeg output change made ten tools appear unavailable, and its dated summary says 39 tools while a current packaging test expects 40. Treat those records as a reminder to validate the actual package and executable rather than reuse a stale count. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:31-38] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:59] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:150-153] [SOURCE: AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:423-432] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-18] [INFERENCE: preflight the actual Figma CLI rather than assuming a bundled runtime model]

## 17. References

Primary local sources consulted:

- [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-18,42-54]
- [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-148]
- [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145-191]
- [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-32]
- [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:260-295]
- [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:4,42-111]
- [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-186]
- [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2-11]
- [SOURCE: AI Systems/Product Owner/SYNC.md:8-15]
- [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-84]
- [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:43-83,143-145]
- [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:10-55]
- [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:4-27]
- [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:2-12]
- [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:201,903-952]
- [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-103]
- [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:78-123]
- [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/scratch/verification/review-parent.md:98]
- [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9-83]
- [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:354-418]
- [SOURCE: AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:418-439]
- [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:59,150-153]
- [SOURCE: specs/z-staging-po-017-research/spec.md:48-51,101-104]
- [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-config.json:3-8,99-102]
- [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-strategy.md:62-89]
- [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/findings-registry.json:795-818]
- [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:6-10,55-56]

## Convergence Report

- Stop reason: maxIterationsReached.
- Total iterations: 8.
- Questions answered: 5 / 5 tracked key questions.
- Remaining tracked questions: 0; implementation questions remain in Section 12.
- Last three iterations: iteration 6 (newInfoRatio 0.66), iteration 7 (0.70), iteration 8 (0.52).
- Convergence threshold: 0.05; convergence mode was off and did not terminate the loop.
- Divergence summary: no pivots or saturated directions were recorded in the lineage registry; open runtime questions remain.
- The config recorded resource_map_present as false, so the synthesis does not cite a spec-root resource-map placeholder. [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/deep-research-config.json:99-102] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/findings-registry.json:795-818]
- The phase workflow’s parent spec writeback, targeted spec validation, telemetry write, and context generation are outside this lineage boundary; they were not performed. The staging phase itself expects a separate 20-iteration DeepSeek run and fresh Opus synthesis. [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:2210-2233] [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:2240-2245] [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:2347-2363] [SOURCE: specs/z-staging-po-017-research/spec.md:48-51,101-104] [SOURCE: specs/z-staging-po-017-research/research/lineages/luna/iterations/iteration-008.md:55-56]


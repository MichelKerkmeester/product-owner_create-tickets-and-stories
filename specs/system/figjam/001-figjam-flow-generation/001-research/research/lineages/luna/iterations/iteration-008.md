# Iteration 8: Integrated architecture, risks, and build sequence

## Focus
Integrate the capability, input, diagram, embedding, plugin, and hub findings into one risk-ordered implementation plan, and answer the remaining precedent question.

## Actions Taken
- Re-read the local steering path before the iteration; no steer.md was present.
- Compared the Product Owner FigJam specification and active router with the Figma CLI/MCP and diagram contracts.
- Reconciled the Media Editor plugin packaging rules with Moneybird’s hub registry, route checks, and recorded route-review defects.
- This was static source review; no live Figma MCP discovery, CLI help session, plugin build, or FigJam board mutation was performed.

## Findings
1. Recommended architecture: keep Product Owner as the workflow owner for source classification, flow semantics, and FigJam-only delivery, while routing explicitly requested board reads and writes to an embedded mcp-figma tool packet; this matches Moneybird’s default-workflow/non-default-tool split and avoids making a low-level CLI own the product workflow. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:73] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:82] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:5] [INFERENCE: Product Owner should remain the default workflow packet and mcp-figma should be a tool packet]
2. For Figma links, parse fileKey/nodeId and request scoped design data or referenced images only after live MCP tool/schema discovery; the manual lists the MCP as file/node retrieval and image download, while FigJam creation uses the CLI’s fj write verbs. The manuals document screenshot-url for website captures into Figma but do not establish arbitrary local screenshot OCR/import, so treat screenshot extraction as an unresolved adapter spike. Product docs should preserve claim-level current/approved/proposal/retired/unknown status and stop composition when authority does not resolve a conflict. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:129] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:143] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:168] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:181] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:184] [INFERENCE: screenshot OCR/import is not proven by the consulted MCP and CLI references]
3. Carry over flow semantics—distinct node types, top-down direction, decisions with at most three exits, labeled branches, and restrained density—but implement the geometry with FigJam-native objects: preserve orthogonal routing and readable, non-overlapping, unobscured connectors while translating SVG-specific masks, pixel gaps, bridges, and grid enforcement into verified FigJam equivalents. The parent spec forbids HTML/SVG output, so validators and export contracts for those formats do not carry over. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:25] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:260] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:264] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:291] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:295] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:82] [INFERENCE: FigJam-native geometry must be measured in a prototype before any SVG spacing thresholds are reused]
4. Vendor the mcp-figma subtree as a clearly owned copy plus a narrow Product Owner FigJam adapter; keep the shared .skilled source authoritative and sync accepted improvements through an explicit diff/patch review before re-vendoring, since Product Owner’s parity note governs only its hand-written Claude Project mirrors and keeps no manifest, lock, or checksum ledger. Product Owner’s current manifest is a standalone single-mode manifest, so the vendor package should not be mistaken for a hub registry. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:67] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:83] [SOURCE: AI Systems/Product Owner/SYNC.md:8] [SOURCE: AI Systems/Product Owner/SYNC.md:10] [SOURCE: AI Systems/Product Owner/SYNC.md:15] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:11] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:2] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [INFERENCE: a reviewed one-way patch and re-vendor cycle reduces silent divergence across the two repositories]
5. Build a thin Claude Code plugin around the installed figma-ds-cli rather than bundling Media Editor’s custom server; expose preflight/version/help, safe FigJam reads, explicit-target gated writes, and board read-back. Convert Product Owner to a Moneybird-style hub with its current workflow as the sole default workflow packet and mcp-figma as a non-default tool packet, then pin routes for explicit FigJam output intent, ordinary Figma UI feedback, negation, quoted tool names, and mixed inputs. Moneybird’s prefix-match, raw-negation, and corpus/live-model gaps show why gold-route replay, mutation guards, and live smoke must be separate gates. Sequence feasibility first, then vendor/sync, hub/router, flow engine, plugin, and integrated checks; Figma auth/rate limits, drifting @latest schemas, secrets, and output gating remain risks. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:15] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:181] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:5] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:13] [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:4] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:903] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:944] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:109] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:122] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:79] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:143] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/001-research/spec.md:145] [INFERENCE: the proposed phase sequence and verification gates are risk-based recommendations]

## Questions Answered
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?

## Questions Remaining
- Whether the current installed figma-ds-cli build exposes the documented FigJam arguments and can safely create/read back a representative board; this run did not perform a live CLI or board check. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:165] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95]

## Next Focus
The research cap is reached. Downstream implementation should begin with a live, isolated FigJam feasibility spike and keep its board, CLI, plugin, and route evidence distinct from this static review.

## Sources Consulted
- AI Systems/Product Owner/sk-product-owner/SKILL.md:44, 73, 97
- AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-84
- AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141-160, 168-186
- AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2-11
- AI Systems/Product Owner/SYNC.md:8-15
- .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-18
- .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95-148
- .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:145-184
- .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-32
- .skilled/skills/sk-design/sk-design-diagram/SKILL.md:260-295
- AI Systems/Media Editor/runtime/claude-plugin/README.md:9-83
- AI Systems/Moneybird Accountant/SKILL.md:30-38
- AI Systems/Moneybird Accountant/mode-registry.json:5-27
- AI Systems/Moneybird Accountant/hub-router.json:2-12
- AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-105
- AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:78-123

## Assessment
newInfoRatio: 0.52. This pass primarily integrated earlier evidence; the new contribution is the gated phase order and combined architecture risk review. Static-source confidence is high for the documented contracts and low for live FigJam command behavior because no runtime probe was performed.

## Reflection
What worked: combining source-level authority and route contracts exposed where the workflow packet must own input policy and where a tool packet can safely take over board operations. What remains unverified: exact live CLI arguments, screenshot extraction, and board read-back behavior.

## Recommended Next Focus
Begin with the live feasibility gate, then vendor/sync, hub conversion, flow engine, plugin packaging, and integrated route and board checks.

## Workflow Conflicts
- The phase spec describes a 20-iteration DeepSeek run and a fresh Opus 5.5 synthesis, while this detached Luna lineage is configured for eight iterations with lineage-local artifacts. This run follows the dispatched Luna scope; it does not claim to satisfy the separate multi-lineage or Opus synthesis requirements. [SOURCE: specs/z-staging-po-017-research/spec.md:48-51] [SOURCE: specs/z-staging-po-017-research/spec.md:101-104]


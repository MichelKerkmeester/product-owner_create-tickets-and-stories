# Iteration 2: Input-specific paths to a FigJam-only flow

## Focus
Define an evidence-preserving intake path for screenshots, Figma flows, and product documents, while keeping FigJam as the sole user-facing output.

## Actions Taken
- Compared the Figma MCP's documented read surface with Product Owner Doc Mode's source authority and classification rules.
- The reducer marked the five init questions as legacy-import questions and advised using the inbox path {spec_folder}/research/inbox.jsonl; that path falls outside the bound lineage, so no inbox file was written. The strategy template says direct edits are a compatibility path and records them as legacy imports. [SOURCE: .skilled/skills/system-deep-loop/deep-research/assets/deep-research-strategy.md:35] [SOURCE: .skilled/skills/system-deep-loop/deep-research/assets/deep-research-strategy.md:44]

## Findings
1. Input handling should branch by source type before flow synthesis: local Figma MCP provides Figma file/node context, while Product Owner Doc Mode supplies source classification and authority rules for written product material. Treating all three inputs as the same MCP payload would cross two documented boundaries. [INFERENCE: based on .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:32 and AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141]
2. For a Figma flow, accept a Figma URL, extract its fileKey and optional nodeId, discover the live tool schema, then read the smallest relevant node scope and referenced images. The local manual says tools and schemas can change under @latest and recommends node-scoped reads when the schema permits because responses can be token-heavy. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:129] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:146]
3. The local MCP manual documents file/node retrieval and downloading Figma-referenced images, but no direct screenshot-upload or OCR tool. The separate screenshot-url CLI command captures a URL or recreates a webpage into Figma, so it does not establish a supported path for arbitrary attached screenshots. Use screenshots as visual source evidence and keep unobserved transitions marked unknown until supported. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:250] [INFERENCE: based on .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112 and AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:149]
4. For product docs, classify each material claim as current behavior, approved direction, proposal, retired, or unknown; keep status markers with the claim, and stop silent reconciliation when no scoped source authority resolves a conflict. This provides the source-to-transition evidence rules for a FigJam flow derived from written requirements. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:168] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:181]
5. FigJam-only output needs a dedicated flow route or explicit mode boundary: current Product Owner Doc Mode promises one Markdown artifact and a Markdown export path, while the parent spec excludes HTML/SVG and requires FigJam as the only output. Keep any normalization model internal and place source/status notes in FigJam text or stickies so the board remains the sole deliverable. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:64] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:82] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [INFERENCE: based on those sources]

## Questions Answered
- How should Product Owner ingest screenshots, Figma flows, and product documentation into a FigJam-only output?

## Questions Remaining
- Which sk-design-diagram flowchart rules transfer to FigJam, and what must be adapted?
- How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories?
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?

## Next Focus
Translate diagram quality constraints into FigJam-native shapes, connectors, lane structures, labels, and verification steps.

## Sources Consulted
- .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:32-43, 93-114, 124-148
- .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:237-250, 348-358
- .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-152
- AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:64-68, 139-188, 200-244
- AI Systems/Product Owner/sk-product-owner/SKILL.md:195-216
- AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-83

## SCOPE VIOLATIONS
- scope_violation: The documented question-inbox path resolves from the phase spec folder to research/inbox.jsonl outside the bound lineage. No out-of-lineage inbox was created; the current reducer registry retains the imported questions. [SOURCE: .skilled/skills/system-deep-loop/deep-research/assets/deep-research-strategy.md:35]

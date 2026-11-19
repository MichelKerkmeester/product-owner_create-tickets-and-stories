# Iteration 1: FigJam write surface and its hard runtime limits

## Focus

Enumerate what the Figma MCP path and the `figma-ds-cli` path can actually do inside FigJam, and separate the two: which verbs write, which read, which are gated, and which cannot run at all without a live Figma Desktop session. This opens the first key question because every later design of the Product Owner pipeline depends on the real write surface, not the assumed one.

## Findings

1. FigJam authoring exists only in the CLI surface, as the `fj` command group: `fj list|info|nodes` is read-only, `fj sticky|shape|text|connect|move|update` is mutating, `fj delete <nodeId> [-p]` is destructive, and `fj eval <code> [-p]` is arbitrary execution. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348]
2. The Figma MCP direction available in this repo is read-only design context: the registered `figma` manual is the third-party Framelink `figma-developer-mcp` over stdio, which wraps the Figma REST API and "does not drive Figma Desktop", so it cannot create or edit FigJam nodes. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:35] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:68]
3. The skill's premise is CLI-primary with an optional MCP: `figma-ds-cli` is the canonical binary, and a full read of the CLI repo found no MCP server inside it; an "MCP for Figma" is always a separate external server. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:360]
4. Every FigJam write is classed MUTATING and therefore needs confirmation plus an explicit target plus a one-line rollback before it runs; destructive `fj delete` and arbitrary `fj eval` are omitted from the normal path entirely. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:51] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:184]
5. FigJam writes cannot run headless: the CLI drives the live Figma Desktop app over a local daemon on `127.0.0.1:3456`, needs the app open with a file, needs Node 18+, and treats macOS as the supported baseline with Linux and Windows experimental. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/README.md:26] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/README.md:99]
6. The documented command surface drifts from the source, so a FigJam verb and its flags must be verified with `<bin> <command> --help` before being written into a Product Owner procedure; the skill records documented-but-unregistered commands and primitive-name drift as confirmed gaps. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:17] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:372]

## Ruled Out

- Treating "Figma MCP" as the FigJam writer. The MCP is a read surface for design context, so a Product Owner flow that claims "the MCP builds the FigJam board" is describing a capability the wired server does not have.
- Assuming a headless server-side render step. There is no API-key path for authoring; closure of Desktop or a missing daemon stops the work.

## Dead Ends

- Searching the mcp-figma skill for an official Figma Dev Mode MCP path. The reference explicitly places it out of scope for this skill, so it is not a fallback the Product Owner may rely on today.

## Edge Cases

- Ambiguous input: the topic says "through the Figma MCP", while the repo's write path is the CLI. Selected interpretation: research the whole transport pair (CLI plus optional MCP) and state which one each claim belongs to; deferred alternative was to answer only about the MCP, which cannot answer the FigJam question at all.
- Contradictory evidence: none; the CLI reference and the tool surface agree that `fj` writes exist and that the MCP is read-only.
- Missing dependencies: `figma-ds-cli` was not installed or executed in this environment, so all verb flags remain documentation-grade, not live-verified. Fallback: cited the skill's own guidance to verify with `--help`.
- Partial success: none; six findings gathered from four files.

## Sources Consulted

- `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:17,51,149-152,184,190-191,222,235`
- `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348,360,372`
- `.skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:17,32-40,68`
- `.skilled/skills/mcp-tooling/mcp-figma/README.md:16,26,78,99,109`

## Assessment

- New information ratio: 1.0
- Questions addressed: Figma MCP/FigJam capability and limits.
- Questions answered: none fully; the first key question is partially answered and needs the connector and node-level limits.

## Reflection

- What worked and why: reading the gating taxonomy before the feature catalogs gave the write/read split in one pass, because the skill classifies every verb exactly once.
- What did not work and why: the topic's "Figma MCP" framing nearly steered the iteration into describing an authoring MCP; the repo's own routing line corrected it.
- What I would do differently: pull the exact `fj` sub-verbs and their flags from the CLI reference earlier, so the iteration could state argument-level detail rather than group-level detail.

## Recommended Next Focus

Iteration 2: open the connector question. Determine whether `fj connect` builds directional arrows with labels, how many connectors and nodes a FigJam board can hold, and which of those limits are documented in this repo versus unstated, so a flow model can be planned against a real budget.

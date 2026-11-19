# Iteration 8: How a Product Owner skill package is built

## Focus

Open the embedding question from the package side: what files define a Product Owner skill, which of them are generated, and what a second skill would have to add so it routes and passes the existing gates. This deepens the earlier Product Owner findings with package mechanics rather than scope statements.

## Findings

1. A Product Owner skill is a self-contained leaf package with a fixed part list: `SKILL.md`, `graph-metadata.json`, `leaf-manifest.json`, `leaf-manifest.config.json`, `leaf-aliases.json`, plus `references/`, `assets/`, `changelog/`, `manual-testing-playbook/` and `README.md`. [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2]
2. The manifest is generated, not hand-maintained: the config names `generate-leaf-manifest.cjs` as the producer and says `leaf-aliases.json` is the derived identity projection, regenerated together through `ci-skill-root-metadata.cjs --fix`. An embedded skill therefore needs the generator in its loop or its manifests rot. [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:11]
3. `graph-metadata.json` declares skill identity and inter-skill edges: `skill_id`, `family`, `category`, `depends_on`, `enhances`, `siblings`, `conflicts_with` and `prerequisite_for`, plus domains and intent signals. A new skill must declare where it sits relative to `sk-product-owner` and the MCP transport, not just exist on disk. [SOURCE: AI Systems/Product Owner/sk-product-owner/graph-metadata.json:3] [SOURCE: AI Systems/Product Owner/sk-product-owner/graph-metadata.json:9]
4. Product Owner is its own git repository nested inside the workspace, which is the concrete form of the "two git repos" in the topic; the skill package lives in the nested repo while the shared skill lives in the workspace repo. [SOURCE: AI Systems/Product Owner/.git]
5. The current package is explicitly a standalone single-mode skill with no `mode-registry.json`, so a parent-hub conversion is a structural change to how skills are declared, not a configuration toggle. [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:9]
6. Adding a second skill touches four surfaces at once: a new skill directory, the bootstrap routing line in `AGENTS.md` that today names only `sk-product-owner`, the generated manifests, and the Project-side documentation; a package-only copy would not route. [SOURCE: AI Systems/Product Owner/AGENTS.md:7] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:9]

## Ruled Out

- Treating the embedded skill as a folder copy. Three of its files are generated projections, so a plain copy drifts from its own schema on the first edit.
- Encoding the diagram capability as a route inside `sk-product-owner`. The manifest config declares one workflow mode, and the router contract maps commands to artifact lanes, not to a second capability.

## Dead Ends

- Looking for a `mode-registry.json` in the Product Owner package. It is absent by design.

## Edge Cases

- Ambiguous input: "embedding a duplicate" could mean vendoring the whole mcp-figma skill or writing a PO-native skill that calls it. Selected the package-mechanics view and left the vendoring decision to the sync iteration.
- Contradictory evidence: none.
- Missing dependencies: the generator scripts were not located in the PO repo during this iteration, so their presence there is unverified.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2,9,11`
- `AI Systems/Product Owner/sk-product-owner/graph-metadata.json:3,9`
- `AI Systems/Product Owner/sk-product-owner/leaf-aliases.json:1-8`
- `AI Systems/Product Owner/AGENTS.md:7`
- `AI Systems/Product Owner/.git` (nested repository)

## Assessment

- New information ratio: 1.0
- Questions addressed: what a Product Owner skill package contains and what embedding requires.
- Questions answered: none fully; the embedding question now has its mechanics but not its duplication policy.

## Reflection

- What worked and why: reading the manifest config before the manifest exposed the generator contract, which a file listing alone would have hidden.
- What did not work and why: a first attempt to treat `leaf-manifest.json` as authored led to a wrong assumption about hand-editing.
- What I would do differently: locate the generator scripts in the nested repo in the same pass, since their absence would make the embedding plan unworkable.

## Recommended Next Focus

Iteration 9: read the Media Editor Claude Code plugin as the packaging precedent: plugin manifest, marketplace entry, bundled skill, server layout and install path, so the Product Owner plugin form can copy what already works rather than invent a layout.

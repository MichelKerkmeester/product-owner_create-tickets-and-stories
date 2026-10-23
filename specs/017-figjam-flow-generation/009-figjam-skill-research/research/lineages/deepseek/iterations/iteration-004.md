# Iteration 4: `mkaralevich__pi-figma-labor` — staged write, per-mutation undo, structural verification

## Focus

The fourth route: Labor's native-node tools. This iteration targets the write lifecycle rather than the model — how a board is built safely, verified structurally, and rolled back — and tests Flow Mode's all-at-once write against it.

## Actions Taken

1. Read `mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md` (139 lines).
2. Mapped its workflow, placement, connector, font, verification and limit sections against Flow Mode's hosted and `fj` routes.
3. Cross-checked its screenshot fallbacks against iteration 2 and 3 read-back findings.

## Findings

1. The write is staged: create **one** native pattern first, verify it with `get_screenshot`, `get_figjam` and a Labor read, then batch the remaining nodes, and finish with a screenshot of the created or changed root node [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:15] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:18]. Flow Mode's write is one shot — every diagram is sent per call and the board is read only after the whole write [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:114]. A one-node canary would catch a schema or colour failure before the remaining nodes are spent.

2. A wrong mutation is undone immediately with `labor_undo`, not repaired in place [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:139]. Flow Mode's `fj` rollback is page duplication before the first write, then Undo in the session or restore from version history [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:127]. Per-mutation undo is finer-grained and does not depend on a pre-write snapshot being taken.

3. Verification has a structural checklist beyond visuals: text is present, connector endpoints are correct, table dimensions and cell indexes are correct, section visibility is correct, and no temporary nodes remain [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:127] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:133]. Flow Mode's read-back covers node count, connector count, labels and decision-exit labels only [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65]; endpoint correctness is not in it, which iteration 3 finding 6 also flagged.

4. Read-back has documented fallbacks: if `get_screenshot` is unavailable, use the image from `get_figjam` or `labor_zoom_to_node` for manual inspection [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:125]. Flow Mode's read-back assumes a screenshot exists and has no degraded path when it does not [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65].

5. Temporary test nodes are an explicit lifecycle concept: they are created for the canary and must be removed before completion [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:19] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:133]. Flow Mode has no scratch-node concept, so any probe shape it writes stays on the board and inflates the read-back counts.

6. Placement starts by scanning nearby top-level nodes before choosing coordinates, creating sections before their content, passing `parentId` when content belongs in a section, and avoiding reparenting finished nodes unless local coordinates are recalculated [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:36] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:39]. Flow Mode's `fj` route computes every position but has no "scan before placing" rule [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:123]; this is the same collision risk iteration 2 raised with sections.

7. Connector defaults are typed: `ELBOWED` for structure, straight connectors use `CENTER` or `NONE` magnets, elbowed and curved connectors usually use `AUTO`, and endpoints must be re-read after every reassignment [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:61] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:79]. Flow Mode's `fj connect` takes no label and no documented magnet or line-type policy [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:124]; on the hosted route the generator owns these choices.

8. Font ownership is explicit: dedicated text tools load required fonts, `labor_run_script` must load fonts before changing embedded text, new connector labels need a valid fallback font, and code blocks require Source Code Pro Medium [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:110] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:113]. This corroborates iteration 3 finding 9 with a second independent repo and adds a code-block-specific font requirement.

9. The capability limits are stated as product constraints, not style advice: components, variants, variables and design libraries are Design-only; widgets, stamps, highlights and embeds may be inspectable without being creatable [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:137] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:138]. Flow Mode's four-shape rule happens to stay inside the creatable set, but the skill does not state the boundary, so an operator asking for a widget or component would hit an undocumented wall [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97].

10. The route confirms the file-kind pre-flight requirement from iteration 3: confirm `figma.editorType === "figjam"` when it is unclear [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:13]. Two independent repos now require the guard, which makes it a corpus-level norm rather than one skill's habit.

## Ruled Out

- Adopting Labor's `labor_*` tool surface into Flow Mode: Flow Mode's Desktop fallback is `figma-ds-cli fj`, and adding a third vendor CLI would double the connection and daemon surface without adding a capability.
- Treating `labor_undo` as directly callable from Flow Mode: the principle transfers, the verb does not.

## Dead Ends

- Looking for a Mermaid parser or pre-write model check in this repo: the skill is node-level and has none.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: none; the skill's staged write is compatible with, not contrary to, Flow Mode's one-shot generator.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- None in full. Q2 now has four routes recorded; two repos remain (rocket-path, FMCP) plus two Mermaid-side repos.

## Questions Remaining

- Q1, Q2, Q4, Q5 remain open.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`

## Assessment

- New information ratio: 0.90 (9 new, 2 partial — the editorType guard and font rule corroborate iterations 2 and 3)
- Questions addressed: Q2 (fourth route), Q1 (verification depth)
- Questions answered: none

## Reflection

- What worked and why: reading for lifecycle rather than rules produced the canary-write and scratch-node findings, which no earlier source had.
- What did not work and why: nothing failed.
- What I would do differently: earlier iterations should have separated lifecycle from rule content; this is the first iteration that did.

## Recommended Next Focus

Iteration 5: `amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams` plus its `references/examples.md` — a fifth route and the first source that may carry worked diagram examples to test the density and label rules.

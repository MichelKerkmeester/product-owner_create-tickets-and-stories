# Iteration 11: the candidate improvement table, tested against the actual Flow Mode files

## Focus

Convert ten iterations of corpus evidence into a ranked candidate list and verify each target against the real Flow Mode surfaces, including the two Claude Project mirrors and the Flow Mode Delivery kernel. Deepens iterations 2, 4, 7, 8 and 10 by naming the file each change lands in.

## Actions Taken

1. Read the two Claude Project knowledge mirrors and the Flow Mode Delivery section of the kernel.
2. Diffed both mirrors against their authoritative skill sources to separate intentional adaptation from drift.
3. Built a 13-row candidate table, each row naming the Flow Mode target file and the corpus source.
4. Checked the page rule's blast radius across all three surfaces.

## Findings

1. **Emoji rule** — add an emoji error to `sk-product-owner/scripts/flow_check.py` (the `MARKUP_MARKS` tuple at line 44 and `diagram_problems`), sourced from the official universal constraint and ompug's line-level emoji error [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:151]. It is the cheapest fix in the set and closes a tool-level rejection.

2. **Reserved-ID rule** — add `end`, `subgraph`, `graph` plus the Mermaid keyword list to `flow_check.py`, sourced from the official constraint and ompug's `FIGMA_RESERVED`/`FLOW_KEYWORDS` sets [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:52] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37]. rocket-path's state-diagram warning confirms the hazard is not flowchart-specific [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:79].

3. **Underscore-ID rule** — make an underscore in a node ID an error and non-camelCase a warning in `flow_check.py`, sourced from the official routing warning and ompug's error severity [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:53] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:526]. This is the only one of the four known gaps with an unambiguous corpus consensus.

4. **Page rule and rollback** — replace the new-page target and clear-the-page rollback in `sk-product-owner/references/flow-mode.md` (lines 115 and 117), the knowledge mirror (lines 93 and 95) and the kernel (line 249) with "read the target section before writing, delete only the nodes the write created", sourced from the official `createPage` warning, ompug's section id and scoped deletion, and Mermaid Jam's section containment [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:674] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:30]. This is the only change that touches three surfaces, and skipping the mirrors leaves the defect live in the Project.

5. **Uncertain-call reconciliation** — add a rule to `flow-mode.md`'s hosted route: record intent before the call and read the board back before any retry, because a failed call is indistinguishable from a landed one, sourced from ompug's `pending_action` protocol [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:5] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117]. Flow Mode's current retry rule assumes the first write either landed or did not, which is exactly the assumption the driver was built to avoid.

6. **`fileKey` reuse** — add a reuse rule to `flow-mode.md`: pass the existing board's `fileKey` when iterating, and delete the old diagram's nodes first if replacing, sourced from the official post-generation guidance [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:109] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110]. Flow Mode currently says nothing about a second diagram, so every iteration creates a new draft [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:63].

7. **Connector-direction verification** — extend the read-back in `flow-mode.md` to compare each connector's start and end against the model, not only its count and label, sourced from `parse-figjam`'s cap-based direction logic and southleft's connection-graph query [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:221]. A permuted connector currently passes Flow Mode's read-back.

8. **Missing-label list** — change the `Read-back:` line in `flow-mode.md` and `flow-templates.md` to name the labels that are absent or extra, not only the counts, sourced from ompug's `label_ratio` missing list and IamTheLime's "name what differs" discipline [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:1191] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:12]. Counts alone cannot tell an operator what to fix.

9. **Accent family, not hex** — change the accent rule in `flow_check.py` and the wording in `flow-mode.md` from one distinct hex to one accent family with an allowed note/warning role, sourced from the official semantic-colour guidance and IamTheLime's MAIN/note/warning palette [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:267] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:26]. This resolves iteration 10's verdict into a rule change.

10. **Label-length cap** — add a hard label cap to `flow_check.py`, sourced from ompug's 80-character cap and Mermaid Jam's 120-character cap [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:25] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:138]. Flow Mode's one-line rule bounds line breaks but not length, and the board stretches long labels.

11. **Subgraph policy** — add an explicit subgraph rule to `flow-mode.md` and `flow_check.py`: reject subgraphs, or allow them at one level with quoted IDs, sourced from the corpus conflict between the official two-level support, rocket-path's recommendation and Mermaid Jam's outright rejection [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:157] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:152] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23]. Silence is the only indefensible position.

12. **Route hygiene on `fj`** — add the file-kind pre-flight, the font-loading rule with the Inter Medium default, and immediate undo after a wrong mutation to `flow-mode.md`'s `fj` section, sourced from southleft's `editorType` guard, FMCP's font default and Labor's `labor_undo` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:24] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:59] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:139]. These are three cheap failure modes Flow Mode currently leaves to the vendored packet.

13. **Pre-load and containment** — add the "load the diagram skill before every `generate_diagram` call" rule and the "one section per diagram, one legend per board" convention to `flow-mode.md`, sourced from the official mandatory-load statement, ompug's per-action skill map and its `DC ·` section prefix [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:8] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:29] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:26]. It makes a multi-diagram board navigable and puts the generator's own rules in scope at call time.

## Ruled Out

- Adding a REST read-back implementation to Flow Mode: it needs a Figma token and a REST dependency, so it stays a recommendation rather than a change.
- Adding the `fj` route to the Claude Project mirror: the mirror correctly states that the Desktop route is unavailable in a Project [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:99].
- Changing the 9-node or 3-exit caps: iteration 10 found both defensible.

## Dead Ends

- Looking for a fourth Flow Mode surface: the skill, its asset, the two mirrors and the kernel are the full set; no further file repeats the page rule.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: the mirror and the source intentionally differ on the check method (script versus rule-by-rule) and on the route (hosted only versus hosted plus `fj`); treated as designed adaptation, not drift [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:40].
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- All five key questions were already answered; this iteration answers the follow-on question of where each change lands.

## Questions Remaining

- None. Iterations 12–20 will stress-test the ranking, deepen individual rows, and widen where new evidence appears.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Templates.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- the corpus files cited in each row

## Assessment

- New information ratio: 0.58 (3 new — the three-surface page blast radius, the mirror's intentional adaptations, the full target map; 10 partial synthesis rows)
- Questions addressed: follow-on targeting
- Questions answered: none new

## Reflection

- What worked and why: diffing the mirrors against the skill separated real drift from designed adaptation, which prevents a wrong "fix the mirror to match" recommendation.
- What did not work and why: nothing failed, but the row count is larger than one iteration can rank well; ordering belongs in synthesis.
- What I would do differently: read the mirrors before iteration 10 so the limit verdicts could account for kernel constraints.

## Recommended Next Focus

Iteration 12: stress-test the two weakest rows — accent family (row 9) and subgraph policy (row 11) — against additional corpus evidence, and check whether `flow_check.py`'s self-test style supports the new rules without new dependencies.

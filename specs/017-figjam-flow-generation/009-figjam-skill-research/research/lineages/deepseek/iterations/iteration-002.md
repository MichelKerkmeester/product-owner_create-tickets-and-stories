# Iteration 2: `IamTheLime__dotfiles` — `figjam-diagrams`, the projector-readable board

## Focus

Read the strongest community board-design skill in the corpus (230-line SKILL plus `references/api-notes.md` and `references/themes.md`) and test it against iteration 1's official contract. Builds on iteration 1 (official hosted contract) and answers Q3 on pages, file creation and rollback.

## Actions Taken

1. Read `IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md` (230 lines).
2. Read `references/api-notes.md` (127 lines) and `references/themes.md` (105 lines).
3. Compared the palette, structure, shape, verification and recovery rules with `flow_check.py` and `flow-mode.md`.
4. Tested the page claim against iteration 1's `figma-use-figjam` finding.

## Findings

1. The skill's stated verification is visual and mandatory: "Verify with `get_screenshot` before declaring anything finished", because "overlaps are invisible until you look" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:12]. Flow Mode's read-back does require a screenshot check for stretched or overlapping connectors [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65], so the rule agrees; what IamTheLime adds is a named tool and a pre-declaration gate rather than a step in a prose list.

2. `figma.createPage()` does not exist in FigJam, **but boards can have several pages**: `figma.root.children` lists them and `figma.setCurrentPageAsync(page)` switches [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:18] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:20]. This refines iteration 1 finding 4: the impossibility is page **creation**, not page existence. Flow Mode's new-page rule is unachievable from a plugin, but a pre-existing empty page could be selected through the page API; the honest fix is to drop page creation and keep "read the target before writing".

3. Structure replaces pages: "Nothing lives loose on the canvas" and "`page.children` should contain exactly one section" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:122] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:129]. This is a directly adoptable replacement for Flow Mode's page-based rollback: one board section per diagram gives a deletable, addressable unit that is not a page [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117].

4. The palette rule is "one MAIN colour carries all emphasis; everything else stays quiet", and explicitly forbids a second accent family [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:19] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:23]. It nevertheless keeps note (`#c2e5ff`) and warning (`#ff6655`) roles alongside `MAIN` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:26]. Flow Mode's checker counts **distinct hex values** and permits one, so this palette would fail Flow Mode even though it obeys "one accent" [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:51]. The rule to adopt is "one accent family", not "one hex".

5. Text belongs in text nodes, never in a shape's built-in text, because shape text "cannot be styled per run, it centres by default, its wrapping is not yours to control" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:79] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:81]. This is only actionable on the `fj`/`use_figma` route; `generate_diagram` owns its node text. It is a `fj`-route quality rule Flow Mode lacks [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:123].

6. Shape vocabulary is deliberately smaller and sharper than Flow Mode's four: `SQUARE` (never `ROUNDED_RECTANGLE`), `DIAMOND` for a decision, dashed border for commentary or a superseded state, and borderless for ordinary boxes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:152] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:156] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:159]. It has no stadium and no merge-dot circle, so adopting it wholesale would delete two of Flow Mode's four shapes [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97]. The transferable part is the **information-bearing border** (bright = standout, dashed = commentary), not the shape list.

7. Deleting a node silently deletes its connectors, so after any removal the skill requires re-listing connectors and confirming every decision still has all its branches [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:188]. This is the missing caution on the official fileKey-replacement recipe from iteration 1 finding 6, which says to delete the old diagram's nodes before regenerating without warning that the delete cascades [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110].

8. Connector labels sit at the line midpoint with no offset control, and "long connector labels collide with boxes"; the skill's fix is a few words on the connector and detail in a box [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:117] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:81]. Flow Mode's one-plain-line label rule gives the generator as the reason [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:101]; IamTheLime gives the geometric reason, which survives a route switch.

9. The density numbers are spatial and route-dependent: 20–24px box padding, 30px between boxes in a row, 120–160px between bands, 60px section padding, and one fixed flow-box size reused throughout [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:106] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:110]. Flow Mode has no spacing guidance at all because the hosted generator owns layout [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:103]; these numbers are only adoptable on the `fj` route, where Flow Mode computes every position.

10. Read-back needs a bounded inspection strategy: `get_figjam` on a whole page can exceed the response limit and fail to parse, so query a node or return a filtered summary; `get_metadata` is design-file only; `get_screenshot` needs a real `nodeId` and section ids are the useful ones [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:9] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:14]. Flow Mode's read-back does not name an inspection tool or a bounded query [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65], so this is a concrete adoptable recipe.

11. Branches can be distinguished without colour by `connectorEndStrokeCap` (`ARROW_LINES`, `ARROW_EQUILATERAL`, `TRIANGLE_FILLED`, `DIAMOND_FILLED`, `CIRCLE_FILLED`, `NONE`), which survives greyscale and colour blindness [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:78] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:166]. Flow Mode's one-accent rule creates the same risk; this is a route-compatible alternative on `fj`, and a reader-accessibility argument the hosted route cannot express.

12. Tables are their own primitive: `figma.createTable()` for genuinely tabular content, not a grid of shapes, and tables have no strokes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:192] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:89]. Flow Mode has no comparison-table pattern, and its four-shape rule would force a shape grid if a flow comparison were requested [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:39].

## Ruled Out

- Adopting IamTheLime's shape list `SQUARE`/`DIAMOND`/dashed as Flow Mode's vocabulary: it removes stadium start/end and the merge-dot circle, both load-bearing in Flow Mode's patterns, without replacing their semantics.
- Adopting the 120–160px band spacing into the hosted route: the generator owns layout, so the number has no lever there.

## Dead Ends

- Searching for a `read-back` or verification helper inside this skill: verification is prose and screenshots, with no script. Recorded so later iterations do not re-scan for one.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: the skill says one MAIN colour while its palette carries note and warning hues; resolved as "one accent family" and recorded in finding 4.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- Q3: FigJam page creation is impossible (`createPage` missing) but boards may hold several pre-existing pages selectable via `figma.setCurrentPageAsync`; sections are the creation-free unit. `generate_diagram` creates its own file and reuses `fileKey`; rollback therefore means deleting generated nodes, not clearing a page. Flow Mode's new-page rule should be rejected and replaced by "read the target section/page before writing; delete generated nodes to roll back".

## Questions Remaining

- Q1 (per-skill checks), Q2 (write routes), Q4 (identifier hazards), Q5 (limits) remain open.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`

## Assessment

- New information ratio: 0.96 (11 new, 1 partial — the page finding refines iteration 1 rather than replacing it; (11 + 0.5) / 12 = 0.958, rounded to 0.96)
- Questions addressed: Q3 (answered), Q5 (deepened), Q2 (partial)
- Questions answered: Q3

## Reflection

- What worked and why: reading the API notes alongside the design skill produced the mechanically useful half — the palette stays a design opinion, the API notes become an implementable checklist.
- What did not work and why: no script exists in this repo, so it cannot answer Q1's "machine-enforced" half.
- What I would do differently: for repos with no executable check, record the absence once (done here) and spend later calls on the rule text instead.

## Recommended Next Focus

Iteration 3: `southleft__figma-console-mcp-skills/skills/figjam-create-content` plus its `figjam-snippets.md`, the third distinct write route (console bridge). Compare its route and verification with the hosted route from iteration 1 and the plugin route from iteration 2.

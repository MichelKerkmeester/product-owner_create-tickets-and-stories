# Iteration 10: five-limit verdicts, widened by `parse-figjam` (found with `gh search`)

## Focus

Two jobs in one iteration. First, judge Flow Mode's five deliberate limits against the accumulated evidence from iterations 1–9. Second, widen the corpus with a new repo not in the pinned eight: `rrichardsonv/parse-figjam`, found with `gh search repos "figjam diagram"`, read through the GitHub API because it is not pinned locally. Builds on iterations 1, 2, 5, 6, 7, 8, 9.

## Actions Taken

1. Searched `gh search repos "figjam diagram"` and selected `rrichardsonv/parse-figjam` (the only new result with a real skill surface).
2. Read `SKILL.md` via `gh api repos/rrichardsonv/parse-figjam/contents/SKILL.md` (no local write).
3. Re-read the official shape table to test Flow Mode's four-shape set.
4. Weighed each of the five limits against every earlier finding.

## Findings

1. Widened corpus: `parse-figjam` is a read-back-only skill that extracts semantic context from FigJam board JSON produced by the Figma REST API, with no write route at all [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:8]. It fills the one role every pinned source treats as secondary — reading a board as data rather than as a picture.

2. The read is deliberately semantic: it extracts `name`, `characters`, `type` and `children`, and ignores fifteen layout and appearance fields including `absoluteBoundingBox`, `size`, `cornerRadius`, `shapeType` and `effects` [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:31] [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:62]. Flow Mode's read-back compares counts and labels from a screenshot; a REST semantic read is cheaper, deterministic and searchable, and would make the "missing label" list iteration 9 asked for trivial to produce [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65].

3. Connector direction is derived from the caps, not from the model's order: one arrow means directed, both arrows bidirectional, none undirected [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50]. Flow Mode's read-back counts connectors and labels but never checks whether an arrow points the way the model said [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65]. This is a confirmed verification gap.

4. A dashed line is a distinct relationship type, not styling: `strokeDashes` present means dashed, absent means solid, and the relationship is reported with its line style [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:48] [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:102]. Flow Mode has no dashed/solid semantic and its one-accent rule cannot express one [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:47].

5. Colour meaning is not assumed: if a section named `legend` exists its contents map colours to meanings, and without one and with significant variation the skill asks the user [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:57] [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:58]. Flow Mode's single accent is self-explanatory (happy path), but there is no legend convention on multi-diagram boards, which iteration 9 also flagged [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:102].

6. Unknown content is surfaced, never skipped: a missing endpoint becomes `"external reference to [nodeId]"`, an unknown node type is included with its raw type name, and an empty section is noted rather than omitted [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:144] [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:145]. Flow Mode's read-back has no unknown-item category, so an unexpected node is neither reported nor counted.

7. The full JSON tree is never reproduced in output [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:146], corroborating iterations 2, 3, 6 and 7 on bounded reads and returning only what the comparison needs.

8. Limit verdict — **TD only: keep as house style, reject as a rule**. No corpus source mandates top-to-bottom. The official default is LR; rocket-path uses LR with TD only for decision trees; ompug's linter accepts five directions; Mermaid Jam accepts five [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:211]. The rule should become "TD is the default for user flows; a linear hand-off may use LR", and `flow_check.py` should accept both.

9. Limit verdict — **9 nodes: keep, with a naming obligation**. The official soft cap is ~20, ompug's is ~25, FMCP times out at 7–12 nodes per call, and rocket-path's densest worked example is exactly 9 [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:329] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:31] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:22]. Nine is defensible for board reading and matches the only practitioner example at that size. What is missing is ompug's rule that anything omitted in a split is named, never dropped silently [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:32].

10. Limit verdict — **3 exits per decision: keep unchanged**. The official guidance treats 2–3 level decision trees as the normal case, rocket-path's decision trees use three labelled exits, and no source allows a fourth without splitting [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:92]. Flow Mode's rule is the corpus's clearest enforceable contribution.

11. Limit verdict — **one accent colour: change the unit from hex to accent family**. The official guidance allows multiple semantic colours for status, ownership and subsystem; IamTheLime keeps one accent plus note and warning roles; FMCP keeps a per-lane semantic palette [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:267] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:26]. Counting distinct hexes rejects a disciplined palette; counting accent families preserves the intent.

12. Limit verdict — **four shapes: keep, and cite the vendor table as justification**. The official table lists rectangle, stadium, circle (rendered as an ellipse) and diamond as distinct rendered shapes, so all four Flow Mode shapes are vendor-validated, while most other Mermaid shapes fall back to rectangles [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:35] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:41]. rocket-path's "full range" claim is the counterexample that proves the limit's value [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:52].

13. The new source also exposes a round-trip Flow Mode lacks: it can emit Mermaid from a board as one of six output choices [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:112]. Flow Mode only goes model → board, so revising an existing board from its model is impossible without retyping the model.

## Ruled Out

- Pinning `parse-figjam` into the local corpus: it was read through the GitHub API, and adding files would write outside this lineage.
- Adopting a REST read-back as Flow Mode's primary verification: the hosted MCP route already returns a board link, and a REST token is a new dependency; it is a recommended complement, not a replacement.

## Dead Ends

- Broader `gh search` queries ("figjam skill", "figma diagram skill") returned no additional skill repos; only `parse-figjam` had substance. Recorded so later iterations do not repeat the searches.

## Edge Cases

- Ambiguous input: `parse-figjam` was not in the pinned corpus; treated as a widened source and cited by URL.
- Contradictory evidence: its semantic read versus Flow Mode's screenshot read; resolved as complementary, not conflicting.
- Missing dependencies: none.
- Partial success: the search yielded one usable repo, not several.

## Questions Answered

- Q5: all five limits now have a verdict with corpus evidence. Two survive unchanged (3 exits, 4 shapes), one survives with an added obligation (9 nodes), one changes unit (one accent family, not one hex), and one is rejected as a rule (TD only).

## Questions Remaining

- None of the five key questions remains open. Iterations 11–20 will deepen improvement candidates, test the synthesis ranking, and widen where new sources or files appear.

## Sources Consulted

- `https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`

## Assessment

- New information ratio: 0.77 (7 new from the widened source, 6 partial/synthesis verdicts; (7 + 3) / 13 = 0.769)
- Questions addressed: Q5 (answered), Q2 (round-trip gap)
- Questions answered: Q5

## Reflection

- What worked and why: combining synthesis with a genuinely new source kept the iteration from being a restatement; the read-back-only repo produced the direction and legend checks the write-oriented corpus lacked.
- What did not work and why: three of four `gh search` queries returned nothing usable, so widening cost more calls than expected.
- What I would do differently: search with one broad term and filter by description rather than trying narrow phrases.

## Recommended Next Focus

Iteration 11: test the candidate improvements against the actual Flow Mode files, starting with the four that touch `flow_check.py` (emoji, reserved IDs, underscores, accent family) and the two that touch `flow-mode.md` (page rule, uncertain-call reconciliation). Build a first ranked improvement table for synthesis.

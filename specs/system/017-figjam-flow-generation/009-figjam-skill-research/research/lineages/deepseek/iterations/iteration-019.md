# Iteration 19: attacking the top rows

## Focus

Play sceptic against ranks 1, 2 and 3–5 and against the containment row. Four attacks landed: the emoji range was too narrow, the ID case rule was wrong, the section rule collides with the never-move rule, and `fileKey` reuse is more important than the table ranked it. Deepens iterations 14, 18 and 15.

## Findings

1. **Emoji range corrected.** The proposed `\u2600-\u27BF` range misses pictographs above it and includes nothing above the BMP; ompug's published regex covers `1F000–1FAFF`, `1FC00–1FFFD`, `☀–➿`, `⌀–⏿` and `⬀–⯿` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:173]. Adopt that range verbatim rather than inventing a narrower one; a checkmark `✓` sits inside `☀–➿` and is rejected, which matches the sanitizer this corpus already runs [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:310].

2. **Reserved-ID case handling corrected to case-insensitive.** ompug lowercases the ID before comparing it against both sets [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:520]. Iteration 14's exact-match advice is withdrawn: the cost is rejecting `End`, an ID no Flow Mode diagram needs, and the benefit is matching the only linter in the corpus.

3. **Attack on the edge rule: thick edges are stylistic, not semantic.** `==>` changes stroke weight, not direction, so a thick edge does not break the flow's meaning. It should still be rejected, but for a different reason: Flow Mode already has one emphasis channel, colour, and a second one makes two ways to say "important" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:102]. The error message should say that, or the rule reads as arbitrary.

4. **Attack on the edge rule: dashed and undirected edges have legitimate uses elsewhere.** A dashed edge often means "later" or "optional", and an undirected edge means a plain association; both are meaningful in other diagram types. In Flow Mode they are not needed because a label carries "later" and a loop back with `-->` carries repetition [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:48]. The rule stands, with a named alternative in the message so a user is not left without a way to express the intent.

5. **Attack on the section rule: it collides with "the generator owns the layout".** `generate_diagram` without a `fileKey` creates a new file in drafts, and adding to an existing file places the diagram beside the old one; section placement is a separate `use_figma` step that reparents nodes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110]. Reparenting is a move, and Flow Mode forbids moving generated nodes. The two rules cannot both stand unqualified.

6. **Resolution: scope the never-move rule, do not drop containment.** Allow exactly one post-write move — reparenting the diagram into a named section without changing its relative geometry — and keep the ban on rearranging nodes or rewiring connectors. Ompug's placement script exists for this purpose and handles parent/local coordinates [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:103]. On a route with no section step, the diagram lives in its own file and containment is satisfied by the file.

7. **The page rule's replacement gets simpler, not harder.** There is no page to name: the target is a file (new, or existing by `fileKey`) and optionally a section. The gate's effect becomes "a new file, or N nodes added to an existing file"; the rollback becomes "delete the created nodes or section". That removes the impossible page choice entirely instead of substituting another page-shaped rule [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:109].

8. **`fileKey` reuse is under-ranked at 10.** Without it, every regeneration creates a draft file; the official guidance counts four regenerations as four files to clean up [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102]. Reuse is also the mechanism that makes revision possible at all, so it moves to rank 3, ahead of the three ID rules, and the page-rule row merges into it.

9. **Deleting the old diagram before regenerating is the official replacement recipe.** It is the rollback path, not a page clear: delete the previous diagram's nodes via `use_figma`, then regenerate with the same `fileKey` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110]. Flow Mode's recovery section should adopt that sentence instead of "re-run into a cleared page".

10. **Section idempotency is by name, which the read-back can use.** Ompug's placement reuses a section already tagged with the same diagram and recognises its sections by name [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:12]. Flow Mode's `Read-back:` line can name the section and count only its children, which is the v2 format from iteration 16.

11. **The edge rule survives all four attacks.** No corpus source uses an undirected or dashed edge in a flowchart that Flow Mode targets, and the named alternatives cover the intents. Its rank stays 1.

12. **The table's top five are now: edge rule, section/file rule, `fileKey` reuse, emoji, reserved IDs.** Underscore moves to six. The shift is not cosmetic: it puts the two write-route fixes above three mechanical checks, because the write-route failures lose work while the checks only lose a call [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117].

## Ruled Out

- **Narrow emoji range**: contradicted by the corpus sanitizer.
- **Exact-match reserved IDs**: contradicted by the corpus linter.
- **Dropping containment to preserve never-move**: loses the rollback boundary.
- **Keeping `fileKey` at rank 10**: contradicted by the draft-file count.

## Dead Ends

- Looking for a generator flag that targets a section directly: the official skill exposes `fileKey` and a separate `use_figma` step, not a section parameter. Recorded so the plan does not assume one.

## Edge Cases

- Ambiguous input: whether reparenting into a section changes coordinates. Ompug's script computes parent/local coordinates, so the plan should verify visually after the one allowed move.
- Contradictory evidence: the never-move rule versus containment; resolved by scoping the rule.
- Missing dependencies: a `use_figma`-capable connector for the section step; without it, file-per-diagram is the fallback.
- Partial success: a section step that runs but places the diagram outside the section; read-back by section id catches it.

## Questions Answered

- Follow-on: do the top rows survive a sceptical read? Three do, with message and scope fixes; one moves up.
- Follow-on: how do page, section and never-move coexist? File target, optional section via one allowed organizational move, no page language.

## Questions Remaining

- None. Iteration 20 consolidates the decisions and prepares the synthesis.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md`

## Assessment

- New information ratio: 0.68 (four new facts — emoji ranges, case-insensitivity, section/never-move conflict, draft-file count — plus a rank change)
- Questions addressed: sceptical review of the top rows
- Questions answered: both above

## Reflection

- What worked and why: attacking the section rule found a direct contradiction with an existing Flow Mode rule, which no amount of corpus reading would have surfaced without the cross-check.
- What did not work and why: the first emoji regex was invented rather than copied from the corpus sanitizer, and it was both too narrow and too wide in different ranges.
- What I would do differently: for every proposed regex, copy the corpus's published pattern first and only narrow it with a measured reason.

## Recommended Next Focus

Iteration 20: consolidate the final decisions, restate the corrected top five, and prepare the synthesis structure — ranked changes, targets, sources, proof, human steps.

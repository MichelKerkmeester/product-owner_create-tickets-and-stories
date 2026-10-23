# Iteration 18: the ranked table

## Focus

Rank every surviving candidate by impact, effort and risk, with its target files, corpus source and proof. This is the ranking the synthesis will publish. Deepens iterations 11–17 and settles the two rows iteration 12 reversed.

## Method

- **Impact**: 5 means a silent wrong board or a tool rejection today; 1 means polish.
- **Effort**: 5 means three surfaces and a parity pass; 1 means a constant and a condition.
- **Risk**: 5 means destructive or hard to reverse; 1 means additive and self-tested.
- Ties break toward the change with the stronger corpus consensus.
- Two earlier candidates are excluded: accent family (withdrawn, iteration 12) and subgraph support (rejected, iteration 12).

## The table

| Rank | Change | Target | Corpus source | Impact | Effort | Risk | Proof |
|---|---|---|---|---|---|---|---|
| 1 | Reject undirected, bidirectional, dashed and thick edges | `flow_check.py` | parse-figjam cap logic; southleft graph query | 5 | 1 | 2 | self-test planted `---` and `-.->` |
| 2 | Replace the new-page rule with a named section, in all eight statements | `flow-mode.md`, mirror, kernel | official `createPage`; ompug scoped delete; Jam containment | 5 | 4 | 5 | paragraph count 8/8, parity read |
| 3 | Emoji error | `flow_check.py` | official SKILL:49; ompug lint:151 | 4 | 1 | 1 | self-test planted emoji |
| 4 | Reserved-ID error | `flow_check.py` | official SKILL:52; ompug lint:37 | 4 | 1 | 1 | self-test planted `end` |
| 5 | Underscore-ID error | `flow_check.py` | official SKILL:53; ompug lint:526 | 4 | 1 | 1 | self-test planted underscore |
| 6 | Read-back v2: section scope, endpoint direction, missing/extra names | `flow-mode.md`, `flow-templates.md`, mirror | parse-figjam direction; ompug missing list | 4 | 3 | 2 | worked passing and failing lines |
| 7 | Raw-text markup scan (dead `<`, `>`, `**` marks) | `flow_check.py` | extractor `clean_label` probe | 3 | 2 | 1 | self-test planted HTML tag |
| 8 | 80-character label cap | `flow_check.py` | ompug build:25; Jam reviser:138 | 3 | 1 | 1 | self-test planted 81 chars |
| 9 | Uncertain-call reconciliation before retry | `flow-mode.md`, mirror | ompug pending-action | 3 | 2 | 2 | a failed-call scenario read-through |
| 10 | `fileKey` reuse for revisions | `flow-mode.md`, mirror | official SKILL:109 | 3 | 2 | 2 | rule read against Section 5 |
| 11 | One section per diagram, one legend per board | `flow-mode.md`, mirror | ompug `DC ·` prefix; IamTheLime legend | 3 | 2 | 2 | a multi-diagram scenario |
| 12 | Reject subgraphs explicitly | `flow-mode.md`, `flow_check.py` | official subgraph recipe; Jam rejection | 2 | 1 | 1 | self-test planted subgraph |

## Findings

1. **Rank 1 is the edge-operator rule, not the page rule.** The page rule is destructive when it fires, but it needs a shared board and a human who ignores the gate; an undirected or reversed connector happens on every diagram where someone writes `---` by habit, and nothing today catches it [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77]. Impact 5, effort 1.

2. **Rank 2 is the page rule because the failure is unrecoverable.** A cleared shared page loses work no read-back can restore, and the vendor API cannot create the replacement page the rule assumes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13]. Its effort (four surfaces) and risk (5) are the highest in the table.

3. **Ranks 3–5 are one batch of three one-line rules.** Emoji, reserved IDs and underscores share a shape, a proof and a failure mode: the generator rejects or mangles the model. Their corpus consensus is the strongest in the set, and each is one constant plus one condition [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37].

4. **Rank 6 is the read-back v2 because it turns the board from "looks done" into "proven done".** Endpoint matching is the only check that catches a swapped branch, and the missing/extra lists are the only output an operator can act on [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50].

5. **Rank 7 exists because a rule that cannot fire is worse than no rule.** The markup check claims five marks and enforces one; fixing it is a regex on raw text and a planted tag [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:242]. It ranks below the read-back because the generator silently sanitises rather than rejects.

6. **Rank 8 is the label cap, deliberately low-risk.** An 81-character label is a readability problem, not a failure, so it belongs after the rules that break boards [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:25].

7. **Ranks 9–10 are write-safety rules without a mechanical proof.** Uncertain-call reconciliation and `fileKey` reuse change behaviour on the second write and the second revision, and neither can be self-tested; they are verified by reading the route against a scenario [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:5].

8. **Rank 11 is containment, which is also the rollback boundary.** It ranks below `fileKey` because it depends on the page rule landing first; a section convention on a page-clearing rule is incoherent [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:26].

9. **Rank 12 is the subgraph rejection: a documented decision, not a defect fix.** It ranks last because the current behaviour (silently passing a subgraph) is rarer than the others and the fix is one regex plus one bullet [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23].

10. **Two rows from iteration 11 do not survive.** Accent family is withdrawn for lack of a palette; subgraph support is rejected for coherence. Both are recorded as decisions so a future reader does not re-open them as gaps [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:45].

11. **Two cheap rows sit outside the top twelve.** The pre-load rule and the `fj` hygiene trio (editorType, Inter Medium, undo) are real but route-specific; they belong in the same batch as ranks 9–11 rather than in the headline list [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:8] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:24].

12. **The ranking is stable under a different weighting.** Raising effort's weight moves the page rule down but not out of the top three; raising risk's weight moves it to first. No reasonable weighting drops the edge rule or the three ID rules from the top five [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:523].

## Ruled Out

- **Ranking by corpus frequency**: the page rule appears in more sources than the edge rule but fires less often.
- **Combining the three ID rules into one row**: the synthesis needs distinct target changes, and each has its own planted model.
- **Including withdrawn rows to reach a count**: the table has twelve real changes without them.

## Edge Cases

- Ambiguous input: impact scores are judgements; the method states the scale so a reader can re-weight.
- Contradictory evidence: none.
- Missing dependencies: ranks 2, 6, 9 and 10 depend on the mirror batch; noted in the table's effort column.
- Partial success: none.

## Questions Answered

- Follow-on: what is the final order, and why? The table above.
- Follow-on: which earlier candidates are gone? Accent family and subgraph support.

## Questions Remaining

- None. Iterations 19–20 test the table's weakest assumptions and prepare the synthesis.

## Sources Consulted

- the corpus and Flow Mode files cited in each row

## Assessment

- New information ratio: 0.35 (ranking and weighting only; no new external evidence)
- Questions addressed: final order
- Questions answered: above

## Reflection

- What worked and why: writing the impact scale before scoring kept the page rule from winning on drama alone; the edge rule fires more often and costs less to fix.
- What did not work and why: the first ordering put read-back v2 at rank 3, until the missing/extra lists were recognised as an output change that needs the format work in rank 6.
- What I would do differently: score impact and frequency separately from the start; they are not the same axis.

## Recommended Next Focus

Iteration 19: attack the top three rows as a sceptic would — find the case where the edge rule rejects a legitimate model, where the section rule breaks on a board with no sections, and where the ID rules reject a valid diagram.

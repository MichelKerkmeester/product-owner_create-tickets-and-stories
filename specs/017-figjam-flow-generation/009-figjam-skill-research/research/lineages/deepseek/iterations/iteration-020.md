# Iteration 20: consolidation

## Focus

Close the research with the final decisions, the corrected ranking, and the exact work the synthesis must publish. No new external evidence; this iteration consolidates iterations 1–19. Deepens iterations 18 and 19.

## Final decisions

### The five limits

| Limit | Decision | Basis |
|---|---|---|
| TD only | Keep as the default house style; stop treating it as a generator rule | Four corpus sources accept or prefer LR; no source mandates TD |
| 9 nodes | Keep, and name anything omitted when splitting | Official soft cap ~20; ompug ~25; FMCP timeout band 7–12; densest practitioner example is 9 |
| 3 decision exits | Keep unchanged | Official decision trees and rocket-path examples both use three |
| One accent colour | Keep one hex; do not adopt "accent family" | No palette exists, so a family check would be arbitrary; one hex is exact and self-testable |
| Four shapes | Keep, and cite the vendor table | Rectangle, stadium, ellipse-circle and diamond all render distinctly; most other shapes fall back |

### Rejected directions

- **Subgraph support**: rejected. It needs tinted fills, per-subgraph direction and node-to-node edges, each colliding with an existing Flow Mode rule.
- **Accent families**: withdrawn for lack of a defined palette.
- **Post-write restyling**: rejected except for one organizational move into a section, which preserves relative geometry.
- **REST read-back as the primary check**: rejected as a new dependency; structural read remains preferred where the route offers one.

### The ranked changes

| Rank | Change | Primary target | Corpus source | Proof |
|---|---|---|---|---|
| 1 | Reject undirected, bidirectional, dashed and thick edges; name the label or loop-back alternative | `flow_check.py` | parse-figjam; southleft | self-test planted `---`, `<-->`, `-.->`, `==>` |
| 2 | Replace page language with file and optional section across eight statements | `flow-mode.md`, mirror, kernel | official `createPage`; ompug; Jam | 8/8 paragraph count; parity read |
| 3 | Reuse `fileKey`; delete old diagram nodes before regenerating | `flow-mode.md`, mirror | official generate-diagram | recovery scenario read |
| 4 | Emoji error using the corpus ranges | `flow_check.py` | ompug sanitizer | self-test planted emoji |
| 5 | Reserved-ID error, case-insensitive | `flow_check.py` | official; ompug lint | self-test planted `end` |
| 6 | Underscore-ID error | `flow_check.py` | official; ompug lint | self-test planted underscore |
| 7 | Read-back v2: section scope, endpoint direction, missing/extra names | `flow-mode.md`, asset, mirror | parse-figjam; ompug | worked passing and failing lines |
| 8 | Raw-text markup scan for HTML tags and emphasis | `flow_check.py` | extractor probe | self-test planted `<b>` |
| 9 | 80-character label cap after cleaning | `flow_check.py` | ompug; Jam | self-test planted 81 chars |
| 10 | Uncertain-call reconciliation before retry | `flow-mode.md`, mirror | ompug pending-action | failed-call scenario |
| 11 | One section per diagram, legend when colour carries meaning | `flow-mode.md`, mirror | ompug; IamTheLime | multi-diagram scenario |
| 12 | Reject subgraphs explicitly | `flow-mode.md`, `flow_check.py` | official; Jam | self-test planted subgraph |
| 13 | Route hygiene and pre-load rule | `flow-mode.md`, `fj` section | official; southleft; FMCP; Labor | route read-through |

## Findings

1. **The final set is thirteen changes, twelve ranked and one route-specific batch.** The ranking changed twice under scrutiny: `fileKey` rose from ten to three, and the page rule fell from two to a file-level rule inside rank 2 [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:115]. The synthesis should publish the final order, not iteration 11's first draft.

2. **The checker work is one batch of six rules.** Edge operators, emoji, reserved IDs, underscores, raw-text markup and label length all live in `flow_check.py`, all are one constant plus one condition, and all are proven by `--self-test` with a planted model each [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:40]. The synthesis should present them as one reviewable change with six planted cases.

3. **The write-route work is a second batch across three surfaces.** Page, `fileKey`, uncertain-call, containment and the never-move scope touch `flow-mode.md`, the mirror and one kernel line; their proof is a paragraph count plus the parity read after a commit [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249].

4. **The read-back work is a third batch.** Section scope, endpoint direction, missing/extra lists and the worked failing line touch Section 6, the asset and the mirror prose; the kernel needs no change [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:122].

5. **Every mechanical rule has a planted model; no write-route rule does.** That asymmetry is honest: the checker can prove rejection, while the write rules are verified by reading a scenario and by the board read-back at run time [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:119].

6. **The parity gate cannot certify any batch until the untracked files are committed and the declaration is clean.** Today it exits 2 without checking [SOURCE: AI Systems/z — Claude Project Sync Loop/validate_parity.py:90]. The synthesis must name this as a precondition, not a result.

7. **The kernel review is a human step after the batch lands.** A dated review line names a reviewer and a content key recomputed from the committed kernel; writing it earlier would claim a review that did not happen [SOURCE: AI Systems/Product Owner/SYNC.md:13].

8. **The skill and kernel versions move once, at the end of the batch.** Kernel v1.2.2 to v1.3.0 for the rule change, skill 1.2.1.0 to 1.2.2.0; a single bump per side keeps the release stamp coherent [SOURCE: AI Systems/Product Owner/SYNC.md:17].

9. **The strongest single finding of the research is the page rule.** It is the only Flow Mode instruction that is impossible on the vendor API and destructive on a shared board, and it appears in eight statements across three files plus two recovery sections [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13]. The second strongest is the unchecked edge operator, which silently produces undirected or reversed connectors [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77].

10. **The research changed its own mind four times, and each reversal is recorded.** Accent family withdrawn, exact-match IDs withdrawn, subgraph support rejected, `fileKey` promoted. Keeping the reversals visible is what makes the final list trustworthy [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:45].

11. **No claim in the final list depends on a board that was never written.** Every write-route finding is a rule read against a corpus source; the hosted route's behaviour was not executed here, and the synthesis must say so where it matters [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:111].

12. **The synthesis needs no new file outside the lineage.** Its content is the ranked changes, the five-limit verdicts, the rejected directions, the batch order and the external preconditions; all are already in iterations 1–20 [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:95].

## Ruled Out

- Any further corpus widening: twenty iterations reached saturation; the last three new sources changed details, not the ranking.
- Any change to the 9-node, 3-exit or four-shape rules: each survived the stress test.
- Any claim that the parity gate passes today: it cannot run.

## Dead Ends

- Searching for a generator parameter that targets a section directly: none exists; placement is a separate step.
- Searching for a page-creation workaround in the plugin API: none exists; the restriction is absolute.

## Edge Cases

- Ambiguous input: whether the mirror should adopt the v2 read-back line verbatim; yes, with the script mention dropped.
- Contradictory evidence: the never-move rule versus section placement; resolved by one scoped organizational move.
- Missing dependencies: commit authority, a human reviewer and a clean declaration are external.
- Partial success: the research proves rules, not board behaviour; stated explicitly.

## Questions Answered

- All five key questions are answered, with the limit verdicts in the table above.
- The final ranked list and batch order are settled.

## Questions Remaining

- None within the research scope. Implementation, commit and review are outside it.

## Sources Consulted

- the Flow Mode files and corpus sources cited throughout iterations 1–20

## Assessment

- New information ratio: 0.25 (consolidation only)
- Questions addressed: all
- Questions answered: all

## Reflection

- What worked and why: keeping a running table and attacking its top rows produced a final order that survived four reversals; the reversals are the evidence of rigour, not a weakness.
- What did not work and why: the early iterations trusted corpus patterns as rules before checking the target file; two recommendations had to be withdrawn as a result.
- What I would do differently: read the target implementation before the fifth source, not after the tenth.

## Recommended Next Focus

Synthesis: publish the thirteen changes in final order with targets, sources, proof, batch order and the external preconditions; state the five-limit verdicts and the rejected directions; keep every citation to a corpus or Flow Mode file.

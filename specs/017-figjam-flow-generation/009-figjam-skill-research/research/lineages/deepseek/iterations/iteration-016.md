# Iteration 16: read-back format, direction counting, and the eighth page statement

## Focus

Write the replacement `Read-back:` line and the read-back rules, and correct iteration 15's surface count: the page rule also lives in both error-recovery sections. Deepens iterations 15 and 10.

## Actions Taken

1. Searched all three surfaces for page, cleared-page and empty-page wording; found eight statements, not seven.
2. Read Section 6 and the reply shape in `flow-templates.md`.
3. Drafted the read-back line with section scope and direction counts.
4. Checked that the reply stays three lines.

## Findings

1. **Correction: the page rule is eight statements, not seven.** The missed pair sits in error recovery: "Re-run the write into a cleared page" in the skill and the identical sentence in the mirror [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:127]. Iteration 15's count was wrong, and a fix that skipped these would leave the recovery path instructing a page clear.

2. **The recovery sentence is the most dangerous of the eight.** It authorises a second write into a cleared page after a mismatch, which is exactly the operation the vendor API cannot perform and the one that destroys other work when the page is shared [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159]. Replace it with "remove only the nodes this write created, or write into a new section the user names, then read back again".

3. **Read-back line v2 adds section scope.** Proposed shape: `Read-back: 8 of 8 nodes in section Signup, 8 of 8 connectors directed, 2 of 2 decision exits labelled; missing: none; extra: none` [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:140]. Section scope stops other board content from inflating or deflating the counts, and the trailing lists make the mismatch case concrete rather than prose-only.

4. **Direction must be counted by endpoint match, not by arrowhead presence.** A connector whose arrowhead points backwards still has an arrowhead; the count only means something when each connector's start and end are compared with the model's source and target [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:221]. "8 of 8 connectors directed" should mean eight endpoint pairs matched, not eight arrows seen.

5. **The decision-exit count should verify label and target per exit.** Counting two labelled exits is weaker than checking that `Yes` goes to the success node and `No` to the error node, which the checker already validates on the model [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:68]. The read-back should mirror that check on the board, so a swapped branch fails.

6. **Prefer a structural read over a screenshot when both exist.** A screenshot proves legibility and layout; it cannot prove connector direction, section membership or a missing label. `parse-figjam`'s semantic read and southleft's connection graph are the right primitives [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:8]. The rule should say structural first, screenshot second, not the reverse.

7. **Name the read that produced the line.** If the route offers only a visual read, the line should read `Read-back (visual):` rather than implying endpoint verification. That single token keeps the reply honest without adding a line [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:139].

8. **The reply stays three lines.** The kernel promises the board URL, the `Read-back:` line and the `HVR self-scan:` line, and "nothing else", so detail belongs inside the existing lines, never in a fourth [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]. The v2 line is longer but still one line.

9. **`flow-templates.md` must carry the same shape verbatim.** Its reply block is the pattern a run copies, so a divergence between Section 6 and the asset produces two formats [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:122]. One source of truth, or the next reader picks the wrong one.

10. **The mismatch case needs a worked line, not only a rule.** Example: `Read-back: 7 of 8 nodes in section Signup, 6 of 8 connectors directed, 2 of 2 decision exits labelled; missing: "Confirm email"; extra: "Skip"` [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:142]. It shows an operator exactly what to fix and proves the format can express partial failure.

11. **The kernel needs no format change.** Its line names the `Read-back:` line without prescribing its contents, so the change lands in the skill and the asset only; the mirror's Section 6 prose should follow, because it states the counts too [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:108]. That keeps the kernel stable while the skill's format moves.

12. **A read-back failure should not trigger a retry by default.** The recovery rule currently says re-run after the user agrees; with direction checking, a mismatch is often a model or labeling fault, and a rewrite duplicates the section. The order should be: report, diagnose, then either fix the model or rewrite the section, on agreement [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:157].

13. **The v2 line stays under 160 characters in the passing case.** The proposed passing line is 118 characters; the failing example is 149, so both fit one visual line at normal board-voice width and need no wrapping rule [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:122].

## Ruled Out

- **A fourth reply line for details**: violates the kernel's "and nothing else".
- **Cap-only direction counting**: proves an arrowhead exists, not where it points.
- **Screenshot-only read-back as the default**: cannot establish endpoints or containment.
- **Changing the kernel line**: it does not prescribe the format.

## Dead Ends

- Searching for a fifth page statement in `flow-templates.md`: the asset has none, so the surface set is the skill, the mirror and the kernel, with eight statements total.

## Edge Cases

- Ambiguous input: a board whose section holds unrelated content; resolved by scoping the read to the section and naming any extra items.
- Contradictory evidence: none.
- Missing dependencies: a route with no structural read; handled by the `(visual)` token.
- Partial success: a read that returns nodes but no connectors; the line reports `0 of 8 connectors directed` and names the absence.

## Questions Answered

- Follow-on: what is the exact read-back line, and how does it fail? The v2 shape and the worked mismatch line.
- Follow-on: how many page statements exist? Eight, corrected from seven.

## Questions Remaining

- None for read-back. The remaining iterations rank the full set and test the write-route additions against the parity gate.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md`

## Assessment

- New information ratio: 0.62 (the eighth statement, the endpoint-match definition, the structural-first rule and the `(visual)` token are new; the rest refine iterations 15 and 10)
- Questions addressed: read-back format, page surface count
- Questions answered: both above

## Reflection

- What worked and why: grepping every synonym for page found the recovery statement that iteration 15 missed; the count was only as good as the search terms.
- What did not work and why: iteration 15 searched "new page" and "cleared the page" but not "cleared page", which is why the recovery pair slipped.
- What I would do differently: search each rule by its concept words, not by one remembered phrase.

## Recommended Next Focus

Iteration 17: rank the full improvement set against the parity gate's constraints — which changes can land as one reviewable batch, which touch the kernel, and which need a human review before the drift check can pass.

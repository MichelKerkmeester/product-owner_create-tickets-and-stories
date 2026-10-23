# Iteration 15: write-route replacement text across the skill, the mirror and the kernel

## Focus

Turn the write-route rows into the exact sentences that replace the page rule in all three surfaces, add uncertain-call reconciliation, `fileKey` reuse and section containment, and state the manual parity work each change triggers. Deepens iterations 11 and 12.

## Actions Taken

1. Located every statement of the page rule: three in `flow-mode.md`, three in the mirror, one in the kernel.
2. Drafted replacement text for each, keeping the kernel's version to one line.
3. Read the parity method in `SYNC.md` to state the review and version work the change requires.
4. Checked the `fj` rollback separately, since it is route-specific.

## Findings

1. **The page rule is seven statements across three files, not one.** `flow-mode.md` carries it at the gate, the write bullet and the rollback; the mirror repeats all three; the kernel compresses it into the Flow Mode Delivery line [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:63] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:115] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:41] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:93] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:95] [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]. A fix that edits one surface leaves six live statements of a rule the vendor API forbids.

2. **Gate replacement, skill side.** Replace "The page is a new page or one confirmed empty, never a page that holds other work" with "The target is a plan, file and section named in the message; the section is created if absent, and no existing content is cleared" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:63]. The gate keeps its four disclosures — plan, file, effect, rollback — and loses the impossible page choice.

3. **Write-bullet replacement, skill side.** Replace the new-page bullet with "Write into a named section. Read the section first when it exists: an existing section is extended only by adding the nodes this write creates, and a section holding anything else is left untouched" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:115]. The rollback boundary becomes the section id rather than the page.

4. **Rollback replacement, skill side.** Replace the clear-the-page sentence with "The rollback is to delete the section this write created, or the node and connector ids it recorded when it extended an existing section. Read the target before deleting and stop if it holds anything the write did not create" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117]. This keeps the existing stop condition and removes the assumption that the page is disposable.

5. **Uncertain-call rule, new bullet.** Add "A failed or timed-out call is not a no-op. Read the board before any retry and continue only when the diagram is absent or the same write can be identified; never send the same diagram twice on the assumption that the first call failed" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:113]. This is the ompug pending-action rule expressed as a Flow Mode instruction [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:5].

6. **`fileKey` reuse, new bullet.** Add "When revising a board, pass its existing `fileKey` rather than creating another draft, and remove the previous diagram's section before writing its replacement" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:109]. Today every iteration on a flow risks a new draft because the route never mentions reuse [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:111].

7. **Containment, new bullet.** Add "One diagram per section, named for the diagram. When colour carries meaning across a multi-diagram board, one legend section names it" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:26]. It gives the rollback a boundary, makes read-back scoped, and answers the legend gap from iteration 10.

8. **The kernel line can carry the same rule in one sentence.** Replace "Write one diagram per call into a new or confirmed-empty page" with "Write one diagram per call into a named section, created if absent, never clearing existing content" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]. The kernel keeps its single-line shape and its other clauses, including the explicit-yes gate.

9. **The mirror's gate and write bullets need the same three replacements.** The mirror's Section 5 is not a byte copy — it already drops the `fj` route and the script check — but its page rule is identical to the skill's, so all three statements change in the same way [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:93]. Parity is manual: the mirror is hand-written from the skill, and this is exactly the paragraph that applies inside a Project.

10. **The `fj` rollback stays as it is.** "Duplicate the page before the first write" is a Desktop operation that creates a page through the app, not through a plugin, so the vendor `createPage` restriction does not apply to it [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:127] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13]. It should be reworded only to say "duplicate the file" if a page cannot be duplicated safely, which the corpus does not establish; leave it.

11. **A rule change moves three versions, and two of them are not the skill's.** The skill frontmatter moves a minor version, the kernel H1 moves a minor version because a rule changed, and the dated review note is added only after a named human confirms the review [SOURCE: AI Systems/Product Owner/SYNC.md:17] [SOURCE: AI Systems/Product Owner/SYNC.md:13]. Claiming the review or the version bump without those steps would be a false completion claim.

12. **The drift gate is read-only and comes after the edit.** The parity method's third step compares commit timestamps between each skill file and its mirror; editing the skill without the mirror turns the gate red, and editing the mirror without the skill leaves the next drift check blind [SOURCE: AI Systems/Product Owner/SYNC.md:12]. Both sides must land in one change.

13. **No new Project knowledge file is needed.** The Flow Mode mirror already owns the write routes; the change edits three paragraphs and adds three bullets there, rather than creating a second document the kernel would have to route to [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:85]. Fewer files, one parity pair.

## Ruled Out

- **Editing the kernel only**: leaves the skill and mirror stating the impossible page rule.
- **Rewording the `fj` rollback**: route-specific and still valid.
- **A new knowledge file for write safety**: the existing mirror already owns the section.
- **Claiming the kernel review in the change**: only a named human can confirm it.

## Dead Ends

- Looking for a page-creation workaround: the vendor restriction is absolute for plugins, and every corpus source that writes through a plugin uses sections or existing pages instead. Recorded so no later iteration hunts for one.

## Edge Cases

- Ambiguous input: whether an existing section may be extended. Resolved as additive-only, with a stop if it holds foreign content.
- Contradictory evidence: the `fj` route can duplicate a page while the plugin cannot create one; resolved by keeping the route-specific rollback.
- Missing dependencies: the parity gate and the human review are external steps, named rather than assumed.
- Partial success: none.

## Questions Answered

- Follow-on: what exact text replaces the page rule, and where? Seven statements, three files, with the sentences above.
- Follow-on: what does the change cost in parity work? A skill minor bump, a kernel minor bump, a dated review note after human confirmation, and the drift check.

## Questions Remaining

- Whether the section name should carry a run id, which affects idempotency on retries. Left for the write-safety iteration if evidence appears.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `AI Systems/Product Owner/SYNC.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md`

## Assessment

- New information ratio: 0.55 (the seven-statement count, the parity cost and the section-boundary rollback are new; the rest are replacements for earlier rows)
- Questions addressed: write-route text, parity work
- Questions answered: both above

## Reflection

- What worked and why: counting every statement of the page rule before drafting text prevented a one-file fix that would have left the kernel lying.
- What did not work and why: the first draft changed the `fj` rollback too, until the route distinction showed it was still valid.
- What I would do differently: count surface occurrences for every rule row before writing replacement text, not after.

## Recommended Next Focus

Iteration 16: the read-back row — connector direction, missing-label list, screenshots as fallback — as replacement text for Section 6 and the `flow-templates.md` reply shape, with the exact `Read-back:` line format it produces.

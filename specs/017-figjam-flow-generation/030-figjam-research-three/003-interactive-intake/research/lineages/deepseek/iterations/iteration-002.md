# Iteration 2: How public skills decide they know enough to act

## Focus

Widen from the packet to the corpus, to see how skills outside this repo handle a thin brief before drawing. Read Figma's own `figma-generate-diagram` skill and its sibling `figma-spec`, the `generate-project-plan` workflow skill (the only multi-round board intake in the corpus), Adobe's Spectrum diagram skill, `ompug`'s diagram-plan document and `prasantloki`'s FigJam builder. Builds on iteration 1 finding 5 (Flow Mode asks only in five situations) and finding 6 (the packet's facts exist in prose with no completeness test).

## Actions Taken

1. Read `research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md` and `skills/figma-spec/SKILL.md`.
2. Read `workflow-skills/generate-project-plan/SKILL.md` Steps 1 to 4 and their checkpoints.
3. Read `adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md` and `references/diagram-house-style.md`.
4. Read `ompug__diagram-codebase/docs/DESIGN.md` (diagram plan) and `prasantloki__figjam-builder/SKILL.md` (very large boards).

## Findings

1. **Figma's own diagram skill carries the same one-question doctrine, and the packet quotes it almost verbatim, so the loop has to go past upstream rather than match it.** Figma says to ask one or two focused questions when the description is thin and closes with "One good question beats one wasted diagram" [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:69]. Flow Mode carries the same sentence and the same examples [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144]. The good behaviour to keep is the high-value question; the gap is that neither source asks a second round when the answer is still thin.

2. **Figma's project-plan skill is the corpus's one real multi-round intake, and it models rounds as typed steps.** Every step declares `[Type: Research | Confirm | Write]`, with `Confirm` meaning no board writes and a user decision gate, and `Write` meaning a screenshot plus a question after it [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:227], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:229]. A read-only step ends in a self-check, and the self-check is allowed to fail and loop: "Enough signal to draft candidate section cards in Step 2. If not, loop back and ask" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255].

3. **Its confidence test is a per-section readiness state, not a score.** Each approved section must be either `ready` (no gaps) or carry a specific non-empty gap list [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:298]. The gap list holds "specific facts the user must supply, framed as answerable questions (no 'figure it out yourself' gaps)" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:295]. That is a named-fact model with a binary threshold per fact, which is the shape the brief asks for.

4. **It caps the shape of a round, not the number of rounds: at most four questions per call.** The multi-select fires "per batch of ≤4 candidates (max 4 questions per call, 4 options each → up to 16 candidates per call)" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276]. Nothing in the skill bounds how many rounds it may take, so its intake can loop for as long as gaps remain. This is the exact failure the round cap must prevent.

5. **It proposes rather than only asks, and the proposal carries four fields plus a preview.** Each candidate section card names a title, a one-line description, why it was suggested and a default block shape, and the user ticks the set [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:279]. Content is then proposed with its shape and a short preview, and the answer is Yes, Edit or Skip [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:319]. That is the sparring step the brief asks for, in a working example.

6. **Its answers persist as a named object with explicit skips.** The selected set is stored as `approved_sections` and never re-derived [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:279]. An edited section is re-shown and re-asked, and a skipped section is marked `skipped` and never written [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:320]. Recorded answers, edits and declines are all first-class state, which is what makes later turns build on earlier ones.

7. **A machine-readable board plan already exists as a precedent, with a purpose field and named omissions.** `ompug`'s diagram plan gives every diagram a `purpose` defined as "one sentence: what question this diagram answers" [SOURCE: research/corpus/ompug__diagram-codebase/docs/DESIGN.md:157], a `notes` list for what was left out [SOURCE: research/corpus/ompug__diagram-codebase/docs/DESIGN.md:173] and a `skipped` array carrying `{type, reason}` [SOURCE: research/corpus/ompug__diagram-codebase/docs/DESIGN.md:148]. Oversized diagrams are split, "never truncated silently" [SOURCE: research/corpus/ompug__diagram-codebase/docs/DESIGN.md:193]. The packet's provenance table and `Left out:` line cover the omissions but not the purpose sentence as a written field.

8. **The asking that does exist upstream is scope-bounding, not comprehension-building.** `prasantloki`'s builder asks the user which sections matter for a board over 200 nodes instead of reading it all, because it is "faster and more useful" [SOURCE: research/corpus/prasantloki__figjam-builder/SKILL.md:417]. Figma's own skill asks which variation to keep and remembers the answer for the session [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:112]. Both ask to bound work or to settle a preference, and neither asks what the board must convince its reader of.

9. **The nearest thing to a cap on asking upstream is a cap on regenerating.** Adobe stops after two regenerations on the same complaint and says to "stop, ask what's specifically wrong" [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161]. Figma's skill sets the same two-attempt bound [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:98]. The packet already carries that bound [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:262]. A cap on the repair loop is not a cap on the intake loop, and no corpus source has the second.

10. **One fact is already MUST-ask and never inferred, which is the model for a hard fact.** Figma's Specs skill requires `whoami` before any call, forbids inferring the plan from a file key, and stops the workflow when the plan is unclear [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]. The packet adopted the plan rule at its gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]. A confidence model should borrow this "never infer, always ask" class for the reader and the board's question rather than only for the plan.

## Ruled Out

- **Copying `approved_sections` as a literal mechanism.** It stores a set of board sections; the intake needs a set of facts with a status each. The precedent is the stored answer object, not its schema.
- **Treating the four-questions-per-call limit as the round cap.** It caps one message's width, and the project-plan skill loops without a round bound [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255].

## Dead Ends

- Search for a confidence score or numeric threshold in the corpus. The only numbers are node, edge and attempt budgets; no skill scores its own understanding. Corpus-wide search returned no match.
- Adobe's Spectrum diagram material is a house-style critic, not an intake. It adds no question structure beyond the two-attempt stop [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161].

## Edge Cases

- Ambiguous input: "intake" in the corpus can mean selecting sections (project plan) or bounding source reading (figjam-builder). This pass treats both as intake moves and separates them by what they settle.
- Contradictory evidence: none. Every source agrees that thin input should be asked about, and none has a stop rule.
- Missing dependencies: Figma's `AskUserQuestion` tool is a Claude Code surface; its limits are quoted as a shape, not assumed available in this repo.
- Partial success: the corpus contains no written-intake skill for FigJam diagrammatic content itself, only the project-plan board. That absence is recorded rather than filled by inference.

## Sources Consulted

- `research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md`
- `research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md`
- `research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md`
- `research/corpus/ompug__diagram-codebase/docs/DESIGN.md`
- `research/corpus/prasantloki__figjam-builder/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`

## Assessment

- New information ratio: 0.7
- Questions addressed: key question 2, with corpus evidence.
- Questions answered: none completed yet; the corpus supplies the shape, and the threshold still needs the public elicitation sources.

## Reflection

- What worked and why: reading the corpus's only multi-round skill (project plan) was the highest-yield move, because it shows rounds, batching, proposals, stored answers and skips in one working flow.
- What did not work and why: a broad grep for "clarifying question" across all 22 repos returned mostly the Figma redistributions, which are byte copies and not independent evidence.
- What I would do differently: read `generate-project-plan` in iteration 1 as the contrast case, since it makes the packet's missing loop obvious in one file.

## Recommended Next Focus

Iteration 3: go to the public elicitation and critique sources for the missing half the corpus cannot supply: how many rounds a clarifying intake should take, when to stop, how to ask few high-value questions, and what a design critique asks before judging a visual. Build on finding 1 and finding 3.

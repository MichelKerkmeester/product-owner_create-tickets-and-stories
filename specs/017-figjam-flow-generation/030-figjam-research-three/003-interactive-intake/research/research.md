# Interactive intake research

## 1. Summary

The packet does not need a new interviewer, it needs a definition of done for understanding and a loop that stops. Today the intake is one question then a draft [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:58], and Flow Mode asks only in five situations, none of them confidence-driven [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75]. The loop belongs in `flow-mode.md`, because a Flow route loads only that leaf pair [SOURCE: AI Systems/Product Owner/ROUTER.md:91]. The top three changes are a nine-row Brief with a status per row, a draw-ready threshold with an ordered stop rule and an energy cap, and a dependency-ordered question bank where every question carries a recommended answer.

## 2. What the packets already do well

- The gate asks once and names the plan, file, effect, extensions, read calls and rollback [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]
- The pre-drawing test asks whether a list, table or paragraph serves the reader better [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:89]
- An undrawable request is named plainly and mapped to the nearest drawable type that answers the same question [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:93], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95]
- Never invent, and a thin source is asked about rather than filled [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144]
- The two dials default to Balanced and Mixed and are stated choices [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:150], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:151]
- The type table is already phrased as the reader's question, which is the question bank's backbone [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79]
- The per-type needs table already lists what a gantt needs against what a sequence needs [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:132]
- The remove test and the keep-one accent test are written and sharp [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:37], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:49]
- The budget splits rather than shrinks, and the cut order is fixed [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170]
- Quick skips nothing in Flow Mode, because the check and gate guard a shared plan [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:53]
- Provenance and omission are first-class, one row per drawn item and a named `Left out:` line [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]
- The repair loop is bounded at two attempts on the same diagram [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:262]
- The plan is must-ask and never inferred, which is the model for a hard fact [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]
- The generator owns the layout, so no node is moved or restyled by hand [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164]
- The clarification file holds the question and nothing else, which stops a half-artifact [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97]

## 3. Ranked changes

### Rank 1. Add the nine-row Brief with a status per row to Flow Mode intake

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, a new subsection after Section 4 INTAKE
- **Comes from:** the coverage guarantee, a named dimension set where a blank row is the one forbidden thing [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md], and the per-section readiness state that is `ready` or carries a specific gap list [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:298]
- **The gap:** the packet states its facts once as prose and has no test that says which are still unknown [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:132]. The dials say how much and for whom, not what the board is about [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:146]
- **What changes:** nine rows, being reader, question, outcome, scope, entry, exit, actors, decisions and states, sources and class. Each row carries a value, a source and one status of captured, corrected, assumed or unasked. Reader and question may never be assumed, borrowing the never-infer class the plan already has [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]. `assumed` is only for a fact no supplied source can answer, and it must name what would settle it
- **Effort:** small
- **Mirror or kernel:** `claude project/knowledge/Product Owner - Templates - Flow Mode.md`, written by hand from the skill source [SOURCE: AI Systems/Product Owner/SYNC.md:10]

### Rank 2. Add the draw-ready threshold, the ordered stop rule and the energy cap

- **Changes:** `flow-mode.md` Section 2 workflow and the `$flow` energy line
- **Comes from:** both failure poles being named in practice, since premature convergence causes underspecified features and probing past a convergence signal is an anti-pattern [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. A sibling skill already selects a count of rounds by energy [SOURCE: .skilled/skills/sk-prompt/SKILL.md:343]
- **The gap:** no stop rule exists, and the five asking situations are situational rather than confidence-driven [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75]
- **What changes:** draw when no row is unasked, the reader and question are settled, at most two rows are assumed and each names its settlement. Stop asking on the first of: complete and confirmed, two consecutive rounds that change no row, a user stop, or the energy cap. Quick is zero rounds, Standard three, Deep five. At the cap the packet draws with the assumed rows named or takes the no-route branch and offers a table [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:211]. The cap counts rounds, not questions, which is why a per-call width limit is not it [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276]
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Templates - Flow Mode.md` and one sentence in the kernel [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:254]

### Rank 3. Add the question bank with a recommended answer per question

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md`, a new part after the type reply, pointed at from `flow-mode.md` Section 4
- **Comes from:** every question carrying a recommended answer drawn from the sources [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md], and batched rounds working in public practice [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276]
- **The gap:** the type table is already question-shaped and has never been used as an interview [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79]
- **What changes:** three dependency-ordered rounds. Round one is reader, question and outcome. Round two is entry and exit, plus actors. Round three is decisions and states, plus sources and class. One to three questions per round, never a question a supplied source already answers [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:121]. A vague answer is re-asked with the probe set: a concrete scenario, an edge case, a contradiction, a term, a scale, a failure mode or a boundary [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. A corrected row is recorded as `corrected` and counts as settled
- **Effort:** medium
- **Mirror or kernel:** `claude project/knowledge/Product Owner - Assets - Flow Templates.md`

### Rank 4. Add the sparring step and the outline pass

- **Changes:** `flow-mode.md` workflow steps 2 to 4, and `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md` Section 2
- **Comes from:** the preview-then-ask loop that ends in Yes, Edit or Skip [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:319], a proposal that carries a title, a one-line description, why it was suggested and a shape [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276] and a written purpose field per board [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:157]
- **The gap:** the remove test depends on a `userIntent` sentence the intake never establishes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:38], and that sentence is composed only at the write call [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186]. A review that judges layout before agreeing the message is the same category error [SOURCE: https://design.google/library/reviewing-the-design-review]
- **What changes:** three proposals in cost order. An outline, one line per node and edge with its Brief row, which the remove test can run on. Two named framings with what each buys and costs, with one recommended. A Mermaid sketch in chat, never written to a board. The look is then settled with four proposed choices: the accent by the keep-one test [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:49], the detail level and audience from the captured rows, whether the board needs sections at all [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164], and four critique questions asked about the sketch, opening with where the eye goes first and whether that is the most important node [SOURCE: https://thecrit.co/resources/design-critique-questions]
- **Effort:** medium
- **Mirror or kernel:** `Product Owner - Templates - Flow Mode.md` and `Product Owner - Rules - Flow Quality Rubric.md`

### Rank 5. Add the per-round replay, the single playback and the gate line

- **Changes:** `flow-mode.md` Section 8 and the reply contract in `assets/flow-templates.md`, plus one line in the step 7 gate
- **Comes from:** confirmation being a separate step from coverage, where the understanding is played back and waits before anything is written [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md], and a decisions table closed with a confidence per decision [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]
- **The gap:** the gate's facts are all write-side and none is the board's message or reader [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]
- **What changes:** each round opens with a compact replay of the settled rows. Before the model there is one full playback that waits for one answer. The gate gains the Brief's question and outcome, so the yes covers the purpose and not only the destination. The reply keeps its five lines [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235]
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Templates - Flow Mode.md` and `Product Owner - Assets - Flow Templates.md`

### Rank 6. Add the challenge ladder and the type-first sequencing

- **Changes:** `flow-mode.md` Sections 3 and 5, and `quality-rubric.md` Section 2
- **Comes from:** the negative-space pass, which asks what the work must refuse before it is confirmed [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md], and the fixed cut order the packet already has [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170]
- **The gap:** the ladder starts at the type, so a brief that names no type is never challenged, and filling nine rows for an impossible board wastes the user's time [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95]
- **What changes:** five rungs in cost order. What must this board not do. Would a list, table or paragraph serve better [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:89]. The remove test on the outline. Split rather than shrink, offering an overview board and a detail board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162]. Name every omission in the reply line [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]. The type is challenged before the Brief, because a state diagram's actors are not a sequence's participants
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Rules - Flow Quality Rubric.md` and `Product Owner - Templates - Flow Mode.md`

### Rank 7. Give the Product Owner lane a board block and one named exception

- **Changes:** `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`, a board block in the comprehensive question, and `AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md` core rule 1 with the MUST NOT list
- **Comes from:** the template's artifact-shaped blocks, energy first and assumptions last, with no board fact anywhere [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:55], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:85], and the second-round ban [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:519]
- **The gap:** a FigJam request that reaches the Product Owner lane inherits questions about deliverable type, scope and sources, and the packet's own escalation still says one question [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:65]. This is the half of the brief that Flow Mode's own file cannot reach
- **What changes:** when FLOW is detected, the comprehensive question gains one block naming the reader, the question the board answers and what the reader should decide. Core rule 1 names a board intake as a legal second round, bounded by Rank 2's stop rule, so the ban on a second round keeps its force everywhere else [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:58]
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Assets - Interactive Response Templates.md` and `Product Owner - System - Interactive Mode.md`, plus the kernel's Ask before drafting paragraph [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:9]

### Rank 8. Add the Quick and just-do-it rules for board facts

- **Changes:** `interactive-mode.md` Quick lane and protected facts, and the `$flow` energy line in `flow-mode.md`
- **Comes from:** a non-interactive run that never asks and proceeds on stated assumptions, flagging each one [SOURCE: .skilled/skills/sk-prompt/SKILL.md:340]
- **The gap:** Quick may skip routine intake, and the facts it may never skip are Doc-shaped, so no board fact is protected [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:109]
- **What changes:** Quick fills the nine rows from sources and defaults, then sends one message with the rows, the framing and an offer to draw unless corrected, marking each inferred row `assumed` with what would settle it. Just do it is that path and never Raw, which skips the phase flow [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75]. The check, gate and read-back then run unchanged [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:53]
- **Effort:** small
- **Mirror or kernel:** `Product Owner - System - Interactive Mode.md`, `Product Owner - Templates - Flow Mode.md` and one kernel sentence

### Rank 9. Carry the loop in the kernel and rebuild the two mirrors by hand

- **Changes:** `AI Systems/Product Owner/claude project/Custom Instructions.md` Flow row and Flow Mode Delivery, plus `claude project/knowledge/Product Owner - Templates - Flow Mode.md` and `Product Owner - System - Interactive Mode.md`
- **Comes from:** the kernel already owning both mirrors, Flow Mode for intake and Interactive Mode for the one-question path [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:210]
- **The gap:** the Flow row names sources and output with no intake [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:126], and a Project cannot hold a state machine or write a file, so turn state survives only in the conversation [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234]
- **What changes:** two sentences of policy, being that the Brief runs before the type choice and is replayed once before the gate, and that a Quick request gets one proposed Brief instead of rounds. No per-row table and no round counter in the kernel, because they would drift from the skill
- **Effort:** small
- **Mirror or kernel:** the kernel and both mirrors, written by hand under the manual parity method [SOURCE: AI Systems/Product Owner/SYNC.md:10]

### Rank 10. Name the intake in the packet's ALWAYS list and the ROUTER FLOW row

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/SKILL.md` ALWAYS list and `AI Systems/Product Owner/ROUTER.md` FLOW leaves description
- **Comes from:** the ALWAYS list being where a reader learns the run order [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:168]
- **The gap:** a rule that lives only inside a reference is easy to skip, and the FLOW leaf pair is everything a Flow request loads [SOURCE: AI Systems/Product Owner/ROUTER.md:91]
- **What changes:** one ALWAYS item saying the Brief is filled before a type is chosen, and one ROUTER note saying `flow-mode.md` carries the intake rounds
- **Effort:** small
- **Mirror or kernel:** none, because the router prose is not mirrored into a Knowledge file

### Rank 11. Carve out the test contract and add four scenarios

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md` pass condition, four new scenario files under `boundaries/`, and index rows in `manual-testing-playbook.md`
- **Comes from:** the current fail line, which fails a run that asks more than one question [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:71]
- **The gap:** the loop cannot pass as written, and no scenario covers an under-specified brief
- **What changes:** the pass condition separates one question that settles the artifact from rounds that settle the board. Four scenarios cover a thin brief, an over-broad brief, a wrong type and just do it at Quick energy
- **Effort:** medium
- **Mirror or kernel:** none

## 4. Rejected ideas

- A confidence score out of 100, because practice states completeness and no calibrated number exists [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]
- One question at a time strictly, because a board has nine facts and dependency order resolves the conflict with batched rounds [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276]
- Putting the loop only in `interactive-mode.md`, because a Flow route never loads it [SOURCE: AI Systems/Product Owner/ROUTER.md:37]
- Reusing the clarification export as the record, because the file holds the question and nothing else [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97]
- A sticky or section on the board, because an extension the gate did not name needs its own yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168]
- A new packet or a new Knowledge file, which would double the parity surface for no gain
- A brief rule in `flow_check.py`, because the check reads the model and the Brief precedes it [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170]
- Mapping just do it to Raw, because Raw skips the check and gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75]
- A fifteen-question budget, because it counts questions where the unit is a round
- Copying `approved_sections` as a literal mechanism, because the precedent is a stored answer object rather than its schema [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:279]

## 5. Corrections to the iterations

- Iteration 2 and the lineage draft say Flow Mode carries Figma's "one good question" sentence at `flow-mode.md:144`. Line 144 asks for one or two focused questions and names the same examples, but the sentence itself is only in the corpus [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:69]
- Iterations 1 and 5 cite FJ-020's pass and fail lines at `command-conflict-asks.md:29`. They are at lines 70 and 71, with line 33 carrying the same pair in the scenario header [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:70]
- Iteration 1 cites the comprehensive template at `interactive-response-templates.md:53`, `:59` and `:81`. The energy block is at line 55, the deliverable block at line 59 and Assumptions to challenge at line 85, so the template has seven blocks rather than six [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:55]
- Iteration 4 cites `sk-prompt`'s 10, 3 and 0 ladder at `SKILL.md:341`. It is at line 343 [SOURCE: .skilled/skills/sk-prompt/SKILL.md:343]
- Iterations 1 and 4 cite `sk-product-owner/SKILL.md:305` for the Quick rule. The file is shorter than that and the rule lives at line 198 [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:198]
- The lineage draft cites the no-route branch at `flow-mode.md:209`. It is at line 211 [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:211]
- Iteration 5 says the ranking holds eight changes and then lists nine, and the draft's Section 12 lists nine. The count is eleven here, because the Product Owner lane's own question template and the packet's ALWAYS list were not separately ranked
- Iteration 1 finds the packet quotes Figma "almost verbatim" at line 144. The examples match word for word and the closing sentence does not, which strengthens rather than weakens the finding

## 6. Claims not verified

- Every public URL below was read by the iterations and could not be opened here, so each claim rests on the iteration's quotation of it
- The VisSnacks critique ordering of describe, pinpoint purpose and evaluate is paraphrased by iteration 3 and never quoted, so it is not used as evidence here
- The Gause and Weinberg context-free-question PDF is image-only and was not readable by iteration 3
- Whether users accept a three-round Standard cap, since the number is chosen from `sk-prompt`'s ladder at human scale rather than measured
- Whether the outline catches an over-broad brief before a model exists, since the remove test is written for a model
- Whether a state diagram has a meaningful actors row, as opposed to an owner per transition

## 7. Sources

- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md`
- `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md`
- `AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md`
- `AI Systems/Product Owner/ROUTER.md`
- `AI Systems/Product Owner/SYNC.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `.skilled/skills/sk-prompt/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/003-interactive-intake/research/corpus/ompug__diagram-codebase/docs/DESIGN.md`
- https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md
- https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md
- https://design.google/library/reviewing-the-design-review
- https://thecrit.co/resources/design-critique-questions

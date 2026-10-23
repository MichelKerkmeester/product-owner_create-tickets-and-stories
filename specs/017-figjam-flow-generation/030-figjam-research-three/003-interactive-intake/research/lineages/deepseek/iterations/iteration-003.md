# Iteration 3: What elicitation and critique practice say about confidence, stopping and sparring

## Focus

Widen from the packet and the corpus to public practice. Read requirements-elicitation method (a coverage-guarantee method and a deep-clarification skill), Gause and Weinberg's context-free questions, and two design-critique sources (Google's design review guidance and a critique-question library). The question: what makes an intake confident enough to act, when must it stop, and how does a critique settle what the work should convey before judging how it looks? Builds on iteration 2 finding 3 (per-section readiness) and iteration 1 finding 1 (single-shot intake).

## Actions Taken

1. Searched four angles: context-free elicitation questions, round counts and stopping, design-critique question practice, completeness checklists.
2. Fetched and read a requirements-elicitation method with a coverage contract, a deep-clarification skill, Google's design-review guidance, the Gause–Weinberg context-free-question extract and a critique-question library.
3. Compared each stop rule and factual model against the packet's two dials and the Flow gate.

## Findings

1. **Public practice already has a coverage guarantee: a named dimension set, each row either captured or explicitly assumed.** The method states that "the same set of dimensions must be covered wherever a requirement is elicited" and that a requirement is not finished until every dimension is captured or "explicitly recorded as an unconfirmed assumption"; leaving a dimension blank is the one thing it forbids [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. Its dimension table covers outcome, purpose, boundaries and edge cases, failure behaviour, glossary terms, rationale and out-of-scope [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. The brief's named facts (reader, question, scope, entry and exit, actors, decisions, states, sources) are the board-shaped instance of the same idea.

2. **The stop rule separates "assumed" from "unasked", which is the distinction a confidence model needs.** A row may be marked assumed only where the answer cannot be obtained, and the guess must name what would settle it; "`assumed` is for unobtainable answers, never for unasked questions", and marking something assumed while someone who could answer is present "is not honesty; it is declining to ask" [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. That maps directly onto the FigJam case: a thin brief is an unasked question, not an assumption to fill.

3. **The outcome row is the spine and the one most often missed, and it needs a checkable criterion rather than a workflow.** The method warns that criteria describing steps "read as thorough and verify nothing", and asks for a fit criterion phrased so the answer is yes or no [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. For a board the equivalent sentence is what must be true for its reader afterwards, which is exactly the `userIntent` sentence the write call already carries but the intake never establishes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186].

4. **The negative-space pass adds a question no checklist can generate: what should this guarantee that it does not?** Before confirming, the method asks that inverse question once, reads the description back as a promise and checks both halves, and asks what the capability must refuse, not only what it must do [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. This is the mechanism for challenging an over-broad brief that iteration 5 will need.

5. **Confirmation is a separate step from coverage: the understanding is played back and confirmed before anything is written.** The method's "confirm before acting" step plays back the capability, its boundaries, its failure behaviour and the still-open assumptions, and waits [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. The packet's gate confirms the write, not the understanding; this is the missing playback step, and it is cheap because the model already exists by then [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65].

6. **Rounds and batching are in open conflict across public practice, and the resolution is dependency order.** A deep-clarification skill forbids batching: "one question at a time", wait for the response, and "do not batch questions" [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. Figma's project-plan intake batches up to four multiple-choice questions per call [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276]. The reconciliation is in the deep-clarification skill's own first step: map the decision tree and resolve dependent decisions first [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. Independent facts can share a round; a fact that changes the next question cannot.

7. **Two stopping rules from practice can be adopted almost verbatim: diminishing returns and a hard question budget.** The deep-clarification skill ends when every branch is explored and the user confirms, when the user asks to stop, when three consecutive questions yield no new information, or when the session exceeds 15 questions without convergence and unresolved items are parked [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. Three consecutive no-new-information answers and a total question budget are both testable on a transcript, which the packet's current contract is not.

8. **Evidence-first resolution removes questions that the supplied sources can answer.** The deep-clarification skill checks the codebase before asking and, when it finds the answer, states the finding and asks only whether it is still current [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. Flow Mode already reads the sources, classifies claims and applies Doc Mode's authority order, so a board intake that asks a fact the supplied schema or doc already states would spend a round on nothing [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:121].

9. **Every question carries a recommended answer, which is the small-scale form of sparring.** The deep-clarification skill states each question with "a recommended answer" drawn from the codebase, an ADR or domain knowledge, then waits [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. This is the same move the project-plan card makes at section scale [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:319]. A board intake can propose the reader, the board's question and the detail level rather than ask open questions about them.

10. **A reusable probe set exists for challenging a vague answer: concrete scenario, edge case, contradiction, terminology, scale, failure mode and boundary.** The deep-clarification skill names each with an example, and requires a vague answer to be grilled rather than accepted: "a vague answer is not an answer; it is the next thing to grill" [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md], [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. This is the question bank's raw material for the facts a user answers loosely, such as "show the whole process" or "keep it simple".

11. **A design review starts by agreeing on the problem, and its questions change by stage.** Google's guidance says to "first clearly articulate (and agree!) on the problem you are trying to solve", maps early work to the problem, mid-stage to the solution and late stage to implementation, and warns that pulling later-stage questions forward gets less actionable insight [SOURCE: https://design.google/library/reviewing-the-design-review]. For a board the problem stage is the message and reader, and the solution stage is the model; judging layout before agreeing on the message is the same category error.

12. **Critique practice adds the questions that make "how it should look" discussable without taste assertions.** A critique-question library opens with "where does your eye go first", asks whether that is the most important element, then spacing groupings and whether a squint still shows the primary element [SOURCE: https://thecrit.co/resources/design-critique-questions]. Other critique teaching orders the moves as describe, then pinpoint purpose, then evaluate, and forbids prescribing [SOURCE: https://pages.graphics.cs.wisc.edu/VisSnacks/tutorials/4-critique/]. These are the look questions the packet's rubric applies after the write, and the brief wants them asked before it.

13. **Both failure poles are named in public practice, which fixes what the threshold is for.** Premature convergence is "the root cause of underspecified features", so bounded clarification is not automatically a virtue [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. Its own anti-patterns list the other pole: do not keep probing after the user signals convergence [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. The intake needs both a floor (never draw under-specified) and a ceiling (never interrogate past it), and the brief's threshold is the floor.

## Ruled Out

- **Adopting a fixed 15-question budget as the round cap.** The figure counts questions, and the brief's unit is a round; a round may carry one to three questions, so the budget has to be expressed in rounds and in no-new-information answers [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Copying the seven-dimension checklist wholesale.** Its dimensions are requirement-shaped (glossary, ADR rationale). The board model needs its own nine facts, borrowing the coverage rule rather than the rows [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Treating Google's stage list as a schema.** It describes a review conversation's focus, not the intake's stored state [SOURCE: https://design.google/library/reviewing-the-design-review].

## Dead Ends

- The Gause–Weinberg context-free-question extract returned an image-only PDF of 148 characters, so its examples could not be quoted directly; the secondary descriptions of context-free questions were read from the search index instead and are not used as evidence here.
- A search for a numeric confidence threshold on clarification in requirements engineering returned no authoritative number. Practice states completeness and stop conditions, not a calibrated score.

## Edge Cases

- Ambiguous input: "confidence" in public practice means coverage of named dimensions, not a probability. This pass adopts the coverage reading and treats any number as a presentation of coverage, never as a probability the packet can compute.
- Contradictory evidence: batching is forbidden by one source and required by another (finding 6). Both are cited and the conflict is resolved by dependency order rather than dropped.
- Missing dependencies: the context-free-question primary source was unreadable (see Dead Ends).
- Partial success: the public sources give stop rules, coverage rows and critique questions; none gives a board-specific question bank. That gap is for iteration 4 and the synthesis.

## Sources Consulted

- https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md
- https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md
- https://design.google/library/reviewing-the-design-review
- https://thecrit.co/resources/design-critique-questions
- https://pages.graphics.cs.wisc.edu/VisSnacks/tutorials/4-critique/
- https://assets.ctfassets.net/bncv3c2gt878/4mvcQWNWhWQ0sgiKWCakEU/cce06a8bdc4d3e274ca47eb72d60fbe0/Gause_-_Context-Free_Questions.pdf (unreadable)
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md`

## Assessment

- New information ratio: 0.75
- Questions addressed: key question 2, completed; key question 3 opened.
- Questions answered: "Which named facts must a board intake establish before drawing, and what confidence model, threshold and stop rule make it confident enough to draw?"

## Reflection

- What worked and why: the coverage-guarantee method supplied the two missing concepts in one document — a named-dimension completeness contract and the assumed-versus-unasked distinction. Both are about the record, not the conversation, which is why they translate to a checklist the packet can hold.
- What did not work and why: the Gause–Weinberg PDF was an image, so the primary source on context-free questions could not be quoted; the secondary material was not strong enough to stand as evidence.
- What I would do differently: search for an elicitation method with an explicit coverage table first, rather than starting from interview technique, because the table is the confidence model's skeleton.

## Recommended Next Focus

Iteration 4: deepen into how answers persist and what changes when the user declines the loop. Read the repo's `.skilled/skills/sk-prompt/` question method, the packet's energy rules, the "just do it" paths in both packets, and the state files a later turn could read. Build on finding 2 and finding 9, and on iteration 1 finding 8 (Quick energy).

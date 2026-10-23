# Iteration 1: What the current intake does, and where it stops before a board

## Focus

Audit the current intake behaviour end to end, so later iterations design against the contract that exists rather than an imagined one. Read `sk-product-owner` Interactive Mode and its response templates, the router's clarification bands and contract, `sk-create-figjam`'s type choice, intake, gate and ambiguity recovery, the hub and `AGENTS.md`, the claude.ai kernel, and one manual-testing scenario. The question for this pass: what does the packet already do well, and where does the flow stop before a FigJam board is drawn? Builds on nothing earlier in this lineage; it is the baseline every later iteration deepens.

## Actions Taken

1. Read `sk-product-owner/references/interactive-mode.md` (572 lines) and `sk-product-owner/assets/interactive-response-templates.md`.
2. Read `sk-product-owner/SKILL.md` Sections 2, 3 and 4, `references/routing.md` confidence bands, and the kernel's Interactive and Flow sections.
3. Read `sk-create-figjam/SKILL.md`, `references/flow-mode.md` Sections 2 to 5 and 9, `references/quality-rubric.md`, `assets/flow-templates.md`.
4. Read `AGENTS.md` steps 7 and 12 and the Flow Mode exemption, plus `manual-testing-playbook/boundaries/command-conflict-asks.md` (FJ-020).

## Findings

1. **The intake is single-shot by written contract, so there is nothing today to cap at N rounds.** The architecture is `Start -> Single Question (ALL info) -> Wait -> Process -> Deliver` [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:54]. Core rule 1 asks for all unresolved information at once, and only a source conflict with no authority winner, a promised source not yet sent or a decision the user calls unsettled may hold the draft a second time [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:58]. The MUST NOT list names the same prohibition: "Ask a second clarification round for anything but a source conflict with no authority winner, a promised source still missing or a decision the user calls unsettled" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:519]. The kernel repeats the one-consolidated-question rule [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:9], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:114].

2. **The single question is one fixed template across every artifact kind, not a plan derived from what is missing.** The comprehensive template asks the same six blocks in the same order, opening with an energy choice and ending with "Assumptions to challenge" [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:53], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:59], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:81]. It carries no board-specific fact such as the reader or the question the board answers, so a FigJam request either inherits artifact-shaped questions or leaves the packet [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:59].

3. **Nothing measures confidence; the state machine has a wait, not a threshold.** The states are `start`, `comprehensive_question`, `processing`, `delivery` and `complete`, and the question state waits for input once before moving on [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:188], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:194]. The quality self-rating scores the question being asked, not the understanding behind it: clarity, completeness, assumption challenge, perspective diversity and mechanism depth, each at 8 or above [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:436]. A well-scored question can still leave the reader and the board's message unknown.

4. **The router's clarification path answers "which artifact", not "what does the board say".** Confidence bands route HIGH at 0.85 or above, LOW at 0.40 or above into Interactive Mode, and anything under 0.40 into Interactive Mode with one comprehensive question [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:40], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:41]. The contract describes the fallback as the one clarifying question [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:77]. The kernel states the same floor [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:37]. No band distinguishes a settled artifact from an unsettled board.

5. **Flow Mode has no intake loop at all; it asks only in five enumerated situations.** Those are two types fitting [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75], two step orders fitting or no authoritative source winning [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:111], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:121], an unclear plan or file [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:274], and a read-back that differs from the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:258]. Otherwise the packet's only escalation is an ON_DEMAND pointer to Interactive Mode "when the sources, the type, the target file or the order cannot be settled" [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:65], and the packet's escalation paragraph still says "ask one question" [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:185].

6. **The packet already holds a facts model in prose: the two dials, the pre-drawing test, the never-invent rule and the per-type needs table.** Detail level defaults to Balanced, audience to Mixed, and each is a stated choice the user can change [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:150], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:151]. Before drawing, the packet asks whether a list, table or paragraph would serve better [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:89]. It maps an undrawable request to the nearest drawable type [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95], and states that a missing step, service, field or date is asked about or left as a named gap, never invented [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144]. The per-type needs table already lists what a gantt needs versus what a sequence needs [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:132]. These are the raw facts, stated once, with no completeness test that would say which are still unknown.

7. **The gate is a consent gate, not a comprehension check.** Step 7 names the target plan and file, what will be written, any planned extensions, the read calls the write will spend and the rollback, then waits for a yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]. The kernel's Flow Mode Delivery repeats the same list and the read-back condition [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:254]. Every named fact is write-side. None asks the user to confirm the board's message, its reader, its accent or its detail level.

8. **Energy scales depth, not exploration: Quick shortens intake and the protected list is artifact-shaped.** The energy choice opens the comprehensive question and defaults to Standard [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:102], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:109]. Quick may skip routine intake but never Doc purpose, audience, source authority, contradiction handling or claim status [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:109], [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:305]. The protected list is Doc facts; no board fact is protected at Quick energy [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:9].

9. **The current test contract forbids the loop this brief asks for.** FJ-020's pass condition is one question naming both artifacts, and its fail condition is reached if "more than one question is asked" [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:29]. A multi-round intake therefore needs a named, deliberate exception and a new scenario family, not a quiet loosening of the one-question rule.

## Ruled Out

- **Treating Interactive Mode's five quality dimensions as the confidence model.** They score the question's phrasing, and each can be 8+ while the reader, scope and board message stay unknown [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431]. The confidence model has to score understanding of the feature, not the question text.
- **Reading the router's 0.85 band as an intake confidence.** It scores artifact intent from keywords, so a request can route to FLOW at HIGH confidence with a one-line brief [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38]. Routing confidence and board confidence are different scales.

## Dead Ends

- Searching `sk-create-figjam` for an existing intake questionnaire found only the type/order/plan questions listed in finding 5. The packet's intake is source reading (Section 4), not interviewing.

## Edge Cases

- Ambiguous input: "intake" can mean the ambiguity question or the source-reading step. This pass treats them separately: Interactive Mode's question flow, and Flow Mode's Section 4 intake.
- Contradictory evidence: none in this pass; both surfaces agree on the one-question rule and neither holds a confidence model.
- Missing dependencies: none.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/routing.md`
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `AI Systems/Product Owner/AGENTS.md`

## Assessment

- New information ratio: 0.85
- Questions addressed: key questions 1 and 5.
- Questions answered: "What do sk-product-owner Interactive Mode, the router clarification path, sk-create-figjam's gate and the kernel do today, and where does the flow stop short of a board?"

## Reflection

- What worked and why: reading the contract files in the order a request actually travels (router band, Interactive Mode state machine, Flow Mode workflow, gate, kernel) exposed the structural gap. The one-question rule is not an oversight in one file; it is stated in five places, so a loop needs an explicit exception.
- What did not work and why: trying to derive a confidence model from Interactive Mode's quality dimensions failed because those dimensions score phrasing, not feature understanding.
- What I would do differently: read the manual-testing playbook first next time, because FJ-020 shows the loop is currently a test failure and that shapes every design choice.

## Recommended Next Focus

Iteration 2: widen to the corpus. Read Figma's own `figma__mcp-server-guide` skills that ask before acting, the `figma-spec` and FigJam skills, Adobe's diagram house style, and two community FigJam builders, to extract how public skills decide when they know enough to act. Build on finding 5 and finding 6.

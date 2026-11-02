# Iteration 6: The flowchart rules sk-design-diagram actually enforces

## Focus

Enumerate the flow-chart rules at their source so the transfer question can be decided rule by rule. This opens the third key question from the rule side rather than the FigJam side: what does the current diagram system require of a flowchart, and how much of that is grammar rather than rendering?

## Findings

1. The flowchart type is defined by a shape-carries-type grammar: oval for start and end, rectangle for step or action, diamond for a decision with at most three exits, and a small filled ink dot for a merge point where branches rejoin. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20]
2. Layout and labelling rules follow: flow runs top to bottom, a diamond conventionally exits Yes to the right and No below, every outgoing arrow is labelled regardless of convention, coral appears only on the happy path or the single most consequential decision, and a crossing arrow gets a small arc jump. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:25] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:26]
3. Three anti-patterns are named explicitly: using fill color to signal node type, a decision with four or more exits, and unlabelled decision branches. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:29]
4. One of those anti-patterns is already machine-checked on the ASCII path: the validator counts decision words and fails the run with an error when decision points exist but no YES/NO labels are found. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/scripts/validate-flowchart.sh:82]
5. The type's stated fit is decision logic, algorithms, user-facing branching flows, onboarding routing and support-triage trees, which matches the Product Owner input material rather than an architecture diagram's component vocabulary. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:15]
6. The diagram skill itself cannot render a FigJam board: it supports only `html-svg` and `ascii-markdown`, and its skip list names a canvas artifact as out of scope, so a FigJam path must port the rules rather than reuse the renderer. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:10] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:42]

## Ruled Out

- Reusing the HTML/SVG renderer for FigJam. FigJam has no documented HTML or SVG import verb, and the skill explicitly excludes canvas deliverables.
- Keeping the arc-jump crossing rule. It is an SVG geometry trick with no FigJam equivalent in the six-verb surface.

## Dead Ends

- Searching the ASCII validator for shape rules. It validates labels, arrows and nesting depth, not shape vocabulary, so shape semantics live only in the type reference.

## Edge Cases

- Ambiguous input: "flow chart rules" could mean the HTML/SVG type rules or the ASCII validator rules. Selected both and labelled which is normative for what.
- Contradictory evidence: none.
- Missing dependencies: no rendered flowchart was inspected, so the rules are read from the reference rather than observed in output.
- Partial success: none.

## Sources Consulted

- `.skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:15,20-32`
- `.skilled/skills/sk-design/sk-design-diagram/scripts/validate-flowchart.sh:74-88`
- `.skilled/skills/sk-design/sk-design-diagram/SKILL.md:10,42`

## Assessment

- New information ratio: 0.95
- Questions addressed: which flow rules exist to carry over.
- Questions answered: none fully; this iteration inventories the rules, and iteration 7 decides each one.

## Reflection

- What worked and why: separating grammar from rendering in the first read made the portability question tractable, because grammar rules survive a transport change while renderer rules do not.
- What did not work and why: assuming the validator encoded shape rules was wrong; it encodes labels and depth.
- What I would do differently: read the validator first for the subset it checks, then the type reference for the rest, to avoid double-counting a rule as enforced when it is only described.

## Recommended Next Focus

Iteration 7: classify every rule from this inventory against the six-verb FigJam surface, deciding portable, replaceable or unenforceable for each, and name the FigJam-native substitute where a rule cannot survive.

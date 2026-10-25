# Iteration 001 — shared visual language and evidence baseline

## Focus

Audit the existing shared board visual grammar, rendered examples, rubric score contract, and distributed design tokens.

## Actions Taken

- Read the composer, Python model filler, style guide, quality rubric, manual scorecard, flow mode, and the seven type references.
- Inspected all nine rendered board screenshots and compared their captions and scores in the gallery.

## Findings

1. Keep the current first-glance hierarchy and spacious framing: the 64 px title, 28 px subtitle, 24 px section labels, 20 px nodes, 16 px supporting text, white board section, generous margins, aligned key, and source line create a legible entry order; user-flow, ER, and gantt examples show distinct layouts while retaining the same title and key grammar. [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:87-103,1125-1140,1142-1150,1194-1202; AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:189-204; AI Systems/Product Owner/sk-create-figjam/assets/screenshots/README.md:25-33; visual: user-flow-board.png, er-board.png, gantt-board.png]
2. Preserve meaning-based color, shape, and key semantics across types: kind-to-shape/color mappings are shared, the pink accent is reserved for the chosen first-glance object, and the key explains marks; sequence arrows, state roles, and architecture lanes deliberately retain different type-specific semantics within that common grammar. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:28-36,40-82,83-95,137-152; AI Systems/Product Owner/sk-create-figjam/references/types/sequence.md:47-58; AI Systems/Product Owner/sk-create-figjam/references/types/state.md:48-54; AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:42-53]
3. Prioritize compact back-edge routing and sequence overview legibility: state-board.png and state-on-existing-board.png show return transitions making long perimeter loops, process-board.png shows long lane trunks, and sequence-board.png is the lowest-scoring type at 19/22 while keeping a much taller lifeline layout; the gallery scores the other seven boards 21–22/22. Tune route length, label placement, and type-specific density without weakening read-back fidelity. [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/screenshots/README.md:25-33; AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:600-623; AI Systems/Product Owner/sk-create-figjam/references/types/sequence.md:47-58; visual: state-board.png, state-on-existing-board.png, process-board.png, sequence-board.png]
4. Unify the design score contract before changing visuals: quality-rubric.md Section 7 scores eight criteria out of 16, while the playbook and screenshot README use a 22-point total with extra crossings, shared-trunk, label-collision, hygiene, and reply checks; the current gallery therefore cannot be compared from the rubric alone. Name one canonical 22-point scorecard or explicitly label the 16-point design subtotal and its six operational points. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:124-139; AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:81-118; AI Systems/Product Owner/sk-create-figjam/assets/screenshots/README.md:19-33]
5. The design record is split across a style guide, JavaScript constants, Python checks, and a hand-copied Project composer: the guide claims to be the one source for color/type/spacing, but SHAPE, TINT, KINDS, TYPE, GRID and gaps live in compose-board.js, accepted pairs live in common.py, and the Project mirror parity check compares the compact JavaScript block only. This creates a clear need for a validated shared specification while preserving the current swatch and contrast rules. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:18-28,99-115,189-215; AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:17-103; AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:69-76,925-929; AI Systems/Product Owner/sk-create-figjam/claude project/knowledge/Product Owner - Assets - Flow Board Composer.md:1-16]

## Questions Answered

- How does the shared composer establish hierarchy, alignment, color, spacing, and connector clarity across all seven types?
- Which current visual strengths should remain, and which screenshot evidence points to the highest-value design changes?

## Questions Remaining

- Should the editable style spec live at packet scope, and what token schema can safely cover shared and type-specific board treatments?
- How should the CLI composer, one-call JavaScript composer, Claude Project mirror, rubric, and scorecard validate the same spec?

## Next Focus

Build a concrete style-spec location, typed token schema, safe parsing/fallback contract, and cross-runtime parity plan; test the recommendation against public DESIGN.md and design-token examples.

## Workflow execution note

The dispatched request names an active workflow YAML, while the checked-in skill says its command YAML owns state, executor selection, convergence, and synthesis. The repository inventory found no workflow YAML at the named route, so I followed the prompt’s inline-executor instruction and recorded state only through the gateway and reducer. [SOURCE: .skilled/skills/system-deep-loop/deep-research/SKILL.md:261-272; runtime inventory: no workflow YAML present]

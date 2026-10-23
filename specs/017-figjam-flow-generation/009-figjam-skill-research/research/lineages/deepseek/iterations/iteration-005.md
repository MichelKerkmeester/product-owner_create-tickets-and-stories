# Iteration 5: `amo-tech-ai__rocket-path-ai` — a rival `generate_diagram` playbook and its examples

## Focus

A community skill that uses the **same** hosted `generate_diagram` route as Flow Mode, with a full examples library. This is the cleanest A/B against Flow Mode: same tool, different rules. Builds on iteration 1 (official route) and iteration 4 (staged write).

## Actions Taken

1. Read `rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md` (154 lines).
2. Read `references/examples.md` (386 lines), sampling the flowchart, decision-tree, subgraph and use-case examples.
3. Compared its direction, quoting, shape, validation and delivery rules with Flow Mode and with the official contract.

## Findings

1. This skill uses the same hosted route as Flow Mode — "the `generate_diagram` MCP tool, which converts Mermaid.js syntax into editable FigJam boards" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:8]. Same tool, so every difference below is a rule choice, not a route artefact.

2. Its delivery has **no read-back**: Step 4 is "The tool returns a FigJam link. Share it with the user" and suggests opening the board to edit [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:105]. Flow Mode's counted read-back is therefore not a corpus norm; it is a Flow Mode strength that the closest competitor lacks [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:140].

3. It quotes **every** shape and edge label by default: `A["Start"]`, `A -->|"Yes"| B` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:48] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:51]. The official skill quotes only labels with special characters [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:323], and Flow Mode's templates are unquoted [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:45]. Universal quoting is the safe superset: it satisfies the official special-character rule without changing rendered text.

4. It advertises the "full range of shapes" — rect, rounded, diamond, stadium, subroutine, circle, flag, hexagon [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:52]. This contradicts the official warning that "most silently fall back to a plain rectangle in FigJam" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:33]. Flow Mode's four-shape rule is closer to the documented renderer behaviour; this repo's permissiveness is a trap, not a capability.

5. It defaults to `LR` and uses `TD` only for decision trees [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:47]. Combined with iteration 1's official default, that is **three** independent sources preferring LR for process flows. Flow Mode's TD-only rule is a deliberate house style, not a corpus norm, and should be documented as such rather than justified as a generator requirement [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:62].

6. Its only validation is post-hoc: "the `generate_diagram` tool will reject invalid syntax" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:38]. This is the second corpus source (after official Figma's prose checklist, iteration 1) with no pre-write model gate, deepening iteration 1 finding 9: Flow Mode's executable `flow_check.py` is the outlier in the good direction.

7. It reserves `end` for state-diagram class names [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:79], corroborating the reserved-word hazard in a **second** diagram type and strengthening the case for a node-ID check in `flow_check.py` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44].

8. It recommends subgraphs for complex flowcharts (`subgraph "Section Name"`) and its examples use quoted subgraph names [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:152] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:51]. Flow Mode has no subgraph policy at all — it neither uses nor forbids them — while the official reference supports them at up to two levels of nesting [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:157].

9. Its densest worked example is a **9-node** `flowchart LR` onboarding flow, and its decision trees use three labelled exits [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:22] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:92]. That is empirical support for Flow Mode's 9-node and 3-exit caps from a practitioner who never adopted them — the limits match what a hand-authored example library actually draws.

10. It repeats the emoji prohibition as a general rule for every diagram type [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:41], a third independent confirmation of iteration 1 finding 2 and further evidence that `flow_check.py`'s missing emoji rule is a real defect [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44].

11. Its iteration advice is only "start simple — generate a minimal diagram first, then iterate" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:151]; unlike iteration 4's canary, it attaches no verification to the minimal first diagram, so the iteration is unguarded.

## Ruled Out

- Adopting this repo's shape vocabulary: it conflicts with the official renderer behaviour and with Flow Mode's four-shape discipline.
- Adopting its LR default wholesale: Flow Mode's TD-only is a product decision about reading user flows on a board; the corpus shows LR is common, not that TD is wrong.

## Dead Ends

- Searching for a pre-write validator or a read-back in this repo: none exists.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: this repo's "full range of shapes" versus the official fall-back warning; the official reference wins because it describes renderer behaviour, not aspiration.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- None in full. Q5 now has three sources agreeing on density and exits but disagreeing on direction.

## Questions Remaining

- Q1, Q2, Q4, Q5 remain open; two FigJam repos (FMCP, Ompug) and the Mermaid-side repos are unread.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md`
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`

## Assessment

- New information ratio: 0.85 (7 new, 4 partial — three findings corroborate iterations 1–4 and one refines the direction debate)
- Questions addressed: Q5 (three-source support for 9 nodes/3 exits), Q1 (a no-check competitor)
- Questions answered: none

## Reflection

- What worked and why: reading a same-route competitor produced the cleanest evidence so far, because route variables cancel out.
- What did not work and why: nothing failed; the examples file is long and only the densest examples were worth citing.
- What I would do differently: compare same-route skills earlier, since rule differences are most legible when the tool is constant.

## Recommended Next Focus

Iteration 6: `atezer__FMCP/skills/figjam-diagram-builder` — a fifth distinct route and the likeliest source of a diagram-type taxonomy or builder pipeline, to test Q1's "machine-enforced" half.

# Iteration 6: `atezer__FMCP` — safe-mode bridge, deterministic coordinates, phased writes

## Focus

A bridge-plugin route written for scale rather than beauty: response-size safety, deterministic coordinates, and explicit node limits per call. This is the first corpus source that treats write mechanics as an engineering budget, and it directly tests Flow Mode's 9-node cap and its `fj` position computation.

## Actions Taken

1. Read `atezer__FMCP/skills/figjam-diagram-builder/SKILL.md` (180 lines). The source is Turkish; claims below are from its structure and code, not from idiom.
2. Extracted the response-size rules, coordinate constants, three-phase write, per-call node limits, font rule and error taxonomy.
3. Compared them with Flow Mode's `fj` route and with iterations 2–4.

## Findings

1. The skill exists to stop tool results from breaking the session: it mandates short returns — `"OK: 12 node, 14 connector"`, errors capped near 200 characters, small JSON — and forbids returning big node lists, `currentPage.children` or pluginData dumps [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:49] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:53]. Flow Mode has no response-size budget for its read-back, and iteration 2 already warned that a whole-page read can overflow [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65].

2. Coordinates are never persisted between steps; they are recomputed every step from one constant table (`OX=3500, OY=100, LW=160, CW=300, LH=200, HH=64, NW=240, NH=76`) so a retry lands in the same place [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:72] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:77]. Flow Mode's `fj` route computes every position but specifies no constant table [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:123]; without one, two runs of the same model can produce different layouts.

3. Production is split into three phases — ground (lanes, background, headers), then nodes (cards, text, badges), then connectors (arrows and decision links) — with a short result returned after each phase [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:82] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:84]. This sits between Flow Mode's single hosted call and iteration 4's one-node canary: it is a per-layer checkpoint, not a per-node one.

4. Per-call node limits are explicit and time-based: 1–6 `shapeWithText` nodes fit the default 5000ms, 7–12 need `timeout: 10000`, and 13+ must be split across calls [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:150] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:152]. Flow Mode's 9-node cap falls inside the 7–12 band, so the cap already implies a non-default timeout on this route [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:43]; Flow Mode's `fj` route states no timeout at all.

5. The font failure is named precisely: `createShapeWithText()` defaults to **Inter Medium**, and loading Inter Regular is not enough — the shape still fails [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:59] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:65]. Iterations 3 and 4 said "load fonts"; this gives the exact style that must be loaded.

6. The decision diamond is built manually with `createPolygon(pointCount=4)` plus `rotation=45` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:119]. This shows the shape vocabulary is a function of the route's primitives, not a universal design rule, and supports Flow Mode keeping a route-specific four-shape set rather than a global one [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97].

7. Retry policy is tiered: a timeout is retried once, then scope is narrowed (fewer nodes, lower depth); an empty response means checking the target node or page; rate limits are checked explicitly [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:171] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:172]. Flow Mode's recovery is ask-then-re-run into a cleared page [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159], which has no bounded retry count and no scope-reduction step.

8. Large-file reads start at low scope (`depth=1`, `verbosity="summary"`, screenshots excluded) and only then go node by node [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:99] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:103]. This is the third independent source for bounded read-back, after iteration 2's whole-page warning and iteration 3's `MAX_NODES` cap.

9. Scan safety is explicit: never scan or return `figma.currentPage.children`; keep only the nodes created in the current step in a local `created[]` list and use that list for zoom [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:90] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:92]. Flow Mode's read-back has no "created nodes only" list, so it cannot distinguish its own output from pre-existing board content — the same problem iteration 2's section rule solves structurally.

10. The skill carries evolution triggers — if the bridge adds FigJam-specific tools, or the payload limit changes, or new diagram types are requested, the strategy must be revised [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:178] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:180]. Flow Mode has no stated trigger that would tell a maintainer when its route assumptions have expired.

11. Swimlanes are a first-class pattern with a per-lane semantic palette and dashed connectors for alternative flow [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:110] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:115]. Flow Mode's TD-only, four-shape model cannot express lanes at all, so any cross-role flow is forced into a linear chain [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:100].

## Ruled Out

- Adopting the F-MCP bridge as a Flow Mode route: it requires a third-party plugin plus Desktop, and Flow Mode already has a Desktop fallback.
- Adopting the swimlane pattern into Flow Mode's current model: it needs a lane primitive and a second layout axis, neither of which the Mermaid-to-FigJam route exposes.

## Dead Ends

- No pre-write model check exists here; the skill is purely execution safety. Recorded so Q1 is not re-probed in this repo.

## Edge Cases

- Ambiguous input: the source is Turkish; the structural rules and code constants are unambiguous, but idiomatic claims are avoided.
- Contradictory evidence: none.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- None in full. Q5 gains a time-based justification for small diagrams; Q2 gains a fifth route.

## Questions Remaining

- Q1, Q2, Q4, Q5 remain open.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`

## Assessment

- New information ratio: 0.90 (9 new, 2 partial — font and bounded-read findings corroborate earlier iterations)
- Questions addressed: Q2 (fifth route), Q5 (node-count/timeout relationship)
- Questions answered: none

## Reflection

- What worked and why: reading a scale-oriented skill produced operational constraints (timeouts, constants, return sizes) that design-oriented skills never state.
- What did not work and why: the Turkish source slows literal citation, so only structural claims were used.
- What I would do differently: request a translation only if a rule is ambiguous; code constants were sufficient here.

## Recommended Next Focus

Iteration 7: `ompug__diagram-codebase` — a Mermaid-generation pipeline with tests, and the first corpus source that parses and lints Mermaid rather than writing nodes. It is the best candidate for answering Q1's machine-enforced half and Q4's identifier hazards.

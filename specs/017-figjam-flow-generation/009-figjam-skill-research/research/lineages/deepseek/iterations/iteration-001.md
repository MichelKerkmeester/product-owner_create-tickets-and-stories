# Iteration 1: Figma's official hosted-route contract (`figma-generate-diagram` + `figma-use-figjam`)

## Focus

Establish the authoritative contract Flow Mode writes against: Figma's own `figma-generate-diagram` skill and its flowchart reference, plus the `figma-use-figjam` skill. This is the baseline against which all community repos are measured. No prior iteration; this is the frame.

## Actions Taken

1. Read `figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md` (112 lines).
2. Read `figma-use-figjam/SKILL.md` (64 lines).
3. Read the direction, shapes, text-quality, density, validation, and colour sections of `figma-generate-diagram/references/flowchart.md` (407 lines, sections 1, 2, 6, 7, 8, 9).
4. Compared each rule with `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py` and `references/flow-mode.md`.

## Findings

1. Figma requires the `figma-generate-diagram` skill to be loaded before **every** `generate_diagram` call, because skipping it "causes preventable rendering failures and low-quality output"; the tool accepts Mermaid and returns an editable FigJam diagram [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:8]. Flow Mode has no equivalent pre-load requirement: its guard is the standalone `flow_check.py`, which knows only the Mermaid model, not the tool schema or its failure modes [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:62].

2. Emojis are a hard tool-level rejection, stated as universal constraint #1 and repeated in the label audit: "No emojis (tool rejects)" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:318]. Flow Mode's check has no emoji rule at all: `MARKUP_MARKS` lists only `<`, `>`, newline, `**` and backtick, so an emoji-bearing label passes [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44]. This is a confirmed Flow Mode gap, not a hypothetical.

3. Reserved node IDs are named explicitly — `end`, `subgraph`, `graph` — and node IDs must be camelCase with no spaces because "underscores can break edge routing in some processors" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:52] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:53]. The same pair is repeated in the flowchart reference [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:321]. `flow_check.py` never inspects node IDs — it validates shape, direction, label markup, decision exits and node count only — so `end`, `subgraph`, `graph` and underscore IDs pass the pre-write gate [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:57].

4. FigJam has one implicit page, and `figma.createPage()` throws `TypeError: figma.createPage no such property 'createPage' on the figma global object`; the official guidance is to organize with FigJam sections instead [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13]. The same warning is carried in the generate-diagram constraints for hybrid `use_figma` extensions [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:57]. Flow Mode's gate nevertheless offers "a new page, or a page you have read and found empty" as the target and defines rollback as "clearing the page" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:115] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117]. For a FigJam board created by `generate_diagram`, that page premise is unsatisfiable: there is no page to create and nothing to clear.

5. `generate_diagram` creates its own file: calling `create_new_file` first is explicitly forbidden, and every call without a `fileKey` creates a new draft file [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:92] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102]. Flow Mode's gate asks the operator to state "the target plan, file and page" before the write [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:63], which presumes the operator supplies a file that the hosted route would only create.

6. Official iteration policy is `fileKey` reuse plus deliberate deletion: pass the existing board's `fileKey` for follow-ups, and to replace rather than add, delete the old diagram's nodes through `use_figma` before regenerating [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:109] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110]. Flow Mode has no `fileKey` guidance, no reuse rule and no delete-before-regenerate recipe; its recovery says re-run into a cleared page only after user agreement [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159].

7. Direction: the official default is `flowchart LR`, with `TD`/`TB` reserved for hierarchies, taxonomies, deep narrow trees or many siblings at one level [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:27]. Flow Mode makes TD mandatory for every diagram [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:41]. The official guidance therefore supports TD as a valid choice but not as the only choice.

8. Density: official soft caps are ~20 nodes fine, 20–30 consider subgraphs, 30+ split; the validation checklist uses "≤ ~25 nodes" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:329] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:349]. Flow Mode caps at 9 nodes and requires splitting a longer flow [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:99]. Flow Mode is 2.2–2.8× stricter than the vendor's own soft cap.

9. Official validation is a prose checklist of eight human judgements (cycle check, orphans, input/output, label audit, shape audit, colour audit, subgraph audit, density check) with no executable checker [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:337]. Flow Mode is the outlier in the good direction: it is the only source so far with a machine-enforced gate and planted-failure self-test [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:154].

10. Official colour guidance permits multiple semantic colours — status, ownership, subsystem — as long as colour encodes meaning and not every node is painted [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:267] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:282]. Flow Mode's one-accent rule is stricter than the vendor and is enforced by counting distinct hex values in `style`/`classDef`/`linkStyle` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:47].

## Ruled Out

- Treating `figma-generate-diagram`'s workflow reference as primary for this iteration: it covers hybrid annotations/colour-coding, which belongs to the write-route iteration, not the rule baseline.
- Reading the duplicate `skills-figquery/` tree as a separate source: it is a mirrored copy, not independent evidence.

## Edge Cases

- Ambiguous input: none; the official skill is explicit.
- Contradictory evidence: Flow Mode requires a page target, official FigJam has no page. Recorded as finding 4 with both sources; the contradiction is real and is the first confirmed Flow Mode defect.
- Missing dependencies: none.
- Partial success: none; all reads succeeded.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`

## Assessment

- New information ratio: 0.90 (10 findings, all new; no prior packet evidence existed)
- Questions addressed: Q1 (rule/check baseline, official half), Q4 (identifier hazards, official half), Q5 (limits, official half)
- Questions answered: none in full; all three need the community repos before an adopt/reject verdict

## Reflection

- What worked and why: reading the vendor skill first fixed the ground truth before community repos could muddy it. The vendor file names the four known gaps in plain text, so the gap analysis does not depend on inference.
- What did not work and why: nothing failed; the mirrored `skills-figquery/` tree is a duplicate risk to avoid in later iterations.
- What I would do differently: cite the flowchart reference's section numbers alongside lines so later iterations can revisit the rule without re-reading 407 lines.

## Recommended Next Focus

Iteration 2: `IamTheLime__dotfiles/agents/skills/figjam-diagrams` — the most likely source of a second executable rule set and a concrete write recipe; compare its check list and write route against the official contract established here.

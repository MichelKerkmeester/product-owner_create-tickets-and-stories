# Iteration 8: `memi-design__mermaid-jam` — parser-level diagnostics, ID normalization, revise-before-generate

## Focus

The only corpus tool that parses Mermaid itself and renders it into FigJam. This iteration closes Q1 (which checks are machine-enforced) and Q4 (emoji, reserved IDs, underscores) with the last unread source, and deepens iteration 7's linter comparison. Builds on iterations 1, 7.

## Actions Taken

1. Read `memi-design__mermaid-jam/README.md` (141 lines).
2. Read `src/parser/mermaidJam.ts` (1159 lines): unsupported-construct table, header validation, ID generation, label cleaning.
3. Read `src/shared/reviser.ts` (first 160 lines): the local repair pass and its limits.
4. Checked `src/plugin/main/renderer.ts` for position preservation.

## Findings

1. Mermaid Jam is a local-only FigJam plugin that converts pasted Mermaid and markdown into native sections, shape cards and dynamic connectors [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:14]. It is a sixth route — a full parser plus renderer — and the only source that takes arbitrary Mermaid as its primary input rather than generating Mermaid internally.

2. Its header diagnostic names all five accepted directions: `flowchart TD` or `graph LR` with direction `TD, TB, BT, LR, or RL` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:113]. This is the fourth independent source treating direction as a per-diagram choice, and the strongest single piece of counterevidence to Flow Mode's TD-only rule [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:61].

3. Unsupported constructs are rejected with diagnostics rather than silently dropped: class definitions, class assignments, style directives, linkStyle, click callbacks, init directives, icons and images [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:24] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:31]. Flow Mode's accent rule is expressed through exactly `style`, `classDef` and `linkStyle` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:47], so an accent rule is only meaningful on routes that support styling.

4. IDs are normalized rather than checked: `sanitizeId` keeps only alphanumeric words, upper-cases each word, joins the first five, and prefixes `Step` when the result does not start with a letter [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:845] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:857]. Underscores cannot survive, and duplicates get a numeric suffix [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:849]. That is a third strategy: ompug suffixes reserved words, Flow Mode relies on author discipline, Mermaid Jam rewrites the ID.

5. Labels are repaired, not only rejected: the reviser removes filler phrases ("in order to", "that are", "the user") and hard-caps a label at 120 characters with a word-safe ellipsis [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:133] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:138]. Compare ompug's 80-character cap and Flow Mode's no cap; all three approaches accept that long labels are a defect.

6. "Revise" is a repair-then-parse pass: it strips fences, normalizes arrow glyphs to `-->`, adds `flowchart TD` when the header is missing, dedupes statements, quotes labels with special characters, then re-parses and serializes only if the result is valid [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:66] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:115]. Flow Mode has no repair pass; a failing model must be edited by hand and re-checked [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:151].

7. The reviser refuses oversized sources: above 700 lines it returns an error telling the user to split into diagrams under 700 lines [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:24] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:28]. This is a pre-work size gate; Flow Mode's equivalent is a post-model node cap, which does not bound the input size that produced it [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:43].

8. Generated output is always contained in a FigJam section [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:30], and on update it preserves manually moved node positions when IDs match [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:27] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/plugin/main/renderer.ts:876]. Flow Mode guarantees neither: the hosted route adds a new diagram rather than updating one, and its rollback is a page clear rather than a container-scoped replace [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117].

9. Diagnostics are line-numbered and returned before generation, together with a cleaned source; generation is refused when any diagnostic is an error [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:143] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:144]. This is the third executable pre-write check in the corpus, after Flow Mode and ompug, and it reports diagnostics as data rather than console text.

10. Unsupported Mermaid types — pie, gantt, erDiagram, classDiagram — return explicit diagnostics instead of bad output [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:44], corroborating iteration 7's skip-with-reason rule as a corpus norm.

11. Subgraphs are the one construct the corpus cannot agree on: the official reference supports them up to two nesting levels [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:157], rocket-path recommends them [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:152], and Mermaid Jam rejects them outright as unsupported [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23]. Flow Mode's silence is therefore a gap either way: it should state whether subgraphs are allowed and, if so, cap nesting at two.

## Ruled Out

- Adopting Mermaid Jam's plugin as a Flow Mode route: it is a consumer-facing plugin with its own UI and no MCP surface, so Flow Mode cannot call it.
- Adopting ID rewriting into Flow Mode: the provenance table depends on stable authored IDs, so rewriting them would break node-to-source mapping [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33].

## Dead Ends

- No emoji-specific handling was found in this repo; its label cleaning removes markdown syntax but not emoji. Recorded so Q4's emoji verdict rests on the three sources that address it directly.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: Mermaid Jam rejects styling constructs that Flow Mode's accent rule depends on; resolved as a route capability difference, not a rule conflict.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- Q1: only three corpus sources machine-enforce a pre-write check — Flow Mode's `flow_check.py`, ompug's `lint.py`, and Mermaid Jam's parser diagnostics. Figma's official skill is a prose checklist; IamTheLime verifies by screenshot; southleft and Labor verify by read-back; rocket-path relies on tool rejection. Flow Mode is therefore in the strongest tier and its gap is rule coverage, not the existence of a gate.
- Q4: emojis are a hard rejection in every source that addresses them (official, ompug, rocket-path), and `flow_check.py` does not check them; reserved IDs `end`/`subgraph`/`graph` are named by official, enforced by ompug with a wider keyword list, and echoed by rocket-path for state diagrams; underscores are warnings in prose but **errors** in ompug because they break edge routing, and Mermaid Jam strips them entirely at ID generation. All three should become errors in `flow_check.py`, with non-camelCase left as a warning.

## Questions Remaining

- Q2 (full route/read-back matrix; ompug's driver unread) and Q5 (limits verdict) remain open.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/plugin/main/renderer.ts`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`

## Assessment

- New information ratio: 0.91 (9 new, 2 partial — direction and skip-with-reason findings corroborate earlier iterations; (9 + 1) / 11 = 0.909)
- Questions addressed: Q1 (answered), Q4 (answered), Q2 (sixth route)
- Questions answered: Q1, Q4

## Reflection

- What worked and why: reading a real parser produced implemented policy on every hazard the topic names, including the ID-rewrite strategy no skill prose mentioned.
- What did not work and why: no emoji handling exists here, so the emoji verdict had to rest on the other three sources.
- What I would do differently: read this repo before writing iteration 7's "only other executable gate" claim, which needed correcting to three.

## Recommended Next Focus

Iteration 9: deepen iteration 2's section/rollback finding by reading `memi-design__mermaid-jam`'s renderer container code and `ompug`'s Figma driver, then close Q2 with a complete route/read-back matrix.

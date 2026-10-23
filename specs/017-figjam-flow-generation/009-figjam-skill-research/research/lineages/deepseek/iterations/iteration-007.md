# Iteration 7: `ompug__diagram-codebase` — the only Mermaid linter that mirrors the official rules

## Focus

The corpus's one true pre-write validator: a 978-line Python linter for Figma `generate_diagram` rules, plus a builder that derives deterministic IDs and a sanitizer. This is the direct competitor to `flow_check.py` and the decisive source for Q1 and Q4. Builds on iteration 1 (official rules) and iteration 5 (same-route A/B).

## Actions Taken

1. Read `skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py` (978 lines, rule inventory and flow checks).
2. Read `sanitize.py` (353 lines, normalization), `parsecheck.py` (102 lines, optional real parser) and the ID/label portions of `build.py` (819 lines).
3. Read `references/diagram-types.md` (55 lines) for density and split policy.
4. Compared the rule set line by line with `flow_check.py` and the official skill.

## Findings

1. The linter is an explicit machine port of the official rules: "Rules come from the official figma-generate-diagram skill and its references", `lint()` returns `{severity, rule, line, message}`, and "Any error means the text must not be sent to Figma" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:3] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:14]. Flow Mode's `flow_check.py` is the only other executable pre-write gate in the corpus [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:6]; everything else is prose, read-back or tool rejection.

2. The reserved-ID check is broader than the official prose: `end`, `subgraph`, `graph` **plus** the Mermaid keywords `style`, `class`, `classdef`, `click`, `default`, `flowchart`, `direction`, `linkstyle` are errors [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:45] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:523]. This answers Q4's reserved-word half with an implemented list, not an inference.

3. Underscores are an **error**, with the reason written into the message: "node id ... contains '_' (breaks Figma edge routing)" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:526]. Non-camelCase IDs are only a warning, and subgraph IDs get both checks [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:532] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:539]. The severity split is a usable design: underscores break routing, so they block; case style is cosmetic, so it warns.

4. Its direction rule accepts `LR`, `TD`, `TB`, `RL` and `BT`, and only requires `LR` for architecture diagrams [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:211] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:213]. This is machine-enforced counterevidence to Flow Mode's TD-only check [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:61]: the corpus's most rigorous linter treats direction as a per-diagram-type choice.

5. Emoji, literal `\n`, HTML tags, control/invisible characters, unbalanced quotes and backticks are all caught at the line level [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:150] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:157]. Flow Mode checks only HTML, newline and markdown marks, and would pass an emoji [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44].

6. The sanitizer is the other half of the same policy: `normalize_text` strips HTML, emoji, invisible and control characters, literal escapes and backticks, then collapses whitespace [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:307] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:315]. So the project rejects hand-written text and **fixes** generated text. Flow Mode only rejects; adopting sanitize-on-build for labels would turn an emoji failure into a silent, deterministic repair.

7. IDs are generated deterministically and reserved words are avoided by an allocator that appends a suffix (`end` becomes a legal ID) [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:223] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:263]. Flow Mode leaves node IDs to the author and its templates use short handwritten names, so a reserved word is a preventable authoring error rather than an impossible one [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33].

8. `id_map(spec)` exposes the spec-id → Mermaid-id mapping "so the Figma driver can verify what was drawn" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:10] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:365]. Flow Mode's provenance table maps nodes to sources, not model IDs to board node IDs, so its read-back cannot trace a specific board node back to a model node [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:109].

9. Labels are length-capped at 80 characters with an ellipsis, and IDs at 32 with a short hash [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:24] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:25] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:202]. Flow Mode has no label-length limit, only a one-line rule, while the official reference warns long labels stretch shapes awkwardly [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:320].

10. A real Mermaid parser check exists but is optional, and when unavailable it must be reported "as not run (never as passed)" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/parsecheck.py:2] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/parsecheck.py:63]. Flow Mode's extractor is hand-written and vendored, so a construct it accepts may still fail the real parser; Flow Mode has no "not run" state at all [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:13].

11. Density is a split-and-name policy, not only a cap: readability limits are about 25 nodes and 30 edges, oversized diagrams split into `-part-2`, `-part-3`, and "anything left out is named in the diagram's `notes`, never dropped silently" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:31] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:32]. Flow Mode splits at 9 nodes but does not require naming what was omitted [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:99].

12. Unsupported diagram types are skipped with a reason rather than faked [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:37], matching Flow Mode's honesty rule for unreachable routes [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:131] but applied one level earlier, at request classification.

## Ruled Out

- Adopting the full lint rule set verbatim into `flow_check.py`: most rules are already there, and the additions must be split into errors (emoji, reserved IDs, underscores) versus warnings (camelCase, backticks) rather than imported wholesale.
- Adopting the 25-node density cap: it is 2.8× Flow Mode's 9 and belongs to codebase architecture diagrams, not product user flows.

## Dead Ends

- Looking for a FigJam writer in this repo: the driver exists (`figma/driver.py`) but is outside the FigJam diagram-skill surface this run is comparing; the linter and builder are the transferable part.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: this repo's `LR` default and 25-node cap both conflict with Flow Mode's TD-only and 9-node rules; recorded as conflicts, not resolved in Flow Mode's favour.
- Missing dependencies: none; all files read directly.
- Partial success: none.

## Questions Answered

- None in full, but Q1 and Q4 are now one iteration from closure: only `memi-design__mermaid-jam` remains unread on the Mermaid side.

## Questions Remaining

- Q1, Q2, Q4, Q5 remain formally open.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/parsecheck.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`

## Assessment

- New information ratio: 0.91 (10 new, 2 partial — reserved-word and emoji findings corroborate iteration 1 but gain implemented severity)
- Questions addressed: Q1 (a second executable gate), Q4 (implemented reserved and underscore checks), Q5 (density counterexample)
- Questions answered: none

## Reflection

- What worked and why: reading source code rather than skill prose produced the only implemented rule list in the corpus, including the severity choices that prose never states.
- What did not work and why: the driver layer is large and not needed for this comparison; stopping at the linter/builder kept the iteration focused.
- What I would do differently: read source before prose for any repo that ships code.

## Recommended Next Focus

Iteration 8: `memi-design__mermaid-jam` — the only Mermaid-parser-based tool left. Read its parser (`src/parser/mermaidJam.ts`) to close Q4 on identifier and label handling, then answer Q1 and Q4 explicitly.

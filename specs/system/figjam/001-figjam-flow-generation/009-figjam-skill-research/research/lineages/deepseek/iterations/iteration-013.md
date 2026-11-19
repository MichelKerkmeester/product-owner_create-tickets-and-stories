# Iteration 13: what the extractor actually exposes — a new gap in edge operators and two dead markup checks

## Focus

Write the proposed checks against real extractor data instead of assumed fields. Reading `mermaid_extract.py` and probing it with five edge operators and a markup label turned up two findings that no corpus source could have produced: Flow Mode never validates edge operators at all, and half of its markup rule can never fire. Deepens iterations 12 and 7.

## Actions Taken

1. Read `Node`, `Edge`, `Diagram`, `clean_label`, `add_node`, `parse_block` and the extractor's limits.
2. Probed a model with `-->`, `-.->`, `---`, `<-->` and `==>` to see what the parser records.
3. Probed a model with emoji, `**bold**`, `<b>tag</b>` and `<br/>` to see what survives cleaning.
4. Checked that the extractor's own node cap does not shadow Flow Mode's nine-node rule.

## Findings

1. **Every proposed check has its data already.** `Node` exposes `id`, `label`, `shape`; `Edge` exposes `source`, `target`, `label`, `style`, `arrowhead`, `bidirectional`, `undirected` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:63] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:79]. The reserved-ID, underscore, emoji and length rules are conditions on fields that already exist; none needs a parser change.

2. **New gap: `flow_check.py` never validates edge operators.** A probe of `-.->`, `---`, `<-->` and `==>` produced `style=dashed`, `undirected=True`, `bidirectional=True` and `style=thick` respectively, and all four pass the checker because it only looks at edge labels [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:181]. Flow Mode's model is therefore allowed to contain an undirected connector, a two-way connector, a dashed relationship or a thick edge — four semantics the board will faithfully render and the read-back has no vocabulary to reject.

3. **The edge rule should be: solid, one-directional, arrow at the target.** That is the only operator set consistent with a flow whose connectors mean "then". `---` yields a connector with no arrowhead, which `parse-figjam` would read as undirected [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50]; `<-->` yields two arrowheads, read as bidirectional. Both contradict a directed user flow and neither is caught today.

4. **Two of the five markup marks are dead conditions.** `clean_label` strips `<...>` tags and `**`/`__` emphasis before the checker sees a label, so the `<`, `>` and `**` entries in `MARKUP_MARKS` can never match a `node.label` or `edge.label` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:234] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44]. A probe confirmed `Use **bold** and <b>tag</b>` arrives as `Use bold and tag`.

5. **Only the line-break mark survives cleaning.** `<br/>` becomes a real newline and the cleaned label keeps it, so `\n` still fires — which is why the planted line-break test passes and hides the dead marks [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:139]. The rule's guarantee is narrower than its docstring claims: it rejects line breaks, not markup.

6. **The raw text still carries markup to the generator.** The extractor is a checker-side reader; the Mermaid block sent to `generate_diagram` is the original text. So a model with `**bold**` passes the check and the generator silently drops the markup, producing plain text rather than a rejected model. The rule should either scan `block_text` (as the accent check already does) or be reworded to cover line breaks only [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:46].

7. **Backticks are stripped only when they wrap the whole label**, so the backtick mark is dead for the common case and would fire only for an interior backtick [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:239]. A raw-text scan resolves all three dead marks in one change.

8. **Emoji survives cleaning**, so the emoji rule can run on `node.label` and `edge.label` directly; the probe kept `Start ✅` and `Yes 👍` intact [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:249]. No raw-text scan is needed for emoji.

9. **Node IDs are never cleaned**, so the reserved-word and underscore rules can test `node.id` exactly as written; `_strip_class_suffix` removes only a `:::class` attachment [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:569]. A reserved word in a label is harmless; only an ID matters.

10. **The extractor's limits do not shadow the checker's.** `MAX_NODES = 2000` and `MAX_EDGES = 5000` sit far above Flow Mode's 9, so a ten-node model parses and then fails the checker's rule; the existing planted test is reachable [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:36] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:75]. Had the extractor capped at 9, the checker's test would have exited 2 instead of 1.

11. **The subgraph scan must be anchored to a statement start.** A label such as `Enter subgraph settings` contains the word but is not a subgraph; anchoring `^\s*subgraph\b` on the raw block avoids the false positive, matching the accent check's anchored-regex style [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:47].

12. **The edge rule and the board read-back can share one vocabulary.** Model-side `style` and `arrowhead` map directly onto `parse-figjam`'s `strokeDashes` and cap fields, so the checker's error names the same property the read-back inspects [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:42] [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:48]. That makes the new rule the first Flow Mode rule with an exact inverse check.

## Ruled Out

- Adding a parser change for edge rules: `Edge` already carries the needed fields.
- Checking markup on `node.label`: two marks are dead there; raw text is the only honest surface.
- Treating a reserved word in a label as a defect: the generator only reserves IDs.

## Dead Ends

- Probing `parse_block` with a `subgraph` model returned no diagram, so subgraph structure is not modelled; this confirms the raw-text scan rather than a node-level check. Recorded so a later iteration does not look for subgraph nodes.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: `clean_label` promises to "flatten markup without interpreting it", which is true, but the checker's docstring implies rejection; resolved by recommending a raw-text scan.
- Missing dependencies: none.
- Partial success: the probe model was parsed but not rendered, so the board effect of a dashed edge is inferred from the Mermaid operator, not observed.

## Questions Answered

- Follow-on: can all five proposed checks be written against existing fields? Yes.
- Follow-on: does any current rule not do what it says? Yes — the markup rule, for three of its five marks.

## Questions Remaining

- Whether a thick or dashed edge is ever useful in a Flow Mode diagram; the corpus treats dashed as a distinct relationship but Flow Mode has no need for one at nine nodes.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md`

## Assessment

- New information ratio: 0.70 (four genuinely new: unchecked edge operators, two dead markup marks, cleaning behavior, extractor caps; the rest are partial synthesis)
- Questions addressed: implementation feasibility, rule integrity
- Questions answered: both follow-ons above

## Reflection

- What worked and why: probing the parser instead of reading only its dataclasses produced the edge-operator gap, which is the most consequential finding since iteration 7.
- What did not work and why: the earlier iterations trusted `MARKUP_MARKS` at face value; only a probe showed three marks cannot fire.
- What I would do differently: probe every check against the parser before declaring it implementable.

## Recommended Next Focus

Iteration 14: turn the edge rule and the raw-text markup scan into precise replacement text for `flow_check.py` and the `flow-mode.md` rule list, including the two planted models they need, and check the change against the checker's exit codes.

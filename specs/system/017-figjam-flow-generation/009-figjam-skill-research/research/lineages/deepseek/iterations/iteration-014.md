# Iteration 14: replacement text for the checker and the rule list, with the planted models it needs

## Focus

Turn iterations 12 and 13 into exact replacement text: constants and conditions for `flow_check.py`, the nine-bullet rule list for `flow-mode.md`, and the planted models that prove each rule. Also recalculate the "first six rules" sentence the new bullets invalidate. Deepens iterations 12, 13 and 11.

## Actions Taken

1. Drafted the constants, helper and conditions against the real `Node`/`Edge` fields.
2. Reordered the rule list so the check/read-back split stays a clean prefix.
3. Tested the five shipped patterns in `flow-templates.md` against the proposed rules by inspection.
4. Checked the exit-code paths each new rule uses.

## Findings

1. **The rule list grows from seven bullets to nine, and the split sentence must change with it.** Current order is shapes, exits, nodes, direction, labels, accent, generator; the check owns the first six and the read-back owns the last [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:95]. Inserting edges after direction and subgraphs after edges gives nine bullets, the check owning the first eight and the read-back the last [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97]. Leaving the sentence at "first six" would silently misdescribe the gate.

2. **Proposed constants** — add `MAX_LABEL = 80`, `EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")`, `RESERVED_IDS = {"end", "subgraph", "graph", "flowchart"}`, `SUBGRAPH = re.compile(r"^\s*subgraph\b", re.I | re.M)` and `HTML_TAG = re.compile(r"<[A-Za-z/][^>]*>")` beside the existing block [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:40]. The reserved set stays small because only keywords that break parsing belong there; Mermaid's wider keyword list is a linter concern, not a gate concern [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37].

3. **Reserved IDs should be matched exactly, not case-insensitively.** Mermaid keywords are lowercase and IDs are case-sensitive, so `End` is a legal ID while `end` is not; iteration 12's whole-word, case-insensitive suggestion would reject a legal model [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:63]. Membership in a set is simpler than a regex and has no false positives.

4. **Edge condition** — inside the existing edge loop: reject `edge.style != "solid"`, `edge.undirected` and `edge.bidirectional`, with one message naming the operator's meaning, for example `edge a to b is undirected; Flow Mode connectors are solid and one-way` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77]. The probe confirmed the three fields carry exactly these states for `---`, `<-->`, `-.->` and `==>` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:181].

5. **The raw markup scan must not look for a bare `<` or `>`.** `>` occurs in every `-->` operator and `<` in `<-->`, so a naive scan would flag the whole model. Match an HTML tag (`<[A-Za-z/][^>]*>`) and `**` instead, and keep the newline check on the cleaned label [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:46]. This is the precise correction to iteration 13's "scan raw text" recommendation.

6. **Emoji check belongs on the cleaned labels.** One condition in the node loop and one in the edge loop, both using the same regex, since a decision-exit label renders the same way as a node label [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:66] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:78]. The probe showed emoji survive `clean_label` untouched.

7. **Label length should be measured after cleaning.** The cleaned label is what renders, so `len(node.label) > MAX_LABEL` is the honest test; measuring the raw source would count markup the board never shows [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:63]. One condition, shared by node and edge labels.

8. **Underscore stays an error and camelCase stays unenforced.** `"_" in node.id` is exact and testable; a camelCase warning would need a second output channel and a non-binary exit code the checker does not have [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:83]. Deferring the warning keeps the gate's contract: exit 0 passes, 1 fails, 2 unreadable.

9. **Subgraph rejection is a raw-text condition, not a node condition.** `SUBGRAPH.search(block_text)` reports `subgraph blocks are not supported; split the diagram at a hand-off` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:57]. Anchoring at line start avoids a label that merely contains the word, and the check does not need to count nesting because every subgraph is rejected.

10. **Eight planted models prove the new rules.** Emoji label, reserved `end` ID, underscore ID, 81-character label, an undirected `---` edge, a dashed `-.->` edge, a `subgraph` block and an HTML-tag label; each must exit 1 [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:119]. Without them the self-test proves only the old six rules, and a regression in any new condition would pass unnoticed.

11. **The good fixture and all five shipped patterns survive.** `GOOD` uses camelCase IDs, short labels, one accent and solid arrows; the longest label in `flow-templates.md` is 27 characters and none of the patterns uses a dashed edge, an underscore or a subgraph [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:109] [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:39]. The change is additive at both sites.

12. **The rule wording should fold length and emoji into the existing label bullet.** Replace "Labels are one plain line" with "Labels are one plain line of at most 80 characters, with no HTML tag, emphasis markup or emoji", which keeps nine bullets rather than growing eleven and puts all label constraints in one place [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:101]. The edge and subgraph bullets are new; length and emoji are not.

13. **The check's docstring needs the same edit as the rule list.** It enumerates the rules today, so a new edge rule that is absent from the docstring makes `--help` and the self-test describe different contracts [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:16]. Update both in the same change or the docstring becomes the next stale mirror.

## Ruled Out

- A camelCase warning: needs a warning channel and a non-binary exit code.
- A bare `<`/`>` raw scan: collides with arrow operators.
- Counting subgraph nesting: rejected outright, so counting is wasted work.
- A separate emoji helper module: one regex used twice is smaller.

## Dead Ends

- Trying to keep the "first six rules" sentence by appending new rules after the read-back bullet: that would put a model rule in the read-back half and misstate the gate. Reordering is the only coherent option.

## Edge Cases

- Ambiguous input: a label that legitimately contains `<` as prose, such as "value < 5"; the HTML-tag regex ignores it, which is the right outcome.
- Contradictory evidence: none.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- Follow-on: what exact text changes, and in what order? Nine bullets, two new, one reworded, one sentence recalculated, docstring matched.
- Follow-on: do the shipped patterns still pass? Yes, by inspection.

## Questions Remaining

- None for the checker. The remaining iterations test the ranking and the write-route rows.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md`

## Assessment

- New information ratio: 0.60 (three new implementation facts: exact-match reserved IDs, HTML-tag scan, cleaned-label length; the rest are refinements of iterations 12–13)
- Questions addressed: implementation text, rule ordering
- Questions answered: both above

## Reflection

- What worked and why: writing the actual conditions exposed two mistakes in the earlier recommendations — case-insensitive reserved matching and a bare-angle-bracket scan — before either reached a plan.
- What did not work and why: the first draft appended new bullets at the end, which broke the check/read-back split; reordering fixed it.
- What I would do differently: draft the rule list before the code, since the doc's ordering constrains what the check must own.

## Recommended Next Focus

Iteration 15: the write-route rows — page rule, uncertain-call reconciliation, `fileKey` reuse and containment — written as replacement text for `flow-mode.md` and the two mirrors, with the manual parity note each one needs.

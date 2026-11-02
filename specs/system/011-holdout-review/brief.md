You are a fresh reviewer. Review and advise. Edit nothing outside AI Systems/Product Owner/specs/011-holdout-review/, run no sync compiler, commit nothing. Read-only commands and gate runs are fine.

Repo: /Users/michelkerkmeester/MEGA/Development/AI Systems.

A held-out test was just run against the Product Owner skill. A source the skill had never seen was written by hand, and a fresh Sonnet at high effort wrote a Story from it. Judge both the result and the rules that produced it, and say what should change.

Read, in this order:
1. The source: "Product Context/z — Product Owner/Story Drafts/Creator - Deals - Saved Deals Shelf/context.md"
2. The result: "AI Systems/Product Owner/export/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md"
3. The rules that govern them: AI Systems/Product Owner/sk-product-owner/references/story-mode.md sections 1, 3, 4 and 9, and sk-product-owner/assets/story-template.md
4. The two commits that set the current Requirements rule: git show ba2bec3 and git show 095479a
5. The investigation those commits came from: AI Systems/Product Owner/specs/010-requirements-bloat/findings.md
6. For comparison, three stories written from real sources under AI Systems/Product Owner/export/Story Drafts/, including "Highlights - Onboarding - Instagram ReAuth" and "Creator - Onboarding - Social Relink Flow"

The source was written with deliberate traps, one per rule that changed. Judge how many held:
- hard values that must survive verbatim: 24px, 44x44, 2 columns, h3, 24px spacing, a 50 cap, second menu item
- copy the source quotes, which must appear in backticks: "Saved to your shelf", "Nothing saved yet", "Browse deals"
- copy the source only paraphrases: the empty-state body, written as "Body explains that bookmarking a deal keeps it here". Under the current rule this must be struck or pointed at the design, and it survived into the artifact unchanged. Explain why the rule failed on it when it caught the four equivalents in the ReAuth story
- two reuse maps, which must become constraints
- a cross-ticket dependency on a Deal expiry ticket, which must be carried rather than invented
- a pattern reference to the Highlights delete warning, which must point rather than restate
- an explicit out-of-scope line about push notifications, where nobody asked for a delivery view

Then advise, with evidence and exact text:
1. The one surviving paraphrase. Give the smallest rule change that catches it without misfiring on a legitimate constraint. State plainly if the answer is a named phrase list rather than a principle, and give the list.
2. The out-of-scope line. The source says push notifications are out of scope and the requester asked for no delivery view, and the artifact put it in Requirements as a Notifications group. Say where it belongs: a Requirements constraint, a forced Delivery section, or dropped. Justify against the current opt-in Delivery rule.
3. Judge every other section of the artifact against the rules, not only Requirements: the H1, the About umbrella, Problem, Solution as a decision rather than a preview, Expected outcomes, the six acceptance criteria and whether any holds a value that Requirements should own, and the absent Delivery.
4. The output path. The artifact landed at export/Story Drafts/<name>/<name>.md because the source sat in a folder of that name. The Story Draft kind was retired, so that path convention no longer means anything. Say what the path should be and which file states it.
5. Anything in the current rules that is now redundant, contradictory or unreachable after today's four changes to the Requirements contract, with the lines to cut.
6. Whether this source is worth keeping as a permanent held-out fixture, and if so where it should live and what should reference it so a future rule change is tested against it rather than against a source the model has already seen.

Write the report to AI Systems/Product Owner/specs/011-holdout-review/findings.md and also print it. Rank anything you would change as P0 to P3 with file, line, current text and replacement. Prose rules: no em dashes, no semicolons in prose, no curly quotes, bullets never end in a full stop. Factual, no praise.

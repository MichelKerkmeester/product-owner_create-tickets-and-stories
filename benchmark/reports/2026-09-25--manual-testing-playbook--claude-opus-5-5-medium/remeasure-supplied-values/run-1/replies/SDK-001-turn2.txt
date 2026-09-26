I updated the reference with all your changes, in the same file. The main change for you: the free-shipping banner item is gone. The banner says "over €50" but the rule gives free shipping at exactly €50.00, and that point came only from the context doc. Now that it's background only, I didn't think it belonged in the reference. It's still a real wording mismatch, so it may be worth raising separately.

Path: `export/001 - doc-promotion-stacking.md`
Verified: read-back succeeded; 163 lines
HVR self-scan: 0 hard blockers. Fixed: none in this pass. Kept with reason: em dashes in the `**Term** — definition` bullets and the `Status: … — …` lines, which are the two formats the Doc rules allow.

- **Readers and purpose:** the Overview now names CS agents and Checkout engineers as the readers. It says the reference predicts the discount on any cart except the four open cases, which it lists.
- **Merchandisers and Admin:** I removed the merchandiser reader and the Admin setup line. The glossary no longer says where promotions are set up. The one remaining Admin mention is the note's own line that older orders still show two codes there.
- **Governing source:** the source list says the rules note governs every rule. The context doc is linked as background only, so all rule wording now comes from the note.
- **Retired two-codes rule:** it keeps its retired label, and the status line now says CS keeps it to explain and refund orders placed before 2026-05-01. The section now opens with the refund behavior: a refund on a two-code order splits the discount across both codes, which today's one-code rules wouldn't predict.

**Quality summary**
- **Source safety:** pass. Every rule traces to the rules note, and current, retired and open cases are each labelled.
- **Shape:** pass. It's still a behavior reference.
- **ClickUp layout:** pass. It follows the ClickUp formatting rules, with no spacer headings in the file.
- **Readability and voice:** pass.

The two conclusions I flagged last time are still in: a 15% code after a 20% promotion equals 12% off the original price, and a code can push an order back under the free-shipping threshold. Tell me if you'd rather drop them.
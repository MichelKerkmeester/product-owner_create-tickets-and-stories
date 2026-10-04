Path: `export/fernhouse-save-card-draft.md`
Verified: read-back succeeded; 138 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the fixed labels `Given`/`When`/`Then`/`And` and `Mark as done, if the criteria are met` (template wording the synonym-cycling rule requires repeating), the subject-fixed triads `web, iOS and Android`, `card number, expiry and CVC`, the three stored card fields, and the three payment events (content lists rather than tic density), the two `TBD...` slots (card-exempted house token inside Delivery), and the supplied strings in backticks (`Save this card for next time`, `unchecked by default`, `You can save up to 5 cards`, `Card ending 7031`, `Expires 08/28`, `€150`, `£130`, `CVC`, `Remove this card?`, `Account > Payment methods`) preserved verbatim.

**Artifact kind:** Story (Barter house Story shape, not Epic).

**Quality summary:** Completeness, Clarity, Accuracy, Actionability, Relevance and Mechanism Depth all clear their floors. Every section the Story shape requires is present and populated from supplied material, the source's three surface groups are mirrored one-for-one in `#### Requirements`, and each acceptance criterion names the surface it verifies with the how left open.

**What changed**
*   Title reset to the house `{Persona} - {Area} - {Feature}` form: `Customer - Checkout - Save card for next time` (drops the `PRD -` prefix, adds the persona)
*   `#### Problem` / `#### Solution` pulled to H4, and `**Expected outcomes**` demoted from an H4 heading to the bold label the house shape uses, with the missing section-close divider added
*   Requirements rewritten as `- []` hard constraints with the source values intact, `**Checklist**` build steps dropped and folded into the requirement groups (checkbox, sixth-card refusal, saved-card list and CVC field, account screen and `Remove this card?` confirmation, events)
*   `1\.` acceptance criteria authored from scratch, since the source had none
*   `#### **References**` omitted (no links supplied)

**Two things to check before Checkout picks it up**
1.  The source checklist stored card `brand`, but the company constraint allows only a token, the last four digits and expiry, so the story carries the tighter company limit.
2.  The source's `Copy for a declined saved card TBD...` is carried as an `**Open:**` line, and the open question repeats under Delivery Rabbit holes. The source's wallet/bank exclusion also lands in No-gos. Both are additions from the source and company context, not invented requirements. The context draft itself is untouched.

**Summary:** Priya's draft is now a house-format Story, ready for the Checkout team. The hard values (5-card limit, `€150`/`£130` CVC step, exact label and card strings) sit in Requirements, and the outcomes are verified in six Given/When/Then criteria across web, iOS and Android. Say the word if you want the `**Open:**` copy question dropped, which would remove the forced Delivery section, or if you want this split into a Story plus its task breakdown.
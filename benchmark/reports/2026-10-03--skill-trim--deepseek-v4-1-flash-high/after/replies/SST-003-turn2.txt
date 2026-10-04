Path: `export/fernhouse-save-card-draft.md`
Verified: read-back succeeded; 147 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in the Delivery Estimation slot (the house placeholder the card exempts), and the full stops inside the declined-card message and `Remove this card?`, which are exact supplied copy in backticks.

**Quality summary:** all six quality checks clear their floor. The format gate passes with no blocking findings, and the only advisories are length caps on lines that carry supplied values or the source's own wording. The artifact is 1,195 words against the 1,400 Story budget. The kind is a Story, one feature area with requirements, and both supplied files are untouched (the draft still hashes to its fixture value).

Priya's draft is now a house-format Story titled `Customer - Checkout - Save card for next time`, with her checklist dissolved into `- []` constraint groups rather than carried as build steps. Your three answers landed: the declined message is quoted exactly, the `€150` and `£130` re-entry rules now read as the order total including shipping, and the three events stay unnamed, delegated to the Data team's tracking plan with the rule that each needs a tracking-plan row and a `DATA` task before an `FE` task sends it.

**Two decisions are still open**, each as an `**Open:**` line under its requirement and repeated in Rabbit holes, which is what forced a Delivery close:
*   Card brand storage, where the draft keeps `brand` and the Fernhouse context allows token, last four digits and expiry `and nothing else`. Lotte owns that rule, so I named her to settle it with Checkout
*   Expired cards in the account, which you did not answer, so I left whether they show under `Account > Payment methods` and count toward the 5-card limit open

**Additions you can strike:**
*   All six acceptance criteria, since the draft had none
*   The `**Stored card data**` items and the `No other card data is stored` constraint, taken from the company context rather than the draft
*   The tracking-plan and `DATA` task rule, also from the company context
*   Checkout product named as the expired-cards decider, and an added check that a removed card stops showing at checkout

One flag for Priya: I carried `Card ending 7031` and `Expires 08/28` exactly as she wrote them. They read as sample values, so confirm whether they are fixed copy. Next step is Lotte's brand-storage ruling, after which I can lift that `**Open:**` line and its Rabbit holes entry.
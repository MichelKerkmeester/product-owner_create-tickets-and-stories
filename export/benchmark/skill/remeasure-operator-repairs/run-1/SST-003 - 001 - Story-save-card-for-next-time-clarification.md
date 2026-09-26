# Save card for next time: questions before the Story rewrite

I'll restructure Priya's draft into the house Story shape and save it as `fernhouse-save-card-draft.md` in `export/`. Her source file stays untouched. The title will be `Customer - Checkout - Save card for next time`, and the build checklist comes out of Requirements. Before I draft, I need these decisions in one reply:

**1. Card brand vs the stored-data rule.** The draft shows the card brand logo and lists "token, brand, last four and expiry only" as the stored fields. The company context (Known constraints) says Fernhouse may store a card token, the last four digits and the expiry date, "and nothing else". Which should the Story follow?
- Drop the brand logo and store token, last four and expiry only
- Keep the brand logo, with the brand not stored by Fernhouse. Checkout decides how to get it, and I name that as an addition
- Carry it as an `**Open:**` line until someone rules on it. Who decides: Lotte, Priya or someone else?

**2. Declined saved card copy.** The draft ends on "Copy for a declined saved card TBD". Should I carry it as an `**Open:**` line with the owner who settles it? That also adds a `## Delivery` section with `TBD...` slots. Or should I leave it out of scope for this Story?

**3. Checklist items that carry constraints.** The remove action and its `Remove this card?` confirmation move into the Managing saved cards group. For the three events (card saved, card removed, order paid with a saved card), should I:
- Name them in the house `object_action` pattern, for example `card_saved`, `card_removed`, and confirm a name for the third
- Or require a tracking-plan row for each and leave the names to the Data team

**4. Expired cards outside checkout.** The draft hides expired cards at checkout. Do they still appear under `Account > Payment methods`, and do they count toward the limit of 5?

**5. Delivery section.** Apart from question 2, do you want Estimation, Rabbit holes and No-gos included, or should the Story end on Acceptance criteria?

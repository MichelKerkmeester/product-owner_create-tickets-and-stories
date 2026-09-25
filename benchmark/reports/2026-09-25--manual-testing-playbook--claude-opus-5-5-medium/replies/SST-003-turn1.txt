I've rebuilt Priya's draft as a house-format **Story**. The source file is untouched, and the new version is saved under the same filename.

Path: `export/fernhouse-save-card-draft.md`
Verified: read-back succeeded; 146 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in the two Delivery slots (the house placeholder, allowed by the style rules).

**Quality summary:** all six quality checks clear their minimum. Accuracy is the one to watch: two open questions are still in the Story, and the Checkout team shouldn't start those parts until they're answered.

**What changed**
- **Title:** changed to `Customer - Checkout - Save card for next time`. The export line above the title was dropped.
- **Checklist removed:** each item now appears either as a requirement or as an open question. There are new "Card data" and "Tracking" groups, and the remove button and `Remove this card?` confirmation went into "Managing saved cards".
- **Requirements split:** each bullet now holds one rule. Priya's values are carried over word for word.
- **Acceptance criteria added:** the draft had none, so I wrote five.

**Needs a decision before Checkout picks it up**
1. **Card brand conflicts with company policy.** The draft stores the card brand. The company context allows only the token, last four digits and expiry. I kept the company rule as the requirement and marked brand as open. Lotte owns that rule, so I've named her to decide with Checkout.
2. **No copy yet for a declined saved card.** This is marked as open, with Priya named to supply it.

These two open questions made me add a Delivery section at the end. Its Rabbit holes list both of them, and Estimation and No-gos are left as `TBD...`.

**Things I added that you can strike**
- All five acceptance criteria.
- A line saying `7031` and `08/28` stand for each card's own last four digits and expiry, since they read as sample values.
- The €150 threshold applies to NL, BE, DE and FR. I took that from the four euro markets in the company context.
- The Tracking rule that each event needs a tracking-plan row and a DATA task before any front-end task sends it. This comes from the company context.
- Lotte and Priya named as the people who settle the two open questions.

If ClickUp is connected here, I can push this as a task once you approve.
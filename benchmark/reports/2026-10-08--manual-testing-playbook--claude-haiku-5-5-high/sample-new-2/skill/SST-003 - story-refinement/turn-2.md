Nothing is drafted yet. Some of the questions in `export/001 - Story-save-card-clarification.md` are answered, but the card storage conflict and several others are still open. That file is unchanged.

**Recorded from your answers:**
- Declined-card copy is agreed: "This card was declined. Choose another card or enter a new one."
- The €150 and £130 CVC limits apply to the order total, including shipping.
- The three tracking events stay in as a requirement without names. The names come later from the Data team.

**Still open:**
- **Card storage (item 1):** The draft stores the card brand and shows a brand logo. The company context limits stored data to the token, last four digits and expiry date. Lotte, Head of Product, owns that context, so this needs her decision or a confirmed change to the context before I can write the Story.
- **Account screen owner (item 2):** Does Checkout or Storefront own `Account > Payment methods`?
- **Problem figures (item 3):** What source and date window support the 17% and 9% drop-off figures? Is the 68% claim about people or orders?
- **Build checklist (item 5):** Should the Story stand alone, or should the checklist split into child tasks?
- **Sample values (item 6):** Are `Card ending 7031` and `Expires 08/28` literal copy or example data?
- **Title and role (item 7):** Confirm `Customer - Checkout - Save card for next time` and the signed-in customer role.

Once those are answered, I'll write the Story with the declined-card copy and CVC wording. The unnamed events will carry an `**Open:**` line, which also adds a Delivery section.
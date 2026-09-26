# Save card for next time: clarification before the house Story

I'll restructure Priya's draft into the house Story shape. I'll keep a copy under its original basename and won't touch the source. I need these decisions in one reply before I draft:

**1. Card brand vs the stored-data rule:** The draft keeps the card brand and shows a brand logo at the payment step. The company context says Fernhouse may store a card token, the last four digits and the expiry date "and nothing else". Which wins?
*   Brand is cleared for storage, so the context doc is out of date and I keep brand and the logo
*   The context doc wins, so brand leaves the stored fields and the logo requirement drops or becomes an `**Open:**` line
*   Keep it as an `**Open:**` line owned by a named person

**2. CVC threshold basis:** `€150` / `£130` applies to "orders over". Is that the subtotal as the glossary defines it (after promotions, before shipping) or the order total including shipping? Does exactly `€150.00` skip the CVC?

**3. Declined saved card:** The draft leaves this copy `TBD...`. Do you have the string or an owner? If not, I carry it as an `**Open:**` line, and that opts in a `## Delivery` section with Estimation, Rabbit holes and No-gos, left `TBD...` where unknown.

**4. Build checklist:** A house Story holds no checklist. I'd move its hard values into Requirements (`Remove this card?`, a sixth card refused, token/last four/expiry only, guest checkout hidden) and drop the rest. Or do you want the Story with its tasks as a bundle? If so, is Priya's BE / FE Web / FE iOS / FE Android / FE all / DATA split the task list?

**5. Analytics:** The draft names three events without event names. Should I carry one requirement that points at the Data tracking plan, or do you have the `object_action` names? I won't invent them.

**6. Expired cards:** They're hidden at checkout. Do they still show under `Account > Payment methods` so the customer can remove them?

**7. Title and delivery view:** I plan to use `Customer - Checkout - Save card for next time`. Does that work? Since the Checkout team picks this up next, do you want the `## Delivery` section even if question 3 doesn't force it?

**8. References:** Do you have any Figma or ClickUp links to carry? Without links, References is omitted.

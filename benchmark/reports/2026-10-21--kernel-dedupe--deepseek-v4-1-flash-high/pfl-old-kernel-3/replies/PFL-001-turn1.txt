Flow Mode, user flow proposed, Standard energy. Sources read: Lotte's spec and `context/fernhouse-context.md`.

Two things before the questions. No Figma connector is reachable from this Project, so I cannot create a board in the Fernhouse Product plan. I can take this through the full intake and hand you the checked model as a Mermaid block instead, and say why each cut was made. Tell me if you would rather stop there.

## What your sources already settle

| Brief row | Value | Status |
|---|---|---|
| Scope | One alert request from a sold-out product page to one email. Restock and warehouse work sit outside it | captured |
| Entry | Product page of a sold-out item, customer taps `Notify me` | captured |
| Exit | The customer gets one email when the item is back in stock | captured |
| Decision | Signed in or guest, which is the only branch the spec states | captured |
| Actors | Customer (signed in or guest) and the system that saves the alert and sends the mail | captured |
| Sources and class | Lotte's spec: approved direction, with push alerts marked proposal. Company context: current behavior | captured |
| Reader and question | Not stated in either source | unasked |
| Outcome | Not stated in either source | unasked |
| States | Alert saved is named. What the customer sees at that moment is not | unasked |

The context fills in the surrounding behavior: customers buy on web, iOS and Android, `accounts-service` holds sign-in and the web wishlist, `catalog-service` holds stock synced from the warehouse, and email leaves through the email delivery provider.

## Round one

**Question 1, the reader and the question the board answers**

Reading: Lotte owns the spec, and the change lands on a product page with an emailed follow-up. Neither source names the team that owns the alert itself.

Recommended reader: the team building the product page change, with design and the team that owns the email attached, mixed audience, read on a laptop.

Recommended question: *Which screens does a customer pass through from tapping `Notify me` on a sold-out product page to the one email, and where do they choose?*

Recommended type: user flow, because the question is screens and one choice. If you would rather see the alert's own life instead, from requested to notified to expired, that is a state diagram and a different board.

Why: the spec is written as a walk through what a customer does, so a user flow can be read against it screen by screen.

Recommended outcome: the reader agrees the screen list and sees that the guest branch is the only place the flow adds a screen.

**Question 2, what this board must not do**

Reading: the spec marks push alerts as "a proposal only, nobody has agreed them yet", and the context lists promotions push as already live in the apps, which is a different feature.

Recommended: the board carries no push alert step and no restock, warehouse or merchandising work.

Why: a proposal drawn beside agreed behavior reads as shipped, and the reader has no way to tell the two apart on a board.

## Next round

Round two asks entry, exit and actors, and the sources leave two spots open there. What the customer sees once a guest alert is saved, and whether the board carries the email itself or stops at it being sent.

Answer either question above, or say go and I take both recommendations.
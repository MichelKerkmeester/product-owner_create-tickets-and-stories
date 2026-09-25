````markdown
# Customer - Checkout - Save card for next time

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers can save a card at checkout and pay with it on their next order without typing the card number again. This covers the card form in checkout on web, iOS and Android, saved cards at the payment step, and a place in the account to see and remove saved cards.

### Problem
* * *
Every card payment today means typing the full card number, expiry and CVC, even for a customer on their tenth order. In the apps the payment step loses 17% of the customers who reach it, against 9% on web, and card entry is where most of them stop. Returning customers place 68% of app orders, so most of the people typing their card again have done it before.

### Solution
* * *
A signed-in customer ticks a box on the card form to keep the card, and on the next order their saved cards come first at the payment step. Saving is always the customer's choice, so no card is kept without them asking. Customers see and remove their saved cards from their account.

#### **Expected outcomes**
* * *
*   Returning app customers get through the payment step faster and drop off less
*   Fewer repeat orders are abandoned at card entry
*   No new CS contacts about cards being kept without the customer asking
* * *
##   

## Requirements
* * *
**Saving a card**
* * *
*   The checkbox label is `Save this card for next time`, shown under the card fields
*   The checkbox is unchecked by default
*   The checkbox is on the card form on web, iOS and Android
*   Only signed-in customers see the checkbox. Guest checkout never saves a card
*   A customer can hold at most `5` saved cards. At the limit the checkbox is replaced by `You can save up to 5 cards`
*   The back end refuses a sixth card
*   Cards only. Wallet and bank payments stay as they are

**Paying with a saved card**
* * *
**Open:** the copy for a declined saved card is not written yet. Priya, as Checkout PM, settles it.

*   Saved cards show first at the payment step
*   Each saved card shows in the format `Card ending 7031`, with `Expires 08/28` under it and the card brand logo on the left
*   Orders over `€150`, or `£130` in the UK, ask for the `CVC` again before paying
*   Expired cards are hidden at checkout

**Managing saved cards**
* * *
*   Saved cards live under `Account > Payment methods` on web, iOS and Android
*   Each saved card has a remove button that asks `Remove this card?` before the card is removed

**Card data**
* * *
**Open:** the draft stores the card brand, but the company card data rule allows only the card token, the last four digits and the expiry date. Checkout agrees with Lotte, who owns the company context, whether the brand logo comes from the payment provider when the card is shown or the rule changes.

*   Card details stay with the payment provider. The account stores the provider's card token, the last four digits and the expiry date, and nothing else

**Tracking**
* * *
*   Events fire when a card is saved, when a card is removed and when an order is paid with a saved card
*   Event names follow the `object_action` convention, and each event has a row in the Data team's tracking plan and a DATA task before any client sends it
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Card form
* * *
1\. **A signed-in customer keeps a card only when they ask to**
* * *
*   **Given** a signed-in customer on the card form on web, iOS or Android
*   **When** they tick the save checkbox and pay
*   **Then** the card is waiting for them at the payment step on their next order and in their account
*   **And** a card paid with the box left unticked is not kept
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Guests are never offered to save a card**
* * *
*   **Given** a customer checking out as a guest
*   **When** they reach the card form
*   **Then** no save option shows and the card is not kept after payment
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A customer at the saved card limit can still pay**
* * *
*   **Given** a signed-in customer who already has the maximum number of saved cards
*   **When** they reach the card form
*   **Then** they are told they have reached the limit instead of seeing the save option
*   **And** they can pay with a new card without it being kept
* * *
- [ ] _Mark as done, if the criteria are met_

#### Payment step
* * *
4\. **A returning customer pays without typing their card number**
* * *
*   **Given** a signed-in customer with a saved card that has not expired
*   **When** they reach the payment step
*   **Then** their saved cards come first and they can pay with one without typing the card number or expiry
*   **And** on an order above their market's CVC threshold they confirm the CVC before the payment goes through
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Expired cards stay out of the payment step**
* * *
*   **Given** a signed-in customer with a saved card past its expiry date
*   **When** they reach the payment step
*   **Then** that card does not show
* * *
- [ ] _Mark as done, if the criteria are met_

#### Account
* * *
6\. **A customer removes a card they no longer want kept**
* * *
*   **Given** a signed-in customer with a saved card
*   **When** they remove it from their payment methods and confirm
*   **Then** the card no longer shows in their account or at the payment step
*   **And** backing out of the confirmation leaves the card in place
* * *
- [ ] _Mark as done, if the criteria are met_

#### Tracking
* * *
7\. **Saved card use shows up in reporting**
* * *
*   **Given** the Data team reading the analytics tool
*   **When** a customer saves a card, removes a card or pays with a saved card
*   **Then** each action appears as its own event carrying the standard event properties
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   The copy for a declined saved card is not written yet, so the payment step's decline state cannot be finished until Priya settles it
*   Storing the card brand conflicts with the card data rule, which allows only the card token, the last four digits and the expiry date

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
````

Export-equivalent path: `export/fernhouse-save-card-draft.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: two `TBD...` slots (the fixed placeholder allowed in Delivery), and Given/When/Then repeated in every criterion (fixed labels).

**Artifact kind:** Story. You said to restructure as needed, so I rebuilt Priya's draft in the house format instead of only tidying it.

**Quality:** Passes the house format and heading depth checks. Every value in the draft made it into Requirements unchanged: labels, the 5-card limit, `€150`/`£130`, `Remove this card?` and `Account > Payment methods`.

**What changed from the draft**
- **Title and header:** the `PRD -` prefix is gone, the title now follows the context's `Customer - Checkout - …` pattern, and Priya's export header line is dropped.
- **Checklist removed:** each item was moved into Requirements:
  - "BE: refuse a sixth card" is now a bullet under Saving a card.
  - The per-platform checkbox items became one platform bullet.
  - `Remove this card?` went under Managing saved cards.
  - Storage became a new Card data group.
  - The event item became a new Tracking group.
- **Acceptance criteria:** the draft had none. I wrote seven, grouped by screen.
- **Delivery section:** added because the two open items below require it. Estimation and No-gos stay `TBD...`.

**Needs a decision before pickup**
- **Card brand vs the card data rule:** the draft stores the card brand, but the company context allows only the token, last four digits and expiry. The brand logo at the payment step depends on it. I kept to the context rule and marked this Open rather than choosing an approach.
- **Declined saved card copy:** still not written. It's marked Open under Paying with a saved card.

**Things I added that the draft didn't say** (remove any you don't want)
- The Tracking group's second bullet (the `object_action` naming and a tracking plan row before any client sends the event) comes from the company context.
- Criterion 3's "can still pay with a new card without it being kept."
- Criterion 6's "backing out of the confirmation leaves the card in place."
- Criterion 7 as a whole.

**Worth confirming with Priya**
- `Card ending 7031` and `Expires 08/28` look like sample values. I kept them and labelled the line as a format.
- The draft hides expired cards at checkout but doesn't say whether they still show under Payment methods.

Next step: settle the two open items with Priya and Lotte, then hand it to Checkout.
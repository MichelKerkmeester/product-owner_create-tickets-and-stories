# Customer - Checkout - Save card for next time

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers can save a card at checkout and pay with it on their next order without typing the card number again. This covers the card form in checkout on web, iOS and Android, the saved card at the payment step, and a place in the account to see and remove saved cards.

### Problem
* * *
Every card payment today means typing the full card number, expiry and CVC, even for a customer on their tenth order. In the apps the payment step loses 17% of the customers who reach it, against 9% on web, and card entry is where most of them stop. Returning customers place 68% of app orders, so most of the people typing their card again have done it before.

### Solution
* * *
A signed-in customer chooses to keep a card when they pay, and the next time they reach the payment step that card is waiting for them, so a repeat order no longer starts with card entry. Saving is always the customer's choice, because a card kept without asking costs more trust than the typing it saves. The card itself stays with the payment provider, and customers manage their saved cards from their account.

#### **Expected outcomes**
* * *
*   Returning app customers get through the payment step faster and drop off less
*   Fewer repeat orders are abandoned at card entry
*   No new CS contacts about cards being kept without the customer asking
##   

## Requirements
* * *
**Saving a card**
* * *
*   The checkbox appears on the card form in checkout on Web, iOS and Android
*   The checkbox label is `Save this card for next time`, shown under the card fields
*   The checkbox is unchecked by default
*   Only signed-in customers see the checkbox
*   Guest checkout has no card saving
*   A customer can hold 5 saved cards
*   At the limit the checkbox is replaced by `You can save up to 5 cards`
*   The limit of 5 holds for the account on every platform, so a sixth card is refused
*   Only cards can be saved, and wallet and bank payments stay as they are

**Card data**
* * *
**Open:** The draft keeps the card brand next to the token, but the company card-data rule allows the token, the last four digits and the expiry date, and nothing else. Lotte, as owner of that rule, decides with Checkout whether brand may be stored or whether the brand logo at the payment step has to come from the payment provider.

*   Fernhouse stores the payment provider's card token, the last four digits and the expiry date against the account, and nothing else

**Paying with a saved card**
* * *
*   Saved cards show first at the payment step
*   Each saved card reads `Card ending 7031` with `Expires 08/28` under it, where 7031 and 08/28 stand for that card's own last four digits and expiry
*   The card brand logo sits on the left of each saved card
*   Orders whose total including shipping is over `€150` in the NL, BE, DE and FR markets ask for the `CVC` again before paying
*   Orders whose total including shipping is over `£130` in the UK ask for the `CVC` again before paying
*   Expired cards are hidden at checkout
*   A declined saved card shows `This card was declined. Choose another card or enter a new one.`

**Managing saved cards**
* * *
*   Saved cards live under `Account > Payment methods` on web and in the apps
*   Each saved card has a remove button
*   Removing a card asks `Remove this card?` before the card is removed

**Tracking**
* * *
*   Three events are tracked: card saved, card removed and order paid with a saved card
*   Each event gets a row in the Data team's tracking plan and a DATA task before any FE task sends it
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Saving a card
* * *
1\. **A card is kept only when the customer asks for it**
* * *
*   **Given** a signed-in customer is paying by card in checkout
*   **When** they tick the save option and the payment goes through
*   **Then** the card is offered at the payment step on their next order
*   **And** a customer who leaves the option unticked, or checks out as a guest, has no card kept
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The saved-card limit is clear before the customer tries to pass it**
* * *
*   **Given** a signed-in customer already holds the maximum number of saved cards
*   **When** they reach the card form in checkout
*   **Then** they are told they have reached the limit instead of being offered the save option
*   **And** no further card is added to their account on any platform
* * *
- [ ] _Mark as done, if the criteria are met_

#### Paying with a saved card
* * *
3\. **A returning customer pays without typing their card again**
* * *
*   **Given** a signed-in customer has a saved card that has not expired
*   **When** they reach the payment step
*   **Then** their saved cards come first and they can pay with one without entering the card number or expiry
*   **And** when the order total including shipping is above the CVC threshold for their market, they confirm the CVC before the payment goes through
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A declined saved card leaves the customer a way to pay**
* * *
*   **Given** a signed-in customer pays with a saved card
*   **When** the card is declined
*   **Then** they are told the card was declined and can pay with another saved card or a new one without leaving the payment step
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **An expired card is never offered**
* * *
*   **Given** a signed-in customer has a saved card whose expiry has passed
*   **When** they reach the payment step
*   **Then** that card is not offered and the customer can pay with another saved card or a new one
* * *
- [ ] _Mark as done, if the criteria are met_

#### Managing saved cards
* * *
6\. **A customer can remove a saved card and it stays gone**
* * *
*   **Given** a signed-in customer has a saved card
*   **When** they remove it from their account and confirm
*   **Then** the card no longer appears in their account or at the payment step on web, iOS or Android
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

*   Card brand storage: the draft stores brand, the card-data rule does not allow it, and the brand logo at the payment step depends on how Lotte and Checkout settle it

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *

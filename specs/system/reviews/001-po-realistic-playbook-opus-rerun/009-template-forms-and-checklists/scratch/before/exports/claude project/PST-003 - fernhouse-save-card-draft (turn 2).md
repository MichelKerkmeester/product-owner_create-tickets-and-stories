# Customer - Checkout - Save card for next time

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers can save a card at checkout on web, iOS and Android, reuse it without retyping, and remove it in their account.

### Problem
* * *
Every card payment means typing the card number, expiry and CVC, even on a tenth order. The app payment step loses 17% against 9% on web, mostly at card entry, and returning customers place 68% of app orders.

### Solution
* * *
A signed-in customer ticks a box to keep the card, and no card is kept unless asked.

#### **Expected outcomes**
* * *
*   Returning app customers pay faster, and fewer repeat orders stop at card entry
*   No new CS contacts about cards saved unasked
* * *
##   

## Requirements
* * *
**Saving a card**
* * *
*   `Save this card for next time` sits unchecked under the card fields on web, iOS and Android
*   Only signed-in customers see it, and guests never save a card
*   A customer holds at most `5` saved cards, and at the limit `You can save up to 5 cards` replaces the checkbox
*   The back end refuses a sixth card
*   Only cards are covered, not wallet or bank payments

**Paying with a saved card**
* * *
*   Saved cards show first at the payment step
*   Each shows as `Card ending 7031`, with `Expires 08/28` under it and the brand logo on the left
*   Orders whose total including shipping is over `€150`, or `£130` in the UK, ask for the `CVC` again before paying
*   Expired cards are hidden at checkout
*   A declined saved card shows `This card was declined. Choose another card or enter a new one.`

**Managing saved cards**
* * *
*   Saved cards live under `Account > Payment methods` on web, iOS and Android
*   Each has a remove button asking `Remove this card?` first

**Card data**
* * *
**Open:** the draft stores the card brand, which the company card data rule forbids. Checkout agrees with Lotte, who owns the company context, whether the provider supplies the logo at display time or the rule changes.

*   Card details stay with the payment provider, and the account keeps only its card token, last four digits and expiry date

**Tracking**
* * *
*   Events fire when a card is saved, removed or used to pay
*   The Data team names the three events
*   Before any client sends an event, it needs a Data team tracking plan row and a DATA task
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Card form
* * *
1\. **A signed-in customer keeps a card only when they ask to**
* * *
*   **Given** a signed-in customer at the card form on web, iOS or Android
*   **When** they tick save and pay
*   **Then** the card waits at their next payment step and in their account
*   **And** a card paid unticked is not kept
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Guests are never offered to save a card**
* * *
*   **Given** a guest customer
*   **When** they reach the card form
*   **Then** no save option shows and the card is not kept
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A customer at the saved card limit can still pay**
* * *
*   **Given** a signed-in customer at the saved card limit
*   **When** they reach the card form
*   **Then** the limit message replaces the save option
*   **And** they can pay with a new card without keeping it
* * *
- [ ] _Mark as done, if the criteria are met_

#### Payment step
* * *
4\. **A returning customer pays without typing their card number**
* * *
*   **Given** a signed-in customer with an unexpired saved card
*   **When** they reach the payment step
*   **Then** saved cards come first and they pay with one without typing the number or expiry
*   **And** above their market's CVC threshold, they confirm the CVC first
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Expired cards stay out of the payment step**
* * *
*   **Given** a signed-in customer with an expired saved card
*   **When** they reach the payment step
*   **Then** that card does not show
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **A declined saved card leaves the customer a way to pay**
* * *
*   **Given** a signed-in customer paying with a saved card
*   **When** the card is declined
*   **Then** they are told the card was declined
*   **And** they can pick another saved card or a new one without leaving the payment step
* * *
- [ ] _Mark as done, if the criteria are met_

#### Account
* * *
7\. **A customer removes a card they no longer want kept**
* * *
*   **Given** a signed-in customer with a saved card
*   **When** they remove it and confirm
*   **Then** it is gone from their account and the payment step
*   **And** backing out keeps it
* * *
- [ ] _Mark as done, if the criteria are met_

#### Tracking
* * *
8\. **Saved card use shows up in reporting**
* * *
*   **Given** the Data team in the analytics tool
*   **When** a customer saves, removes or pays with a saved card
*   **Then** each action is its own event with the standard event properties
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

*   Storing the card brand conflicts with the card data rule

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *

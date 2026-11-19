# Customer - Checkout - Save card for next time

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers can save a card at checkout and pay with it on their next order without typing the card number again. This story covers the card form in checkout on web, iOS and Android, saved cards at the payment step, and a place in the account to see and remove saved cards.

### Problem
* * *
Today every card payment means typing the full card number, expiry and CVC, even for a customer placing their tenth order. In the apps, the payment step loses 17% of the customers who reach it, compared with 9% on web, and card entry is where most of them stop. Returning customers place 68% of app orders, so most of the people typing their card details again have typed them before.

### Solution
* * *
At checkout, a signed-in customer can choose to keep a card. On their next order, their saved cards are ready at the payment step. The card itself stays with the payment provider, and Fernhouse keeps only what it needs to show the card back to the customer. Customers see and remove saved cards from their account, so a card is only kept for as long as the customer wants.

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
*   The checkbox label is `Save this card for next time`, shown under the card fields and unchecked by default
*   Only signed-in customers see the checkbox, on web, iOS and Android. Saving is not available in guest checkout
*   A customer can hold `5` saved cards. At the limit, the checkbox is replaced by `You can save up to 5 cards`
*   The service refuses a sixth saved card, whatever the client sends
*   Cards only. Wallet and bank payments stay as they are
*   For each saved card, Fernhouse stores the payment provider's card token, the last four digits and the expiry date, and nothing else

**Paying with a saved card**
* * *
**Open:** Fernhouse may not store the card brand, so it is not yet decided where the brand logo gets its brand from. Checkout settles this before the FE tasks start.

*   Saved cards show first at the payment step as `Card ending 7031`, with `Expires 08/28` under it and the card brand logo on the left
*   Orders over `€150`, or `£130` in the UK, ask for the `CVC` again before paying
*   The `€150` and `£130` limits apply to the order total including shipping
*   Expired cards are hidden at checkout
*   A declined saved card shows `This card was declined. Choose another card or enter a new one.`

**Managing saved cards**
* * *
*   Saved cards live under `Account > Payment methods` on web and in the apps
*   Each saved card has a remove button, and removing asks `Remove this card?` before the card is removed

**Tracking**
* * *
*   Three events are needed: card saved, card removed and order paid with a saved card. Their names come from the Data team's tracking plan
*   Each event needs a tracking plan row and a DATA task before any FE task sends it
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Saving a card
* * *
1\. **A card is kept only when the customer asks for it**
* * *
*   **Given** a signed-in customer paying by card at checkout
*   **When** they tick the save checkbox and the order is paid
*   **Then** the card is ready to pay with at the payment step on their next order
*   **And** a customer who leaves the box unticked, or checks out as a guest, has no card kept
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The saved card limit holds**
* * *
*   **Given** a customer who already has the maximum number of saved cards
*   **When** they pay by card at checkout
*   **Then** they see the limit message where the checkbox would be, and they can still pay with the card they typed
*   **And** no route on any surface saves one more card
* * *
- [ ] _Mark as done, if the criteria are met_

#### Paying with a saved card
* * *
3\. **A returning customer pays without typing the card number**
* * *
*   **Given** a signed-in customer with a saved card that has not expired
*   **When** they reach the payment step
*   **Then** their saved cards are listed before other payment methods, and they can pay with one without typing the card number
*   **And** expired saved cards are not offered
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Larger orders ask for the CVC again**
* * *
*   **Given** a customer paying with a saved card
*   **When** the order total including shipping is over the CVC limit for their market
*   **Then** they enter the CVC before the payment goes through
*   **And** an order below the limit is paid without the CVC
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A declined saved card leaves the customer a way to pay**
* * *
*   **Given** a customer paying with a saved card
*   **When** the payment provider declines the card
*   **Then** they see the declined message and can pay with another saved card or a new card in the same checkout
* * *
- [ ] _Mark as done, if the criteria are met_

#### Managing saved cards
* * *
6\. **A customer can remove a saved card**
* * *
*   **Given** a signed-in customer with a saved card in their account
*   **When** they remove it and confirm
*   **Then** the card is gone from their account and is no longer offered at checkout
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

*   Where the brand logo gets its brand from, because the card data rule does not allow Fernhouse to store the brand

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   Saving a card in guest checkout
*   Saving wallet or bank payments
* * *

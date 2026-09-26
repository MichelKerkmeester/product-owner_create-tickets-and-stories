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
A signed-in customer chooses to keep a card when they pay, and the next time they check out that card is waiting at the top of the payment step. Saving is always the customer's choice, because a card kept without asking costs more trust than the typing it saves. The card itself stays with the payment provider, and customers manage their saved cards from their account.

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
*   The checkbox label is `Save this card for next time`, shown under the card fields and `unchecked by default`
*   The checkbox is on the checkout card form on web, iOS and Android
*   Only signed-in customers see it. No saving in guest checkout
*   A customer can hold 5 saved cards. At the limit the checkbox is replaced by `You can save up to 5 cards`
*   A sixth card is refused by the service as well as hidden in the client
*   Cards only. Wallet and bank payments stay as they are

**Stored card data**
* * *
*   Card data stays with the payment provider. Fernhouse stores the card token, the last four digits and the expiry date, and nothing else

**Paying with a saved card**
* * *
**Open:** the card brand logo needs the brand, which the stored-data rule does not allow Fernhouse to keep. Lotte owns that rule in the company context, so the logo waits on her ruling.

*   Saved cards show first at the payment step as `Card ending 7031` with `Expires 08/28` under it
*   An order whose total including shipping is over `€150`, or over `£130` in the UK, asks for the `CVC` again before paying
*   Expired cards are hidden at checkout
*   A declined saved card shows `This card was declined. Choose another card or enter a new one.`

**Managing saved cards**
* * *
**Open:** the draft does not say whether expired cards appear under `Account > Payment methods` or count toward the limit of 5. Checkout product settles it before the account tasks are cut.

*   Saved cards live under `Account > Payment methods` on web and in the apps
*   Each saved card has a remove action that asks `Remove this card?` before removing it

**Tracking**
* * *
*   Three events: card saved, card removed and order paid with a saved card
*   Event names are set by the Data team and are not fixed in this Story
*   Each event needs a row in the Data team's tracking plan and a DATA task before any FE task sends it
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Checkout
* * *
1\. **Signed-in customers choose whether to keep a card**
* * *
*   **Given** a signed-in customer is paying by card on web, iOS or Android
*   **When** they complete the payment with the save option ticked
*   **Then** the card is kept for their next order, and a card is never kept when the option is left unticked
*   **And** a guest checking out never sees the option
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A saved card pays the next order without retyping the card number**
* * *
*   **Given** a signed-in customer has at least one saved card that has not expired
*   **When** they reach the payment step on their next order
*   **Then** their saved cards are offered before any other payment method, and they can pay with one without typing the card number
*   **And** an expired card is never offered
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Higher-value orders confirm the card holder**
* * *
*   **Given** a customer pays with a saved card
*   **When** the order total including shipping is over the market's CVC threshold
*   **Then** the order is paid only after the customer enters the CVC
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A declined saved card leaves the customer a way to pay**
* * *
*   **Given** a customer pays with a saved card
*   **When** the payment provider declines it
*   **Then** no order is placed, the customer is told the card was declined, and they can pick another card or enter a new one without leaving checkout
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Customers at the card limit know why they cannot save more**
* * *
*   **Given** a signed-in customer already holds the maximum number of saved cards
*   **When** they pay with a new card
*   **Then** they cannot save it, on any platform, and they are told the limit instead of seeing the save option
* * *
- [ ] _Mark as done, if the criteria are met_

#### Account
* * *
6\. **Customers control which cards are kept**
* * *
*   **Given** a signed-in customer has saved cards
*   **When** they open their payment methods in the account on web, iOS or Android
*   **Then** they see every saved card and can remove one after confirming
*   **And** a removed card is no longer offered at checkout on any platform
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

*   The card brand logo at the payment step conflicts with the stored-data rule and waits on Lotte's ruling
*   Whether expired cards appear under `Account > Payment methods` and count toward the limit of 5 is not decided

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No saving cards in guest checkout
*   No change to wallet and bank payments
* * *

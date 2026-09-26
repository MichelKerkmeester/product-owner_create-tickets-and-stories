# Customer - Checkout - Save card for next time

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers can save a card at checkout and reuse it, across the card form on web, iOS and Android, the payment step and the account.

#### Problem
* * *
Each card payment means typing number, expiry and CVC. The app payment step loses 17% against 9% on web, mostly at card entry, and returning customers place 68% of app orders.

#### Solution
* * *
Saving is always the customer's choice, because a card kept without asking costs more trust than the typing it saves. The card itself stays with the payment provider.

**Expected outcomes**
* * *
*   Returning app customers pay faster and drop off less
*   Fewer repeat orders abandoned at card entry
*   No CS contacts about cards kept unasked
##   

## Requirements
* * *
**Saving a card**
* * *
- [] A checkbox on the checkout card form on Web, iOS and Android, unchecked by default
- [] Label `Save this card for next time`, under the card fields
- [] Only signed-in customers see it, with no saving at guest checkout
- [] An account holds 5 saved cards across platforms, and a sixth is refused
- [] At the limit the checkbox becomes `You can save up to 5 cards`
- [] Only cards, with wallet and bank payments unchanged

**Card data**
* * *
**Open:** The draft stores card brand, but the company card-data rule allows only token, last four digits and expiry date. Lotte, the rule's owner, decides with Checkout whether brand may be stored or the logo must come from the payment provider.

- [] Fernhouse stores only the provider's card token, last four digits and expiry date against the account

**Paying with a saved card**
* * *
- [] Saved cards show first at the payment step
- [] Each reads `Card ending 7031` over `Expires 08/28`, with 7031 and 08/28 as that card's values
- [] The card brand logo sits on the left
- [] Orders over `€150` with shipping in NL, BE, DE and FR ask for the `CVC` again
- [] Orders over `£130` with shipping in the UK ask for the `CVC` again
- [] Expired cards are hidden at checkout
- [] A declined card shows `This card was declined. Choose another card or enter a new one.`

**Managing saved cards**
* * *
- [] Saved cards live under `Account > Payment methods` on web and apps
- [] Each has a remove button
- [] Removing a card first asks `Remove this card?`

**Tracking**
* * *
- [] Track card saved, card removed and order paid with a saved card
- [] Each needs a Data team tracking plan row and a DATA task before any FE task sends it
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Saving a card
* * *
1\. **A card is kept only when the customer asks for it**
* * *
*   **Given** a signed-in customer pays by card
*   **When** they tick save and payment succeeds
*   **Then** the card is offered at their next payment step
*   **And** an unticked option or guest checkout keeps no card
* * *
- [] _Mark as done, if the criteria are met_

2\. **The saved-card limit is clear before the customer tries to pass it**
* * *
*   **Given** a signed-in customer holds the maximum saved cards
*   **When** they reach the card form
*   **Then** they see the limit message instead of the save option
*   **And** no card is added on any platform
* * *
- [] _Mark as done, if the criteria are met_

#### Paying with a saved card
* * *
3\. **A returning customer pays without typing their card again**
* * *
*   **Given** a customer with an unexpired saved card
*   **When** they reach the payment step
*   **Then** saved cards come first, payable without number or expiry
*   **And** above their market's CVC threshold including shipping, they confirm the CVC first
* * *
- [] _Mark as done, if the criteria are met_

4\. **A declined saved card leaves the customer a way to pay**
* * *
*   **Given** a customer pays with a saved card
*   **When** the card is declined
*   **Then** they see the decline and can use another saved or new card on the same step
* * *
- [] _Mark as done, if the criteria are met_

5\. **An expired card is never offered**
* * *
*   **Given** a customer with an expired saved card
*   **When** they reach the payment step
*   **Then** it is not offered, and another saved or new card works
* * *
- [] _Mark as done, if the criteria are met_

#### Managing saved cards
* * *
6\. **A customer can remove a saved card and it stays gone**
* * *
*   **Given** a saved card
*   **When** the customer removes it and confirms
*   **Then** it no longer appears in the account or at the payment step on web, iOS or Android
* * *
- [] _Mark as done, if the criteria are met_
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

*   Card brand storage: the card-data rule forbids brand, so the logo waits on Lotte and Checkout

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *

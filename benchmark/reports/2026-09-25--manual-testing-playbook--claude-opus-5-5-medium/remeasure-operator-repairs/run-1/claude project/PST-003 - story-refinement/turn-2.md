```markdown
# Customer - Checkout - Save card for next time

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers can save a card at checkout and pay with it on their next order without typing the card number again. This covers the card form in checkout on web, iOS and Android, saved cards at the payment step and a place in the account to see and remove saved cards.

### Problem
* * *
Every card payment today means typing the full card number, expiry and CVC, even for a customer on their tenth order. In the apps the payment step loses 17% of the customers who reach it, against 9% on web, and card entry is where most of them stop. Returning customers place 68% of app orders, so most of the people typing a card again have typed it before.

### Solution
* * *
A signed-in customer can choose to keep a card when paying, and saved cards come first at the payment step on the next order. Saving is opt-in, because a card kept without the customer asking costs trust and CS contacts. Card details stay with the payment provider, and customers see and remove their saved cards from their account.

#### **Expected outcomes**
* * *
*   Returning app customers get through the payment step faster and drop off less
*   Fewer repeat orders are abandoned at card entry
*   No new CS contacts about cards kept without the customer asking
##   

## Requirements
* * *
**Saving a card**
* * *
**Open:** Whether the card brand may be stored with a saved card. The draft stores it for the brand logo, and the company context allows the card token, last four digits and expiry date only. Lotte, who owns the company context, settles it with Checkout.

*   The checkbox sits on the card form on web, iOS and Android, under the card fields
*   The checkbox label is `Save this card for next time`, unchecked by default
*   Only signed-in customers see the checkbox. Guest checkout has no saving
*   A customer can hold `5` saved cards. At the limit the checkbox is replaced by `You can save up to 5 cards`
*   The back end refuses a sixth saved card
*   Fernhouse stores the payment provider's card token, last four digits and expiry date against the account. The card number and CVC are never stored
*   Cards only. Wallet and bank payments stay as they are

**Paying with a saved card**
* * *
*   Saved cards show first at the payment step
*   Each saved card reads `Card ending 7031` with `Expires 08/28` under it and the card brand logo on the left, with the logo pending the open question under Saving a card
*   Orders whose total including shipping is over `€150`, or over `£130` in the UK, ask for the `CVC` again before paying
*   Expired saved cards are hidden at checkout
*   A declined saved card shows `This card was declined. Choose another card or enter a new one.`

**Managing saved cards**
* * *
*   Saved cards live under `Account > Payment methods` on web and in the apps
*   Removing a card asks `Remove this card?` before the card is removed

**Analytics**
* * *
*   Events for card saved, card removed and order paid with a saved card, named by the Data team in its tracking plan before any client sends them
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Card form
* * *
1\. **A signed-in customer can keep a card for next time**
* * *
*   **Given** a signed-in customer paying by card
*   **When** they choose to save the card and the payment is authorised
*   **Then** the card is offered at the payment step on their next order
*   **And** a customer who leaves the checkbox unticked has no card saved
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Guests and customers at the limit cannot save a card**
* * *
*   **Given** a guest, or a signed-in customer who already holds the maximum number of saved cards
*   **When** they reach the card form
*   **Then** they cannot save the card, and the customer at the limit is told why
*   **And** they can still pay by typing the card as they do today
* * *
- [ ] _Mark as done, if the criteria are met_

#### Payment step
* * *
3\. **A returning customer pays without retyping the card**
* * *
*   **Given** a signed-in customer with a saved card that has not expired
*   **When** they reach the payment step
*   **Then** their saved cards come first and they can pay with one without typing the card number
*   **And** expired saved cards do not appear
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Higher-value orders confirm the CVC**
* * *
*   **Given** a customer paying with a saved card
*   **When** the order total including shipping is over the CVC threshold for their market
*   **Then** they confirm the CVC before the payment goes through
*   **And** orders at or under the threshold go through without it
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A declined saved card leaves the customer a way to pay**
* * *
*   **Given** a customer paying with a saved card
*   **When** the payment provider declines the card
*   **Then** they are told the card was declined and can choose another saved card or enter a new one
*   **And** no order exists until a payment is authorised
* * *
- [ ] _Mark as done, if the criteria are met_

#### Account
* * *
6\. **A customer removes a saved card**
* * *
*   **Given** a signed-in customer with a saved card
*   **When** they remove it from their account and confirm
*   **Then** it no longer appears at the payment step on web, iOS or Android
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

*   Card brand storage is undecided. The brand logo at the payment step waits on Lotte and Checkout agreeing whether the brand may be stored

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
```

Export-equivalent path: `export/fernhouse-save-card-draft.md`

HVR self-scan: 0 hard blockers. Fixed: an Oxford comma in the About scope sentence. Kept with reason: three `TBD...` Delivery slots (fixed house token) and the full stop inside the declined-card string (agreed product copy, quoted exactly).

I've restructured Priya's draft into the house Story format. It's ready for Checkout once the card brand question below is settled. It covers the card form, the payment step and the account on web, iOS and Android, with 6 acceptance criteria.

**Your answers:**
- The declined-card message is now a requirement, using your exact wording.
- The CVC limit now applies to the order total including shipping.
- The three analytics events stay unnamed. One requirement points at the Data team's tracking plan instead.

**Decisions I made where you didn't answer. Tell me if any are wrong:**
- **Card brand:** the company context only allows storing the card token, last four digits and expiry date. Priya's draft also stores the brand for the logo. I've left this as an open question for Lotte and Checkout rather than picking a side. Because a question is open, the Story now has a Delivery section, and I've left Estimation and No-gos as `TBD...` placeholders.
- **Priya's build checklist:** I moved its values into Requirements and left out the task split. No separate tasks were created.
- **Title:** I used `Customer - Checkout - Save card for next time`.
- **References:** left out, because no links were supplied.
- **Removed:** the export note at the top of the draft and the old `PRD -` title.

**Things I added that Priya's draft doesn't say. Strike any you don't want:**
- The Analytics group is new. The rule that events are named before any app sends them comes from the company context.
- Criterion 5 says no order exists until a payment goes through. That also comes from the company context.
- Criterion 2 says a customer at the limit is told why. That's my reading of the replacement message.

**Still not covered:**
- Whether expired cards still show under `Account > Payment methods`.
- `Card ending 7031` and `Expires 08/28` are copied as written. They look like example values, not fixed text.

**Next step:** get Lotte's decision on the card brand. I'll then remove the open question, the logo caveat and the Delivery section, unless you want Delivery kept.
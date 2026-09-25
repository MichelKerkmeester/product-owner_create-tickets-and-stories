Exported from the Checkout team space on 2026-09-22. Written by Priya, Product Manager, Checkout. Status: draft, not refined yet.

# PRD - Checkout - Save card for next time

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
Offer a checkbox on the card form so a signed-in customer can choose to keep the card, and show saved cards first at the payment step next time. The card itself stays with the payment provider, and we keep only what we need to show it back to the customer. Customers manage their saved cards from their account.

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
*   Only signed-in customers see it. No saving in guest checkout
*   A customer can hold 5 saved cards. At the limit the checkbox is replaced by `You can save up to 5 cards`
*   Cards only. Wallet and bank payments stay as they are

**Paying with a saved card**
* * *
*   Saved cards show first at the payment step as `Card ending 7031` with `Expires 08/28` under it and the card brand logo on the left
*   Orders over `€150`, or `£130` in the UK, ask for the `CVC` again before paying
*   Expired cards are hidden at checkout

**Managing saved cards**
* * *
*   Saved cards live under `Account > Payment methods` on web and in the apps

**Checklist**
- [ ] BE: store the payment provider's card token against the account (token, brand, last four and expiry only)
- [ ] BE: refuse a sixth card
- [ ] FE Web: checkbox on the card form, hidden in guest checkout
- [ ] FE iOS: checkbox on the card form, hidden in guest checkout
- [ ] FE Android: checkbox on the card form, hidden in guest checkout
- [ ] FE all: saved card list at the payment step, CVC field for orders over €150 or £130
- [ ] FE all: Account > Payment methods screen with a remove button and the `Remove this card?` confirmation
- [ ] DATA: events for card saved, card removed and order paid with a saved card
- [ ] Copy for a declined saved card TBD...
* * *
##   

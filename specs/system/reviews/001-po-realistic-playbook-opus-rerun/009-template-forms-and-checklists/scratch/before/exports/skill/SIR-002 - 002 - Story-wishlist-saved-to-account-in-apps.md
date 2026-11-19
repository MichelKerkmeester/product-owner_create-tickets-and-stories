# Customer - Wishlist - One wishlist across web and the apps

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers' iOS and Android wishlists become the account list web shows, and customers without an account keep the device wishlist.

It changes how the apps were built, not a defect. Lotte, Head of Product, signed off the direction on 2026-09-24.

### Problem
* * *
The apps save the wishlist on the device and web to the account, so customers lose items on a new phone or reinstall and cannot find items across surfaces.

CS tagged `412` wishlist contacts from `2026-07-01` to `2026-09-20`, the third biggest tag after WISMO and returns, rising from 118 in July to 155 in September to the 20th. 23 also carry a complaint tag.

| What the customer says happened | Contacts |
|---------------------------------|----------|
| Wishlist gone after a new phone or after reinstalling the app | 171 |
| Saved items in the app, cannot find them on web | 138 |
| Saved items on web, cannot find them in the app | 64 |
| Could not add any more items | 39 |

Several of the 39 had a full web list and a shorter app list, unaware they were two.

### Solution
* * *
The apps save a signed-in customer's wishlist to the account, and a first sign-in on a device moves earlier device items into it. Guests keep the device wishlist, so it works without signing in.

#### **Expected outcomes**
* * *
*   Signed-in customers keep one wishlist across web, iOS and Android, a new phone and a reinstall
*   Fewer wishlist contacts to CS, where the three cross-device groups make up 373 of the 412
##   

## Requirements
* * *
**Signed-in customers on iOS and Android**
* * *
*   The wishlist is saved to the customer's account, not the device
*   The apps show the web account wishlist, and a change on one surface shows on the others

**First sign-in on a device**
* * *
*   Device items saved before the first sign-in there move into the account list
*   When the two lists together pass `50 items`, the account list keeps the `50` most recently added

**Limit**
* * *
*   The account wishlist holds up to `50 items` everywhere, as today

**Customers without an account**
* * *
*   The app wishlist stays on the device and works without an account, as today
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A signed-in customer's wishlist follows them across surfaces**
* * *
*   **Given** a signed-in customer has wishlist items
*   **When** they open it on web, iOS or Android on the same account
*   **Then** they see the same items on each surface
*   **And** adding or removing an item on one surface shows on the others
- [ ] _Mark as done, if the criteria are met_

2\. **The wishlist survives a new phone or a reinstall**
* * *
*   **Given** a signed-in customer has wishlist items in the app
*   **When** they sign in on a new phone or after a reinstall
*   **Then** every earlier item shows
- [ ] _Mark as done, if the criteria are met_

3\. **Items saved before signing in are kept**
* * *
*   **Given** a customer saved app items as a guest, and their account already has a wishlist
*   **When** they first sign in on that device
*   **Then** the device items appear in their account wishlist on every surface
*   **And** an item that was on both lists appears once
- [ ] _Mark as done, if the criteria are met_

4\. **Combined lists over the limit keep the newest items**
* * *
*   **Given** the device and account lists together exceed the limit
*   **When** the customer first signs in on that device
*   **Then** the account wishlist keeps the newest items up to the limit
- [ ] _Mark as done, if the criteria are met_

5\. **Customers without an account keep today's wishlist**
* * *
*   **Given** a customer uses the app without signing in
*   **When** they save, view or remove wishlist items
*   **Then** the wishlist works on that device as today
- [ ] _Mark as done, if the criteria are met_
* * *
##   

# Customer - Wishlist - One wishlist across web and the apps

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story makes a signed-in customer's wishlist on iOS and Android the same list web shows, saved to their account. Customers without an account keep the device wishlist they have today.

This is a change to how the apps were built, not a defect fix. Lotte, Head of Product, signed off the direction on 2026-09-24.

### Problem
* * *
In the apps the wishlist is saved on the device, and on web it is saved to the account. Customers see one shop and expect one list, so they lose items when they change phones or reinstall the app, and they cannot find app items on web or web items in the app.

CS tagged `412` wishlist contacts between `2026-07-01` and `2026-09-20`, the third biggest tag after WISMO and returns, rising from 118 in July to 155 in September up to the 20th. 23 of them also carry a complaint tag.

| What the customer says happened | Contacts |
|---------------------------------|----------|
| Wishlist gone after a new phone or after reinstalling the app | 171 |
| Saved items in the app, cannot find them on web | 138 |
| Saved items on web, cannot find them in the app | 64 |
| Could not add any more items | 39 |

Several of the 39 who hit the limit had a full list on web and a shorter one in the app, and did not know they were two lists.

### Solution
* * *
For a signed-in customer, the apps save the wishlist to the account, so the list follows the customer to a new phone and matches what web shows. The first time a customer signs in on a device, whatever they saved on it before moves into the account list, so nothing built as a guest is lost. Guests keep the device wishlist unchanged, because the wishlist has to keep working for customers who never sign in.

#### **Expected outcomes**
* * *
*   Signed-in customers keep their wishlist through a new phone or a reinstall
*   Signed-in customers see the same wishlist on web, iOS and Android
*   Fewer wishlist contacts to CS, where the three cross-device groups above account for 373 of the 412
##   

## Requirements
* * *
**Signed-in customers on iOS and Android**
* * *
*   The wishlist is saved to the customer's account, not the device
*   The apps show the same account wishlist web shows, and an item added or removed on one surface shows on the others

**First sign-in on a device**
* * *
*   Items saved on the device before the customer's first sign-in on that device move into the account list
*   When the device list and the account list together pass `50 items`, the account list keeps the `50` most recently added

**Limit**
* * *
*   The account wishlist holds up to `50 items` on every surface, unchanged from today

**Customers without an account**
* * *
*   The app wishlist stays saved on the device and works without an account, as it does today
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A signed-in customer's wishlist follows them across surfaces**
* * *
*   **Given** a signed-in customer has items on their wishlist
*   **When** they open the wishlist on web, iOS or Android while signed in to the same account
*   **Then** they see the same items on each surface
*   **And** an item they add or remove on one surface shows the change on the others
- [ ] _Mark as done, if the criteria are met_

2\. **The wishlist survives a new phone or a reinstall**
* * *
*   **Given** a signed-in customer has items on their wishlist in the app
*   **When** they install the app on a new phone, or reinstall it, and sign in
*   **Then** their wishlist shows every item it held before
- [ ] _Mark as done, if the criteria are met_

3\. **Items saved before signing in are kept**
* * *
*   **Given** a customer saved items in the app without an account, and their account already has a wishlist
*   **When** they sign in on that device for the first time
*   **Then** the items from the device appear in their account wishlist on every surface
*   **And** an item that was on both lists appears once
- [ ] _Mark as done, if the criteria are met_

4\. **Combined lists over the limit keep the newest items**
* * *
*   **Given** the device list and the account list together hold more items than the limit
*   **When** the customer signs in on that device for the first time
*   **Then** the account wishlist keeps the most recently added items up to the limit
- [ ] _Mark as done, if the criteria are met_

5\. **Customers without an account keep today's wishlist**
* * *
*   **Given** a customer uses the app without signing in
*   **When** they save, view or remove wishlist items
*   **Then** the wishlist works on that device exactly as it does today
- [ ] _Mark as done, if the criteria are met_
* * *
##   

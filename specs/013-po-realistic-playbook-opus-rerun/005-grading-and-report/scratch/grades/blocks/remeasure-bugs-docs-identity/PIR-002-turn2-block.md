# Customer - Wishlist - Account wishlist in the apps

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story saves the wishlist to the account for signed-in customers on iOS and Android, so one list follows them across web and the apps and survives a new phone. Customers without an account keep the device wishlist they have today. Product signed off the change on 2026-09-25.

### Problem
* * *
The apps save the wishlist on the device and web saves it to the account, so a customer who shops on both has two separate lists, and the app list is lost with the phone. This has been the design since the wishlist first shipped in the apps, and nothing about it changed in 4.8.0 or 4.8.2. From 2026-07-01 to 2026-09-20 CS logged `412` contacts tagged wishlist, the third biggest tag after WISMO and returns. The count rose every month, from 118 in July to 139 in August and 155 in September up to the 20th:
*   `171` lost the wishlist after a new phone or a reinstall
*   `138` saved items in the app and could not find them on web
*   `64` saved items on web and could not find them in the app
*   `39` reached the `50 items` limit, several of them with a full list on web and a second list in the app they did not know was separate

23 of those contacts also carry a complaint tag.
* * *

### Solution
* * *
Make the account the home of the wishlist for every signed-in customer, on every surface. Customers see the app and the website as one shop, so one list per account answers the first three groups of contacts and removes the hidden second list behind several of the limit contacts. Items a customer saved on a device before signing in move into the account the first time they sign in there, so nothing saved while signed out is lost. Customers without an account keep the device wishlist, because the app wishlist has always worked without sign-in and this change keeps that.
* * *

#### **Expected outcomes**
* * *
*   Signed-in customers keep their wishlist when they change phones or reinstall the app
*   Signed-in customers see the same wishlist on web, iOS and Android
*   Fewer helpdesk contacts tagged wishlist
* * *
##   

## Requirements
* * *
**Signed-in customers in the apps**
* * *
*   On iOS and Android, a signed-in customer's wishlist is saved to the account
*   The apps show the same account wishlist that web shows

**First sign-in on a device**
* * *
**Open:** A customer who is already signed in on the app when this release reaches them never signs in for the first time on that device. Whether their device items move into the account list on the first launch after the update is not decided, and Product settles it before the app tasks start.

*   The first time a customer signs in on a device, the items saved on that device move into the account list

**Wishlist limit**
* * *
*   The account wishlist holds up to `50 items`
*   When the device items and the account items together pass `50 items`, the account list keeps the `50` most recently added

**Customers without an account**
* * *
*   The device wishlist works as it does today for customers without an account
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **One wishlist on web and in the apps**
* * *
*   **Given** a signed-in customer adds an item to the wishlist in the iOS or Android app
*   **When** they open the wishlist on web, signed in to the same account
*   **Then** the item is there
*   **And** an item removed on any surface is gone from the others
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The wishlist survives a new phone**
* * *
*   **Given** a signed-in customer has items on their wishlist
*   **When** they install the app on a new phone or reinstall it, and sign in
*   **Then** the wishlist shows the same items it showed before
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Items saved before sign-in are kept**
* * *
*   **Given** a customer saved items in the app without signing in
*   **When** they sign in on that device for the first time
*   **Then** those items are on the account wishlist on web and in the apps
*   **And** the app shows one wishlist, not a device list beside an account list
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Moving items never takes the list past the limit**
* * *
*   **Given** a customer's device items and account items together pass the limit
*   **When** they sign in on that device for the first time
*   **Then** the account wishlist keeps the most recently added items up to the limit, on every surface
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Customers without an account keep the wishlist they have**
* * *
*   **Given** a customer uses the app without an account
*   **When** they add, view or remove wishlist items
*   **Then** the wishlist works on that device as it does today
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

*   Customers already signed in on the app when the release reaches them never sign in for the first time on that device. Product has to decide whether their device items move into the account list on the first launch after the update

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *

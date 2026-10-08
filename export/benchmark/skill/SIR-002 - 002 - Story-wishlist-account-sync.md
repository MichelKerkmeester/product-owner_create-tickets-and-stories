# Customer - Account - Wishlist sync

* * *
## Problem
* * *
Wishlists in the iOS and Android apps are saved only on the device, while the web wishlist is saved to the account. A customer who gets a new phone or reinstalls the app loses the list, and a list built in the app cannot be seen on web. The wishlist tag drew 412 contacts between 1 July and 20 September 2026, 171 of them about a list lost after a new phone or reinstall, and the tag has grown every month. Agents explain that the app and web lists are separate, and customers do not take that well: 23 of the 412 contacts also carry a complaint tag. Customers lose saved items without doing anything wrong, and each contact lands on the CS team.
* * *
##   

## Solution
* * *
Signed-in customers on iOS and Android keep their wishlist on the account, so the app shows the same list web shows. The first sign-in on a device moves the items saved there into that account wishlist, so a list built before signing in is not lost. Customers without an account keep the device wishlist as it works today.

**Expected outcomes**
* * *
*   A signed-in customer sees the same wishlist on web and in the app
*   A customer's device items appear in their account wishlist after the first sign-in on that device
*   A signed-out customer keeps a working device wishlist
* * *
##   

## Requirements
* * *
**Wishlist limit**
* * *
- [] A wishlist holds up to `50` items
- [] When the account and device lists together pass `50` items, the account wishlist keeps the `50` most recently added items

**Account wishlist**
* * *
- [] Signed-in customers on iOS and Android keep their wishlist on the account, the same list web shows

**First sign-in on a device**
* * *
**Open:** How an item saved on both the device and the account is handled, and which account receives the device items when two accounts sign in on one device. Lotte, Head of Product, decides.

- [] The first sign-in on a device moves the items saved on that device into the account wishlist
- [] Items already on the account wishlist stay there

**Customers already signed in**
* * *
**Open:** Whether customers who were already signed in when this ships have their device items moved, since their first sign-in has already passed. Lotte, Head of Product, decides.

**Signed-out customers**
* * *
- [] Signed-out customers keep the device wishlist, which works without an account
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **A signed-in customer sees one wishlist on web and in the app**
* * *
*   **Given** a signed-in customer has items on their wishlist
*   **When** they open the wishlist on web, or in the iOS or Android app
*   **Then** both show the same items
- [] _Mark as done, if the criteria are met_

2 ) **A customer's device items join their account wishlist on first sign-in**
* * *
*   **Given** a customer has items saved on a device and has never signed in on that device
*   **When** they sign in to the iOS or Android app
*   **Then** those items appear in their account wishlist
*   **And** the items already on their account wishlist remain
- [] _Mark as done, if the criteria are met_

3 ) **The account wishlist keeps the most recently added items when the limit is reached**
* * *
*   **Given** the device and account items together would pass the wishlist limit
*   **When** the customer signs in on the device
*   **Then** the account wishlist keeps the most recently added items up to the limit
- [] _Mark as done, if the criteria are met_

4 ) **A signed-out customer keeps a working device wishlist**
* * *
*   **Given** a customer is signed out in the iOS or Android app
*   **When** they save an item to the wishlist
*   **Then** the item is kept on the device, with no account needed
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### Rabbit holes
* * *
*   Items saved on both the device and the account, the open question under First sign-in on a device
*   Two accounts signing in on one device, the same open question under First sign-in on a device
*   Customers already signed in when this ships, the open question under Customers already signed in

#### No-gos
* * *
*   TBD...
* * *

# Customer - Wishlist - Account wishlist in the apps

* * *
## Problem
* * *
The apps keep the wishlist on the device, so a customer who changes phones or reinstalls the app loses it. Between 1 July and 20 September 2026, 412 contacts were tagged wishlist, and 171 of them report a list lost this way. The tag grew each month, from 118 contacts in July to 155 in September up to the 20th. Returning customers place 68% of app orders against 44% on web, so the loss lands on repeat buyers. Agents tell customers the app list does not come back, and 23 of the 412 contacts also carry a complaint tag.
* * *
##   

## Solution
* * *
Signed-in customers keep their app wishlist in their account, so the app shows the same list as web and the list follows the customer to a new phone or a reinstall. On the first sign-in on a device, the items saved on that device join the account wishlist. Customers without an account keep the device wishlist.

**Expected outcomes**
* * *
*   Signed-in customers see the same wishlist in the apps and on web
*   A new phone or a reinstall no longer removes a signed-in customer's wishlist
*   Items saved on a device before the first sign-in join the account wishlist
*   Customers without an account keep the device wishlist
* * *
##   

## Requirements
* * *
**Account wishlist in the apps**
* * *
- [] Signed-in iOS and Android customers save and remove wishlist items in the account wishlist, which is the list web shows
- [] The account wishlist holds up to `50` items

**First sign-in on a device**
* * *
- [] Items saved on the device move into the account wishlist on the first sign-in on that device
- [] When the device and account wishlists together hold more than `50` items, the account wishlist keeps the `50` most recently added items

**Guest wishlist**
* * *
- [] Customers without an account keep the device wishlist, saved on the device and holding up to `50` items
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **The app shows the same wishlist as web**
* * *
*   **Given** a signed-in customer has items on their wishlist on web
*   **When** they open their wishlist in the iOS or Android app
*   **Then** the app shows the same items that web shows
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A new phone keeps the signed-in wishlist**
* * *
*   **Given** a signed-in customer has items on their wishlist
*   **When** they sign in on a new phone or after reinstalling the app
*   **Then** their wishlist shows the same items
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Device items join the account on first sign-in**
* * *
*   **Given** a customer has items saved on a device and has never signed in on that device
*   **When** they sign in on that device
*   **Then** those items appear in their account wishlist
*   **And** the device wishlist no longer holds them
* * *
- [] _Mark as done, if the criteria are met_

4 ) **The account wishlist keeps the most recent items**
* * *
*   **Given** the device and account wishlists together hold more items than the account limit
*   **When** the first sign-in moves the device items into the account
*   **Then** the account wishlist holds the most recently added items, up to the limit
*   **And** the items left out are not in the wishlist on web or in the app
* * *
- [] _Mark as done, if the criteria are met_

5 ) **Guest wishlist stays on the device**
* * *
*   **Given** a customer has no account
*   **When** they save items to the wishlist in the app
*   **Then** the items are saved on the device
*   **And** no account holds them
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

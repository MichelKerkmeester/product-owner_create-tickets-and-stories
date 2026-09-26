# Customer - Wishlist - Account wishlist in the apps

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story saves the iOS and Android app wishlist to the account, so a signed-in customer has one wishlist in the apps and on web. Lotte, Head of Product, signed off on 2026-09-24.

Apps have always saved it on the device, web to the account, and nothing broke in 4.8.0 or 4.8.2, so this is a product change, not a fix.

#### Problem
* * *
One shop has two wishlists: the app list is lost with a new phone or reinstall, and the web list never shows in the app.

CS tagged `412` wishlist contacts from `2026-07-01` to `2026-09-20`, third after WISMO and returns, rising from 118 in July to 139 in August and 155 in September to the 20th.

171 lost it after a new phone or reinstall, 138 missed app items on web, 64 missed web items in the app and 39 hit the limit, several unaware of two lists. 23 also carry a complaint tag.

#### Solution
* * *
Signed-in customers get one account wishlist everywhere. Items saved on a device before signing in move into it, so the switch never costs what was saved, and customers without an account keep the device wishlist.

**Expected outcomes**
* * *
*   Signed-in customers keep their wishlist across a new phone or reinstall
*   The same wishlist on web and in the apps
*   Fewer wishlist contacts to CS
* * *
##   

## Requirements
* * *
**Platforms**
* * *
- [] The `iOS` and `Android` apps

**Account wishlist**
* * *
- [] For customers signed in to the app, which shows and edits the same account wishlist as web
- [] The limit stays at `50 items`

**First sign-in on a device**
* * *
- [] On first sign-in on a device, its items move into the account wishlist
- [] Past `50` combined, the `50` most recently added stay
- [] A product in both lists is kept once and counts once toward the limit

**Customers without an account**
* * *
- [] The app keeps saving the wishlist on the device, as today
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The same wishlist in the app and on web**
* * *
*   **Given** a customer signed in to the app and on web
*   **When** they add or remove an item on either surface
*   **Then** the other shows the same wishlist when next opened
* * *
- [] _Mark as done, if the criteria are met_

2\. **A new phone or a reinstall keeps the wishlist**
* * *
*   **Given** a signed-in customer with wishlist items
*   **When** they sign in on a new phone or after a reinstall
*   **Then** every item is there, nothing restored by hand
* * *
- [] _Mark as done, if the criteria are met_

3\. **Items saved before signing in are kept**
* * *
*   **Given** a customer saved items in the app while signed out
*   **When** they first sign in on that device
*   **Then** those items are in the account wishlist, in the app and on web
*   **And** the app shows one wishlist
* * *
- [] _Mark as done, if the criteria are met_

4\. **A move that passes the limit keeps the newest items**
* * *
*   **Given** device and account items together exceed the limit
*   **When** the customer first signs in on that device
*   **Then** the most recently added items up to the limit stay, from either list
* * *
- [] _Mark as done, if the criteria are met_

5\. **Customers without an account keep today's wishlist**
* * *
*   **Given** a customer without an account
*   **When** they save and remove items
*   **Then** it works on that device as today
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

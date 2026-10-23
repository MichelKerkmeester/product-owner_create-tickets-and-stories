```markdown
# Customer - Wishlist - One list across web and the apps

* * *
## Problem
* * *
The app saves the wishlist on the phone while web saves it to the account, so items saved in the app are missing on web and the whole list is lost on a new phone. Customers raised this `412` times between `2026-07-01` and `2026-09-20`, the third biggest helpdesk tag after WISMO and returns, rising from `118` in July to `155` in September. `23` of those contacts also carry a complaint tag, and agents can only tell customers the two lists are separate. Repeat customers place `68%` of app orders, so a lost list puts that trade at risk.
* * *
##   

## Solution
* * *
One account list replaces the two lists for every signed-in customer, so what a customer sees stops depending on which device they picked up. Device items are carried into that list at the first sign-in, because a customer who saved something expects to find it later. A customer who never signs in keeps the device list.

**Expected outcomes**
* * *
*   A customer sees one wishlist on web, `iOS` and `Android`
*   A new phone or a reinstall no longer loses the saved items
*   Agents stop explaining that the app list and the web list are separate
* * *
##   

## Requirements
* * *
**Account wishlist in the apps**
* * *
- [] Signed-in customers on `iOS` and `Android` read and write the wishlist saved to their account
- [] The account wishlist holds the same items as the `Web` wishlist, so a change on one surface shows on the others
- [] `Web` keeps its current behaviour, including requiring sign-in to see the wishlist

**Device items on first sign-in**
* * *
- [] The first sign-in on a device moves the items saved on that device into the account wishlist
- [] An item already in the account wishlist is not added a second time by the move

**Item limit**
* * *
- [] The limit stays at `50` items per wishlist
- [] When the two lists together hold more than `50` items, the account wishlist keeps the `50` most recently added

**Customers without an account**
* * *
- [] A customer without an account keeps the wishlist saved on the device, and it works without signing in
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **One wishlist on web and in the apps**
* * *
*   **Given** a signed-in customer with items in their account wishlist
*   **When** they open the wishlist in the `iOS` or `Android` app
*   **Then** they see the items the account wishlist holds on `Web`
*   **And** an item they add in the app is in the account wishlist on `Web` and in the other app
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Device items move into the account on first sign-in**
* * *
*   **Given** a customer with items saved on a device and an account they have not signed in with on that device
*   **When** they sign in on that device for the first time
*   **Then** those items are in their account wishlist
*   **And** an item that was already in the account wishlist appears once, not twice
* * *
- [] _Mark as done, if the criteria are met_

3 ) **A new phone brings the list back**
* * *
*   **Given** a signed-in customer who saved items in the app
*   **When** they install the app on a new phone and sign in
*   **Then** their wishlist is there with the items saved to their account
* * *
- [] _Mark as done, if the criteria are met_

4 ) **The merge keeps the newest items within the limit**
* * *
*   **Given** a customer whose device list and account wishlist together hold more items than the limit allows
*   **When** the two lists merge at sign-in
*   **Then** the account wishlist keeps the most recently added items up to the limit
*   **And** the items dropped are the ones added longest ago
* * *
- [] _Mark as done, if the criteria are met_

5 ) **Signed-out customers keep the device list**
* * *
*   **Given** a customer who is not signed in
*   **When** they add an item to the wishlist and close the app
*   **Then** the item is there when they open the app again
*   **And** the wishlist works without them signing in
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### External dependencies
* * *
*   **App store review** - `iOS` and `Android` store review of the build that carries the app change, and the update lag after a release, hold the customer-facing change back until it passes. Date: TBD...

#### Rabbit holes
* * *
*   TBD...

#### No-gos
* * *
*   TBD...
* * *
```

Export-equivalent path: `export/NNN - Story-wishlist-one-list-across-web-and-apps.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the three `TBD...` tokens, which are the house Delivery placeholder the Human Voice card names as an exemption.
Quality: every floor met | Kind: Story | Energy: Quick

The Story gives signed-in customers on `iOS` and `Android` the account wishlist web already shows, moves each device's items into it at the first sign-in, and leaves the device list alone for customers without an account. Requirements carry the `50` item limit and the recency rule for the merge, and the five criteria cover the shared list, the first sign-in move, a new phone, the limit at merge and the signed-out case.

### Open items
1. **Device list after the move**
   - **Situation:** The brief moves device items into the account and says nothing about what the device holds afterwards
   - **Open:** Confirm the device list is cleared, or name what a customer who signs out sees
2. **Saving at the limit**
   - **Situation:** The limit stays at `50` and the merge keeps the newest, and the brief says nothing about a signed-in customer adding a 51st item
   - **Open:** Confirm the oldest item drops, or the add is refused as it is today
3. **Repeat sign-ins**
   - **Situation:** I read "the first time they sign in on a device" as once per device, so a later sign-in on the same device does not merge again
   - **Open:** Strike it if the merge should run on every sign-in
4. **Web behaviour**
   - **Situation:** I added a requirement that web keeps its current behaviour, including requiring sign-in
   - **Open:** Strike it if web may change in the same work
5. **Delivery section**
   - **Situation:** I wrote `## Delivery` because an app store review is undated and outside the team's control
   - **Open:** Strike the section if you did not want a delivery view

Want me to change anything?
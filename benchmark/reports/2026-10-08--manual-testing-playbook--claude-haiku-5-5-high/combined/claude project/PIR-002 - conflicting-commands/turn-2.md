```markdown
# Customer - Wishlist - Account sync

* * *
## Problem
* * *
Customers who build a wishlist in the app lose it after a new phone or a reinstall, and they cannot see app items on web, because the apps save the wishlist on the device only. From 1 July to 20 September, 412 helpdesk contacts were tagged wishlist, the third largest tag and rising each month. Agents explain that the two lists are separate, and customers take that badly, with 23 of those contacts also carrying a complaint tag. Each contact is CS time spent on a list the customer expected to still be there.
* * *
##   

## Solution
* * *
Signed-in customers on iOS and Android move their wishlist to the account, so the app shows the same list that web already shows. Items saved on a device before the customer signs in there come with them, so the list follows the customer to a new phone. Customers without an account keep the device wishlist, which works as it does today.

**Expected outcomes**
* * *
*   Signed-in customers on iOS and Android see the same wishlist in the app as on web
*   Items saved on a device before sign-in are in the account wishlist after the first sign-in there
*   Customers without an account keep the device wishlist as it works today
* * *
##   

## Requirements
* * *
**Wishlist storage**
* * *
- [] Signed-in customers on iOS and Android have their wishlist saved to the account
- [] The account wishlist is the same list the web shows
- [] Customers without an account keep the device wishlist as it works today

**Sign-in migration**
* * *
- [] On a customer's first sign-in on a device, the items saved on that device move into the account wishlist
- [] Moved items keep the time they were added on the device

**Limit**
* * *
- [] The wishlist holds up to `50` items
- [] When the account wishlist and the moved device items together pass `50` items, the `50` most recently added items are kept
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A signed-in customer sees the same wishlist in the app and on web**
* * *
*   **Given** a signed-in customer has items in their wishlist in the app
*   **When** they open the wishlist on web
*   **Then** the same items appear in the list the app shows
* * *
- [] _Mark as done, if the criteria are met_

2\. **A first sign-in on a device moves the items saved there into the account**
* * *
*   **Given** a customer has items saved on a device and has not signed in on that device before
*   **When** they sign in on that device
*   **Then** the items saved on that device appear in their account wishlist
* * *
- [] _Mark as done, if the criteria are met_

3\. **The wishlist keeps the most recently added items when the combined list is over the limit**
* * *
*   **Given** a signed-in customer's account wishlist and the items moved from the device together pass the limit
*   **When** the first sign-in on that device combines them
*   **Then** the most recently added items are kept, up to the limit
* * *
- [] _Mark as done, if the criteria are met_

4\. **A customer without an account keeps the device wishlist**
* * *
*   **Given** a customer has not signed in to an account in the app
*   **When** they save items to the wishlist
*   **Then** the items stay on the device and work as they do today
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Artifact kind: Story. It has hard requirements and no child-story set, so it is not an Epic. Energy: Quick. The Problem uses Maud's 1 July to 20 September counts from the feedback file as supplied.

Export-equivalent path: `export/NNN - Story-wishlist-account-sync.md`

Two additions the chat names so you can strike them:
- Moved device items keep the time they were added on the device. The "50 most recently added" rule needs that time to work. Strike the line if the migration should stamp a new time.
- The Solution and Requirements state the migration and the sign-in criterion only as you described them. No Delivery section is written, because you did not ask for one and no requirement carries an open part.

One thing your brief does not settle: when the combined list is over 50, what happens to the older items? They could be removed from the account and device, or kept but hidden. I have not written either. Tell me which, and I will add it as a requirement.

Nothing has been saved or pushed. The artifact is the rendered block above.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
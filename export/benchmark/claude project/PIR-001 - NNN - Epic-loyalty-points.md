# Epic - Guest - Loyalty points

* * *
## About
* * *
Roamstay gives guests no points, member tiers or member-only prices today. This epic adds a points scheme to the Guest app on iOS, Android and web. It is split into several child stories, each owning one part of the lifecycle.

#### Problem
* * *
Only 19% of guests book a second stay within 12 months, and the Guest app gives them nothing for coming back. Roamstay has no points scheme, no member tiers and no member-only prices, so a completed stay leaves nothing for the next booking. Leadership wants more guests to return.

**The following issues rise from that:**
*   A completed stay earns a guest nothing toward a later booking
*   No member tier or member-only price sets a returning guest apart
####   

#### Goal
* * *
Raise the share of guests who book a second stay within 12 months from 19% today to 25% by the end of 2027.

**Direct user/Roamstay benefits:**
*   Guests see points earned on completed stays and can spend them at checkout on Pay now bookings
*   Roamstay sees more guests book a second stay within 12 months
####   

#### Solution
* * *
In order to get there, we will:
*   Let guests join the points scheme from Account
*   Credit points on completed stays
*   Show the points balance and history under Account
*   Let guests spend points at checkout on Pay now bookings, since Pay at property guests pay the property directly

The scheme runs across the Guest app on iOS, Android and web. The point value and who pays for points are not decided yet, so this epic sets no number and names no payer.

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Join
* * *
*   Guest - Account - Join the points scheme

#### Earn
* * *
*   Guest - Loyalty points - Earn points on completed stays

#### Balance and history
* * *
*   Guest - Account - Points balance and history

#### Spend
* * *
*   Guest - Loyalty points - Spend points at checkout on Pay now bookings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **Guests can join the points scheme from Account**
* * *
*   **Given** a signed-in guest on iOS, Android or web
*   **When** they join the points scheme from Account
*   **Then** their points balance appears under Account
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Points are earned on completed stays**
* * *
*   **Given** a joined guest with a stay at a property
*   **When** that stay is completed
*   **Then** the points for it appear in the guest's balance under Account
*   **And** the stay is listed in the guest's points history
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Points can be spent at checkout on Pay now bookings**
* * *
*   **Given** a joined guest with a points balance, booking a stay with Pay now
*   **When** the guest reaches checkout
*   **Then** the guest can spend points on that booking
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Points cannot be spent on Pay at property bookings**
* * *
*   **Given** a joined guest with a points balance, booking a stay with Pay at property
*   **When** the guest reaches checkout
*   **Then** points cannot be spent on that booking
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

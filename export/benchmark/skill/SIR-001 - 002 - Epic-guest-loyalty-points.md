# Epic - Guest - Loyalty points

* * *
## About
* * *
Members earn points on completed stays and spend them on a later Pay now booking, in the Guest app on iOS, Android and web.

### Problem
* * *
Roamstay has no points scheme, member tiers or member-only prices, and 19% of guests book a second stay within 12 months.

**The following issues rise from that:**
*   A completed stay earns nothing toward the next
*   81% of guests book no second stay on Roamstay within 12 months
###   

### Goal
* * *
Raise guests booking a second stay within 12 months from 19% to 25% by the end of 2027.

**Direct user/Roamstay benefits:**
*   Every completed stay earns something for a later booking
*   Guests have a reason to book here rather than elsewhere
###   

### Solution
* * *
In order to get there, we will:
*   Let signed-in guests join the points programme from Account
*   Credit points per completed stay
*   Show points balance and history under Account
*   Let members spend points at checkout on Pay now only, because Pay at property guests pay the property

Point value and who funds points are undecided, so earning and spending amounts wait until both are settled.

#### **References**
* * *
No designs or linked documents yet.

## Scope
* * *
Each of four child stories owns one lifecycle part, with its own requirements and acceptance criteria.

#### Joining
* * *
*   Guest - Loyalty points - Join from Account

#### Earning
* * *
*   Guest - Loyalty points - Earn points on completed stays

#### Balance and history
* * *
*   Guest - Loyalty points - Points balance and history under Account

#### Spending
* * *
*   Guest - Loyalty points - Spend points at checkout on Pay now bookings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes, and each child story carries its own screen and state criteria.

1\. **A signed-in guest can join from Account on every platform**
* * *
*   **Given** a signed-in non-member on iOS, Android or web
*   **When** they join from Account
*   **Then** they are a member
*   **And** the other two platforms show it when signed in there
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A member earns points for each completed stay**
* * *
*   **Given** a member with a booked stay
*   **When** the stay is completed
*   **Then** its points are credited to their balance
*   **And** a stay cancelled before completion earns no points
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A member can see their balance and what changed it**
* * *
*   **Given** a member
*   **When** they open their points under Account
*   **Then** they see their balance and history of each earning stay and spending booking
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A member can spend points on Pay now bookings only**
* * *
*   **Given** a member with points at checkout
*   **When** they pick a Pay now rate plan
*   **Then** they can spend points, reflected in the total charged and balance
*   **And** a Pay at property rate plan offers no points spending
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

# Epic - Guest - Loyalty points

* * *
## About
* * *
Loyalty points let a member earn points on completed stays and spend them at checkout on a later Pay now booking. It covers the Guest app on iOS, Android and web.
This Epic is split into four child stories, each owning one part of the points lifecycle and carrying its own detailed requirements and acceptance criteria.

### Problem
* * *
Roamstay has no loyalty or points scheme. Guests earn no points, and there are no member tiers or member-only prices. Today 19% of guests book a second stay within 12 months.

**The following issues rise from that:**
*   A completed stay leaves the guest with nothing to carry into their next booking
*   81% of guests do not book a second stay on Roamstay within 12 months
###   

### Goal
* * *
Raise the share of guests who book a second stay within 12 months from 19% today to 25% by the end of 2027.

**Direct user/Roamstay benefits:**
*   Guests get something back for every completed stay and can use it on a later booking
*   Roamstay gives guests a reason to book their next stay here rather than elsewhere
###   

### Solution
* * *
In order to get there, we will:
*   Let a signed-in guest join the points programme from Account
*   Credit points to a member for each completed stay
*   Show the member's points balance and history under Account
*   Let a member spend points at checkout on Pay now bookings only, because a Pay at property guest pays the property directly

The value of a point and who pays for points are not decided. This Epic puts no number on either, and the earning and spending stories cannot fix their amounts until both are settled.

#### **References**
* * *
No designs or linked documents yet.

## Scope
* * *
Each child story owns one part of the points lifecycle and carries its own detailed requirements and acceptance criteria.

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
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A signed-in guest can join from Account on every platform**
* * *
*   **Given** a signed-in guest who is not yet a member, on the Guest app on iOS, Android or web
*   **When** they join the points programme from Account
*   **Then** they are a member
*   **And** they see the same membership on the other two platforms when signed in there
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A member earns points for each completed stay**
* * *
*   **Given** a member with a booked stay
*   **When** the stay is completed
*   **Then** points for that stay are credited to their balance
*   **And** a stay cancelled before it is completed earns no points
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A member can see their balance and what changed it**
* * *
*   **Given** a member
*   **When** they open their points under Account
*   **Then** they see their current balance and a history entry for each stay that earned points and each booking that spent them
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A member can spend points on Pay now bookings only**
* * *
*   **Given** a member with points at checkout
*   **When** the rate plan they pick is Pay now
*   **Then** they can spend points on that booking, and the total charged and their balance both reflect it
*   **And** a Pay at property rate plan offers no way to spend points
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

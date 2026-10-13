# Epic - Guest - Loyalty points

* * *
## About
* * *
Loyalty points for guests on the Guest app on iOS, Android and web.
Four child stories carry the detailed requirements and acceptance criteria.

### Problem
* * *
Roamstay gives a returning guest nothing. There is no points scheme, no member tiers and no member-only prices, so a fifth stay costs what the first did.

**The following issues rise from that:**
*   A completed stay leaves nothing that carries over to the next booking
*   Neither Account nor checkout recognises a returning guest
###   

### Goal
* * *
Raise the share of guests who book a second stay within `12 months` from `19%` today to `25%` by the end of 2027.

**Direct user/Roamstay benefits:**
*   Guests get visible value from every completed stay to spend on a later Pay now booking
*   Roamstay gets a reason for repeat bookings, measured against the `25%` target
###   

### Solution
* * *
In order to get there, we will:
*   Let a signed-in guest join from Account
*   Add points to a member's balance when a stay completes
*   Show the balance and points history under Account
*   Let members spend points on Pay now bookings only, because Pay at property guests pay the property

The value of a point and who funds points are not decided, and no child story should assume either until they are.

## Scope
* * *
Each child story owns one part of the points lifecycle.

#### Joining and earning
* * *
*   Guest - Loyalty points - Join from Account
*   Guest - Loyalty points - Earn points on completed stays

#### Seeing and spending
* * *
*   Guest - Loyalty points - Points balance and history under Account
*   Guest - Loyalty points - Spend points at checkout on Pay now bookings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the criteria for its own screens and states.

1\. **A guest can join from Account on every platform**
* * *
*   **Given** a signed-in guest on iOS, Android or web
*   **When** they join loyalty points from Account
*   **Then** they are a member at once
*   **And** their membership shows on all three platforms, whichever they joined on
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Completed stays earn points**
* * *
*   **Given** a member with a booked stay
*   **When** the stay is completed
*   **Then** points for that stay are added to their balance
*   **And** a stay cancelled before completion adds no points
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The balance and the history agree**
* * *
*   **Given** a member with points activity
*   **When** they open their points under Account
*   **Then** they see their balance, every earning stay and every spending booking
*   **And** the balance matches the history
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Points can be spent on Pay now bookings only**
* * *
*   **Given** a member with points at checkout
*   **When** they choose Pay now
*   **Then** they can spend points on it
*   **And** a Pay at property option offers no way to spend points
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

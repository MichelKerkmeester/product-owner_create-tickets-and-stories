# Epic - Guest - Loyalty points

* * *
## About
* * *
Roamstay has no loyalty or points scheme today, so this Epic describes new work. Guests on the Guest app on iOS, Android and web earn points on completed stays and spend them at checkout on Pay now bookings. Their points balance and history sit under Account.

#### Problem
* * *
Today `19%` of guests book a second stay within `12 months`. Guests earn no points on their stays, and Roamstay has no member tiers or member-only prices. No points scheme rewards a second booking today.

####   

#### Goal
* * *
Raise the share of guests who book a second stay within `12 months` from `19%` today to `25%` by `end of 2027`.

**Direct user benefits:**
*   Guests earn points on completed stays and spend them at checkout on Pay now bookings
*   Guests see their points balance and history under Account
####   

#### Solution
* * *
Points come from completed stays and can be spent at checkout. Guests join the scheme from Account, which is also where they see their balance and history. Spending is limited to Pay now bookings, since Pay at property guests pay the property directly.

The point value and who pays for points are not decided. This Epic sets no number for either. Until they are settled, the child stories that depend on them carry them as open, and the supplied notes do not name who decides.

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Join and earn
* * *
*   Guest - Account - Join the points scheme
*   Guest - Stays - Earn points on completed stays

#### Balance and history
* * *
*   Guest - Account - Points balance and history

#### Spend at checkout
* * *
*   Guest - Checkout - Spend points on Pay now bookings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **Guests earn points on completed stays**
* * *
*   **Given** a guest who has joined the points scheme and has a completed stay in the Guest app
*   **When** they open Account
*   **Then** the points for that stay appear in their points history
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Guests join the points scheme from Account**
* * *
*   **Given** a guest with an account in the Guest app
*   **When** they join the points scheme from Account
*   **Then** their points balance appears under Account
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Points are spent only on Pay now bookings**
* * *
*   **Given** a guest with points in their balance
*   **When** they reach checkout on a Pay now booking
*   **Then** they can spend points on that booking
*   **And** checkout on a Pay at property booking has no points spending option
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

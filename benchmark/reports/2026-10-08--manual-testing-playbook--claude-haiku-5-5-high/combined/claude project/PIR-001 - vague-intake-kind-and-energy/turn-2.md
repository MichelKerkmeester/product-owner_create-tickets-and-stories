````````markdown
# Epic - Guest - Loyalty points

* * *
## About
* * *
Roamstay has no loyalty or points scheme. This epic adds one to the Guest app on iOS, Android and web, so guests earn points on completed stays, see them under Account and spend them at checkout. It is split into four child stories, each owning one part of the lifecycle.

#### Problem
* * *
Repeat bookings are the measure this epic is judged on, and most guests do not come back within a year.

**The following issues rise from that:**
*   Guests earn no points on a completed stay
*   There are no member tiers or member-only prices
*   Only 19% of guests book a second stay within 12 months
####   

#### Goal
* * *
Raise the share of guests who book a second stay within 12 months from 19% today to 25% by the end of 2027.

**Direct user/Roamstay benefits:**
*   Guests get value back from stays they have already completed
*   Guests can see what they have earned and used under Account
*   Guests can use points on a Pay now booking at checkout
####   

#### Solution
* * *
In order to get there, we will:
*   Let guests join the points scheme from Account
*   Earn points on each completed stay
*   Show the points balance and history under Account
*   Let guests spend points at checkout on Pay now bookings

The point value and who pays for points are not decided, so this epic sets no number for either. Spending applies to Pay now bookings only, because Pay at property guests pay the property directly.

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Join and earn
* * *
*   Guest - Account - Join the points scheme
*   Guest - Trips - Earn points on completed stays

#### See and spend
* * *
*   Guest - Account - Points balance and history
*   Guest - Checkout - Spend points on Pay now bookings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Guests earn and see points on every Guest app platform**
* * *
*   **Given** a guest on the Guest app on iOS, Android or web
*   **When** a stay is completed
*   **Then** the guest has earned points for that stay
*   **And** the points balance and history under Account show it
* * *
- [] _Mark as done, if the criteria are met_

2\. **Guests can spend points only on Pay now bookings**
* * *
*   **Given** a guest with points who books a stay with Pay at property
*   **When** the guest reaches checkout
*   **Then** points cannot be applied to that booking
* * *
- [] _Mark as done, if the criteria are met_

3\. **Repeat bookings are reported against the 19% baseline**
* * *
*   **Given** the points scheme is live on the Guest app
*   **When** the repeat booking rate is reported
*   **Then** it shows the share of guests who book a second stay within 12 months
*   **And** it is shown against the 19% baseline
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
````````

Export-equivalent path: `export/002 - Epic-loyalty-points.md`

Artifact kind: Epic. Deeper pass applied. The point value and funding are left unnumbered, as you asked, and the Solution says both are undecided.

Left out on purpose:
- **Delivery:** not requested, and an Epic has no requirements to carry an `**Open:**` line.
- **References:** none were supplied.
- **Added Later:** you named no deferred capability.

Additions for you to strike:
- **Area names in the child story titles:** Account for joining and viewing, Trips for earning, Checkout for spending. Please confirm these match your areas.
- **Acceptance criterion 3:** the repeat booking rate reported against the 19% baseline. It is my addition, and it needs a definition of "second stay" from the data side.
- **Direct benefits and the framing sentence in Problem:** I wrote these from the goal.

Still open for the child stories, which I have not answered: earn basis (per night or per completed stay, and on what amount), whether city tax counts, how points work across the five currencies, whether email-only guests can earn, and whether points reverse on refunds.

Quality status: Epic shape checks pass. Acceptance criteria stay at release level.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Next step: tell me whether to add a Delivery view or draft the first child story.
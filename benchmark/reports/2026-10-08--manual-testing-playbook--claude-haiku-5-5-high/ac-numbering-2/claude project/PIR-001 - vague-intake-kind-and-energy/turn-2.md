```markdown
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
```

Artifact kind: Epic, following the Epic shape with no Requirements section.

Export-equivalent path: `export/NNN - Epic-loyalty-points.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: I checked all six dimensions against the Epic shape and none sits under its floor. Accuracy rests on the 19% baseline and the 25% target you supplied, and I have not verified either.

Assumptions for you to correct:

- **Child story titles:** I put join and balance under Account, and earn and spend under Loyalty points. The titles are my proposal.
- **Open decisions:** the point value and the payer are named in Solution as undecided, with no number and no payer.
- **Second-stay window:** the 12 months has no start point in your brief, such as the first stay. I used the wording as given.
- **Still unsettled, left to child stories:** what earns points, when credit happens, whether city tax counts, how currencies work, what happens on cancellation or refund, and whether email-only bookers can join.
- **No Delivery section:** you did not ask for one, and no requirement carries an Open line. If you want estimation or rabbit holes, say so.
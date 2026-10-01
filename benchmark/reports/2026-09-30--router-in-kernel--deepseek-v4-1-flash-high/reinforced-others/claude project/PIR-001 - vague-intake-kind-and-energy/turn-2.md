<!-- Deliverable Block -->

# Epic - Guest - Loyalty points

* * *
## About
* * *
Loyalty points gives a guest a reason to book a second stay. Guests join the programme from Account, earn points when a stay completes, see the balance and its history under Account and spend points at checkout. The work lands on the Guest app across iOS, Android and web.
This Epic is split into four child stories, each owning one part of the points lifecycle and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
Roamstay runs no loyalty or points scheme, so nothing a guest does on one stay carries into the next. Returning to book again starts from the same place as the first booking, and the product has no lever aimed at the second stay.

**The following issues rise from that:**
*   A guest has no programme to join, so no completed stay counts toward anything
*   A completed stay earns nothing, so nothing brings the guest back to book again
*   The Guest app shows no points balance and no history of earning or spending
*   Checkout offers nothing a returning guest can spend
####   

#### Goal
* * *
Move the share of guests who book a second stay within `12 months` from `19%` to `25%` by the end of 2027.

**Direct user/Roamstay benefits:**
*   A guest earns on a completed stay, so the programme works from the first booking
*   A returning guest can spend a balance at checkout, so a second booking offers something a first did not
*   Balance and history sit under Account, so earning and spending are visible in one place
*   Guests on iOS, Android and web get the programme in the app they already use
####   

#### Solution
* * *
In order to get there, we will:
*   Let a guest join the programme from Account, so points belong to the guest rather than to one booking
*   Award points when a stay completes, and show the balance and its history under Account
*   Let a guest spend points at checkout on `Pay now` bookings only, since a `Pay at property` guest pays the property directly on arrival

The point value is not decided, and neither is who funds the points. Neither is assumed here, and both have to be settled before earning and spending are built.

## Scope
* * *
Each child story owns one part of the points lifecycle and carries its own detailed requirements and acceptance criteria.

#### Joining
* * *
*   Guest - Loyalty - Join from Account

#### Earning
* * *
*   Guest - Loyalty - Earn points on a completed stay

#### Balance and history
* * *
*   Guest - Loyalty - Points balance and history under Account

#### Spending
* * *
*   Guest - Loyalty - Spend points at checkout on a Pay now booking
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A guest joins from Account and earns points when a stay completes**
* * *
*   **Given** a guest with a Roamstay Account on the Guest app
*   **When** they join the programme from Account and then complete a stay
*   **Then** the points for that stay land on their balance once the stay completes, not when it is booked
* * *
- [] _Mark as done, if the criteria are met_

2\. **The balance and its history are visible under Account**
* * *
*   **Given** a guest who has earned or spent points
*   **When** they open Account
*   **Then** their current balance and the earning and spending behind it are listed
* * *
- [] _Mark as done, if the criteria are met_

3\. **Points can be spent at checkout on `Pay now` bookings only**
* * *
*   **Given** a guest with a points balance at checkout
*   **When** the booking is a `Pay now` booking
*   **Then** the guest can spend points on that booking before it is paid
*   **And** a `Pay at property` booking offers no way to spend points, because that guest pays the property on arrival
* * *
- [] _Mark as done, if the criteria are met_

4\. **The programme behaves the same on iOS, Android and web**
* * *
*   **Given** the Guest app on iOS, Android and web
*   **When** a guest joins, earns, checks a balance and spends points
*   **Then** every step is available on all three platforms and the balance agrees across them
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

`Export-equivalent path: export/002 - Epic-loyalty-points.md`

Artifact kind: Epic, with a Goal, a Scope of four child stories and release-level acceptance criteria, and no Requirements section.

Quality: six-dimension gate pass. Every claim traces to your brief or to the Roamstay context, so Accuracy holds. The Goal carries `19%`, `25%` and the end of 2027 once, and no point value, funding model or child-story link is invented anywhere.

`HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: `Pay now` and `Pay at property`, which the context carries as product identifiers, the fixed house lines In order to get there, we will and The following issues rise from that, and the repeated Given, When, Then and And labels, which house grammar fixes rather than penalises.`

Additions you may strike. The iOS, Android and web parity criterion is mine, drawn from the surfaces you named, so cut it if the release only has to work where a given story ships. I read joining as needing an Account, which leaves a guest who books with an email address only without a path to join. No `## Delivery` section, because an Epic carries no requirements, you did not ask for a delivery view and nothing supplied is an undated external constraint. Instead the two undecided items sit in Solution, so nobody reads the epic and assumes a point value or a payer. Child stories are named as plain text with no links, and the scope groups follow the points lifecycle.

Next: settle the point value and who funds points, since earning and spending cannot be built without them, then the four child stories take those decisions into their own requirements and criteria.
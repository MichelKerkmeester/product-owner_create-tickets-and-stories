```markdown
# Epic - Guest - Loyalty points

* * *
## About
* * *
Loyalty points let a guest join from Account, earn points on completed stays, see their balance and history under Account and spend points at checkout on Pay now bookings. The work covers the Guest app on iOS, Android and web.
This Epic is split into four child stories. Each one carries its own detailed requirements and acceptance criteria.

### Problem
* * *
Roamstay gives a guest nothing for coming back. There is no loyalty or points scheme, no member tiers and no member-only prices, so a guest's fifth stay is booked on the same terms as their first. Today `19%` of guests book a second stay within `12 months`.

**The following issues rise from that:**
*   A completed stay leaves the guest with nothing that carries over to their next booking
*   Neither Account nor checkout recognises a returning guest, so a repeat booking looks and costs the same as a first one
###   

### Goal
* * *
Raise the share of guests who book a second stay within `12 months` from `19%` today to `25%` by the end of 2027.

**Direct user/Roamstay benefits:**
*   Guests get value back from every completed stay, and they can see it and spend it on a later Pay now booking
*   Roamstay gets a reason for guests to book again, which it can measure against the `25%` target
###   

### Solution
* * *
In order to get there, we will:
*   Let a signed-in guest join loyalty points from Account
*   Add points to a member's balance when a stay is completed
*   Show the points balance and a history of points earned and spent under Account
*   Let a member spend points at checkout on Pay now bookings. Pay at property bookings are left out, because those guests pay the property directly

The value of a point and who pays for points are not decided yet. This Epic sets neither, and no child story should assume a value or a funder until both are decided.

## Scope
* * *
Each child story owns one part of the points lifecycle and carries its own detailed requirements and acceptance criteria.

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
Each child story carries the detailed criteria for its own screens and states.

1\. **A guest can join from Account on every platform**
* * *
*   **Given** a signed-in guest on the Guest app on iOS, Android or web
*   **When** they join loyalty points from Account
*   **Then** they are a member from that moment
*   **And** their membership shows on iOS, Android and web, whichever platform they joined on
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Completed stays earn points**
* * *
*   **Given** a member with a booked stay
*   **When** the stay is completed
*   **Then** points for that stay are added to their balance
*   **And** a stay cancelled before it is completed adds no points
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The balance and the history agree**
* * *
*   **Given** a member who has earned or spent points
*   **When** they open their points under Account
*   **Then** they see their current balance and every stay that earned points and every booking that spent them
*   **And** the balance matches the history
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Points can be spent on Pay now bookings only**
* * *
*   **Given** a member with points who reaches checkout
*   **When** they choose a Pay now payment option
*   **Then** they can spend points toward that booking
*   **And** a Pay at property payment option offers no way to spend points
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Epic-guest-loyalty-points.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

This is an Epic, drafted in full depth. It meets the quality bar on all six dimensions. I checked Completeness against the Epic format, which has a Goal and a Scope listing the child stories but no requirements section of its own. There are no reference links because you didn't send any.

**How I used your answers:**
- The four child stories are exactly the ones you listed. They're in plain text because none exist in ClickUp yet.
- The goal uses your figures word for word: from 19% to 25% by the end of 2027.
- Only Pay now bookings can spend points, and I kept your reason for leaving out Pay at property.
- The point value and who pays for points are marked as undecided in one sentence, with no number on either.

**Things I added that you didn't ask for (remove any you don't want):**
- In criterion 1, someone who joins on one platform is a member on all three.
- In criterion 2, a stay cancelled before it's completed earns no points.
- In criterion 3, the balance always matches the history.
- I wrote the child story titles in the context file's story title format.

**Left for the child stories to decide:**
- Whether guests who book with just an email address can earn points
- What makes a stay "completed"
- Whether a refund after the stay takes points back
- Whether city tax counts toward points

**Not included, but you might want it:**
- **A way to measure the goal.** Nothing in the Epic tracks the 19% to 25% target. If you want that, I'd add a tracking story owned by Data.
- **A Delivery section.** You didn't ask for one, so I left it out. If you'd like the undecided point value and funding listed there as risks, I can add it.
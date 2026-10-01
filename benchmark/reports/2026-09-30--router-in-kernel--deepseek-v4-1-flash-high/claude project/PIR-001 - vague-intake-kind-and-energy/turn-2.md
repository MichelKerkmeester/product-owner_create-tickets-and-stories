```markdown
# Epic - Guest - Loyalty points on stays

* * *
## About
* * *
Roamstay guests earn nothing on a completed stay today, and the scheme this epic introduces gives a finished stay something to return to. The work covers the Guest app on iOS, Android and web, and it splits into four child stories, each owning one part of the points lifecycle and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
Roamstay has no loyalty or points scheme. A guest books a stay, gets a confirmation email and a trip in their account, and the product then offers nothing that brings them back. `19%` of guests book a second stay within 12 months, which is the number this epic exists to move.

**The following issues rise from that:**
*   `19%` of guests book a second stay within 12 months, so most first stays are not followed by a second
*   A completed stay earns the guest nothing, and there are no member tiers or member-only prices
####   

#### Goal
* * *
Raise repeat bookings to `25%` of guests booking a second stay within 12 months by the end of 2027, from `19%` today.

**Direct guest/Roamstay benefits:**
*   A guest gets something back from a completed stay
*   A returning guest has a reason to book again on Roamstay rather than elsewhere
*   Repeat bookings rise, which is the outcome the scheme is measured on
####   

#### Solution
* * *
In order to get there, we will:
*   Let a guest join the points scheme from Account, on iOS, Android and web
*   Award points on a stay once it is completed
*   Keep a points balance and history under Account, so a guest can see what each stay earned and what each spend cost
*   Let a guest spend points at checkout on a `Pay now` booking, where the points spent reduce the amount charged

`Pay at property` stays out of spending, because those guests pay the property directly. Two decisions remain open and neither carries a value here: what a point is worth, and who funds points.

## Scope
* * *
Each child story owns one part of the points lifecycle and carries its own detailed requirements and acceptance criteria.

#### Joining and earning
* * *
*   Guest - Loyalty - Join from Account
*   Guest - Loyalty - Earn points on completed stays

#### Balance and spending
* * *
*   Guest - Loyalty - Points balance and history in Account
*   Guest - Loyalty - Spend points at checkout on Pay now
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A guest can join the points scheme from Account**
* * *
*   **Given** a guest signed in on the Guest app
*   **When** they open Account and join the points scheme
*   **Then** they are in the scheme, and Account shows their points balance
*   **And** joining works on iOS, Android and web
* * *
- [] _Mark as done, if the criteria are met_

2\. **A completed stay earns points, and nothing else does**
* * *
*   **Given** a guest who is in the points scheme
*   **When** a stay they booked is completed
*   **Then** the points for that stay are credited to their account
*   **And** a booking that is cancelled or never completed credits nothing
* * *
- [] _Mark as done, if the criteria are met_

3\. **A guest can see their balance and history in Account**
* * *
*   **Given** a guest who has earned points
*   **When** they open Account
*   **Then** they see their current balance together with the history of awards and spends
*   **And** the balance and history match on iOS, Android and web
* * *
- [] _Mark as done, if the criteria are met_

4\. **Points can be spent at checkout on `Pay now` bookings only**
* * *
*   **Given** a guest with a points balance at checkout
*   **When** they pay with `Pay now`
*   **Then** the points they choose to spend reduce the amount charged, and their balance falls to match
*   **And** a `Pay at property` booking offers no way to spend points
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Epic-loyalty-points-on-stays.md`

Artifact kind: Epic, in the Barter house format.

HVR self-scan: 0 hard blockers. Fixed: no banned term, metaphor, setup phrase or unfixed generalisation stood in the draft. Kept with reason: the repeated Given, When, Then and And labels, which are fixed house labels so the synonym-cycling rule requires the repetition, and the hyphen-joined H1 and child-story names, which are house title grammar.

Quality status: six-dimension gate passes, read against the Epic shape. Completeness holds a Goal and a Scope of four child stories with no `## Requirements`, which is the Epic contract rather than a gap. Accuracy holds because `19%`, `25%`, end of 2027, the three platforms, the `Pay now` limit and the `Pay at property` exclusion come from you or from the context file, and no point value or funding party appears anywhere. Deep energy applied the five perspectives, user, business, technical, risk and delivery.

Additions I made, so you can strike any. The child-story working titles and the area word `Loyalty` are mine, since the stories need names in the H1 shape before they exist. The two Scope group names are mine. The Problem, Goal and Solution prose and the three benefit lines are derived from your `19%` to `25%` goal and from the context line that no scheme, tiers or member-only prices exist today. Criterion 2 draws "a cancelled or never completed booking credits nothing" from your "completed stays", and the cross-platform parity clauses come from your iOS, Android and web scope.

What is deliberately absent. No `## Delivery`, because you did not ask for a delivery view and nothing forced one, so Acceptance criteria closes the artifact. No `## Requirements`, which the Epic shape delegates to the child stories. No `#### **References**`, because no links were supplied. No links in Scope, because the child stories do not exist yet, and no date or number was invented for them.

Next step: the four child stories can follow as Stories against this Epic, each carrying its own requirements. The point value and the funding decision become `**Open:**` lines on the earning and spending stories when those are drafted. Say the word and I will draft any of them, or add a delivery view to this Epic. No ClickUp tooling is connected in this session, so there is nothing to publish.
```markdown
# Epic - Guest - Loyalty points

* * *
## About
* * *
Loyalty points give a guest something to come back for. This epic adds the programme to the Guest app, and it is split into several child stories, each owning one part of it and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
A guest who completes a stay with Roamstay earns nothing for it, and the product has no member tiers and no member-only prices. A guest who comes back is treated exactly like a first-time guest. Repeat bookings sit at `19%` of guests within 12 months, against a target of `25%` by the end of 2027.

**The following issues rise from that:**
*   A guest has no balance to return to, so a second booking starts from the same place as the first
*   Nothing under Account shows a guest what their stays have built up
*   Only `19%` of guests book a second stay within 12 months, against a target of `25%` by the end of 2027
####   

#### Goal
* * *
Raise repeat bookings so `25%` of guests book a second stay within 12 months by the end of 2027, up from `19%` today.

**Direct user/Barter benefits:**
*   A guest gets something back for a completed stay, so a second booking starts from a balance
*   Roamstay gains a way to move repeat bookings that it can measure against the `25%` target
####   

#### Solution
* * *
In order to get there, we will:
*   Let a guest join the programme from Account, on iOS, Android and web
*   Credit the points a completed stay earns, and show the balance and its history under Account
*   Let a guest spend points at checkout on a Pay now booking
*   Keep Pay at property bookings unchanged, since those guests pay the property directly

## Scope
* * *
Each child story owns one part of the programme and carries its own detailed requirements and acceptance criteria.

#### Account
* * *
*   Guest - Loyalty - Join from Account
*   Guest - Loyalty - Points balance and history
####   

#### Earning
* * *
*   Guest - Loyalty - Earn points on completed stays
####   

#### Spending
* * *
*   Guest - Loyalty - Spend points at checkout on Pay now bookings
####   

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release.

**Points on Pay at property bookings**
*   Guests who pay the property directly earn points for the stay
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A guest can join the programme from Account, and the membership holds on every platform**
* * *
*   **Given** a guest with a Roamstay account on iOS, Android or web
*   **When** they join the programme from Account
*   **Then** they are a member on every platform they are signed in on, with no second join
* * *
- [] _Mark as done, if the criteria are met_

2\. **A completed stay adds the points it earns to the member's balance**
* * *
*   **Given** a member whose booking has run its full stay
*   **When** the stay completes
*   **Then** the balance shows the points that stay earns, and the history names the stay
* * *
- [] _Mark as done, if the criteria are met_

3\. **A guest can spend points at checkout on a Pay now booking**
* * *
*   **Given** a member with a balance and a Pay now booking at checkout
*   **When** they spend points on that booking
*   **Then** the booking records the redemption and the balance drops by it
*   **And** a Pay at property booking offers no redemption
* * *
- [] _Mark as done, if the criteria are met_

4\. **The programme's effect on repeat bookings can be reported**
* * *
*   **Given** the programme is live for members
*   **When** a member books a second stay inside the window the goal names
*   **Then** that repeat booking counts against the goal the epic names
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   What a point is worth is not decided, so no value may be read into this epic
*   Who pays for points is not decided, so earning and spending stay blocked until it is
*   A guest who books with an email address only has no account, so a completed stay on that booking has no balance to earn into

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No point value and no funding model fixed in code, copy or content before the decision lands
*   No redemption on a Pay at property booking, because those guests pay the property directly
* * *
```

Export-equivalent path: export/001 - Epic-loyalty-points.md

Artifact kind: Epic, at Deep energy, so all five perspectives went into it (guest value, business goal, technical surface, the risk in the undecided parameters, and delivery honesty).

Quality summary. Source safety: every number, platform and child story comes from you or the context file, the two undecided parameters carry no number, and no link is invented. Shape fit: About with Problem, Goal and Solution, a Scope of your four child stories plus one deferred capability, release-level criteria and no Requirements section. House grammar: dividers, `*   ` bullets, `- []` checkboxes, spacer headings and the Mark-as-done lines all hold. Delivery state: written, with `TBD...` left where nobody has sized the work.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` (the house placeholder token), Added Later (the template's own casing) and the fixed template labels The following issues rise from that and Direct user/Barter benefits.

Additions you can strike, all named so you can drop any that do not fit. Delivery is written at all, on the grounds that the epic carries two undecided parameters that a developer would otherwise fill in. The Added Later item for points on stays paid at the property is inferred from your reason for the Pay now restriction. The email-only guest rabbit hole comes from the context file, since those bookings have no account. The No-go against fixing a value or a funding model, and criterion 4 tying the release to the repeat-booking goal, are both mine. The four child story titles and the three Scope group names are my suggestion in the house shape, so rename them freely.

Next step: put the point value and the funding model in front of whoever owns them, because earning and spending cannot ship without both. When those land, I can cut the four child stories as separate PRDs in the order the Scope lists them.
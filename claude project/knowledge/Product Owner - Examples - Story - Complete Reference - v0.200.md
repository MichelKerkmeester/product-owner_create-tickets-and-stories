# Product Owner - Examples - Story - Complete Reference - v0.200

The maximal house Story: every optional enrichment populated as a reference for what is available. The story preamble, an About umbrella with Problem, a Solution that carries a User Story promise block, Expected outcomes and References, a Definition of Ready gate, Requirements holding only hard constraints with a PRD value line, a Rule block, a Which-means-that block and one priority marker on each group, outcome-led Given/When/Then acceptance criteria grouped by surface with Mark-as-done lines, a Definition of Done gate, plus a Delivery close present because the request asked for a delivery view and sizing. A reference for what is available, not the default a small Story needs. Most Stories use far less. Simple Stories drop every optional block, so reach for these only when a Story earns them.

---

# Organizer - Presale - Access windows & redemption limits

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Organizers on Marquee open a presale by handing out codes that unlock early ticket prices. Today a code works the instant it is created, for anyone who has it, with no cap and no end, so a leaked code drains the presale allocation and a code stays live long after the presale should have closed. This story gives every presale code a time-boxed access window and a redemption cap, and lets an organizer revoke a code the moment it leaks, so a code only ever works when and as much as the organizer intended.

A presale code moves through one lifecycle:
*   `draft` → created but not yet live, redeems nothing
*   `active` → inside its window and under its cap, redeemable
*   `exhausted` → cap reached, no more redemptions
*   `closed` → window ended or the code was revoked

### Problem
* * *
Organizers cannot control when a code works or how far it spreads:
*   A code goes live the instant it is created, with no start and no end
*   There is no cap, so one shared code can drain the whole presale allocation
*   A leaked code keeps working with no way to shut it off
*   A code stays redeemable long after the presale window should have closed

### Solution
* * *
Give every presale code one shared window-and-cap lifecycle with three controls:
*   A time-boxed access window with a start and an end
*   A redemption cap per code
*   An instant revoke that closes a single leaked code

#### **User Story**
* * *
As an organizer running a presale:
*   I want each code to work only inside a window I set, so that early access opens and closes on schedule without me watching it
*   I want each code to stop after a set number of uses, so that a shared code cannot drain the allocation
*   I want to revoke a leaked code in one action, so that I can shut it off the moment I notice it

#### **Expected outcomes**
* * *
*   A presale code only works during the window the organizer set for it
*   A shared or leaked code can never redeem more than its cap
*   A leaked code can be shut off in one action, without disturbing the codes that are still safe
*   No code stays redeemable after the presale it belongs to has closed

#### **References**
* * *
Components
*   [Page | Presale composer](https://www.figma.com/design/marquee/presale?node-id=1-2)
*   [Visuals | Windows & limits](https://www.figma.com/design/marquee/presale-visuals?node-id=3-4)
Flows
*   [Set a window and cap](https://www.figma.com/design/marquee/presale-flows?node-id=5-6)
*   [Revoke a code](https://www.figma.com/design/marquee/presale-flows?node-id=7-8)
Lifecycle
*   [Presale code lifecycle](https://www.figma.com/board/marquee/presale-lifecycle?node-id=9-10)
Spec
*   [Marquee - Presale Code Lifecycle Spec](https://docs.marquee.example/presale/codes)
* * *
##   

#### **Definition of Ready**
* * *
Check off as met. Pull requirements into a sprint only when every box is checked:
- [ ] Every acceptance criterion is agreed as an outcome, and every hard requirement is confirmed with the team that has to meet it
- [ ] Dependencies identified (the order service exposes a confirmed-order webhook and the checkout hold-and-release is live)
- [ ] Sized by the team and each requirement fits comfortably in a sprint
* * *
##   

## Requirements
* * *
**Access windows** ← PRIO
* * *
**PRD:** As an organizer running a presale, I want each code to work only inside a set start and end time, so that early access opens and closes exactly when the presale is meant to run.

*   Every code carries a start and an end, stored as `opens_at` and `closes_at` in `UTC`
*   A code redeems nothing outside that window

#### **Rule**
* * *
**Window bound:** `opens_at <= now() < closes_at`
A redemption outside the window is refused. `now()` is compared in `UTC` and shown to the organizer in their own local time.
* * *

Which means that:
*   A code cannot be redeemed a moment before it opens or a moment after it closes
*   An attempt outside the window returns "This code is not active right now." and consumes nothing

**Redemption limits**
* * *
**PRD:** As an organizer protecting the presale allocation, I want each code to stop after a set number of uses, so that a shared or leaked code cannot drain more tickets than I intended.

*   Every code carries a `max_redemptions` value
*   A redemption counts only against a confirmed order

#### **Rule**
* * *
**Redemption cap:** `redemptions < max_redemptions`
The count is incremented only on a confirmed order. An abandoned checkout releases its hold and does not count.
* * *

Which means that:
*   The code redeems at most `max_redemptions` times, never one more
*   A checkout that is abandoned frees its seat back to the remaining count

**Instant revoke**
* * *
**PRD:** As an organizer who spots a leaked code, I want to revoke it in one action, so that it stops working immediately without touching the codes that are still safe.

*   Revoke applies to a single code, never to a presale or a batch
*   A revoked code is closed permanently and cannot be reopened

#### **Rule**
* * *
**Revoke effect:** `state = revoked` blocks every redemption
A revoked code is closed for good. It cannot be reopened, and a new code must be issued instead.
* * *

Which means that:
*   A revoked code refuses every redemption from the moment it is revoked
*   Orders already confirmed before the revoke stand, and only new redemptions are blocked
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Access windows
* * *
1\. **A code works during the window the organizer set**
* * *
*   **Given** a code inside its access window with redemptions still available
*   **When** a member enters it at checkout
*   **Then** the presale price unlocks and the redemption is counted against that code
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A code outside its window does nothing at all**
* * *
*   **Given** a code whose window has not opened yet, or has already closed
*   **When** a member enters it
*   **Then** it is refused with "This code is not active right now." and nothing is consumed
*   **And** the organizer reads that window in their own local time wherever the code is shown
* * *
- [ ] _Mark as done, if the criteria are met_

#### Redemption limits
* * *
3\. **A code stops at the cap the organizer set**
* * *
*   **Given** a code with redemptions still available inside its window
*   **When** members keep redeeming it
*   **Then** it redeems up to `max_redemptions` and no further, even under two members confirming at the same moment
*   **And** every attempt past the cap is refused as fully redeemed
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **An abandoned checkout gives its seat back**
* * *
*   **Given** a member holding the last seat under the cap
*   **When** they abandon checkout before confirming
*   **Then** the seat returns to the remaining count and another member can still use the code
* * *
- [ ] _Mark as done, if the criteria are met_

#### Revoke
* * *
5\. **Revoking a leaked code stops it at once, and only it**
* * *
*   **Given** an open, un-exhausted code and other live codes in the same presale
*   **When** the organizer revokes that one code
*   **Then** the next attempt to redeem it is refused immediately
*   **And** every other code in the presale keeps working
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **A revoke never undoes an order already placed**
* * *
*   **Given** a member who confirmed an order before the code was revoked
*   **When** the organizer revokes the code
*   **Then** that member keeps their order and only new redemptions are blocked
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

#### **Definition of Done**
* * *
Verify for every requirement above before its task closes:
- [ ] The requirement's acceptance criteria all pass against a staging presale with realistic redemption volume
- [ ] Tests added covering the window bound, the redemption cap, the abandoned-checkout release and the revoke lock, with CI green
- [ ] Reviewed by a second engineer
- [ ] A load test confirms two members racing for the last seat never push the count past `max_redemptions`
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   One sprint for two engineers: window and cap logic in the first week, revoke and the last-seat race guard in the second

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Timezone handling for the window bounds: store `opens_at` and `closes_at` in `UTC` and show the organizer's local time everywhere, rather than building a per-code timezone picker

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No bulk code generation or CSV import screen, because this story governs only how a single existing code behaves
* * *

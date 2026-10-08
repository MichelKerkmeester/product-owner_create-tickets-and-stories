```markdown
# Epic - Customer - Self-serve returns

* * *
## About
* * *
Signed-in customers on web, iOS and Android start a return themselves, inside the 30-day window from delivery, instead of contacting CS.

This Epic splits the work into four child stories, one per part of the return lifecycle: starting a return from order history, the return label by email, the return status on the order page and the refund after the warehouse check.

#### Problem
* * *
Today a customer has to contact CS. An agent then creates the return in Admin, emails a return label and issues the refund after the warehouse checks the item. CS handles about 1,900 return requests a month.

**The following issues rise from that:**
*   Every return waits for a CS agent, so no step starts until the customer makes contact
*   A refund takes 6 days on average from the first contact
*   The order page shows only the order's shipping state, so customers have no way to see a return's progress there
####   

#### Goal
* * *
Signed-in customers start and follow their own returns inside the 30-day window from delivery, so CS stops creating the returns customers can start themselves. By the end of Q1 2027, at least 60% of returns start without a CS contact. Today every return starts with a CS contact.

**Direct user/Barter benefits:**
*   Customers start a return from their order history, with the items and a reason, without waiting for CS
*   Customers see where a return stands on the order page
*   CS keeps only the returns that still need a person, including pallet items
####   

#### Solution
* * *
In order to get there, we will:
*   Let signed-in customers start a return from order history on web, iOS and Android, with the items and a reason, inside the 30-day window
*   Email the customer a return label for each return they start
*   Show the return status on the order page
*   Refund the customer once the warehouse has checked the returned item
*   Keep pallet items with CS, as today

## Scope
* * *
Each child story owns one part of the return lifecycle and carries its own requirements and acceptance criteria. The four children are named as plain text until they have links.

#### Start a return
* * *
*   Customer - Self-serve returns - Start a return from order history
*   Customer - Self-serve returns - Return label by email

#### Track the return
* * *
*   Customer - Self-serve returns - Return status on the order page

#### Refund
* * *
*   Customer - Self-serve returns - Refund after the warehouse check

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release.

**Guest returns**
*   Guests start a return, which the order-history start cannot reach, because a guest has no order history
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A signed-in customer returns an item without contacting CS**
* * *
*   **Given** a signed-in customer with an item delivered within 30 days of delivery
*   **When** they start a return from their order history, with the items and a reason
*   **Then** the return starts without a CS contact
*   **And** the return label arrives by email
* * *
- [] _Mark as done, if the criteria are met_

2\. **The return status shows on the order page**
* * *
*   **Given** a customer with a return started from their order history
*   **When** they open that order
*   **Then** the order page shows the current return status
* * *
- [] _Mark as done, if the criteria are met_

3\. **A refund follows the warehouse check**
* * *
*   **Given** a return started from order history
*   **When** the warehouse has checked the returned item
*   **Then** the customer is refunded
*   **And** no refund is issued before that check
* * *
- [] _Mark as done, if the criteria are met_

4\. **An item past the 30-day window cannot start a return**
* * *
*   **Given** a signed-in customer with an item delivered more than 30 days ago
*   **When** they look for a return option on that item
*   **Then** the customer cannot start a return for it themselves
* * *
- [] _Mark as done, if the criteria are met_

5\. **Pallet items still go through CS**
* * *
*   **Given** an order with a pallet item
*   **When** the customer wants to return that item
*   **Then** the return goes through a CS contact, as it does today
* * *
- [] _Mark as done, if the criteria are met_

6\. **At least 60% of returns start without a CS contact by the end of Q1 2027**
* * *
*   **Given** the returns started up to the end of Q1 2027
*   **When** Q1 2027 ends
*   **Then** at least 60% of them started without a CS contact
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### External dependencies
* * *
*   **Apple App Store and Google Play review** - approve each app release that carries the return flow, and keep the return start, return status and label request blocked in the iOS and Android apps until then. Date: TBD...

#### Rabbit holes
* * *
*   Whether a self-serve refund above €200 per order needs CS lead approval, as a CS agent's refund does today, is not settled
*   Every label the carrier creates is charged, whether or not the parcel ships, so a label for a return that never ships costs money

#### No-gos
* * *
*   Pallet items get no self-serve return, so CS keeps creating those returns by hand
* * *
```

Export-equivalent path: `export/NNN - Epic-self-serve-returns.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` (fixed Delivery placeholder).

**Artifact kind:** Epic, from `$e`. Scope names the four child stories as plain text because none exist yet.

**Delivery section:** written because the app-store review is an undated constraint outside the team's control, which the context file describes under known constraints. Estimation and Rabbit holes stay `TBD...` where your brief gives nothing.

**Additions I made, strike any you disagree with:**
- Criterion 4: customers outside the 30-day window cannot start a return. Read from "inside the 30-day window".
- Criterion 6: the 60% target written as a release check.
- Scope groups: Start a return, Track the return, Refund.
- Rabbit hole on label charges, and the App Store and Google Play external dependency. Both come from `context/fernhouse-context.md`, not your brief.
- The label-charge rule assumes return labels come from the parcel carrier, as other labels do.

**One decision to settle before the refund child story is written:** the context file caps a CS agent's refund at €200 per order, with a CS lead approving above that. Your brief does not say whether a self-serve refund follows the same cap. Rabbit holes records it as open. When the refund story is written, it carries the question as an `**Open:**` line.

**Context file to update when this ships:** `fernhouse-context.md` says the order page status never changes after dispatch. Return status changes that, so the line needs updating then.
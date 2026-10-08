# Epic - Customer - Self-serve returns

* * *
## About
* * *
Signed-in customers handle a return without contacting CS, from starting it to receiving the refund. The change splits into four child stories listed under Scope, and guest returns sit under Added Later.

#### Problem
* * *
Customers have 30 days from delivery to return an item, but there is no self-serve return today. A customer contacts CS, a CS agent creates the return in Admin and emails a return label, the warehouse checks the item, and the agent refunds. CS handles about 1,900 return requests a month, and a refund takes 6 days on average from first contact.

**The following issues rise from that:**
*   Signed-in customers cannot start a return from their own order history
*   Every return waits on a CS agent to create it by hand in Admin
####   

#### Goal
* * *
The aim is that signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin. By the end of Q1 2027, at least 60% of returns start without a CS contact.

**Direct user/Barter benefits:**
*   Signed-in customers start a return from order history without contacting CS
*   CS stops creating returns by hand in Admin for the returns this epic covers
####   

#### Solution
* * *
In order to get there, we will:
*   Let signed-in customers start a return from order history, choosing the items and a reason
*   Email the return label to the customer
*   Show the return status on the order page, which today never changes after dispatch
*   Refund the customer once the warehouse has checked the returned item
*   Keep pallet items with CS, and hold guest returns in Added Later

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Starting the return
* * *
*   Customer - Self-serve returns - Start from order history

#### After the return starts
* * *
*   Customer - Self-serve returns - Return label by email
*   Customer - Self-serve returns - Return status on order page

#### Refund
* * *
*   Customer - Self-serve returns - Refund after warehouse check

#### Added Later
* * *
Capabilities that belong to the epic but do not block the first release.

**Guest returns**
*   Guest customers, who have no order history today, start a return without blocking the first release
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **Signed-in customers start a return themselves**
* * *
*   **Given** a signed-in customer on web, iOS or Android with an item delivered inside the 30-day return window
*   **When** the customer starts a return from order history, picks the items and gives a reason
*   **Then** the return is created without a CS contact
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The return label reaches the customer by email**
* * *
*   **Given** a return started by a signed-in customer
*   **When** the return label is issued
*   **Then** the customer receives the label by email
* * *
- [] _Mark as done, if the criteria are met_

3 ) **The order page shows the return status**
* * *
*   **Given** a return started on an order
*   **When** the customer opens that order on web or in the app
*   **Then** the order page shows the current return status
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Refunds follow the warehouse check without a CS contact**
* * *
*   **Given** the warehouse has checked the returned items
*   **When** the check result is recorded
*   **Then** the customer receives the refund without a CS contact
* * *
- [] _Mark as done, if the criteria are met_

5 ) **The Q1 2027 target is met**
* * *
*   **Given** returns started on web, iOS and Android during Q1 2027
*   **When** Q1 2027 closes
*   **Then** at least 60% of those returns start without a CS contact
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
*   **App store review** - the iOS and Android stores approve each app release that carries the return flow, and the update reaches most customers about a week after release. Date: TBD...

#### Rabbit holes
* * *
*   Whether the €200 per-order CS refund limit applies once a refund no longer goes through a CS agent, and who decides
*   Each parcel carrier label is charged on creation, even if the parcel never ships, so creation timing sets the cost of abandoned returns

#### No-gos
* * *
*   Pallet items stay with CS and get no self-serve return
* * *

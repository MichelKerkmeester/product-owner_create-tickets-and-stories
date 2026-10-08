# Epic - Customer - Self-serve returns

* * *
## About
* * *
Self-serve returns let signed-in customers on web, iOS and Android start a return themselves, inside the 30-day window. The work is split into four child stories, grouped by part of the return lifecycle.

#### Problem
* * *
Customers have 30 days from delivery to return an item, but there is no self-serve return today, so the customer contacts CS. A CS agent creates the return in Admin and emails a return label. The agent issues the refund once the warehouse checks the item.

**The following issues rise from that:**
*   Every return starts with a CS contact, so CS creates each one by hand in Admin
*   A refund takes 6 days on average from the first contact
*   Customers cannot start a return from their order history
####   

#### Goal
* * *
Signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin. By the end of Q1 2027, at least 60% of returns start without a CS contact.

**Direct user/Fernhouse benefits:**
*   Customers start a return from their own order history, without a CS contact
*   CS stops creating returns by hand in Admin
*   Fewer return requests need a CS agent, from about 1,900 a month
####   

#### Solution
* * *
In order to get there, we will:
*   Let signed-in customers start a return from order history, choosing the items and a reason
*   Send the return label by email
*   Show the return status on the order page
*   Refund the customer after the warehouse check
*   Keep pallet items with CS

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Start a return
* * *
*   Customer - Self-serve returns - Start a return from order history

#### Label and status
* * *
*   Customer - Self-serve returns - Return label by email
*   Customer - Self-serve returns - Return status on the order page

#### Refund
* * *
*   Customer - Self-serve returns - Refund after the warehouse check

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release.

**Guest returns**
*   Return start for guest orders, which have no order history today
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **Signed-in customers start a return themselves**
* * *
*   **Given** a signed-in customer with a delivered item inside its 30-day return window
*   **When** they start a return from order history on web, iOS or Android
*   **Then** the return is created from the items and reason they chose, with no CS contact
*   **And** no CS agent creates the return by hand in Admin
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The customer gets the return label by email**
* * *
*   **Given** a signed-in customer with a return started from order history
*   **When** the return is submitted
*   **Then** a return label arrives by email
*   **And** the order page shows the return status
* * *
- [] _Mark as done, if the criteria are met_

3 ) **The refund follows the warehouse check**
* * *
*   **Given** a return started through self-serve
*   **When** the warehouse has checked the item
*   **Then** the refund is issued only after that check
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Pallet items and guest orders get no self-serve return**
* * *
*   **Given** an order that holds a pallet item, or a guest order
*   **When** the customer looks for a return on that order
*   **Then** no self-serve return is offered
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

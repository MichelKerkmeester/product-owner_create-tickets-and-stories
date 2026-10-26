# Customer - Returns - Start a return

* * *
## Problem
* * *
A Fernhouse customer who wants to return an item cannot start the return themselves. They contact CS, an agent creates the return in Admin and emails a return label, and the warehouse checks the item before the agent refunds. CS handles about 1,900 return requests a month this way, and a refund takes 6 days on average from the first contact. Every return costs agent time and keeps the customer waiting inside the 30 days they have from delivery.
* * *
##   

## Solution
* * *
A customer starts a return from the order they received, on web, iOS or Android, and no longer needs a CS agent to create it. The request is made from the order itself because that is where the customer already finds the delivery that starts the return window. The agent's return handling in Admin stays as it is.

**Expected outcomes**
* * *
*   Customers ask for a return without contacting CS
*   Fewer return requests reach the helpdesk
* * *
##   

## Requirements
* * *
**Return window**
* * *
- [] A return can be started up to `30 days` from delivery

**Platforms**
* * *
- [] The flow ships on web, iOS and Android
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **Start a return without contacting CS**
* * *
*   **Given** a customer has a delivered order that is inside its return window
*   **When** they ask to return an item from that order
*   **Then** the return is registered
*   **And** the customer sees that Fernhouse received the request
*   **And** the flow works the same way on web, iOS and Android
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A return outside the window cannot be started**
* * *
*   **Given** a customer's order is past its return window
*   **When** they look to return an item from it
*   **Then** no return is registered
*   **And** the customer is told why
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

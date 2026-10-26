# Customer - Returns - Self-serve return

* * *
## Problem
* * *
Customers cannot start a return themselves today. They have `30 days` from delivery, but they must contact CS, where an agent creates the return in Admin and emails a return label, and the warehouse checks the item before the agent refunds. CS handles about `1,900` return requests a month, and a refund takes `6 days` on average from the first contact. Returns are the second biggest contact tag after WISMO, so the workload sits with CS while the wait sits with the customer.
* * *
##   

## Solution
* * *
A customer starts a return from their order, on the surfaces they already shop on, instead of contacting CS. The request reaches CS and the warehouse through the returns handling that exists today, so only the way in changes, because the way in is where the contact and the wait begin.

**Expected outcomes**
* * *
*   Customers start a return without contacting CS
*   Return requests reach CS already started

#### **References**
* * *
Flows
*   [Self-serve return (proposed)](<figma-url>)
* * *
##   

## Requirements
* * *
**Return window**
* * *
- [] The return window is `30 days` from delivery

**Surfaces**
* * *
- [] The return flow is available on `Web`, `iOS` and `Android`
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **Start a return from an order inside the window**
* * *
*   **Given** a customer is viewing an order delivered within the return window
*   **When** they start a return from that order
*   **Then** the return request is created without a contact to CS
*   **And** the customer sees that the request was received
* * *
- [] _Mark as done, if the criteria are met_

2 ) **No return is offered once the window has ended**
* * *
*   **Given** a customer is viewing an order whose return window has ended
*   **When** they look for a way to return it
*   **Then** no return can be started from that order
*   **And** the customer is told the window has ended
* * *
- [] _Mark as done, if the criteria are met_

3 ) **CS can handle a request the customer started**
* * *
*   **Given** a customer has started a return
*   **When** a CS agent opens returns in Admin
*   **Then** the request is there to handle
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

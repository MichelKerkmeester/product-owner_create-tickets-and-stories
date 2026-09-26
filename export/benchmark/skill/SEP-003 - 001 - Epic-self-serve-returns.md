# Epic - Customer - Self-serve returns

* * *
## About
* * *
Signed-in customers on web, iOS and Android start their own returns inside the return window. Four child stories follow one return to refund, guest returns follow later and pallet items stay with CS.

#### Problem
* * *
Today CS creates each return in Admin and emails a label, the warehouse checks the item and the agent refunds it. CS handles about `1,900` return requests a month this way, and a refund takes `6 days` on average from first contact.

**The following issues rise from that:**
*   Every return costs a CS contact, even for just a label
*   Return volume turns directly into agent time
*   The customer cannot see return status without contacting CS again
####   

#### Goal
* * *
CS stops creating returns by hand, and by the end of Q1 2027 at least `60%` of returns start without a CS contact.

**Direct customer and Fernhouse benefits:**
*   Customers start a return at any time from order history
*   CS time moves to pallet items, guest orders and other contacts needing an agent
####   

#### Solution
* * *
In order to get there, we will:
*   Let signed-in customers start a return from order history with items and a reason, inside the `30 days` window
*   Email a return label once the return starts
*   Show the return status on the order page
*   Refund after the warehouse checks the items
*   Keep pallet item returns out of self-serve and with CS

#### **References**
* * *
Context
*   [Fernhouse company context](<../context/fernhouse-context.md>)

## Scope
* * *
Each child story owns one part of the lifecycle.

#### Starting a return
* * *
*   Customer - Returns - Start a return from order history
*   Customer - Returns - Return label by email

#### After the return is sent
* * *
*   Customer - Returns - Return status on the order page
*   Customer - Returns - Refund after the warehouse check

#### Added Later
* * *
Capabilities that belong to the epic but do not block the first release.

**Guest returns**
*   Guest checkout customers start a return without an account
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A signed-in customer starts a return without contacting CS**
* * *
*   **Given** a signed-in customer on web, iOS or Android with a delivered order inside the `30 days` window
*   **When** they start a return in order history with items and a reason
*   **Then** the return exists without a CS agent creating it
*   **And** the customer receives a return label by email
* * *
- [] _Mark as done, if the criteria are met_

2\. **The customer follows the return to the refund**
* * *
*   **Given** a customer started a return themselves
*   **When** they open the order page on web, iOS or Android
*   **Then** they see the return's current status
*   **And** they are refunded after the warehouse check, without contacting CS
* * *
- [] _Mark as done, if the criteria are met_

3\. **Returns outside the self-serve scope stay with CS**
* * *
*   **Given** an item delivered more than `30 days` ago, a pallet item or an item from a guest order
*   **When** the customer wants to return it
*   **Then** self-serve return is unavailable
*   **And** its return goes through CS as it does today
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

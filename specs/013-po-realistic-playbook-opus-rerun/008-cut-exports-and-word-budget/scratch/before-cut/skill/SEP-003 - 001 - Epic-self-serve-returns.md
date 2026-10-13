# Epic - Customer - Self-serve returns

* * *
## About
* * *
Signed-in customers on web, iOS and Android can start a return themselves inside the return window, instead of contacting CS and waiting for an agent to create it in Admin. The epic is split into four child stories that follow one return from request to refund. Guest returns follow in a later release, and pallet items stay with CS.

### Problem
* * *
There is no self-serve return today. A customer who wants to return something must contact CS, a CS agent creates the return in Admin and emails a return label, the warehouse checks the item and the agent refunds it. CS handles about `1,900` return requests a month this way, and a refund takes `6 days` on average from the first contact.

**The following issues rise from that:**
*   Every return costs at least one CS contact, even when the customer only wants a label
*   CS agents create each return by hand in Admin, so return volume turns directly into agent time
*   The customer cannot see where the return stands and has to contact CS again to find out
###   

### Goal
* * *
Signed-in customers start their own returns, so CS stops creating returns by hand in Admin. By the end of Q1 2027, at least `60%` of returns start without a CS contact.

**Direct customer and Fernhouse benefits:**
*   Customers start a return at any time from their order history, without waiting for a CS reply
*   CS time moves from creating returns to the contacts that need an agent, such as pallet items and guest orders
###   

### Solution
* * *
In order to get there, we will:
*   Let a signed-in customer start a return from order history on web, iOS and Android, choosing items and a reason, inside the `30 days` return window
*   Email the customer a return label once the return is started
*   Show the return status on the order page, so the customer can follow the return without contacting CS
*   Refund the customer after the warehouse has checked the returned items
*   Keep pallet items out of self-serve, so their returns stay with CS

#### **References**
* * *
Context
*   [Fernhouse company context](<../context/fernhouse-context.md>)

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria. Pallet items stay with CS in every story.

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
*   Customers who checked out as a guest start a return themselves, without an account or order history
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A signed-in customer starts a return without contacting CS**
* * *
*   **Given** a signed-in customer on web, iOS or Android with a delivered order inside the `30 days` return window
*   **When** they start a return from order history, choosing the items and a reason
*   **Then** the return exists without a CS agent creating it in Admin
*   **And** the customer receives a return label by email
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The customer follows the return to the refund**
* * *
*   **Given** a customer has started a return themselves
*   **When** they open the order page on web, iOS or Android
*   **Then** they see the current status of the return
*   **And** they are refunded after the warehouse has checked the returned items, without contacting CS
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Returns outside the self-serve scope stay with CS**
* * *
*   **Given** an item delivered more than `30 days` ago, a pallet item or an item from an order placed as a guest
*   **When** the customer wants to return it
*   **Then** they cannot start a self-serve return for it
*   **And** its return goes through CS as it does today
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

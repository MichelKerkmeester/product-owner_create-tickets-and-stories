# Epic - Customer - Self-serve returns

* * *
## About
* * *
Self-serve returns lets signed-in customers on web, iOS and Android start a return from their order history within the `30 days` return window. They get the return label by email, follow the return on the order page and receive the refund once the warehouse has checked the items.
This Epic is split into four child stories. Each one owns one part of the return lifecycle and carries its own detailed requirements and acceptance criteria.

### Problem
* * *
Customers cannot start a return themselves today. Every return starts with a CS contact. The customer writes in, a CS agent creates the return in Admin and emails a return label, the warehouse checks the item, and then the agent issues the refund. CS handles about `1,900` return requests a month this way, and a refund takes `6 days` on average from the first contact.

**The following issues rise from that:**
*   Every return costs a CS contact, about `1,900` a month
*   A customer who wants to return an item has to wait for an agent before anything happens
*   CS agents create every return by hand in Admin and email every label themselves
*   The order page stops at `Shipped`, so a customer cannot see where a return stands
###   

### Goal
* * *
By the end of Q1 2027, at least `60%` of returns start without a CS contact. To get there, signed-in customers on web, iOS and Android start their own returns inside the return window, and CS stops creating returns by hand in Admin.

**Direct user/Fernhouse benefits:**
*   Customers start a return whenever they want, without waiting for a CS reply
*   Customers see where their return stands on the order page
*   CS agents stop creating returns and emailing labels by hand
*   Return contacts no longer take up CS time
###   

### Solution
* * *
In order to get there, we will:
*   Let a signed-in customer start a return from order history, choosing the items and a reason
*   Email the return label to the customer once the return is started
*   Show the return's status on the order page
*   Issue the refund after the warehouse has checked the returned items

## Scope
* * *
Each child story owns one part of the return lifecycle and carries its own detailed requirements and acceptance criteria. Returns of pallet items stay with CS and are not part of this epic.

#### Starting a return
* * *
*   Customer - Self-serve returns - Start a return from order history
*   Customer - Self-serve returns - Return label by email

#### After the return is sent
* * *
*   Customer - Self-serve returns - Return status on the order page
*   Customer - Self-serve returns - Refund after the warehouse check

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release.

**Guest returns**
*   A customer who checked out as a guest starts a return themselves, even though guests have no order history to start it from
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A signed-in customer starts a return without contacting CS**
* * *
*   **Given** a signed-in customer on web, iOS or Android with an order delivered within the last `30 days`
*   **When** they choose the items and a reason from their order history
*   **Then** the return is created without any CS contact
*   **And** no CS agent creates that return by hand in Admin
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A return cannot start outside the return window**
* * *
*   **Given** a signed-in customer with an order delivered more than `30 days` ago
*   **When** they open that order in their order history
*   **Then** the order offers no self-serve return
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The customer gets the return label without asking for it**
* * *
*   **Given** a customer who has started a self-serve return
*   **When** the return is created
*   **Then** the customer receives the return label by email
*   **And** no CS agent sends that label by hand
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **The customer can follow the return through to the refund**
* * *
*   **Given** a started self-serve return
*   **When** the customer opens the order on web, iOS or Android
*   **Then** the order page shows where the return currently stands
*   **And** the refund is issued only after the warehouse has checked the returned items
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Pallet items stay with CS**
* * *
*   **Given** a signed-in customer with a pallet item in a delivered order
*   **When** they look for a return in their order history
*   **Then** the pallet item cannot be returned through self-serve, and its return stays with CS
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

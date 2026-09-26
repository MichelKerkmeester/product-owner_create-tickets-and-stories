# Epic - Customer - Self-serve returns

* * *
## About
* * *
Signed-in customers on web, iOS and Android start a return from order history within the `30 days` window, get the label by email, track it on the order page and get refunded after the warehouse check. Four child stories each own one part.

#### Problem
* * *
Every return starts with a CS contact, and an agent creates it in Admin, emails a label and refunds after the warehouse check. A refund takes `6 days` on average from first contact.

**The following issues rise from that:**
*   Every return costs a CS contact, about `1,900` a month
*   Customers wait for an agent before anything happens
*   Agents create every return and email every label by hand
*   The order page stops at `Shipped`, hiding where a return stands
####   

#### Goal
* * *
By the end of Q1 2027, at least `60%` of returns start without CS, and CS stops creating returns by hand.

**Direct user/Fernhouse benefits:**
*   Customers start returns anytime, without waiting for CS
*   Customers see their return's status on the order page
*   CS stops creating returns and emailing labels, freeing time from return contacts
####   

#### Solution
* * *
In order to get there, we will:
*   Let signed-in customers start a return from order history, with items and a reason
*   Email the label once the return starts
*   Show the return's status on the order page
*   Refund after the warehouse checks the items

## Scope
* * *
Each child story carries its own requirements and criteria. Pallet item returns stay with CS, outside this epic.

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
These do not block the first release.

**Guest returns**
*   Guest-checkout customers start returns themselves, though they have no order history
* * *
##   

## Acceptance criteria
* * *
Release-level outcomes, with detailed criteria in each child story.

1\. **A signed-in customer starts a return without contacting CS**
* * *
*   **Given** a signed-in web, iOS or Android customer with an order delivered in the last `30 days`
*   **When** they pick items and a reason in order history
*   **Then** the return is created with no CS contact
*   **And** no agent creates it by hand in Admin
* * *
- [] _Mark as done, if the criteria are met_

2\. **A return cannot start outside the return window**
* * *
*   **Given** a signed-in customer with an order delivered more than `30 days` ago
*   **When** they open that order in their order history
*   **Then** it offers no self-serve return
* * *
- [] _Mark as done, if the criteria are met_

3\. **The customer gets the return label without asking for it**
* * *
*   **Given** a customer starting a self-serve return
*   **When** the return is created
*   **Then** they get the label by email
*   **And** no agent sends it by hand
* * *
- [] _Mark as done, if the criteria are met_

4\. **The customer can follow the return through to the refund**
* * *
*   **Given** a started self-serve return
*   **When** the customer opens the order on web, iOS or Android
*   **Then** the page shows where the return stands
*   **And** the refund comes only after the warehouse check
* * *
- [] _Mark as done, if the criteria are met_

5\. **Pallet items stay with CS**
* * *
*   **Given** a signed-in customer with a delivered pallet item
*   **When** they look for a return
*   **Then** the pallet item has no self-serve return and stays with CS
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

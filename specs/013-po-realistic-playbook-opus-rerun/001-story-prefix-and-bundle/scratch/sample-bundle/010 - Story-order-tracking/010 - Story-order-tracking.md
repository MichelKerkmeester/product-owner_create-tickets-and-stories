# Shopper - Orders - Order tracking

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A shopper who wants to know where an order is has to ask support today. This story gives every order a status timeline on its detail screen, so the shopper can check progress at any time and support hears only about orders that are stuck.

### Problem
* * *
Shoppers cannot see where an order is:
*   The order detail screen shows the order date and nothing after it
*   Support answers the same where-is-my-order question many times a day
* * *

### Solution
* * *
Show the order's progress where the shopper already looks for it. The detail screen gains a timeline fed by the carrier's status updates, and an order that stops moving says so on its own, because a shopper who has to ask about a delay has already lost trust in the date.
* * *

#### **Expected outcomes**
* * *
*   Fewer support requests asking where an order is
*   Shoppers learn about a delay before they have to ask
* * *

#### **Tasks**
* * *
*   [Orders - Order status API](<010.1 - task-order-status-api.md>)
*   [Orders - Order tracking screen](<010.2 - task-order-tracking-screen.md>)
* * *
##   

## Requirements
* * *
**Status timeline**
* * *
*   The timeline shows `Paid`, `Packed`, `Shipped` and `Delivered`, in that order
*   A status with no newer one after `48 hours` is marked `Delayed`
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The shopper can see where an order is**
* * *
*   **Given** a shopper with an order that has shipped
*   **When** they open the order
*   **Then** the timeline shows every status the order has reached, and the latest one is clear at a glance
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A stuck order is flagged without a support request**
* * *
*   **Given** an order that has not moved past its latest status within the delay limit
*   **When** the shopper opens the order
*   **Then** the order reads as delayed, so the shopper knows before they have to ask
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

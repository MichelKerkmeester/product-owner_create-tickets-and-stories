# Brand - Payouts - Pause payout

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A brand can pause a pending payout when it needs to hold it. The pause carries a reason, lasts a fixed time and releases on its own, so the brand never has to remember to undo it.

### Problem
* * *
A brand that needs to hold a pending payout has no way to do it. The payout goes out on its normal course even when the brand needs time first.

### Solution
* * *
Give the brand a Pause payout control on a pending payout. Pausing asks for a reason, holds the payout for a fixed period and marks the payout as paused in the list. When the period ends the hold lifts by itself, because a hold that needs a manual release is a hold a brand can forget and leave a creator waiting.

#### **Expected outcomes**
* * *
*   A brand can hold a pending payout without contacting anyone
*   Every pause has a recorded reason
*   A paused payout resumes on its own without brand action
* * *
##   

## Requirements
* * *
**Pause duration**
* * *
*   A pause lasts exactly `24 hours`

**Reason**
* * *
*   The reason field is required to pause a payout

**Pause control**
* * *
*   The toggle label reads `Pause payout`

**Payout row**
* * *
*   A paused payout shows a `paused` badge on its row
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **Pause a pending payout with a reason**
* * *
*   **Given** a brand has a pending payout
*   **When** the brand turns on the pause and gives a reason
*   **Then** the payout is held and its row shows it as paused
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A pause without a reason is refused**
* * *
*   **Given** a brand has started to pause a pending payout
*   **When** the reason is left empty and the brand confirms
*   **Then** the payout is not paused
*   **And** the brand is told a reason is needed, and anything already entered is kept
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The pause releases on its own**
* * *
*   **Given** a payout has been paused and the hold period has run out
*   **When** the hold period ends
*   **Then** the payout is released with no action from the brand
*   **And** the row no longer shows it as paused
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

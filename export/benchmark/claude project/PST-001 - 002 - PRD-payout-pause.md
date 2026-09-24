# Brand - Payouts - Payout pause

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story gives brands a way to pause a pending payout. It covers the pause control, the required reason, the automatic release and how a paused payout shows on the payout row.

### Problem
* * *
A brand that needs to hold a pending payout has no way to pause it.

### Solution
* * *
A brand pauses a pending payout when it needs to hold it. The payout releases when the hold ends, so nobody has to remember to switch the pause off, and the payout row shows which payouts are paused.

#### **Expected outcomes**
* * *
*   Brands hold a pending payout when they need to, without waiting on anyone else
*   Held payouts release automatically, and the payout row shows which payouts are held
* * *
##  

## Requirements
* * *
**Payout pause**
* * *
*   The toggle label reads `Pause payout`
*   The reason field is required
*   The pause lasts exactly `24 hours`

**Payout row**
* * *
*   A paused payout shows a `paused` badge
* * *
##  

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A paused payout releases by itself**
* * *
*   **Given** a brand has a payout pending
*   **When** the brand pauses the payout, supplying a reason
*   **Then** the payout releases automatically when the hold ends
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Paused payouts are visible on the payout row**
* * *
*   **Given** a payout is paused
*   **When** the brand views the payout row
*   **Then** the payout row shows the payout as paused
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##  

# Brand - Payouts - Payout pause

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story gives a brand a way to pause a payout that is still pending, so the payout waits while the brand needs it held. The pause runs for a set time and ends by itself when the time is up.

### Problem
* * *
A payout that is pending leaves on its own schedule. When a brand needs to hold one, there is no way to do that today.

### Solution
* * *
Pending payouts gain a pause. A brand pauses the payout and records why, and the release resumes when the pause runs out.

#### **Expected outcomes**
* * *
*   A brand can pause a payout that has not released yet, whenever it needs to
*   The paused payout releases again when the pause ends, with no one acting
* * *
##   

## Requirements
* * *
**Pending payout pause**
* * *
*   A pause of a pending payout lasts exactly `24 hours`
*   The reason field is required
*   The toggle that starts a pause reads `Pause payout`
*   The payout row of a paused payout shows a `paused` badge
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A brand pauses a payout that has not released**
* * *
*   **Given** a payout that is still pending
*   **When** the brand pauses it
*   **Then** the payout waits instead of releasing
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The payout releases when the pause ends**
* * *
*   **Given** a payout that is paused
*   **When** the pause ends
*   **Then** the payout releases on its own
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

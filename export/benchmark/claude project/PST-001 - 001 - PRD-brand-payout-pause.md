# Brand - Payouts - Pause payout

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A brand can hold a pending payout by pausing it. The pause lasts a fixed window, ends on its own and needs a stated reason, so a brand can stop a payout it is unsure about without having to remember to restart it.

### Problem
* * *
A brand that needs to hold a pending payout has no way to do it. The payout stays pending and goes out on schedule, so the brand cannot stop it while it checks the details.

### Solution
* * *
Give the brand a Pause payout control on each pending payout. Pausing asks for a reason, marks the payout as paused in the list and holds it for a fixed window. When the window ends the payout is released without any action from the brand, because a hold that needs a manual restart would strand payouts nobody remembers to release.

#### **Expected outcomes**
* * *
*   Brands can hold a pending payout while they check it
*   Every pause carries a recorded reason
*   Paused payouts are released without manual follow-up

## Requirements
* * *
**Pause window**
* * *
*   Only a pending payout can be paused
*   The pause lasts exactly `24 hours`
*   The pause releases automatically when the `24 hours` end

**Reason**
* * *
*   The reason field is required
*   A payout cannot be paused while the reason is empty

**Pause toggle**
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

1\. **Hold a pending payout**
* * *
*   **Given** a brand has a pending payout
*   **When** the brand pauses it and gives a reason
*   **Then** the payout is held and does not go out while the pause lasts
*   **And** the payout row shows that it is paused
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A pause always has a reason**
* * *
*   **Given** a brand is pausing a pending payout
*   **When** the reason is left empty
*   **Then** the payout is not paused and stays pending
*   **And** the brand can see the reason is needed
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The pause releases automatically after the hold**
* * *
*   **Given** a payout has been paused for the full hold
*   **When** the hold ends
*   **Then** the pause is released and the payout continues as a normal pending payout, with no action from the brand
*   **And** the payout row no longer shows it as paused
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

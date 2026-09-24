```markdown
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
```

**Export-equivalent path:** `export/002 - PRD-payout-pause.md`

**Artifact kind:** Story. The notes name one feature area with hard requirements, so the Story shape resolved; an Epic would need an initiative split across child stories.

**HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.**

**Quality:** voice, house grammar, heading depth and requirement-to-criterion traceability pass. Every supplied hard value lands in Requirements with its wording intact, inside backticks: the `24 hours` duration, the required reason field, the `Pause payout` toggle label and the `paused` badge. Both criteria stay outcome-led and leave the mechanism to the developer, and neither would need editing if a token changed.

**Assumptions you can correct:** the H1 reads `Brand - Payouts - Payout pause`, where `Payouts` as the area segment is my inference, since the notes named no epic or initiative. I read the note's "paused badge" as the literal badge text `paused`, and "the reason field is required" as a reason field the brand fills when pausing. No links were supplied, so `#### **References**` is omitted, and no Delivery section is written because you did not ask for one and nothing in the notes forced it.

**Next step:** say the word if the area segment, the badge text or any value needs adjusting. This session has no ClickUp connector connected, so the artifact is delivered here only.
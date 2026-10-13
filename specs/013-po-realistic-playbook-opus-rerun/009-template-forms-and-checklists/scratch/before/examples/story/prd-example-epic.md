---
title: "Product Owner - Examples - Story - Epic - v0.200"
description: "Instantiates the house PRD shape as an Epic: an About umbrella with Problem, Goal and Solution, a Scope of child stories grouped by lifecycle plus an Added Later group, a few release-level outcome-led Given/When/Then acceptance criteria, and the Delivery close, present because the request asked for a delivery view and sizing, with no Requirements section."
version: "0.200"
contextType: asset
---

# Epic - Gatherwell - Event Check-in v2

* * *
## About
* * *
Check-in v2 rebuilds how organizers admit attendees at the door of a live event, replacing the single scan screen with a flow that also covers manual lookup, offline capture and post-event reconciliation.
This Epic is split into several child stories, each owning one part of the door lifecycle and carrying its own detailed requirements and acceptance criteria.

### Problem
* * *
The current door experience (v1) was built for one small conference and assumes a fast, always-online connection and a clean guest list. At larger venues that assumption breaks the moment the network drops or a ticket is scanned twice, and door staff have no fallback beyond a paper list.

**The following issues rise from that:**
*   Door staff cannot admit anyone while the venue Wi-Fi is down, so queues stall at the entrance
*   A ticket scanned twice looks identical to a first scan, so the same code can admit two people
*   When a scan fails there is no way to find an attendee by name or email
*   Headcounts from different door devices disagree, so organizers never trust the live total
###   

### Goal
* * *
Admit every valid attendee quickly and exactly once, whether or not the door device is online, and give organizers one headcount they can trust.

**Direct user/Gatherwell benefits:**
*   Door staff keep the queue moving even when connectivity drops
*   An attendee is admitted once and only once, on any device
*   Staff can resolve a failed scan without leaving the door
*   Organizers see a single reconciled count they can act on
###   

### Solution
* * *
In order to get there, we will:
*   Rebuild the scan flow so a valid ticket admits in one tap and a reused ticket is stopped with a clear reason
*   Add a manual lookup path that finds an attendee by name or email when a scan cannot be read
*   Capture check-ins locally while offline and reconcile them against the server once connectivity returns
*   Attribute every admission to one door device so counts reconcile to a single total

#### **References**
* * *
Components
*   [Page | Door Check-in](https://www.figma.com/design/EXAMPLE0000/Gatherwell-Check-in-v2?node-id=1-100)
*   [Component | Ticket result card](https://www.figma.com/design/EXAMPLE0000/Gatherwell-Check-in-v2?node-id=1-240)

Flows
*   [Door scan](https://www.figma.com/design/EXAMPLE0000/Gatherwell-Check-in-v2?node-id=2-100)
*   [Manual lookup](https://www.figma.com/design/EXAMPLE0000/Gatherwell-Check-in-v2?node-id=2-200)
*   [Offline capture and sync](https://www.figma.com/design/EXAMPLE0000/Gatherwell-Check-in-v2?node-id=2-300)

## Scope
* * *
Each child story owns one part of the door lifecycle and carries its own detailed requirements and acceptance criteria.

#### Door scan
* * *
*   [Admit an attendee from a valid ticket](https://app.clickup.com/t/000000000/EX-1001)
*   [Stop a duplicate or invalid ticket](https://app.clickup.com/t/000000000/EX-1002)

#### Manual lookup
* * *
*   [Find an attendee by name or email](https://app.clickup.com/t/000000000/EX-1003)
*   [Resolve an attendee the search cannot find](https://app.clickup.com/t/000000000/EX-1004)

#### Offline capture
* * *
*   [Queue check-ins while the device is offline](https://app.clickup.com/t/000000000/EX-1005)
*   [Reconcile the offline queue when connectivity returns](https://app.clickup.com/t/000000000/EX-1006)

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release. Designs for them are still in progress.

**Badge printing**
*   Print a name badge automatically the moment an attendee is admitted

**Group check-in**
*   Admit an entire party from a single ticket in one action

**Live capacity board**
*   Show a venue-wide headcount that updates as each door admits attendees
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Every valid attendee is admitted, and admitted only once**
* * *
*   **Given** a ticket presented at the door of a live event
*   **When** a staff member scans it
*   **Then** a valid ticket admits the attendee in one tap, and a reused, refunded or unrecognized one is refused with the reason named
*   **And** no ticket ever produces a second admission, on that device or any other
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Staff can still admit an attendee when the scan fails**
* * *
*   **Given** a ticket that cannot be read at the door
*   **When** a staff member looks the attendee up by name or email
*   **Then** the attendee can be admitted from the search result without leaving the door
*   **And** that admission carries the same weight as a scanned one everywhere it is counted
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The queue keeps moving when the venue loses connectivity**
* * *
*   **Given** a door device that has gone offline mid-event
*   **When** staff carry on admitting attendees
*   **Then** admissions continue at the same speed and none is lost when connectivity returns
*   **And** a ticket admitted offline on one device cannot be admitted again on another
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Organizers see one headcount they can trust**
* * *
*   **Given** several door devices admitting attendees to the same event
*   **When** their check-ins have synced
*   **Then** the event shows a single total, with each admission attributed to the door that made it
*   **And** that total counts every admitted attendee exactly once
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   Roughly one six-week cycle for two engineers and one designer: door scan and manual lookup in the first half, offline capture and reconciliation in the second

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Barcode symbology: support `QR` and `Code 128` only, and do not build a general-purpose scanner that tries to guess unknown formats

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No attendee self-service kiosk in this epic: every admission goes through a staffed door device
* * *

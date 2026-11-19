# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets members on iOS, Android and Desktop open, read, edit and create pages without a connection. It is available on every plan, Free included. The epic is split into four child stories, one for each area in the offline mode brief. Each story covers iOS, Android and Desktop together.

### Problem
* * *
Loomlist needs a connection for everything beyond the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. Between April and August, 31% of Plus workspaces that gave a cancellation reason named offline access.

**The following issues rise from that:**
*   A member without a connection cannot open any page other than the one on screen
*   An edit made while the connection is gone is retried until the app closes and then lost
*   Some of the `lost-edit` tickets Marta raised in #sync-eng start with a dropped connection
###   

### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online. All four areas ship on iOS, Android and Desktop in Q1 2027, on every plan.

**Direct user/Loomlist benefits:**
*   Members on the move keep reading pages and checking off to-dos when the connection drops
*   Work done offline reaches teammates instead of being lost when the app closes
*   Loomlist answers the offline access reason that 31% of cancelling Plus workspaces gave

**We will know it works when:**
*   The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
###   

### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device with their blocks, inline databases and to-dos, capped at 1 GB including images and files
*   Let members edit blocks, check off to-dos and create pages and to-dos offline, with every change queued on the device in the order it was made
*   Upload queued changes oldest first when the connection returns, following the conflict handling the Sync team settles on 2026-10-09
*   Show members when they are offline and how many changes are waiting to sync, and give them a storage screen where they can see space used, lower the cap and clear offline data

Sharing, inviting, moving a page to another workspace and deleting a page stay online only. This epic does not cover Web, choosing which pages to keep offline, searching pages that are not kept on the device or offline access in the Support console.

## Scope
* * *
Each child story owns one area and carries its own requirements and acceptance criteria for iOS, Android and Desktop.

#### Can start now
* * *
These two stories do not depend on the conflict handling decision, so they can start first.

*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Waits for the conflict handling decision
* * *
Joana, Engineering Manager, Sync, decides on 2026-10-09 how sync-service handles conflicting edits. Today sync-service keeps the version that reaches it last, per block, on protocol v3. That means a phone that was offline for a day can replace a whole morning of a teammate's edits. Neither story below can be finalised before that decision.

*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Members can open and read recent pages without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan
*   **When** they lose the connection
*   **Then** they can open and read the pages they opened most recently, with their blocks, inline databases and to-dos
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Work done offline reaches teammates once the device is back online**
* * *
*   **Given** a member who edited blocks, checked off to-dos or created pages and to-dos without a connection
*   **When** their device is back online
*   **Then** their changes upload in the order they made them and teammates see them
*   **And** no change made offline is lost because the app closed before the connection returned
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Online-only actions show as unavailable offline**
* * *
*   **Given** a member without a connection
*   **When** they reach sharing, inviting, moving a page to another workspace or deleting a page
*   **Then** the control shows as unavailable
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Members can see their offline state and control the storage it uses**
* * *
*   **Given** a member using offline mode on iOS, Android or Desktop
*   **When** they look at the top bar or open the storage settings
*   **Then** they can see whether they are offline and how many changes are waiting to sync
*   **And** they can see the space offline mode uses, lower the cap and clear offline data
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

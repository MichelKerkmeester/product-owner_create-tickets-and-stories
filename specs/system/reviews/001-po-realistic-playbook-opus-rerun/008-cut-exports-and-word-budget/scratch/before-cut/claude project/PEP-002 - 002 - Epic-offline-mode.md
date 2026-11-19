# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets a member open, read, edit and create pages on iOS, Android and Desktop with no connection, on every plan including Free. Web stays online only.

The epic has four child stories, one for each area of the offline mode brief, and each story covers iOS, Android and Desktop together. The target is Q1 2027 for all four stories on all three platforms.

### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. Between April and August, 31% of Plus workspaces that gave a cancellation reason named offline access.

**The following issues rise from that:**
*   A member without a connection cannot open any page except the one already on screen
*   An edit made while the connection is gone is retried until the app closes, then lost, and some `lost-edit` tickets start this way
###   

### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   Members keep working on their recent pages when the connection drops or never arrives
*   Work done offline reaches the workspace instead of disappearing when the app closes
*   The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
###   

### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device with their blocks, inline databases and to-dos, capped at 1 GB, whichever limit comes first
*   Count images and files toward the cap, and remove a page that falls out of the 500 the next time the app has a connection
*   Let members edit blocks, check off to-dos and create pages and to-dos offline, queuing every change on the device in the order it was made
*   Start uploading queued changes within 30 seconds of the connection returning, oldest first
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only, with their controls shown as unavailable offline
*   Add an offline marker in the top bar and a count of changes waiting to sync
*   Add a storage screen in settings where the member sees space used, lowers the 1 GB cap and clears offline data

## Scope
* * *
Each child story owns one area of offline mode, covers iOS, Android and Desktop together and carries its own detailed requirements and acceptance criteria.

Conflict handling is not settled: Joana, Engineering Manager, Sync, decides how sync-service handles conflicting edits on 2026-10-09, choosing between the options in the #sync-eng thread. Today sync-service resolves every overlap with block-level last-writer-wins on protocol v3, so a device that was offline for a day can replace a whole morning of a teammate's edits.

Offline reading and the indicator do not depend on that decision, so they can start first.

#### Starts before the conflict decision
* * *
*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Finalised after the conflict decision
* * *
*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect

#### Out of scope
* * *
*   Web, because a browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case
*   Choosing which pages to keep offline
*   Searching pages that are not kept on the device
*   Offline access in the Support console
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Recent pages open without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan including Free, with no connection
*   **When** they open a page the device keeps offline
*   **Then** the page opens with its blocks, inline databases and to-dos
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Work done offline reaches the workspace**
* * *
*   **Given** a member with no connection
*   **When** they edit blocks, check off to-dos or create pages and to-dos
*   **Then** every change is kept on the device in the order it was made, even if the app closes before the connection returns
*   **And** once the device is back online, members who can open those pages see every change that did not conflict with another edit
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Online-only actions show as unavailable offline**
* * *
*   **Given** a member with no connection
*   **When** they reach for sharing, inviting, moving a page to another workspace or deleting a page
*   **Then** each of those controls shows as unavailable
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Members can see their offline state and manage storage**
* * *
*   **Given** a member on iOS, Android or Desktop
*   **When** the device has no connection
*   **Then** they can see that they are offline and how many changes are waiting to sync
*   **And** from settings they can see the space offline data uses, lower the cap and clear offline data
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

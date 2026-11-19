# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets members on iOS, Android and Desktop open, read, edit and create pages without a connection. Their changes reach everyone else once the device is back online. It is available on every plan, Free included, and the target is Q1 2027 for all four areas on all three platforms.
This Epic is split into four child stories, one per area, and each story covers iOS, Android and Desktop together. Web is out of scope, because a browser tab cannot be relied on to keep a local copy between visits and Desktop covers the laptop case. Also out of scope: choosing which pages to keep offline, searching pages that are not kept on the device and offline access in the Support console.

### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

**The following issues rise from that:**
*   A member without a connection can't open any page other than the one on screen
*   An edit made while the connection is gone is retried until the app closes and then lost, which is how some of the `lost-edit` tickets Marta raised in #sync-eng start
*   Offline editing under today's sync rules would add a new way to lose work. sync-service resolves every overlap with block-level last-writer-wins on protocol v3, so a phone that was offline for a day can replace a whole morning of a teammate's edits, and the replaced edits never appear in page history
###   

### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   Members on the move keep reading pages and checking off to-dos when the connection drops
*   Work done offline reaches teammates instead of being lost when the app closes
*   Plus workspaces that cancel over missing offline access get that access

**How we will know it works:**
*   The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
###   

### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device with their blocks, inline databases and to-dos, capped at 1 GB, whichever limit comes first
*   Let members edit blocks, check off to-dos and create pages and to-dos with no connection, and queue every change on the device in the order it was made
*   Upload queued changes, oldest first, when the connection returns, using whichever conflict-handling option Joana chooses on 2026-10-09
*   Show members when they are offline, how many changes are waiting to sync and how much space offline data uses

## Scope
* * *
Each child story owns one area and covers iOS, Android and Desktop together. It carries its own detailed requirements and acceptance criteria.

#### Starts before the conflict decision
* * *
*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Waits on the conflict decision
* * *
Joana, Engineering Manager, Sync, decides how sync-service handles conflicting edits on 2026-10-09. These two stories can't be finalised until that decision is made.

*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Recently opened pages open without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, in a workspace on any plan, Free included
*   **When** their device has no connection and they open a page they opened recently
*   **Then** the page opens with its blocks, inline databases and to-dos
*   **And** offline data never uses more space than the member's storage limit
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Work done offline is kept**
* * *
*   **Given** a member whose device has no connection
*   **When** they edit blocks, check off to-dos or create pages and to-dos
*   **Then** every change is kept on the device in the order it was made
*   **And** closing the app before the connection returns loses none of those changes
*   **And** sharing, inviting, moving a page to another workspace and deleting a page show as unavailable
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Teammates see offline changes once the device is back online**
* * *
*   **Given** a device with changes waiting to sync
*   **When** its connection returns
*   **Then** the changes start uploading, oldest first
*   **And** everyone who can open the changed pages sees those changes
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Members can see and control offline mode**
* * *
*   **Given** a member on iOS, Android or Desktop
*   **When** their device loses its connection
*   **Then** the top bar marks them as offline and shows how many changes are waiting to sync
*   **And** from settings they can see the space offline data uses, lower the storage limit and clear offline data
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

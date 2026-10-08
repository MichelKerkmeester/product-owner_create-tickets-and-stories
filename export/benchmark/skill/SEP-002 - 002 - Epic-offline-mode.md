# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages without a connection, on any plan, Free included. It splits into four child stories, one per area in the offline brief.

#### Problem
* * *
Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. Of the Plus workspaces that gave a cancellation reason between April and August, 31% named offline access.

**The following issues rise from that:**
*   Pages other than the one on screen do not open without a connection
*   Edits made without a connection are retried until the app closes, then lost
*   Some lost-edit tickets raised by Support start with a dropped connection
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection on any plan, and everyone else sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   Members keep working on iOS, Android and Desktop when the connection drops
*   Edits made without a connection upload when the connection returns, instead of being lost
*   The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
####   

#### Solution
* * *
Because only the open page works without a connection today, the device keeps the most recently opened pages, bounded by 500 pages and 1 GB, whichever limit comes first. Members can lower that limit and clear offline data from a storage screen in settings.

Members edit while offline, and each change queues on the device in the order it was made. The queue uploads when the connection returns, and how overlapping edits resolve stays open until the conflict decision lands.

Sharing, inviting, moving a page to another workspace and deleting a page stay online only, so their controls show as unavailable offline. Choosing which pages stay offline, searching pages not kept on the device, offline access in the Support console and Web stay out of this epic.

## Scope
* * *
Each child story owns one area and carries its own detailed requirements and acceptance criteria. Offline reading and the offline indicator can start first, because the conflict decision does not block them. Offline editing and creation and offline sync cannot be finalized until Joana's conflict decision lands on 2026-10-09.

#### Child stories
* * *
*   Member - Offline reading - Read kept pages
*   Member - Offline editing and creation - Edit and create without a connection
*   Member - Offline sync - Upload queued changes on reconnect
*   Member - Offline indicator and storage - Indicator and storage screen
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Members read kept pages on any plan without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan, who has opened a page while online
*   **When** the connection is gone
*   **Then** that page opens with its blocks, inline databases and to-dos
* * *
- [] _Mark as done, if the criteria are met_

2\. **Edits made without a connection are kept and reach others once the device is back online**
* * *
*   **Given** a member with no connection on iOS, Android or Desktop
*   **When** they edit blocks, check off to-dos or create pages and to-dos
*   **Then** each change is kept on the device in the order it was made
*   **And** other members see the change once the device is back online
* * *
- [] _Mark as done, if the criteria are met_

3\. **Sharing, inviting, moving and deleting stay online only**
* * *
*   **Given** a member with no connection
*   **When** they look at the sharing, invite, move or delete controls for a page
*   **Then** those controls show as unavailable
* * *
- [] _Mark as done, if the criteria are met_

4\. **Queued changes upload within 30 seconds of the connection returning**
* * *
*   **Given** changes waiting on the device
*   **When** the connection returns
*   **Then** queued changes start uploading within 30 seconds
*   **And** they upload oldest first
* * *
- [] _Mark as done, if the criteria are met_

5\. **Members see the offline marker and how many changes wait to sync**
* * *
*   **Given** a member with no connection
*   **When** they look at the top bar
*   **Then** a small offline marker shows
*   **And** the count of changes waiting to sync is visible
* * *
- [] _Mark as done, if the criteria are met_

6\. **Members manage offline storage from settings**
* * *
*   **Given** a member on any plan
*   **When** they open the storage screen in settings
*   **Then** it shows the space offline data uses
*   **And** it lets them lower the offline cap and clear offline data
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

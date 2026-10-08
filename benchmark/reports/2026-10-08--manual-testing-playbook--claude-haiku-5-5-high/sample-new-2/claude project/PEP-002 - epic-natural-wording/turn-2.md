```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets members on iOS, Android and Desktop open, read, edit and create pages without a connection, on every plan, Free included. The change is split into four child stories, one for each area of the offline lifecycle, and each child story covers iOS, Android and Desktop together.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. Of the Plus workspaces that gave a cancellation reason between April and August, 31% named offline access.

**The following issues rise from that:**
*   The app cannot open another page without a connection, so the member is stuck on the page already on screen
*   An edit made while the connection is gone is retried until the app closes and then lost
*   Some `lost-edit` tickets raised in Support start with a dropped connection
*   Sync-service resolves overlapping edits with block-level last-writer-wins, so a phone offline for a day can replace a whole morning of a teammate's edits
####   

#### Goal
* * *
Members on iOS, Android and Desktop can open, read, edit and create pages without a connection, on any plan. Everyone else sees their changes once the device is back online, and all four areas ship for Q1 2027.

**Direct user/Barter benefits:**
*   Members on the move keep checking off to-dos and reading pages through a dropped connection
*   Edits made offline reach the workspace instead of disappearing
*   Support sees fewer `lost-edit` tickets caused by a dropped connection

**How we will know it works:**
*   The share of mobile sessions that hit the no-connection screen halves within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device, with their blocks, inline databases and to-dos, capped at 1 GB, whichever limit comes first
*   Let members edit blocks, check off to-dos and create pages and to-dos with no connection, queuing each change in the order it was made
*   Start uploading queued changes within 30 seconds of the connection returning, oldest first
*   Settle how overlapping edits resolve, an open decision named in Scope
*   Show a small offline marker in the top bar and a count of changes waiting to sync
*   Add a storage screen in settings that shows space used, lets members lower the 1 GB cap and clears offline data

Images and files count toward the 1 GB cap, and a page that falls out of the 500 is removed the next time the app has a connection. Sharing, inviting, moving a page to another workspace and deleting a page stay online only, and their controls show as unavailable offline.

Web, choosing which pages stay offline, searching pages not kept on the device and offline access in the Support console are out of scope.

## Scope
* * *
Each child story owns one of the four areas and carries its own detailed requirements and acceptance criteria.

#### Child stories
* * *
*   Platform - Offline reading - Open kept pages without a connection
*   Platform - Offline editing - Edit, check off and create without a connection
*   Platform - Sync on reconnect - Upload queued changes when the connection returns
*   Platform - Offline controls - Indicator and storage settings

Offline editing and sync on reconnect wait on the conflict decision that Joana, Engineering Manager, Sync, makes on 2026-10-09. Offline reading and the indicator do not depend on it and can start first.
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Members read kept pages with no connection, on any plan**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan, has opened a page while online
*   **When** the connection is gone
*   **Then** the page opens from the device with its blocks, inline databases and to-dos
*   **And** the page does not fall back to a no-connection screen
* * *
- [] _Mark as done, if the criteria are met_

2\. **Members edit and create without a connection, and no change is lost**
* * *
*   **Given** a member on iOS, Android or Desktop is offline
*   **When** they edit a block, check off a to-do or create a page
*   **Then** the change shows on the device at once
*   **And** the change waits in a queue in the order it was made
*   **And** the change is kept until it uploads, instead of being lost when the app closes
* * *
- [] _Mark as done, if the criteria are met_

3\. **Sharing and deletion stay online only**
* * *
*   **Given** a member is offline
*   **When** they open the controls to share, invite, move or delete a page
*   **Then** each of those controls shows as unavailable
* * *
- [] _Mark as done, if the criteria are met_

4\. **Queued changes start uploading when the connection returns**
* * *
*   **Given** changes are waiting on a device
*   **When** the connection returns
*   **Then** the queued changes start uploading, oldest first
* * *
- [] _Mark as done, if the criteria are met_

5\. **Members see when they are offline and what is waiting**
* * *
*   **Given** a member is offline with changes waiting to sync
*   **When** they look at the top bar
*   **Then** a small offline marker shows
*   **And** the count of changes waiting to sync is shown
* * *
- [] _Mark as done, if the criteria are met_

6\. **Members control the space that offline data takes**
* * *
*   **Given** a member opens the storage screen in settings
*   **When** they clear offline data
*   **Then** the offline data is removed from the device
*   **And** the storage screen shows the space in use
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-offline-mode.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The Epic has four child stories, one per area in Oskar's brief, each covering iOS, Android and Desktop. It has six release-level criteria, and Free is covered in the About and in the first criterion.

Please check these additions, since I made them rather than took them from your answers:
- The child story titles are my proposal, so rename them freely.
- The title uses the Platform segment, because the scope spans three platforms.
- Conflict handling is drafted now and named as an open dependency in Scope. I did not hold it for Joana's 2026-10-09 decision. Tell me if you want it held.
- The brief does not say where Desktop's offline store lives, in the web client it wraps or in the native shell. I left it open, so the Desktop work in each child has to settle it.
- The Epic has no References or Delivery section, because you supplied no links and nothing forced a delivery view.
- The lower-the-cap behavior is not one of the six criteria. It belongs in the storage child story.
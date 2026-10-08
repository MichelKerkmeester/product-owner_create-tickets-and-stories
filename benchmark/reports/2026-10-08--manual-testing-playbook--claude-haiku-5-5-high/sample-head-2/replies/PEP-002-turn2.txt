```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets members on iOS, Android and Desktop keep working when the connection drops, and lets their changes reach every other member once the device is back online.
This Epic is split into four child stories, one for each offline area, and each child story covers iOS, Android and Desktop together.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Today the mobile apps keep the open page on screen but cannot open another page without a connection.

**The following issues rise from that:**
*   Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute
*   In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access
*   An edit made while the connection is gone is retried until the app closes, then lost, and some `lost-edit` tickets start this way
*   Sync-service resolves overlaps with block-level last-writer-wins on protocol v3, so a phone offline for a day can overwrite a teammate's morning of edits
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and every other member sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   Members keep reading and editing when the connection drops, instead of meeting a no-connection screen
*   Edits made offline reach the other members instead of being lost
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device, with their blocks, inline databases and to-dos, capped at 1 GB, whichever limit comes first
*   Let members edit blocks, check off to-dos and create pages and to-dos with no connection, queuing each change in the order it was made
*   Keep sharing, inviting, moving a page and deleting a page online only, and show their controls as unavailable offline
*   Start uploading queued changes within 30 seconds of the connection returning, oldest first
*   Show an offline marker in the top bar and a count of changes waiting to sync
*   Add a storage screen in settings that shows space used, lets the member lower the 1 GB cap and clears offline data
*   Make offline mode available on every plan, Free included

## Scope
* * *
Each child story owns one of the four offline areas and covers iOS, Android and Desktop together.
Offline reading and the offline indicator do not depend on the conflict decision, so they can start first. Offline editing and creation, and sync on reconnect, wait for Joana's decision on 2026-10-09.

Web, choosing which pages stay offline, searching pages not kept on the device and offline access in the Support console stay out of scope.

#### Offline areas
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
*   Platform - Offline mode - Offline indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Pages open, read and edit without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop has opened pages while connected
*   **When** the connection is gone
*   **Then** the member can open and read those pages, and can edit blocks, check off to-dos and create pages and to-dos
* * *
- [] _Mark as done, if the criteria are met_

2\. **Queued changes reach every other member once the device is back online**
* * *
*   **Given** a member has made changes while offline
*   **When** the connection returns
*   **Then** the changes start uploading within 30 seconds, oldest first, and every other member can see them
* * *
- [] _Mark as done, if the criteria are met_

3\. **Offline data stays within its limits**
* * *
*   **Given** a device holds offline pages, images and files
*   **When** the device reaches 500 pages or 1 GB, whichever limit comes first
*   **Then** the device keeps no more than 500 pages and 1 GB of offline data
*   **And** a page that falls out of the 500 is removed the next time the app has a connection
* * *
- [] _Mark as done, if the criteria are met_

4\. **Online-only actions show as unavailable offline**
* * *
*   **Given** a member is offline
*   **When** they look at the controls for sharing, inviting, moving or deleting a page
*   **Then** those controls show as unavailable
* * *
- [] _Mark as done, if the criteria are met_

5\. **Fewer sessions hit the no-connection screen, and fewer edits are lost**
* * *
*   **Given** the release has been live for 8 weeks
*   **When** the share of mobile sessions that hit the no-connection screen is compared with the share before release
*   **Then** that share has dropped by half, and lost-edit tickets that start with a dropped connection have stopped arriving
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: export/NNN - Epic-offline-mode.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Artifact kind is Epic. Oskar's four areas are the four child stories, each covering iOS, Android and Desktop. The Free plan line sits in Solution as your direction.

Please check these additions, which the brief does not state:
- The child story titles follow the house pattern, and the names are mine.
- The two Goal benefit lines are my wording of the brief's goal.
- Criterion 5 uses the brief's two measures. The brief gives no pre-release baseline, so the criterion compares against the share before release.

I drafted now rather than wait for Joana's 2026-10-09 decision. The Scope states that editing and creation and sync wait for it. Tell me if you want the Epic held until that decision lands.

How Desktop keeps its offline copy is not in the brief, so the Epic states the outcome only. The brief excludes Web because a browser tab cannot keep a local copy, and Desktop wraps the web client. That mechanism is still open.

The Epic has no Delivery section because nobody asked for one and nothing in the brief forces it. It has no References section because no links were supplied.
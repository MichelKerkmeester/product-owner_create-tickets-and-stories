```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets members on iOS, Android and Desktop open, read, edit and create pages without a connection, and lets everyone see their changes once the device is back online. It is available on every plan, Free included.

The work splits into four child stories, one per area: offline reading, offline editing and creation, sync on reconnect and the offline indicator with storage settings. Web, choosing which pages stay offline, searching pages that are not kept on the device and offline access in the Support console stay out of scope.

#### Problem
* * *
Today the mobile apps keep the open page on screen but cannot open another page without a connection. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute.

**The following issues rise from that:**
*   An edit made while the connection is gone is retried until the app closes, then lost
*   Some `lost-edit` tickets start with an edit made while the connection was gone
*   A phone offline for a day can replace a whole morning of a teammate's edits
*   Of Plus workspaces that gave a cancellation reason from April to August, 31% named offline access
####   

#### Goal
* * *
Members on iOS, Android and Desktop can open, read, edit and create pages without a connection, and everyone sees their changes once the device is back online. The target is Q1 2027 for all four areas on iOS, Android and Desktop.

**Direct user/Barter benefits:**
*   Members keep reading and checking off to-dos when the connection drops
*   Offline edits leave the device instead of being retried until the app closes
*   Support sees fewer `lost-edit` tickets that start with a dropped connection

**How we will know it works:**
*   The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device, with their blocks, inline databases and to-dos, within a 1 GB cap
*   Let members edit blocks, check off to-dos and create pages and to-dos offline, with changes queued in the order they were made
*   Upload queued changes within 30 seconds of the connection returning, oldest first
*   Show an offline marker in the top bar, a count of changes waiting to sync and a storage screen in settings where members see space used, lower the cap and clear offline data

Images and files count toward the cap. A page that falls out of the 500 is removed the next time the app has a connection. Sharing, inviting, moving a page to another workspace and deleting a page stay online only, and their controls show as unavailable offline.

## Scope
* * *
Each child story owns one part of offline mode, covers iOS, Android and Desktop together, and carries its own detailed requirements and acceptance criteria.

The editing and sync stories wait on the conflict-handling decision due 2026-10-09 from the Sync team. Offline reading and the indicator can start first.

#### Offline use
* * *
*   Platform - Offline mode - Read pages offline
*   Platform - Offline mode - Edit and create offline

#### Reconnect
* * *
*   Platform - Offline mode - Sync on reconnect

#### Visibility and control
* * *
*   Platform - Offline mode - Offline indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Members keep reading, editing and creating without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan, with recently opened pages on the device
*   **When** the connection drops
*   **Then** they can open, read, edit and create those pages and check off to-dos on them
*   **And** sharing, inviting, moving and deleting pages show as unavailable until the connection returns
* * *
- [] _Mark as done, if the criteria are met_

2\. **Queued changes start uploading as soon as the connection returns**
* * *
*   **Given** changes queued on a device while it had no connection
*   **When** the connection returns
*   **Then** the queued changes start uploading within 30 seconds, oldest first
* * *
- [] _Mark as done, if the criteria are met_

3\. **Offline storage stays within its limits**
* * *
*   **Given** a device holding offline pages, images and files
*   **When** the storage cap or the 500-page limit is reached, whichever comes first
*   **Then** the device keeps no more data than the limit allows, and removes a page that falls out of the 500 the next time the app has a connection
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-offline-mode.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Artifact kind: Epic. The body has About, Scope and release-level acceptance criteria. It has no Requirements section, and no Delivery section because nothing requested or forced one. Each Scope bullet is plain text because no child story exists yet, and I invented no links.

Assumptions to correct:

- **Conflict decision:** The editing and sync stories are held on the 2026-10-09 decision. The Epic describes no conflict behavior and writes no criterion for it, because the #sync-eng options were not supplied.
- **References:** Omitted, because no links were supplied. Send the #sync-eng thread, the `lost-edit` tickets or any other links and I will add them.
- **Target:** Q1 2027 is taken from the brief unchanged. Tell me if the sync stories should move when the decision lands.
- **Structure:** The child story titles and the three Scope groups are my proposal under the house title pattern. Rename or strike either.
- **Out of scope:** Web, page selection, search of pages not kept on the device and the Support console come from the brief and sit in About.

Next step: confirm or correct these points. If you would rather hold the whole Epic until 2026-10-09, say so and I will hold it.
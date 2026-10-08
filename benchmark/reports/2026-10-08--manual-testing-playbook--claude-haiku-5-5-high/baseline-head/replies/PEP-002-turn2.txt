```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages without a connection, and sends their changes to everyone once the device is back online. Offline mode is for every plan, Free included.

The work splits into four child stories, one per area of the offline lifecycle, and each child story covers iOS, Android and Desktop together. Web, choosing which pages stay offline, searching pages not kept on the device and offline access in the Support console are out of scope.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

**The following issues rise from that:**
*   Members on iOS and Android cannot open another page without a connection
*   An edit made while the connection is gone is retried until the app closes, then lost
*   Some `lost-edit` tickets start with a dropped connection
*   31% of Plus workspaces that gave a reason name offline access
####   

#### Goal
* * *
Members on iOS, Android and Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online. Target: Q1 2027 for all four areas on iOS, Android and Desktop.

**Direct user/Barter benefits:**
*   Members keep working through a dropped connection on iOS, Android and Desktop
*   Offline mode is available on Free, Plus and Team alike
*   Mobile sessions that reach the no-connection screen fall by half within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device, within a 1 GB cap that images and files count toward
*   Let members edit blocks, check off to-dos and create pages and to-dos with no connection, queuing each change in the order it was made
*   Upload queued changes within 30 seconds of reconnecting, oldest first, and remove pages that fall out of the 500 when online
*   Keep sharing, inviting, moving and deleting pages online only, showing their controls as unavailable offline
*   Show an offline marker in the top bar, a count of changes waiting to sync and a storage screen in settings

## Scope
* * *
Each child story owns one part of the offline lifecycle and carries its own detailed requirements and acceptance criteria. Offline editing and creation and Sync on reconnect cannot be settled until Joana, Engineering Manager, Sync, decides how sync-service handles conflicting edits on 2026-10-09.

#### Keep and read
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### Edit and sync
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Offline reading works on every plan**
* * *
*   **Given** a member on a Free, Plus or Team workspace who has opened a page while connected
*   **When** the device loses its connection
*   **Then** the member can open and read that page and the other pages kept on the device
*   **And** each page keeps its blocks, inline databases and to-dos
* * *
- [] _Mark as done, if the criteria are met_

2\. **Members keep editing and creating through a dropped connection**
* * *
*   **Given** a member with no connection on iOS, Android or Desktop
*   **When** they edit a block, check off a to-do or create a page or to-do
*   **Then** the change is kept on the device
*   **And** the change reaches the workspace after the device reconnects, in the order it was made
* * *
- [] _Mark as done, if the criteria are met_

3\. **Queued changes reach the workspace once the device is back online**
* * *
*   **Given** queued changes on a device that has just reconnected
*   **When** sync starts
*   **Then** the changes start uploading within 30 seconds, oldest first
* * *
- [] _Mark as done, if the criteria are met_

4\. **Members can see that they are offline and what is waiting**
* * *
*   **Given** a member whose device has no connection
*   **When** they look at the top bar
*   **Then** an offline marker shows and the count of changes waiting to sync is visible
* * *
- [] _Mark as done, if the criteria are met_

5\. **Actions that need the server stay unavailable offline**
* * *
*   **Given** a member whose device has no connection
*   **When** they open the controls for sharing, inviting, moving or deleting a page
*   **Then** those controls show as unavailable
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: export/NNN - Epic-offline-mode.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Your answers settle the split and the Free plan. Four child stories, one per area, each covering iOS, Android and Desktop, and the Goal and first criterion cover every plan.

Three points are still open, and the draft handles them as follows:

- **Conflict handling:** not decided until Joana's 2026-10-09 call. The editing and sync stories are marked as waiting on it, and the Epic states no conflict rule or conflict criterion.
- **Desktop storage:** whether Desktop's offline store lives in the web client code or the native shell is still unknown. It belongs in the Desktop work inside the child stories, so the Epic does not depend on it.
- **Success baseline:** the brief gives the 8-week halving target with no baseline, so the Goal states the target only.

These are my additions, not your words, so strike any you disagree with: the "Platform" segment in the title, and the group names "Keep and read" and "Edit and sync". The criteria are drawn from the brief's areas and your plan decision.
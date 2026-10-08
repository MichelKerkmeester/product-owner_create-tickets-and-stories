```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode adds an offline layer to the iOS, Android and Desktop apps on every plan, Free included. Members keep pages readable, queue edits and new pages on the device, and upload them when the connection returns.
This Epic splits that work into four child stories, one per area. Each child story carries its own detailed requirements and acceptance criteria.

#### Problem
* * *
There is no offline mode today, so the mobile apps keep only the open page on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

**The following issues rise from that:**
*   An edit made while the connection is gone is retried until the app closes, then lost
*   Some `lost-edit` tickets Marta raised in #sync-eng start with a dropped connection
*   Protocol v3 resolves overlapping edits by block-level last-writer-wins, so a phone offline for a day can replace a teammate's morning of edits
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, on any plan including Free. Everyone else sees their changes once their device is back online. Success shows as the share of mobile sessions that hit the no-connection screen halving within 8 weeks of release, and `lost-edit` tickets that start with a dropped connection stopping.

**Direct user/Loomlist benefits:**
*   Members keep reading and editing through a dropped connection
*   Edits made offline are kept and uploaded instead of lost when the app closes
####   

#### Solution
* * *
Members on iOS, Android and Desktop get one offline mode across four areas. Recently opened pages stay readable, edits and new pages wait on the device in order, and sync uploads them on reconnect. The target is Q1 2027 for all four areas on iOS, Android and Desktop.

Sharing, inviting, moving a page to another workspace and deleting a page stay online only, and their controls show as unavailable offline. Offline reading and the offline indicator do not depend on the conflict decision and can start first.

The offline editing and sync on reconnect areas wait for the sync-service conflict decision that Joana, Engineering Manager, Sync, makes on 2026-10-09. Web, choosing which pages to keep offline, searching pages that are not on the device and Support console access stay out of this Epic.

## Scope
* * *
Each child story owns one area of offline mode and carries its own detailed requirements and acceptance criteria.

#### Offline reading
* * *
*   Platform - Offline mode - Offline reading
*   Covers the 500 most recently opened pages, with their blocks, inline databases and to-dos, kept on the device
*   Caps offline data at 1 GB, whichever limit comes first, with images and files counting toward the cap
*   Removes a page that falls out of the 500 the next time the app has a connection

#### Offline editing and creation
* * *
*   Platform - Offline mode - Offline editing and creation
*   Covers editing blocks, checking off to-dos and creating pages and to-dos without a connection
*   Queues every change on the device in the order it was made
*   Keeps sharing, inviting, moving a page to another workspace and deleting a page online only, with their controls shown as unavailable offline

#### Sync on reconnect
* * *
*   Platform - Offline mode - Sync on reconnect
*   Starts uploading queued changes within 30 seconds of the connection returning, oldest first
*   Cannot be finalised until the sync-service conflict decision lands, due 2026-10-09

#### Offline indicator and storage settings
* * *
*   Platform - Offline mode - Offline indicator and storage settings
*   Shows a small offline marker in the top bar and a count of changes waiting to sync
*   Adds a storage screen in settings that shows space used, lets the member lower the 1 GB cap and clears offline data
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Members keep reading and editing without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan including Free, who has opened a page recently
*   **When** the device loses its connection
*   **Then** the page opens and its blocks, inline databases and to-dos can be read
*   **And** the member can edit blocks, check off to-dos and create pages and to-dos
* * *
- [] _Mark as done, if the criteria are met_

2\. **Queued changes upload after the connection returns**
* * *
*   **Given** a member on iOS, Android or Desktop who has made changes without a connection
*   **When** the connection returns
*   **Then** the queued changes start uploading without the member doing anything
*   **And** they upload oldest first
*   **And** none is lost when the connection returns
* * *
- [] _Mark as done, if the criteria are met_

3\. **The member can see the offline state**
* * *
*   **Given** a member on iOS, Android or Desktop whose connection has dropped
*   **When** they look at the top bar
*   **Then** an offline marker shows, with a count of changes waiting to sync
* * *
- [] _Mark as done, if the criteria are met_

4\. **The member manages offline storage from settings**
* * *
*   **Given** a member on iOS, Android or Desktop with offline data on the device
*   **When** they open the storage screen in settings
*   **Then** the screen shows the space that offline data uses
*   **And** the member can lower the cap or clear offline data
* * *
- [] _Mark as done, if the criteria are met_

5\. **Sharing and other online-only actions show as unavailable offline**
* * *
*   **Given** a member on iOS, Android or Desktop with no connection
*   **When** they look at the controls for sharing, inviting, moving and deleting a page
*   **Then** those controls show as unavailable
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-offline-mode.md`

Shape: Epic. It has four child stories, one per brief area, each covering iOS, Android and Desktop. It has no Requirements section, because the Epic carries no requirements of its own, and no Delivery section, because nothing in the brief asks for one and no requirement carries an open question.

The hard values (500 pages, 1 GB, 30 seconds) sit in the Scope bullets. They move into the child stories' requirements when each story is drafted.

Additions I made that you can strike or change:

- The title segment `Platform`. I have not confirmed it with you.
- I drafted now rather than waiting for the 2026-10-09 conflict decision. The editing and sync areas say they wait for it, and no criterion asserts how overlapping edits resolve.
- Criterion 1 says "recently opened", and criterion 2 says "none is lost". Both come from the brief's wording and the 500-page cap.
- "Any plan including Free" comes from your instruction. The brief does not say it.
- The Desktop storage mechanism is not in the Epic. The offline reading child story will need to settle it.

Quality status: Epic shape checked by hand against the house grammar and the word budget. No score is given.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
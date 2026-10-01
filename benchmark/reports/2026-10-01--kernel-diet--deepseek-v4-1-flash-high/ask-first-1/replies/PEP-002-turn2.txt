```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode gives Loomlist a way to work without a connection on iOS, Android and Desktop. It ships on every plan, Free included, and Web stays out of scope, because a browser tab cannot be relied on to keep a local copy between visits.

The work splits into four child stories, one per area, and each story carries all three platforms together.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

An edit made while the connection is gone is retried until the app closes, then lost. Some of the `lost-edit` tickets Marta raised in #sync-eng start that way.

**The following issues rise from that:**
*   A member cannot open any page but the one already on screen without a connection
*   An edit made offline is retried until the app closes and then lost
*   A device that reconnects after a day can replace a whole morning of a teammate's edits
*   Nothing in the app says it is offline or how much is waiting to sync
####   

#### Goal
* * *
A member can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   A member keeps working when the connection drops instead of stopping
*   Work made offline survives the app closing
*   Changes made offline reach the rest of the workspace
*   A member can see the app is offline and how much is waiting to sync
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device, with their blocks, inline databases and to-dos, capped at 1 GB
*   Count images and files toward that cap, and drop a page that falls out of the 500 the next time the app is online
*   Let a member edit blocks, check off to-dos and create pages and to-dos with no connection, queueing every change in the order it was made
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only, with their controls unavailable offline
*   Upload queued changes within 30 seconds of the connection returning, oldest first
*   Show an offline marker in the top bar with a count of changes waiting to sync
*   Add a storage screen in settings that shows space used and lets the member lower the cap or clear offline data

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.
The sync conflict decision Joana makes on 2026-10-09 gates Offline editing and creation and Sync on reconnect. Offline reading and the indicator can start first.

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

1\. **A member reads with no connection on any of the three platforms**
* * *
*   **Given** a member on iOS, Android or Desktop who has opened pages before
*   **When** the connection is gone and they open one of the pages the device keeps
*   **Then** the page opens with its blocks, inline databases and to-dos, as it read online
*   **And** the same holds on each of the three platforms
* * *
- [] _Mark as done, if the criteria are met_

2\. **A member edits and creates with no connection, and everyone else sees it after**
* * *
*   **Given** a member whose connection has gone
*   **When** they edit a block, check off a to-do or create a page or a to-do
*   **Then** every change stays on the device in the order it was made and survives the app closing
*   **And** once the device is back online, each change reaches the other members and their devices
* * *
- [] _Mark as done, if the criteria are met_

3\. **A member can see the offline state and decide how much the device holds**
* * *
*   **Given** a device with offline data on it
*   **When** the member looks at the top bar and at the storage screen in settings
*   **Then** the app shows that it is offline, how many changes are waiting to sync and how much space the offline data uses
*   **And** the member can lower the storage limit or clear the offline data, and the app applies it
* * *
- [] _Mark as done, if the criteria are met_

4\. **The connection stops being the reason sessions stop and edits are lost**
* * *
*   **Given** the released offline mode on iOS, Android and Desktop
*   **When** 8 weeks have passed since release
*   **Then** the share of mobile sessions that hit the no-connection screen is half what it was before
*   **And** `lost-edit` tickets that start with a dropped connection stop coming in
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Epic-offline-mode.md`

Artifact kind: Epic.

HVR self-scan: 0 hard blockers. Fixed: the brief's "Support sees it too" transition and the doubled June-to-August date range, which the Problem paragraph now states once each. Kept with reason: the two source-fixed enumerations, "blocks, inline databases and to-dos" and the edit, check-off and create triad, which are the brief's own lists rather than prose rhythm, and the template's own Solution lead "In order to get there, we will:", plus Given, When, Then and And as fixed labels.

Quality status: six dimensions pass. Epic shape carries Problem, Goal, Solution and Scope with no Requirements section, release criteria stay release-level, house grammar and heading depth check out with both `##   ` spacers retained.

Scope is a flat list because one story per area leaves nothing for a second level to group. Four things are my call rather than Oskar's, so strike any you disagree with. The title segment reads `Platform` because the work lands on three platforms. Plan coverage sits in About as scope, so Free is stated where the platforms are. The brief's hard values, the 500 pages, the 1 GB cap, the 30 seconds and the queue order, sit in Solution because an Epic delegates its constraints to child stories, and each story will hold the formal items. No `## Delivery` section was written, so the sync conflict decision appears in Scope as a gate on the two dependent stories instead.

Next: Offline reading is the story that does not wait on the sync decision, so it is the cheapest one to cut first.
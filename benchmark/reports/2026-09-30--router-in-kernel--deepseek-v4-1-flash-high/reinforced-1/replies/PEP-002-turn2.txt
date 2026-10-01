```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member keep working in Loomlist when the connection drops. The device keeps the pages they have opened, holds every change they make until the connection returns and shows them what is waiting to sync.
This Epic is split into four child stories, one for each part of Offline mode. Each story covers iOS, Android and Desktop together.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. A member who loses it can read the page in front of them and nothing else, and an edit made without a connection is retried until the app closes and then lost.

**The following issues rise from that:**
*   23% of iOS and Android sessions between June and August started without a connection or lost it within the first minute
*   31% of Plus workspaces that gave a reason in the April to August cancellation survey named offline access
*   Some of the `lost-edit` tickets Marta raised in #sync-eng start with an edit that was dropped this way
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   A member on a phone or a laptop keeps reading and editing when the connection drops
*   An edit made without a connection reaches the workspace instead of disappearing when the app closes
*   Offline access stops being a reason workspaces give when they cancel
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member has opened on the device, so reading works without a connection
*   Queue every offline change on the device in the order it was made, and upload the queue when the connection returns
*   Settle how conflicting edits are handled, since a device that was offline for a day can otherwise replace a morning of a teammate's edits
*   Show the member that they are offline, how many changes are waiting and how much space offline data uses
*   Leave sharing, inviting, moving a page to another workspace and deleting a page online only, with their controls shown as unavailable offline

## Scope
* * *
Each child story owns one part of the offline lifecycle, covers iOS, Android and Desktop, and carries its own detailed requirements and acceptance criteria.

All four share one device-side store and one sync path: the pages a member has opened are kept on the device, and every offline change queues there until the connection returns.

Conflict handling is decided by the Sync team on 2026-10-09, which is why the two stories it gates sit in their own group.

Web, choosing which pages to keep offline, searching pages that are not kept on the device and offline access in the Support console stay outside this Epic.

#### Not gated by conflict handling
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### Gated by conflict handling
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member keeps working when the connection drops**
* * *
*   **Given** a member on iOS, Android or Desktop who has opened pages before
*   **When** the connection drops
*   **Then** they can keep opening the pages kept on their device, edit blocks and to-dos and create pages and to-dos
*   **And** every change they make is held on the device until the connection returns
* * *
- [] _Mark as done, if the criteria are met_

2\. **Everyone sees the offline changes once the device reconnects**
* * *
*   **Given** a device that made changes without a connection
*   **When** the connection returns
*   **Then** the queued changes upload in the order they were made and reach the workspace
*   **And** other members see them with no action of their own
* * *
- [] _Mark as done, if the criteria are met_

3\. **The member can see what Offline mode is doing**
* * *
*   **Given** a member working without a connection or waiting on changes to upload
*   **When** they look at the top bar or the storage screen in settings
*   **Then** they can see that they are offline, how many changes are waiting and how much space offline data uses
*   **And** they can lower the storage cap or clear the offline data from that screen
* * *
- [] _Mark as done, if the criteria are met_

4\. **Offline mode reaches every plan**
* * *
*   **Given** a member on Free, Plus or Team
*   **When** the release ships
*   **Then** Offline mode is available to them on iOS, Android and Desktop without a plan change
*   **And** no part of it is withheld from the Free plan
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-offline-mode.md`

Artifact kind: Epic, since the initiative splits into four child stories with a Goal and no requirements of its own. Shape checks pass: Goal in place of the Story's expected-outcomes label, `## Scope` in place of `## Requirements`, release-level criteria, no ticket fields, no images, no invented links. `#### **References**` is absent because the brief carries no link. House grammar passes: dividers after every content heading, `*   ` bullets, each H2 closed on a `*   ` line above its spacer, every checkbox written `[]`.

Quality: Problem and Goal pass on the brief's own evidence and target. House format passes. Voice passes. Delivery is honestly absent, since nothing asked for it and no undated external constraint forces it, so Acceptance criteria closes the artifact. If you want Estimation, Rabbit holes and No-gos, say so and Joana's 2026-10-09 decision moves into Estimation as the ordinary internal dependency it is.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the three surface names repeated across About, Scope and criterion 1, because the product has three surfaces rather than for stylistic variety, and Oskar's four area labels carried verbatim into the child-story names so each maps back to his brief.

Three things to correct if I have them wrong. I took `Platform` for the H1 segment, since the work covers three surfaces and every plan rather than one persona. I grouped `## Scope` by the conflict-handling gate instead of one group per area, because the gate is what decides what can start now. And I held the brief's hard values for the child stories, where Requirements live: 500 pages, the 1 GB cap, images and files counting toward it, eviction on the next connection, the 30-second upload start, oldest first, protocol v3 block-level last-writer-wins as today's behavior, and the cap lowering and offline-data clearing. Criterion 3 verifies the storage screen at outcome level and leaves those values to the story that owns them.

One flag from the product context: Desktop wraps the web client and takes its changes with no Desktop release, so whichever child story lands Desktop behavior may carry web client work, even though Web stays outside the Epic. Tell me if that web client work needs scope of its own, or if it is simply part of the Desktop side of each story.

Next step: answer this and I can draft the four child stories in the order the Scope groups them, starting with Offline reading and Offline indicator and storage settings, which do not wait on the sync decision.
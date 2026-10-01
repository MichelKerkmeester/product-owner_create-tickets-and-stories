```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop read, edit and create pages with no connection, and settles how their changes reach everyone else once the device is back online. Web stays out of scope, because a browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case.

Choosing which pages to keep offline, searching pages that are not kept on the device and offline access in the Support console sit outside this epic. This Epic is split into several child stories, each owning one part of the offline lifecycle and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute, and 31% of Plus workspaces that gave a reason in the cancellation survey between April and August named offline access. Some of the `lost-edit` tickets Marta raised in #sync-eng start with an edit made while the connection was gone.

**The following issues rise from that:**
*   Only the page already on screen opens without a connection, so nothing else in the workspace is reachable
*   An edit made with no connection is retried until the app closes and is then lost
*   A device that was offline for a day can replace a morning of a teammate's edits, because sync-service resolves overlaps with block-level last-writer-wins on protocol v3
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online. All four areas land on all three platforms in Q1 2027.

**Direct user/Loomlist benefits:**
*   A member keeps reading and working through a dropped connection instead of closing the app
*   An edit made offline survives and reaches the rest of the workspace when the device reconnects
*   Plus workspaces that named offline access in the cancellation survey get the capability they asked for

The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release, and `lost-edit` tickets that start with a dropped connection stop coming in.
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device with their blocks, inline databases and to-dos, capped at 1 GB, whichever comes first
*   Queue every change the member makes with no connection on the device, in the order it was made
*   Start uploading that queue within 30 seconds of the connection returning, oldest first
*   Handle overlapping edits the way Joana's conflict decision on 2026-10-09 settles them
*   Show the offline state in the top bar and give the member a storage screen for the space offline data uses

## Scope
* * *
Each child story owns one part of the offline lifecycle and carries its own detailed requirements and acceptance criteria.

Offline reading and the offline indicator and storage settings start now, because neither waits on conflict handling. Offline editing and creation and Sync on reconnect cannot be finalised until Joana's conflict-handling decision lands on 2026-10-09.

Desktop wraps the web client, so the Desktop part of each story reaches Desktop members with the web build rather than a Desktop release.

#### Ready to start
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### Waits on the conflict decision
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member reads, edits and creates with no connection on iOS, Android and Desktop**
* * *
*   **Given** a member on iOS, Android or Desktop
*   **When** the app starts without a connection or loses one mid-session
*   **Then** they can open a page kept on the device, edit it and create pages and to-dos
*   **And** their offline work survives the app closing and reopening
* * *
- [] _Mark as done, if the criteria are met_

2\. **Changes made offline reach the workspace when the connection returns**
* * *
*   **Given** a device holding changes made with no connection
*   **When** the connection returns
*   **Then** the queued changes upload in the order they were made, without the member doing anything
*   **And** the other members of the workspace see them
* * *
- [] _Mark as done, if the criteria are met_

3\. **The member sees the offline state and controls the space it uses**
* * *
*   **Given** a device working with no connection
*   **When** the member looks at the app
*   **Then** an offline marker shows in the top bar with the number of changes waiting to sync
*   **And** the storage screen shows the space offline data uses, lets the member lower the cap and clears that data
* * *
- [] _Mark as done, if the criteria are met_

4\. **Offline never performs an action that needs the connection**
* * *
*   **Given** a device with no connection
*   **When** the member shares a page, invites someone, moves a page to another workspace or deletes a page
*   **Then** the control shows as unavailable
*   **And** it works as soon as the connection returns
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

`Export-equivalent path: export/001 - Epic-offline-mode.md`

**Artifact kind:** Epic. Child stories are named as plain text, because none exists yet and no links were supplied.

**Quality summary:** House grammar passes, with every H2 section closed by a `* * *` above its spacer and no `## Requirements` section, since the epic delegates requirements to the children. Acceptance criteria sit at release level and hold no hard value. `#### **References**` is omitted, because the brief and context supply no link. No `## Delivery`, because you did not ask for a delivery view and neither opt-in trigger fired.

`HVR self-scan: 0 hard blockers. Fixed: the always-cut modifier pass found nothing to remove in the drafted prose. Kept with reason: the fixed Given/When/Then labels and the house template lines "The following issues rise from that:" and "Direct user/Loomlist benefits:", because the house grammar fixes their wording, plus the source identifiers `lost-edit` and #sync-eng.`

**Additions you can strike:** the Scope sentence about Desktop wrapping the web client is mine, drawn from your product context rather than Oskar's brief. The two success measures sit in Goal rather than in a criterion, and the four exclusions sit in About prose, since an unrequested No-gos section would have meant a Delivery section nobody asked for.

**On your split question, I drafted Oskar's four areas and would keep them.** Each area is a different mechanism (a device store, an edit queue, the sync engine, the offline and storage UI), so each child story can be sized, built and reviewed on its own, and the conflict decision cuts across two of them exactly as Oskar's Dependency section says. Splitting per platform copies all four mechanisms three times, and the two blocked areas would then be blocked inside every platform story. Platform is a surface dimension inside each story instead, which the release-level criteria above already carry.

One wrinkle worth settling before the children are written. Desktop adds nothing of its own beyond the capture shortcut, so the Desktop part of each story is web-client work, which would reach Web members too while Web stays out of scope. Either Web offline is accepted as a consequence, or the Desktop behaviour needs a gate that keeps it off the Web surface.

**Next step:** say the word and I will draft the two unblocked child stories (Offline reading, then Offline indicator and storage settings), each carrying the supplied values still held at epic level here, such as the 500-page and 1 GB caps, the eviction rule, and image and file counting toward the cap. The two depending on Joana's 2026-10-09 decision are better left until it lands, or drafted with an open line on the conflict behaviour.
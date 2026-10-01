```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member keep reading, editing and creating on iOS, Android and Desktop with no connection, and the workspace sees the changes once the device reconnects. Web stays out of scope, because a browser tab cannot be relied on to keep a local copy between visits and Desktop covers the laptop case. Offline mode ships on every plan, Free included.
The epic is split into four child stories, one per area. Each child covers iOS, Android and Desktop, and carries its own detailed requirements and acceptance criteria.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen.

**The following issues rise from that:**
*   Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute
*   In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access
*   An edit made while the connection is gone is retried until the app closes and then lost
*   Some of the `lost-edit` tickets Marta raised in #sync-eng start that way
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   Reading, editing, checking off to-dos and creating pages keep working when the connection drops
*   Work done without a connection is not lost when the app closes
*   Changes made offline reach every other device once the connection returns
*   A member can see that they are offline and how many changes are waiting
####   

#### Solution
* * *
In order to get there, we will:
*   Keep a capped copy of recently opened pages on each device, so those pages open and read with no connection
*   Queue every change made offline on the device in the order it was made, then upload the queue when the connection returns
*   Settle how conflicting edits are resolved before the queue ships, so a device that was offline cannot replace a teammate's work
*   Show the offline state in the top bar and give the member a storage screen to see and manage what is kept

## Scope
* * *
Each child story owns one part of the offline lifecycle and carries its own detailed requirements and acceptance criteria.

#### Offline reading
* * *
*   Member - Offline mode - Reading pages without a connection

#### Offline editing and creation
* * *
*   Member - Offline mode - Editing and creating pages offline

#### Sync on reconnect
* * *
*   Member - Offline mode - Syncing queued changes on reconnect

#### Offline indicator and storage
* * *
*   Member - Offline mode - Offline indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member can keep working with no connection**
* * *
*   **Given** a member on iOS, Android or Desktop whose connection is gone
*   **When** they open a page they have opened before, edit a block, check off a to-do or create a page or a to-do
*   **Then** each of those completes on the device with no connection
*   **And** sharing, inviting, moving a page to another workspace and deleting a page show as unavailable instead of failing
* * *
- [] _Mark as done, if the criteria are met_

2\. **Nothing a member does offline is lost**
* * *
*   **Given** a member working with no connection
*   **When** the app closes, the device restarts or the app reopens before the connection returns
*   **Then** every change they made is still waiting to upload, in the order they made it
*   **And** no change is discarded while the device stays offline
* * *
- [] _Mark as done, if the criteria are met_

3\. **Queued changes reach everyone else once the connection is back**
* * *
*   **Given** a device that changed blocks while offline
*   **When** the connection returns
*   **Then** its queued changes upload and appear on the workspace's other devices
*   **And** an upload that fails keeps the change queued rather than discarding it
* * *
- [] _Mark as done, if the criteria are met_

4\. **The member can see the offline state and manage what is stored**
* * *
*   **Given** a device that is offline or holding changes that have not uploaded
*   **When** the member looks at the top bar or opens the storage screen in settings
*   **Then** the offline marker and the count of changes waiting to sync are visible
*   **And** the member can see the space offline data uses, lower the cap and clear offline data
* * *
- [] _Mark as done, if the criteria are met_

5\. **Offline mode is the same on every surface and every plan**
* * *
*   **Given** a member on iOS, Android or Desktop, in a Free, Plus or Team workspace
*   **When** they read, edit, create or reconnect
*   **Then** offline mode behaves the same on each surface
*   **And** no part of it is withheld on Free
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   Target: all four areas on iOS, Android and Desktop in Q1 2027
*   Offline reading and the offline indicator can start first, since neither depends on the conflict-handling decision
*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Conflict handling is undecided, and sync-service resolves every overlap with block-level last-writer-wins on protocol v3 today
*   A device offline for a day can therefore replace a morning of a teammate's edits, and Joana settles the replacement on 2026-10-09

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No Web client in this epic
*   No member control over which pages are kept offline
*   No search across pages that are not kept on the device
*   No offline access in the Support console
* * *
```

Export-equivalent path: `export/002 - Epic-offline-mode.md`

Artifact kind: Epic, new, taking the next number in the lane after the 001 clarification. Scope carries four child stories as plain text, one per area, and the Epic holds no Requirements of its own because the fixed limits belong to the children.

The supplied limits travel into the children rather than the Epic: reading pages offline takes the 500 most recently opened pages, the 1 GB cap, images and files counting toward it, and eviction at the next connection. Editing and creating offline takes block edits, to-do check-offs, page and to-do creation, the ordered queue, and the four online-only controls. Sync on reconnect takes the 30-second upload window and oldest-first order. The indicator and storage child takes the marker, the waiting-change count, space used, lowering the cap and clearing offline data.

Quality: Epic shape holds, About opens on narrative, Scope names four separable children with no invented links, criteria stay release-level, house grammar and spacers validated.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the `TBD...` house Delivery placeholder, the `**Given**`/`**When**`/`**Then**`/`**And**` labels that repeat by design, and the two template lines inside Delivery.

Three calls I made where you had not decided, each reversible in a line: Scope groups the four children by area with no wave grouping, and the staging sits in Estimation instead. Delivery is written, because the brief supplies four exclusions and a dated dependency that have no other home, and I can cut it and end on Acceptance criteria if you prefer. The brief's two success measures stay in the brief rather than becoming release criteria, since neither is a behaviour the release guarantees.

Your plan scope is in About and in criterion 5, and each child story will carry it as a requirement. Note for sizing: each child now spans three surfaces, and Desktop work ships with the web client build, so per-child Desktop effort lands on the web clock rather than the fortnightly mobile release.

Next step: tell me which of those three calls to change, or approve the Epic and I will draft the first child story, `Member - Offline mode - Reading pages without a connection`.
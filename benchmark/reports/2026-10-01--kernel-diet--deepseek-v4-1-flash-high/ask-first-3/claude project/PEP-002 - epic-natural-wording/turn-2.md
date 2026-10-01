```markdown
# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode gives a member the same pages and the same editing on iOS, Android and Desktop with no connection, on every plan including Free.
This Epic is split into four child stories, one per area of offline mode, and each child story covers iOS, Android and Desktop together rather than one platform.
The target is Q1 2027 for all four areas.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute, and an edit made while the connection is gone is retried until the app closes and then lost.

**The following issues rise from that:**
*   In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access
*   Some of the `lost-edit` tickets Marta raised in `#sync-eng` start from a dropped connection
*   An overlap resolves with block-level last-writer-wins on protocol v3, so a phone offline for a day can replace a whole morning of a teammate's edits
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   A member's work survives a tunnel or a dead spot, because the device holds it
*   Mobile sessions that used to end at the no-connection screen now keep going
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member has been working in on the device, and queue their offline changes in the order they were made
*   Upload the queue oldest first once the connection returns, and show the member what is stored and what is waiting to sync

## Scope
* * *
Each child story owns one part of the offline lifecycle and carries its own detailed requirements and acceptance criteria.

#### Read and storage
* * *
*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Edit and sync
* * *
**Open:** how sync-service resolves conflicting edits when a device comes back online. Joana, Engineering Manager, Sync, decides on 2026-10-09 from the options in the `#sync-eng` thread.

*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member works offline on all three surfaces**
* * *
*   **Given** a member signed in on iOS, Android or Desktop, with recent pages stored on the device
*   **When** the device has no connection
*   **Then** they open, read, edit and create pages, check off to-dos and see the offline marker
*   **And** their changes reach everyone else once the device is back online
* * *
- [] _Mark as done, if the criteria are met_

2\. **Every plan gets offline mode**
* * *
*   **Given** a workspace on Free, Plus or Team
*   **When** a member opens, reads or edits a page with no connection
*   **Then** offline mode behaves the same on every plan, Free included
* * *
- [] _Mark as done, if the criteria are met_

3\. **Queued changes survive the app closing**
* * *
*   **Given** a member has changed pages with no connection
*   **When** they close the app and reopen it before the connection returns
*   **Then** every change is still queued, in the order it was made
* * *
- [] _Mark as done, if the criteria are met_

4\. **The no-connection share halves**
* * *
*   **Given** the release is live on iOS, Android and Desktop
*   **When** 8 weeks have passed
*   **Then** the share of mobile sessions that hit the no-connection screen is half what it was before the release
* * *
- [] _Mark as done, if the criteria are met_

5\. **Offline edits stop producing lost-edit tickets**
* * *
*   **Given** a member edits with no connection
*   **When** the connection returns
*   **Then** the edit uploads and no `lost-edit` ticket starts from a dropped connection
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...
*   The Sync decision on 2026-10-09 gates offline editing and creation and sync on reconnect, so their size follows it

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   How sync-service resolves conflicting edits is undecided, so offline editing and creation and sync on reconnect cannot be finalised before Joana's decision on 2026-10-09

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   Web stays out of scope, because a browser tab cannot be relied on to keep a local copy between visits
*   Members cannot choose which pages to keep offline
*   Search does not reach pages that are not kept on the device
*   The Support console has no offline access
* * *
```

Export-equivalent path: `export/001 - Epic-offline-mode.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` and `**Open:**`, the fixed house tokens, plus `- [] _Mark as done, if the criteria are met_` and the `No-gos`, `Rabbit holes`, `Estimation` labels the house format fixes, and `#sync-eng`, `lost-edit`, `block-level last-writer-wins` and `protocol v3` as preserved identifiers.

Artifact kind: Epic. Four child stories, one per area, each spanning the three surfaces, so nothing splits per platform. `## Scope` names each story as plain text because none exists yet, and the Epic carries no `## Requirements`, since the hard values belong to the children.

Choices I made on the fields you did not answer, so you can strike any of them. The `**Open:**` line sits in Scope under Edit and sync, with the same question in Rabbit holes, because the conflict decision is not settled and a reader of Scope alone has to see that. `## Delivery` is present only because that Open line forces it, and it closes the artifact. No-gos takes the brief's Out of scope list, and Estimation stays `TBD...` rather than a guessed size, with the Sync decision named as the schedule gate. References is omitted, because no links came with the brief. Every plan including Free is stated in About and proved by criterion 2. Criteria 4 and 5 are the brief's two success measures, which I read as release-level outcomes rather than as a section of their own.

Values held for the child stories rather than lost from the brief: the 500 most recently opened pages, the 1 GB cap with images and files counting toward it, eviction on the next connection, the 30-second upload start, oldest-first order, the online-only list of sharing, inviting, moving and deleting, and the storage screen's used space, lower cap and clear offline data. Say the word and I will pull any of them up to the Epic.

Next step: I can draft the four child stories, starting with offline reading and the indicator and storage settings, which are the two that do not wait on Joana.
```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Loomlist keeps working when a member's connection drops, so the pages they were reading stay open, an edit made without a connection survives, and everything reaches the rest of the workspace on reconnect. The work splits into four child stories, one per area, and each covers iOS, Android and Desktop together on every plan, Free included. Offline reading and the offline indicator can start now, and offline editing and sync on reconnect wait on the conflict handling decision. The target is `Q1 2027` for all four areas.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute, and 31% of Plus workspaces that gave a cancellation reason between April and August named offline access. Support sees the same gap from the other side, because an edit made while the connection is gone is retried until the app closes and then lost.

**The following issues rise from that:**
*   A member without a connection can open only the page already on screen
*   An edit made without a connection is retried until the app closes, then lost
*   A device back after a day offline replaces a whole morning of a teammate's edits
*   Some `lost-edit` tickets Marta raised in #sync-eng start with a dropped connection
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   A member keeps working through a dropped signal without losing an edit
*   Every workspace can depend on it, Free included
*   Fewer `lost-edit` tickets reach Support
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member opens on the device, up to the `500` most recently opened or `1 GB` with their blocks, inline databases and to-dos, whichever limit comes first
*   Queue every change made without a connection on the device in the order it was made
*   Upload queued changes within `30 seconds` of the connection returning, oldest first
*   Show an offline marker in the top bar with a count of changes waiting to sync
*   Add a storage screen in settings for space used, a lower cap and clearing offline data
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only, with their controls unavailable offline
*   Turn it on for every plan, Free included

## Scope
* * *
Each child story owns one part of the offline lifecycle, covers iOS, Android and Desktop together, and holds its own limits, requirements and acceptance criteria.

#### Starts now
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### Waits on the conflict handling decision
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **A member reads their pages without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop with no connection
*   **When** they open a page the device kept
*   **Then** the page opens with its blocks, inline databases and to-dos
*   **And** they can move between those pages without a connection
* * *
- [] _Mark as done, if the criteria are met_

2 ) **An edit made without a connection is not lost**
* * *
*   **Given** a member with no connection
*   **When** they edit a block, check off a to-do, create a page or create a to-do
*   **Then** the change stays on the device through closing and reopening the app
*   **And** the member can see how many changes are waiting to sync
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Queued changes reach the workspace when the connection returns**
* * *
*   **Given** a device holding changes made without a connection
*   **When** the connection returns
*   **Then** the changes upload without the member doing anything
*   **And** everyone else in the workspace sees them
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Actions that need the server show as unavailable offline**
* * *
*   **Given** a member with no connection
*   **When** they reach sharing, inviting, moving a page to another workspace or deleting a page
*   **Then** the control shows as unavailable
*   **And** nothing of that action is queued for later
* * *
- [] _Mark as done, if the criteria are met_

5 ) **Offline mode works on every plan**
* * *
*   **Given** a workspace on the Free plan
*   **When** a member loses the connection
*   **Then** the same offline behaviour applies as on Plus and Team
* * *
- [] _Mark as done, if the criteria are met_

6 ) **The no-connection screen gets rarer after release**
* * *
*   **Given** the release has been live for 8 weeks
*   **When** the mobile sessions that hit the no-connection screen are counted
*   **Then** their share has dropped by half
*   **And** `lost-edit` tickets that start with a dropped connection have stopped
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### Rabbit holes
* * *
*   Conflict handling is unsettled, and Joana chooses between the options in the #sync-eng thread on `2026-10-09`. Offline editing and creation and sync on reconnect stay open until that lands, and work on either before then can be thrown away

#### No-gos
* * *
*   Web, because a browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case
*   Choosing which pages to keep offline
*   Searching pages that are not kept on the device
*   Offline access in the Support console
* * *
```

Export-equivalent path: `export/001 - Epic-offline-mode.md`
HVR self-scan: 0 hard blockers. Fixed: "each carries its own" reworded to "holds", to keep clear of copula-adjacent phrasing. Kept with reason: `TBD...` in Estimation is the house token with its named exemption, and `lost-edit` stays in backticks as a literal ticket label.
Quality: every floor met | Kind: Epic | Energy: Standard

The Epic splits offline mode into the four areas of Oskar's brief, each child story covering iOS, Android and Desktop on every plan. Scope groups the four by what can start now and what waits on Joana's 2026-10-09 decision, and the release criteria carry both measures from his "how we will know it works" list. The page limit, the storage cap and the 30-second upload floor sit in Solution, ready to move into each child story's requirements.

### Open items
1. **Delivery section**
   - **Situation:** The brief supplies four out-of-scope items and one undecided dependency, so I wrote the Delivery close with No-gos and Rabbit holes and left Estimation at `TBD...` because no sizing was supplied
   - **Open:** Strike the section if you want the Epic to end on Acceptance criteria
2. **Title segment**
   - **Situation:** I used `Platform` for the H1 because the work spans iOS, Android and Desktop and belongs to no single persona
   - **Open:** Confirm `Platform`, or name the segment you would search for
3. **Conflict dependency**
   - **Situation:** I read Joana's `2026-10-09` decision as an internal Sync dependency in Rabbit holes rather than an external one
   - **Open:** Confirm, or move it if the Sync decision counts as external
4. **Child story titles**
   - **Situation:** Scope names the four children as plain text in the shape their Story H1 will take, with no links because none exist yet
   - **Open:** Nothing to confirm, send the links when the stories are created
5. **Success measures**
   - **Situation:** I turned both measures from Oskar's list into the last release criterion, including the 8-week window
   - **Open:** Strike it if those measures belong on a dashboard instead of the release gate

Want me to change anything?
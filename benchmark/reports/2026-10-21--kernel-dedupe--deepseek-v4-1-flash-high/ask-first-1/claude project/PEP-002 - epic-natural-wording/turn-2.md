```markdown
# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages with no connection, and everyone else sees their changes once the device is back online. This Epic is split into four child stories, one per area, and each story covers iOS, Android and Desktop together.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Members lose edits when the connection goes, and offline access is one reason Plus workspaces cancel.

**The following issues rise from that:**
*   A member needs a connection for everything past the page already on screen
*   23% of iOS and Android sessions between June and August started without a connection or lost one within the first minute
*   31% of Plus workspaces that gave a reason in the cancellation survey between April and August named offline access
*   An edit made while the connection is gone is retried until the app closes, then lost
*   Some `lost-edit` tickets raised in #sync-eng start with a dropped connection
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online. Every plan gets it, Free included.

**Direct user/Loomlist benefits:**
*   A member keeps reading and editing when the connection drops, instead of losing the work
*   The rest of the workspace sees an offline member's changes once that device reconnects
*   A Plus workspace that named offline access when cancelling has one less reason to leave
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages on the device, capped at 1 GB, so reading works with no connection
*   Let a member edit blocks, check off to-dos and create pages and to-dos offline, with every change queued in the order it was made
*   Start uploading queued changes within 30 seconds of the connection returning, oldest first
*   Show an offline marker in the top bar with the count of changes waiting to sync
*   Give the storage screen space used, a lower cap and a way to clear offline data
*   Make offline mode part of every plan, Free included

## Scope
* * *
Each child story covers iOS, Android and Desktop together and carries its own detailed requirements and acceptance criteria. Offline reading and the indicator can start first, while offline editing and sync on reconnect wait for the conflict-handling decision.

#### Offline reading and the indicator
* * *
*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Offline editing and sync
* * *
*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **A member reads and works with no connection**
* * *
*   **Given** a member signed in on iOS, Android or Desktop with pages kept on the device
*   **When** the app has no connection
*   **Then** those pages open and read with their blocks intact
*   **And** edits, to-dos and new pages made offline wait on the device in the order they were made
*   **And** sharing, inviting, moving a page to another workspace and deleting a page show as unavailable
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The workspace sees an offline member's changes on reconnect**
* * *
*   **Given** a member made changes while the connection was gone
*   **When** that device reconnects
*   **Then** the queued changes upload oldest first
*   **And** the rest of the workspace sees them without the member doing anything
* * *
- [] _Mark as done, if the criteria are met_

3 ) **A member can see the connection state and what the device stores**
* * *
*   **Given** a member with the app open
*   **When** the connection drops
*   **Then** an offline marker shows in the top bar with the count of changes waiting to sync
*   **And** the storage screen shows space used and lets the member lower the cap or clear offline data
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Offline mode reaches every member on every plan**
* * *
*   **Given** a member on Free, Plus or Team
*   **When** they use the app with no connection
*   **Then** offline reading, editing and sync behave the same on that plan as on any other
* * *
- [] _Mark as done, if the criteria are met_

5 ) **The release moves the two measures in the brief**
* * *
*   **Given** offline mode released on iOS, Android and Desktop
*   **When** eight weeks have passed since release
*   **Then** the share of mobile sessions that hit the no-connection screen has halved
*   **And** `lost-edit` tickets that start with a dropped connection stop arriving
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   Q1 2027 to land all four areas on iOS, Android and Desktop, the target Oskar's brief sets

#### Rabbit holes
* * *
*   Conflict handling is undecided until Joana decides on 2026-10-09, so offline editing and sync on reconnect cannot be finalised before then
*   Sync-service resolves every overlap with block-level last-writer-wins on protocol v3, so a device offline for a day can replace a morning of a teammate's edits
*   Protocol v3 has no merge and no conflict copy, and changing it needs every client on a version that speaks the new one

#### No-gos
* * *
*   Web
*   Choosing which pages to keep offline
*   Searching pages that are not kept on the device
*   Offline access in the Support console
* * *
```

Export-equivalent path: `export/002 - Epic-offline-mode.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `lost-edit` and `#sync-eng` kept verbatim as source identifiers.
Quality: every floor met | Kind: Epic | Energy: Standard

The Epic frames offline mode as four child stories, one per area from Oskar's brief, each covering iOS, Android and Desktop. Solution carries the headline limits of 500 pages, 1 GB and the 30-second upload window, and five release-level criteria cover reading and editing, reconnect, the indicator and storage screen, plan coverage and the brief's two measures. The conflict-handling decision sits in Rabbit holes as a dated dependency, with the brief's four exclusions in No-gos.

### Open items
1. **Desktop in scope**
   - **Situation:** The brief puts Desktop in scope while the product context says Desktop wraps the web client and adds only a capture shortcut
   - **Open:** Confirm Desktop ships, and name who settles where its local copy lives
2. **Retention reading**
   - **Situation:** I read the 500-page and 1 GB limits as the whole rule, so a member gets no pin or manual choice
   - **Open:** Strike it if a member can hold a page past both limits
3. **Delivery close**
   - **Situation:** You did not take a position on the Delivery section, so the Epic carries Estimation, Rabbit holes and No-gos as I recommended
   - **Open:** Say if you want it dropped and the exclusions moved into About prose
4. **Epic title segment**
   - **Situation:** The brief names no persona, so the title reads `Epic - Member - Offline mode` because every role and plan gets it
   - **Open:** Confirm Member, or swap the segment to Platform
5. **Release waves**
   - **Situation:** Scope says reading and the indicator can start first, taken from the brief's dependency on Joana's 2026-10-09 decision
   - **Open:** Confirm one Epic over two release waves rather than two separate Epics

Want me to change anything?
No Canvas panel is attached to this session, so the Deliverable Block is rendered here as a fenced block.

```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode keeps a member working in Loomlist when the connection drops, on every plan and on iOS, Android and Desktop. Work done with no connection stays with the member and reaches the workspace when the connection returns. This Epic is split into four child stories, one per offline area, each covering all three platforms.

#### Problem
* * *
Everything past the page already on screen needs a connection, so a member who loses signal cannot open, read or edit anything else.

**The following issues rise from that:**
*   Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute
*   In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access
*   An edit made while the connection is gone is retried until the app closes and then lost, which is how some `lost-edit` tickets start
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   A member keeps working when the connection drops instead of losing the edit
*   Work made offline reaches everyone else once the device reconnects
*   Members on the Free plan get the same offline mode as everyone else
*   Members can see the space offline data uses and clear it when they want
####   

#### Solution
* * *
In order to get there, we will:
*   Ship offline mode on every plan, Free included
*   Keep recently opened pages on the device, so opening and reading carry on without a connection
*   Let blocks, to-dos and new pages be edited and created on the device, with every change queued in the order it was made
*   Upload the queue in order once the connection returns, so the changes reach the workspace
*   Give the member an offline marker, a count of changes waiting to sync and a storage screen they control

## Scope
* * *
Each child story owns one part of the offline lifecycle, covers iOS, Android and Desktop together, and carries its own detailed requirements and acceptance criteria. Web stays out of scope. The offline editing and creation story and the sync on reconnect story cannot be finalised until Sync settles conflict handling on 2026-10-09.

#### Offline reading
* * *
*   Platform - Offline mode - Reading

#### Offline editing and creation
* * *
*   Platform - Offline mode - Editing and creation

#### Sync on reconnect
* * *
*   Platform - Offline mode - Sync on reconnect

#### Offline indicator and storage settings
* * *
*   Platform - Offline mode - Indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member keeps reading without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop who has opened pages recently
*   **When** the connection drops
*   **Then** those pages open and read on the device, with their blocks and inline databases
* * *
- [] _Mark as done, if the criteria are met_

2\. **Work done with no connection is kept and nothing is lost**
* * *
*   **Given** a member editing and creating with no connection
*   **When** they edit a block, check off a to-do or create a page or a to-do
*   **Then** every change is kept on the device in the order it was made
*   **And** no change is lost when the app closes
* * *
- [] _Mark as done, if the criteria are met_

3\. **Everyone else sees the offline work once the device reconnects**
* * *
*   **Given** a device that reconnects after working offline
*   **When** the queued changes upload
*   **Then** everyone who can open the page sees the changes
*   **And** the device no longer shows changes waiting to sync
* * *
- [] _Mark as done, if the criteria are met_

4\. **The member sees the offline state and controls the space it uses**
* * *
*   **Given** a device holding offline data
*   **When** the member opens settings
*   **Then** they see the space used and the changes waiting to sync
*   **And** they can lower the storage cap or clear the offline data
* * *
- [] _Mark as done, if the criteria are met_

5\. **The release reduces sessions that hit the no-connection screen**
* * *
*   **Given** eight weeks after the release reaches members
*   **When** the share of mobile sessions that hit the no-connection screen is measured
*   **Then** it has dropped by half
*   **And** `lost-edit` tickets that start with a dropped connection stop coming in
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

`Export-equivalent path: export/002 - Epic-offline-mode.md`

Quality: Epic kind, four child stories named as plain text in the H1 shape each will take, no `## Requirements` section, release-level criteria, and no `## Delivery` close since you did not ask for one and neither forcing trigger fires. The Sync dependency is dated by another team, which is scheduling rather than an undated external constraint.

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the `lost-edit` ticket label is a supplied identifier, and In order to get there, we will, These are release-level outcomes, Given, When, Then and And are fixed house-template wording.`

Decisions and additions you can strike or change:

*   The brief's four exclusions are scope boundaries rather than outcomes. Web is named in Scope because the title says Platform. Choosing which pages to keep offline, searching pages that are not kept on the device, and offline access in the Support console are No-gos content, so they sit outside the body until you opt into a Delivery close
*   Joana's decision sits as one sentence in Scope rather than an `**Open:**` line, because that marker hangs on a requirement and an Epic has none
*   The per-area hard values in the brief, 500 pages, the 1 GB cap and the 30-second upload window, are not in the Epic, because requirements live in the child stories. They are the first thing each story will need
*   Oskar's area names sit on the Scope group headings, and the story titles drop the repeated word, so `Offline reading` is the group and `Platform - Offline mode - Reading` is its story
*   The product context page says Desktop wraps the web client and picks up web changes with no Desktop release, so the Desktop half of each story is web-client work rather than shell work. Confirm that reading before the stories are sized
*   Free is carried in About and in Solution, since the brief's survey line only mentions Plus workspaces

Next: write the four child stories from their Scope groups, or ask for the Delivery close and I will add estimation, rabbit holes and no-gos.
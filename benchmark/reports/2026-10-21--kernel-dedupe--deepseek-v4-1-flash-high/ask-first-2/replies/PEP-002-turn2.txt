```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages with no connection, and passes their changes to everyone else once the device is back online.
This Epic is split into four child stories, one per area, and each story covers iOS, Android and Desktop together.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. A member on a train or in a basement can read the page in front of them and nothing else.

**The following issues rise from that:**
*   Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute
*   Between April and August, 31% of Plus workspaces that gave a reason in the cancellation survey named offline access
*   A member cannot open any page beyond the one already on screen, so a dropped connection ends the session where it stands
*   An edit made with no connection is retried until the app closes and then lost, and some `lost-edit` tickets start that way
*   Block-level last-writer-wins means a device a day offline can replace a whole morning of a teammate's edits
####   

#### Goal
* * *
A member on any plan, Free included, can open, read, edit and create pages on iOS, Android or Desktop with no connection, and everyone else sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   A member keeps working through a dropped connection instead of stopping at the last page they opened
*   Work made offline reaches the workspace instead of being lost when the app closes
*   A teammate's edits survive another member's day offline
*   Free workspaces get the same offline reading and editing as Plus and Team

We will know it works when the share of mobile sessions that reach the no-connection screen halves within 8 weeks of release, and `lost-edit` tickets that start with a dropped connection stop coming in.
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member has opened on the device, up to 500 pages or 1 GB including images and files, whichever comes first
*   Let a member edit blocks, check off to-dos and create pages and to-dos with no connection, queued in the order they were made
*   Keep sharing, inviting, page moves and page deletes online only, with those controls shown as unavailable offline
*   Upload the queue as soon as the connection returns, oldest first, so other members see the changes
*   Show the member that they are offline, how many changes are waiting to sync, and a storage screen that reports space used

## Scope
* * *
One child story per area, each covering iOS, Android and Desktop together.
Every story carries its own detailed requirements and acceptance criteria.

*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
*   Member - Offline mode - Offline indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **A member keeps reading with no connection**
* * *
*   **Given** a member on iOS, Android or Desktop who has opened pages in the workspace
*   **When** the connection drops
*   **Then** the pages the device keeps still open and read, with their blocks, inline databases and to-dos
*   **And** the app shows that the member is offline
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A member can edit and create offline without losing the work**
* * *
*   **Given** a member with no connection
*   **When** they edit a block, check off a to-do, or create a page or a to-do
*   **Then** every change is queued on the device in the order it was made
*   **And** none of it is lost when the app closes
*   **And** the controls that need a connection are shown as unavailable
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Queued changes reach everyone once the connection returns**
* * *
*   **Given** a device holding changes made with no connection
*   **When** the connection returns
*   **Then** the changes start uploading within 30 seconds, oldest first
*   **And** every other member of the workspace sees them
*   **And** an edit made offline does not replace a teammate's newer edit
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Every plan gets the same offline behavior**
* * *
*   **Given** a workspace on Free, Plus or Team
*   **When** a member works with no connection
*   **Then** reading, editing and creation behave the same on every plan
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   Offline reading and the indicator can start now, since neither depends on the conflict decision
*   Offline editing and creation and Sync on reconnect cannot be estimated until conflict handling is settled on 2026-10-09
*   All four areas target Q1 2027 on iOS, Android and Desktop

#### Rabbit holes
* * *
*   Conflict handling on protocol v3: the options sit in the #sync-eng thread, and Joana settles it on 2026-10-09
*   A protocol change needs every client on a version that speaks it, so devices on older versions stay at risk
*   Block-level last-writer-wins keeps the edit that reaches sync-service last and drops the other, page history included
*   The 1 GB cap counts images and files, so a workspace of large files will evict pages well before 500

#### No-gos
* * *
*   Web: a browser tab cannot be relied on to keep a local copy between visits
*   Choosing which pages a member keeps offline
*   Searching pages that are not kept on the device
*   Offline access in the Support console
* * *
```

Export-equivalent path: `export/NNN - Epic-offline-mode.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Epic | Energy: Standard

The Epic frames offline mode across iOS, Android and Desktop as four child stories, one per area, with every area spanning the three platforms and every plan getting the same behavior. The supplied limits sit where they are observable: 500 pages and 1 GB in Solution, the 30-second upload window in an acceptance criterion.

### Open items
1. **Desktop and the web client**
   - **Situation:** Desktop in scope and Web out, while product context says Desktop wraps the web client with no client of its own
   - **Open:** Confirm the web client's offline work counts as in scope where Desktop needs it, and name its owning team
2. **Conflict guarantee in criterion 3**
   - **Situation:** The criterion promises an offline edit does not replace a teammate's newer one, which is what Joana decides on 2026-10-09
   - **Open:** Confirm the criterion stands as the target outcome or park it with the decision
3. **Delivery section**
   - **Situation:** Written because the brief names four out-of-scope items and an Epic has no other home for them
   - **Open:** Strike it if you want the Epic to close on Acceptance criteria
4. **Detail held back for the child stories**
   - **Situation:** The page that falls out of the 500 being removed at the next connection, the lowerable cap and the clear-offline-data action are per-area detail
   - **Open:** Nothing to confirm, they travel into their own child stories

Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.
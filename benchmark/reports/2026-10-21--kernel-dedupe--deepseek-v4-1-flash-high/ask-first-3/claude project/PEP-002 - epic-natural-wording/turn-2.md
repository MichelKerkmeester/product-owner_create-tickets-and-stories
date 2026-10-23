```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member open, read, edit and create pages on iOS, Android and Desktop with no connection, and hands their changes to the rest of the workspace once the device is back online. The Epic splits into four child stories, one for each area: offline reading, offline editing and creation, sync on reconnect and the offline indicator with storage settings.

#### Problem
* * *
The mobile apps keep the open page on screen and cannot open another without a connection. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

An edit made while the connection is gone is retried until the app closes and then lost. Some of the `lost-edit` tickets Marta raised in #sync-eng start that way.

**The following issues rise from that:**
*   A member cannot open another page once the connection drops
*   An edit made without a connection disappears when the app closes
*   Support gets `lost-edit` tickets that start with a dropped connection
*   Plus workspaces name offline access as a reason to cancel

####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   A member keeps reading and working through a weak signal or a flight
*   An edit made without a connection reaches the workspace instead of being lost
*   Support stops carrying `lost-edit` tickets for edits the product threw away

####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member used most recently on the device, with their blocks, inline databases and to-dos, inside a size cap they can lower
*   Accept edits and new pages of any block type with no connection, queuing each change in the order it was made
*   Upload queued changes oldest first once the connection returns, so a member does not have to act
*   Show an offline marker with a count of changes waiting, and add a storage screen that reports space used
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only

## Scope
* * *
Each child story owns one part of offline mode and carries its own detailed requirements and acceptance criteria. Every story covers iOS, Android and Desktop together, on every plan including Free. Offline reading and the offline indicator do not depend on conflict handling and can start first.

#### Offline areas
* * *
*   Member - Offline - Offline reading
*   Member - Offline - Offline editing and creation
*   Member - Offline - Sync on reconnect
*   Member - Offline - Offline indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **Pages a member opened stay readable without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop who has opened pages on the device
*   **When** the connection drops
*   **Then** a page they opened recently opens and reads in full
*   **And** the pages they used most recently are the ones kept on the device
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A member keeps working with no connection**
* * *
*   **Given** a member on iOS, Android or Desktop with no connection
*   **When** they edit a block, check off a to-do, create a page or create a to-do
*   **Then** the change is accepted and shown on the page with no error
*   **And** it is still there after the app closes and reopens
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Work done offline reaches everyone else**
* * *
*   **Given** a device holding changes made without a connection
*   **When** the connection returns
*   **Then** the changes upload without the member doing anything
*   **And** teammates see them once their own devices sync
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A member can see their offline state and what sits on the device**
* * *
*   **Given** a member on iOS, Android or Desktop with no connection
*   **When** changes queue on the device
*   **Then** an offline marker shows in the top bar with a count of changes waiting
*   **And** the storage screen reports the space offline data uses
*   **And** they can lower the cap or clear offline data from that screen
* * *
- [] _Mark as done, if the criteria are met_

5 ) **Offline mode is on for every plan**
* * *
*   **Given** a member on a Free workspace and a member on a paid one
*   **When** either opens the app with no connection
*   **Then** both can open, read, edit and create
*   **And** no offline capability is withheld from Free
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   Q1 2027 target for all four areas on iOS, Android and Desktop, per the brief, with the order inside it left to the team

#### Rabbit holes
* * *
*   Conflict handling: Joana decides on 2026-10-09 how sync-service handles overlapping edits, and offline editing and sync on reconnect cannot be finalised before that

#### No-gos
* * *
*   No offline mode in a browser tab on Web
*   No picker for which pages to keep offline, since the device keeps the pages used most recently
*   No search across pages that are not kept on the device
*   No offline access in the Support console
* * *
```

Export-equivalent path: `export/NNN - Epic-offline-mode.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `lost-edit`, `#sync-eng` and `2026-10-09` as supplied identifiers, `No-gos` and `Rabbit holes` as fixed Delivery labels.
Quality: every floor met | Kind: Epic | Energy: Standard

The Epic frames offline mode across iOS, Android and Desktop with one child story per area from Oskar's brief, and each story covers all three surfaces rather than one platform. Release-level criteria prove reading, working offline, changes reaching teammates, the marker and storage screen, and availability on every plan. The 2026-10-09 conflict decision sits in Rabbit holes rather than a story, because offline editing and sync on reconnect cannot be finalised until it lands.

### Open items
1. **Delivery section**
   - **Situation:** You answered the split but not the Delivery question, so I included one on my recommendation, with Q1 2027 in Estimation, the conflict decision in Rabbit holes and the brief's Out of scope list in No-gos
   - **Open:** Strike the section if you want the Epic to end on Acceptance criteria
2. **Brief's hard values**
   - **Situation:** The 500 pages, 1 GB cap and 30 seconds sit in the child stories, so the Epic states direction and outcomes without those numbers
   - **Open:** Confirm they belong there, or ask me to lift any of them to epic level
3. **Desktop coverage**
   - **Situation:** The Loomlist context says Desktop wraps the web client and adds nothing of its own, so each child story's Desktop part is web client work while browser tabs stay excluded
   - **Open:** Confirm the child stories can carry Desktop on that basis
4. **Epic title segment**
   - **Situation:** I kept `Epic - Platform - Offline mode` from the clarification, which the last reply asked about and nothing has changed
   - **Open:** Confirm `Platform`, or name a different segment such as `Member`
5. **Child story names**
   - **Situation:** I wrote the four Scope bullets in the `{Persona or platform} - {Area or initiative} - {Feature}` shape with `Member` as the first segment
   - **Open:** Confirm `Member`, or name the segment you want the stories to carry

Want me to change anything?
```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode keeps a member's pages on their device, so reading, editing and creating continue with no connection and everyone else sees the changes once the device is back online.
This Epic is split into four child stories, one per area, each covering iOS, Android and Desktop together and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute, and in the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

Support sees the other end of it. Some of the `lost-edit` tickets Marta raises in #sync-eng start with an edit made while the connection was gone.

**The following issues rise from that:**
*   A page the device has not already loaded cannot be opened, so the work stops the moment the connection drops
*   An edit made with no connection is retried until the app closes and then lost, with nothing in page history to restore
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   A member keeps reading and checking off to-dos through a tunnel, a flight or a weak signal
*   Fewer Plus workspaces name offline access when they give a reason for cancelling
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member has already opened on the device, so they open again with no connection
*   Let a member edit blocks, check off to-dos and create pages and to-dos with no connection
*   Queue every change on the device in the order it was made and upload the queue oldest first when the connection returns
*   Show the member when they are offline, how many changes are waiting to sync and how much space offline data uses

## Scope
* * *
Each child story owns one of the four areas and carries the detailed requirements and acceptance criteria for that area, on iOS, Android and Desktop together.

Web, choosing which pages to keep on the device, searching pages that are not kept on the device and offline access in the Support console are out of scope.

#### Can start now
* * *
*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Waiting on the sync conflict decision
* * *
Joana, Engineering Manager, Sync, decides on 2026-10-09 how sync-service handles conflicting edits, so these two stories cannot be finalised until then.

*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
* * *
##   

## Requirements
* * *
No child story owns these two rules, so they hold at epic level and every child story inherits them.

**Coverage**
* * *
- [] Offline mode is available on every plan, `Free` included
- [] Every area is delivered on iOS, Android and Desktop together
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Reading continues with no connection**
* * *
*   **Given** a member on iOS, Android or Desktop who has opened a page before
*   **When** the device has no connection
*   **Then** the page opens and reads as it did when the member last had a connection
*   **And** the member can move between the pages the device keeps
* * *
- [] _Mark as done, if the criteria are met_

2\. **A member can edit and create with no connection**
* * *
*   **Given** a member whose device has no connection
*   **When** the member edits a block, checks off a to-do, creates a page or creates a to-do
*   **Then** the change is kept on the device in the order it was made
*   **And** the controls for sharing, inviting, moving a page to another workspace and deleting a page show as unavailable
* * *
- [] _Mark as done, if the criteria are met_

3\. **Queued changes reach everyone else when the connection returns**
* * *
*   **Given** a device holding changes made with no connection
*   **When** the connection returns
*   **Then** the changes start uploading within 30 seconds, oldest first
*   **And** other members see them
* * *
- [] _Mark as done, if the criteria are met_

4\. **The member can see the offline state and the space it uses**
* * *
*   **Given** a device holding offline pages and changes waiting to sync
*   **When** the member opens the app
*   **Then** a marker shows the offline state and the count of changes waiting to sync
*   **And** the storage screen shows the space used, lets the member lower the cap and clears offline data
* * *
- [] _Mark as done, if the criteria are met_

5\. **Offline mode is not gated by plan**
* * *
*   **Given** a workspace on any plan, including `Free`
*   **When** a member works with no connection
*   **Then** offline reading, offline editing and sync are available to that member
* * *
- [] _Mark as done, if the criteria are met_

6\. **Both success measures move**
* * *
*   **Given** offline mode released on iOS, Android and Desktop
*   **When** the first 8 weeks after release are measured
*   **Then** the share of mobile sessions that hit the no-connection screen has dropped by half
*   **And** `lost-edit` tickets that start with a dropped connection have stopped arriving
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/001 - Epic-offline-mode.md`

Kind: **Epic.** Four child stories, one per area, each spanning the three platforms you named, with all four areas still in Scope and the two gated ones marked as such.

Calls I made on the items you left open, each easy to reverse:

- Conflict handling sits as an open decision with Joana and the 2026-10-09 date, and the three options in the #sync-eng thread are deliberately not named, so the epic leans on none of them
- `## Requirements` carries one `Coverage` group for every plan including Free and for the three platforms, since no child story owns either rule and all four inherit them. Moving both into the child stories is one word away
- Left to the child stories: the `500`-page set, the `1 GB` cap, images and files counting toward that cap and the removal of a page that falls out of the set on the next connection
- The `30 seconds` upload window stays in the release criteria, because it is the release promise rather than one story's detail
- `## Delivery` omitted per the house default and `#### **References**` omitted because Oskar's brief carries no links, both added on request
- Child stories appear in `## Scope` as plain text with no invented links
- One read of my own, so correct me if it is wrong: the brief scopes Web out while Desktop wraps the web client, so the Desktop work lands in the shared client behind a Desktop gate

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the brief's own figures (23%, 31%, 8 weeks, 30 seconds) and its area names, the house labels `**The following issues rise from that:**` and `**Direct user/Barter benefits:**`, and the Given, When, Then and And labels repeated verbatim across six criteria.

Quality status: house grammar passes, meaning the dividers after headings, `*   ` bullets, `[]` checkboxes, `1\.` numbering with no divider between a Mark-as-done line and the next criterion, and a section close above every `##   ` spacer. Criteria stay release-level, no ticket fields, points or INVEST notes anywhere, and Acceptance criteria is the last section with its spacer as the file's final line.

Next step: say the word and I draft the four child stories against this Scope, in the order you want them.
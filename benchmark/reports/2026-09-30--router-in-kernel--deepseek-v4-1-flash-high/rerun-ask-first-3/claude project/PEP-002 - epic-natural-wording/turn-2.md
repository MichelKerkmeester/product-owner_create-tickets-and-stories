# Epic - Platform - Offline mode

* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages with no connection. Changes made offline reach the workspace once the device is back online, and everyone else sees them. It ships on every plan, Free included.

Web, the Support console, choosing which pages to keep on a device and searching pages that are not kept there stay out of this work.

This Epic is split into four child stories, one per area of the work, each covering iOS, Android and Desktop together and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen, so a member who opens the app in a dead spot reads the one page already there and nothing else.

Between June and August 2026, 23% of iOS and Android sessions started with no connection or lost it within the first minute. In the cancellation survey, 31% of the Plus workspaces that gave a reason between April and August named offline access.

**The following issues rise from that:**
*   A member cannot open any page beyond the one already on screen without a connection
*   An edit made while the connection is gone is retried until the app closes and is then lost
*   Some of the `lost-edit` tickets Marta raised in #sync-eng start with a dropped connection
*   Protocol v3 resolves every overlap with block-level last-writer-wins, so a device offline for a day can replace a whole morning of a teammate's edits
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Barter benefits:**
*   A member keeps working through a tunnel, a train or a dead spot without losing the edit
*   A change made offline lands in the workspace as soon as the connection returns
*   Offline access arrives on every plan, Free included
*   The member can see that they are offline, how much is waiting to sync and how much space it uses
####   

#### Solution
* * *
In order to get there, we will:
*   Keep a copy of the pages the member has worked in on the device, so reading continues with no connection
*   Queue every offline change on the device in the order it was made, and upload the queue when the connection returns
*   Settle how sync-service handles conflicting edits with Sync before the editing and sync stories are finalised, since that decision lands on 2026-10-09
*   Show the member the offline state and let them control the space it uses

## Scope
* * *
Each child story owns one area of the work and carries its own detailed requirements and acceptance criteria. Offline reading and the offline indicator do not wait on the conflict decision, so they can start first.

#### Offline reading
* * *
*   Platform - Offline mode - Offline reading

#### Offline editing and creation
* * *
*   Platform - Offline mode - Offline editing and creation

#### Sync on reconnect
* * *
*   Platform - Offline mode - Sync on reconnect

#### Offline indicator and storage settings
* * *
*   Platform - Offline mode - Offline indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member can read, edit and create with no connection**
* * *
*   **Given** a member on iOS, Android or Desktop who has no connection
*   **When** they open a page kept on the device
*   **Then** they can read it, edit blocks, check off to-dos and create pages and to-dos
*   **And** sharing, inviting, moving a page and deleting a page show as unavailable until the connection returns
* * *
- [] _Mark as done, if the criteria are met_

2\. **A change made offline reaches the workspace when the connection returns**
* * *
*   **Given** a device holding changes made with no connection
*   **When** the connection returns
*   **Then** every queued change reaches the workspace and everyone else sees it
*   **And** the count of changes waiting to sync reaches zero
* * *
- [] _Mark as done, if the criteria are met_

3\. **Every plan gets offline mode, Free included**
* * *
*   **Given** a workspace on the Free plan
*   **When** a member opens the app with no connection
*   **Then** reading, editing and creation behave as they do on Plus and Team
*   **And** no offline action asks the member to upgrade
* * *
- [] _Mark as done, if the criteria are met_

4\. **The release removes the no-connection dead ends and the lost edits**
* * *
*   **Given** the release has shipped to iOS, Android and Desktop
*   **When** the first 8 weeks after release are measured
*   **Then** the share of mobile sessions that reach the no-connection screen is half what it was
*   **And** no `lost-edit` ticket that starts with a dropped connection arrives
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

Export-equivalent path: `export/[NNN] - Epic-offline-mode.md`

Artifact kind: Epic. No `## Requirements`, since an Epic delegates those to its child stories, and no `## Delivery`, since you didn't ask for one and nothing forced it. I can add Delivery in one pass if you want the Out of scope list as No-gos and the conflict decision as a rabbit hole.

HVR self-scan: 0 hard blockers. Fixed: nothing needed. Kept with reason: the Given/When/Then/And labels repeated verbatim in all four criteria, which the house grammar fixes rather than penalises, the template labels `**The following issues rise from that:**` and `**Direct user/Barter benefits:**`, and the literal identifiers `lost-edit`, `#sync-eng` and protocol v3, which travel as the brief wrote them.

Quality: all six floors cleared. Accuracy rests on Oskar's brief and the Loomlist context page, and the undecided conflict handling stays unstated in Goal and in the criteria rather than asserted, since Joana's 2026-10-09 decision settles it. Completeness and Actionability read against the Epic shape: a Goal, a Scope of four separable child stories and release-level criteria, with screen detail left to the children.

Two lines in the criteria are mine, so strike them if they are wrong: the count of changes waiting to sync reaching zero, and no offline action asking the member to upgrade. The child-story titles `Platform - Offline mode - {Area}` are my naming for the intended Story H1s, and the hard values Oskar supplied (the 500 pages, the 1 GB cap, the 30-second upload window) are deliberately held back for those four stories, since an Epic carries no requirements.

Next: say the word and I'll draft the four child stories from the brief, starting with offline reading and the indicator, which can go first while the conflict decision is open.
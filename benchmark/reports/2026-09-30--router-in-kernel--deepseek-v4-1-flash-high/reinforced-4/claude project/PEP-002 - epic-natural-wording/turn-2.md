```markdown
<!-- Product Owner · Story Mode · Epic shape · Epic Template v0.102 -->

# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member keep working in a Loomlist workspace with no connection, on iOS, Android and Desktop, and lets everyone else see their changes once the device is back online.
This Epic is split into four child stories, each owning one part of the offline lifecycle and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
A member needs a connection for everything past the page already on screen, on every surface.
Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute, and 31% of Plus workspaces that gave a reason in the cancellation survey named offline access.
Support sees the same failure: an edit made while the connection is gone is retried until the app closes and then lost, and some `lost-edit` tickets raised in `#sync-eng` start that way.

**The following issues rise from that:**
*   A member cannot open, read, edit or create a page with no connection, on any surface
*   An edit made with no connection is retried until the app closes, then lost
*   A device that was offline for a day can replace a whole morning of a teammate's edits
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages with no connection, and everyone else sees their changes once the device is back online.
The release is judged on two measures: the share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release, and `lost-edit` tickets that start with a dropped connection stop coming in.

**Direct user/Barter benefits:**
*   Members keep working through a lost connection instead of giving up on the app
*   Reading, to-dos and page creation stay available on the move
*   A teammate opening the workspace sees the offline edits rather than a stale page
*   Support stops working tickets where a dropped connection destroyed a member's work
####   

#### Solution
* * *
In order to get there, we will:
*   Keep recently opened pages on each device so their blocks, inline databases and to-dos can be read with no connection
*   Let a member edit blocks, check off to-dos and create pages and to-dos with no connection, queuing every change on the device
*   Upload the queue when the connection returns so the workspace and other members see the changes
*   Show the member that they are offline and how much is waiting to sync, and let them control what the device stores
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only, with their controls unavailable offline

## Requirements
* * *
**Plan availability**
* * *
- [] Offline mode is available on every plan, `Free` included
* * *
##   

## Scope
* * *
Each child story owns one part of the offline lifecycle and carries its own detailed requirements and acceptance criteria.
Conflict handling is not settled, so two of the four child stories cannot be finalised yet. Joana, Engineering Manager for Sync, decides on 2026-10-09 how sync-service handles conflicting edits, and offline editing and creation and sync on reconnect wait on that decision. Offline reading and the offline indicator do not.

#### Ready to start
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### Waiting on the conflict decision
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member can read their workspace with no connection**
* * *
*   **Given** a member on iOS, Android or Desktop whose device has no connection
*   **When** they open a page kept on the device
*   **Then** it opens with its blocks, inline databases and to-dos readable in full
* * *
- [] _Mark as done, if the criteria are met_

2\. **Work done with no connection is kept and survives the app closing**
* * *
*   **Given** a member with no connection who edits a block, checks off a to-do or creates a page
*   **When** they close the app and open it again with no connection
*   **Then** their work is still there and can still be edited
* * *
- [] _Mark as done, if the criteria are met_

3\. **Queued changes upload on their own when the connection returns**
* * *
*   **Given** a member's device holding pages and edits made with no connection
*   **When** the connection returns
*   **Then** the queue starts uploading without the member asking, oldest change first
*   **And** anything that has not uploaded yet is still on the device and still counted
* * *
- [] _Mark as done, if the criteria are met_

4\. **Features that need a connection are unavailable offline**
* * *
*   **Given** a member working with no connection
*   **When** they reach for sharing, inviting, moving a page to another workspace or deleting a page
*   **Then** the control is unavailable rather than failing after the tap
* * *
- [] _Mark as done, if the criteria are met_

5\. **A member can tell they are offline and manage what the device stores**
* * *
*   **Given** a member whose device has gone offline
*   **When** the connection drops or changes pile up
*   **Then** the member can tell they are offline and how much is waiting to sync
*   **And** they can review the space offline data uses, lower the storage cap and clear it
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
Q1 2027 is the target for all four child stories on iOS, Android and Desktop, and sizing sits with the Sync, Mobile Platform and Web and Desktop teams.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Conflict handling is undecided until 2026-10-09, so work on the editing and sync stories before then risks being rebuilt
*   Sync protocol v3 has no merge and no conflict copy, so replacing it needs every client on a version that speaks it
*   Desktop takes whatever build Web runs that day, so a Desktop-only offline path would double the work

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No offline access on Web, because a browser tab cannot be relied on to keep a local copy between visits
*   No choosing which pages are kept offline
*   No searching pages that are not kept on the device
*   No offline access in the Support console
* * *
```

**Export-equivalent path:** `export/002 - Epic-offline-mode.md`

**Artifact kind:** Epic. Four child stories, one per area, each covering iOS, Android and Desktop together.

**Quality status:** Shape fit pass, Goal and Scope with no requirements of its own except the plan rule and release-level criteria. Source reconciliation pass, every supplied figure from the brief appears once and each hard value is placed where the house grammar allows. Longevity pass, the unsettled conflict handling is stated in Scope and named as a rabbit hole without any criterion asserting its undecided behavior. House format pass, dividers, `*   ` bullets, `[]` checkboxes, spacers retained, no bullet ending on a full stop. Voice pass, no blockers.

**HVR self-scan:** 0 hard blockers. Fixed: none required. Kept with reason: `TBD...` is the fixed house Delivery placeholder, the repeated `Given`, `When`, `Then` and `And` are fixed labels rather than synonym cycling, and the template's own lines ("The following issues rise from that:", "In order to get there, we will:") are house wording.

**Where the brief's hard values went.** The 500-page and 1 GB caps, the 30-second upload window and the count of changes waiting all belong to the child stories, since an Epic holds no requirements. The plan rule is the exception, because no single child story owns it and all four have to meet it, so it sits in `## Requirements` under a `Platform` title rather than in a criterion that would have to name a plan.

**Additions to strike if unwanted.** I gave the four child stories `Platform - Offline mode - {Area}` titles, grouped Scope by what can start rather than by lifecycle area so the dependency is visible, put the two success measures in the Goal rather than in the acceptance criteria, and wrote `## Delivery` because Oskar's brief names its own out-of-scope list, which is what No-gos holds. The rabbit hole about Desktop taking Web's build comes from the product context, not from the brief, and the criterion that unuploaded changes stay on the device is my reading of the lost-edit problem.

**One thing to reconcile with Oskar.** The brief's evidence is 31% of Plus workspaces naming offline access, and the plan decision now covers Free as well, so the child stories should carry the entitlement check rather than a Plus-only assumption. The Desktop point from your intake answer stands unresolved only at implementation level, since the context says Desktop runs the web client and Web is out of scope.

**Next step:** say which of these you want changed, or take the four child stories next, starting with offline reading and the indicator, which can be written now.
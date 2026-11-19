# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets a member open, read, edit and create pages on iOS, Android and Desktop without a connection, then syncs their changes once the device is back online. It is available on every plan, Free included, and the target is Q1 2027 for all four areas on all three platforms.

This Epic is split into four child stories, one per area of Oskar's brief. Each story covers iOS, Android and Desktop together and carries its own detailed requirements and acceptance criteria.

### Problem
* * *
Loomlist needs a connection for everything past the page already on screen. The mobile apps keep the open page visible but cannot open another one offline, and an edit made while the connection is gone is retried until the app closes and is then lost.

**The following issues rise from that:**
*   Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute
*   Between April and August, 31% of Plus workspaces that gave a cancellation reason named offline access
*   Some `lost-edit` tickets raised in #sync-eng start with an edit made after the connection dropped
*   sync-service resolves every overlap with block-level last-writer-wins on protocol v3, so a phone offline for a day can replace a teammate's whole morning of edits
###   

### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   Members keep working on their recent pages when the connection drops or never arrives
*   An edit made offline is kept on the device until it syncs instead of being lost when the app closes

**We will know it works when:**
*   The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
*   `lost-edit` tickets that start with a dropped connection stop coming in
###   

### Solution
* * *
In order to get there, we will:
*   Keep a member's most recently opened pages on the device so they open and read without a connection
*   Let members edit, check off to-dos and create pages and to-dos offline
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only
*   Upload changes made offline in the order they were made once the connection returns
*   Show members when they are offline, how many changes are waiting to sync and how much space offline data takes

Web is out of scope because a browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case.

This epic does not cover:
*   Web
*   Choosing which pages to keep offline
*   Searching pages that are not kept on the device
*   Offline access in the Support console

#### **References**
* * *
Sources
*   Offline mode, epic brief by Oskar, Product Manager, Mobile, shared with the Sync, Mobile Platform and Web and Desktop teams on 2026-09-23
*   The #sync-eng thread holding the conflict-handling options

## Scope
* * *
Each child story owns one area of offline mode and carries its own detailed requirements and acceptance criteria for iOS, Android and Desktop.

#### Starts now
* * *
Neither story depends on the conflict-handling decision, so both can start before 2026-10-09.

*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Waits on the conflict-handling decision
* * *
Joana, Engineering Manager, Sync, decides on 2026-10-09 how sync-service handles conflicting edits, choosing between the options in the #sync-eng thread. Both stories can be drafted before then, and neither can be finalised until the decision lands.

If the decision changes protocol v3, every client has to be on a version that speaks the new protocol, and whether the Web client update belongs to this epic is not decided yet.

*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **Recent pages open without a connection**
* * *
*   **Given** a member on any plan, Free included, using iOS, Android or Desktop
*   **When** the device has no connection
*   **Then** the member can open and read the pages the device keeps offline, with their blocks, inline databases and to-dos
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Work done offline is kept and reaches the workspace**
* * *
*   **Given** a member who edits blocks, checks off to-dos or creates pages and to-dos with no connection
*   **When** the device is back online
*   **Then** every change made offline reaches the workspace in the order it was made, and teammates see it
*   **And** no change made offline is lost when the app closes before the connection returns
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Members can tell what works offline and what is still waiting**
* * *
*   **Given** a member using Loomlist with no connection
*   **When** they look at the app
*   **Then** they can see that they are offline and how many changes are waiting to sync
*   **And** sharing, inviting, moving a page to another workspace and deleting a page show as unavailable until the connection returns
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

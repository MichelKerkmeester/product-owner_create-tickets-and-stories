# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets members on iOS, Android or Desktop work on pages without a connection, syncing on reconnect. It covers every plan, Free included, targeting Q1 2027 for all four areas of Oskar's brief on all three platforms.

#### Problem
* * *
Loomlist needs a connection for everything past the page on screen, and an offline edit is retried until the app closes, then lost.

**The following issues rise from that:**
*   From June to August, 23% of iOS and Android sessions started offline or lost the connection within the first minute
*   From April to August, 31% of Plus workspaces giving a cancellation reason named offline access
*   Some `lost-edit` tickets in #sync-eng start with an edit after the connection dropped
*   sync-service resolves overlaps with block-level last-writer-wins on protocol v3, so a phone offline for a day can overwrite a teammate's morning
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages offline, and others see the changes once the device reconnects.

**Direct user/Loomlist benefits:**
*   Members keep working on recent pages when the connection drops or never arrives
*   An offline edit stays on the device until it syncs

**We will know it works when:**
*   The share of mobile sessions hitting the no-connection screen halves within 8 weeks of release
*   `lost-edit` tickets starting with a dropped connection stop
####   

#### Solution
* * *
In order to get there, we will:
*   Keep a member's most recently opened pages on the device for offline reading
*   Let members edit, check off to-dos and create pages and to-dos offline
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only
*   Upload offline changes in order once the connection returns
*   Show offline status, changes waiting to sync and the space offline data takes

Web is out because a browser tab cannot be relied on to keep a local copy.

This epic does not cover:
*   Web
*   Choosing which pages to keep offline
*   Searching pages not kept on the device
*   Offline access in the Support console

#### **References**
* * *
Sources
*   Offline mode, epic brief by Oskar, Product Manager, Mobile, shared with the Sync, Mobile Platform and Web and Desktop teams on 2026-09-23
*   The #sync-eng thread holding the conflict-handling options

## Scope
* * *
Each child story covers one area on iOS, Android and Desktop.

#### Starts now
* * *
Neither story depends on the conflict-handling decision, so both can start before 2026-10-09.

*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Waits on the conflict-handling decision
* * *
Joana, Engineering Manager, Sync, picks from the #sync-eng options on 2026-10-09 how sync-service handles conflicting edits. Both stories can be drafted, not finalised, before then.

If the decision changes protocol v3, every client needs a version that speaks it, and whether the Web client update belongs to this epic is not decided.

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
*   **Given** a member on any plan, Free included, on iOS, Android or Desktop
*   **When** the device is offline
*   **Then** they can read pages kept offline, with blocks, inline databases and to-dos
* * *
- [] _Mark as done, if the criteria are met_

2\. **Work done offline is kept and reaches the workspace**
* * *
*   **Given** a member who edits blocks, checks off to-dos or creates pages and to-dos offline
*   **When** the device reconnects
*   **Then** every offline change reaches the workspace in order, and teammates see it
*   **And** no offline change is lost if the app closes first
* * *
- [] _Mark as done, if the criteria are met_

3\. **Members can tell what works offline and what is still waiting**
* * *
*   **Given** a member using Loomlist offline
*   **When** they look at the app
*   **Then** they see that they are offline and how many changes wait to sync
*   **And** sharing, inviting, moving a page to another workspace and deleting a page show as unavailable until reconnecting
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

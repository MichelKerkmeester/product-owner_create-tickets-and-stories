# Epic - Member - Offline mode

* * *
## About
* * *
Offline mode lets a member open, read, edit and create pages on iOS, Android and Desktop with no connection, on every plan including Free. Web stays online only.

Four child stories, one per brief area, each cover all three platforms by Q1 2027.

#### Problem
* * *
From June to August, 23% of iOS and Android sessions started offline or lost the connection within a minute. From April to August, 31% of Plus workspaces giving a cancellation reason named offline access.

**The following issues rise from that:**
*   Without a connection, a member can open only the page already on screen
*   An offline edit is retried until the app closes, then lost, starting some `lost-edit` tickets
####   

#### Goal
* * *
Members on iOS, Android or Desktop work offline, and others see the changes once the device reconnects.

**Direct user/Loomlist benefits:**
*   Offline work reaches the workspace instead of vanishing
*   Mobile sessions hitting the no-connection screen halve within 8 weeks of release
*   `lost-edit` tickets from dropped connections stop
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the 500 most recently opened pages with blocks, inline databases and to-dos, up to 1 GB, whichever comes first
*   Count images and files toward the cap, dropping a page leaving the 500 on reconnect
*   Let members edit blocks, check off to-dos and create pages and to-dos offline, queued on the device in order
*   Start uploading queued changes, oldest first, within 30 seconds of the connection returning
*   Keep sharing, inviting, moving a page to another workspace and deleting a page online only, unavailable offline
*   Add a top-bar offline marker and a count of changes waiting to sync
*   Add a settings storage screen showing space used, to lower the 1 GB cap and clear offline data

## Scope
* * *
Conflict handling is not settled: Joana, Engineering Manager, Sync, decides on 2026-10-09 from the #sync-eng options. Today sync-service uses block-level last-writer-wins on protocol v3, so a device offline for a day can replace a teammate's morning of edits. Offline reading and the indicator do not depend on it, so they start first.

#### Starts before the conflict decision
* * *
*   Member - Offline mode - Offline reading
*   Member - Offline mode - Offline indicator and storage settings

#### Finalised after the conflict decision
* * *
*   Member - Offline mode - Offline editing and creation
*   Member - Offline mode - Sync on reconnect

#### Out of scope
* * *
*   Web, because a browser tab cannot reliably keep a local copy
*   Choosing which pages to keep offline
*   Searching pages not kept on the device
*   Offline access in the Support console
* * *
##   

## Acceptance criteria
* * *
Release-level outcomes, with detailed criteria in each child story.

1\. **Recent pages open without a connection**
* * *
*   **Given** a member on iOS, Android or Desktop, on any plan including Free, offline
*   **When** they open a page kept on the device
*   **Then** it opens with its blocks, inline databases and to-dos
* * *
- [] _Mark as done, if the criteria are met_

2\. **Work done offline reaches the workspace**
* * *
*   **Given** a member offline
*   **When** they edit blocks, check off to-dos or create pages and to-dos
*   **Then** every change is kept on the device in order, even if the app closes first
*   **And** once back online, members with access see every change that did not conflict with another edit
* * *
- [] _Mark as done, if the criteria are met_

3\. **Online-only actions show as unavailable offline**
* * *
*   **Given** a member offline
*   **When** they reach for sharing, inviting, moving a page to another workspace or deleting one
*   **Then** each shows as unavailable
* * *
- [] _Mark as done, if the criteria are met_

4\. **Members can see their offline state and manage storage**
* * *
*   **Given** a member on iOS, Android or Desktop
*   **When** the device has no connection
*   **Then** they see they are offline and how many changes wait to sync
*   **And** in settings they see the space offline data uses, lower the cap and clear offline data
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

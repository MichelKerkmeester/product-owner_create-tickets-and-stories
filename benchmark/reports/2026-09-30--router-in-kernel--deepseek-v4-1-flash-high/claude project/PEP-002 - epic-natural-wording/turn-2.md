```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages and to-dos with no connection, and gives everyone else their changes once the device is back online. Web stays out of scope, because a browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case.

The epic is split into four child stories, one per area of behavior, each owning its own requirements and acceptance criteria. Offline mode applies to every plan, Free included. Choosing which pages to keep offline, searching pages that are not on the device and offline access in the Support console stay outside this epic.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen, so a member on mobile can read the page in front of them and nothing else.

**The following issues rise from that:**
*   23% of iOS and Android sessions between June and August started without a connection or lost it within the first minute
*   31% of Plus workspaces that gave a cancellation reason between April and August named offline access
*   An edit made without a connection is retried until the app closes and is then lost
*   Some `lost-edit` tickets in #sync-eng start with a dropped connection
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

**Direct user/Loomlist benefits:**
*   A member on iOS, Android or Desktop keeps reading, editing and creating through a dropped connection
*   An edit made offline survives the app closing and reaches the workspace when the device reconnects
*   A member's teammates see that edit once the device is back online
*   A workspace on Free gets the same offline access as one on Plus or Team
*   Support stops seeing edits lost to a dropped connection
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member opens on their device, so those pages open and stay editable with no connection
*   Queue every change made offline in the order it was made and upload the queue once the connection returns
*   Show the member that the device is offline, how many changes are waiting and how much space offline data uses
*   Settle conflict handling before offline editing and sync on reconnect are built, since sync-service resolves overlaps with block-level last-writer-wins on protocol v3 today
*   Joana decides how sync-service handles conflicting edits on 2026-10-09, and two child stories wait on that call
*   Land all four areas on iOS, Android and Desktop in Q1 2027, with no plan gate at build time

## Scope
* * *
Each child story owns one area, covers iOS, Android and Desktop together and carries its own detailed requirements and acceptance criteria. Each is named by the title its story will take.

#### Ready to start
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### After the conflict-handling decision
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own area.

1\. **A member works through a dropped connection on every in-scope surface**
* * *
*   **Given** a member on iOS, Android or Desktop who has used Loomlist on that device while online
*   **When** the device loses its connection
*   **Then** they can open, read, edit and create pages and to-dos with no connection
*   **And** the device shows them that it is offline and how many changes are waiting
* * *
- [] _Mark as done, if the criteria are met_

2\. **Offline mode arrives on every plan, Free included**
* * *
*   **Given** a Free workspace and a Plus or Team workspace
*   **When** a member of either workspace works without a connection
*   **Then** both members can read, edit and create pages offline
*   **And** no offline capability is held back by plan
* * *
- [] _Mark as done, if the criteria are met_

3\. **Offline changes reach the rest of the workspace on reconnect**
* * *
*   **Given** a member who changed pages while their device had no connection
*   **When** the device is back online
*   **Then** the queued changes upload without any action from the member
*   **And** everyone else in the workspace sees those changes
* * *
- [] _Mark as done, if the criteria are met_

4\. **Mobile sessions stop landing on the no-connection screen**
* * *
*   **Given** the share of iOS and Android sessions that reached the no-connection screen before the release
*   **When** 8 weeks have passed since release
*   **Then** that share is at most half of what it was before
* * *
- [] _Mark as done, if the criteria are met_

5\. **Edits made offline stop being lost**
* * *
*   **Given** an edit a member makes while their device has no connection
*   **When** the app closes or the connection returns
*   **Then** the edit survives and reaches the workspace
*   **And** `lost-edit` tickets that begin with a dropped connection stop arriving
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

**Export-equivalent path:** `export/001 - Epic-offline-mode.md`
**Artifact kind:** Epic.

**Changed:** the four child stories are unchanged in count and area, and Scope now says in prose that each one covers iOS, Android and Desktop together, so nobody reads the platform list as a split. The plan scope is recorded twice, each time doing different work: About states who gets offline mode, and a new release criterion makes Free parity something a tester observes rather than an assumption. I also added a Free benefit to the Goal and a no-plan-gate clause to the final Solution bullet, since a plan gate usually enters at build time rather than at scope time.

**Worth flagging:** each of the four child stories will need the plan scope carried into its own requirements, or a plan gate can still appear inside one area. I will put it in all four when we draft them. The Web exclusion and the three other exclusions stay in the About narrative because no Delivery section is written, and the conflict-handling dependency stays in Solution.

**Quality status:** six floors pass on the Epic shape. Accuracy at 9, with every figure, date, identifier and the plan scope tracing to your brief, the product context or your instruction. Completeness reads against the Epic contract, so the absent Requirements and Delivery sections are correct for the kind rather than a gap. The plan scope is testable where it sits, in criterion 2, rather than only declared.

`HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: 2026-10-09, Q1 2027, `lost-edit`, #sync-eng, protocol v3, the 8-week window and "Free included" are supplied values, identifiers and phrasing carried verbatim, and "In order to get there, we will:" plus the `* * *` and `##   ` spacers are fixed house template lines.`

**Next step:** say the word and I will draft the two stories that are ready to start, Offline reading and Offline indicator and storage settings, each with its own requirements holding the 500-page, 1 GB and cap values and the plan scope. The two gated stories follow once Joana's 2026-10-09 conflict decision lands.
```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode lets a member on iOS, Android or Desktop open, read, edit and create pages and to-dos with no connection, and gives everyone else their changes once the device is back online. Web stays out of scope, because a browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case.

The epic is split into four child stories, one per area of behavior, each owning its own requirements and acceptance criteria. Choosing which pages to keep offline, searching pages that are not on the device and offline access in the Support console stay outside this epic.

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
*   Land all four areas on iOS, Android and Desktop in Q1 2027

## Scope
* * *
Each child story owns one area and carries its own detailed requirements and acceptance criteria. Each is named by the title its story will take.

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

2\. **Offline changes reach the rest of the workspace on reconnect**
* * *
*   **Given** a member who changed pages while their device had no connection
*   **When** the device is back online
*   **Then** the queued changes upload without any action from the member
*   **And** everyone else in the workspace sees those changes
* * *
- [] _Mark as done, if the criteria are met_

3\. **Mobile sessions stop landing on the no-connection screen**
* * *
*   **Given** the share of iOS and Android sessions that reached the no-connection screen before the release
*   **When** 8 weeks have passed since release
*   **Then** that share is at most half of what it was before
* * *
- [] _Mark as done, if the criteria are met_

4\. **Edits made offline stop being lost**
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

**On your split question: I recommend Oskar's four areas, not per platform.** The brief hands you the deciding factor itself. Offline reading and the indicator do not wait on Joana's 2026-10-09 conflict decision, and offline editing and sync on reconnect do. Split by area and that boundary is a clean one, so two stories can start in October while two wait. Split per platform and every one of the twelve slices carries a piece of offline editing, so all twelve wait on the same decision and nothing starts early. Platform is then a grouping inside each child story's own acceptance criteria, where it belongs, because the reading story verifies iOS, Android and Desktop against one set of requirements rather than three copies. The Scope groups are named for readiness so the sequencing is read off the epic. If you would rather have the platform split, the Scope regroups in one edit and nothing else in the epic changes.

**Additions you did not supply, so you can strike them:** the two Scope group names and their dependency grouping, and the child-story planning titles in the form `Platform - Offline mode - {area}`.

**What I left out, and why:** no `## Delivery` section, because you did not ask for one and nothing forced it, since Joana's decision has a date and belongs to Estimation rather than an external dependency, and an Epic has no Requirements to carry an `**Open:**` line. That means the four out-of-scope items sit in the About narrative instead of a No-gos list, and the conflict-handling dependency sits in Solution. Say the word and I will add Delivery with Estimation, Rabbit holes, No-gos and the dependency in it. No `#### **References**` section, because the brief supplied no links and inventing one is not an option. The hard values in the brief (500 pages, the 1 GB cap, the 30-second upload window) stay out of the epic by design and belong in the child stories that own them, since an Epic carries no Requirements. Tell me if you want the reading and editing stories drafted next and those values will land there.

**Quality status:** six floors pass on the Epic shape. Completeness reads against the Epic contract, with Goal, Scope and child stories present and the absent Requirements and Delivery sections correct for the kind rather than a miss. Accuracy holds at 9, since every figure, date and identifier traces to the brief or the product context. Actionability rests on the four release-level criteria plus Scope children separable enough to hand on.

`HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: 2026-10-09, Q1 2027, `lost-edit`, #sync-eng, protocol v3 and the 8-week window are supplied values and identifiers carried verbatim, and "In order to get there, we will:" plus the `* * *` and `##   ` spacers are fixed house template lines.`

**Next step:** confirm the four-area split or ask for the platform regrouping, and tell me whether you want the Delivery section. Then I can draft the two stories that are ready to start.
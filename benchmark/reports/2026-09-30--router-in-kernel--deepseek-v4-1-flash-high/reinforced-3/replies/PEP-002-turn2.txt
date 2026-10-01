```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Loomlist needs a connection for everything past the page already on screen, so a member who loses signal stops working where they are. This epic brings offline mode to iOS, Android and Desktop, so work continues with no connection and everyone else sees the changes once the device is back online.
The work is split into four child stories, one per area of the change, and each story covers the three platforms together. Web stays out of scope.

#### Problem
* * *
23% of iOS and Android sessions between June and August started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

Support sees the same fault from the other side: an edit made while the connection is gone is retried until the app closes, then lost. The `lost-edit` tickets Marta raised in #sync-eng start that way.

**The following issues rise from that:**
*   A member can open the page already on screen and nothing else without a connection
*   An edit made while the connection is gone is lost when the app closes before the connection returns
*   Two devices that change the same block between sync sessions resolve it as block-level last-writer-wins, and the edit that loses is replaced with nothing in page history to restore
*   A device back from a day offline arrives with every edit at once, which pushes that overlap rate up
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online. The target is Q1 2027 for all four areas on the three platforms.

**Direct user/Loomlist benefits:**
*   Members keep working through a dropped connection, on a phone in a lift or a laptop on a train
*   An edit made offline reaches the rest of the workspace instead of disappearing when the app closes
*   Fewer sessions end at the no-connection screen, and fewer cancellations name offline access
*   Support stops seeing lost edits that began with a dropped connection
####   

#### Solution
* * *
In order to get there, we will:
*   Keep recently opened pages and their blocks on the device, so reading works with no connection
*   Queue every offline change on the device in the order it was made, then upload it when the connection returns
*   Show the member an offline marker, the count of changes waiting to sync and a storage screen in settings
*   Make offline mode available on every plan, Free included
*   Keep Web out of scope, because a browser tab cannot keep a local copy between visits and Desktop covers the laptop case

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Offline reading and the offline indicator
* * *
*   Platform - Offline mode - Offline reading
*   Platform - Offline mode - Offline indicator and storage settings

#### Offline editing and sync on reconnect
* * *
*   Platform - Offline mode - Offline editing and creation
*   Platform - Offline mode - Sync on reconnect

Both stories in this group wait on conflict handling. Joana decides between Option A, Option B and Option C on 2026-10-09, and neither can be finalised before then.
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member works with no connection on any platform**
* * *
*   **Given** a member signed in on iOS, Android or Desktop with no connection
*   **When** they open Loomlist
*   **Then** they can open, read, edit and create pages kept on the device
*   **And** no part of that work sends them to the no-connection screen
* * *
- [] _Mark as done, if the criteria are met_

2\. **Work done offline reaches the rest of the workspace**
* * *
*   **Given** a change made on a device with no connection
*   **When** the connection returns
*   **Then** the change uploads and everyone who can open the page sees it
*   **And** nothing queued on the device is lost because the app closed first
* * *
- [] _Mark as done, if the criteria are met_

3\. **Offline mode is available on every plan**
* * *
*   **Given** a workspace on Free, Plus or Team
*   **When** a member works with no connection
*   **Then** every offline capability is available to them
*   **And** no offline capability is held behind a paid plan
* * *
- [] _Mark as done, if the criteria are met_

4\. **The release moves the numbers the epic exists for**
* * *
*   **Given** the release has been live on iOS, Android and Desktop for 8 weeks
*   **When** the no-connection sessions and the `lost-edit` queue are measured
*   **Then** the share of mobile sessions that hit the no-connection screen has dropped by half
*   **And** `lost-edit` tickets that start with a dropped connection stop coming in
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Epic-offline-mode.md`

Artifact kind: **Epic**, one child story per area Oskar names, each covering iOS, Android and Desktop together. Platform-wide work takes `Platform` as the H1 segment, so the child stories are named `Platform - Offline mode - {area}` in the shape their own H1 will take.

What I held back deliberately, so nothing is silently dropped:
* The brief's hard values belong to the child stories, not the Epic. The 500-page cache, the 1 GB cap, the 30-second upload on reconnect and the oldest-first order are Requirements material for the stories that own those areas
* I wrote no `## Delivery` section. You did not ask for one, and the conflict decision is dated and internal, so neither forcing condition applies. The dependency is stated in Scope instead
* The brief's out-of-scope list is not carried: choosing which pages to keep offline, searching pages not kept on the device and offline access in the Support console. Say if you want those in a No-gos section, which brings Delivery in
* No `#### **References**` section, since no links came through

Assumptions behind the draft, for you to strike:
* The four areas use Oskar's own wording, and the two Scope groups order them by what the conflict decision holds back rather than by importance
* Criteria 1 and 2 assert the outcome the brief states, and no criterion asserts how conflicting edits resolve, because that is undecided
* Release-level criteria adopt Oskar's two measures, and plan availability became its own criterion from your answer

Next step: the conflict decision lands on 2026-10-09 and will change the Requirements of Offline editing and creation and Sync on reconnect. Offline reading is the story that does not wait on it, so that is the one I would draft first.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `lost-edit` and `#sync-eng` (supplied identifiers), `Given`, `When`, `Then` and `And` repeated verbatim in every criterion (fixed house labels), iOS, Android and Desktop repeated as a three-platform set (fixed by the subject), the fixed template lead-ins `The following issues rise from that:` and `In order to get there, we will:`.
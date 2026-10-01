```markdown
# Epic - Platform - Offline mode

* * *
## About
* * *
Offline mode keeps a member working when the connection is gone. The device holds the pages they have opened, changes queue as they are made, and the workspace catches up when the connection returns. It ships on iOS, Android and Desktop for every plan, Free included. Web stays out, because a browser tab cannot hold a local copy between visits.

This Epic is split into four child stories, one per area: offline reading, offline editing and creation, sync on reconnect, the offline indicator and storage settings. Each story covers all three platforms and carries its own requirements and acceptance criteria.

#### Problem
* * *
Loomlist needs a connection for everything past the page already on screen, so a drop ends the session and its work. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. 31% of Plus workspaces that gave a reason in the April to August cancellation survey named offline access.

**The following issues rise from that:**
*   A session that starts without a connection shows the page already on screen and nothing else
*   An edit made while the connection is gone is retried until the app closes, and then lost
*   Sync-service resolves every overlap with block-level last-writer-wins on protocol v3, so a device away for a day can replace a teammate's morning of edits
*   Some of the `lost-edit` tickets raised in `#sync-eng` start with a dropped connection
####   

#### Goal
* * *
A member on iOS, Android or Desktop can open, read, edit and create pages with no connection, and everyone else sees those changes once the device is back online.

**Direct user/Barter benefits:**
*   A member keeps reading and editing through a dropped connection instead of losing the work
*   Work done offline reaches the rest of the workspace once the connection returns
*   Free workspaces get offline mode alongside Plus and Team
####   

#### Solution
* * *
In order to get there, we will:
*   Keep the pages a member has recently opened on the device, so reading survives a dropped connection
*   Queue edits, checked-off to-dos and new pages on the device while there is no connection
*   Upload the queue as the connection returns, oldest change first
*   Show the connection state, the changes waiting to sync and the space offline data uses

## Scope
* * *
Each child story owns one area of offline mode and covers iOS, Android and Desktop together, and each carries its own detailed requirements and acceptance criteria. All four areas ship in Q1 2027.

Conflict handling is not settled: Joana, the Engineering Manager for Sync, decides how sync-service handles conflicting edits on 2026-10-09. The editing and sync stories cannot be finalised before that lands, while offline reading and the indicator do not depend on it.

#### Offline reading
* * *
*   Platform - Offline mode - Reading

#### Offline editing and creation
* * *
*   Platform - Offline mode - Editing and creation

#### Sync on reconnect
* * *
*   Platform - Offline mode - Sync on reconnect

#### Offline indicator and storage settings
* * *
*   Platform - Offline mode - Indicator and storage settings
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A member keeps reading and editing when the connection drops**
* * *
*   **Given** a member on iOS, Android or Desktop whose connection has dropped
*   **When** they open a page they have already visited and make a change
*   **Then** the page opens with its blocks, inline databases and to-dos, and the change stays on the device until the connection returns
*   **And** closing the app does not discard it
* * *
- [] _Mark as done, if the criteria are met_

2\. **Work done offline reaches the rest of the workspace**
* * *
*   **Given** a device holding changes made with no connection
*   **When** the connection returns
*   **Then** the queued changes upload oldest first, until nothing is left waiting to sync
*   **And** members who can open the page see the change without the author resending it
* * *
- [] _Mark as done, if the criteria are met_

3\. **The member can see the connection state and what offline data uses**
* * *
*   **Given** a member on a device that holds pages offline
*   **When** the connection drops, or they open the storage screen in settings
*   **Then** the top bar shows an offline marker and the changes waiting to sync are counted
*   **And** the storage screen shows the space used and lets them lower the cap or clear offline data
* * *
- [] _Mark as done, if the criteria are met_

4\. **Offline mode is available on every plan, on all three platforms**
* * *
*   **Given** a workspace on any plan, Free included
*   **When** a member uses Loomlist on iOS, Android or Desktop
*   **Then** offline mode is available without an upgrade
*   **And** it behaves the same on Free as on Plus and Team
* * *
##   
```

Export-equivalent path: `export/002 - Epic-offline-mode.md`

Artifact kind: **Epic**. The four areas are an initiative split across child stories, so requirements and screen-level criteria belong to the children, and this artifact carries the Problem, the Goal, the Scope and release-level criteria only. It takes 002 because the clarification block holds 001 in this lane.

Quality: About umbrella present with Problem, Goal and Solution, then Scope with four child stories and four release-level criteria. No `## Requirements`, and no `## Delivery`, since you did not ask for a delivery view and nothing forced one. Joana's decision carries a date, so the dependency sits in the Scope intro rather than in Delivery.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the hyphen separator in the title, which is the house topic-title shape, and the repeated `Given`, `When`, `Then` and `And` labels, which the house grammar fixes verbatim.

My calls, and you can strike any of them:

- The H1 reads `Epic - Platform - Offline mode`, because the work spans three client surfaces and no single platform names it. Web is stated as out of scope in About.
- One Scope group per area, holding the single child story you asked for, with each story named in the form its own H1 will take.
- The supplied values stay with the child story that owns them: the 500-page set and 1 GB cap with Reading, the upload floor and oldest-first order with Sync on reconnect, the cap control and clear-data action with the indicator story. The Epic states outcomes at release level and leaves those numbers where a build would meet them.
- Q1 2027 sits in the Scope intro, since the Epic shape has no field for a target. The two success measures (a halved no-connection session share within 8 weeks, and `lost-edit` tickets stopping) are measurement rather than release outcomes, so they are not criteria. Say the word and I will add a `## Delivery` section with Estimation, the target and those measures.
- `#### **References**` is omitted, because no link came through. Send the brief, the `#sync-eng` thread and the survey and the section goes in.

Next step: confirm the calls above, then I can draft the four child stories from the same brief.
# Sync conflicts and lost edits, options for the 2026-10-09 decision

* * *
> **Status: Proposal — not current product behavior**
> Options A, B and C are candidates, and none of them is approved. Joana, Engineering Manager, Sync, decides on 2026-10-09 once Tomasz's spike on Option B is done. Until then protocol v3 stays as it is.
* * *

## Overview
* * *

On 2026-10-09 Joana decides how sync-service should handle two devices editing the same block. This proposal sets out the three options raised in #sync-eng. It gives Sync and Mobile engineers and the Support lead one shared account of each option's cost, its trade-offs and who backs it. Nothing here is decided.

The decision matters because v3 loses edits without a trace. Support tagged 40 tickets `lost-edit` in August, up from 22 in July. Page history can't restore any of them.
* * *

### Current state in protocol v3
* * *

Protocol v3 settles conflicts with block-level last-writer-wins. A conflict happens when two devices change the same block between their sync sessions. Whichever version reaches sync-service last replaces the other, and the replaced version isn't saved anywhere. Page history only keeps what reached sync-service, so it has nothing to restore. v3 has no merge and no conflict copy. Changing the protocol means every client has to run a version that supports the new protocol.

Marta, Support Lead, says nearly all the August tickets follow the same pattern. A member edits a page on their phone on the train, then edits it again on the laptop at the office, and the phone edit is gone.

*   **`lost-edit` tickets** — 22 in July, 40 in August
*   **Sessions that overwrite** — Over the last 30 days, 0.8% of sync sessions that upload edits overwrote a block another device had changed since this device last pulled. Not every one of these is an edit someone noticed was missing (Yara, Data Lead)
*   **What those sessions changed** — 58% changed only a to-do's checkbox, due date or assignee. 42% changed text (Yara)
*   **Phones** — Pages edited on phones show up more often than their share, because phones sync less often in the background (Yara)

The ticket counts and the session share measure different things, so this proposal keeps them apart.

Until the decision, Support keeps telling members that edits made on two devices at the same time can overwrite each other.
* * *

## Options
* * *

### Option A, field-level last-writer-wins
* * *

Option A splits a block into fields and applies last-writer-wins to each field separately. If a member checks off a to-do on the phone and renames it on the laptop, both changes are kept. If both devices edit the same text, one edit is still lost.

*   **Fields** — Text, checked state, due date, assignee and reminder
*   **Protocol fit** — Works within v3 by adding a new message type
*   **Cost** — About 3 weeks of server work plus a client update (Tomasz's estimate)
*   **Covers** — "a bit over half" of overwriting sessions, based on Yara's 58% split. Tomasz calls it "the cheapest change that fixes the to-do half of these tickets"
*   **Leaves** — The 42% of overwriting sessions that changed text still lose one edit
*   **Status** — Proposed. Tomasz is writing down what Option A would take as a first step
* * *

### Option B, three-way merge on block text
* * *

With Option B, the device also sends the version it started from, and sync-service merges both edits against that base version. If the merge can't place both edits, the server keeps the later edit in place and inserts the other one as a copy of the block directly below it, labelled `Conflicting edit from {device name}`. The device name is the one the member gave the device in settings, such as Work laptop. The copy is mocked in the frame `Sync / Conflict copy`.

*   **Client change** — Clients must keep the base version, which v3 clients don't. That means a release on every platform
*   **Cost** — Roughly 6 to 8 weeks (Tomasz's estimate)
*   **Covers** — Marta estimates that 33 of the 40 August tickets would have ended with both texts on the page
*   **Formatting fallback** — Saskia, iOS Engineer, wants any block with formatting to go straight to the conflict copy. The spike includes this rule
*   **Storage** — Keeping a base version for every edited block uses storage on mobile. The cost is unknown
*   **Merge risk** — Rich text merges are prone to bugs, such as bold across a merged boundary or a mention split in half
*   **Unknown** — How often the merge falls back to a copy
*   **Status** — Proposed. Tomasz is running a two-week spike against a sample of real August conflicts
* * *

### Option C, a CRDT for block text
* * *

With Option C, simultaneous text edits always merge and there's never a conflict copy. It needs protocol v4 and a migration of every page and every client.

*   **Cost** — About two quarters (Tomasz's estimate)
*   **Status** — Kept on the list as the long-term option. Nobody is sizing it now
* * *

### Options and trade-offs
* * *

| Option | Benefit | Cost or risk | Evidence | Status |
| ---| ---| ---| ---| --- |
| A, field-level last-writer-wins | Keeps both edits when they change different fields of a block | About 3 weeks of server work plus a client update. Edits to the same text still lose one | 58% of overwriting sessions changed only a checkbox, due date or assignee | Proposed |
| B, three-way merge on block text | Merges text edits and shows a labelled copy when it can't | Roughly 6 to 8 weeks and a release on every platform. Mobile storage cost and fallback rate unknown. Rich text merge bugs | Marta's estimate of 33 of 40 August tickets | Proposed, in spike |
| C, CRDT for block text | Simultaneous text edits always merge, with no conflict copy | Protocol v4 and a migration of every page and every client, about two quarters | Tomasz's estimate only | Long-term, not sized |
* * *

## Where the thread landed
* * *

Option B has the most support in the thread, and two people back it only with conditions. There's no recommendation or decision on record.

*   **Selin, Product Designer, Sync** — Backs Option B because it's the one she can explain to members. She thinks a silently merged paragraph that reads wrong is worse than a visible copy
*   **Marta, Support Lead** — Backs Option B, based on her estimate of 33 of the 40 August tickets
*   **Tomasz, Backend Engineer, Sync** — Leans towards Option B, but only with Saskia's formatting fallback. He sees Option A as the cheapest change for the to-do half
*   **Saskia, iOS Engineer** — Worried about Option B on mobile because of storage and rich text merge bugs. If Option B is chosen, she wants blocks with formatting to go straight to the conflict copy
*   **Yara, Data Lead** — Provided the numbers without taking a position
*   **Joana, Engineering Manager, Sync** — Didn't decide in the thread. She notes that Option B has the most support, but its storage cost on mobile and how often the merge falls back to a copy are still unknown
* * *

## Open decisions
* * *

*   [ ] **Choose the option.** Joana decides on 2026-10-09 among Options A, B and C, including whether Option A comes first
*   [ ] **Measure Option B's storage cost on mobile.** Part of Tomasz's spike
*   [ ] **Measure how often Option B's merge falls back to a copy.** Part of Tomasz's spike, with the formatting fallback in place
*   [ ] **Write down what Option A takes as a first step.** Owned by Tomasz
* * *

### Out of scope
* * *

*   Offline editing plans and their effect on conflict volume
*   Sizing Option C
*   Changes to what Support tells members before the decision
* * *

### Source basis
* * *

*   **#sync-eng thread export, lost edits between devices** — Governing source, exported by Joana on 2026-09-22. Covers current v3 behavior, the options and each person's position
*   **Loomlist product context** — Background on how v3 and page history work today, kept by Elif, Product Operations, last updated 2026-09-22
*   **`Sync conflicts, options for v3 and after`** — Cited in the thread but not supplied. The options above are described only as the thread states them
*   **`Sync / Conflict copy`** — Design frame cited in the thread but not supplied

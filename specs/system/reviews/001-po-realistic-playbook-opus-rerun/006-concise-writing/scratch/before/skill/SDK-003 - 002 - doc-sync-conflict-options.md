# Sync conflicts and lost edits: options before the 2026-10-09 decision

* * *
> **Status: Proposal — not decided**
> This document compares three candidate changes to how sync-service handles conflicts. None is approved or built. Joana, Engineering Manager, Sync, decides on 2026-10-09 after a two-week spike on Option B.
* * *

## Overview
* * *
Joana decides on 2026-10-09 how Loomlist should handle two devices changing the same block. Three options are on the table and none is chosen. This document sets out what each would cost, what it fixes and where people in the #sync-eng thread landed, so the Sync and Mobile engineers and the Support lead can read it before that call.

The problem is growing and members cannot recover from it. Support tagged 40 tickets `lost-edit` in August, up from 22 in July, and nearly all follow one pattern: a member edits a page on their phone, edits it again on a laptop and the phone edit is gone. Page history does not hold the lost version either, so Support has nothing to restore.
* * *

### Current state
* * *
Status: Current behavior — verified for sync protocol v3, per the context page and Tomasz in the thread

Protocol v3 resolves conflicts with block-level last-writer-wins. In each sync session a device uploads the blocks it changed and pulls newer ones. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other, and the replaced version is never written anywhere.

Page history only keeps what reached sync-service, which means an edit that lost a conflict never appears in it. Protocol v3 has no merge and no conflict copy, and changing the protocol needs every client on a version that speaks the new one. Pages edited on phones are over-represented in conflicts, since phones sync less often in the background.
* * *

### What the numbers show
* * *
| Figure | Value | Source | Note |
| --- | --- | --- | --- |
| `lost-edit` tickets, July | 22 | Marta | |
| `lost-edit` tickets, August | 40 | Marta | Nearly all describe edits on two devices |
| Sync sessions uploading edits that overwrite a block another device changed since this device last pulled | 0.8% | Yara, last 30 days to 2026-09-14 | Not every one is an edit anyone missed, but each replaced somebody's version of a block |
| Share of those sessions that changed only a to-do's checkbox, due date or assignee | 58% | Yara, 2026-09-17 | |
| Share of those sessions that changed text | 42% | Yara, 2026-09-17 | |
| August tickets that would have ended with both texts on the page under Option B | 33 of 40 | Marta's estimate | From going back through the August tickets |

Yara's reading is that Option A alone covers a bit over half, because it handles the 58% and leaves the text changes as they are. The 0.8% counts sync sessions while the 33 of 40 counts tickets, so the two figures measure different things and should not be combined.
* * *

### Desired outcome
* * *
The thread's shared aim is that an edit made on one device is no longer replaced without a trace by an edit on another. The options differ in how much of that they deliver and in what they cost to build and roll out.
* * *

## The three options
* * *
Status: Proposal — none approved, all three still on the table per the pinned thread summary
* * *

### Option A, field-level last-writer-wins
* * *
Option A splits a block into fields and applies last-writer-wins to each field instead of the whole block. The fields are text, checked state, due date, assignee and reminder. Checking off a to-do on the phone while renaming it on the laptop would keep both changes, but two edits to the same text still lose one.

*   **Cost** — about 3 weeks of server work plus a client update, by Tomasz's estimate
*   **Protocol** — fits inside v3 with a new message type
*   **Coverage** — the to-do half of the conflicts, a bit over half of the 0.8% by Yara's split
*   **Leaves open** — every conflict where two devices edit the same text
* * *

### Option B, three-way merge on block text
* * *
Option B merges text edits against the version each device started from. The device sends that base version with its edit, and sync-service merges both edits against it. When the merge cannot place both edits, the server keeps the later edit in place and inserts the other as a copy of the block right below it, labelled `Conflicting edit from {device name}`.

The device name is the one the member gave the device in settings, such as Work laptop. Selin has mocked the copy in the frame `Sync / Conflict copy`, which was not supplied for this document.

Saskia's condition travels with this option: any block with formatting skips the merge and goes straight to the conflict copy. Tomasz's lean toward B depends on that fallback, and the spike includes it.

*   **Cost** — roughly 6 to 8 weeks, by Tomasz's estimate
*   **Clients** — every client must keep the base version, which v3 clients do not, so B needs a release on every platform
*   **Coverage** — text conflicts end with both edits on the page, merged or as a conflict copy
*   **Unmeasured** — the mobile storage cost of keeping a base version of every edited block and how often the merge falls back to a copy
*   **Not stated** — how B treats to-do field changes such as checked state or due date, since the thread describes the merge for block text only
* * *

### Option C, a CRDT for block text
* * *
Option C replaces last-writer-wins for block text with a CRDT, so concurrent text edits always merge and there is never a conflict copy. It needs protocol v4 and a migration of every page and every client.

*   **Cost** — two quarters, by Tomasz's estimate
*   **This round** — stays on the list as the long-term option, and nobody sizes it before 2026-10-09
* * *

### Options and trade-offs
* * *
| Option | Fixes | Leaves or risks | Cost, Tomasz's estimate | Release needed | Status |
| --- | --- | --- | --- | --- | --- |
| A, field-level last-writer-wins | Concurrent changes to different fields of one block, such as a check-off and a rename | Two edits to the same text still lose one | About 3 weeks of server work plus a client update | A client update, inside v3 | Proposal |
| B, three-way merge on block text | Text conflicts end with both edits on the page | Base-version storage on mobile and rich text merge bugs, plus an unmeasured fallback rate to conflict copies | Roughly 6 to 8 weeks | Every platform | Proposal, in the spike |
| C, CRDT for block text | Concurrent text edits always merge, with no conflict copy | Protocol v4 and a migration of every page and client. Selin's view is that a silently merged paragraph that reads wrong is worse than a visible copy | Two quarters | Every client, plus a page migration | Proposal, long-term, not sized |
* * *

### Where people landed
* * *
| Person | Position | Condition or concern |
| --- | --- | --- |
| Tomasz, Backend Engineer, Sync | Leans B | Only with Saskia's formatting fallback. Sees A as the cheapest change that fixes the to-do half of the tickets |
| Selin, Product Designer, Sync | B | B is the option she can explain to members, and a visible copy is better than a silently merged paragraph that reads wrong |
| Marta, Support Lead | B | Estimates that 33 of the 40 August tickets would have ended with both texts on the page |
| Saskia, iOS Engineer | Worried about B on mobile | Storage for base versions and rich text merge bugs such as bold across a merged boundary or a mention split in half. If B goes ahead, formatted blocks go straight to the conflict copy |
| Yara, Data Lead | No stated position | Supplied the 0.8% rate and the 58% and 42% split |
| Joana, Engineering Manager, Sync | Not deciding in the thread | B has the most support, but its mobile storage cost and fallback rate are unknown |

Oskar, Product Manager, Mobile, also posted in the thread. His input was about offline editing, which this document leaves out.
* * *

## Decision and next steps
* * *
Status: Approved direction — interim plan set by the decision owner on 2026-09-22, not a choice between the options

No option is chosen. Joana owns the decision and makes it on 2026-10-09. Until then the plan from the thread holds:

*   Tomasz runs a two-week spike on Option B against a sample of real August conflicts, with Saskia's formatting fallback in it
*   Tomasz writes down what Option A would take as a first step
*   Option C stays on the list as the long-term option and is not sized
*   Protocol v3 stays as it is
*   Support keeps telling members that edits made on two devices at the same time can overwrite each other

The spike is there to answer the two questions Joana named as open: what B costs in storage on mobile and how often the merge falls back to a copy.
* * *

### Dependencies and risks
* * *
*   **Every-client releases** — B needs a release on every platform and C needs every client on protocol v4. The context page notes that iOS and Android ship every two weeks and roll out over 7 days, and that Desktop runs the web client, so a Web change reaches Desktop without a Desktop release
*   **Mobile storage** — B keeps a base version of every edited block on the device, and nobody has measured that cost yet
*   **Rich text merges** — a merged boundary can break formatting or split a mention. Saskia's fallback avoids this by sending formatted blocks to the conflict copy, so the fallback rate decides how often members see a copy instead of merged text
*   **Lost edits continue** — until a change ships, conflicting edits keep disappearing with nothing to restore, and tickets went from 22 in July to 40 in August
* * *

## Open decisions
* * *
*   [ ] **Choose an option** by 2026-10-09, owned by Joana, including whether Option A goes first
*   [ ] **Measure B's mobile storage cost** in Tomasz's spike
*   [ ] **Measure B's fallback rate**, meaning how often the merge ends in a conflict copy with the formatting fallback on
*   [ ] **Write down what A would take** as a first step, owned by Tomasz
*   [ ] **Settle how B treats to-do fields**, since the thread describes the merge for block text only
*   [ ] **Settle mixed-version behavior** during a rollout, when some clients keep a base version and others still run v3. The thread does not cover it
*   [ ] **Agree the member message** Support uses once a change ships
* * *

### Out of scope
* * *
*   Offline editing plans and their effect on the conflict rate, including Oskar's input in the thread
*   Sizing Option C in this round
* * *

### Source basis
* * *
*   **`context/loomlist-sync-conflict-thread.md`** — governs the options, figures, positions and plan. The #sync-eng thread from 2026-09-14 to 2026-09-22, exported by Joana
*   **`context/loomlist-context.md`** — background on how protocol v3 behaves today, kept by Elif, Product Operations, last updated 2026-09-22
*   **Not supplied** — Tomasz's doc `Sync conflicts, options for v3 and after` and Selin's frame `Sync / Conflict copy`, both cited in the thread and not read for this document

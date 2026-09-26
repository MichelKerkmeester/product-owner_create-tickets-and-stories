# Sync conflicts and lost edits, options for protocol v3 and after

* * *
> **Status: Proposal — not decided**
> This document sets out three candidate changes to how sync-service handles conflicts. None of them is approved or built. Joana, Engineering Manager, Sync, decides on 2026-10-09, and until then protocol v3 stays as it is.
* * *

## Overview
* * *
Joana has to choose how Loomlist stops losing edits when a member changes the same block on two devices. The options on the table are field-level last-writer-wins (Option A), a three-way merge on block text (Option B) and a CRDT for block text (Option C). This document is for the Sync and Mobile engineers and the Support lead, so they can read each option's cost and trade-offs and where the thread landed before the call is made.

The ticket count is climbing. August closed with 40 Support tickets tagged `lost-edit`, up from 22 in July, and Support cannot restore the lost edits because page history does not have them.

### Current state
* * *
Status: Current behavior — protocol v3, as described in the thread and the product context page

Protocol v3 is block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other one. The replaced version is not written anywhere. Page history only holds what reached sync-service, so it has nothing to give back, and v3 has no merge and no conflict copy.

Marta, Support Lead, describes the typical ticket: a member edits a page on their phone on the train, then edits it again on the laptop at the office, and the phone edit is gone. Until a decision lands, Support keeps telling members that edits made on two devices at the same time can overwrite each other.

Yara, Data Lead, measured the scale over the last 30 days, as of 2026-09-14:

*   **Overwrites** — 0.8% of sync sessions that upload edits overwrite a block another device changed since this device last pulled. Not every one is an edit anyone missed, but each one replaced somebody's version of a block
*   **What changed** — 58% of those sessions changed only a to-do's checkbox, due date or assignee, and 42% changed text
*   **Devices** — pages edited on phones are over-represented, since phones sync less often in the background

Any protocol change needs every client on a version that speaks the new protocol. iOS and Android ship every two weeks and roll out over 7 days, so a change that needs a release on every platform waits on those cycles.

## Options
* * *
Each option below comes from Tomasz, Backend Engineer, Sync, in the doc `Sync conflicts, options for v3 and after`. The cost figures are his estimates.

### Option A, field-level last-writer-wins
* * *
Status: Proposal — not decided

Option A splits a block into fields (text, checked state, due date, assignee, reminder) and applies last-writer-wins to each field instead of the whole block. Checking off a to-do on the phone while renaming it on the laptop keeps both changes. Two edits to the same text still lose one.

*   **Cost** — fits inside v3 with a new message type, about 3 weeks of server work plus a client update
*   **Coverage** — Yara's split puts this at a bit over half of the overwriting sessions, the 58% that changed only to-do fields
*   **What it leaves** — every text conflict, the 42%, still loses one edit, as it does under v3 today

### Option B, three-way merge on block text
* * *
Status: Proposal — not decided

With Option B, the device sends the version of the block it started from, and sync-service merges both edits against that base. When the merge cannot place both edits, the server keeps the later edit in place and inserts the other one as a copy of the block right below it, labelled `Conflicting edit from {device name}`. The device name is the one the member gave the device in settings, such as Work laptop. Selin, Product Designer, Sync, has mocked the copy in the frame `Sync / Conflict copy`.

*   **Cost** — roughly 6 to 8 weeks
*   **Client impact** — clients have to keep the base version of each edited block, which v3 clients do not, so it needs a release on every platform
*   **Mobile storage** — keeping a base version for every edited block costs storage on the device, and nobody has sized that yet
*   **Merge risk** — rich text merges are where bugs hide, such as bold running across a merged boundary or a mention split in half
*   **Formatting fallback** — Saskia, iOS Engineer, wants any block with formatting to go straight to the conflict copy instead of being merged

Marta went back through the August tickets and thinks 33 of the 40 would have ended with both texts on the page under Option B. That is her read of the tickets rather than a measured figure, and it does not separate clean merges from conflict copies.

### Option C, a CRDT for block text
* * *
Status: Proposal — long-term option, not sized

Option C replaces block text with a CRDT, so concurrent text edits always merge and there is never a conflict copy.

*   **Cost** — Tomasz estimates two quarters
*   **Protocol** — needs protocol v4
*   **Migration** — every page and every client has to migrate

### Options and trade-offs
* * *

| Option | Keeps both edits when | Still loses an edit when | Cost estimate | Client release |
| ---| ---| ---| ---| --- |
| A, field-level last-writer-wins | The two devices changed different fields of a block | Both devices changed the same text | About 3 weeks of server work plus a client update | A client update, inside v3 |
| B, three-way merge | The merge can place both text edits, or it falls back to a visible conflict copy | Not stated in the thread | 6 to 8 weeks | Every platform, clients must keep base versions |
| C, CRDT for block text | Always, concurrent text edits merge | Not stated in the thread | Two quarters | Protocol v4 and a migration of every page and client |

## Where the thread landed
* * *
Status: Proposal — positions from the #sync-eng thread, 2026-09-14 to 2026-09-22

Option B has the most support, and Joana has said so without deciding. Selin backs it because she can explain it to members: a silently merged paragraph that reads wrong is worse than a visible copy. Marta gave it a +1 on the strength of her August ticket read.

Tomasz leans toward B too, but only with Saskia's formatting fallback. He also points out that A is the cheapest change that fixes the to-do half of the tickets. Saskia did not choose an option. She raised the mobile storage and rich text risks, and she made the formatting fallback her condition if the team goes with B.

Nobody argued for C as the next step. Joana keeps it on the list as the long-term option, and nobody sizes it now.

### What happens before the decision
* * *
Joana named two unknowns about B: what it costs in storage on mobile and how often the merge falls back to a copy. To answer them, Tomasz runs a two-week spike on B against a sample of real August conflicts, with Saskia's formatting fallback included. In the same spike he writes down what A would take as a first step. Protocol v3 and the Support message to members stay as they are until 2026-10-09.

### Dependencies and risks
* * *
*   **Every-platform release** — B needs a release on every platform and C needs every client migrated, so either one waits on the iOS and Android release and rollout cycles
*   **Mobile storage** — the storage cost of base versions under B is unknown until the spike reports
*   **Fallback rate** — how often members get a conflict copy instead of one merged block is unknown until the spike reports
*   **Rich text merges** — B can produce broken formatting or split mentions unless formatted blocks skip the merge
*   **Text conflicts under A** — shipping A alone leaves the 42% of overwriting sessions that changed text exactly as they are today

## Open decisions
* * *
*   [ ] **Which option, or which order** — Joana decides on 2026-10-09, including whether A ships first as a step
*   [ ] **Storage cost of B on mobile** — answered by Tomasz's spike
*   [ ] **How often the merge falls back to a copy** — answered by the same spike against August conflicts
*   [ ] **What A takes as a first step** — Tomasz writes it down during the spike
*   [ ] **Formatting fallback** — whether formatted blocks always go straight to the conflict copy if B is chosen, raised by Saskia and tested in the spike

### Out of scope
* * *
*   Offline editing plans, left out at the requester's direction
*   Sizing Option C, which Joana has deferred

### Source basis
* * *
*   `context/loomlist-sync-conflict-thread.md` — governs this document, covering the options, cost estimates, positions, spike plan and decision date
*   `context/loomlist-context.md` — background on how protocol v3, page history and the release cycles work today

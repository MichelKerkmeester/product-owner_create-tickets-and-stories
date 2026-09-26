# Sync conflict options before the 2026-10-09 decision

* * *
> **Status: Proposal — not decided, not current product behavior**
> Options A, B and C below are candidates from the #sync-eng thread. Joana, Engineering Manager, Sync, decides on 2026-10-09. Until then protocol v3 stays as it is.
* * *

## Overview
* * *
Loomlist has to decide how sync-service should handle two devices editing the same block, because today one of the two edits is lost for good. This document sets out the three options on the table, what each costs, what each leaves unsolved and where people in the #sync-eng thread landed. It is for the Sync and Mobile engineers and the Support lead to read before Joana makes the call on 2026-10-09. It makes no recommendation, since nothing is settled.

The problem is showing up in Support. August closed with 40 tickets tagged `lost-edit`, up from 22 in July. Nearly all describe the same case: a member edits a page on their phone and then on a laptop, and the phone edit is gone with no copy in page history to restore.
* * *

### Current state in protocol v3
* * *
Status: Current behavior — protocol v3, as described in the thread and the Loomlist product context page

Protocol v3 resolves conflicts with block-level last-writer-wins. A conflict is two devices changing the same block between their sync sessions, where a sync session is one exchange in which a device uploads changed blocks and pulls newer ones. When that happens, sync-service keeps the version that reaches it last and replaces the other.

The replaced version is never written anywhere. Page history only keeps what reached sync-service, so an edit that lost a conflict never appears in it and Support has nothing to restore. v3 has no merge and no conflict copy, and changing the protocol needs every client on a version that speaks the new one.
* * *

### What the data shows
* * *
Yara, Data Lead, pulled these figures from the last 30 days as of 2026-09-14.

*   **Overwrite rate** — 0.8% of sync sessions that upload edits overwrite a block another device changed since this device last pulled. Not every one is an edit someone missed, but each one replaced somebody's version of a block
*   **Where it happens** — pages edited on phones are over-represented, since phones sync less often in the background
*   **What changed** — 58% of those sessions changed only a to-do's checkbox, due date or assignee, and 42% changed text

That split is the main input to the options below, because it decides how much of the problem a to-do-only fix removes.
* * *

### Until the decision
* * *
v3 stays unchanged until 2026-10-09. Support keeps telling members that edits made on two devices at the same time can overwrite each other.
* * *

## Options
* * *
### Option A, field-level last-writer-wins
* * *
Status: Proposal — described by Tomasz, Backend Engineer, Sync

Option A splits a block into fields and applies last-writer-wins to each field separately instead of to the whole block. Checking off a to-do on the phone while renaming it on the laptop then keeps both changes. Two edits to the same text still lose one.

*   **Fields** — text, checked state, due date, assignee, reminder
*   **Protocol** — fits inside v3 with a new message type
*   **Cost** — about 3 weeks of server work plus a client update, per Tomasz's estimate
*   **Coverage** — Yara puts it at a bit over half of the overwriting sessions, the 58% that changed only to-do fields
*   **Left unsolved** — the 42% of sessions that changed text
* * *

### Option B, three-way merge on block text
* * *
Status: Proposal — described by Tomasz, spike in progress

With Option B the device sends the version of the block it started from, and sync-service merges both edits against that base. When the merge cannot place both edits, the server keeps the later edit in place and inserts the other one as a copy of the block directly below it, labelled `Conflicting edit from {device name}`. So no edit is dropped silently: it is either merged or visible as a copy.

*   **Conflict copy label** — `Conflicting edit from {device name}`, using the name the member gave the device in settings, such as Work laptop. Selin has mocked it in the frame `Sync / Conflict copy`
*   **Client change** — clients have to keep the base version, which v3 clients do not, so it needs a release on every platform
*   **Cost** — roughly 6 to 8 weeks, per Tomasz's estimate
*   **Formatting fallback** — Saskia, iOS Engineer, wants any block with formatting to go straight to the conflict copy instead of being merged. Tomasz leans B only with this fallback, and the spike includes it
*   **Mobile storage** — keeping a base version for every edited block costs storage on the device. How much is not known yet
*   **Merge risk** — rich text merges are where bugs hide, such as bold across a merged boundary or a mention split in half
*   **Unknown** — how often the merge falls back to a conflict copy
* * *

### Option C, a CRDT for block text
* * *
Status: Proposal — long-term option, not being sized now

Option C replaces block text with a CRDT, so concurrent text edits always merge and there is never a conflict copy. It needs protocol v4 and a migration of every page and every client. Tomasz estimates two quarters. Joana has kept it on the list as the long-term option and asked that nobody size it now.
* * *

### Options and trade-offs
* * *

| Option | What it fixes | What it leaves | Cost estimate | Main risk or unknown |
| ---| ---| ---| ---| --- |
| A, field-level last-writer-wins | To-do field conflicts, a bit over half of overwriting sessions | Text conflicts still lose one edit | About 3 weeks server work plus a client update | Does nothing for the 42% that changed text |
| B, three-way merge on block text | Text conflicts, either merged or kept as a visible copy | A conflict copy whenever the merge cannot place both edits | Roughly 6 to 8 weeks, release on every platform | Mobile storage cost, rich text merge bugs, fallback rate |
| C, CRDT for block text | All concurrent text edits, with no conflict copy | Nothing named in the thread | About two quarters, protocol v4 and full migration | Size and migration, and it is not being sized now |

All cost figures are Tomasz's estimates from the thread, not sized plans.
* * *

### Where people in the thread landed
* * *
Most support in the thread is for Option B, with conditions attached. Nobody argued for C as the near-term answer.

*   **Selin, Product Designer, Sync** — for B. It is the option she can explain to members, and she holds that a silently merged paragraph that reads wrong is worse than a visible copy
*   **Marta, Support Lead** — for B. Going back through August, she thinks 33 of the 40 tickets would have ended with both texts on the page. This is her estimate, not a measured figure
*   **Saskia, iOS Engineer** — worried about B on mobile because of storage and rich text merge bugs. Accepts it only if any block with formatting goes straight to the conflict copy
*   **Tomasz, Backend Engineer, Sync** — leans B, but only with Saskia's fallback. Sees A as the cheapest change that fixes the to-do half of the tickets
*   **Yara, Data Lead** — took no position and supplied the overwrite rate and the 58/42 split
*   **Joana, Engineering Manager, Sync** — not deciding in the thread. Notes that B has the most support but that its mobile storage cost and fallback rate are unknown
* * *

## Decision and open questions
* * *
Joana owns the decision and will make it on 2026-10-09.

Before then, Tomasz runs a two-week spike on Option B against a sample of real August conflicts, with Saskia's formatting fallback included. He also writes down what Option A would take as a first step. Option C stays on the list without sizing.
* * *

### Open decisions
* * *
*   [ ] **Pick the option.** Joana decides on 2026-10-09 between A, B and C, with A as a possible first step
*   [ ] **Measure mobile storage for B.** The spike needs to show what keeping base versions costs on the device
*   [ ] **Measure the fallback rate for B.** The spike needs to show how often real August conflicts end as a conflict copy, with the formatting fallback applied
*   [ ] **Scope A as a first step.** Tomasz writes down what A would take
* * *

### Out of scope
* * *
*   Offline editing plans and their effect on conflict rates
*   Sizing Option C
* * *

### Source basis
* * *
*   **#sync-eng thread export, 2026-09-14 to 2026-09-22** — governs the options, figures, positions and next steps. Exported by Joana on 2026-09-22
*   **Loomlist product context page, updated 2026-09-22** — background on how sync sessions, conflicts and page history work in v3 today
*   **`Sync conflicts, options for v3 and after`** — Tomasz's options doc, cited in the thread but not supplied. The option descriptions here come from his summary in the thread

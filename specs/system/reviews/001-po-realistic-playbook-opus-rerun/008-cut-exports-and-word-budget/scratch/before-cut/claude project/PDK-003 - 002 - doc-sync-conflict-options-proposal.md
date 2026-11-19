# Sync conflicts: options to replace block-level last-writer-wins

* * *
> **Status: Proposal — not decided.** Options A, B and C are candidates from the #sync-eng thread, and none of them is approved. Joana, Engineering Manager, Sync, decides on 2026-10-09. Until then, protocol v3 stays as it is.
* * *

## Overview
* * *
The decision is how sync-service should handle a conflict, which is two devices changing the same block between their sync sessions. It is needed now because Support closed August with 40 tickets tagged `lost-edit`, up from 22 in July, and none of those edits can be restored. Joana will choose between Option A, Option B and Option C on 2026-10-09.

This page is for the Sync and Mobile engineers who would build the chosen option and for Marta, Support lead, whose team answers the tickets. It sets out each option's cost, what it fixes and what it leaves, and where each person in the thread ended up. It does not recommend an option, because that decision belongs to Joana.

### Current state
* * *
Status: Current behavior — sync protocol v3, as described by Tomasz in the thread and by the Loomlist product context page

Protocol v3 resolves conflicts with block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other one. The replaced version is not saved anywhere, so page history, which keeps only what reached sync-service, has nothing to restore.

Nearly all of the August tickets follow the same pattern. A member edits a page on their phone on the train and then edits it again on the laptop at the office. The phone edit is gone.

In the 30 days before 2026-09-14, Yara found 0.8% of sync sessions that upload edits overwrote a block another device had changed since the uploading device last pulled. Not every one was an edit someone missed, but each replaced someone's version of a block. Pages edited on phones are overrepresented, because phones sync less often in the background.

Yara split the overwriting sessions by what changed:

*   **58%** — changed only a to-do's checkbox, due date or assignee
*   **42%** — changed text

Any change to this behavior needs client work. v3 has no merge and no conflict copy, and changing the protocol requires every client to run a version that supports the new one.

## The options
* * *
Status: Proposal — all three options are candidates, and the costs are Tomasz's estimates from the thread

Tomasz wrote the options up in the doc `Sync conflicts, options for v3 and after`. That doc was not part of the material for this page, so each option below is described from the thread alone.

### Option A, field-level last-writer-wins
* * *
Option A is the cheapest change. It fixes the to-do side of the problem and leaves text conflicts as they are today.

*   **How it works** — a block splits into fields (text, checked state, due date, assignee, reminder), and last-writer-wins applies per field, not per block
*   **What it fixes** — checking off a to-do on the phone while renaming it on the laptop keeps both changes
*   Yara puts that at a bit over half of the overwriting sessions, which matches the 58% that changed only to-do fields
*   **What it leaves** — two edits to the same text still lose one, which affects the 42% of overwriting sessions that changed text
*   **Cost** — about 3 weeks of server work plus a client update, fitting inside v3 with a new message type

### Option B, three-way merge on block text
* * *
Option B keeps both text edits, either merged or as a visible copy. In exchange, every client has to store more and ship a release.

*   **How it works** — the device sends the version it started from, and sync-service merges both edits against that base
*   If the merge can't place both, the later edit stays and the other becomes a copy of the block directly below, labelled `Conflicting edit from {device name}`
*   **Conflict copy** — `{device name}` is the member's name for the device in settings, for example Work laptop, and Selin has mocked the copy in `Sync / Conflict copy`
*   **What it fixes** — no text edit is dropped, and by Marta's own read, 33 of the 40 August tickets would have kept both texts
*   **What it leaves** — edits the merge can't place end up as a conflict copy, which the member has to reconcile by hand
*   **Cost** — roughly 6 to 8 weeks, and because clients must keep the base version, which v3 clients don't, every platform needs a release
*   **Proposed condition** — Saskia wants any block with formatting to go straight to the conflict copy instead of being merged

### Option C, a CRDT for block text
* * *
Option C removes text conflicts completely. It costs the most and needs a new protocol.

*   **How it works** — concurrent text edits always merge, and there is never a conflict copy
*   **What it fixes** — no text edit is ever lost or split out into a copy
*   **Cost** — protocol v4 and a migration of every page and every client, which Tomasz estimates at two quarters

### Options compared
* * *

| Option | Both edits kept when | Still lost | Client impact | Rough cost | Status |
| --- | --- | --- | --- | --- | --- |
| A, field-level last-writer-wins | The devices changed different fields of the same block | One of two edits to the same text | Client update, new message type inside v3 | About 3 weeks of server work plus a client update | Proposal |
| B, three-way merge on block text | The merge can place both text edits. Otherwise both survive, one as a conflict copy | No text edit | Release on every platform, clients keep base versions | Roughly 6 to 8 weeks | Proposal, most support in the thread |
| C, CRDT for block text | Always, for concurrent text edits | No text edit | Protocol v4 and migration of every page and client | About two quarters | Proposal, long-term, not being sized |

## Where the thread landed
* * *
Option B has the most support, but two people attached conditions to it. Nobody argued for C as the near-term fix.

Selin prefers B from the design side. A visible copy is something she can explain to members, and a silently merged paragraph that reads wrong is worse. Marta backs B because of her 33-of-40 estimate.

Saskia is worried about B on mobile, because a base version for every edited block costs storage on the device. Rich text merges are also where bugs tend to appear, for example bold across a merged boundary or a mention split in half. Her formatting fallback is her condition for B.

Tomasz leans towards B as well, but only with Saskia's fallback. He calls A the cheapest change that fixes the to-do half of the tickets.

Joana chose not to decide in the thread. B has the most support, but she named two things that nobody knows yet: how much storage B costs on mobile and how often the merge falls back to a copy. C stays on the list as the long-term option.

Status: Approved direction — set by Joana in the thread on 2026-09-22

Tomasz is running a two-week spike on Option B against a sample of real August conflicts, with Saskia's formatting fallback included. He is also writing down what Option A would take as a first step, and nobody is sizing C now.

Until the decision, v3 stays as it is, and Support keeps telling members that edits made on two devices at the same time can overwrite each other.

### Risks and dependencies
* * *
*   **Every client has to support the new protocol** — A needs a client update, B a release on every platform and C every client on v4
*   **Rich text merge bugs** — bold across a merged boundary or a mention split in half, which Saskia's fallback avoids by never merging formatted blocks
*   **Mobile storage for B** — clients would keep a base version for every edited block, a cost the spike is meant to measure
*   **To-do fields under B and C** — the thread covers B and C for block text only, not a conflicting checkbox, due date or assignee change

### Open decisions and pending evidence
* * *
*   [ ] **Choose between Options A, B and C:** Joana decides on 2026-10-09
*   [ ] **Measure B's storage cost on mobile:** Tomasz's spike should produce this number
*   [ ] **Measure how often B falls back to a conflict copy:** Also from the spike, on real August conflicts with the formatting fallback included
*   [ ] **Write down what Option A would take as a first step:** Tomasz owns this alongside the spike
*   [ ] **Confirm the spike's timing:** The thread gives two weeks but no start date, so it is unconfirmed that results will be ready before 2026-10-09

### Out of scope
* * *
*   Offline mode plans and how each option would hold up under them
*   Sizing Option C
*   A recommendation from this page, since the choice belongs to Joana

### Source basis
* * *
*   **Thread export, #sync-eng, lost edits between devices** — the governing source for the options, costs, numbers, positions and next steps, exported by Joana on 2026-09-22
*   **Loomlist product context** — background only, for how protocol v3, page history and protocol changes work today, kept by Elif, Product Operations
*   **`Sync conflicts, options for v3 and after`** — Tomasz's options doc, mentioned in the thread but not supplied
*   **`Sync / Conflict copy`** — Selin's design frame, mentioned in the thread but not supplied

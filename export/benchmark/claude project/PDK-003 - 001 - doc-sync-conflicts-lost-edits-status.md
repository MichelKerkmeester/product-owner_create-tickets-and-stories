# Sync conflicts and lost edits: where things stand

* * *
> **Status: Not decided.** The way protocol v3 loses edits today is current behavior. Options A, B and C are proposals from the #sync-eng thread, and none of them is approved. Joana, Engineering Manager, Sync, decides on 2026-10-09.
* * *

Members lose edits when they change the same page on two devices. Support closed August with 40 tickets tagged `lost-edit`, up from 22 in July. The lost edit cannot be restored because page history never recorded it. The cause is the way sync protocol v3 handles a conflict. It is not a fault in any one client.

The #sync-eng thread has three fixes on the table, and Option B has the most support. Nothing is decided yet. Joana will decide on 2026-10-09, after Tomasz runs a two-week spike on Option B. Until then v3 stays as it is.

This page is for the Sync, Mobile, Support and Data people in that thread and for anyone who needs the state of the question before the decision. It summarises the thread Joana exported on 2026-09-22, checked against the Loomlist product context page.

## How edits get lost today
* * *
Status: Current behavior — sync protocol v3, as described by Tomasz in the thread and by the Loomlist product context page

The loss comes from one rule in sync-service. Phones run into it more often than other devices.

### What protocol v3 does
* * *
Protocol v3 settles conflicts with block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other one. The replaced version is not saved anywhere.

That is why Support cannot restore anything. Page history keeps only what reached sync-service, so an edit that lost a conflict never appears in it. Nearly all the tickets Marta reviewed follow one pattern. A member edits a page on their phone on the train and then edits it again on the laptop at the office. The phone edit is gone.

A fix reaches members only when every client runs a version that supports the new protocol. v3 has no merge and no conflict copy, and a protocol change needs every client to be on a version that supports it.

### How often it happens
* * *
Yara measured the 30 days before 2026-09-14. In that period, 0.8% of sync sessions that upload edits overwrote a block that another device had changed since this device last pulled. Each of those sessions replaced someone's version of a block, but not every one was an edit that someone missed. Pages edited on phones show up more often than their share, because phones sync less often in the background.

Yara then split those overwriting sessions by what changed:

*   **58%** — changed only a to-do's checkbox, due date or assignee
*   **42%** — changed text

Oskar expects offline editing to push the 0.8% up sharply. A phone that was offline for a day comes back with every edit at once. He does not want to ship offline editing on top of v3 as it works today. Loomlist has no offline mode yet, so this is a requirement for the fix rather than a cause of today's tickets.

## The options on the table
* * *
Status: Proposal — none of the three options is approved

Tomasz wrote the options up in the doc `Sync conflicts, options for v3 and after`. That doc was not part of the material for this page. The costs below are his estimates from the thread.

| Option | What changes | What still gets lost | Rough cost | Status |
| --- | --- | --- | --- | --- |
| Option A, field-level last-writer-wins | A block splits into fields (text, checked state, due date, assignee, reminder), and last-writer-wins applies to each field separately. Checking off a to-do on the phone while renaming it on the laptop keeps both changes | Two edits to the same text still lose one | About 3 weeks of server work plus a client update. Fits inside v3 with a new message type | Proposal |
| Option B, three-way merge on block text | The device sends the version it started from, and sync-service merges both edits against that base. If it cannot place both edits, the later edit stays in place and the other goes in as a copy of the block directly below it, labelled `Conflicting edit from {device name}` | No text edit is dropped. An edit the merge cannot place survives as a conflict copy | Roughly 6 to 8 weeks. Clients must keep the base version, which v3 clients do not do, so every platform needs a release | Proposal, most support in the thread |
| Option C, a CRDT for block text | Concurrent text edits always merge, and there is never a conflict copy | No text edit, since concurrent text edits always merge | Needs protocol v4 and a migration of every page and every client. About two quarters | Proposal, long-term, not being sized |

### Where the thread landed
* * *
Option B has the most support, with conditions. Selin finds a visible copy easier to explain to members than a silently merged paragraph that reads wrong. She has mocked the copy in the frame `Sync / Conflict copy`. The `{device name}` in the label is the name the member gave the device in settings, for example Work laptop. Marta estimates that under B, 33 of the 40 August tickets would have ended with both texts on the page. That number is her own read of the tickets, not a measurement.

Saskia's concerns about B are on mobile. Keeping a base version for every edited block costs storage on the device, and the offline work Oskar is scoping needs a lot of pages stored there too. Rich text merges are also where bugs tend to appear, such as bold across a merged boundary or a mention split in half. Her condition is that any block with formatting goes straight to the conflict copy instead of being merged.

Tomasz also leans towards B, but only with Saskia's fallback. He calls A the cheapest change that fixes the to-do half of the tickets. Yara's split puts A's coverage at a bit over half of the overwriting sessions.

C stays on the list as the long-term option. Nobody is sizing it now.

## What happens before the decision
* * *
Status: Approved direction — set by Joana in the thread on 2026-09-22

Joana will decide on 2026-10-09 and chose not to decide in the thread. The decision waits on two things nobody knows yet about B: how much storage it costs on mobile and how often the merge falls back to a copy. Until the decision, protocol v3 stays as it is.

*   [ ] **Run a two-week spike on Option B.** Tomasz runs it against a sample of real August conflicts, with Saskia's formatting fallback included
*   [ ] **Write down what Option A would take as a first step.** Tomasz owns this alongside the spike
*   [ ] **Keep the current support message.** Support keeps telling members that edits made on two devices at the same time can overwrite each other
*   [ ] **Decide on 2026-10-09.** Joana chooses between Option A, Option B and Option C

### Open questions
* * *
*   **B's storage cost on mobile** — unknown until the spike reports
*   **How often B falls back to a conflict copy** — unknown until the spike reports. The spike includes the formatting fallback, which sends every formatted block to a copy
*   **Offline editing** — Oskar needs the chosen option to hold up when a phone comes back after a day offline. The thread does not say how A or B would handle that
*   **Spike timing** — the thread gives the spike's length as two weeks but no start date, so it is not confirmed that results will be ready before 2026-10-09
*   **The rest of the `lost-edit` tickets** — Marta says nearly all August tickets follow the two-device pattern. The context page describes a second way edits get lost: an edit made without a connection is retried until the app closes and is then lost. Nobody has checked whether that explains the remaining tickets

### Sources
* * *
*   **Thread export, #sync-eng, lost edits between devices** — exported by Joana on 2026-09-22 from the thread Marta started on 2026-09-14. Source for the options, the numbers and the next steps
*   **Loomlist product context** — kept by Elif, Product Operations, and last updated 2026-09-22. Source for how sync-service, page history and protocol changes work today
*   **`Sync conflicts, options for v3 and after`** — Tomasz's options doc. The thread mentions it, but it was not supplied, so this page is not checked against it
*   **`Sync / Conflict copy`** — Selin's design frame. The thread mentions it, but it was not supplied

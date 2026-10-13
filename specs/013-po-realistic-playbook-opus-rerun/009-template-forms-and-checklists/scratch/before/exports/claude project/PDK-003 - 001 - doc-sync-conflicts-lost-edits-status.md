# Sync conflicts and lost edits: where things stand

* * *
> **Status: Not decided.** Protocol v3's edit loss is current behavior, and Options A, B and C from the #sync-eng thread are unapproved proposals. Joana, Engineering Manager, Sync, decides on 2026-10-09.
* * *

Members lose edits when they change the same page on two devices. Support closed August with 40 tickets tagged `lost-edit`, up from 22 in July, and none could be restored. The cause is how sync protocol v3 handles a conflict, not any one client.

This page summarises Joana's 2026-09-22 thread export for its Sync, Mobile, Support and Data people, checked against the Loomlist product context page.

## How edits get lost today
* * *
Status: Current behavior — sync protocol v3, per Tomasz in the thread and the Loomlist product context page

### What protocol v3 does
* * *
Protocol v3 settles conflicts with block-level last-writer-wins: when two devices change the same block between sync sessions, the last version to reach sync-service replaces the other, unsaved. Page history holds only what reached sync-service, so nothing can be restored.

Nearly all tickets Marta reviewed follow one pattern: a phone edit on the train, then a laptop edit at the office, and the phone edit is gone.

v3 has no merge or conflict copy, and a fix reaches members only once every client supports the new protocol.

### How often it happens
* * *
In the 30 days before 2026-09-14, Yara found that 0.8% of edit-uploading sync sessions overwrote a block another device changed since this device's last pull, though not every one was a missed edit. Phone-edited pages are overrepresented, because phones sync less in the background.

Yara split those sessions by what changed:

*   **58%** — only a to-do's checkbox, due date or assignee
*   **42%** — text

Oskar expects offline editing to push the 0.8% up sharply and does not want to ship it on v3. Loomlist has no offline mode yet, so this is a requirement for the fix, not a cause of today's tickets.

## The options on the table
* * *
Status: Proposal — none approved

Tomasz's options doc `Sync conflicts, options for v3 and after` was not supplied, so costs are his thread estimates.

| Option | What changes | What still gets lost | Rough cost | Status |
| --- | --- | --- | --- | --- |
| Option A, field-level last-writer-wins | Each field (text, checked state, due date, assignee, reminder) gets its own last-writer-wins, so checking off a to-do on the phone while renaming it on the laptop keeps both | Two edits to the same text still lose one | About 3 weeks of server work plus a client update, inside v3 with a new message type | Proposal |
| Option B, three-way merge on block text | The device sends its starting version, and sync-service merges both edits against it. If it cannot place both, the later edit stays and the other goes in as a copy of the block directly below, labelled `Conflicting edit from {device name}` | No text edit. An edit the merge cannot place survives as a conflict copy | Roughly 6 to 8 weeks, and every platform needs a release, because clients must keep the base version | Proposal, most support in the thread |
| Option C, a CRDT for block text | Concurrent text edits always merge, with no conflict copy | No text edit | Protocol v4 and a migration of every page and client, about two quarters | Proposal, long-term, not being sized |

### Where the thread landed
* * *
Selin finds a visible copy easier to explain than a silently merged paragraph that reads wrong, and mocked it in `Sync / Conflict copy`, where `{device name}` is the member's device name from settings, such as Work laptop.

Marta estimates, by her own read rather than a measurement, that B would have kept both texts in 33 of the 40 August tickets.

Saskia's mobile concerns: base versions cost device storage that Oskar's offline work also needs, and rich text merges are bug-prone, such as bold across a merged boundary or a split mention. Her condition is that any formatted block goes straight to the conflict copy.

Tomasz leans towards B only with Saskia's fallback, and calls A the cheapest fix for the to-do half of the tickets. Yara's split puts A's coverage at a bit over half of the overwriting sessions.

C stays as the long-term option, unsized for now.

## What happens before the decision
* * *
Status: Approved direction — set by Joana in the thread on 2026-09-22

Joana chose not to decide in the thread, and v3 stays as it is until 2026-10-09. The decision waits on two unknowns about B: its storage cost on mobile and how often the merge falls back to a copy.

*   [ ] **Run a two-week spike on Option B:** Tomasz, on real August conflicts, with Saskia's formatting fallback
*   [ ] **Write down what Option A would take as a first step:** Tomasz, alongside the spike
*   [ ] **Keep the current support message:** Support keeps telling members that edits made on two devices at the same time can overwrite each other
*   [ ] **Decide on 2026-10-09:** Joana chooses between Option A, Option B and Option C

### Open questions
* * *
*   **B's storage cost on mobile** — unknown until the spike reports
*   **How often B falls back to a conflict copy** — unknown until the spike reports, and the formatting fallback adds every formatted block
*   **Offline editing** — Oskar needs the fix to handle a phone back from a day offline, which the thread does not cover for A or B
*   **Spike timing** — two weeks but no start date, so results before 2026-10-09 are unconfirmed
*   **The rest of the `lost-edit` tickets** — nearly all fit the two-device pattern, per Marta, but the context page describes a second loss path
*   An offline edit is retried until the app closes, then lost, and nobody has checked whether that explains the remaining tickets

### Sources
* * *
*   **Thread export, #sync-eng, lost edits between devices** — Joana's 2026-09-22 export of the thread Marta started on 2026-09-14, the source for options, numbers and next steps
*   **Loomlist product context** — kept by Elif, Product Operations, updated 2026-09-22, the source for how sync-service, page history and protocol changes work today
*   **`Sync conflicts, options for v3 and after`** — Tomasz's options doc, mentioned but not supplied or checked
*   **`Sync / Conflict copy`** — Selin's design frame, mentioned but not supplied

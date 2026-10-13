# Sync conflicts: options to replace block-level last-writer-wins

* * *
> **Status: Proposal — not decided.** Options A, B and C are unapproved candidates from the #sync-eng thread. Joana, Engineering Manager, Sync, decides on 2026-10-09, and protocol v3 stays as it is until then.
* * *

## Overview
* * *
The decision is how sync-service handles a conflict: two devices changing the same block between sync sessions. Support closed August with 40 tickets tagged `lost-edit`, up from 22 in July, and none of those edits can be restored.

This page is for the Sync and Mobile engineers who would build the option and for Marta, Support lead, whose team answers the tickets.

### Current state
* * *
Status: Current behavior — sync protocol v3, per Tomasz in the thread and the Loomlist product context page

Under v3's block-level last-writer-wins, the last version to reach sync-service replaces the other, unsaved, so page history has nothing to restore. Nearly all August tickets are a phone edit on the train, then a laptop edit at the office, losing the phone edit.

In the 30 days before 2026-09-14, Yara found that 0.8% of edit-uploading sync sessions overwrote a block another device changed since the uploader's last pull, though not every one was a missed edit. Phone-edited pages are overrepresented, because phones sync less in the background.

Yara split the overwriting sessions by what changed:

*   **58%** — only a to-do's checkbox, due date or assignee
*   **42%** — text

Any change needs client work. v3 has no merge and no conflict copy, and a protocol change needs every client on a version that supports it.

## The options
* * *
Status: Proposal — all three are candidates, with costs from Tomasz's thread estimates

Tomasz's options doc `Sync conflicts, options for v3 and after` was not supplied, so each option comes from the thread.

### Option A, field-level last-writer-wins
* * *
*   **How it works** — each field (text, checked state, due date, assignee, reminder) gets its own last-writer-wins
*   **What it fixes** — checking off a to-do on the phone while renaming it on the laptop keeps both
*   Yara puts that at a bit over half of overwriting sessions, matching the 58%
*   **What it leaves** — two edits to the same text still lose one, the 42%

### Option B, three-way merge on block text
* * *
*   **How it works** — the device sends its starting version, and sync-service merges both edits against it
*   If the merge can't place both, the later edit stays and the other becomes a copy of the block directly below, labelled `Conflicting edit from {device name}`
*   **Conflict copy** — `{device name}` is the member's device name from settings, such as Work laptop, mocked by Selin in `Sync / Conflict copy`
*   **What it fixes** — no text edit is dropped, and by Marta's own read, 33 of the 40 August tickets would have kept both texts
*   **What it leaves** — an edit the merge can't place becomes a conflict copy to reconcile by hand
*   **Cost** — a release on every platform, because clients must keep the base version
*   **Proposed condition** — Saskia wants formatted blocks sent straight to the conflict copy

### Option C, a CRDT for block text
* * *
*   **How it works** — concurrent text edits always merge, with no conflict copy
*   **What it fixes** — no text edit is lost or split into a copy

### Options compared
* * *

| Option | Both edits kept when | Still lost | Client impact | Rough cost | Status |
| --- | --- | --- | --- | --- | --- |
| A, field-level last-writer-wins | The devices changed different fields of one block | One of two edits to the same text | Client update, new message type inside v3 | About 3 weeks of server work plus a client update | Proposal |
| B, three-way merge on block text | The merge places both text edits. Otherwise both survive, one as a conflict copy | No text edit | Release on every platform, clients keep base versions | Roughly 6 to 8 weeks | Proposal, most support in the thread |
| C, CRDT for block text | Always, for concurrent text edits | No text edit | Protocol v4 and migration of every page and client | About two quarters | Proposal, long-term, not being sized |

## Where the thread landed
* * *
Nobody argued for C as the near-term fix.

Selin prefers B because a visible copy is easier to explain than a silently merged paragraph that reads wrong. Marta backs B on her 33-of-40 estimate.

Saskia worries about the device storage for B's base versions and about rich text merge bugs, such as bold across a merged boundary or a split mention, so her formatting fallback is her condition.

Tomasz leans towards B only with Saskia's fallback, and calls A the cheapest fix for the to-do half of the tickets.

Joana chose not to decide in the thread, pending the two measurements below. C stays as the long-term option.

Status: Approved direction — set by Joana in the thread on 2026-09-22

Tomasz is running a two-week spike on Option B against real August conflicts, with Saskia's formatting fallback, and writing down what Option A would take as a first step.

Support keeps telling members that edits on two devices at once can overwrite each other.

### Risks and dependencies
* * *
*   **Every client has to support the new protocol** — A needs a client update, B a release everywhere and C every client on v4
*   **Rich text merge bugs** — Saskia's fallback avoids them
*   **Mobile storage for B** — a base version per edited block, which the spike measures
*   **To-do fields under B and C** — the thread covers B and C for block text only, not a conflicting checkbox, due date or assignee change

### Open decisions and pending evidence
* * *
*   [ ] **Choose between Options A, B and C:** Joana decides on 2026-10-09
*   [ ] **Measure B's storage cost on mobile:** from Tomasz's spike
*   [ ] **Measure how often B falls back to a conflict copy:** also from the spike
*   [ ] **Write down what Option A would take as a first step:** Tomasz, alongside the spike
*   [ ] **Confirm the spike's timing:** two weeks but no start date, so results before 2026-10-09 are unconfirmed

### Out of scope
* * *
*   Offline mode plans and how each option holds up under them
*   Sizing Option C
*   A recommendation from this page, since the choice is Joana's

### Source basis
* * *
*   **Thread export, #sync-eng, lost edits between devices** — the governing source for options, costs, numbers, positions and next steps, exported by Joana on 2026-09-22
*   **Loomlist product context** — background only, for how protocol v3, page history and protocol changes work today, kept by Elif, Product Operations
*   **`Sync conflicts, options for v3 and after`** — Tomasz's options doc, mentioned but not supplied
*   **`Sync / Conflict copy`** — Selin's design frame, mentioned but not supplied

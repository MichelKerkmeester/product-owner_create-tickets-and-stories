# Sync conflicts and lost edits: options for v3 and after

* * *

> Status: Proposal — no option is approved, and the decision is not made. Decision owner: Joana, Engineering Manager, Sync. Decision date: 2026-10-09. Until then, v3 stays as it is.

* * *

## Overview

* * *

Two devices that change the same block between their sync sessions can lose one of the edits. Under protocol v3, the lost edit is not kept anywhere, including page history.

Support logged 40 tickets tagged `lost-edit` in August, up from 22 in July.

This document sets out the three options in the Sync thread, what each costs and where the people in the thread landed. It is written for the Sync and Mobile engineers and the Support lead, ahead of the decision. Nothing here is settled.

The #sync-eng thread, exported 2026-09-22, is the source for the options, figures and positions. The Loomlist product context page, last updated 2026-09-22, is background on how v3 works today.

## Current behavior in v3

* * *

### How a conflict plays out

* * *

Status: Current behavior — per the thread and the context page, as of 2026-09-22.

Protocol v3 uses block-level last-writer-wins, with no merge and no conflict copy. Each device uploads its changed blocks in a sync session and pulls newer ones. When two devices change the same block between sessions, the version that reaches sync-service last replaces the other.

A typical case is an edit on a phone on the train, then another on a laptop at the office. The phone edit is gone, and page history does not have it either, because history holds only what reached the server.

### What the figures show

* * *

Status: Current behavior — figures as reported in the thread, for the 30 days to 2026-09-14.

*   0.8% of sync sessions that upload edits overwrote a block another device had changed since this device last pulled
*   Not every overwrite is a missed edit, but each one replaced someone's version of a block
*   Pages edited on phones are over-represented, since phones sync less often in the background
*   Of the overwriting sessions, 58% changed only a to-do's checkbox, due date or assignee, and 42% changed text
*   Marta estimates that 33 of the 40 August tickets would have ended with both texts on the page, the outcome Option B produces

The 33 figure is Marta's reading of the tickets, not a measured count. The ticket counts and the session percentages measure different things, and the thread does not link them, so read the 58% and 42% split as a share of sessions.

### What members are told today

* * *

Status: Current behavior — per Joana's message of 2026-09-22.

Until the decision, v3 stays as it is, and Support keeps telling members that edits made on two devices at the same time can overwrite each other.

Status: Current behavior — per the context page, which the thread does not discuss.

The context page records a second loss path. An edit made while the connection is gone is retried until the app closes, then lost. No option in the thread addresses it.

## The three options

* * *

Status: Proposal — none of the three options is approved.

The options differ in what they change. Option A stays inside v3. Option C needs protocol v4. v3 clients do not keep the base version that Option B requires, so B needs a client release on every platform. The thread does not say whether B also needs a new protocol version.

### Side by side

* * *

| Option | What changes | Cost in the thread | Client impact | Main trade-off |
| --- | --- | --- | --- | --- |
| A. Field-level last-writer-wins | Splits a block into fields and applies last-writer-wins to each one | About 3 weeks of server work plus a client update | A client update, with no sizing given | Two edits to the same text still lose one |
| B. Three-way merge on block text | Merges both edits against a base version, and keeps the other edit as a copy when the merge cannot place both | Roughly 6 to 8 weeks | Clients keep the base version, so a release on every platform | Base versions cost storage, and the merge can fall back to a copy |
| C. CRDT for block text | Merges concurrent text edits, so no conflict copy is made | Two quarters, Tomasz's rough estimate, not a sizing | Protocol v4, and a migration of every page and every client | The longest estimate, and the long-term option |

### Option A: field-level last-writer-wins

* * *

Status: Proposal — not approved.

Option A splits a block into fields and applies last-writer-wins to each one. Checking off a to-do on the phone while renaming it on the laptop keeps both edits. Two edits to the same text still lose one.

Option A fits inside v3 as a new message type, at about 3 weeks of server work plus a client update. Tomasz calls it the cheapest change that fixes the to-do half of the tickets, and his spike also writes down what A would take as a first step.

Yara's split puts 58% of the overwriting sessions in the to-do group, covering checkbox, due date and assignee changes. She says Option A alone covers a bit over half. The thread does not count reminder changes, which Option A also splits out. The 42% of sessions that changed text stay exposed.

### Option B: three-way merge with a conflict copy

* * *

Status: Proposal — not approved.

The device sends the base version it started from, and sync-service merges both edits against that base. When the merge cannot place both edits, the server keeps the later edit in place and inserts the other as a copy of the block directly below it.

The copy is labelled `Conflicting edit from {device name}`, using the name the member gave the device in settings, such as `Work laptop`. Selin, Product Designer, mocked the copy in the frame `Sync / Conflict copy`. She argues that a visible copy beats "a silently merged paragraph that reads wrong".

Roughly 6 to 8 weeks. Clients must keep the base version, which v3 clients do not, so the option needs a release on every platform. Keeping a base version for every edited block costs storage, and the thread has no mobile figure.

Saskia, iOS Engineer, raised rich-text merge bugs, such as bold across a merged boundary or a mention split in half. She wants any block with formatting sent straight to the conflict copy. Tomasz leans B only with that fallback.

### Option C: CRDT for block text

* * *

Status: Proposal — not approved, and not sized.

Concurrent text edits always merge, so Option C never produces a conflict copy. It needs protocol v4 and a migration of every page and every client.

Tomasz gave a rough estimate of two quarters on 2026-09-15. Joana wrote on 2026-09-22 that C stays on the list as the long-term option and that nobody sizes it now, so treat two quarters as an early estimate. The thread does not say how Option C would handle formatted text, which is the case Saskia raised for B.

## Where people landed and what is open

* * *

### Positions in the thread

* * *

Status: Proposal — these are positions in the thread, and none is a decision.

| Person | Position | Reason in the thread |
| --- | --- | --- |
| Marta, Support Lead | Backs B | Estimates 33 of the 40 August tickets would have ended with both texts on the page |
| Tomasz, Backend Engineer, Sync | Leans B, with Saskia's formatting fallback | Calls A the cheapest change for the to-do half of the tickets |
| Selin, Product Designer, Sync | Prefers B | A visible copy beats a silently merged paragraph that reads wrong |
| Saskia, iOS Engineer | Worried about B, and wants a fallback if B goes ahead | Mobile storage for base versions, and rich-text merge bugs |
| Yara, Data Lead | No preference recorded | Supplied the 0.8% figure and the 58% and 42% split |
| Oskar, Product Manager, Mobile | No preference recorded | No preference between the three options is recorded |
| Joana, Engineering Manager, Sync | Decision owner, not deciding in the thread | B has the most support, and the decision is due 2026-10-09 |

Joana wrote that B has the most support, but the team does not yet know the mobile storage cost or how often the merge falls back to a copy.

Tomasz runs a two-week spike on B against a sample of real August conflicts, with Saskia's formatting fallback in it. The spike also writes down what A would take as a first step. Joana decides on 2026-10-09, and C stays on the list, unsized.

### Open questions

* * *

*   Mobile storage cost of keeping a base version for each edited block
*   How often the three-way merge falls back to a conflict copy
*   Whether Option B needs a new protocol version
*   How a v3 client handles the new message type that Option A adds
*   How Option C handles formatted text
*   How much of the problem Option A covers in tickets, since Yara's split counts sessions
*   Size of Option C, since two quarters is an early estimate
*   The options document and the `Sync / Conflict copy` frame, named in the thread but not supplied

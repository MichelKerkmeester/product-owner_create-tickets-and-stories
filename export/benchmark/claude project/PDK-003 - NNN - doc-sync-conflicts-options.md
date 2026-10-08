# Sync conflicts and lost edits: options for v3 and after

* * *

> Status: Proposal, decision not made — Options A, B and C are candidates for sync protocol v3 and later. Joana, Engineering Manager, Sync, decides on 2026-10-09. Until then v3 stays as it is. The sources end on 2026-09-22.

* * *

## Overview

* * *

This document sets out three candidate fixes for lost edits: field-level last-writer-wins, a three-way merge with conflict copies and a CRDT for block text. It is for the Sync and Mobile engineers and the Support lead, to read before Joana makes the call on 2026-10-09. Nothing is decided.

It covers how v3 behaves today and where people in the #sync-eng thread landed, with the cost and trade-offs of each option. It leaves out offline mode plans. The thread is the source for the options and positions. The Loomlist product context page, updated 2026-09-22, is background on v3.

### Current behavior in v3

* * *

Protocol v3 is block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other, and the replaced version is never written anywhere. Page history keeps only what reached the server, so a lost edit cannot be restored.

**How often:** Yara's figures cover the 30 days to 2026-09-14. 0.8% of sync sessions that upload edits overwrote a block another device had changed since this device last pulled. Not every overwrite was an edit someone missed, and phones are over-represented because they sync less often in the background. The query behind these figures is not in the sources.

**Member message:** Support tells members that edits made on two devices at the same time can overwrite each other. That stays the message until the decision.

## Options

* * *

### Option A: field-level last-writer-wins

* * *

**Change:** Split a block into fields (text, checked state, due date, assignee and reminder) and apply last-writer-wins to each field. A to-do checked off on a phone while its text is renamed on a laptop keeps both edits. Two edits to the same text still lose one.

**Cost:** About 3 weeks of server work for a new message type, plus a client update. The change fits inside v3. The thread gives no size for the client update.

**Coverage:** On Yara's split, 58% of overwrite sessions changed only a to-do's checkbox, due date or assignee, so A covers a bit over half. The split does not name reminders, so where reminder changes fall is unknown.

**Trade-off:** It is the cheapest change, and Tomasz calls it the fix for the to-do half of the tickets. The 42% of overwrites that changed text stay as they are.

### Option B: three-way merge on block text

* * *

**Change:** The device sends the version it started from, which is the base. Sync-service merges both edits against that base. Where the merge cannot place both, it keeps the later edit in place and inserts the other as a copy directly below it.

**Copy:** The copy is labelled `Conflicting edit from {device name}`, using the name the member gave the device in settings, such as Work laptop. Selin's mock is in the frame `Sync / Conflict copy`.

**Cost:** Roughly 6 to 8 weeks. Clients must keep the base version, which v3 clients do not, so the change needs a release on every platform. Saskia flags the storage a base version takes for each edited block on mobile, and Joana notes that this cost is not yet known.

**Fallback:** Saskia asked that any block with formatting go straight to the conflict copy, and Tomasz backs B only with that condition. Rich text merges are where bugs hide, such as bold across a merged boundary or a mention split in half.

**Trade-off:** The copy is visible, and Selin judges a silently merged paragraph that reads wrong to be the worse outcome. The thread does not say how often a merge falls back to a copy, which is the number the spike is meant to produce. Marta estimates 33 of the 40 August tickets would have ended with both texts on the page. That is her reading of the tickets, not a test.

### Option C: CRDT for block text

* * *

**Change:** Concurrent text edits always merge, so there is never a conflict copy.

**Cost:** It needs protocol v4 and a migration of every page and every client. Tomasz's rough estimate is two quarters. Joana notes that nobody sizes it now, and it stays on the list as the long-term option. Changing the protocol needs every client on a version that speaks it, per the product context page.

**Trade-off:** It removes the conflict copy for text, and with it the fallback question. The thread does not say how C handles formatted text, which is the case Saskia raised for B.

### Comparison

* * *

| | Option A | Option B | Option C |
| --- | --- | --- | --- |
| Change | Field-level last-writer-wins | Three-way merge on block text | CRDT for block text |
| Cost in the thread | About 3 weeks of server work, plus a client update | Roughly 6 to 8 weeks | About two quarters, rough estimate, not sized |
| Protocol | Stays in v3 | Not stated in the thread | Protocol v4 |
| Client work | Client update, size not given | Release on every platform | Every client migrated |
| Covers | Edits to different fields of a block | Text edits the merge can place, with a copy for the rest | All concurrent text edits, with no copy |
| Main trade-off | Same-text edits still lose one | Mobile storage, and the fallback rate is unknown | Largest migration, formatted text not covered in the thread |

## Where people landed

* * *

**Marta, Support Lead:** Backs B and asks what to tell members and what to change.

**Tomasz, Backend Engineer, Sync:** Leans B, but only with Saskia's formatting fallback. He calls A the cheapest change for the to-do half of the tickets.

**Selin, Product Designer, Sync:** Prefers B because it is the option she can explain to members. A visible copy beats a silent merge that reads wrong.

**Saskia, iOS Engineer:** Worried about B on mobile because of base-version storage and rich text merge bugs. Her formatting fallback is the condition the thread attaches to B.

**Yara, Data Lead:** Reported the figures behind the options: the 0.8% overwrite rate and the 58% and 42% split. She takes no position on the options.

**Joana, Engineering Manager, Sync:** Is not deciding in the thread. She notes that B has the most support but that mobile storage and fallback frequency are unknown. Tomasz runs a two-week spike on B with Saskia's fallback, and C stays listed but unsized.

Across the thread, B has the most support, and Tomasz and Saskia both tie it to the formatting fallback. The thread treats A as the cheapest first step and does not say whether A and B could ship in sequence.

## Open questions

* * *

None of these has an answer in the sources, and each one bears on the call. The fallback rate, the storage figure and the spike matter most for B. The others sit under A, the timeline and the member message.

*   [] **Measure how often a merge falls back to a copy**
*   [] **Size base-version storage on mobile**
*   [] **Confirm whether the B estimate includes platform releases**
*   [] **Size the client update in Option A**
*   [] **Check where reminder changes fall in Yara's split**
*   [] **Decide whether A ships before B or instead of it**
*   [] **Agree what members are told before the decision**

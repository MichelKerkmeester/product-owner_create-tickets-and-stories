```markdown
# Sync conflicts and lost edits: options for the 2026-10-09 decision

* * *
> **Status: Proposal — not decided, Joana decides on 2026-10-09**
> This document sets out candidate changes to how sync-service handles conflicts. None of them is current behavior or approved direction. Joana, Engineering Manager, Sync, owns the decision and will make it on 2026-10-09.
* * *

## Overview
* * *

Joana decides on 2026-10-09 what sync-service should do when two devices change the same block. Under protocol v3, one of the two edits is lost for good. Support tickets about this rose from 22 in July to 40 in August. This document sets out the three options from the #sync-eng thread, with their cost, their trade-offs and each person's position in the thread. It is written for the Sync and Mobile engineers and the Support lead to read before the call is made.
* * *

### Current state
* * *

**Status: Current behavior — protocol v3, per the #sync-eng thread and the Loomlist context page**

Protocol v3 applies last-writer-wins at the block level. Suppose two devices change the same block between their sync sessions. The version that reaches sync-service last replaces the other one, and the replaced version is never saved anywhere. Page history only keeps what reached sync-service, so Support has nothing to restore. v3 cannot merge edits or create a conflict copy. Changing the protocol requires every client to run a version that supports the new one.

Support closed August with 40 tickets tagged `lost-edit`, up from 22 in July. Nearly all of them follow the same pattern. A member edits a page on their phone on the train and edits it again on the laptop at the office, and the phone edit is gone.

In the 30 days before 2026-09-14, 0.8% of sync sessions that uploaded edits overwrote a block that another device had changed since this device last pulled. Not every one of these is an edit someone noticed was missing, but each one replaced someone's version of a block. Pages edited on phones show up more often than their share, because phones sync less often in the background. Of those sessions, 58% changed only a to-do's checkbox, due date or assignee. The other 42% changed text.

Today Support tells members that edits made on two devices at the same time can overwrite each other.
* * *

### Desired outcome
* * *

When two devices change the same block, an edit should never disappear without a trace. Either both edits end up in the block, or the member can see the edit that lost and act on it. The thread sets no target for the conflict rate or the number of `lost-edit` tickets.
* * *

### Principles and constraints
* * *

*   **A visible copy is better than a silent bad merge** — Selin's design position. A merged paragraph that reads wrong is worse than a conflict copy the member can see
*   **Protocol changes reach members through client releases** — every client has to run a version that supports the new protocol. iOS and Android ship every two weeks and roll out over 7 days. Desktop runs the web client, so a web change reaches Desktop without a Desktop release
*   **Edits already lost stay lost** — v3 never saved the replaced version, so none of the options can bring back edits lost before the change
* * *

## Options
* * *

### Option A, field-level last-writer-wins
* * *

Option A splits a block into separate fields and applies last-writer-wins to each field instead of to the whole block. This fixes conflicts where two devices change different fields of the same to-do. It does not fix two edits to the same text.

*   **Candidate behavior or design** — a block splits into text, checked state, due date, assignee and reminder, and last-writer-wins applies to each field separately. If a member checks off a to-do on the phone and renames it on the laptop, both changes are kept
*   **What it does not fix** — two edits to the same text still lose one
*   **Coverage** — 58% of the overwriting sessions changed only a to-do's checkbox, due date or assignee. In Yara's words, Option A alone "covers a bit over half"
*   **Cost** — about 3 weeks of server work plus a client update. It fits inside v3 with a new message type. This is Tomasz's estimate
*   **Status** — Proposed. Tomasz is writing up what A would take as a first step
* * *

### Option B, three-way merge on block text
* * *

Option B merges two text edits against the version both devices started from. When the merge cannot place both edits, the losing edit stays visible as a labelled copy instead of disappearing.

*   **Candidate behavior or design** — the device sends the version it started from, and sync-service merges both edits against that base. When the merge cannot place both edits, the server keeps the later edit in place and inserts the other one as a copy of the block directly below it
*   **Conflict copy label** — `Conflicting edit from {device name}`, using the name the member gave the device in settings, such as Work laptop. The design is mocked in the frame `Sync / Conflict copy`
*   **Formatting fallback** — Saskia's condition: any block with formatting skips the merge and goes straight to the conflict copy. Tomasz supports B only with this fallback
*   **Coverage** — Marta's estimate from going back through August is that 33 of the 40 tickets would have ended with both texts on the page
*   **Cost** — roughly 6 to 8 weeks. Clients must keep the base version, which v3 clients do not, so B needs a release on every platform. This is Tomasz's estimate
*   **Risks** — keeping a base version for every edited block costs storage on mobile. Rich text merges are where bugs hide, such as bold running across a merged boundary or a mention split in half
*   **Status** — Proposed. A two-week spike is running
* * *

### Option C, a CRDT for block text
* * *

Option C replaces block text with a CRDT, a data type that merges concurrent edits automatically. Concurrent text edits then always merge and a conflict copy is never needed. It is the largest change of the three.

*   **Candidate behavior or design** — concurrent text edits always merge, and there is never a conflict copy
*   **Cost** — about two quarters. It needs protocol v4 and a migration of every page and every client. This is Tomasz's estimate
*   **Status** — On the list as the long-term option. Nobody is sizing it now
* * *

### Options and trade-offs
* * *

| Option | What it keeps | Cost (Tomasz's estimate) | Main risk or gap | Status |
| ---| ---| ---| ---| --- |
| A, field-level last-writer-wins | Both edits when they touch different fields of a block | About 3 weeks of server work plus a client update, inside v3 | Two edits to the same text still lose one. Covers a bit over half of the overwriting sessions | Proposed, first-step write-up in progress |
| B, three-way merge on block text | Both text edits when the merge can place them, otherwise the later edit plus a labelled copy | Roughly 6 to 8 weeks, release on every platform | Base-version storage on mobile and fallback rate both unknown. Rich text merge bugs | Proposed, spike running |
| C, CRDT for block text | Both text edits, always merged, never a copy | About two quarters, protocol v4 and a full migration | Largest cost of the three, not sized | Long-term option, not sized now |
* * *

### Where people in the thread landed
* * *

| Person | Role | Position | Reason given |
| ---| ---| ---| --- |
| Selin | Product Designer, Sync | B | The option she can explain to people. A visible copy is better than a silently merged paragraph that reads wrong |
| Marta | Support Lead | B | Estimates that 33 of the 40 August tickets would have ended with both texts on the page |
| Tomasz | Backend Engineer, Sync | Leans B, but only with Saskia's fallback | A is the cheapest change that fixes the to-do half of the tickets |
| Saskia | iOS Engineer | Worried about B. If B goes ahead, formatted blocks go straight to the conflict copy | Storage cost of keeping a base version for every edited block, plus rich text merge bugs |
| Yara | Data Lead | No position stated | Supplied the 0.8% session rate and the 58% and 42% split |
| Joana | Engineering Manager, Sync | Not deciding in the thread | B has the most support, but its mobile storage cost and how often it falls back to a copy are unknown |
* * *

## Recommendation or decision
* * *

No decision has been made and this document makes no recommendation. Joana decides on 2026-10-09. B has the most support in the thread. Joana named two unknowns the spike has to answer first: what B costs in storage on mobile and how often the merge falls back to a conflict copy.
* * *

### Interim plan until 2026-10-09
* * *

**Status: Approved direction — set by Joana on 2026-09-22, in place until the decision**

*   Tomasz runs a two-week spike on Option B against a sample of real August conflicts, with Saskia's formatting fallback included
*   Tomasz writes down what Option A would take as a first step
*   Option C stays on the list as the long-term option and nobody sizes it now
*   v3 stays as it is
*   Support keeps telling members that edits made on two devices at the same time can overwrite each other
* * *

### Dependencies and risks
* * *

*   **Spike results** — the decision depends on the spike measuring B's mobile storage cost and its fallback rate. There are no results yet
*   **Rich text merges** — bold running across a merged boundary or a mention split in half are the known failure cases. The formatting fallback avoids them by skipping the merge
*   **To-do fields under B** — the thread describes B as a merge on block text only. It does not say how B handles a to-do's checkbox, due date or assignee, which are the fields in 58% of the overwriting sessions
* * *

## Open decisions
* * *

*   [ ] **Choose A, B or C, or A as a first step.** Joana decides on 2026-10-09
*   [ ] **Measure the base-version storage cost on mobile.** This is part of Tomasz's spike on B
*   [ ] **Measure how often the merge falls back to a conflict copy.** This is part of Tomasz's spike on B
*   [ ] **Confirm that formatted blocks go straight to the conflict copy.** This is Saskia's condition for B, and Tomasz supports it
*   [ ] **Settle how B handles to-do field changes.** The thread does not cover it
*   [ ] **Agree what Support tells members after the decision.** Marta raised this, and the thread names no owner
* * *

### Out of scope
* * *

*   Offline editing plans, including their effect on the conflict rate
*   Sizing Option C
* * *

### Source basis
* * *

*   [#sync-eng thread export, 2026-09-14 to 2026-09-22](context/loomlist-sync-conflict-thread.md) — governs current behavior, the options, each person's position and the interim plan
*   [Loomlist product context, updated 2026-09-22](context/loomlist-context.md) — background on how v3 works today and on the client release cadence
*   **`Sync conflicts, options for v3 and after` and the frame `Sync / Conflict copy`** — mentioned in the thread but not supplied. The options are described only as the thread describes them
```

Export-equivalent path: `export/002 - doc-sync-conflicts-options-proposal.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the `—` in the `*   **Term** — definition` bullets and the two `Status: {class} — {qualifier}` labels, which the format requires.

**Quality summary:**
- **Source safety:** pass. The thread is treated as authoritative and the context doc as background. v3 is labelled current behavior, Joana's interim plan approved direction and A, B and C proposals. Effort figures are credited to Tomasz and "33 of 40" to Marta.
- **Shape fit:** pass. It's a proposal that opens with the decision, who it affects and why it matters now.
- **ClickUp layout:** pass for a file export. There are no spacer headings because you didn't say whether this goes to ClickUp.
- **Readability:** pass.
- **Voice:** pass.

**What's in it:**
- **Options and positions:** all three options, with their estimated cost and trade-offs, and a table of where each person in the thread landed.
- **Neutral stance:** it makes no recommendation. It states that B has the most support and names the two unknowns Joana is waiting on from the spike.
- **Offline plans left out:** Oskar's comment isn't in the positions table, and Saskia's storage concern appears without its link to offline work.

**Things I added that aren't directly in the thread**, so you can remove any of them:
- **"To-do fields under B":** listed as a risk and an open decision. The thread describes B for block text only and never says how B handles checkbox, due date or assignee conflicts.
- **"Agree what Support tells members after the decision":** listed as an open decision. Marta asked what to tell members, and the thread doesn't answer for the period after 2026-10-09.
- **"Edits already lost stay lost":** listed as a constraint. It follows from v3 never saving the replaced version, but nobody in the thread says it.
- **The release-cadence constraint:** comes from the context doc (iOS and Android ship every two weeks, and Desktop picks up web changes without its own release).
- **The "Desired outcome" section:** I wrote this myself, and it notes that the thread sets no numeric target.
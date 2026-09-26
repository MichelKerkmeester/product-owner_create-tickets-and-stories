# Sync conflicts and lost edits: options before the 2026-10-09 decision

* * *
> **Status: Proposal — not decided**
> Three candidate sync-service conflict changes, none approved or built. Joana, Engineering Manager, Sync, decides on 2026-10-09 after a two-week spike on Option B.
* * *

## Overview
* * *
This compares options for two devices changing one block in Loomlist, with each one's cost, fix and #sync-eng support, for Sync and Mobile engineers and the Support lead.

Support tagged 40 tickets `lost-edit` in August, up from 22 in July, nearly all a phone edit lost to a later laptop edit with nothing to restore.
* * *

### Current state
* * *
Status: Current behavior — verified for sync protocol v3, per the context page and Tomasz in the thread

Protocol v3 uses block-level last-writer-wins: when two devices change one block between syncs, the later arrival replaces the other, which is never stored or kept in page history.

V3 has no merge or conflict copy, and a new protocol needs every client updated. Phone-edited pages are over-represented in conflicts, since phones sync less often in the background.
* * *

### What the numbers show
* * *
| Figure | Value | Source | Note |
| --- | --- | --- | --- |
| `lost-edit` tickets, July | 22 | Marta | |
| `lost-edit` tickets, August | 40 | Marta | Nearly all describe edits on two devices |
| Sync sessions overwriting a block another device changed since this one last pulled | 0.8% | Yara, last 30 days to 2026-09-14 | Not every one a missed edit, but each replaced someone's version |
| Of those, only a to-do's checkbox, due date or assignee changed | 58% | Yara, 2026-09-17 | |
| Of those, text changed | 42% | Yara, 2026-09-17 | |
| August tickets that would keep both texts under Option B | 33 of 40 | Marta's estimate | From rereading the August tickets |

The 0.8% counts sessions and the 33 of 40 tickets, so they should not be combined.
* * *

### Desired outcome
* * *
The shared aim: an edit on one device is never replaced without a trace by one on another.
* * *

## The three options
* * *
Status: Proposal — none approved, all three still on the table per the pinned thread summary
* * *

### Option A, field-level last-writer-wins
* * *
Option A applies last-writer-wins per field: text, checked state, due date, assignee and reminder.

*   **Protocol** — fits inside v3 with a new message type
*   **Coverage** — the to-do half, a bit over half of the 0.8% by Yara's reading of the 58%
* * *

### Option B, three-way merge on block text
* * *
Option B merges text edits against the base version each device sends. When both cannot be placed, the later edit stays and the other becomes a copy below, labelled `Conflicting edit from {device name}`.

The device name comes from settings, such as Work laptop, and Selin mocked it in the frame `Sync / Conflict copy`, not supplied here. Saskia's condition, in the spike: any formatted block skips the merge and goes straight to the copy.

*   **Clients** — v3 clients keep no base version, so every platform needs a release
*   **Coverage** — both text edits stay, merged or as a copy
*   **Unmeasured** — mobile base-version storage and the fallback rate to a copy
* * *

### Option C, a CRDT for block text
* * *
Option C uses a CRDT for block text, costed in the table below.
* * *

### Options and trade-offs
* * *
| Option | Fixes | Leaves or risks | Cost, Tomasz's estimate | Release needed | Status |
| --- | --- | --- | --- | --- | --- |
| A, field-level last-writer-wins | Concurrent changes to different fields of a block, such as a check-off and a rename | Two edits to the same text still lose one | About 3 weeks of server work plus a client update | A client update, inside v3 | Proposal |
| B, three-way merge on block text | Both text edits stay on the page | Mobile base-version storage, rich text merge bugs and an unmeasured fallback rate to copies | Roughly 6 to 8 weeks | Every platform | Proposal, in the spike |
| C, CRDT for block text | Concurrent text edits always merge, with no copy | Protocol v4 and migrating every page and client. Selin finds a silently merged paragraph that reads wrong worse than a visible copy | Two quarters | Every client, plus a page migration | Proposal, long-term, not sized |
* * *

### Where people landed
* * *
| Person | Position | Condition or concern |
| --- | --- | --- |
| Tomasz, Backend Engineer, Sync | Leans B | Only with Saskia's formatting fallback. Sees A as the cheapest fix for the to-do half |
| Selin, Product Designer, Sync | B | She can explain B to members, and a visible copy beats a silent wrong merge |
| Marta, Support Lead | B | Estimates 33 of the 40 August tickets would have kept both texts |
| Saskia, iOS Engineer | Worried about B on mobile | Base-version storage and merge bugs such as bold across a merged boundary or a split mention. If B goes ahead, formatted blocks go straight to the copy |
| Yara, Data Lead | No stated position | Supplied the 0.8% and the 58% and 42% split |
| Joana, Engineering Manager, Sync | Not deciding in the thread | B has most support, but its mobile storage cost and fallback rate are unknown |

* * *

## Decision and next steps
* * *
Status: Approved direction — interim plan set by the decision owner on 2026-09-22, not a choice between the options

No option is chosen. Joana decides on 2026-10-09, and until then the thread's plan holds:

*   Tomasz runs a two-week spike on Option B against a sample of real August conflicts, with Saskia's fallback
*   Tomasz writes down what Option A would take as a first step
*   Option C stays as the long-term option, unsized before 2026-10-09
*   Protocol v3 stays as it is
*   Support keeps warning members that simultaneous edits on two devices can overwrite
* * *

### Dependencies and risks
* * *
iOS and Android ship every two weeks and roll out over 7 days. Desktop runs the web client, so a Web change needs no Desktop release.

*   **Every-client releases** — B needs one on every platform, and C needs protocol v4 everywhere
*   **Mobile storage** — B's base versions, cost unmeasured
*   **Rich text merges** — broken formatting or a split mention, which Saskia's fallback avoids
*   **Lost edits continue** — until a change ships
* * *

## Open decisions
* * *
*   [] **Choose an option** by 2026-10-09, owned by Joana, and whether A goes first
*   [] **Measure B's mobile storage cost** in Tomasz's spike
*   [] **Measure B's fallback rate** to a copy, with the formatting fallback on
*   [] **Write down what A would take** as a first step, owned by Tomasz
*   [] **Settle how B treats to-do fields** such as checked state or due date, as the thread covers block text only
*   [] **Settle mixed-version behavior** during a rollout, when some clients keep a base version and others still run v3, which the thread does not cover
*   [] **Agree the member message** Support uses once a change ships
* * *

### Out of scope
* * *
*   Offline editing plans and their effect on the conflict rate, including input from Oskar, Product Manager, Mobile
*   Sizing Option C in this round
* * *

### Source basis
* * *
*   **`context/loomlist-sync-conflict-thread.md`** — the #sync-eng thread, 2026-09-14 to 2026-09-22, exported by Joana, governing options, figures, positions and plan
*   **`context/loomlist-context.md`** — protocol v3 today, kept by Elif, Product Operations, updated 2026-09-22
*   **Not supplied** — Tomasz's doc `Sync conflicts, options for v3 and after` and Selin's frame `Sync / Conflict copy`, cited in the thread but not read

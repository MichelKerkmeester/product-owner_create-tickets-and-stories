````markdown
# Sync conflicts: options to replace block-level last-writer-wins

* * *
> **Status: Proposal — not decided.** Options A, B and C are candidates from the #sync-eng thread, and none of them is approved. Joana, Engineering Manager, Sync, decides on 2026-10-09. Until then, protocol v3 stays as it is.
* * *

## Overview
* * *
The decision is how sync-service should handle a conflict, which is two devices changing the same block between their sync sessions. Today protocol v3 keeps whichever version arrives last and drops the other one for good. Joana will choose between Option A, Option B and Option C on 2026-10-09.

This page is for the Sync and Mobile engineers who would build the chosen option and for Marta, Support lead, whose team answers the tickets. It sets out each option's cost, what it fixes and what it leaves, and where each person in the thread ended up. It does not recommend an option. That decision belongs to Joana.

The decision is needed now because the ticket count is rising and the lost edits can't be recovered. Support closed August with 40 tickets tagged `lost-edit`, up from 22 in July. None of those edits can be restored.

### Current state
* * *
Status: Current behavior — sync protocol v3, as described by Tomasz in the thread and by the Loomlist product context page

Protocol v3 resolves conflicts with block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other one. The replaced version is not saved anywhere. Page history keeps only what reached sync-service, so it has nothing to restore.

Nearly all of the August tickets follow the same pattern. A member edits a page on their phone on the train and then edits it again on the laptop at the office. The phone edit is gone.

Yara measured the 30 days before 2026-09-14. In that period, 0.8% of sync sessions that upload edits overwrote a block another device had changed since the uploading device last pulled. Not every one of those was an edit that someone missed, but each one replaced someone's version of a block. Pages edited on phones show up more often than their share, because phones sync less often in the background. Yara split the overwriting sessions by what changed:

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

*   **How it works** — a block is split into fields (text, checked state, due date, assignee, reminder). Last-writer-wins then applies to each field separately instead of to the whole block
*   **What it fixes** — checking off a to-do on the phone while renaming it on the laptop keeps both changes. Yara puts A's coverage at a bit over half of the overwriting sessions, which matches the 58% that changed only to-do fields
*   **What it leaves** — two edits to the same text still lose one of them. That covers the 42% of overwriting sessions that changed text
*   **Cost** — about 3 weeks of server work plus a client update. It fits inside v3 with a new message type

### Option B, three-way merge on block text
* * *
Option B keeps both text edits, either merged or as a visible copy. In exchange, every client has to store more and ship a release.

*   **How it works** — the device sends the version it started from, and sync-service merges both edits against that base. If the merge can't place both edits, the server keeps the later edit in place and inserts the other one as a copy of the block directly below it, labelled `Conflicting edit from {device name}`
*   **Conflict copy** — `{device name}` is the name the member gave the device in settings, for example Work laptop. Selin has mocked the copy in the frame `Sync / Conflict copy`
*   **What it fixes** — no text edit is dropped. Marta estimates from her own read of the tickets that 33 of the 40 August tickets would have ended with both texts on the page
*   **What it leaves** — edits the merge can't place end up as a conflict copy, which the member has to reconcile by hand
*   **Cost** — roughly 6 to 8 weeks. Clients have to keep the base version, which v3 clients don't do, so every platform needs a release
*   **Proposed condition** — Saskia wants any block with formatting to go straight to the conflict copy instead of being merged

### Option C, a CRDT for block text
* * *
Option C removes text conflicts completely. It costs the most and needs a new protocol.

*   **How it works** — concurrent text edits always merge, and there is never a conflict copy
*   **What it fixes** — no text edit is ever lost or split out into a copy
*   **Cost** — protocol v4 and a migration of every page and every client. Tomasz estimates two quarters

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

Saskia is worried about B on mobile. Keeping a base version for every edited block costs storage on the device. Rich text merges are also where bugs tend to appear, for example bold across a merged boundary or a mention split in half. Her formatting fallback is her condition for B.

Tomasz leans towards B as well, but only with Saskia's fallback. He calls A the cheapest change that fixes the to-do half of the tickets.

Joana chose not to decide in the thread. B has the most support, but she named two things that nobody knows yet: how much storage B costs on mobile and how often the merge falls back to a copy. C stays on the list as the long-term option.

Status: Approved direction — set by Joana in the thread on 2026-09-22

Tomasz is running a two-week spike on Option B against a sample of real August conflicts, with Saskia's formatting fallback included. He is also writing down what Option A would take as a first step. Nobody is sizing C now. Until the decision, v3 stays as it is, and Support keeps telling members that edits made on two devices at the same time can overwrite each other.

### Risks and dependencies
* * *
*   **Every client has to support the new protocol** — B needs a release on every platform and C needs every client migrated to v4. A needs a client update for its new message type
*   **Rich text merge bugs** — Saskia's examples are bold across a merged boundary and a mention split in half. Her fallback avoids them by sending formatted blocks to a copy instead
*   **Mobile storage for B** — clients would keep a base version for every edited block. The spike is meant to measure the cost
*   **To-do fields under B and C** — the thread describes B and C for block text only. It doesn't say how either one handles a conflicting checkbox, due date or assignee change

### Open decisions and pending evidence
* * *
*   [ ] **Choose between Options A, B and C.** Joana decides on 2026-10-09
*   [ ] **Measure B's storage cost on mobile.** Tomasz's spike should produce this number
*   [ ] **Measure how often B falls back to a conflict copy.** Also from the spike, on real August conflicts with the formatting fallback included
*   [ ] **Write down what Option A would take as a first step.** Tomasz owns this alongside the spike
*   [ ] **Confirm the spike's timing.** The thread gives its length as two weeks but no start date, so it isn't confirmed that results will be ready before 2026-10-09

### Out of scope
* * *
*   Offline mode plans and how each option would hold up under them
*   Sizing Option C
*   A recommendation from this page. The choice belongs to Joana

### Source basis
* * *
*   **Thread export, #sync-eng, lost edits between devices** — the governing source for the options, costs, numbers, positions and next steps. Exported by Joana on 2026-09-22
*   **Loomlist product context** — background only, for how protocol v3, page history and protocol changes work today. Kept by Elif, Product Operations
*   **`Sync conflicts, options for v3 and after`** — Tomasz's options doc. The thread mentions it, but it was not supplied
*   **`Sync / Conflict copy`** — Selin's design frame. The thread mentions it, but it was not supplied
````

Export-equivalent path: `export/002 - doc-sync-conflict-options-proposal.md`

I rewrote the status page as a proposal for the Sync and Mobile engineers and Marta. It covers all three options, with cost, what each fixes and what each leaves. It also shows where each person in the thread ended up and Joana's plan up to 2026-10-09. It recommends nothing. This version replaces 001.

**Offline mode:** everything about it is gone. That includes Oskar's points, the offline half of Saskia's storage concern, the part on offline retries I'd added in 001 and the open question about offline editing. "Out of scope" names offline mode, so readers know it was left out on purpose.

**One addition from me:** under "Risks and dependencies" I noted that the thread describes B and C for block text only. It doesn't say what happens when two devices change a to-do's checkbox, due date or assignee. The engineers may want that answered before the call. Remove it if you'd rather keep strictly to what the thread says.

**Quality summary:**
- **Source safety: pass.** The thread governs, and the context doc is used only for how v3 works today. Each section has its own status line, costs are marked as Tomasz's estimates and Marta's 33 of 40 as her own read of the tickets. The two files the thread mentions but you didn't send are marked as not supplied.
- **Shape fit: pass.** It opens with the decision, who it's for and why it's needed now. The options are clearly marked as not decided.
- **ClickUp layout: pass.** Uses ClickUp-style dividers and bullets, with sentence-case headings. There are 3 main sections out of 12 headings, and no empty spacer headings, since this is a file export.
- **Readability: pass.** Each option opens with its trade-off before the details.
- **Voice: pass.** See the self-scan below.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: em dashes only in the `*   **Term** — definition` bullets and the `Status: {class} — {qualifier}` lines, both allowed exceptions.
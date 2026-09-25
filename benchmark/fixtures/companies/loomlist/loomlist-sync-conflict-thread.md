# Thread export, #sync-eng, lost edits between devices

Exported from the #sync-eng channel in the team chat by Joana, Engineering Manager, Sync, on 2026-09-22.
Started by Marta, Support Lead, on 2026-09-14. Messages are in order, reactions left out.

---

**Marta**, Support Lead, 2026-09-14 09:12

August closed with 40 tickets tagged `lost-edit`, up from 22 in July. Nearly all tell the same story. Someone edits a page on their phone on the train and then again on the laptop at the office. The phone edit is gone. Page history does not have it either, so we cannot restore anything. Can we talk about what we tell people and what we change?

**Tomasz**, Backend Engineer, Sync, 2026-09-14 09:40

That is protocol v3 doing what it was built to do. It is block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last replaces the other, and the replaced version is never written anywhere. Page history only sees what reached the server, so it has nothing to give back.

**Yara**, Data Lead, 2026-09-14 11:05

Last 30 days: 0.8% of sync sessions that upload edits overwrite a block another device changed since this device last pulled. Not every one of those is an edit anyone missed, but each one replaced somebody's version of a block. Pages edited on phones are over-represented, since phones sync less often in the background.

**Tomasz**, 2026-09-15 10:20

Three options, written up in the doc `Sync conflicts, options for v3 and after`.

Option A, field-level last-writer-wins. We split a block into fields (text, checked state, due date, assignee, reminder) and apply last-writer-wins per field. Checking off a to-do on the phone while renaming it on the laptop keeps both. Two edits to the same text still lose one. Fits inside v3 with a new message type, about 3 weeks of server work plus a client update.

Option B, three-way merge on block text. The device sends the version it started from, and sync-service merges both edits against that base. When the merge cannot place both edits, the server keeps the later edit in place and inserts the other one as a copy of the block right below it, labelled `Conflicting edit from {device name}`. Clients have to keep the base version, which v3 clients do not, so it needs a release on every platform. Roughly 6 to 8 weeks.

Option C, a CRDT for block text. Concurrent text edits always merge and there is never a conflict copy. It needs protocol v4 and a migration of every page and every client. By my estimate that is two quarters.

**Selin**, Product Designer, Sync, 2026-09-15 14:02

From the design side Option B is the one I can explain to people. The copy is mocked in the frame `Sync / Conflict copy`, with `Conflicting edit from {device name}` using the name the member gave the device in settings, like Work laptop. A silently merged paragraph that reads wrong is worse than a visible copy.

**Marta**, 2026-09-15 15:30

+1 for B. Going back through August, I think 33 of the 40 would have ended with both texts on the page.

**Saskia**, iOS Engineer, 2026-09-16 09:10

Worried about B on mobile. Keeping a base version for every edited block costs storage, and the offline work Oskar is scoping wants a lot of pages on the device. Rich text merges are also where bugs hide, like bold across a merged boundary or a mention split in half. If we go with B, I want any block with formatting to go straight to the conflict copy.

**Tomasz**, 2026-09-16 09:45

Fair. For the record I lean B too, but only with Saskia's fallback. A is the cheapest change that fixes the to-do half of these tickets. Yara, can you split the 0.8% by what changed?

**Yara**, 2026-09-17 16:20

58% of those sessions changed only a to-do's checkbox, due date or assignee. 42% changed text. So Option A alone covers a bit over half.

**Oskar**, Product Manager, Mobile, 2026-09-18 10:05

Offline editing will push that 0.8% up a lot, because a phone that was offline for a day comes back with every edit at once. Whatever we pick has to hold up for that. I do not want to ship offline editing on top of v3 as it is today.

**Joana**, Engineering Manager, Sync, 2026-09-22 11:30

Thanks all. I am not deciding in this thread. B has the most support here, but we do not know yet what it costs in storage on mobile or how often the merge falls back to a copy.

Tomasz runs a two-week spike on B against a sample of real August conflicts, with Saskia's formatting fallback in it, and writes down what A would take as a first step. C stays on the list as the long-term option and nobody sizes it now.

I will decide on 2026-10-09. Until then v3 stays as it is, and Support keeps telling members that edits made on two devices at the same time can overwrite each other.

---

Pinned at the end of the thread:

Status: not decided
Decision owner: Joana, Engineering Manager, Sync
Decision date: 2026-10-09
On the table: Option A, Option B, Option C

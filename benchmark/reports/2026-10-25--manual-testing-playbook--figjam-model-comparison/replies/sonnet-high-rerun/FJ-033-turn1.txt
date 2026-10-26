Round 1 of 3. Nothing is written to the board yet. Here is what I have settled, then three questions.

**Settled so far**
- Reader: leadership, for an update
- Question: how does block sync work?
- Type: architecture, since you want the parts and how they connect
- Parts named: desktop, web and iOS apps, the sync platform, Apple's push service
- Target: the existing file `<test-file-key>`, as a new board section beside what it holds. A file you name needs no plan and no new file. The Loomlist Product plan and the Barter drafts fallback apply only if that file can't be opened. I read the file once before the write gate, so I can name any section that already shares the board's title.

**1. What the board must not do**
- Reading: a leadership board stays at the level of named parts.
- Question: what should it refuse to show?
- Recommended: no message order for one sync (that would be a sequence diagram), no queues, workers or replicas, and no speed or reliability claims.
- Why: extra internals or numbers you didn't give would be invented.

**2. The outcome**
- Reading: your description makes three points. All three apps share one sync platform, it stores every change, and it wakes sleeping iPhones through Apple's push service.
- Question: what should leadership be able to decide or do after reading it?
- Recommended: understand how a change made on one device reaches a sleeping iPhone, with no decision asked.
- Why: your message names no decision, so the board explains rather than proposes.

**3. Source status and names**
- Reading: your message is the only source. The architecture layout needs an entry point between the apps and the sync platform, and a store for the changes. Without names from you I would draw "Entry point" and "Change store", named by what they do and marked assumed on the source line. Apple's push service is called by the sync platform directly.
- Question: is this how sync works today, and do you have names for the entry point and the store?
- Recommended: current behavior, with the two parts drawn by capability.
- Why: a proposal would carry its status in the labels. Your wording reads as live behavior.

Reply with corrections, or say "use the recommended answers" and I'll send the full playback next.
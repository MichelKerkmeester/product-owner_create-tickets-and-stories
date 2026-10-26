I still can't draw the board, because there's no source for block sync. Your "use the recommended answers" settles questions 2 and 3, but question 1 (the source) had no default I could take without inventing services.

I spent one read call on the target file, `<draft-file-key>`, in case it held the answer. It holds three Roamstay boards: two booking-status boards and a change-booking-dates flow. None of them mentions block sync, services or sync calls. The workspace has no Barter sync doc either.

**What I've settled on the recommended answers (all assumed)**
- **Reader:** an engineer or PM who needs the parts and their calls
- **Question:** which parts take part in block sync and how do they connect?
- **Type:** architecture. I'll switch to a sequence diagram if you want the order of one sync instead
- **Scope:** one sync path, with no deployment detail, monitoring or logging, and no services that sync never touches
- **Target:** the existing file, as a new section beside the three boards already there, which I won't touch

**Still unasked**
- Reading: nothing I can read names the Barter services behind block sync.
- Question: which source should I read? That could be the sync service's doc, the repo path for its routes, handlers and consumers, or a ClickUp doc or task.
- Recommended: send the engineering doc or the repo path. Anything that names every deployable part, who calls whom and what sits outside the system will do.
- Why: an architecture board needs those three things. If I guessed a gateway, a database or a queue, the board would show a system that may not exist.

Once the source arrives, I'll read it, write the playback of what it settled, and then ask the write-gate question. Nothing is written to the file before that yes.
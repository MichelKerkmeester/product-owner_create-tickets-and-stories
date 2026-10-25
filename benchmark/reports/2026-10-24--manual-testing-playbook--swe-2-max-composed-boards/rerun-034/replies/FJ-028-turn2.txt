The check passed and the board composes, so this is the write gate. Nothing has been written.

```text
Question: which work runs when, and what holds the release?
Outcome: a reader can see the order of the offline mode work, the critical path and the release date.
First glance: Desktop and iOS integration, the critical task that holds the release.
Second glance: Sync engine and Conflict screen build, the two builds integration waits for.
Last glance: Beta, 5 percent of workspaces, and the Release milestone.
Plan: Loomlist Product, as you named it. I can't confirm which plan owns the file from here.
File: the existing FigJam file <test-file-key>. No new file is created.
Writes: one new board section, "Offline mode launch", with 3 sections, 5 tasks and 1 milestone on one axis. It has a title, a subtitle, a key and a source line, and it is drawn for a laptop.
Extensions: none.
Calls: create_session, one use_figma and one get_figjam read-back. On a Starter plan or a View or Collab seat, Figma allows six tool calls a month, so these three count against that.
Rollback: delete the one board section this write returns. I do that only after you say yes to the deletion. The file and anything else in it stay as they are.
Write it?
```

The pre-write check printed `PASSED` for the model, 6 tasks in 3 sections. The composer built it with 6 items to read back and fits in a single `use_figma` call. The board lands to the right of anything already in the file, so it covers nothing.
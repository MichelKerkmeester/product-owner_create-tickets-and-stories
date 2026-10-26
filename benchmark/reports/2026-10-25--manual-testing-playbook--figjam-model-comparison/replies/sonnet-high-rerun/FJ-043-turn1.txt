The check fails on the layout measures, as expected. It exits with status 1.

I ran `flow_check.py` on a user flow where `Start` branches into five parallel steps (`Pick one` to `Pick five`) that rejoin at `Done`. The model carried one valid green `style` line, which the check requires.

```text
  diagram 1, user flow: a rank holds 5 steps, at most 4: split the flow so a rank reads at a glance
FAILED 1 of 1 diagram(s) in model.mmd
exit status: 1
```

- **Exit status:** 1 means a rule failed. 0 would mean every diagram passed, and 2 would mean the file was unreadable.
- **Failing measure:** the rank width limit (`MAX_RANK_WIDTH = 4`, `figjam_checks/layout.py:30`). The check output has no other failures. The check's own planted fixture "a rank of five steps" expects this same message.
- **My first try:** I used an off-palette yellow fill, which added a second failure about the fill colour. I replaced it with the style guide's green pair so the only failure left is the layout one.
- **Board:** I did not write one. A failed check blocks the write, and Flow Mode needs your yes at the write gate in any case. The existing file `<draft-file-key>` is untouched, and I created no new file.
- **Cleanup:** the model was in a temp folder that I deleted. Nothing went to `export/`.

Finding: to get a board that passes, split the five-way branch so no rank holds more than four steps. For example, group two of the picks into one step. I can playback that revised model and then ask for the write gate against `<draft-file-key>`. Do you want me to?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
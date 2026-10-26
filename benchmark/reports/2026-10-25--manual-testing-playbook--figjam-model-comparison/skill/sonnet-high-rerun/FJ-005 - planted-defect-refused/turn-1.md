The check fails as expected, exit status 1, and it names all three rules.

```
  diagram 1, sequence: line 3: G carries the alias GuestApp, which the generator drops: the id is what the board shows, so make the id readable
  diagram 1, sequence: line 6: a note is dropped by the generator: draw it afterwards through the hybrid workflow
  diagram 1, sequence: participant id G is what the board shows: write a readable name of 3 to 20 characters, such as AuthServer
FAILED 1 of 1 diagram(s) in model.mmd
exit status: 1
```

I ran `python3 -I scripts/flow_check.py` on a throwaway three-message model with `participant G as GuestApp` and a `Note over G,BookingApi`. The model sat in a temporary folder outside the repo, and I deleted the folder afterwards. Nothing went to `export/`.

- **Board not written:** the check failed and no one has said yes at the write gate, so I made no write to FigJam file `<draft-file-key>` and created no new file. If you want the board, the model has to pass first: rename `G` to `GuestApp` as the id, drop the alias, and move the note to a hybrid-workflow note on top after the compose.

Finding: the check reads `G` as both a banned alias and a too-short id, so renaming it to `GuestApp` clears two of the three rules at once.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
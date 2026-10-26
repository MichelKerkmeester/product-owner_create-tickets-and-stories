The check fails on this model and names both rules. Nothing was written to FigJam or ClickUp, and nothing was saved to `export/`.

**Model checked** (`seq-alias-note.md`, in a scratch temp directory):
```
sequenceDiagram
    participant Api as "Booking API"
    participant Guest
    Guest->>Api: Book
    Note over Guest: waits
```

**Command:** `python3 -I sk-create-figjam/scripts/flow_check.py <model>`

**Output:**
```
  diagram 1, sequence: line 2: Api carries the alias "Booking API", which the generator drops: the id is what the board shows, so make the id readable
  diagram 1, sequence: line 5: a note is dropped by the generator: draw it afterwards through the hybrid workflow
FAILED 1 of 1 diagram(s) in seq-alias-note.md
```

**Exit status:** `1`. Per the script's contract, 1 means a rule failed. 0 is a pass and 2 is an unreadable file.

- **Alias rule:** it flags line 2, the `Api as "Booking API"` participant. The generator drops the alias, so the id has to be readable on its own.
- **Note rule:** it flags line 5, the `Note over Guest` line. The generator drops notes, so a note has to be added afterwards through `references/hybrid-workflow.md`.

**FigJam file:** I didn't use file key `<draft-file-key>` or create a new file. You asked for a check, not a board, and Flow Mode only writes after you say yes at its write gate. The model also fails, so it couldn't pass that gate anyway.

If you want a board, give me a model that passes. That means making the participant id readable (`BookingApi`) and moving the "waits" note to a hybrid-workflow note. I'd then write it into `<draft-file-key>` once you say yes.
# FJ-024 turn 2 transcript

**User:** Yes, that reading is right.

**Assistant:**

```
Question: which parts carry a block change from one Loomlist client to the others, and how do they connect?
Outcome: the engineering team can see where a block change is written, where it is published, and how a sleeping iOS device is woken.
First glance: Sync Service, where every block change is written and published.
Second glance: the Change Stream that carries each change on to the Push Worker.
Last glance: Apple Push, the external hop that wakes a sleeping iOS device.
Plan: Loomlist Engineering, as you named it.
File: the existing FigJam file <test-file-key>, drawn as a new board section beside what is already there.
Writes: one composed board, 9 nodes and 8 connectors in 6 lanes, with a title, a key and a source line, at the Laptop reading distance.
Extensions: none.
Calls: one use_figma to compose the board and one get_figjam to read it back.
Rollback: delete the one section the write returns, and only on a second yes. Every existing board in the file stays as it is.
Note: the file already holds nine sections named Block sync or Loomlist block sync. This write adds a tenth and replaces none of them.
```

Write it?

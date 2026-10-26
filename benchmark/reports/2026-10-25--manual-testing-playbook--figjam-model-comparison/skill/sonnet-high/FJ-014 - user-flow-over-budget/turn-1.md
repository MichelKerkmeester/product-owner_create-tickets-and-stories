The check failed on the node budget, as expected, and exited with status 1.

```
diagram 1, user flow: 10 nodes, at most 9: split the flow
diagram 1, user flow: the longest path runs 10 steps, at most 8: split the flow
FAILED 1 of 1 diagram(s) in ten-node-flow.mmd
```

**Exit status:** `1`. In `flow_check.py`, 0 means every diagram passes, 1 means a rule failed and 2 means the file was unreadable.

I ran `scripts/flow_check.py` on a straight `flowchart LR` of 10 nodes. It was a stadium start, eight screens in a row and a stadium goal. It carried the one required `style` line and nothing else. The user-flow rules cap a diagram at 9 nodes (`references/types/user-flow.md` Section 3), so the node count tripped the budget. The same chain also tripped a second rule, a longest path of 10 steps against a maximum of 8.

No board was written, so nothing went to `<draft-file-key>` and no new file was created. Nothing has passed the check, and the write gate hasn't opened. The test model lived in a temporary folder that I deleted afterwards. Nothing was saved to `export/`.

Flow Mode splits an over-budget flow into two diagrams, with a named hand-off between them. I can split this one and re-run the check. The board write into that file would still wait for your yes at the gate.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
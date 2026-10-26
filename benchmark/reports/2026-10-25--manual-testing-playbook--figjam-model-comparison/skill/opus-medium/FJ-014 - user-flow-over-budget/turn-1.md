The check failed on the node budget, as expected, so nothing was written to FigJam.

**Model checked:** a straight left-to-right user flow with 10 nodes: `Open app → Home → Search → Results → Detail → Cart → Address → Payment → Review order → Order placed`. It has one `style` line on the goal, no decisions and no zones. I saved it in a temporary folder outside the repo, ran `python3 scripts/flow_check.py` on it, then deleted the folder. Nothing is left in `export/` or the repository.

**Output:**
```
  diagram 1, user flow: 10 nodes, at most 9: split the flow
  diagram 1, user flow: the longest path runs 10 steps, at most 8: split the flow
FAILED 1 of 1 diagram(s) in model.md
```

**Exit status:** `1`, which the script defines as "a rule fails" (0 means pass, 2 means unreadable).

The first line is the node budget rule from `references/types/user-flow.md`: a user flow can have at most 9 nodes. The second line is a separate length limit that a straight flow of 10 trips at the same time: the longest path can run at most 8 steps.

**Board:** I did not write to FigJam file `<test-file-key>` and did not create a new file. Flow Mode writes nothing until every diagram passes the check, and it also needs your yes at the write gate. To get a board, the flow has to be split into two diagrams that hand off through a matching end and start label, in that same file.

Do you want me to split it into two diagrams that pass, and write them to `<test-file-key>` once you approve?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
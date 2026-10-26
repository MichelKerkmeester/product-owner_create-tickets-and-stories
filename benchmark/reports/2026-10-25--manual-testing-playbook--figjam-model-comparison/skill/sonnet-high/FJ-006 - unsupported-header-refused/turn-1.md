The check fails on the pie model as expected, and it points at the type table. Exit status is **1**.

I ran `scripts/flow_check.py` on a three-slice pie block ("Signup sources": Search 40, Referral 35, Social 25). The model sat in a scratch folder outside the repo, which I deleted afterwards.

```
  diagram 1, unknown: a pie block: Flow Mode does not draw it, see references/flow-mode.md Section 3
FAILED 1 of 1 diagram(s) in model.md
exit status: 1
```

- **Exit code:** per the script's usage text, 0 means every diagram passes, 1 means a rule failed and 2 means the file was unreadable. The 1 here is a rule failure, not an unreadable file.
- **Pointer:** the message cites `references/flow-mode.md` Section 3, "PICK THE DIAGRAM TYPE". That section holds the type table and a "What Flow Mode does not draw" sub-table, which lists "Pie, mindmap, Venn, quadrant" with the nearest drawable type "None. Offer a table or a list in a Doc".
- **Board write:** I wrote nothing to FigJam. The check blocks before the write gate, so file `<draft-file-key>` was not touched and no new file was created.
- **Cleanup:** nothing was saved to `export/`, and the scratch model is gone.
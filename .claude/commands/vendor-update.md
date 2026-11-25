---
description: Update every vendored skill from the public Skilled repository and run the gates
argument-hint: "[--package NAME] [--ref REF]"
allowed-tools: Bash, Read
version: 1.0.0.0
---

# Vendor update

Run this from the repository root:

```bash
bash scripts/update-vendored.sh $ARGUMENTS
```

The script syncs every entry of `vendor.json` with upstream, prints any rebuild
line again under a heading, then runs `bash benchmark/gates/run_gates.sh`.

Then:

1. Run every `rebuild:` line the script printed, in the folder it names. A stale
   build is the one failure the gates cannot see.
2. Read the gate summary line at the end of the output. A failing gate prints its
   own output under its name.
3. Report three things:
   - what moved: each entry the sync pulled, with its file count and commit
   - what failed: any refused entry, any rebuild that failed, any red gate
   - what to commit: the pulled files together with `vendor.json`, and the
     changelog material the commit subjects give

Do not commit anything yourself. Name the files and leave the commit to the user.

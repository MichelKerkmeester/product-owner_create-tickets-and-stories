The check fails on a layout measure, as expected, and exits with status 1.

I ran `sk-create-figjam/scripts/flow_check.py` on a user flow. The start node branches into five parallel steps: choose a plan, add a payment method, verify the email, set up the profile and invite a teammate. All five rejoin at one done node.

```text
  diagram 1, user flow: a rank holds 5 steps, at most 4: split the flow so a rank reads at a glance
FAILED 1 of 1 diagram(s) in model.md
exit status: 1
```

- **Cause:** `MAX_RANK_WIDTH` in `figjam_checks/layout.py` is 4, and the five-way split puts 5 steps in one rank. That is the only rule that fired. The other layout measures passed: longest path, crossings, label length and connectors per step.
- **Write gate:** the packet writes nothing until every diagram passes, so no board was written and `<draft-file-key>` is untouched. No new file was created either, so the Barter team plan and drafts instruction did not come into play.
- **Cleanup:** I ran the model from a scratch folder outside the repo and deleted it afterwards. Nothing was saved to `export/`.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Do you want me to split the five steps into two ranks, re-run the check and then ask for your yes to write the board into `<draft-file-key>`?
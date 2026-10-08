```markdown
# BE - SHIP - Label webhook fix

I'll create the task. Before drafting, I need the decisions below in one response.

**Format & scope:** Confirm one standalone BE task covering all five points, with no subtasks and the title above. If the alerting in point 5 belongs to another owner, name the owner and I will leave that point out.

**Source:** The notes cite carrier guide 3.2, which is not in context. Attach the guide, or confirm the notes are the source for the carrier values.

**Failure path:** The thread covers recreating a shipment only for `SERVICE_UNAVAILABLE`. Should `ADDRESS_INVALID` and `OTHER` keep their current handling?

**Open carrier question:** The carrier has not confirmed whether `label.created` can follow `label.failed` for the same shipment. Should the guard handle that case now, or wait for the carrier's answer?

**Stragglers:** The 10-minute GET returns a fresh `label_url` that expires after 24 hours. Should the GET path copy the label into our own storage, as the webhook path does?

**Signature:** Is the `X-Carrier-Signature` check, with `401` on mismatch against the raw body, part of this task?

**Acceptance:** Are the thread's values the acceptance conditions: a `2xx` inside `5 seconds`, `event_id` kept for `7 days`, a GET after `10 minutes`, an alert after `30 minutes` and paging when more than 5 are stuck? Name any further test you need.

**Polling:** Polling stays out, as the thread rejected it. Confirm that the 10-minute GET is one read per straggler, with no polling loop.

**Out of scope:** Confirm these stay out: the 37 duplicate labels already billed, the 12 late orders already sent late and any repair of shipments stuck before the fix. Name any you want in.
```

Export-equivalent path: `export/NNN - task-label-webhook-fix-clarification.md`

I read the three context files and the Task Mode guidance. `$t` asks its one question before any draft, so nothing is drafted yet. Three answers shape the design: how the guard treats the failure codes, whether the carrier's open question on `label.created` after `label.failed` is settled, and who owns the alerting. Once you answer, the task follows as the next number in the task lane.

Quality status: not applicable, no artifact drafted.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
**Deliverable Block**

```markdown
# Diagnosing and requeueing a failed notification retry

* * *
> **Status: Current behavior — verified for the notification retry pipeline.** This guide reflects the retry mechanics as supplied in the governing engineering notes.
* * *

## Overview
* * *

A failed notification does not wait quietly: its retries run on a 30 second backoff, attempt six moves it to the failed queue, and support recovers it from there with the Requeue action. This guide shows a support agent how to tell a notification that is still retrying from one that has exhausted its attempts, and how to requeue the failed one without expecting the requeue to fix the underlying cause.
* * *

###   

### Before you start
* * *

*   **Required context** — You need to reach the failed queue, where support requeues with the Requeue action
* * *
##   

## Process
* * *

### 1. Confirm the notification exhausted its retries
* * *

A retry runs on a 30 second backoff for five attempts. While those attempts are still running, the notification is inside the retry cycle and needs no support action. Attempt six moves the notification to the failed queue, so a notification you find there has used all five attempts and is ready to be requeued.

*   **Retry window** — Five attempts, each 30 seconds after the previous one
*   **Failed state** — Attempt six moves the notification to the failed queue. What you find there has exhausted its retries
* * *

### 2. Requeue from the failed queue
* * *

Find the failed notification in the failed queue and use its Requeue action. If delivery keeps failing after the requeue, attempt six moves the notification back to the failed queue, so requeueing recovers it rather than repairing what made it fail.

*   **Requeue action** — Available to support from the failed queue
*   **Effect** — A requeued notification restarts the 30 second backoff, which means a fresh run of five attempts
* * *

### Quality checks
* * *

*   [ ] Does the notification sit in the failed queue rather than inside the retry window?
*   [ ] After the Requeue action, has the notification left the failed queue and restarted its 30 second backoff?
* * *

### Boundaries and exceptions
* * *

*   **Initial failure cause** — The notes cover the retry schedule and recovery, not why the first delivery fails. Diagnosing that cause is outside this guide
*   **Requeue limits** — The notes do not state whether the same notification can be requeued more than once. Do not assume a cap either way
*   **Surfaces and permissions** — The notes do not describe which screens or permissions surface the failed queue and the Requeue action
```

---

Export-equivalent path: `export/002 - doc-notification-retry-requeue-guide.md`

Quality summary:

- Source safety: pass — every claim traces to the notes, classified as current behavior, no conflicts to resolve
- Shape fit: pass — Guide, because a support agent follows an ordered diagnose-then-requeue process
- ClickUp layout: pass — `* * *` dividers, `*   ` bullets, sentence-case headings, spacer headings retained as the ClickUp-paste affordance
- Readability: pass — takeaway-first paragraphs, the one caveat that prevents a wrong expectation kept in step 2
- Voice: pass — 0 hard blockers

The guide covers exactly what the notes support: the 30 second backoff, five attempts, the failed queue at attempt six, the Requeue action and the restart it triggers. What the notes do not cover, the failure cause, any cap on repeat requeues, and the screens that surface the failed queue, sits in Boundaries and exceptions rather than being invented. One assumption you can correct: whether the initial delivery counts as attempt one is not stated in the notes, so the guide mirrors the notes' own counting, five attempts on the backoff with attempt six as the move to the failed queue.

HVR self-scan: 0 hard blockers. Fixed: none, the draft carried no banned term into the final copy. Kept with reason: definition-bullet em dashes (Doc Mode exemption), the question-form checklist items (template pattern), "Requeue" capitalized as a literal identifier, and "30 second" in the source's own notation.
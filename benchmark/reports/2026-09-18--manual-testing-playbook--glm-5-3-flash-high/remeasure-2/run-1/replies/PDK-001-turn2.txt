**Deliverable Block** — new Doc, Guide shape, support agents

```markdown
# Notification retry troubleshooting

* * *
> **Status: Current behavior — verified for the notification retry pipeline.** Sourced from engineering notes, designated authoritative for this document
* * *

## Overview
* * *
This guide shows support agents how to diagnose a notification whose retries have failed and how to requeue it. You need access to the failed queue, because that is where you use the Requeue action. A notification reaches the failed queue when its retry cycle ends, and it stays there until you requeue it.
* * *

### How the retry behaves
* * *
When a notification fails, its retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue.

A notification that starts failing takes at least two and a half minutes to reach the failed queue, because five 30 second waits separate the first failure from attempt six. Until attempt six, the notification is inside its retry cycle and not in the failed queue.
* * *

## Process
* * *
### 1. Check the failed queue
* * *
Open the failed queue and find the notification. Its presence there is the diagnosis: the notification reached attempt six, so its five 30 second retries are spent. If you do not see it, the notification is either still inside its retry cycle or it has already succeeded.
* * *

### 2. Requeue the notification
* * *
With the notification in view, use the **Requeue** action. A requeued notification restarts the backoff, so the 30 second waits and the five attempts run again. If the attempts keep failing, attempt six moves the notification back to the failed queue, and you can requeue it again.
* * *

### Quality checks
* * *
*   [ ] You confirmed the retries were spent before you requeued the notification
*   [ ] After the Requeue action, the notification is no longer in the failed queue
* * *

### Boundaries and exceptions
* * *
*   **Failure causes** — the supplied notes do not say why attempts fail, so this guide diagnoses the state, not the cause
*   **Repeated failures** — the supplied notes state no limit on how many times the same notification can be requeued
*   **Success behavior** — what happens when an attempt succeeds is not covered by the supplied notes
```

---

Export-equivalent path: `export/002 - doc-notification-retry-troubleshooting.md`

Source safety: pass — one authoritative source, every claim traced to it, the two derived facts (the 2.5 minute wait, the missing-from-queue cases) kept as hedged readings, and the undocumented success side marked out of scope rather than invented. Shape fit: pass — you stated Guide, so the mechanics come first and the diagnose-then-requeue steps follow. ClickUp layout: pass — `* * *` after every non-title heading, `*   ` bullets, no spacer headings in the export, sentence case throughout. Readability: pass — takeaway-first paragraphs, one caveat kept for each action that could go wrong. Voice: pass.

The guide covers the mechanics (30 second backoff, five attempts, attempt six into the failed queue, Requeue restarts the backoff), the diagnosis, the requeue step, and three honest boundaries: failure causes, requeue limits and success behavior are not in the notes, so none of them is invented. Two readings you can still correct: I computed the 2.5 minutes as five 30 second waits ahead of attempt six whichever attempt the count starts from, so it is written as "at least", and I treated only the requeue as the way a failed notification starts retrying again because the notes name no other. Tell me if either clashes with the real pipeline and I will revise in place. There is no ClickUp connector in this conversation, so there is nothing to offer there.

HVR self-scan: 0 hard blockers. Fixed: the step 2 heading echo, cut to the continuity lead. Kept with reason: the em dash in the status label and the three definition bullets (sanctioned ClickUp and Human Voice exemptions), the unhyphenated `30 second` and the capitalized sentence-initial `Attempt six` (preserved source wording), and the capitalized `Requeue` (preserved action identifier).
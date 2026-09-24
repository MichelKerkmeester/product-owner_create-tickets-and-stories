**Deliverable Block — Guide, Doc Mode (create, current behavior)**

````markdown
<!-- Doc Mode. Template: Guide v0.100. Source: engineering notes, designated authoritative. Quality: pass -->

# Requeue a failed notification retry

* * *
> **Status: Current behavior — verified against the engineering notes for the notification retry pipeline.** The notes are the governing source for every claim in this guide.
* * *

## Overview
* * *
This guide takes a support agent from a failed notification to a requeued retry: first confirming the notification exhausted its 30 second backoff attempts, then requeueing it from the failed queue. It covers the retry schedule, the failed queue and the Requeue action. It does not cover why a notification fails, because the engineering notes do not cover failure causes.
* * *

### Before you start
* * *
*   **Required context** — The notification sits in the failed queue, where it lands when attempt six follows the five 30 second backoff attempts
*   **Known limitation** — The notes cover the retry schedule and the Requeue action, so this guide diagnoses by queue state and not by failure cause
* * *
## Process
* * *
### 1. Confirm the notification exhausted its retries
* * *
The retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue. That sequence is the diagnosis, because the queue tells you where the notification stands without opening anything else.

*   **Notification in the failed queue** — Its five attempts ran, attempt six followed, and the notification is waiting on a requeue
*   **Notification not in the failed queue** — It is still inside the retry window, so let attempt six run before you requeue
* * *
### 2. Requeue the notification
* * *
Support can requeue from the failed queue with the **Requeue** action. A requeued notification restarts the backoff, which means a fresh run of five attempts on the 30 second backoff. The earlier attempt count does not carry over.

**Expected result**
* * *
The notification restarts the backoff. If the new attempts also fail, attempt six returns the notification to the failed queue.
* * *
## Boundaries and exceptions
* * *
*   **Failure cause** — The notes do not say what makes a notification fail, so this guide diagnoses by queue state only
*   **Requeue limit** — The notes do not state how many times a notification can be requeued. Each requeue restarts the 30 second backoff, so every run gets its own five attempts
````

**Export-equivalent path:** `export/002 - doc-requeue-failed-notification-retry.md`

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the Status label delimiter and the bold-lead definition bullets, both sanctioned ClickUp exceptions, and the supplied notes' present-tense facts, which are preserved source claims rather than newly edited prose.`

**Quality summary**

- Source safety: pass — every claim traces to a supplied notes line or wears its status
- Shape fit: pass — Guide, the ordered diagnose-then-requeue process the purpose names
- ClickUp layout: pass — `* * *` dividers, `*   ` bullets, sentence-case headings, no spacer headings in the export
- Readability: pass — takeaway-first sections, one idea per paragraph, both bullets single sentences
- Voice: pass — no banned terms, no copula avoidance, one triad in the overview only

**Summary:** A two-step support guide: step 1 reads the failed queue as the diagnostic signal, since a notification only lands there when attempt six follows the five 30 second backoff attempts, and step 2 applies the Requeue action, which restarts the backoff with a fresh five attempts. Both failure causes and the requeue limit are unstated in the notes, so the guide flags them as boundaries instead of inventing them. Two assumptions you can correct: I read the notes' failed-queue rule as applying again after a requeue, and I read "30 second backoff" as the notes wrote it without interpreting whether the interval is fixed or expanding. If the notes say otherwise on either point, tell me and I will revise the guide in place.
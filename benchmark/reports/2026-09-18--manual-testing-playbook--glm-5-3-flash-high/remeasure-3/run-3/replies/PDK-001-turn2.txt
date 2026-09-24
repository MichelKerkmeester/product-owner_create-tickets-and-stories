All Doc gate fields are resolved: single source, your explicit authority designation, current-behavior status, Guide shape, scope fixed by the stated purpose. One source, no conflicts, so nothing blocks the draft. Here is the deliverable:

* * *

# Notification retry: diagnose and requeue

* * *
> **Status: Current behavior — the engineering notes govern every claim in this guide.** The notes cover the retry timing and the Requeue action, which is what this procedure needs
* * *

## Overview
* * *
A notification that fails its attempts ends up in the failed queue, where support can requeue it with the Requeue action. This guide covers how to tell whether a notification is still inside its attempts or already in the failed queue, and how to requeue it when it is. It is written for support agents. Use it when a customer reports a notification that did not arrive.
* * *

### Before you start
* * *
*   **Required context** — the notification must be in the failed queue before you can act, because support requeues from there with the Requeue action, and the notes give no other path
* * *

## Process
* * *

### 1. Check the failed queue
* * *
Diagnosis means locating the notification, because the notes explain the retry timing but not why a send failed. The deciding rule: the retry runs for five attempts on a 30 second backoff, and attempt six moves it to the failed queue. So your check is whether the failed queue already holds it.

*   **In the failed queue** — its five attempts are done, because attempt six is what moves a notification there, so continue with step 2
*   **Not in the failed queue** — the notification is still inside its attempts, so wait until attempt six has passed and check the failed queue again
* * *

### 2. Requeue from the failed queue
* * *
The requeue itself is one action. It restarts the 30 second backoff, so the notification gets another five attempts, and when they fail, attempt six moves the notification to the failed queue again.

*   **Requeue action** — find the notification in the failed queue and requeue it with the Requeue action
*   **If it fails again** — attempt six moves it back to the failed queue, where you requeue it the same way
* * *

### Quality checks
* * *
*   [ ] Did you confirm the notification was in the failed queue, not still inside its attempts, before you acted?
*   [ ] If it was not there yet, did you wait for attempt six and check the failed queue again?
*   [ ] Did you requeue the notification with the Requeue action?
*   [ ] Did the notification restart the 30 second backoff and leave the failed queue?
* * *

### Boundaries and exceptions
* * *
*   **Still inside its attempts** — the notification needs no action from support until attempt six moves it to the failed queue
*   **Delivered or failed** — the notes do not explain how to tell a delivered notification from one still inside its attempts, so a notification that is missing from the failed queue can be either
*   **Timing expectations** — the notes give the 30 second backoff and no overall duration, so do not promise a customer an exact countdown
*   **Repeat requeues** — the notes set no limit, and each requeue restarts the 30 second backoff for another five attempts

* * *

**Export-equivalent path:** `export/002 - doc-notification-retry-pipeline-guide.md`

**Quality:**
- Source safety: pass. Single source, your explicit designation, every claim classified current behavior, no conflicts to resolve
- Shape fit: pass. Guide, ordered as check then requeue, and the opening answers what you can do, who it is for and when to use it
- ClickUp layout: pass. Dividers after every content heading, `*   ` bullets throughout, sentence case headings, no spacer headings in the export, no bullet ends in a full stop
- Readability: pass. One idea per paragraph, takeaway first, the four quality checks and four boundaries stay short
- Voice: pass

**Assumptions you can correct:** diagnosis here means locating the notification, because the notes cover timing and the requeue path but not why a send failed. I also kept the attempt numbering exactly as the notes word it, so I did not decide whether attempt one is the initial send or the first retry, and the guide stays silent on that gap.

**Next step:** if any value reads differently from the pipeline you know, tell me which line and I will revise it.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the definition-bullet and status-label em dashes under the Doc Mode exemptions, and "Requeue" kept capitalized as the supplied action label.
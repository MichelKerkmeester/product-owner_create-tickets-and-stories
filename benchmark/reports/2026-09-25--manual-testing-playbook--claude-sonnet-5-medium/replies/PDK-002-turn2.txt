````markdown
<!-- Mode: Doc | Template: Behavior reference | Score: 27/30 -->
# Payout pause behavior reference

* * *

> **Status: Current behavior — scope limited to release timing.** Note A governs, as designated by the requester. Note B is a retired draft and does not describe how the feature works today.

* * *

## Overview

* * *

A payout pause holds a payout, and the hold ends by itself after 24 hours. Nobody has to clear it. This reference is for anyone who needs to predict when a paused payout is released.

It covers release timing only. The two source notes say nothing else about the feature, so the gaps are listed under "Not established" rather than filled in.

## Release behavior

* * *

### How a pause ends

* * *

A paused payout stays held for 24 hours and is then released automatically.

*   **Hold period** — 24 hours
*   **Release** — automatic, when the hold period ends
*   **Brand action** — not needed for release

### States and outcomes

* * *

| State | Condition | Outcome |
| --- | --- | --- |
| Paused | Less than 24 hours of hold have passed | The payout stays held |
| Paused | The 24-hour hold period has ended | The payout is released automatically |
| Released | The pause has ended | The payout is no longer held |

### Retired behavior

* * *

An earlier draft, Note B, said the pause held until the brand cleared it manually. That draft is retired. It is kept here as history so nobody mistakes it for current behavior, and it does not override the automatic release above.

## Not established

* * *

The supplied notes do not cover the points below. Treat each as unknown until a source confirms it.

*   What starts a pause, and who can start one
*   When the 24-hour period begins
*   Whether a brand or an operator can end a pause before 24 hours
*   What the brand sees while a payout is paused
*   What happens if the payout cannot be released when the hold ends
````

Export-equivalent path: `export/NNN - doc-payout-pause-behavior-reference.md`

- Source safety: pass. Your designation makes Note A current behavior and Note B retired, and both statuses are labelled beside their claims.
- Shape fit: pass. Behavior reference, chosen because you asked for one.
- ClickUp layout: pass. Spacer headings are left out because this is a file export.
- Readability: pass.
- Voice: pass.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: em dashes in the `*   **Term** — definition` bullets and the status label, both sanctioned ClickUp forms.

Assumptions you can correct:
- The audience is anyone who needs to predict when a paused payout is released. You didn't state one.
- Scope is release timing only, because the notes cover nothing else.
- Note B's claim that a brand can clear a pause is retired. I did not carry it forward as an early-release option, and that is now listed as unknown.

If you can supply sources for the gaps, such as what triggers a pause or when the 24 hours start, I can extend the reference.
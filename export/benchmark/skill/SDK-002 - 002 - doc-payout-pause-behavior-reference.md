# Payout pause behavior

* * *
> **Source basis**
> *   **Current behavior** — Note A governs and covers the release mechanism only
> *   **Retired material** — Note B, a retired draft, retained for historical context
* * *

## Overview
* * *
This reference explains how long a payout pause lasts and how it ends. Note A governs, and its verified scope is the release mechanism alone, so any question the notes do not answer stays open in this document rather than settled by assumption. It is for anyone who needs to predict when payouts resume after a pause, such as support answering a brand or product assessing an incident's blast radius.
* * *

## How the pause ends
* * *
### Automatic release after 24 hours
* * *
A payout pause is not indefinite. Once a pause is active, it holds for 24 hours, after which the payout flow releases automatically. No manual action is needed, because the release needs no trigger beyond the elapsed 24 hours.

*   **When** — a payout pause is active and 24 hours have passed since it started
*   **Then** — the pause releases automatically and payouts resume
*   **Status** — Current behavior, governed by Note A
* * *

**Example**
* * *
*   **Given** — a payout pause started at 09:00 on 3 June
*   **When** — 24 hours have passed, so it is 09:00 on 4 June
*   **Then** — the pause releases with no action from anyone
* * *

### The retired note
* * *
Note B is a retired draft. It described the pause as holding until the brand clears it manually, with no automatic release. Note A governs, so that is no longer the rule, and the note states nothing about current behavior. It is retained here so a reader who remembers the manual-clear wording knows where it came from and why this document no longer carries it.
* * *

### Boundaries and unknowns
* * *
*   **Pause trigger** — what starts a payout pause is not covered by the supplied notes
*   **Early release** — whether anyone can end a pause before 24 hours is not covered, and Note B's manual-clear rule is retired, so it does not settle this
*   **Pause effects** — what happens to payouts while the pause is active, such as queueing, is not covered by the supplied notes

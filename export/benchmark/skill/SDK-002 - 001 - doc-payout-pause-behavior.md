# Payout pause behavior reference

* * *
> **Status: Current behavior — verified for the pause duration and release only.** Every other aspect of the payout pause is unverified because the supplied notes do not cover it.
* * *

## Overview
* * *
A payout pause holds a payout for a fixed 24 hours and then releases it without anyone acting. This reference explains that timing rule for anyone who needs to predict when a paused payout moves again, such as support, product and engineering.

The rule comes from Note A, which the document owner designated as the governing source. Note B described a different release mechanism and was designated a retired draft, so it appears here only as history.

## Behavior rules
* * *
### Pause duration and release
* * *
The pause has a fixed length, so a paused payout has a known release point that needs no action from the brand.

*   **When** — A payout pause is in effect
*   **Then** — The pause holds for 24 hours, then releases automatically
*   **Why** — Not stated in the supplied notes
*   **Status** — Current behavior, per Note A

### Superseded draft
* * *
Note B described a pause that holds until the brand clears it manually. It is a retired draft and does not describe current behavior.

`Status: Retired material — retained for historical context`

*   **Retired claim** — The pause holds until the brand clears it manually
*   **Effect on this reference** — The manual-clear rule is not a current release condition and must not be read as one

### Boundaries and exceptions
* * *
The notes cover the release timing and nothing else, so the items below are unknown and stay out of the settled rules.

*   **Manual clearing today** — Whether the brand or anyone else can end a pause before the 24 hours elapse is not stated
*   **Pause trigger and actor** — What starts a pause and who can start it are not stated
*   **Scope of the hold** — Which payouts a pause holds, and what the brand and the creator see during it, are not stated
*   **Start of the 24 hours** — The event that starts the 24-hour count is not stated
*   **Repeat pauses** — Whether a released payout can be paused again is not stated

### Sources
* * *
*   **Note A** — Supplied note, designated as governing by the document owner, source of the current release rule
*   **Note B** — Supplied note, designated by the document owner as a retired draft, kept for historical context only

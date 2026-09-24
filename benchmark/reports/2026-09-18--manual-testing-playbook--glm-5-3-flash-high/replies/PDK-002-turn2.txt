Note A wins on your designation, Note B drops to retired material, and the draft is safe to compose. Here is the behavior reference.

```markdown
# Payout pause behavior

* * *
> **Source basis**
> *   **Current behavior** — Note A: a payout pause holds for 24 hours, then releases automatically
> *   **Retired material** — Note B, a retired draft: the pause holds until the brand clears it manually
* * *

## Overview
* * *

A payout pause holds payouts for 24 hours and then releases itself, with no manual step. This reference explains that hold and release, so you can predict when a paused payout starts moving again. Note A governs the behavior below and Note B, an earlier draft, is retained as history.

* * *
## Behavior rules
* * *

### Timing
* * *
**1. Hold**
* * *

A pause is a hold, not a cancellation. While it is active, payouts do not move.

*   **When** — A payout pause is active
*   **Then** — Payouts are held
*   **Status** — Current behavior, Note A

* * *
**2. Automatic release**
* * *

The pause ends itself at the 24 hour mark. Nobody clears it.

*   **When** — 24 hours have elapsed since the pause started
*   **Then** — The pause releases automatically and payouts are no longer held
*   **Status** — Current behavior, Note A

* * *
### Example
* * *
*   **Given** — A payout pause is active
*   **When** — 24 hours elapse
*   **Then** — The pause releases automatically and payouts are no longer held

* * *
### Retired draft rule
* * *

Note B described a manual ending. It no longer governs.

*   **Retired rule** — The pause holds until the brand clears it manually
*   **Source** — Note B, retired draft
*   **Status** — Retired material, retained for historical context and not current behavior

* * *
## Boundaries and exceptions
* * *

*   **Early release** — Note A does not say whether a pause can end before the 24 hours are up. Whether any manual release survives in current behavior is not established by the supplied sources
*   **Pause lifecycle** — The supplied notes do not say who starts a pause, how, or which payouts it covers
* * *
```

`Export-equivalent path:` `export/002 - doc-payout-pause-behavior.md`

Quality: Source safety pass — the conflict resolved by your designation, Note A current within its scope and Note B kept visible as retired. Shape fit pass — a behavior reference whose reader can predict when a pause ends. ClickUp layout pass — `* * *` dividers, `*   ` bullets, sentence-case headings, no hyphen bullets, no bullet-ending periods. Readability pass. Voice pass.

`HVR self-scan: 0 hard blockers. Fixed: always-cut modifiers. Kept with reason: definition and status-label em dashes under the Doc Mode exemption.`

The retired manual-clearance rule stays separate from the settled 24-hour rule rather than merged into it, and the two gaps Note A leaves open (early release, pause initiation) are flagged in Boundaries instead of filled. Say the word if you want either gap sourced and the reference extended.
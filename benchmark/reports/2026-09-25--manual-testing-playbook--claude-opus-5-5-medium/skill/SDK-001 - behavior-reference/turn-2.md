I've updated the behavior reference to your brief. It's now written for CS agents and the Checkout engineers, takes every rule from the Promotions rules note and uses the company context only for background. I updated the 001 file in place rather than starting a new number, because that file was my own draft from the first pass and not one of your sources. Neither context file was changed.

Path: `export/001 - doc-promotion-stacking.md`
Verified: read-back succeeded; 268 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: em dashes in the `*   **Term** — definition` bullets and the `Status: … — …` lines, which are the ClickUp and status-label formats the skill allows.

**Quality summary**
- **Sources:** pass. Every rule comes from the rules note. The unsettled cases are marked Unverified and the two-codes rule is marked Retired, so neither reads as current behavior.
- **Shape:** pass. It's a behavior reference that walks one cart line through the rules and has a precedence table.
- **ClickUp layout:** pass on my manual check. The project's format validator still isn't reachable here.
- **Readability and voice:** pass.

**What changed:**
- **Readers and scope:** the overview names CS agents and Checkout engineers and says the doc doesn't cover how promotions are set up. I took out the Admin setup lines and the facts I'd pulled from the context doc (team ownership, cart-service, where promotions display).
- **Retired two-codes rule:** it now says it's kept because CS still refunds those orders. The precedence table has a new row: refunding a two-code order splits the discount across both codes, as it did at the time.

**Things I added that aren't in the sources:**
- **Six open questions:** these are still my own analysis of cases the note doesn't settle:
  - two exclusives on one line
  - an exclusive promotion that saves less than another promotion on the same line
  - an exclusive code that reaches no line
  - an automatic promotion over 50% on its own
  - rounding at the cap
  - which price a fixed-amount code is split by
- **Banner wording:** the note on "at least €50" versus "over €50" stays. It now says the rules note decides what the order does and uses the banner text only as the copy customers see.

Strike either if you don't want it. For the open questions, Colette owns the note and can settle them.

If you'd like this in ClickUp, I can push it once you say so.
claude project/PDK-001 - 001 - doc-promotions-stacking.md | 36 | 36 | Dropped | "the cart tells the customer: "Only one code per order. Your new code has replaced the old one."" (the surface showing the message, the cart, is gone; the cut says only "with the message")
claude project/PDK-001 - 001 - doc-promotions-stacking.md | 73 | 71 | Dropped | "Paying with a gift card is a payment, not a promotion, so it comes off the total after discounts and shipping" (the only reason for the ordering is gone; "final total" itself keeps the outcome)
claude project/PDK-001 - 001 - doc-promotions-stacking.md | 134 | 130 | Dropped | "Free-shipping codes stopped on that date, and the one-code rule has covered every order since."
claude project/PDK-001 - 001 - doc-promotions-stacking (turn 2).md | 36 | 36 | Dropped | "the cart tells the customer: "Only one code per order. Your new code has replaced the old one.""
claude project/PDK-001 - 001 - doc-promotions-stacking (turn 2).md | 73 | 71 | Dropped | "Paying with a gift card is a payment, not a promotion, so it comes off the total after discounts and shipping"
claude project/PDK-001 - 001 - doc-promotions-stacking (turn 2).md | 135 | 131 | Dropped | "Free-shipping codes stopped on that date, and the one-code rule has covered every order since."
skill/SDK-001 - 001 - doc-promotion-stacking.md | 72 | 66 | Dropped | "The new code replaces the first, and the cart shows `Only one code per order. ...`" (surface "the cart" gone)
skill/SDK-001 - 001 - doc-promotion-stacking.md | 156 | 141 | Dropped | "A gift card is outside the stack on both sides. As a cart item it takes no discount, and as a payment it is not a promotion." (the only reason the payment comes off after the stack)
skill/SDK-001 - 001 - doc-promotion-stacking.md | 180 | 160 | Changed | "Retired material, refund behavior for pre-2026-05-01 orders" (now "pre-2026-05-01 refunds", which dates the refunds instead of the orders; CS refunds these orders today)
skill/SDK-001 - 001 - doc-promotion-stacking.md | 258 | 236 | Dropped | "Free-shipping codes stopped that day, and since then the one-code rule covers every order"
skill/SEP-001 - 001 - Epic-partner-self-onboarding.md | 12 | 12 | Changed | "Most partners who drop out do so while they wait for an agent to reply, not while they fill anything in." (cut "Most partners drop out while waiting" says most partners drop out, against the 38% in the same section, and loses what they wait for)
skill/SEP-001 - 001 - Epic-partner-self-onboarding.md | 163 | 163 | Changed | "An Ops agent building or editing a self-onboarded listing's setup instead of reviewing it" (cut bans any edit of a self-onboarded listing, a wider No-go than setup work done in place of review)
skill/SEP-002 - 002 - Epic-offline-mode.md | 30 | 28 | Changed | "The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release" (cut "Mobile sessions hitting the no-connection screen halve" measures a count, not a share)
skill/SEP-002 - 002 - Epic-offline-mode.md | 63 | 61 | Changed | "Neither story depends on the conflict-handling decision, so both can start before 2026-10-09." (permission became a plan: "both start")
skill/SEP-003 - 001 - Epic-self-serve-returns.md | 10 | 10 | Changed | "CS handles about `1,900` return requests a month this way" (cut counts "returns", not requests)
skill/SST-001 - 002 - Story-free-cancellation-filter.md | 59 | 59 | Changed | "the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`" (cut "a `Clear filter` button" no longer limits the empty state to one button)

Files read: 7 (each snapshot and cut in full). Problems found: 16 (PDK-001: 3, PDK-001 turn 2: 3, SDK-001: 4, SEP-001: 2, SEP-002: 2, SEP-003: 1, SST-001: 1). No file is free of problems.

## Verdicts on the flagged cuts

- SDK-001 rule 2, dropped "a 15% code on a line that already has 20% off saves less than 15% of the original price": fine. It illustrates the rule; the code block ("taken from the price left after step 1") and the Netherlands example still carry the fact.
- SDK-001 status line "per the Promotions rules note": fine. The snapshot already stated plainly at line 33 that promotions-service applies every rule, so no hedge became a claim. The same holds for Source basis dropping "The note states that".
- SDK-001 cell "refund behavior for pre-2026-05-01 orders" to "pre-2026-05-01 refunds": Changed, listed above. Suggested wording: "refunds on pre-2026-05-01 orders".
- PDK-001, both copies, dropped "a code can take an order from free shipping to paid shipping": fine. It follows from the threshold being checked on the discounted subtotal, and the UK example shows it.
- PDK-001 Retired status lines saying "older orders": fine. "Until 2026-05-01" in the same section anchors the date, and turn 2 keeps "Orders placed before 2026-05-01".
- PDK-001 and SDK-001 rule 9 "comes off the final total": the outcome is fine; the final total is the total after discounts and shipping, and SDK-001's code block keeps the order. The reason sentence that went with it is Dropped, listed above.
- Precedence table body cells, PDK-001 both copies: every row keeps its outcome. "The code applies only to the other lines" equals "blocked on the covered lines and applies to the others"; "All promotions removed" sits under a condition naming automatic promotions.
- Precedence table body cells, SDK-001: every row keeps its outcome. The exclusive-promotion row lost "and applies to the rest", but rule 3 Then still says "applies to the others", so no fact left the file. Only the refund status cell changed meaning, listed above.
- Sale items rule and glossary "which are skipped when it is off" (PDK-001) and "when off, it skips them" (SDK-001): fine. The Sale items rule and the precedence row still say sale items are skipped when `applies_to_sale` is off, and staff codes still always apply.
- SEP-001 Goal: fine. "with no Ops agent doing the setup" and "Ops agents only check a finished listing" still stand in the benefits, the Solution go-live gate and AC1.
- SEP-001 go-live and payouts Solution bullet: fine. "payouts on the checks" is vague on its own, but Getting paid, AC3 and the No-go still name both the bank account and identity checks.
- SEP-001 No-go that lost "instead of reviewing it": Changed, listed above.
- SEP-002 dropped "Desktop covers the laptop case": fine. It is a second reason after the browser-tab reason, which the cut keeps, and the operator allowed cutting explanation past the first reason.
- SEP-002 folded "The mobile apps ... cannot open another one offline": fine. "needs a connection for everything past the page on screen" keeps the fact.
- SEP-003 Scope intro: fine. Pallet items staying with CS still stands in About and Solution, and the child stories' detailed criteria stand in the Acceptance criteria intro.
- SST-001 Solution: fine. Price, deadline, the rate the guest would book and the confirmation-email reason all stand in Requirements and AC2 and AC3.
- SST-001 dropped "so the question lands on Guest Support": fine. Problem still says the question is the top pre-booking Guest Support question, and the Expected outcomes tie fewer such chats to the filter.

## PDK-001 turn copies, shared wording

The snapshots worded the Retired rule's two paragraphs alike in both copies. The cut copies now differ. Turn 1 line 130 reads "Until 2026-05-01 a customer could combine..." and line 132 "Older orders can still show two codes in Admin, and a refund on one splits the discount across both codes." Turn 2 line 131 reads "Until then a customer could combine..." and line 129 "Orders placed before 2026-05-01 can still show two codes in Admin, and a refund on one splits the discount across both codes." Both say the same thing, but the wording diverged where the snapshots matched. Every other shared sentence is worded alike in both cut copies. The remaining differences (Source basis, Overview, glossary automatic promotion, discount code and subtotal, Open questions intro, the banner question, the status line and the related link) were already different in the snapshots.

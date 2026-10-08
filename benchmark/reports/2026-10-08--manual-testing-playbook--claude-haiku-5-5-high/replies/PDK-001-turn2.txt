```markdown
# Discount codes and automatic promotions: how they stack

* * *
> **Source basis**
> *   **Current behavior** — Promotions rules note, owned by Colette in Merchandising, last edited 2026-09-02
> *   **Retired material** — Two codes on one order, retired 2026-05-01 and kept for orders placed before that date
* * *

## Overview
* * *

This reference predicts the discount on any cart. It explains how one discount code and automatic promotions combine and which items they skip. It also covers the cap on each line and how rounding works, plus the free-shipping threshold and gift cards after discounts. CS agents use it to explain an order or a refund. Checkout engineers use it to check a cart total.

The Promotions rules note governs every rule here. The Fernhouse company context note is background only and sets no rule. How merchandisers set up promotions in Admin is out of scope.

### Terms
* * *

*   **Automatic promotion** — A discount that applies without a code, before any code is applied
*   **Discount code** — A code the customer enters in the cart or at checkout
*   **Exclusive** — A flag that stops a promotion or code combining with other discounts, with different effects for codes and promotions
*   **Staff code** — A code starting with `STAFF-`, tied to one staff account
*   **Sale item** — A product whose catalog `compare_at` price is above its current price, and that struck-through price does not count toward the cap
*   **Line** — One cart line, priced before any discount, where caps and rounding apply
*   **Subtotal** — The sum of line prices after every discount and before shipping
*   **Euro markets** — The Netherlands, Belgium, Germany and France

## Behavior rules
* * *

Status: Current behavior — Promotions rules note, last edited 2026-09-02

### Predict a cart total
* * *

Work through these steps in order. They arrange the note's rules into a sequence and add no new rule.

1. If the order has an exclusive code, remove every automatic promotion and apply only that code.
2. Otherwise, each line takes at most one automatic promotion, and the bigger saving applies when two match.
3. A line covered by an exclusive automatic promotion takes no code, though other lines still can.
4. Apply the one discount code, if any, to the price left on each eligible line.
5. Skip sale items unless the code's `applies_to_sale` is switched on, except staff codes, which apply to sale items.
6. Cap each line's total discount at 50% of its price before promotions, cutting the code's share until the line sits at exactly 50%.
7. Round each line's discount to `0.01` with half up rounding.
8. A fixed-amount code is split across eligible lines in proportion to price, and a leftover cent goes to the most expensive line.
9. The order discount is the sum of the line discounts.
10. Take the subtotal after every discount and before shipping, leaving gift cards out.
11. Free shipping applies when that subtotal is at least `€50` in the euro markets or `£45` in the UK.
12. Otherwise, standard shipping applies: `€4.95` in the euro markets or `£3.95` in the UK.
13. Take any gift card payment off the total after discounts and shipping.

### Combinations and precedence
* * *

| Conditions | Outcome |
| --- | --- |
| An exclusive code is entered | Every automatic promotion comes off the order and the code applies alone |
| An exclusive automatic promotion covers a line and a code is entered | No code applies to that line, and the code still applies to other lines |
| A second discount code is entered | The new code replaces the first, and the cart shows "Only one code per order. Your new code has replaced the old one." |
| Two automatic promotions match one line | The bigger saving applies |
| A staff code is entered | The code is exclusive, so every automatic promotion comes off, and it gives 30% off, including on sale items |
| A code is entered on a sale item with applies_to_sale off | The code skips the item |
| A code and an automatic promotion would take a line past 50% | The code's share is cut until the line sits at exactly 50% |
| A gift card is in the cart | It takes no discount and does not count toward the threshold |

### Examples
* * *

#### Code on top of an automatic promotion, Netherlands
* * *

*   **Given** — Stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. Linen tea towels, set of 3, at €24.90. A cast iron casserole at €89.00 with a `compare_at` price of €119.00, so it is on sale. Code HOME15 gives 15% off and has `applies_to_sale` switched off.
*   **When** — The code HOME15 is entered
*   **Then** — The discounts and totals are:

| Line | Price | Automatic | Code | Line total |
| --- | --- | --- | --- | --- |
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99, leaving €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is well over €50, so shipping is free.

#### The 50% cap
* * *

*   **Given** — An oak serving board at €30.00 sits in a clearance promotion of 40% off, leaving €18.00, and code HOME25 gives 25% off.
*   **When** — The code is applied
*   **Then** — The code is cut from €4.50 to €3.00, so the line ends at €15.00, which is 50%.

#### Threshold after discounts, UK
* * *

*   **Given** — A subtotal of £48.00 before the code, and code WELCOME10 takes 10% off.
*   **When** — The code is applied
*   **Then** — The subtotal falls to £43.20, under £45, so standard shipping of £3.95 applies and the order total is £47.15.

#### Gift card in the cart, Netherlands
* * *

*   **Given** — A €25.00 gift card and a bread bin at €32.00, a cart total of €57.00
*   **When** — The order is placed
*   **Then** — Only the bread bin counts toward the threshold, so the order pays €4.95 shipping

## Retired rules
* * *

Status: Retired material — retired on 2026-05-01 and removed from promotions-service on 2026-05-04

### Two codes on one order (retired)
* * *

Until 2026-05-01, a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and the one-code rule has covered every order since.

Orders placed before 2026-05-01 can still show two codes in Admin. A refund on one of them splits the discount across both codes, as it did at the time. This rule is kept so CS can explain those orders. Do not build on it.

## Boundaries and exceptions
* * *

*   **Banner wording** — The banner says "over €50" and "over £45", but the rule says "at least", so an order at exactly €50.00 or £45.00 ships free under the rule. This reference follows the rule, and the sources do not show whether the banner matches promotions-service.
*   **Automatic promotion types** — The sources show percentage-off automatic promotions only, so this reference does not predict any other kind.
*   **Quantity above one** — The rules work per line. The sources do not say how a line with a quantity above one is priced or capped, so this reference does not predict that case.
```

Export-equivalent path: `export/NNN - doc-discount-stacking.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: em dash in the ClickUp definition and status-label shapes, and the quoted banner and cart copy kept verbatim from the sources.

Quality summary:
- Source safety: pass. The rules note is the governing source, the retired two-code rule carries its retired label, and the context note is used only as background.
- Shape fit: pass. Behavior reference, built for a reader who predicts a cart total.
- ClickUp layout: pass. Title, dividers under every content heading, `*   ` bullets, no spacer headings.
- Readability: pass. Prediction steps come first, with a table for the interactions and four worked examples.
- Voice: pass.

Three additions for you to strike or confirm:
- The 13 prediction steps are my arrangement of the note's rules into an order. They add no new rule.
- The banner wording is flagged as unresolved, not corrected. The doc follows the rule, as you directed.
- The doc says the sources show only percentage-off automatic promotions and do not say how a line with quantity above one is priced. These are gaps in the note, not behavior I have filled in.
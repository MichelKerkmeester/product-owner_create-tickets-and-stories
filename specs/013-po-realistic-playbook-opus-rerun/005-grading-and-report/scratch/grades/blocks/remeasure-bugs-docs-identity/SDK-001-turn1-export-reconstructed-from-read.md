# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note, owned by Colette (Promotions lead, Merchandising), last edited 2026-09-02. promotions-service applies these rules. If this reference and the note ever disagree, the note wins
> *   **Retired material** — Two codes on one order, retired on 2026-05-01 and kept for orders placed before that date
> *   **Unknown** — The open questions listed under Boundaries and open questions, which the note does not settle
* * *

## Overview
* * *
This reference explains how Fernhouse combines automatic promotions and discount codes on one order, line by line, up to the free-shipping decision. It is for CS agents explaining a total to a customer, engineers checking what promotions-service returned and merchandisers setting up a promotion that will meet other promotions in the same cart.

The short version: automatic promotions apply first, one per line, then one discount code applies to the price that is left. Exclusive promotions, staff codes, sale items and the 50% line cap change that default. Free shipping is decided last, on the subtotal after every discount.
* * *

### Glossary
* * *
*   **Automatic promotion** — A discount that applies without a code, set up by a merchandiser in Admin. Only merchandisers can create or change one
*   **Discount code** — A code the customer types in the cart or at checkout
*   **`exclusive`** — A marking on a promotion or code meaning it combines with nothing
*   **`applies_to_sale`** — A promotion setting. When it is off, the promotion skips sale items
*   **Sale item** — A product whose `compare_at` price in catalog-service is above its current price. The storefront shows the `compare_at` price struck through
*   **Staff code** — A code starting with `STAFF-`, tied to one staff account
*   **Line** — One product in the cart with its quantity. Every discount is worked out per line
*   **Subtotal** — The sum of the lines after every discount and before shipping
* * *

### Where the rules run
* * *
promotions-service works out every discount and the free-shipping threshold. The storefront and the apps show what it returns and never compute a discount themselves. When a discount looks wrong on one surface, the number to check is the one promotions-service returned, because a client cannot produce a different one on its own.
* * *

## Stacking rules
* * *
### How a line is discounted
* * *
**1. One automatic promotion per line**
* * *
A line takes at most one automatic promotion. When two automatic promotions match the same line, the one with the bigger saving applies and the other is ignored for that line.

**2. Automatic promotions first, then the code**
* * *
The discount code applies to the price left after the automatic promotion, never to the original price. A 15% code on a line already at 20% off therefore saves 15% of 80% of the price, which is why the code's saving on a promoted line is smaller than on an unpromoted one.

*   **When** — A line has an automatic promotion and the order has a discount code that is eligible for that line
*   **Then** — The automatic promotion comes off first. The code takes its percentage or share of what remains
*   **Status** — Current behavior

**3. One code per order**
* * *
A customer can use one discount code per order. Entering a second code replaces the first, and the cart shows `Only one code per order. Your new code has replaced the old one.`
* * *

### What changes eligibility
* * *
**4. Exclusive promotions and codes**
* * *
Anything marked `exclusive` combines with nothing, but the effect depends on which side is exclusive.

*   **Exclusive code** — Removes every automatic promotion from the whole order and applies alone
*   **Exclusive automatic promotion** — Blocks codes on the lines it covers only. A code still applies to the other lines in the cart

**5. Staff codes**
* * *
A `STAFF-` code is always exclusive, gives 30% off and also applies to sale items. Because it is exclusive, entering one removes every automatic promotion from the order, following rule 4.

**6. Sale items**
* * *
Codes and automatic promotions skip sale items unless the promotion has `applies_to_sale` switched on. Staff codes are the exception and always apply to sale items. A sale item's struck-through `compare_at` price does not count toward the 50% cap in rule 8.

**7. Gift cards in the cart**
* * *
A gift card bought as a product never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment, not a promotion, so it comes off the total after discounts and shipping and has no effect on stacking.
* * *

### Limits and totals
* * *
**8. The 50% line cap**
* * *
The total discount on a line never goes past 50% of that line's price before promotions. When the rules above would go past the cap, the code's share is cut until the line sits at exactly 50%. The automatic promotion keeps its full saving and the code absorbs the difference.

**9. Rounding and fixed-amount codes**
* * *
Every discount is worked out per line and rounded to 0.01 with half-up rounding. A fixed-amount code is split across the eligible lines in proportion to their price, and a cent left over from rounding goes to the most expensive line. The order discount is the sum of the line discounts.

**10. Free shipping after discounts**
* * *
Free shipping is decided on the subtotal after every discount and before shipping, with gift cards left out. An order ships free when that subtotal is at least €50 in the euro markets or £45 in the UK. Below it, standard shipping is €4.95 or £3.95. A code can therefore push an order under the threshold and add a shipping charge, as the UK example below shows.
* * *

## Combinations and precedence
* * *
| Conditions | Outcome | Status |
| --- | --- | --- |
| Two automatic promotions match one line | The bigger saving applies, the other is ignored on that line | Current behavior |
| Automatic promotion and a code on one line | Automatic first, then the code on the remaining price | Current behavior |
| Customer enters a second code | The new code replaces the first, with the one-code message | Current behavior |
| Exclusive code in the cart | Every automatic promotion is removed from the order and the code applies alone. The note names no savings comparison, so the order can end with less discount than the automatic promotions gave | Current behavior |
| Exclusive automatic promotion on some lines and an ordinary code | The code skips the covered lines and applies to the other eligible lines | Current behavior |
| `STAFF-` code in the cart | Treated as exclusive, 30% off, sale items included | Current behavior |
| Sale item and a promotion with `applies_to_sale` off | The promotion skips the line | Current behavior |
| Automatic promotion plus code would exceed 50% on a line | The code's share is cut so the line ends at exactly 50% off | Current behavior |
| Exclusive code and exclusive automatic promotion in the same cart | Not settled by the note | Unknown |
| Automatic promotion alone above 50% on a line | Not settled by the note | Unknown |
* * *

### Worked examples
* * *
These examples come from the Promotions rules note. The amounts are the note's own.

#### Code on top of an automatic promotion, Netherlands
* * *
Code HOME15 gives 15% off with `applies_to_sale` off. The plates carry the automatic promotion Tableware 20% off, the towels carry none and the casserole is a sale item (€89.00, `compare_at` €119.00).

| Line | Price | Automatic | Code | Line total |
| --- | --- | --- | --- | --- |
| Stoneware dinner plates, set of 4 | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Linen tea towels, set of 3 | €24.90 | none | minus €3.74 | €21.16 |
| Cast iron casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is well over €50, so shipping is free.

#### The 50% cap
* * *
An oak serving board at €30.00 sits in a clearance promotion of 40% off, which leaves €18.00. Code HOME25 would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%. The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00.

#### Threshold after discounts, UK
* * *
The subtotal is £48.00 before the code. WELCOME10 takes 10%, which is £4.80 and leaves £43.20. That is under £45, so standard shipping of £3.95 applies and the order total is £47.15.

#### Gift card in the cart, Netherlands
* * *
A €25.00 gift card and a bread bin at €32.00. Only the bread bin counts toward the threshold, so the order pays €4.95 shipping even though the cart holds €57.00.
* * *

### Retired: two codes on one order
* * *
Status: Retired material — retained for orders placed before 2026-05-01

Until 2026-05-01 a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and the one-code rule has covered every order since. The code path was removed from promotions-service on 2026-05-04.

Orders placed before 2026-05-01 can still show two codes in Admin. A refund on one of those orders splits the discount across both codes, as it did at the time. Do not build on this rule.
* * *

### Boundaries and open questions
* * *
The note leaves these cases open. Colette, as owner of the Promotions rules note, is the person to settle them, and until then none of them should be quoted to a customer as a rule.

*   **Exclusive against exclusive** — An exclusive code removes every automatic promotion, while an exclusive automatic promotion blocks codes on its lines. The note does not say which wins when both are in the same cart, and a `STAFF-` code meeting an exclusive automatic promotion is the same case
*   **Automatic promotion above 50%** — The cap rule says the code's share is cut. It does not say what happens when the automatic promotion alone takes a line past 50%, with or without a code
*   **Base for splitting a fixed-amount code** — The note splits a fixed-amount code "in proportion to their price" and does not say whether that is the price before or after the automatic promotion
*   **Banner wording at exactly the threshold** — The rules make an order free to ship at €50.00 or £45.00 exactly, while the banner copy in the company context reads `Free shipping on orders over €50` and `Free shipping on orders over £45`. The behavior follows the rules. Whether the copy should change is a separate question for the owner of the banner copy
* * *

### Related references
* * *
*   Promotions rules note, Merchandising space, owned by Colette
*   Fernhouse company context, Product space, owned by Lotte

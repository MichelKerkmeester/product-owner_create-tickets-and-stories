# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note, owned by Colette, Promotions lead in Merchandising, last edited 2026-09-02. The note states that promotions-service applies every current rule in it
> *   **Retired material** — Two codes on one order, retired on 2026-05-01 and kept because CS still refunds orders placed under it
> *   **Unknown** — Six combinations the note does not settle, listed under Open questions
* * *

## Overview
* * *

This reference explains what promotions-service does today when discount codes and automatic promotions meet in one cart: which discounts reach each line, in what order, how far they go and the effect on shipping. CS agents use it to explain a total, and Checkout engineers to check a cart against the written rules. Promotion setup is out of scope.

A customer gets at most one code and each line at most one automatic promotion, and the code comes off the price the promotion leaves unless either is marked `exclusive`. Sale items are skipped unless a promotion says otherwise, and no line loses more than half its price before promotions. Six cases stay open, under Open questions.
* * *

### Glossary
* * *

*   **Automatic promotion** — A discount that applies to a line without the customer entering a code
*   **Discount code** — A code the customer enters on the order, staff codes included
*   **`exclusive`** — A flag meaning a promotion or code combines with nothing, and rule 3 sets out what it removes on each type
*   **Sale item** — A product whose `compare_at` price in catalog-service is above its current price, and the storefront shows that price struck through
*   **`applies_to_sale`** — A switch on a promotion or code: when on, it also reaches sale items, and when off, it skips them
*   **Staff code** — A code that starts with `STAFF-` and is tied to one staff account
*   **Subtotal** — The sum of the lines after every discount and before shipping, which the free-shipping threshold is checked against
* * *

### Where the calculation runs
* * *

promotions-service applies every rule in this reference, and the storefront and the apps show what it returns. A discount a customer sees on screen is therefore promotions-service output, so the rules below predict it. The rules note was first written from promotions-service's behavior together with the Checkout team.

Sale status is the one input that comes from elsewhere. A product is a sale item when catalog-service holds a `compare_at` price above its current price, and promotions-service reads that when it decides which discounts reach the line.

The block below lays out the rules note's order for one line. The sale-item and exclusive checks decide which discounts are allowed onto the line before the amounts are worked out.

```text
Allowed onto the line?
  Gift card                   -> nothing, a gift card never takes a discount
  Sale item                   -> each promotion or code skips it unless its applies_to_sale is on
  Exclusive code in the order -> no automatic promotion anywhere in the order
  Exclusive automatic promo   -> no code on the lines it covers

Amounts, in order:
  1. Automatic promotion      -> at most one per line, the bigger saving when two match
  2. Discount code            -> taken from the price left after step 1
  3. 50% cap                  -> the code's share is cut until the line sits at 50%

Every line discount is rounded to 0.01, half up
Order discount = sum of the line discounts
Subtotal -> free-shipping threshold -> shipping -> gift card payment off the total
```
* * *

## Stacking rules
* * *

Status: Current behavior — as recorded in the Promotions rules note, which states that promotions-service applies it
* * *

### Which discounts reach a line
* * *

**1. One code per order**
* * *

A cart holds one discount code at a time, and a new code replaces the old one rather than adding to it.

*   **When** — A customer enters a second code on an order that already has one
*   **Then** — The new code replaces the first, and the cart shows `Only one code per order. Your new code has replaced the old one.`
* * *

**2. Automatic promotions first, then the code**
* * *

The code is always worked out on the price left after the automatic promotion, never on the original price. This is why a 15% code on a line that already has 20% off saves less than 15% of the original price.

*   **When** — A line matches an automatic promotion and the order has a discount code that reaches the same line
*   **Then** — The automatic promotion comes off first, then the code comes off the remaining price
*   **When** — Two automatic promotions match the same line
*   **Then** — Only one applies, the one with the bigger saving
* * *

**3. Exclusive promotions and codes**
* * *

An `exclusive` promotion or code combines with nothing, but its reach differs by type. An exclusive code clears the whole order of automatic promotions. An exclusive automatic promotion blocks codes only on its own lines.

*   **When** — The customer enters an exclusive code
*   **Then** — Every automatic promotion is removed from the order and the code applies alone
*   **When** — An exclusive automatic promotion covers some lines and the customer enters a code
*   **Then** — The code skips the lines the exclusive promotion covers and still applies to the other lines
* * *

**4. Staff codes**
* * *

A staff code behaves like an exclusive code with a fixed value and a wider reach.

*   **When** — A code starting with `STAFF-` is used
*   **Then** — It is always exclusive, gives 30% off and also applies to sale items. Each staff code is tied to one staff account
* * *

**5. Sale items**
* * *

A product with a `compare_at` price above its current price is on sale, and discounts leave it alone by default.

*   **When** — A line holds a sale item
*   **Then** — Codes and automatic promotions skip it, unless that promotion or code has `applies_to_sale` switched on. Staff codes always reach it
* * *

### How far a discount can go
* * *

**6. The 50% cap**
* * *

No line loses more than half of its price before promotions, and the code is the part that gives way.

*   **When** — The automatic promotion and the code together would take more than `50%` of the line's price before promotions
*   **Then** — The code's share is cut until the line sits at exactly 50%
*   **How** — The cap uses the line's current price before promotions, not the struck-through `compare_at` price, so a sale item's earlier price never raises it
* * *

**7. Rounding and fixed-amount codes**
* * *

Every discount is worked out line by line, so the order discount is always the sum of the rounded line discounts.

*   **When** — Any discount is calculated
*   **Then** — Each line discount is rounded to `0.01` with `half up` rounding
*   **When** — The code is a fixed amount rather than a percentage
*   **Then** — The amount is split across the eligible lines in proportion to their price. A cent left over from rounding goes to the most expensive line
* * *

### What the stack decides afterwards
* * *

**8. Free-shipping threshold**
* * *

The threshold is checked after every discount, so a code can push an order below it.

*   **When** — The subtotal after every discount and before shipping is at least `€50` in the euro markets or `£45` in the UK
*   **Then** — The order ships free
*   **When** — The subtotal is below that
*   **Then** — Standard shipping applies, €4.95 in the euro markets or £3.95 in the UK
* * *

**9. Gift cards**
* * *

A gift card is outside the stack on both sides. As a cart item it takes no discount, and as a payment it is not a promotion.

*   **When** — A gift card is in the cart
*   **Then** — It never takes a discount and does not count toward the free-shipping threshold
*   **When** — A customer pays with a gift card
*   **Then** — The gift card comes off the total after discounts and shipping
* * *

## Combinations and precedence
* * *

| Conditions | Outcome | Status |
| ---| ---| --- |
| Automatic promotion and code on the same line, neither exclusive | Automatic promotion first, code on the remaining price | Current behavior, rule 2 |
| Two automatic promotions match one line | The bigger saving applies, the other does not | Current behavior, rule 2 |
| Customer enters a second code | The second code replaces the first | Current behavior, rule 1 |
| Exclusive code with automatic promotions in the cart | Every automatic promotion is removed from the order, the code applies alone | Current behavior, rule 3 |
| Exclusive automatic promotion on some lines, plus a code | The code skips the covered lines and applies to the rest | Current behavior, rule 3 |
| Staff code on a sale item | 30% off applies, and no automatic promotion applies anywhere in the order | Current behavior, rules 3 and 4 |
| Sale item, `applies_to_sale` off | The promotion or code skips the line | Current behavior, rule 5 |
| Automatic promotion and code together above 50% | The code's share is cut to bring the line to 50% | Current behavior, rule 6 |
| Gift card in the cart with a code | No discount on the gift card, and it does not count toward the threshold | Current behavior, rule 8 |
| Exclusive code on a line an exclusive automatic promotion covers | Not stated | Unknown |
| Percentage code plus free-shipping code, order placed before 2026-05-01 | Both applied | Retired material |
| Refund on one of those two-code orders | The refunded discount is split across both codes, as it was at the time | Retired material, refund behavior for pre-2026-05-01 orders |
* * *

### Examples
* * *

These are the worked examples from the Promotions rules note, with the note's own figures.

#### Code on top of an automatic promotion, Netherlands
* * *

The cart has stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. It also has linen tea towels, set of 3, at €24.90 with no promotion, and a cast iron casserole at €89.00 with a `compare_at` price of €119.00, making it a sale item. Code HOME15 gives 15% off and has `applies_to_sale` off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99 and leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79.

The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is over the threshold, so shipping is free.
* * *

#### The 50% cap
* * *

*   **Given** — An oak serving board at €30.00 in a clearance promotion of 40% off, which leaves €18.00
*   **When** — Code HOME25 would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%
*   **Then** — The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00
* * *

#### Threshold after discounts, UK
* * *

*   **Given** — A subtotal of £48.00 before the code
*   **When** — Code WELCOME10 takes 10%, which is £4.80 and leaves £43.20
*   **Then** — £43.20 is under £45, so standard shipping of £3.95 applies and the order total is £47.15
* * *

#### Gift card in the cart, Netherlands
* * *

*   **Given** — A €25.00 gift card and a bread bin at €32.00
*   **When** — The threshold is checked
*   **Then** — Only the bread bin counts, so the order pays €4.95 shipping even though the cart holds €57.00
* * *

## Boundaries and history
* * *

### Open questions
* * *

Status: Unverified — the Promotions rules note does not settle these cases

Each case below can come up in an ordinary cart, and each one has two rules that could apply and no written answer. Colette owns the note, so she is the person who can add the answer.

*   **Two exclusives on one line** — Which wins when an exclusive code and an exclusive automatic promotion meet on the same line
*   **Exclusive against bigger saving** — Whether an exclusive promotion with the smaller saving still takes the line and still blocks the code
*   **An exclusive code that reaches no line** — Whether it still removes the automatic promotions, as with `applies_to_sale` off in a cart of sale items only
*   **An automatic promotion above 50% on its own** — What happens with or without a code, since the cap is met by cutting the code's share
*   **Rounding at the cap** — Which way the capped amount rounds, since a capped line sits at exactly 50% and half of €39.95 is €19.975
*   **The price a fixed-amount code is split by** — Whether the split follows each line's price before or after the automatic promotion
* * *

### Free-shipping banner wording
* * *

An order whose subtotal is exactly €50.00 or £45.00 ships free, because rule 8 sets the threshold at "at least" that amount. The banner reads `Free shipping on orders over €50` and `Free shipping on orders over £45`, so a customer at exactly the threshold may expect to pay shipping and not be charged. The rules note governs the order, and neither source says whether the wording difference is intended.
* * *

### Retired rule: two codes on one order
* * *

Status: Retired material — retired on 2026-05-01, kept because CS still refunds orders placed under it

No order placed today can carry two codes, but CS still refunds orders that do. Until 2026-05-01 a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped that day, and since then the one-code rule covers every order, with the code path removed from promotions-service on 2026-05-04.

An order placed before 2026-05-01 can still show two codes in Admin. When a CS agent refunds one of those orders, the refund splits the discount across both codes, as it did at the time. Nothing new should be built on this rule.
* * *

### Related references
* * *

*   [Promotions rules](../context/fernhouse-promotions-rules.md), the governing source for every rule here
*   [Fernhouse company context](../context/fernhouse-context.md), background on markets, surfaces and services

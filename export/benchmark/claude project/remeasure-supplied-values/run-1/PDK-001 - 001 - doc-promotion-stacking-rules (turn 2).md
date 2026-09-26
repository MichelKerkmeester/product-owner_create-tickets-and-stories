# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — Promotions rules, owned by Colette (Promotions lead, Merchandising), last edited 2026-09-02. This note governs every rule in this reference, and promotions-service applies it
> *   **Background** — Fernhouse company context, owned by Lotte (Head of Product), last updated 2026-09-18. It is used only for where discounts are calculated and for the banner copy, and it gives way to the rules note wherever the two differ
> *   **Retired material** — The two-codes rule from Promotions rules, retired on 2026-05-01 and kept because CS still refunds orders placed under it
> *   **Unknown** — Five open points listed under Boundaries and exceptions
* * *

## Overview
* * *
This reference lets you predict the discount on any Fernhouse cart. It covers automatic promotions and one discount code on the same order, and promotions-service combines them line by line. It sets out the order they apply in, what blocks a code, what caps a line, how rounding works and how the result feeds the free-shipping threshold.

It is written for CS agents, who explain totals to customers and refund orders, and for the Checkout engineers, whose services carry the prices promotions-service returns. The rules hold in all five markets. How a promotion is set up in Admin is outside this reference.
* * *

### Glossary
* * *
*   **Automatic promotion** — A discount that applies without a code
*   **Discount code** — A code the customer types in the cart or at checkout
*   **`exclusive`** — A flag on a promotion or code meaning it combines with nothing
*   **Sale item** — A product whose `compare_at` price in catalog-service is above its current price. The storefront shows the `compare_at` price struck through
*   **`applies_to_sale`** — A switch on a promotion that lets it discount sale items. With the switch off, sale items are skipped
*   **Staff code** — A code starting with `STAFF-`, tied to one staff account
*   **Subtotal** — The sum of the lines after every discount and before shipping
* * *

### Where discounts are calculated
* * *
Status: Background — from the Fernhouse company context

Discounts are worked out in promotions-service only. The web storefront and the iOS and Android apps show the amounts it returns and never compute a discount themselves.

Two other services hold the inputs. catalog-service holds prices and `compare_at` prices, which decide whether a line is a sale item. cart-service, which Checkout owns, holds the line prices after automatic promotions.
* * *

## Behavior rules
* * *
Status: Current behavior — applied by promotions-service, per Promotions rules last edited 2026-09-02

### One code per order
* * *
A customer can use `one discount code per order`. A second code never stacks with the first. When a customer enters a new code on an order that already has one, the new code replaces the old one and the cart shows "Only one code per order. Your new code has replaced the old one."
* * *

### Order of application
* * *
promotions-service applies `automatic promotions first`, then the discount code on the price that is left. A percentage code therefore works on the reduced line price, not on the original one.

Each line takes at most one automatic promotion.

*   **When** — Two automatic promotions match the same line
*   **Then** — The one with the bigger saving applies to that line
* * *

### Exclusive promotions and codes
* * *
A promotion or code marked `exclusive` combines with nothing. What it blocks depends on whether it is a code or an automatic promotion.

*   **Exclusive code** — Removes every automatic promotion from the order and applies alone
*   **Exclusive automatic promotion** — Blocks codes on the lines it covers. A code still applies to the other lines on the order
* * *

### Sale items and staff codes
* * *
A product is on sale when catalog-service holds a `compare_at` price above its current price. Codes and automatic promotions skip sale items unless the promotion has `applies_to_sale` switched on.

Staff codes start with `STAFF-` and are tied to one staff account. They are always exclusive, give 30% off and also apply to sale items. Because a staff code is exclusive, it removes every automatic promotion from the order in the same way as any exclusive code.
* * *

### The 50% cap
* * *
The total discount on a line never goes past `50%` of that line's price before promotions. The struck-through `compare_at` price does not count, so the cap on a sale item is half its current price rather than half its old price.

*   **When** — The automatic promotion and the code together would take a line past the cap
*   **Then** — The code's share is cut until the line sits at exactly 50%
* * *

### Free shipping and gift cards
* * *
An order ships free when the subtotal, after every discount and before shipping, is at least `€50` in the euro markets or `£45` in the UK. Below that, standard shipping is €4.95 in the euro markets or £3.95 in the UK. Because the threshold is checked after discounts, a code can take an order from free shipping to paid shipping.

A `gift card` in the cart never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment, not a promotion, and it comes off the total after discounts and shipping.
* * *

### Rounding and fixed-amount codes
* * *
Every discount is worked out per line and rounded to `0.01` with `half up` rounding. The order discount is the sum of the line discounts.

A fixed-amount code is split across the eligible lines in proportion to their price, and a cent left over from rounding goes to the most expensive line. Sale items without `applies_to_sale` and gift cards are not eligible, so they take no share of the code.
* * *

## Combinations and precedence
* * *

| Conditions | Outcome | Authority or status |
| ---| ---| --- |
| A second code is entered | It replaces the first code | Current behavior |
| Two automatic promotions match one line | The bigger saving applies | Current behavior |
| Automatic promotion and a non-exclusive code on one line | Automatic promotion first, then the code on the remaining price | Current behavior |
| Exclusive code on an order with automatic promotions | Every automatic promotion is removed and the code applies alone | Current behavior |
| Exclusive automatic promotion and a code | The code is blocked on the covered lines and applies to the other lines | Current behavior |
| Code or automatic promotion on a sale item, `applies_to_sale` off | The sale item is skipped | Current behavior |
| Staff code on a sale item | The code applies at 30%, alone | Current behavior |
| Automatic promotion and code together pass 50% of the line price | The code's share is cut to leave the line at exactly 50% | Current behavior |
| Subtotal after discounts below `€50` or `£45` | Standard shipping of €4.95 or £3.95 applies | Current behavior |
| Gift card in the cart | No discount on the gift card, and it does not count toward the threshold | Current behavior |
| Order placed before `2026-05-01` with two codes, one refunded | The refund splits the discount across both codes as at the time | Retired material |
* * *

### Worked examples
* * *
All four examples and their figures come from the Promotions rules note.

#### Code on top of an automatic promotion, Netherlands
* * *
The cart holds stoneware dinner plates (set of 4) at €39.95 with the automatic promotion Tableware 20% off, and linen tea towels (set of 3) at €24.90 with no promotion. It also holds a cast iron casserole at €89.00 with a `compare_at` price of €119.00, which makes it a sale item. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99 and leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is well over the threshold, so shipping is free.
* * *

#### The 50% cap
* * *
An oak serving board at €30.00 sits in a clearance promotion of 40% off, which leaves €18.00. Code HOME25 would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%. The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00.
* * *

#### Threshold after discounts, UK
* * *
The subtotal is £48.00 before the code. Code WELCOME10 takes 10%, which is £4.80 and leaves £43.20. That is under £45, so standard shipping of £3.95 applies and the order total is £47.15.
* * *

#### Gift card in the cart, Netherlands
* * *
The cart holds a €25.00 gift card and a bread bin at €32.00. Only the bread bin counts toward the threshold, so the order pays €4.95 shipping even though the cart holds €57.00.
* * *

### Retired rule: two codes on one order
* * *
Status: Retired material — retired on 2026-05-01, code path removed from promotions-service on 2026-05-04

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and since then the one-code rule covers every order. Do not build on this rule, and do not use it to predict a new cart.

CS still refunds orders placed under it. An order placed before `2026-05-01` can show two codes in Admin, and a refund on one of those orders splits the discount across both codes as it did at the time.
* * *

### Boundaries and exceptions
* * *
*   **Banner wording at the threshold** — The company context gives the banner copy as `Free shipping on orders over €50` and `Free shipping on orders over £45`. The rules note gives free shipping at exactly €50.00 or £45.00, and the rules note governs. Neither source says whether the banner copy should change
*   **Exclusive automatic promotion and other lines** — The note says an exclusive automatic promotion combines with nothing but only describes its effect on codes. Whether it also removes automatic promotions from other lines is not stated
*   **Automatic promotion above 50% on its own** — The cap is described only as cutting the code's share. How a line is capped when its automatic promotion alone passes 50% is not stated
*   **Fixed-amount code at the cap** — When the cap cuts a fixed-amount code on one line, the note does not say whether the cut amount moves to other eligible lines or is dropped
*   **Equal savings** — When two automatic promotions on one line give the same saving, the note does not say which one applies
* * *

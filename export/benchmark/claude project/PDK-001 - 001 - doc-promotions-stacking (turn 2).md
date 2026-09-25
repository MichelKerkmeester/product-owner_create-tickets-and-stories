# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note, owned by Colette (Promotions lead, Merchandising), last edited 2026-09-02. promotions-service applies every rule in it
> *   **Retired material** — The two-codes rule, retired on 2026-05-01 and kept because CS still refunds orders placed under it
> *   **Unknown** — Four cases the rules note does not settle, listed under Open questions
* * *

## Overview
* * *
This reference explains the discount promotions-service gives an order today when a discount code meets one or more automatic promotions. It also covers how that discount decides free shipping. It is for CS agents explaining or refunding an order, and for Checkout engineers who need to know what promotions-service will return for a cart. With it, either reader can work out the discount on any cart without opening another document.

promotions-service applies every rule below, and the storefront and the apps show what it returns. How a promotion is created or changed in Admin is outside this document.

### Glossary
* * *
*   **Automatic promotion** — A discount that applies without a code
*   **Discount code** — A code the customer enters on the order. One per order
*   **`exclusive`** — A flag on a promotion or code. An exclusive promotion or code combines with nothing
*   **`applies_to_sale`** — A flag that lets a promotion or code discount sale items. When it is off, sale items are skipped
*   **Sale item** — A product whose `compare_at` price in catalog-service is above its current price, shown struck through
*   **Staff code** — A code starting with `STAFF-`, tied to one staff account
*   **Subtotal** — The order total after every discount and before shipping

## Behavior rules
* * *
Status: Current behavior — per the Promotions rules note, last edited 2026-09-02

### Discounts on each line
* * *
promotions-service works line by line. It settles each line's discount first, and the order discount is the sum of the line discounts.

**One code per order**
* * *
A customer can use one discount code per order. Entering a second code replaces the first, and the cart tells the customer: "Only one code per order. Your new code has replaced the old one."

**Automatic promotions first, then the code**
* * *
Automatic promotions apply first. The discount code then applies to the price that is left. Each line takes at most one automatic promotion, and when two match the same line, the one with the bigger saving applies.

**Exclusive promotions and codes**
* * *
A promotion or code marked `exclusive` combines with nothing. What it removes depends on which side carries the flag.

*   **Exclusive code** — Removes every automatic promotion from the order and applies alone
*   **Exclusive automatic promotion** — Blocks codes on the lines it covers. A code still applies to the other lines

**Staff codes**
* * *
Staff codes start with `STAFF-` and are tied to one staff account. They are always exclusive, give 30% off and also apply to sale items. Because they are exclusive, a staff code removes every automatic promotion from the order.

**Sale items**
* * *
A product is on sale when catalog-service holds a `compare_at` price above its current price. Codes and automatic promotions skip sale items unless the promotion has `applies_to_sale` switched on. Staff codes are the one exception, as they always apply to sale items.

**The 50% cap**
* * *
The total discount on a line never goes past 50% of that line's price before promotions. The struck-through `compare_at` price is not that base. When the rules above would push a line past the cap, the code's share is cut until the line sits at exactly 50%.

**Rounding and fixed-amount codes**
* * *
Every discount is worked out per line and rounded to 0.01 with half-up rounding. A fixed-amount code is split across the eligible lines in proportion to their price. A cent left over from rounding goes to the most expensive line.

### What the discounted subtotal decides
* * *
**Free-shipping threshold**
* * *
An order ships free when the subtotal, after every discount and before shipping, is at least €50 in the euro markets or £45 in the UK. Below that, standard shipping is €4.95 or £3.95. This means a code can take an order from free shipping to paid shipping.

**Gift cards**
* * *
A gift card in the cart never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment, not a promotion, so it comes off the total after discounts and shipping.

## Combinations and precedence
* * *

| Conditions | Outcome | Rule |
| --- | --- | --- |
| Customer enters a second code | The new code replaces the first | One code per order |
| Two automatic promotions match one line | The one with the bigger saving applies | Automatic promotions first |
| Automatic promotion and code on one line, neither exclusive | Automatic promotion first, then the code on the price that is left | Automatic promotions first |
| Exclusive code on an order with automatic promotions | Every automatic promotion is removed and the code applies alone | Exclusive |
| Exclusive automatic promotion on some lines, plus a code | The code is blocked on the covered lines and applies to the others | Exclusive |
| Staff code on an order with automatic promotions | Every automatic promotion is removed, and the staff code gives 30% off with sale items included | Staff codes, Exclusive |
| Sale item, and the code or promotion has `applies_to_sale` off | That line is skipped | Sale items |
| Automatic promotion plus code would take a line past 50% | The code's share is cut until the line sits at exactly 50% | The 50% cap |
| Gift card in the cart | Never discounted and not counted toward the threshold | Gift cards |
* * *

### Examples
* * *
#### Code on top of an automatic promotion, Netherlands
* * *
The cart holds stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. It also holds linen tea towels, set of 3, at €24.90 with no promotion, and a cast iron casserole at €89.00 with a `compare_at` price of €119.00, which makes it a sale item. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99 and leaves €31.96. HOME15 then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is well over €50, so shipping is free.

#### The 50% cap
* * *
An oak serving board at €30.00 sits in a clearance promotion of 40% off, which leaves €18.00. Code HOME25 would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%. The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00.

#### Threshold after discounts, UK
* * *
The subtotal is £48.00 before the code. Code WELCOME10 takes 10%, which is £4.80 and leaves £43.20. That is under £45, so standard shipping of £3.95 applies and the order total is £47.15.

#### Gift card in the cart, Netherlands
* * *
The cart holds a €25.00 gift card and a bread bin at €32.00. Only the bread bin counts toward the threshold, so the order pays €4.95 shipping even though the cart holds €57.00.

### Open questions
* * *
The Promotions rules note does not settle the cases below, so this document gives no outcome for them. Colette owns the note and is the person to ask.

*   **Exclusive code meets an exclusive automatic promotion** — An exclusive code removes every automatic promotion, and an exclusive automatic promotion blocks codes on its lines. The note does not say which wins when both sit on one order. Staff codes are always exclusive, so the same gap covers a staff code
*   **Exclusive and non-exclusive automatic promotions on one line** — The bigger saving normally wins. The note does not say whether the `exclusive` flag changes that
*   **Automatic promotion alone above 50%** — The cap only says how the code's share is cut. It does not say what happens when an automatic promotion by itself goes past 50%
*   **Base for splitting a fixed-amount code** — "In proportion to their price" does not say whether that is the price before or after automatic promotions

### Retired rule: two codes on one order
* * *
Status: Retired material — retired on 2026-05-01, kept because CS still refunds orders placed before that date

Orders placed before 2026-05-01 can still show two codes in Admin. A refund on one of those orders splits the discount across both codes, as it did at the time.

Until 2026-05-01 a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and the one-code rule has covered every order since. The code path was removed from promotions-service on 2026-05-04, so nothing new should build on this rule.

### Related references
* * *
*   [Promotions rules](context/fernhouse-promotions-rules.md) — the governing note, owned by Merchandising

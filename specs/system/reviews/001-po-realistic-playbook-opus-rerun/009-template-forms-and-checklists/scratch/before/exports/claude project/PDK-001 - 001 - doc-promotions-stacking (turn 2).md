# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note, owned by Colette (Promotions lead, Merchandising), last edited 2026-09-02. promotions-service applies every rule in it
> *   **Retired material** — The two-codes rule, retired on 2026-05-01, kept because CS still refunds orders placed under it
> *   **Unknown** — Four cases the note does not settle, under Open questions
* * *

## Overview
* * *
This reference explains the discount promotions-service gives an order today when a code meets automatic promotions, and how free shipping is decided. It lets CS agents explain or refund an order and Checkout engineers predict what promotions-service returns, without another document.

promotions-service applies every rule below, and the storefront and apps show its result. Creating or changing a promotion in Admin is out of scope.

### Glossary
* * *
*   **Automatic promotion** — A discount that applies without a code
*   **Discount code** — A code the customer enters on the order, one per order
*   **`exclusive`** — A flag that makes a promotion or code combine with nothing
*   **`applies_to_sale`** — A flag that lets a promotion or code discount sale items
*   **Sale item** — A product whose catalog-service `compare_at` price, shown struck through, is above its current price
*   **Staff code** — A `STAFF-` code tied to one staff account
*   **Subtotal** — The order total after every discount and before shipping

## Behavior rules
* * *
Status: Current behavior — per the Promotions rules note, last edited 2026-09-02

### Discounts on each line
* * *
The order discount is the sum of the line discounts.

**One code per order**
* * *
A second code replaces the first, and the cart tells the customer: "Only one code per order. Your new code has replaced the old one."

**Automatic promotions first, then the code**
* * *
The code applies to what the promotion leaves. A line takes one automatic promotion at most, the bigger saving when two match.

**Exclusive promotions and codes**
* * *
*   **Exclusive code** — Removes every automatic promotion from the order and applies alone
*   **Exclusive automatic promotion** — Blocks codes on its own lines only

**Staff codes**
* * *
Staff codes are always exclusive and give 30% off, sale items included.

**Sale items**
* * *
Codes and promotions skip sale items unless `applies_to_sale` is on, and staff codes always apply.

**The 50% cap**
* * *
A line's discount never passes 50% of its pre-promotion price, not the `compare_at` price. Past that, the code's share is cut to exactly 50%.

**Rounding and fixed-amount codes**
* * *
Line discounts round half up to 0.01. A fixed-amount code splits across eligible lines by price, with a leftover cent to the priciest line.

### What the discounted subtotal decides
* * *
**Free-shipping threshold**
* * *
An order ships free when the subtotal after every discount is at least €50 in the euro markets or £45 in the UK, and otherwise shipping is €4.95 or £3.95.

**Gift cards**
* * *
A gift card in the cart takes no discount and does not count toward the threshold. Paying with one is a payment, not a promotion, so it comes off the total after discounts and shipping.

## Combinations and precedence
* * *

| Conditions | Outcome | Rule |
| --- | --- | --- |
| Second code entered | It replaces the first | One code per order |
| Two automatic promotions on one line | The bigger saving applies | Automatic promotions first |
| Promotion and code on one line, neither exclusive | Promotion first, then the code | Automatic promotions first |
| Exclusive code with automatic promotions | All promotions removed, the code alone | Exclusive |
| Exclusive promotion on some lines, plus a code | The code applies only to the other lines | Exclusive |
| Staff code with automatic promotions | All promotions removed, 30% off with sale items | Staff codes, Exclusive |
| Sale item, `applies_to_sale` off | Skipped | Sale items |
| Promotion plus code past 50% | The code's share is cut to 50% | The 50% cap |
| Gift card in the cart | No discount, not counted toward the threshold | Gift cards |
* * *

### Examples
* * *
#### Code on top of an automatic promotion, Netherlands
* * *
The cart holds stoneware dinner plates, set of 4, at €39.95 with Tableware 20% off, linen tea towels, set of 3, at €24.90, and a cast iron casserole at €89.00, a sale item with `compare_at` €119.00. Code HOME15 gives 15% off with `applies_to_sale` off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20%, €7.99, leaving €31.96, then 15% of €31.96, €4.794, rounded to €4.79. The towels take 15% of €24.90, €3.735, rounded half up to €3.74, and shipping is free.

#### The 50% cap
* * *
An oak serving board at €30.00 has 40% clearance off, leaving €18.00. HOME25 would add 25% of €18.00, €4.50, a total of €16.50 or 55%, so the capped code gives €3.00 and the line ends at €15.00.

#### Threshold after discounts, UK
* * *
A £48.00 subtotal loses £4.80 to WELCOME10 at 10%, leaving £43.20, under £45. So £3.95 shipping applies and the total is £47.15.

#### Gift card in the cart, Netherlands
* * *
A €25.00 gift card and a €32.00 bread bin total €57.00, but only the bread bin counts, so €4.95 shipping applies.

### Open questions
* * *
The rules note does not settle these, so this document gives no outcome for them. Ask Colette, who owns the note.

*   **Exclusive code meets an exclusive automatic promotion** — Which wins, with staff codes in the same gap
*   **Exclusive and non-exclusive automatic promotions on one line** — Whether `exclusive` overrides the bigger saving
*   **Automatic promotion alone above 50%** — The cap only covers cutting the code
*   **Base for splitting a fixed-amount code** — Price before or after automatic promotions

### Retired rule: two codes on one order
* * *
Status: Retired material — retired on 2026-05-01, kept because CS still refunds older orders

Orders placed before 2026-05-01 can still show two codes in Admin, and a refund on one splits the discount across both codes.

Until 2026-05-01 a customer could combine one percentage code with one free-shipping code. Free-shipping codes stopped that day, and the one-code rule has covered every order since. The code path left promotions-service on 2026-05-04, so nothing new should build on this rule.

### Related references
* * *
*   [Promotions rules](context/fernhouse-promotions-rules.md): the governing note, owned by Merchandising

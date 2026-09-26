# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — the Promotions rules note owned by Colette, Promotions lead, last edited 2026-09-02, which states that promotions-service applies every current rule. It governs every rule in this document
> *   **Retired material** — the two-codes rule in the same note, retired on 2026-05-01
> *   **Unknown** — four cases the note does not settle, listed under Open cases
* * *

## Overview
* * *
This reference lets CS agents and Checkout engineers predict the discount on any Fernhouse cart, down to the cent, when automatic promotions and a discount code meet on the same order. CS agents use it to explain a discount to a customer and to refund older orders correctly. Checkout engineers use it to check what a cart should show. The four open cases at the end are the only carts it cannot predict.

promotions-service applies every rule below, and the storefront and the apps show what it returns. A discount on screen is therefore the result promotions-service returned for that cart.
* * *

### Glossary
* * *
*   **Automatic promotion** — a discount that applies to matching lines without a code
*   **Discount code** — a code the customer enters on the order
*   **`exclusive`** — a flag on a promotion or code that stops it combining with anything
*   **`applies_to_sale`** — a flag that lets a promotion or code discount sale items. It is off unless switched on
*   **Sale item** — a product whose `compare_at` price in catalog-service is above its current price, shown struck through
*   **Staff code** — a discount code starting with `STAFF-`, tied to one staff account
*   **Line price before promotions** — the line's own price, which is the base for the 50% cap. The `compare_at` price is never the base
*   **Subtotal** — the sum of the lines after every discount and before shipping
* * *

## Behavior rules
* * *
Status: Current behavior — declared by the Promotions rules note for promotions-service, all markets

### Order of application
* * *
Automatic promotions apply first, and the discount code then applies to the price that is left. The rule's own wording is `automatic promotions first`. Because the code works on the reduced price, a percentage code is worth less on a promoted line than its face value: a 15% code after a 20% automatic promotion takes 12% of the original line price.

Each line takes at most one automatic promotion. When two automatic promotions match the same line, the one with the bigger saving applies and the other gives nothing on that line.
* * *

### One code per order
* * *
A customer can use `one discount code per order`. Entering a second code replaces the first, and the cart tells the customer with this message: "Only one code per order. Your new code has replaced the old one."
* * *

### Exclusive promotions and codes
* * *
A promotion or code marked `exclusive` combines with nothing, but the effect depends on which side carries the flag.

*   **Exclusive code** — removes every automatic promotion from the whole order and applies alone
*   **Exclusive automatic promotion** — blocks codes on the lines it covers only. A code still applies to the other lines in the order

The case where both sides are exclusive is not settled by the note, see Open cases.
* * *

### Staff codes
* * *
A staff code starts with `STAFF-`, is tied to one staff account and gives 30% off. Staff codes are always exclusive, so a staff code removes every automatic promotion from the order. They are also the one kind of code that always applies to sale items.
* * *

### Sale items
* * *
A product is on sale when catalog-service holds a `compare_at` price above its current price. Codes and automatic promotions skip sale items unless the promotion has `applies_to_sale` switched on. A skipped sale item stays at its full current price while the code still discounts the other eligible lines in the order.
* * *

### The 50% cap
* * *
The total discount on a line never goes past `50%` of that line's price before promotions. The struck-through `compare_at` price does not count toward that base, so a sale item's saving against `compare_at` is not part of the cap.

When an automatic promotion plus a code would push a line past the cap, the code's share is cut until the line sits at exactly 50%. The automatic promotion keeps its full saving.
* * *

### Rounding and fixed-amount codes
* * *
Every discount is worked out per line and rounded to `0.01` with `half up` rounding. The order discount is the sum of the line discounts, never a separate calculation on the order total.

A fixed-amount code is split across the eligible lines in proportion to their price. A cent left over from rounding goes to the most expensive line.
* * *

### Free shipping after discounts
* * *
The free-shipping check runs on the subtotal after every discount and before shipping. An order ships free when that subtotal is at least `€50` in the euro markets or `£45` in the UK. Below that, standard shipping is €4.95 or £3.95. A code can therefore drop an order below the threshold and add shipping back, which the UK example below shows.
* * *

### Gift cards
* * *
A `gift card` in the cart never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment, not a promotion, so it comes off the order total after discounts and shipping have been worked out.
* * *

## Combinations and precedence
* * *

| Conditions | Outcome | Status |
| --- | --- | --- |
| Two automatic promotions match one line | The bigger saving applies, the other gives nothing on that line | Current behavior |
| Automatic promotion and a code on one line | Automatic first, then the code on the price that is left | Current behavior |
| Customer enters a second code | The new code replaces the old one and the cart shows the replacement message | Current behavior |
| Exclusive code, automatic promotions on some lines | Every automatic promotion is removed and the code applies alone | Current behavior |
| Exclusive automatic promotion, ordinary code | The code is blocked on the promoted lines and applies to the other lines | Current behavior |
| Staff code in the cart | Exclusive, 30% off every eligible line, sale items included | Current behavior |
| Sale item, promotion or code without `applies_to_sale` | The sale item is skipped | Current behavior |
| Automatic promotion plus code over 50% of the line | The code's share is cut so the line sits at exactly 50% | Current behavior |
| Gift card line and a code | The gift card line takes no discount | Current behavior |
| Exclusive code and exclusive automatic promotion in one order | Not settled by the note | Unknown |
| Automatic promotion alone over 50% of the line | Not settled by the note | Unknown |
| Two automatic promotions with an equal saving on one line | Not settled by the note | Unknown |
* * *

### Examples
* * *
These four examples come from the Promotions rules note. They use HOME15, HOME25 and WELCOME10 as sample codes.

#### Code on top of an automatic promotion, Netherlands
* * *
The cart holds stoneware dinner plates at €39.95 with the automatic promotion Tableware 20% off, linen tea towels at €24.90 with no promotion and a cast iron casserole at €89.00 with a `compare_at` price of €119.00. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
| --- | --- | --- | --- | --- |
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99 and leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is over the threshold, so shipping is free.
* * *

#### 50% cap on a clearance line
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
Status: Retired material — retired on 2026-05-01, kept so CS can explain and refund orders placed before that date. Do not build on it

CS still refunds orders placed under this rule. A refund on an order that shows two codes splits the discount across both codes, as it did at the time, so the current one-code rules do not predict that refund.

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and since then the one-code rule covers every order. The code path was removed from promotions-service on 2026-05-04, which means no new order can carry two codes. Orders placed before `2026-05-01` can still show two codes in Admin.
* * *

### Open cases
* * *
The note leaves these cases open, so do not promise a customer an outcome for them until Colette, who owns the note, settles them.

*   **Exclusive code meets an exclusive automatic promotion** — the exclusive code rule says it removes every automatic promotion, and the exclusive automatic promotion rule says it blocks codes on its lines. Both cannot hold for the same line
*   **Automatic promotion alone above 50%** — the cap says a line never goes past 50%, but the note only describes cutting a code's share. It does not say what happens to an automatic promotion above 50% with no code
*   **Equal savings on one line** — the note says the bigger saving wins and names no tie-break
*   **Base for splitting a fixed-amount code** — "in proportion to their price" does not say whether that is the line price before or after the automatic promotion
* * *

### Related references
* * *
*   [Promotions rules](../context/fernhouse-promotions-rules.md), owned by Colette in the Merchandising space. The governing source for every rule here
*   [Fernhouse company context](../context/fernhouse-context.md), owned by Lotte in the Product space. Company background only, not a source for these rules

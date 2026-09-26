````markdown
# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note, owned by Colette in Merchandising, last edited 2026-09-02 and applied by promotions-service. It covers every rule, combination and worked example below
> *   **Retired material** — The two-code rule, retired on 2026-05-01 and kept so CS can explain older orders
> *   **Unknown** — The cases under Open questions, which the note does not settle
* * *

## Overview
* * *
This reference explains which discounts a Fernhouse order ends up with when a discount code and automatic promotions meet in one cart. Each line takes at most one automatic promotion, and then one code applies to the price that is left. An exclusive promotion or code, a sale item or the 50% line cap can stop that code or make it smaller.

It is for CS agents explaining a discount on an order, for engineers checking what promotions-service returned and for merchandisers setting up a promotion that has to work alongside codes. Read it when a discount looks wrong or when you need to predict what a new promotion will do to carts that already carry a code.

promotions-service works out every discount and the free-shipping threshold. The storefront and the apps show what it returns and never compute a discount themselves. catalog-service holds the `compare_at` prices that make a product a sale item. Only merchandisers can create or change a promotion in Admin.
* * *

### Terms
* * *
*   **Automatic promotion** — A discount that applies without a code, set up by a merchandiser in Admin
*   **Discount code** — A code the customer types in the cart or at checkout
*   **`exclusive`** — A flag on a promotion or code. An exclusive promotion or code combines with nothing
*   **Sale item** — A product whose `compare_at` price in catalog-service is above its current price, shown struck through
*   **`applies_to_sale`** — A switch on a promotion or code. When it is on, the discount also reaches sale items
*   **Staff code** — A code that starts with `STAFF-` and is tied to one staff account
*   **Line price before promotions** — The line's price before any automatic promotion or code. The 50% cap is measured against it, never against the `compare_at` price
*   **Subtotal** — The sum of the lines after every discount and before shipping
* * *

## Behavior rules
* * *
Status: Current behavior — Promotions rules note, applied by promotions-service in all five markets

Rules 1 to 8 decide the discount on each line. Rules 9 and 10 decide what the discounted subtotal means for shipping.
* * *

### Which discounts reach a line
* * *
**1. Automatic promotions first, then the code**
* * *
The code always takes its share from the price the automatic promotion left, not from the original price.

*   **When** — A line matches an automatic promotion and the order carries a code that also applies to that line
*   **Then** — The automatic promotion comes off first, and the code applies to the remaining price
* * *

**2. One automatic promotion per line**
* * *
*   **When** — Two automatic promotions match the same line
*   **Then** — The one with the bigger saving applies and the other does not
* * *

**3. One code per order**
* * *
*   **When** — A customer enters a second code
*   **Then** — The new code replaces the first, and the cart shows "Only one code per order. Your new code has replaced the old one."
* * *

### Exclusive and staff codes
* * *
**4. Exclusive codes and promotions**
* * *
An exclusive promotion or code combines with nothing. What it removes depends on whether it is a code or an automatic promotion.

*   **Exclusive code** — Removes every automatic promotion from the order and applies alone
*   **Exclusive automatic promotion** — Blocks codes on the lines it covers. A code still applies to the other lines
* * *

**5. Staff codes**
* * *
Staff codes are always exclusive, so a staff code removes every automatic promotion from the order and applies alone. It gives 30% off and also applies to sale items. Each staff code is tied to one staff account.
* * *

### Limits on a line's discount
* * *
**6. Sale items**
* * *
*   **When** — A line is a sale item and the promotion or code has `applies_to_sale` switched off
*   **Then** — The promotion or code skips that line, and the line keeps its price
* * *

**7. The 50% cap**
* * *
The total discount on a line never goes past `50%` of the line price before promotions. The struck-through `compare_at` price does not count toward that base.

*   **When** — The automatic promotion plus the code would take more than 50% off a line
*   **Then** — promotions-service cuts the code's share until the line sits at exactly 50%
* * *

**8. Rounding and fixed-amount codes**
* * *
Every discount is worked out per line and rounded to `0.01` with `half up` rounding. The order discount is the sum of the line discounts.

A fixed-amount code is split across the eligible lines in proportion to their price. A cent left over from rounding goes to the most expensive line.
* * *

### Discounts and shipping
* * *
**9. Free-shipping threshold**
* * *
Free shipping is judged on the subtotal after every discount and before shipping, so a code can take an order back under the threshold.

*   **Euro markets** — Free at `€50` or more. Below that, standard shipping is €4.95
*   **UK** — Free at `£45` or more. Below that, standard shipping is £3.95
* * *

**10. Gift cards**
* * *
A `gift card` in the cart never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment rather than a promotion, and it comes off the total after discounts and shipping.
* * *

## Combinations and precedence
* * *

| Conditions | Outcome | Authority or status |
| ---| ---| --- |
| Two automatic promotions match one line | The bigger saving applies and the other is dropped | Current behavior |
| Automatic promotion and a non-exclusive code on the same line | Automatic promotion first, then the code on the remaining price | Current behavior |
| Customer enters a second code | The second code replaces the first | Current behavior |
| Exclusive code in the order | Every automatic promotion is removed and the code applies alone | Current behavior |
| Exclusive automatic promotion on a line and a code in the order | The code is blocked on that line and still applies to the other lines | Current behavior |
| Staff code in the order | Every automatic promotion is removed, 30% off applies, sale items included | Current behavior |
| Sale item and `applies_to_sale` switched off | The promotion or code skips the line | Current behavior |
| Automatic promotion plus code would pass 50% of the line price before promotions | The code's share is cut until the line sits at exactly 50% | Current behavior |
| Subtotal after discounts below €50 or £45 | Standard shipping of €4.95 or £3.95 applies | Current behavior |
| Order placed before 2026-05-01 with a percentage code and a free-shipping code | Both codes stay on the order, and a refund splits the discount across both | Retired material |
* * *

### Worked examples
* * *
#### Code on top of an automatic promotion, Netherlands
* * *
The cart holds stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. Linen tea towels, set of 3, cost €24.90 with no promotion. A cast iron casserole costs €89.00 with a `compare_at` price of €119.00, so it is a sale item. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

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
A €25.00 gift card and a bread bin at €32.00 are in the cart. Only the bread bin counts toward the threshold, so the order pays €4.95 shipping even though the cart holds €57.00.
* * *

### Retired behavior: two codes on one order
* * *
Status: Retired material — retired on 2026-05-01, code path removed from promotions-service on 2026-05-04

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and since then the one-code rule covers every order. This is kept so CS can explain older orders. Do not build on it.

Orders placed before `2026-05-01` can still show two codes in Admin. A refund on one of those orders splits the discount across both codes as it did at the time.
* * *

### Open questions
* * *
The Promotions rules note does not settle the cases below. Treat them as unknown until Merchandising confirms the behavior.

*   **Exclusive automatic promotion against a bigger saving** — An exclusive automatic promotion combines with nothing, and the bigger saving wins when two match one line. The note does not say which applies when a non-exclusive promotion on the same line saves more
*   **Two automatic promotions with the same saving** — No rule picks between them
*   **Automatic promotion above 50% on its own** — The cap cuts the code's share. The note does not say what happens when an automatic promotion alone would take more than 50% off a line
*   **Fixed-amount code meeting the cap** — When the cap cuts a fixed-amount code on one line, the note does not say whether the cut amount moves to other eligible lines or is lost
*   **Banner copy at exactly the threshold** — The banner reads `Free shipping on orders over €50` and `Free shipping on orders over £45`, while the rule ships free at exactly €50.00 or £45.00. promotions-service follows the rule. Whether the copy should change is an open question in the `PROMO` area
````

Export-equivalent path: `export/001 - doc-promotions-stacking.md`

HVR self-scan: 0 hard blockers. Fixed: rephrased "Web, iOS and Android" as "the storefront and the apps" to avoid a second triad in the Overview. Kept with reason: em dashes in `*   **Term** — definition` bullets and in the `Status:` labels (sanctioned ClickUp delimiter and status-label shape). The cart message is quoted exactly as the source writes it.

**Quality**
- Source safety: pass. Current rules, the retired two-code rule and the unsettled cases are labelled separately. The company context says the Promotions rules note governs how discounts combine, so I found no conflict about authority.
- Shape fit: pass. It's a behavior reference, because readers need to predict what discount an order gets.
- ClickUp layout: pass. It uses `* * *` dividers under every heading, `*   ` bullets and sentence-case headings. I left out spacer headings because this is a file export.
- Readability: pass. Each rule comes first and the worked example follows it.
- Voice: pass.

**Summary**
This reference covers the 10 current rules from the Promotions rules note, plus a table showing what happens when they combine and all four worked examples. I checked the arithmetic in the examples and it holds. The retired two-code rule is kept in its own section with its retirement dates.

**What I assumed or added (tell me to cut any of these)**
- **Audience:** I wrote it for CS agents, engineers and merchandisers, because the rules note names them.
- **Scope:** I included free shipping and gift cards because the discounted subtotal decides shipping.
- **Open questions:** I added this section myself. It lists gaps I found in the note, not rules the note states. One of them is that the banner says "over €50" but the rule gives free shipping at exactly €50.00. Colette may want to confirm or close these before the document is shared.
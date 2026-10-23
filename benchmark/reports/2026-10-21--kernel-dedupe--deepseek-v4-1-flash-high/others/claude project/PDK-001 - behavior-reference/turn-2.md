```markdown
# Discount codes and automatic promotions: how they stack

* * *
> **Source basis**
> *   **Current behavior** — Merchandising's promotions rules note governs every rule below, and states that promotions-service applies all of it
> *   **Current behavior** — The Fernhouse company context, for markets, currencies and shipping fees, and background only beyond that
> *   **Retired material** — The two-code rule retired on `2026-05-01`, kept so CS can explain orders placed before it
* * *

## Overview
* * *

promotions-service works out every discount and the storefront and apps show what it returns. This reference explains what happens when a code meets an automatic promotion on the same order: which applies first, which wins, where the cap cuts the discount and when shipping stops being free.

CS agents use it to explain an order whose discount looks wrong. Checkout engineers use it to predict the discount on a given cart and to keep the cart and checkout showing what promotions-service returns.

### Glossary
* * *

*   **`automatic promotion`** — A discount that applies without a code
*   **`discount code`** — A code the customer types in the cart or at checkout
*   **`sale item`** — A product whose `compare_at` price is higher than its price, shown struck through
*   **`subtotal`** — The sum of the lines after promotions and before shipping
*   **`exclusive`** — A flag on a promotion or code that stops it combining with anything
*   **`applies_to_sale`** — The switch that lets a code or promotion apply to sale items
*   **`compare_at`** — The reference price catalog-service holds above the current price
*   **`market`** — One of NL, BE, DE, FR or UK, which sets the currency and the shipping fees

### Where the discount is worked out
* * *

promotions-service owns every discount, and no client computes one. cart-service holds the line prices after automatic promotions, and web, iOS and Android show what promotions-service returns. A discount that looks wrong on one surface is a promotions-service question.

Every amount in this reference is the price the customer sees, which includes VAT at the market's rate.

## Behavior rules
* * *

### Codes and automatic promotions
* * *

**One code per order**

A customer can use `one discount code per order`. Entering a second code replaces the first, and the cart says so: "Only one code per order. Your new code has replaced the old one."

**Order of application**

`automatic promotions first`, then the code on the price that is left. Each line takes at most one automatic promotion. When two match the same line, the one with the bigger saving applies.

**Exclusive promotions and codes**

A promotion or code marked `exclusive` combines with nothing. An exclusive code removes every automatic promotion from the order and applies alone. An exclusive automatic promotion blocks codes on the lines it covers, and a code still applies to the other lines.

**Staff codes**

Staff codes start with `STAFF-` and are tied to one staff account. They are always exclusive, give 30% off and also apply to sale items.

### Line pricing
* * *

**Sale items**

A product is on sale when catalog-service holds a `compare_at` price above its current price. Codes and automatic promotions skip sale items unless the promotion has `applies_to_sale` switched on.

**The 50% line cap**

The total discount on a line never goes past `50%` of that line's price before promotions, and the struck-through `compare_at` price does not count. When the rules above would go past the cap, the code's share is cut until the line sits at exactly `50%`.

**Rounding**

Every discount is worked out per line and rounded to `0.01` with `half up` rounding. A fixed-amount code is split across the eligible lines in proportion to their price, and a cent left over from rounding goes to the most expensive line. The order discount is the sum of the line discounts.

### Shipping and payment
* * *

**Free shipping**

An order ships free when the subtotal, after every discount and before shipping, is at least `€50` in the euro markets or `£45` in the UK. Below that, standard shipping is `€4.95` or `£3.95`.

**Gift cards**

A `gift card` in the cart never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment, not a promotion, and comes off the total after discounts and shipping.

## Combinations and precedence
* * *

| Conditions | Outcome | Status |
|---|---|---|
| A second code entered while one is applied | The new code replaces the old one and the cart shows the message quoted in Codes and automatic promotions | Current behavior |
| Automatic promotion and a code on one line | The automatic applies first and the code takes its share of the reduced price | Current behavior |
| Two automatic promotions match one line | The bigger saving applies and the line takes no second promotion | Current behavior |
| `exclusive` code on an order carrying automatic promotions | Every automatic promotion is removed and the code applies alone | Current behavior |
| `exclusive` automatic promotion on a line, with a code entered | The code is blocked on that line and still applies to the rest | Current behavior |
| Sale item meets a code without `applies_to_sale` | The item is skipped and keeps its sale price | Current behavior |
| Discounts would take a line past `50%` of its pre-promotion price | The code's share is cut until the line sits at exactly `50%` | Current behavior |
| Subtotal after discounts reaches `€50` in the euro markets or `£45` in the UK | Shipping is free | Current behavior |
| Subtotal after discounts stays below the threshold | Standard shipping of `€4.95` or `£3.95` is charged | Current behavior |
| `gift card` in the cart | It takes no discount and is left out of the threshold | Current behavior |
| `gift card` used to pay | It comes off the total after discounts and shipping | Current behavior |

### Examples
* * *

#### Code on top of an automatic promotion, Netherlands
* * *

The cart holds stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off, linen tea towels, set of 3, at €24.90 with no promotion, and a cast iron casserole at €89.00. The casserole has a `compare_at` price of €119.00, so it is on sale. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
|---|---|---|---|---|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99 and leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74.

The subtotal is well over the threshold, so shipping is free.

#### The 50% cap
* * *

An oak serving board at €30.00 sits in a clearance promotion of 40% off, which leaves €18.00. Code HOME25 would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%.

The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00.

#### Threshold after discounts, UK
* * *

The subtotal is £48.00 before the code. Code WELCOME10 takes 10%, which is £4.80 and leaves £43.20. That is under £45, so standard shipping of £3.95 applies and the order total is £47.15.

#### Gift card in the cart, Netherlands
* * *

A €25.00 gift card and a bread bin at €32.00. Only the bread bin counts toward the threshold, so the order pays €4.95 shipping even though the cart holds €57.00.

### Boundaries and exceptions
* * *

Two combinations fall outside the settled rules above, and neither has a decision recorded. Treat each as a question for Merchandising rather than something to work out from the rules.

The first is a line whose only discount is an automatic promotion past `50%`. The cap cuts the code's share, so nothing describes what happens when there is no code to cut.

The second is an `exclusive` automatic promotion sitting beside a bigger non-exclusive one on the same line. Order of application gives the line to the bigger saving, while the exclusive rule says an exclusive combines with nothing.

The payment session and refunds fall outside this reference, apart from refunds on orders placed before `2026-05-01`.

## Retired rules
* * *

**Status: Retired material — retained for historical context**

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and since then the one-code rule covers every order.

Orders placed before `2026-05-01` can still show two codes in Admin, and a refund on one of them splits the discount across both codes as it did at the time. The code path was removed from promotions-service on `2026-05-04`.
```

Export-equivalent path: `export/001 - doc-discount-code-promotion-stacking.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the em dash survives only in the glossary definition bullets, the source-basis rows and the `Status: Retired material — retained for historical context` label, all sanctionable Doc Mode shapes; the cart message, the four worked examples and every figure in them stay verbatim.
Quality: every floor met | Kind: Doc, behavior reference | Energy: Standard | Source safety pass, Shape fit pass, ClickUp layout pass, Readability pass, Voice pass

The audience line now names CS and Checkout engineers, with the cart and checkout surfaced as the surfaces they work on, and every merchandiser and Admin setup thread is gone, including the glossary definition of an automatic promotion and the old out-of-scope line. The authority split is stated in the source basis: the rules note governs, the context doc supplies markets, currencies and shipping fees and nothing more. The retired two-code rule keeps its label and its refund consequence, since that is what CS needs it for.

### Open items
1. **Automatic promotion above the cap**
- **Situation:** The cap cuts the code's share, so a line discounted only by a larger automatic promotion has no stated outcome, which leaves one cart shape unpredictable.
- **Open:** It sits in Boundaries as unsettled. Strike it if Merchandising has a rule covering it.
2. **Exclusive against a bigger automatic promotion**
- **Situation:** Order of application gives the line to the bigger saving, while the exclusive rule says an exclusive combines with nothing.
- **Open:** Recorded as unsettled rather than choosing a winner. Name which governs and the section settles.
3. **VAT sentence**
- **Situation:** The line stating that amounts include VAT at the market's rate rests on the context doc alone, now designated background only.
- **Open:** Kept for CS explaining amounts. Say if it should come out with the rest of the background material.

Want me to change anything?
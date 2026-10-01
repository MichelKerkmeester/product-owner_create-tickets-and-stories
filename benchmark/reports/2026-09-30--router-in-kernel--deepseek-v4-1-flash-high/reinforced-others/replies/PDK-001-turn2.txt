# Fernhouse promotions: how discount codes and automatic promotions stack

```
# Fernhouse promotions: how discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — `fernhouse-promotions-rules.md`, owned by Colette, Promotions lead, Merchandising, and applied by `promotions-service`. It governs every rule below
> *   **Current behavior** — `fernhouse-context.md`, owned by Lotte, Head of Product. Background only, for the surfaces, services, markets and thresholds named here
> *   **Retired material** — the two-code rule in the promotions note, retired on `2026-05-01` and kept so CS can explain and refund orders placed before that date
* * *

## Overview
* * *
Every discount a Fernhouse customer sees is computed in `promotions-service`, and no surface computes one for itself. This reference explains what a cart carrying both an automatic promotion and a discount code does, so a reader can predict the discount on any cart: the order the two apply in, what an exclusive promotion or code does to the other, where sale items and the 50% line cap intervene, and how the result moves the free-shipping threshold.

CS agents use it when an order's discount looks wrong, and Checkout engineers use it to predict what a given cart will charge.
* * *
### Glossary
* * *
#### Terms and states
* * *
*   **`automatic promotion`** — A discount that applies without a code
*   **`discount code`** — A code the customer types in the cart or at checkout
*   **`exclusive`** — Marked on a promotion or a code that combines with nothing
*   **`sale item`** — A product whose `compare_at` price is higher than its price, shown struck through
*   **`applies_to_sale`** — The switch that lets a code or automatic promotion reach sale items
*   **`line`** — One product in the cart. A line with quantity 3 is 3 units
*   **`subtotal`** — The sum of the lines after promotions and before shipping
*   **Free-shipping threshold** — The subtotal at which shipping costs nothing, `€50` in the euro markets and `£45` in the UK
* * *
### Structure or context
* * *
`promotions-service` computes the automatic promotions, the discount codes and the free-shipping threshold, `cart-service` holds cart lines and their prices after automatic promotions, and `catalog-service` supplies the price and the `compare_at` price that decide whether a line is a sale item. Web, iOS and Android display those values and never compute one.

Amounts are in the market's currency: `EUR` in the Netherlands, Belgium, Germany and France, and `GBP` in the UK, where parcels also cross a customs border.
* * *
## Behavior rules
* * *
### Combining a code with an automatic promotion
* * *
**1. Order of application**
* * *
The sequence is `automatic promotions first`, then the discount code on the price that is left.
*   **When** — A line carries an automatic promotion and the order carries a code, and neither is exclusive
*   **Then** — The automatic promotion comes off first, and the code takes its percentage from the price that remains
*   **How** — Each line takes at most one automatic promotion. When two match the same line, the one with the bigger saving applies
*   **Status** — Current behavior
* * *

**2. One code per order**
* * *
A customer can use `one discount code per order`.
*   **When** — A customer enters a second code
*   **Then** — The second code replaces the first, and the cart says "Only one code per order. Your new code has replaced the old one."
*   **Status** — Current behavior
* * *

**3. Exclusive promotions and codes**
* * *
A promotion or code marked `exclusive` combines with nothing.
*   **When** — An exclusive code is applied to an order
*   **Then** — Every automatic promotion comes off the order and the code applies alone
*   **When** — An exclusive automatic promotion covers some lines and a code is entered
*   **Then** — The code is blocked on the lines the promotion covers and still applies to the other lines
*   **Status** — Current behavior
* * *

**4. Staff codes**
* * *
A staff code is tied to one staff account, so it belongs to a person rather than to an order.
*   **When** — A code starts with `STAFF-`
*   **Then** — It is always exclusive, gives 30% off and also applies to sale items
*   **Status** — Current behavior
* * *

### Sale items, the cap and rounding
* * *
**5. Sale items**
* * *
*   **When** — `catalog-service` holds a `compare_at` price above the product's current price, so the product is a sale item
*   **Then** — Codes and automatic promotions skip it, unless the promotion has `applies_to_sale` switched on
*   **Status** — Current behavior
* * *

**6. The 50% line cap**
* * *
*   **When** — The automatic promotion and the code together would take more than `50%` of a line's price before promotions
*   **Then** — The code's share is cut until the line sits at exactly 50%
*   **How** — The struck-through `compare_at` price does not count toward the cap
*   **Status** — Current behavior
* * *

**7. Rounding and splits**
* * *
*   **Per line** — Every discount is worked out per line and rounded to `0.01` with `half up` rounding
*   **Fixed-amount code** — Split across the eligible lines in proportion to their price, with a cent left over from rounding going to the most expensive line
*   **Order discount** — The sum of the line discounts
*   **Status** — Current behavior
* * *

### Free shipping and gift cards
* * *
**8. Free-shipping threshold**
* * *
The threshold is tested after every discount, so a code can take an order below it and add shipping back on.
*   **When** — The subtotal, after every discount and before shipping, is at least `€50` in the euro markets or `£45` in the UK
*   **Then** — The order ships free
*   **How** — Below the threshold, standard shipping is €4.95 in the euro markets or £3.95 in the UK
*   **Status** — Current behavior
* * *

**9. Gift cards**
* * *
*   **When** — A `gift card` sits in the cart
*   **Then** — It never takes a discount and does not count toward the free-shipping threshold
*   **How** — Paying with a gift card is a payment rather than a promotion, and comes off the total after discounts and shipping
*   **Status** — Current behavior
* * *

## Combinations and precedence
* * *

| Conditions | Outcome | Status |
| --- | --- | --- |
| An automatic promotion and a code on the same line, neither exclusive | The automatic promotion applies first, then the code on the price left | Current behavior |
| Two automatic promotions match the same line | The line takes one, the one with the bigger saving | Current behavior |
| A second code is entered on an order | It replaces the first code | Current behavior |
| An exclusive code is applied | Every automatic promotion is removed and the code applies alone | Current behavior |
| An exclusive automatic promotion covers some lines and a code is entered | The code is blocked on the covered lines and applies to the rest | Current behavior |
| A staff code is applied | It applies alone at 30% off and reaches sale items | Current behavior |
| A code or automatic promotion meets a sale item without `applies_to_sale` | The line is skipped | Current behavior |
| Combined discounts pass `50%` of a line's price before promotions | The code's share is cut until the line sits at exactly 50% | Current behavior |
| A discount takes the subtotal below the threshold | Standard shipping applies, €4.95 or £3.95 | Current behavior |
| A gift card sits in the cart | No discount on it, and no contribution to the threshold | Current behavior |
* * *
### Examples
* * *
#### Code on top of an automatic promotion, Netherlands
* * *
Cart: stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. Linen tea towels, set of 3, at €24.90, with no promotion. A cast iron casserole at €89.00 with a `compare_at` price of €119.00, so it is a sale item. Code `HOME15` gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
| --- | --- | --- | --- | --- |
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |
* * *
The plates take 20% first, which is €7.99 and leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is well over the threshold, so shipping is free.
* * *
#### The 50% cap
* * *
*   **Given** — An oak serving board at €30.00 sits in a clearance promotion of 40% off, which leaves €18.00
*   **When** — Code `HOME25` would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%
*   **Then** — The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00
* * *

#### Threshold after discounts, UK
* * *
*   **Given** — A subtotal of £48.00 before the code
*   **When** — Code `WELCOME10` takes 10%, which is £4.80 and leaves £43.20
*   **Then** — £43.20 is under £45, so standard shipping of £3.95 applies and the order total is £47.15
* * *

#### Gift card in the cart, Netherlands
* * *
*   **Given** — A €25.00 gift card and a bread bin at €32.00, so the cart holds €57.00
*   **When** — The order is priced
*   **Then** — Only the bread bin counts toward the threshold, so the order pays €4.95 shipping
* * *
### Boundaries and exceptions
* * *
*   **Clients never compute a discount** — Discounts are worked out in `promotions-service` only, and the storefront and apps show what it returns
*   **Banner wording differs from the rule** — The free-shipping banner reads `Free shipping on orders over €50` and `Free shipping on orders over £45`, while the threshold rule is at least €50 or £45. The banner lines are the fixed source strings for every locale, and the promotions note governs the threshold
* * *
## Retired behavior
* * *
**Status: Retired material — retired on `2026-05-01`, with the code path removed from `promotions-service` on `2026-05-04`**

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and since then the `one discount code per order` rule covers every order. Orders placed before that date can still show two codes in Admin, and a refund on one of them splits the discount across both codes as it did at the time. CS still refunds those orders, so this rule stays here for that work.

Do not build on this rule.
```

Export-equivalent path: `export/001 - doc-promotion-stacking.md`

Quality summary
- Source safety: pass — the promotions note governs every rule, the context file is labelled background only, and the retired two-code rule keeps its status label
- Shape fit: pass — Behavior reference retained, with the reader framed as predicting a discount on any cart
- ClickUp layout: pass — structure and dividers unchanged from the previous block
- Readability: pass — audience sentence names the two readers and what each does with it
- Voice: pass — no hard blockers

`HVR self-scan: 0 hard blockers. Fixed: none required. Kept with reason: the ClickUp definition delimiter in the glossary and rule bullets, and the `Status: ... — ...` label delimiter in the source basis and retired section.`

Five changes, no others. Audience is now CS agents and Checkout engineers with prediction as the stated job. The source basis says the rules note governs and the context file is background only. Merchant setup in Admin is gone from the Overview, the Structure or context section and the `automatic promotion` glossary entry, which now reads as a plain discount that applies without a code. The retired section names CS as the refunding party so the reason it is kept is on the page.

Two additions of mine are still in and still strikable: the banner-wording bullet, and the sentence at rule 8 that a code can push an order below the threshold. I kept `Merchandising` only as Colette's owning team in the source basis, since that is provenance rather than setup. No ClickUp connector in this session, so the block above is the artifact.
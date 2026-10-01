````markdown
# Fernhouse promotions: how codes and automatic promotions combine

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note owned by Colette, Promotions lead, in Merchandising, last edited 2026-09-02, governs every rule below. The Fernhouse company context is background on the surfaces, services and terms
> *   **Retired material** — The two-code rule, retired on 2026-05-01 and kept so CS can explain orders placed before it
* * *

## Overview
* * *
An order can carry a discount code and an automatic promotion at the same time, and this reference sets out the order they apply in, what each one does to a line, and the point where the discount stops. CS agents use it to explain a total a customer questions, and Checkout engineers use it to predict the discount on any cart from the rules alone.

The boundary is the order total. Every rule here runs in promotions-service, which returns the discount to the storefront, the iOS and Android apps and Admin, and those clients display the result without working out a discount themselves. Prices, `compare_at` prices and the sale status that follows from them come from catalog-service.

### Glossary
* * *
*   **`automatic promotion`** — A discount that applies without a code
*   **`discount code`** — A code the customer types in the cart or at checkout
*   **`exclusive`** — A marker on a promotion or a code that stops it combining with anything
*   **`sale item`** — A product whose `compare_at` price is above its current price, shown struck through
*   **`applies_to_sale`** — The switch a promotion needs before it reaches a sale item
*   **`subtotal`** — The sum of the lines after promotions and before shipping, and the figure the free-shipping threshold tests
* * *

### Structure or context
* * *
Promotions-service holds automatic promotions, discount codes and the free-shipping threshold, and it is the only place a discount is worked out. A customer enters a code in the cart or at checkout, on the storefront or in the apps. Every line then follows the same order.

```text
line price
  -> one automatic promotion, the bigger saving when two match the line
  -> the discount code on the price that is left
  -> the line's total discount capped at 50% of its price before promotions
  -> order subtotal, the sum of the lines after discounts and before shipping
  -> free-shipping threshold, tested on the subtotal
```
* * *

## Behavior rules
* * *
Each rule below names the condition that triggers it and the result the customer sees.

### Codes and application order
* * *

**1. One code per order**
* * *
A second code replaces the first rather than adding to it, so an order carries one code today.
*   **When** — A customer enters a code while another code sits on the order
*   **Then** — The new code replaces the old one, and the cart shows "Only one code per order. Your new code has replaced the old one."
*   **Status** — Current behavior
* * *

**2. Automatic promotions apply first**
* * *
The automatic promotion comes off the line first, and the code takes its share of the price that is left.
*   **When** — A line matches an automatic promotion and a code applies to the order
*   **Then** — The automatic promotion applies to the line, and the code works on the price after it
*   **Status** — Current behavior
* * *

**3. One automatic promotion per line**
* * *
A line takes at most one automatic promotion, however many of them match it.
*   **When** — Two automatic promotions match the same line
*   **Then** — The one with the bigger saving applies
*   **Status** — Current behavior
* * *

### Exclusive promotions and codes
* * *

**4. An exclusive code applies alone**
* * *
A code marked `exclusive` combines with nothing.
*   **When** — A customer enters an exclusive code
*   **Then** — Every automatic promotion leaves the order and the code applies alone
*   **Status** — Current behavior
* * *

**5. An exclusive automatic promotion blocks codes on its lines**
* * *
The exclusion reaches the lines the promotion covers and stops there.
*   **When** — An exclusive automatic promotion covers some lines and the order also carries a code
*   **Then** — The code is blocked on those lines, and it still applies to the lines the promotion does not cover
*   **Status** — Current behavior
* * *

**6. Staff codes are always exclusive**
* * *
A staff code starts with `STAFF-`, ties to one staff account, gives 30% off and applies to sale items.
*   **When** — A staff code is entered
*   **Then** — It removes every automatic promotion and applies alone, including on sale items
*   **Status** — Current behavior
* * *

### Sale items
* * *

**7. A sale item skips discounts unless the promotion opts in**
* * *
A product is on sale when catalog-service holds a `compare_at` price above its current price, and a sale line keeps that price.
*   **When** — A code or automatic promotion reaches a sale item without `applies_to_sale` switched on
*   **Then** — It skips the line, and a staff code is the one code that still reaches it
*   **Status** — Current behavior
* * *

### The line cap
* * *

**8. The discount on a line stops at 50%**
* * *
The cap is half of the line's price before promotions, and the struck-through `compare_at` price does not count toward it.
*   **When** — The automatic promotion and the code together would take more than 50% off a line
*   **Then** — The code's share is cut until the line sits at exactly 50%
*   **Status** — Current behavior
* * *

### Order total, shipping and gift cards
* * *

**9. Free shipping tests the subtotal after discounts**
* * *
The subtotal is the lines after every discount and before shipping, and it is the figure the threshold uses.
*   **When** — The subtotal is at least €50 in the euro markets or £45 in the UK
*   **Then** — The order ships free
*   **When** — The subtotal falls below the threshold
*   **Then** — Standard shipping applies at €4.95 or £3.95
*   **Status** — Current behavior
* * *

**10. A gift card is a payment, not a promotion**
* * *
A gift card is money in the cart, so the discount rules pass it by.
*   **When** — A gift card sits in the cart
*   **Then** — It takes no discount and does not count toward the free-shipping threshold, and it comes off the total after discounts and shipping
*   **Status** — Current behavior
* * *

### Rounding
* * *

**11. Every discount is worked out and rounded per line**
* * *
The order discount is the sum of the line discounts, and each line is rounded to `0.01` with half-up rounding.
*   **When** — A code carries a fixed amount rather than a percentage
*   **Then** — The amount splits across the eligible lines in proportion to their price, and a cent left over from rounding goes to the most expensive line
*   **Status** — Current behavior
* * *

## Combinations and precedence
* * *
The table records how the common combinations resolve, so nobody has to guess which rule wins.

| Conditions | Outcome | Status |
| ---| ---| --- |
| A code entered while another code is on the order | The new code replaces the old one | Current behavior |
| An automatic promotion and a code on one line | The automatic promotion first, then the code on the price left | Current behavior |
| Two automatic promotions on one line | The bigger saving applies | Current behavior |
| An exclusive code with automatic promotions on the order | The code applies alone and the automatic promotions leave | Current behavior |
| An exclusive automatic promotion with a code | The code is blocked on the covered lines and applies to the rest | Current behavior |
| A code on a sale item without `applies_to_sale` | The line keeps its sale price and the code skips it | Current behavior |
| A promotion and a code reaching past 50% of a line | The code's share is cut so the line lands at exactly 50% | Current behavior |
| A subtotal after discounts below the threshold | Standard shipping applies at €4.95 or £3.95 | Current behavior |
| A gift card in the cart | No discount and no effect on the threshold | Current behavior |
| Two codes on an order placed before 2026-05-01 | One percentage code and one free-shipping code could combine | Retired material |

### Retired rule: two codes on one order
* * *
**Status:** Retired material — retained so CS can explain orders placed before the change

Until 2026-05-01 a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and the one-code rule in rule 1 has covered every order since. Orders placed before 2026-05-01 can still show two codes in Admin, and a refund on one of them splits the discount across both codes as it did at the time. The code path was removed from promotions-service on 2026-05-04, so nothing new builds on this rule.
* * *

### Examples
* * *

#### Code on top of an automatic promotion, Netherlands
* * *
Cart: stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. Linen tea towels, set of 3, at €24.90 with no promotion. A cast iron casserole at €89.00 with a `compare_at` price of €119.00, so it is on sale. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, €7.99, which leaves €31.96, and the code takes 15% of that, €4.794, rounded to €4.79. The towels take 15% of €24.90, €3.735, rounded half up to €3.74. The subtotal is over the threshold, so shipping is free.
* * *

#### The 50% cap
* * *
*   **Given** — An oak serving board at €30.00 in a clearance promotion of 40% off, which leaves €18.00, with code HOME25 taking 25%
*   **When** — The two discounts together would reach €16.50, or 55% of €30.00
*   **Then** — The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00
* * *

#### Threshold after discounts, UK
* * *
*   **Given** — A subtotal of £48.00 before the code, with WELCOME10 taking 10%
*   **When** — The £4.80 discount leaves £43.20, which is under the £45 threshold
*   **Then** — Standard shipping of £3.95 applies and the order total is £47.15
* * *

#### Gift card in the cart, Netherlands
* * *
*   **Given** — A €25.00 gift card and a bread bin at €32.00 in the same cart
*   **When** — Only the bread bin counts toward the threshold
*   **Then** — The order pays €4.95 shipping even though the cart holds €57.00
* * *

### Boundaries and exceptions
* * *
*   **Only orders placed before 2026-05-01 carry two codes** — Every order since runs the one-code rule, so a second code seen on a recent order is a case to raise rather than a second combination
*   **The threshold rule against the banner copy** — Shipping is free once the subtotal reaches €50 or £45, while the banner on web and above the cart in the apps reads "Free shipping on orders over €50". An order sitting exactly on the threshold meets the rule, which is the figure promotions-service applies
*   **Clients never work out a discount** — The storefront, the apps and Admin show what promotions-service returns, so a total anywhere in the product comes from the rules above
````

Export-equivalent path: `export/001 - doc-promotion-stacking.md`

Quality summary
*   Source safety — pass. The rules note governs the behavior and the context doc supplies background only, stated in the source-basis block. The two-code rule carries its retired label in three places: the source basis, the precedence table and its own subsection with the dates and the refund behaviour.
*   Shape fit — pass. Still a behavior reference: CS can explain a total, and a Checkout engineer can take the rules and predict the discount on any cart.
*   ClickUp layout — pass. Dividers after every content heading, `*   ` bullets, definition and status labels, no spacer headings in the file export.
*   Readability — pass. Takeaway-first sections, tables where rows compare, each example next to the rules it shows.
*   Voice — pass.

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the em dash inside the ClickUp definition bullets, the `Status:` label on the retired block and the status-basis bullets, all Doc Mode exemptions, plus the cart copy "Only one code per order. Your new code has replaced the old one." carried verbatim.`

Assumptions you can correct: I kept Admin in the list of surfaces that display the returned discount, because CS reads order codes there, and removed the steps for creating a promotion in Admin. The retired material sits as its own labelled subsection before the examples, so a CS agent refunding an older order meets it before the worked cases. The threshold reading stays flagged as a boundary, since the rule and the banner copy differ at exactly €50.

Next step: if you want the threshold flag turned into work rather than a note, say which side should move and I can draft it as a task.
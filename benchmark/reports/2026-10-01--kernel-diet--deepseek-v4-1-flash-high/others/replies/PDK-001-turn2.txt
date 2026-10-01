```markdown
<!-- Product Owner · Doc Mode · Behavior reference · Doc Templates v0.109 -->

# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Merchandising note `context/fernhouse-promotions-rules.md`, which governs the rules below, last edited 2026-09-02
> *   **Retired material** — The two-code rule the same note retired on 2026-05-01, kept so CS can explain and refund earlier orders
> *   **Background only** — `context/fernhouse-context.md`, for service ownership, market thresholds and shipping fees
* * *

## Overview
* * *
An order can carry two discounts: an automatic promotion that applies on its own, and a discount code the customer types in the cart or at checkout. Both are worked out in `promotions-service`, and the storefront and the apps only show what it returns.

CS agents and Checkout engineers read this to predict the discount on any cart, whether to explain an order back to a customer or to check what `promotions-service` should return.

Everything here follows from the order of application. Automatic promotions run first, a code applies to the price that is left, and the line cap decides what survives.
* * *

### Terminology
* * *
*   **`automatic promotion`** — A discount that applies to an order with no code
*   **`discount code`** — A code the customer types in the cart or at checkout
*   **`sale item`** — A product whose `compare_at` price is higher than its price, shown struck through
*   **`subtotal`** — The sum of the lines after every discount and before shipping
*   **`exclusive`** — A flag on a promotion or code that stops it combining with anything
* * *

### Where the rules run
* * *
`catalog-service` holds the `compare_at` price that makes a product a sale item. `cart-service` holds the line prices after automatic promotions, which also show on product pages. `promotions-service` applies every rule below.
* * *

## Behavior rules
* * *
### How a code and a promotion combine
* * *
**One code per order.** A customer can use `one discount code per order`, and entering a second code replaces the first. The cart says "Only one code per order. Your new code has replaced the old one."

**Automatic promotions first.** Automatic promotions run `automatic promotions first`, the code applies to the price that is left, and each line takes at most one automatic promotion. Where two match the same line, the bigger saving applies.

**Exclusive stops everything.** A promotion or code marked `exclusive` combines with nothing. An exclusive code removes every automatic promotion from the order and applies alone, while an exclusive automatic promotion blocks codes on the lines it covers and leaves a code working on the others.

**Staff codes.** A code starting with `STAFF-` is tied to one staff account, is always `exclusive`, gives 30% off and applies to sale items.

**Sale items.** A product is on sale while `catalog-service` holds a `compare_at` price above its price. Codes and automatic promotions skip sale items unless that discount has `applies_to_sale` switched on.

**Gift cards.** A `gift card` in the cart never takes a discount and does not count toward the free-shipping threshold. It is a payment rather than a promotion, so it comes off the total after discounts and shipping.
* * *

### What limits the total
* * *
**The 50% line cap.** The total discount on a line never goes past `50%` of that line's price before promotions, and the struck-through `compare_at` price does not count. Where the rules above would pass the cap, the code's share is cut until the line sits at exactly 50%.

**Free shipping.** An order ships free when the subtotal, after every discount and before shipping, is at least `€50` in the euro markets or `£45` in the UK. Below that, standard shipping is €4.95 or £3.95.

**Rounding.** Every discount is worked out per line and rounded to `0.01` with `half up` rounding. A fixed-amount code is split across the eligible lines in proportion to their price, and a cent left over from rounding goes to the most expensive line. The order discount is the sum of the line discounts.
* * *

### Retired behavior
* * *
**Status: Retired material — retained for historical context**

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and `one discount code per order` has covered every order since. The code path left `promotions-service` on 2026-05-04.

Orders placed before that date can still show two codes in Admin, and CS still refunds those orders, so a refund on one code splits the discount across both as it did at the time. Do not build on this rule.
* * *

## Combinations and precedence
* * *
The rules above meet on the same order, and the outcome depends on which of them reaches a line first. Every outcome below is current behavior in `promotions-service`.

| Conditions | Outcome |
| ---| --- |
| An exclusive code with automatic promotions on the order | The code applies alone and every automatic promotion is removed |
| An exclusive automatic promotion with a code | The code applies to the lines the promotion does not cover |
| Two automatic promotions matching one line | The bigger saving applies |
| A second code entered in the cart | The new code replaces the first |
| Discounts that would pass the `50%` cap on a line | The code's share is cut so the line sits at exactly `50%` |
* * *

### Examples
* * *
#### Code on top of an automatic promotion, Netherlands
* * *
*   **Given** — Stoneware dinner plates at €39.95 under a Tableware 20% off promotion, linen tea towels at €24.90 with none, and a cast iron casserole at €89.00 with a `compare_at` price of €119.00
*   **When** — Code HOME15, 15% off with `applies_to_sale` off, goes in the cart
*   **Then** — The plates take €7.99 then €4.79 and end at €27.17, the towels take €3.74 and end at €21.16, the casserole stays at €89.00, and the €137.33 subtotal ships free
* * *

#### The 50% cap
* * *
*   **Given** — An oak serving board at €30.00 under a clearance promotion of 40% off, which leaves €18.00
*   **When** — Code HOME25 would take 25% of €18.00, which is €4.50
*   **Then** — The line discount would reach 55%, so the cap allows €15.00, the code gives €3.00 and the line ends at €15.00
* * *

#### Threshold after discounts, UK
* * *
*   **Given** — A £48.00 subtotal before the code
*   **When** — Code WELCOME10 takes 10%, which is £4.80, and leaves £43.20
*   **Then** — £43.20 is under £45, so standard shipping of £3.95 applies and the order total is £47.15
* * *

#### Gift card in the cart, Netherlands
* * *
*   **Given** — A €25.00 gift card and a bread bin at €32.00
*   **When** — The subtotal and the free-shipping threshold are worked out
*   **Then** — Only the bread bin counts, so the order pays €4.95 shipping even though the cart holds €57.00
* * *

### Boundaries and exceptions
* * *
*   **Threshold wording** — The rule reads `at least €50`, the banner reads `over €50`, so the exact threshold subtotal is the one case they treat differently
*   **No client-side discounts** — The storefront and the apps show what `promotions-service` returns and work out no discount themselves
*   **Refunds today** — How a refund reduces a discount already taken on a current order has no rule in the promotions note
```

Export-equivalent path: `export/001 - doc-discount-code-and-promotion-stacking.md` (the same document and label you just reviewed, revised in place)

- Source safety: pass — the rules note governs, the context doc sits under `Background only`, and the two-code rule keeps its retired label with its dates
- Shape fit: pass — Behavior reference, aimed at predicting the discount on any cart
- ClickUp layout: pass — `* * *` after every heading, `*   ` bullets, sentence-case headings, no hyphen bullets
- Readability: pass — takeaway first, one idea per paragraph, values exact
- Voice: pass — no hard blockers

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: em dashes only in the definition bullets and the `Status: Retired material — ...` label, both sanctioned delimiters; backticked source literals such as `one discount code per order`, `applies_to_sale` and `half up` preserved; the cart message carried word for word in straight quotes.

What changed: the audience line now names CS agents and Checkout engineers and the prediction job, the source basis records that the rules note governs while the context doc is background only, the `automatic promotion` definition no longer mentions Admin setup, and the retired section says plainly that CS still refunds those orders and that a refund splits across both codes.

Four things in here are still mine rather than the note's, so strike any you do not want: the Terminology block, the service-ownership note under "Where the rules run", the banner wording boundary, and the refunds boundary scoped to current orders.

Next step: say the word and I will cut any of those four, or widen the retired section if CS needs more of the old two-code refund detail.
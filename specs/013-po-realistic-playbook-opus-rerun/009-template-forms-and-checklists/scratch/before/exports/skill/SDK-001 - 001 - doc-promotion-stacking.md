# How discount codes and automatic promotions stack

* * *
> **Source basis**
> *   **Current behavior** — The Promotions rules note, owned by Colette, Promotions lead in Merchandising, last edited 2026-09-02. promotions-service applies every current rule in it
> *   **Retired material** — Two codes on one order, retired on 2026-05-01 and kept because CS still refunds orders placed under it
> *   **Unknown** — Six combinations the note does not settle, under Open questions
* * *

## Overview
* * *

This reference explains what promotions-service does when discount codes and automatic promotions meet in one cart, through to shipping. CS agents use it to explain a total, and Checkout engineers to check a cart. Promotion setup is out of scope.
* * *

### Glossary
* * *

*   **Automatic promotion** — A discount applied without a code
*   **Discount code** — A code the customer enters on the order, staff codes included
*   **`exclusive`** — A flag meaning a promotion or code combines with nothing, per rule 3
*   **Sale item** — A product whose `compare_at` price in catalog-service is above its current price, shown struck through
*   **`applies_to_sale`** — A switch that lets a promotion or code reach sale items
*   **Staff code** — A code that starts with `STAFF-`, tied to one staff account
*   **Subtotal** — The lines after every discount and before shipping
* * *

### Where the calculation runs
* * *

promotions-service applies every rule here, and the storefront and apps show its result. The rules note was written from its behavior with the Checkout team, and sale status is its one outside input, from catalog-service.

The block below shows the note's order for one line.

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

Status: Current behavior — per the Promotions rules note
* * *

### Which discounts reach a line
* * *

**1. One code per order**
* * *

*   **When** — A customer enters a second code
*   **Then** — It replaces the first, and the cart shows `Only one code per order. Your new code has replaced the old one.`
* * *

**2. Automatic promotions first, then the code**
* * *

*   **When** — A line matches an automatic promotion and a code
*   **Then** — The promotion comes off first, then the code
*   **When** — Two automatic promotions match one line
*   **Then** — Only the bigger saving applies
* * *

**3. Exclusive promotions and codes**
* * *

*   **When** — The customer enters an exclusive code
*   **Then** — Every automatic promotion leaves the order and the code applies alone
*   **When** — An exclusive automatic promotion covers some lines and a code is entered
*   **Then** — The code skips the covered lines and applies to the others
* * *

**4. Staff codes**
* * *

*   **When** — A code starting with `STAFF-` is used
*   **Then** — It is always exclusive, gives 30% off and reaches sale items
* * *

**5. Sale items**
* * *

*   **When** — A line holds a sale item
*   **Then** — Codes and promotions skip it unless `applies_to_sale` is on, and staff codes always reach it
* * *

### How far a discount can go
* * *

**6. The 50% cap**
* * *

*   **When** — The promotion and code together would take more than `50%` of the line's price
*   **Then** — The code's share is cut until the line sits at exactly 50%
*   **How** — The base is the pre-promotion price, never the struck-through `compare_at` price
* * *

**7. Rounding and fixed-amount codes**
* * *

The order discount is the sum of the rounded line discounts.

*   **When** — Any discount is calculated
*   **Then** — Each line discount is rounded to `0.01`, `half up`
*   **When** — The code is a fixed amount
*   **Then** — It is split across eligible lines by price, and a leftover cent goes to the priciest line
* * *

### What the stack decides afterwards
* * *

**8. Free-shipping threshold**
* * *

*   **When** — The subtotal is at least `€50`, or `£45` in the UK
*   **Then** — The order ships free
*   **When** — The subtotal is below that
*   **Then** — Shipping is €4.95, or £3.95 in the UK
* * *

**9. Gift cards**
* * *

A gift card is outside the stack on both sides: as a cart item it takes no discount, and as a payment it is not a promotion.

*   **When** — A gift card is in the cart
*   **Then** — It takes no discount and does not count toward the threshold
*   **When** — A customer pays with a gift card
*   **Then** — It comes off the final total
* * *

## Combinations and precedence
* * *

| Conditions | Outcome | Status |
| ---| ---| --- |
| Promotion and code on one line, neither exclusive | Promotion first, then the code | Current behavior, rule 2 |
| Two automatic promotions match one line | The bigger saving applies | Current behavior, rule 2 |
| Customer enters a second code | It replaces the first | Current behavior, rule 1 |
| Exclusive code with automatic promotions | All promotions removed, the code applies alone | Current behavior, rule 3 |
| Exclusive promotion on some lines, plus a code | The code skips the covered lines | Current behavior, rule 3 |
| Staff code on a sale item | 30% off, and no automatic promotion in the order | Current behavior, rules 3 and 4 |
| Sale item, `applies_to_sale` off | Skipped | Current behavior, rule 5 |
| Promotion and code above 50% | The code's share is cut to 50% | Current behavior, rule 6 |
| Gift card in the cart with a code | No discount, not counted toward the threshold | Current behavior, rule 8 |
| Exclusive code on a line an exclusive promotion covers | Not stated | Unknown |
| Percentage plus free-shipping code, placed before 2026-05-01 | Both applied | Retired material |
| Refund on a two-code order | Split across both codes | Retired material, refund behavior for pre-2026-05-01 orders |
* * *

### Examples
* * *

The examples use the rules note's figures.

#### Code on top of an automatic promotion, Netherlands
* * *

The cart has stoneware dinner plates, set of 4, at €39.95 with Tableware 20% off, linen tea towels, set of 3, at €24.90, and a cast iron casserole at €89.00, a sale item with `compare_at` €119.00. Code HOME15 gives 15% off with `applies_to_sale` off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates lose 20%, €7.99, leaving €31.96, then 15% of that, €4.794, rounded to €4.79. The towels lose 15% of €24.90, €3.735, rounded half up to €3.74, and shipping is free.
* * *

#### The 50% cap
* * *

*   **Given** — An oak serving board at €30.00 with 40% clearance off, leaving €18.00
*   **When** — HOME25 would take 25% of €18.00, €4.50, a total of €16.50 or 55%
*   **Then** — The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00
* * *

#### Threshold after discounts, UK
* * *

*   **Given** — A subtotal of £48.00 before the code
*   **When** — WELCOME10 takes 10%, £4.80, leaving £43.20
*   **Then** — That is under £45, so £3.95 shipping applies and the total is £47.15
* * *

#### Gift card in the cart, Netherlands
* * *

*   **Given** — A €25.00 gift card and a bread bin at €32.00
*   **When** — The threshold is checked
*   **Then** — Only the bread bin counts, so €4.95 shipping applies although the cart holds €57.00
* * *

## Boundaries and history
* * *

### Open questions
* * *

Status: Unverified — the Promotions rules note does not settle these cases

Colette, who owns the note, can add the answers.

*   **Two exclusives on one line** — Which wins, an exclusive code or an exclusive automatic promotion
*   **Exclusive against bigger saving** — Whether an exclusive promotion with the smaller saving still takes the line and blocks the code
*   **An exclusive code that reaches no line** — Whether it still removes promotions, as with `applies_to_sale` off on an all-sale cart
*   **An automatic promotion above 50% on its own** — What happens, with or without a code, as the cap only cuts the code
*   **Rounding at the cap** — Which way it rounds, since half of €39.95 is €19.975
*   **The price a fixed-amount code is split by** — Before or after the automatic promotion
* * *

### Free-shipping banner wording
* * *

An order at exactly €50.00 or £45.00 ships free, because rule 8 says "at least". The banner reads `Free shipping on orders over €50` and `Free shipping on orders over £45`, and neither source says whether the difference is intended. The rules note governs the order.
* * *

### Retired rule: two codes on one order
* * *

Status: Retired material — retired on 2026-05-01, kept because CS still refunds orders placed under it

Until 2026-05-01 a customer could combine one percentage code with one free-shipping code. Free-shipping codes stopped that day, and the one-code rule has covered every order since. The code path left promotions-service on 2026-05-04.

Those orders can still show two codes in Admin, and a refund splits across both. Nothing new should build on this rule.
* * *

### Related references
* * *

*   [Promotions rules](../context/fernhouse-promotions-rules.md), the governing source
*   [Fernhouse company context](../context/fernhouse-context.md), markets, surfaces and services

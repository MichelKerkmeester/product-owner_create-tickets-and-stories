# Promotions rules

Owned by Colette, Promotions lead, Merchandising. Kept in the Merchandising space as the note CS, engineering and merchandisers check when a discount looks wrong. Last edited 2026-09-02. promotions-service applies everything below, and the storefront and the apps show what it returns.

## Current rules

1. **One code.** A customer can use `one discount code per order`. Entering a second code replaces the first, and the cart says so: "Only one code per order. Your new code has replaced the old one."
2. **Order of application.** `automatic promotions first`, then the discount code on the price that is left. Each line takes at most one automatic promotion. When two match the same line, the one with the bigger saving applies.
3. **Exclusive.** A promotion or code marked `exclusive` combines with nothing. An exclusive code removes every automatic promotion from the order and applies alone. An exclusive automatic promotion blocks codes on the lines it covers, and a code still applies to the other lines.
4. **Staff codes.** Staff codes start with `STAFF-` and are tied to one staff account. They are always exclusive, give 30% off and also apply to sale items.
5. **Sale items.** A product is on sale when catalog-service holds a `compare_at` price above its current price. Codes and automatic promotions skip sale items unless the promotion has `applies_to_sale` switched on.
6. **Cap.** The total discount on a line never goes past `50%` of that line's price before promotions. The struck-through `compare_at` price does not count. When the rules above would go past the cap, the code's share is cut until the line sits at exactly 50%.
7. **Free shipping.** An order ships free when the subtotal, after every discount and before shipping, is at least `€50` in the euro markets or `£45` in the UK. Below that, standard shipping is €4.95 or £3.95.
8. **Gift cards.** A `gift card` in the cart never takes a discount and does not count toward the free-shipping threshold. Paying with a gift card is a payment, not a promotion, and comes off the total after discounts and shipping.
9. **Rounding.** Every discount is worked out per line and rounded to `0.01` with `half up` rounding. A fixed-amount code is split across the eligible lines in proportion to their price, and a cent left over from rounding goes to the most expensive line. The order discount is the sum of the line discounts.

## Worked examples

**Code on top of an automatic promotion, Netherlands**

Cart: stoneware dinner plates, set of 4, at €39.95 with the automatic promotion Tableware 20% off. Linen tea towels, set of 3, at €24.90 with no promotion. A cast iron casserole at €89.00 with a `compare_at` price of €119.00, so it is on sale. Code HOME15 gives 15% off and has `applies_to_sale` switched off.

| Line | Price | Automatic | Code | Line total |
|------|-------|-----------|------|------------|
| Dinner plates | €39.95 | minus €7.99 | minus €4.79 | €27.17 |
| Tea towels | €24.90 | none | minus €3.74 | €21.16 |
| Casserole | €89.00 | none | skipped, sale item | €89.00 |
| Subtotal | | | | €137.33 |

The plates take 20% first, which is €7.99 and leaves €31.96. The code then takes 15% of €31.96, which is €4.794 and rounds to €4.79. The towels take 15% of €24.90, which is €3.735 and rounds half up to €3.74. The subtotal is well over the threshold, so shipping is free.

**The 50% cap**

An oak serving board at €30.00 sits in a clearance promotion of 40% off, which leaves €18.00. Code HOME25 would take 25% of €18.00, which is €4.50, for a total discount of €16.50 or 55%. The cap allows €15.00, so the code gives €3.00 and the line ends at €15.00.

**Threshold after discounts, UK**

The subtotal is £48.00 before the code. Code WELCOME10 takes 10%, which is £4.80 and leaves £43.20. That is under £45, so standard shipping of £3.95 applies and the order total is £47.15.

**Gift card in the cart, Netherlands**

A €25.00 gift card and a bread bin at €32.00. Only the bread bin counts toward the threshold, so the order pays €4.95 shipping even though the cart holds €57.00.

## Retired rules

Kept so CS can explain orders placed before the change. Do not build on these.

**Two codes on one order, `retired`**

Until `2026-05-01` a customer could combine one percentage code with one free-shipping code on the same order. Free-shipping codes stopped on that date, and since then the one-code rule covers every order. Orders placed before `2026-05-01` can still show two codes in Admin, and a refund on one of them splits the discount across both codes as it did at the time.

Status: retired on 2026-05-01. The code path was removed from promotions-service on 2026-05-04.

## Change log

| Date | Change | By |
|------|--------|----|
| 2026-09-02 | Added the gift card example after a CS question | Colette |
| 2026-06-10 | Wrote down how a fixed-amount code is split across lines, which promotions-service already did | Colette |
| 2026-05-01 | Two codes on one order retired, one code per order for every order | Colette |
| 2026-03-12 | First version, written from promotions-service's behavior with the Checkout team | Colette |

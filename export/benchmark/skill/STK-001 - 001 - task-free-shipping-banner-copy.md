# FS - PROMO - Shorten the free-shipping banner copy

### About

---

The free-shipping banner sits at the top of every web page and above the cart in the iOS and Android apps. It reads `Free shipping on orders over €50` in the four euro markets and `Free shipping on orders over £45` in the UK. On small phones that copy wraps to two lines, which pushes the page or cart content down and splits the one message customers need to read at a glance.

This task shortens the copy so the banner fits on one line. The thresholds stay the same. Copy is written in English first and then translated, so the two English lines are the source strings for every locale, and the translations have to follow the new wording.

### Requirements

---

1.  **New English source copy**

---

The English lines change in every market and on every surface that shows the banner. Customers who pick English in the language switcher see the en-GB copy with their own market's currency, so a Dutch customer reading in English sees the euro line.

**Checklist**

- [ ] The euro markets (NL, BE, DE, FR) show `Free shipping over €50` in English
- [ ] The UK shows `Free shipping over £45`
- [ ] The change applies on Web, iOS and Android
- [ ] The threshold amounts stay €50 and £45, and only the banner wording changes
- [ ] On the small phone widths where the current copy wraps, the new English copy fits on one line on Web, iOS and Android

2.  **Translated locales**

---

Because the English lines are the source strings, each translation is updated to match the shorter wording rather than left on the old sentence.

**Checklist**

- [ ] The banner copy is updated in `nl-NL`, `nl-BE`, `fr-BE`, `de-DE` and `fr-FR` to match the new English wording
- [ ] Amounts keep the locale formatting the storefront already applies
- [ ] Each translated banner is checked on the same small phone widths, and any locale that still wraps is reported back to Product before release

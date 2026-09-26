# FS - PROMO - Shorten the free-shipping banner copy

## About

---

The free-shipping banner tops every web page and the cart in the iOS and Android apps. It reads `Free shipping on orders over €50` in the four euro markets and `Free shipping on orders over £45` in the UK. On small phones it wraps to two lines, pushing content down.

This task shortens it to one line. English is the source for every locale, so translations follow the new wording.

### Requirements

---

1.  **New English source copy**

---

Customers reading English see the en-GB copy in their market's currency, so a Dutch customer sees the euro line.

**Checklist**

- [] The euro markets (NL, BE, DE, FR) show `Free shipping over €50` in English
- [] The UK shows `Free shipping over £45`
- [] The change applies on Web, iOS and Android
- [] Only the wording changes, and the thresholds stay €50 and £45
- [] The new English copy fits one line on Web, iOS and Android at the small phone widths where the current copy wraps

2.  **Translated locales**

---

Each translation moves to the shorter wording.

**Checklist**

- [] `nl-NL`, `nl-BE`, `fr-BE`, `de-DE` and `fr-FR` match the new English wording
- [] Amounts keep the storefront's current locale formatting
- [] Each locale is checked at the same widths, and any that still wraps goes back to Product before release

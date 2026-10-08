# FE - Web - PROMO - Free shipping banner copy

## About

---

The free-shipping banner sits at the top of every web page and above the cart in the Fernhouse apps, and it shows the threshold for the customer's market. Today it reads `Free shipping on orders over €50` in the euro markets and `Free shipping on orders over £45` in the UK. On small phones that copy wraps to two lines.

This task changes the banner to `Free shipping over €50` and `Free shipping over £45`. The shorter line keeps the same threshold and fits on one line. The English lines are the source strings for every locale, so the translations change with them.

### Requirements

---

1.  **Banner copy**

---

The banner shows the shorter English line in every market, with the threshold amount unchanged. Web and both apps carry the same wording.

**Checklist**

- [] On web, the banner reads `Free shipping over €50` in NL, BE, DE and FR and `Free shipping over £45` in the UK
- [] In the iOS and Android apps, the banner above the cart reads the same wording for each market
- [] The amounts stay €50 in the euro markets and £45 in the UK, matching the threshold promotions-service returns
- [] The wording `Free shipping on orders over €50` and `Free shipping on orders over £45` appears in no market

2.  **Translations**

---

Each locale carries its own translation of the new English line, so the translated banner moves with the source. The English copy shown through the language switcher uses the same lines.

**Checklist**

- [] Each locale shows its translation of the new line for the market's threshold, for nl-NL, nl-BE, fr-BE, de-DE, fr-FR and en-GB
- [] No locale shows the old wording once the change is live

3.  **Small-phone fit**

---

Translated lines can run longer than the English line, so each locale is checked on a small phone, not only the English line.

**Checklist**

- [] On a small phone, the web banner shows its text on one line in every market and locale
- [] On a small phone, the banner in the iOS and Android apps shows its text on one line in every market and locale

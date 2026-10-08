```markdown
# FE - PROMO - Free-shipping banner copy

## About

---

The free-shipping banner sits at the top of every web page and above the cart in the iOS and Android apps. It shows the free-shipping threshold for the market. On small phones the current copy, `Free shipping on orders over €50` and `Free shipping on orders over £45`, wraps to two lines. The shorter copy below is meant to keep each banner on one line.

### Requirements

---

**Banner copy**

---

The banner shows the new threshold copy on every surface that carries it. The two English lines are the source strings for every locale.

**Checklist**

- [] The English banner for the four euro markets reads `Free shipping over €50`
- [] The English banner for the UK reads `Free shipping over £45`
- [] The web banner at the top of every page shows the new copy
- [] The banner above the cart in the iOS and Android apps shows the new copy
- [] The English banner fits on one line on small phones
```

Export-equivalent path: `export/NNN - task-free-shipping-banner-copy.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the two supplied price lines, carried verbatim.

Quality status: ready for review. Requirements state WHAT and WHY only, and the artifact has no open gate.

Assumptions to strike or correct:

- **Title segment.** I used `FE - PROMO` with no surface, because the banner spans web, iOS and Android. If you want a single surface or `FS`, tell me.
- **Owning discipline.** The context file doesn't say whether the banner copy is a client string or comes from `promotions-service`. I assumed client work (`FE`). If it comes from the service, the ticket becomes `BE` or `FS`.
- **Small phones.** The source gives no device width, so the one-line check can't name a size yet. Send the target width and I'll make that checklist item testable.

Translations are outside this ticket. The request supplies English copy only, so the one-line check covers English. The German and French strings may still wrap and need their own check.

`context/fernhouse-context.md` still quotes the old copy on line 20. Lotte's team owns that file, so it should be updated when this ships.
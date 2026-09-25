```markdown
# FE - PROMO - Shorten the free-shipping banner copy

### About

---

The free-shipping banner wraps to two lines on small phones. It sits at the top of every web page and above the cart in the iOS and Android apps. Shorter copy keeps the offer on one line, so the banner takes less space above the cart. Only the copy changes. The threshold amounts stay the same.

### Requirements

---

**Replace the banner copy in every market**

---

The two English lines are the source strings for every locale, so the translations change with them.

**Checklist**

- [ ] In NL, BE, DE and FR, replace "Free shipping on orders over €50" with "Free shipping over €50"
- [ ] In the UK, replace "Free shipping on orders over £45" with "Free shipping over £45"
- [ ] Show the new copy on web, iOS and Android
- [ ] Update the nl-NL, nl-BE, fr-BE, de-DE and fr-FR translations from the new source strings
- [ ] English chosen through the language switcher in a euro market shows "Free shipping over €50"
- [ ] The English banner fits on one line on the small phones where the current copy wraps
- [ ] Keep the €50 and £45 thresholds and the banner's position and styling unchanged
```

Export-equivalent path: `export/NNN - task-free-shipping-banner-copy.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** Checked at Quick level. All six floors pass, the task stays within the request and the facts come from `context/fernhouse-context.md`.

**Summary:** This is a copy-only Quick Task. It swaps the two banner strings, with the €50 line for the four euro markets and the £45 line for the UK. It also keeps the thresholds and the banner's layout as they are.

**Things I added or assumed that you can remove or change:**
- **Title:** The title has no surface segment. The house format expects one surface, but this banner appears on web, iOS and Android. If you'd rather split it, I can turn it into an `FS` parent task with one `FE` subtask per surface.
- **Two added requirements:** The context file says the English lines are the source for every locale. Because of that, I added the translation update and the check for English chosen through the language switcher.
- **One-line check covers English only:** The German and French translations may still wrap on small phones. Tell me if the one-line check should apply to every locale.
- **App release timing:** I didn't say where the banner copy lives. If it's built into the apps, the change reaches customers with 4.9.0 and about a week of store approval and updates. If it comes from a server, it can go live the same day.
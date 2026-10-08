The Doc gate is blocked, so I'm not drafting yet. I read both notes, and one thing needs your decision before I can write the document.

```markdown
# Clarification: how discount codes and automatic promotions stack

I'll document how discount codes and automatic promotions stack. Before I draft, I need the unresolved decisions below in one response.

**Purpose and audience:** Who will read this document, and what should they be able to do after reading it? For example, a CS agent explaining an order, a merchandiser setting up a promotion, or an engineer checking promotions-service.

**Scope and exclusions:** The rules note also covers the free-shipping threshold, gift cards, rounding and the retired two-code rule. Which of these belong in the document, and which are out of scope? Should the retired two-code rule appear as history for CS, or be left out?

**Document status:** Should the document describe current behavior? The rules note labels its main section Current rules. Confirm that status or name another: approved direction, proposal, retired material or unknown.

**Source set and authority:** I plan to use context/fernhouse-promotions-rules.md as the governing source for promotion behavior, with context/fernhouse-context.md for company background. Confirm that, or name any other source the document may use.

**Conflict to resolve:** The rules note sets free shipping at a subtotal of "at least €50" or "at least £45". The company context banner reads "Free shipping on orders over €50" and "Free shipping on orders over £45". At exactly €50.00 or £45.00, the rule gives free shipping and the banner does not. Which wording is correct, and does the banner copy need to change?

**Shape:** The document explains how a cart total is worked out, so a Behavior reference suits a reader who needs to predict an outcome. Confirm that shape, or choose Guide, Catalog, Proposal or Narrative overview.

**Validation:** Are there stacking cases outside these two notes that the document must cover?
```

Export-equivalent path: `export/NNN - doc-discount-stacking-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

No document is drafted yet, so there is no quality score. Once you answer the questions above, I'll draft the document. The threshold conflict matters most, because it decides whether a customer with exactly €50.00 in the euro markets or £45.00 in the UK gets free shipping.
Path: `export/fernhouse-save-card-draft.md`
Verified: read-back succeeded; 124 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the fixed labels `Given`/`When`/`Then`/`And` and `Mark as done, if the criteria are met` (template wording the synonym-cycling rule requires repeating), the subject-fixed triads `web, iOS and Android`, `card number, expiry and CVC`, the three stored card fields, and the three payment events (content lists rather than tic density), and the supplied strings in backticks (`Save this card for next time`, `unchecked by default`, `You can save up to 5 cards`, `Card ending 7031`, `Expires 08/28`, `€150`, `£130`, `CVC`, `This card was declined. Choose another card or enter a new one.`, `Remove this card?`, `Account > Payment methods`) preserved verbatim.

**What changed**
*   The `**Open:**` line is gone. The agreed copy now sits as a hard constraint: `This card was declined. Choose another card or enter a new one.`
*   The CVC rule now reads the order total including shipping: `Orders whose total, including shipping, is over €150, or £130 in the UK, ask for the CVC again before paying`
*   The `## Delivery` section is removed, since resolving the open question removed the only thing forcing it, so the Story now ends on Acceptance criteria with its section close
*   The Tracking group still describes the three events and names none, so the Data team can set the names

**One addition to check:** now that the decline copy is settled, I added a seventh acceptance criterion (`A declined saved card leaves another way to pay`) so the new string is verified by an outcome rather than left unproven. The criterion carries no hard value, leaving the exact copy in Requirements where it belongs. Strike it if you would rather keep the criteria set unchanged.

**Summary:** The Story is now fully settled with no open items and no placeholder Delivery view. The declined-card copy and the shipping-inclusive CVC threshold are both carried as hard constraints, and the source draft remains untouched in `context/`.
# FJ-049 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

**The reading**

* Reader and question: a support agent or new team member asks "where is this claim, who acts next and what status does it hold?"
* Outcome: the reader can name the status and the next actor for any claim, and sees where the guest decides
* Dials: Faithful detail, Mixed audience, Laptop distance
* Target: the existing file `<test-file-key>`, as a new board section beside what it holds
* Source class: the policy text is current behavior. The waiver under 25 euros is a proposal

**Assumed, and what would settle each**

* Reader: assumed support. The policy owner or you can correct it
* Who charges the card: the policy says the claim "is charged" and names no actor. I put both charge steps in the support lane. The policy owner can settle it
* The charge steps carry no status of their own. The policy gives a status only at Reported, With the guest, Under review and Closed, so each charge step ends "then Closed"

**Outline, in drawing order**

0. Question: where is a damage claim, who acts next and what status does it hold?
1. Hotel lane: "Report the damage", status Reported. After check-out | Photos and a repair quote | Quote from a listed supplier
2. Support lane: "Send the claim to the guest", status With the guest. Sends the photos and the quote | Guest sees them and the amount in the app | Asks the hotel for more photos if they do not show the damage
3. Guest lane, the accented decision: "Accept or dispute?", status With the guest. 7 days to answer
4. Accept exit to support lane: "Charge the card on file", then Closed
5. Dispute exit to support lane: "Review the dispute", status Under review. Reads the photos and the guest's reply | Decides within 5 working days
6. Support lane decision: "Uphold or drop?"
7. Uphold exit: "Charge the card", charged within 2 working days, then Closed
8. Drop exit: "Drop the claim", then Closed
9. End: "Claim closed", reached from the three exits above

That is 9 nodes and 10 connectors, with 3 lanes and 3 labelled decision exits. The remove test cuts nothing, because each step holds a status, a handover or a policy rule.

**Two framings**

* Process with lanes (recommended): it shows who acts next and where the claim changes hands, with statuses on the cards. It does not show a status as a thing of its own
* State map: it shows every status and each move between them, but loses the hotel, guest and support handovers

I recommend the process because your question is about movement between the three parties. The state map can come as a later board.

**The look**

* Accent: "Accept or dispute?", marked "the guest decides here". The goal is "Claim closed", unaccented
* Zones: the three lanes only. The support and guest lanes take a note, such as the 7 days the guest has
* Title: "Roamstay damage claim". Subtitle: "From the hotel's report to a closed claim, for support"
* Source line: the claims policy, with the two omissions named

**Left out, as you agreed**

* Claims under 25 euros waived, a rule not yet live
* What happens when the 7 days pass with no reply, which the policy does not state

Is this reading right, including the two assumptions, or should anything change before I check the model?

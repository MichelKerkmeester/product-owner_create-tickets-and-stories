I've confirmed the reading and checked the model. Here's the write plan.

**Question:** which statuses can a Roamstay booking have, what moves it between them, and who sets Cancelled and No-show?
**Outcome:** support can find a booking's status and know who to ask about a Cancelled or No-show booking.

**What the reader should see:**
- **First:** Cancelled.
- **Next:** the moves that lead to an ending: "guest cancels", "missed check-in" and "check out", plus the two notes saying who sets each status.
- **Can wait:** Pending, where every booking starts.

**The model.** The check passed: 7 states and 12 transitions.
```
[*] → Pending → Confirmed: card authorised
Confirmed { [*] → Upcoming → In stay: check in → [*] }
Confirmed → Completed: check out [from In stay]
Pending → Cancelled: guest cancels
Confirmed → Cancelled: guest cancels
Confirmed → No-show: missed check-in [from Upcoming]
Completed, Cancelled, No-show → [*]
```

**File:** the existing FigJam file `<test-file-key>`. No new file gets created.
- None of your Figma plans is called Roamstay Product, and you didn't say which plan you meant. So I'm taking my recommendation: the board goes into this file, whose plan is already set and stays as it is.
- If the file turns out to be a design file and not a FigJam file, I'll stop and ask before doing anything else.

**What gets written:**
- One board titled "Roamstay booking status". It holds the title, the 7 states and 12 transitions, a key and a source line.
- The source line marks "check in" as assumed.
- The board goes to the right of everything already on the page, and nothing that's already there gets touched.

**Notes:** one sticky beside each of two states:
- **Cancelled:** "set by the guest, while Pending or Confirmed"
- **No-show:** "set by the hotel, after a missed check-in"

**Calls this will use:**
- `create_session` on the file.
- One `get_figjam` read of the page before the write, so I can confirm afterwards that the existing content is unchanged.
- One `use_figma` call to draw the board.
- One `use_figma` call to add the notes.
- One `get_figjam` read afterwards to check the board against the model.

**How to undo it:** delete the one board section this write creates, which removes the notes with it. That delete happens only if you separately say yes to it. Nothing else in the file is affected.

Should I write it?
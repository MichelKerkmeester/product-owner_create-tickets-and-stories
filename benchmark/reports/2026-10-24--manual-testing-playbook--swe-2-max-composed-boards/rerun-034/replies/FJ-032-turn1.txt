I haven't written anything to the board. A "Booking status" section with this lifecycle is already on it.

I read the board with `create_session` and one `get_figjam` call. Both are read-only. Section `62:66`, "Booking status", sits at x 2008, y -608, and its subtitle says "Every status a Roamstay booking passes through, what moves it on and who sets Cancelled and No-show". It matches your five rules:
* **Statuses:** Pending, Confirmed (containing Upcoming and InStay), Completed, Cancelled and NoShow
* **Moves:** Pending to Confirmed, Confirmed to Completed, Pending to Cancelled, Confirmed to Cancelled and Confirmed to NoShow
* **Notes and key:** it also carries a key, a source line and two blue stickies that read `note:1` and `note:2`

Two things I can't confirm from the read:
* **Wording:** the existing boxes read `InStay` and `NoShow`, not "In stay" and "No-show".
* **Edge labels:** the read returned layer names instead of label text, so I can't say whether the edges carry "card authorised", "check out" and the rest.

**Reading:** the lifecycle you described is already drawn, so adding it again would put a duplicate beside it.

**Question:** should I leave the existing section as it is, replace it, or add a second copy?
1. Leave it. I'd point you to the section and write nothing.
2. Replace it. I'd model the lifecycle with your wording ("In stay", "No-show") and labelled edges, compose it, read it back and delete the old section only after a second yes from you.
3. Add a second copy beside it.

**Recommended:** 1. The states and moves already match all five rules, and only the spelling differs. Choose 2 if you want the labels to match your wording.

**Left out:** refunds, payment steps, hotel-side cancellation and any No-show window. The source line already on the board says the same.

**Assumed:** a state diagram at Laptop reading distance with a mixed audience, if you choose 2 or 3.

The board also holds two "Block sync" sections (`67:192` and `72:441`). I haven't touched them.

Whichever you pick, the write gets its own message and waits for a separate yes.
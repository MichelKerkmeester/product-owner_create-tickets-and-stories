Before I write anything, here's the gate. I composed the board from the checked model, and nothing is on the file yet. The check passed with 7 states and 12 transitions, and the composed code fits in one `use_figma` call.

Question: which statuses exist and what moves a booking between them?
Outcome: the product and support team leave the retro agreeing every booking status and the move between each pair.
First glance: the Confirmed section, which holds Upcoming and In stay. It's the largest tinted shape, and the check refuses an accent on a section, so the board has no pink outline.
Second glance: the three moves out of Confirmed, check out, guest cancels and missed check-in.
Last glance: Pending, where every booking starts.
Plan and file: the existing FigJam file `<test-file-key>`, so no new file and no plan needed.
Title: "Roamstay booking status lifecycle". The file already has 10 sections titled "Booking status", 6 titled "Booking status lifecycle", "Roamstay booking status" and "Roamstay booking lifecycle for support". I recommend this title because no section on the file uses it, so a later session can find this board by its tag without confusing it with another.
Writes: one new section, 7 states and 12 transitions, with a title, a subtitle, a key and a source line, at the Laptop reading distance. The three end states, Completed, Cancelled and No-show, are drawn in light gray. It lands to the right of the last existing section, and nothing already on the file changes.
Extensions: none.
Calls: one `use_figma` to compose, then a `get_figjam` read-back of the new section. I may add one more read to confirm all 97 earlier sections are still there. I already spent one `get_figjam` read on the board. If your seat is on Figma's six-calls-a-month limit, the write and read-back still fit.
Rollback: delete the one new section the write returns. I'd do that only on your yes to a question that names the board by its title.

Write it to the existing file `<test-file-key>`?
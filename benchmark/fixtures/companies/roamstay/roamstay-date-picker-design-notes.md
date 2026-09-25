# Date picker stay limits, design notes

Source: handover notes pinned to the frame `Date picker / Stay limits` in the Guest app search design file
Written by Ines, Product Designer, Search squad, on 2026-09-14
Walked through with Oskar (Android engineer) and Hana (UX writer). Copy signed off by Hana on 2026-09-11

Hi all, these are my notes for the stay limits work in the date picker. The frames are final. If something in the build doesn't match the file, tell me in the Search squad channel before you work around it.

## Why

Today the picker lets a guest select any range. search-service then turns down anything over 30 nights, and the guest gets a generic "Something went wrong" after tapping Search. Guest Support logged 23 chats about it in August, mostly long stays for work. The picker should stop a range it can't search before the guest taps Search, and say why.

## Limits

- A stay is at least 1 night. Check-in and check-out can't be the same day
- A stay is at most 30 nights, the same limit search-service applies
- Check-in can be at most 365 days from today. Later days show in the calendar but are disabled
- Past days are disabled. Today can be picked as check-in
- On the property page the picker also applies the property's minimum stay. Partners set it in Partner Hub, anywhere from 1 night to 14 nights
- Check-out may land past the 365-day mark. Only check-in is limited

## States in the frame

1. Nothing picked. The button at the bottom reads `Select check-in date` and is disabled
2. Check-in picked. Days that would make the stay too short or longer than 30 nights turn grey. The button reads `Select check-out date` and stays disabled
3. Valid range picked. The range is highlighted, the nights count sits under it and the button reads `Show prices`
4. The guest taps a grey day past the 30-night limit. Nothing gets selected, and helper text under the calendar reads `Stays can be up to 30 nights`
5. Property page only. The guest taps a day inside the property's minimum stay. Nothing gets selected and the helper text reads `This property has a 3-night minimum`, with the property's own number in it

The helper text stays until the guest picks a valid day. It never covers the calendar.

## Copy

| Key | en-GB copy | Where |
|-----|------------|-------|
| `datepicker.cta.checkin` | Select check-in date | Button, state 1 |
| `datepicker.cta.checkout` | Select check-out date | Button, state 2 |
| `datepicker.cta.show_prices` | Show prices | Button, state 3 |
| `datepicker.helper.max_stay` | Stays can be up to {max} nights | Helper text, state 4 |
| `datepicker.helper.min_stay` | This property has a {n}-night minimum | Helper text, state 5 |
| `datepicker.nights` | {count} night, {count} nights | Under the range |

Hana has sent all six keys for translation. The frames show the real numbers, so state 4 reads `Stays can be up to 30 nights` and state 5 reads `This property has a 3-night minimum`.

## Edge cases we walked through

- The guest picks check-in, then taps a day before it. That day becomes the new check-in and the button goes back to `Select check-out date`
- The guest opens the picker with dates already set from an earlier search. The range shows as picked, in state 3
- Dates from an earlier search that break a limit, for example a saved 45-night search from before this change, are cleared and the picker opens in state 1
- A 30-night range across two months keeps the highlight across the month break
- Screen readers announce a grey day as unavailable, followed by the same helper text as states 4 and 5

## Platforms

- iOS and Android use our own calendar component from the design system, never the system date picker
- Web on desktop shows two months side by side. Mobile web and the apps show one month at a time and scroll vertically
- The week starts on Monday, except in `en-US`, where it starts on Sunday

## Answered in the walkthrough

- Oskar asked where the limits come from. The 30-night maximum and the 365-day window come from search-service config, and the property minimum comes with the property details. The apps hard-code none of them
- Oskar asked whether a grey day can still be tapped. Yes. The tap shows the helper text, which is the only way the guest learns why the day is grey

## Not in this work

- Flexible dates and weekend presets
- Prices per night inside the calendar
- Any tracking change. Date selection isn't tracked today and this work adds nothing

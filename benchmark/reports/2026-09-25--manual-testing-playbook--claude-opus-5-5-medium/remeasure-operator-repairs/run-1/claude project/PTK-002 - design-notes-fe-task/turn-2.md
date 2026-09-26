```markdown
# FE - Guest app - SRCH - Date picker stay limits

### About

---

Today the Guest app date picker lets a guest select any range. search-service then rejects any stay over 30 nights, and the guest only sees a generic "Something went wrong" after tapping Search. Guest Support logged 23 chats about this in August, mostly from guests booking long work stays. The picker should stop a range that search can't serve before the guest taps Search, and tell the guest why.

A day turns grey when picking it would create a stay that search-service would reject or the property doesn't allow. A grey day still accepts a tap, because the helper text shown on tap is the only way the guest learns why the day is unavailable. The limits come from search-service config and from the property details, so the Guest app hard-codes none of them.

This is one task covering iOS, Android and web. The Search squad takes it into the 8.13.0 train. search-service stays as it is, and its own 30-night check remains the backstop. Flexible dates, weekend presets, prices per night inside the calendar and any tracking change are out of scope. Date selection isn't tracked today, and this work adds no tracking.

**References**

---

Flows

- `Date picker / Stay limits` frame in the Guest app search design file

### Requirements

---

### **Limits**

---

1.  **Stay length and check-in window**

---

These limits apply to the date picker everywhere in the Guest app. They match the limits search-service already enforces, so every range the guest can pick is one that search can return.

**Checklist**

- [ ] A stay is at least 1 night, so check-in and check-out can't be the same day
- [ ] A stay is at most 30 nights
- [ ] Check-in can be at most 365 days from today, and later days show in the calendar as disabled
- [ ] Check-out can land past the 365-day mark, because only check-in is limited
- [ ] Past days are disabled, and today can be picked as check-in
- [ ] The 30-night maximum and the 365-day window are read from search-service config, and the Guest app hard-codes neither value

2.  **Property minimum stay**

---

On the property page, the picker also applies the minimum stay the partner sets for that property in Partner Hub. The minimum can be anything from 1 night to 14 nights.

**Checklist**

- [ ] On the property page, check-out days that would make the stay shorter than the property's minimum stay are grey
- [ ] The minimum stay comes with the property details, and the Guest app never hard-codes it
- [ ] The picker in the search form applies only the 1-night minimum

### **Picker states**

---

3.  **Nothing picked, check-in picked and valid range**

---

The bottom button tells the guest what to do next. It becomes available only once the guest has picked a range that search can serve.

**Checklist**

- [ ] With nothing picked, the button reads `Select check-in date` and is disabled
- [ ] With check-in picked, days that would make the stay too short or longer than 30 nights turn grey, and the button reads `Select check-out date` and stays disabled
- [ ] With a valid range picked, the range is highlighted, the nights count sits under it and the button reads `Show prices`

4.  **Tapping a grey day**

---

Tapping a grey day selects nothing and explains the limit in helper text under the calendar. This replaces the generic error the guest sees today after tapping Search.

**Checklist**

- [ ] A grey day still accepts a tap, and the tap selects nothing
- [ ] Tapping a grey day past the 30-night limit shows the helper text `Stays can be up to 30 nights`
- [ ] On the property page, tapping a day inside the property's minimum stay shows the helper text with the property's own number, for example `This property has a 3-night minimum`
- [ ] The helper text stays until the guest picks a valid day
- [ ] The helper text never covers the calendar
- [ ] Screen readers announce a grey day as unavailable, followed by the same helper text

### **Edge cases**

---

5.  **Changing and restoring dates**

---

A guest often changes their mind partway through or comes back to the picker with dates from an earlier search. The picker must never restore a range it would not let the guest pick now.

**Checklist**

- [ ] With check-in picked, tapping a day before check-in makes that day the new check-in, and the button goes back to `Select check-out date`
- [ ] Opening the picker with valid dates from an earlier search shows the range as picked, with the button reading `Show prices`
- [ ] Dates from an earlier search that break a limit are cleared and the picker opens with nothing picked. For example, a 45-night search saved before this change
- [ ] A 30-night range that spans two months stays highlighted across the month break

### **Platforms and copy**

---

6.  **Calendar layout per platform and locale**

---

**Checklist**

- [ ] iOS and Android use the design system calendar component, never the system date picker
- [ ] Web on desktop shows two months side by side
- [ ] Mobile web and the apps show one month at a time and scroll vertically
- [ ] The week starts on Monday, except in `en-US`, where it starts on Sunday

7.  **Copy keys**

---

Hana signed off the copy on 2026-09-11 and sent all six keys for translation. `{max}` comes from search-service config and `{n}` comes from the property's minimum stay.

| Key | en-GB copy | Where |
|-----|------------|-------|
| `datepicker.cta.checkin` | Select check-in date | Button, nothing picked |
| `datepicker.cta.checkout` | Select check-out date | Button, check-in picked |
| `datepicker.cta.show_prices` | Show prices | Button, valid range picked |
| `datepicker.helper.max_stay` | Stays can be up to {max} nights | Helper text, grey day past 30 nights |
| `datepicker.helper.min_stay` | This property has a {n}-night minimum | Helper text, grey day inside the property minimum |
| `datepicker.nights` | {count} night, {count} nights | Under the range |

**Checklist**

- [ ] Every string in the picker comes from the six keys above
- [ ] The nights count uses the singular form for 1 night and the plural form for more than 1 night

### **Sign-off**

---

8.  **QA**

---

**Checklist**

- [ ] QA signs off on iOS, Android and web in `en-GB`
- [ ] QA signs off on iOS, Android and web in `en-US`, including the week starting on Sunday
- [ ] search-service is unchanged, and its own 30-night check still rejects a longer stay
```

Export-equivalent path: `export/002 - task-date-picker-stay-limits.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** All six scoring dimensions pass. Every requirement comes from Ines's notes, the conventions file or your answer.

**Choices and additions for you to check:**
- **Property minimum stay:** I kept this in this task under `SRCH` because you asked for one FE task. The conventions give the property page the `PROP` code, so say if you want it split out.
- **Search form minimum:** Group 2 says the search form picker applies only the 1-night minimum. I inferred that from "on the property page the picker also applies". Strike it if that's wrong.
- **Figma:** the frame is listed by name only because no link was supplied.
- **Not answered yet, so not written in:**
  - whether search-service config and the property details already send these limits to the Guest app, or a BE task has to land first
  - whether the design system calendar already supports a grey day that still accepts a tap
  - whether shipping waits for the other five locales' translations
  - whether a cleared saved search shows the guest a message. The task only says the picker opens with nothing picked.

**Next step:** Reply with any fixes. If you'd like this pushed to ClickUp, confirm here first and name the list.
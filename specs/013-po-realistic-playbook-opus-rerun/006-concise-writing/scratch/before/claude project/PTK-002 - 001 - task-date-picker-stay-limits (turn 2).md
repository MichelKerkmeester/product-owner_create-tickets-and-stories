<!-- Mode: Task | Template: Task Templates v0.102 -->
# FE - Guest app - SRCH - Date picker stay limits

### About

---

Today the Guest app date picker lets a guest select any range. `search-service` turns down anything over 30 nights, and the guest only sees a generic `Something went wrong` after tapping Search. Guest Support logged 23 chats about it in August, mostly about long stays for work.

This task makes the date picker block a range that can't be searched before the guest taps Search, and tells the guest why. It covers the Guest app on iOS, Android and web as one task. It applies on the search form and on the property page, where the picker also applies the property's minimum stay. The Search squad takes it into the 8.13.0 app train.

`search-service` doesn't change. Its own 30-night check stays in place as the backstop, so a range that gets past the picker is still turned down. Flexible dates, weekend presets, prices per night inside the calendar and tracking changes are out of scope. Date selection isn't tracked today, and this work adds no events.

The design frames are final. If the build doesn't match the file, raise it with Ines in the Search squad channel before working around it.

**References**

---

Flows

- `Date picker / Stay limits` frame in the Guest app search design file

### Requirements

---

### **Limits**

---

1.  **Where the limits come from**

---

The apps hard-code none of the limits, so a change to search-service config or to a partner's minimum stay reaches the picker without an app release.

**Checklist**

- [ ] The 30-night maximum and the 365-day check-in window come from `search-service` config
- [ ] On the property page, the minimum stay comes with the property details, where a partner sets it in Partner Hub anywhere from 1 night to 14 nights
- [ ] Helper text fills `{max}` and `{n}` from these values, never from a number fixed in the app

2.  **Which days can be picked**

---

The picker enforces the same limits `search-service` applies, so every range it accepts can be searched.

**Checklist**

- [ ] Past days are disabled, and today can be picked as check-in
- [ ] Days more than 365 days after today show in the calendar but are disabled as check-in
- [ ] Check-out may land more than 365 days after today, because only check-in is limited
- [ ] Check-in and check-out can't be the same day, so a stay is at least 1 night
- [ ] A stay is at most 30 nights
- [ ] On the property page, a stay is also at least the property's minimum stay

### **Picker states**

---

3.  **Button and range states**

---

The button at the bottom of the picker tells the guest what to do next and stays disabled until the range is valid.

**Checklist**

- [ ] With nothing picked, the button reads `Select check-in date` (`datepicker.cta.checkin`) and is disabled
- [ ] With check-in picked, days that would make the stay too short or longer than 30 nights turn grey, and the button reads `Select check-out date` (`datepicker.cta.checkout`) and stays disabled
- [ ] With a valid range picked, the range is highlighted, the nights count sits under it (`datepicker.nights`) and the button reads `Show prices` (`datepicker.cta.show_prices`)
- [ ] A 30-night range across two months keeps the highlight across the month break

4.  **Helper text on a grey day**

---

A grey day can still be tapped. Tapping it is the only way the guest learns why the day is grey, so the tap selects nothing and shows helper text under the calendar.

**Checklist**

- [ ] Tapping a grey day past the 30-night limit selects nothing and shows `Stays can be up to 30 nights` (`datepicker.helper.max_stay`)
- [ ] On the property page, tapping a day inside the property's minimum stay selects nothing and shows the helper text with the property's own number, for example `This property has a 3-night minimum` (`datepicker.helper.min_stay`)
- [ ] The helper text stays until the guest picks a valid day
- [ ] The helper text never covers the calendar
- [ ] Screen readers announce a grey day as unavailable, followed by the same helper text a tap would show

5.  **Changing and reopening dates**

---

A guest who changes their mind or comes back from an earlier search always lands in a state that can be searched.

**Checklist**

- [ ] With check-in picked, tapping a day before it makes that day the new check-in, and the button goes back to `Select check-out date`
- [ ] Opening the picker with dates from an earlier search shows the range as picked, with the button reading `Show prices`
- [ ] Opening the picker with earlier dates that break a limit, such as a 45-night search saved before this change, clears them and opens with nothing picked

### **Platforms**

---

6.  **Layout and locale**

---

The same behavior ships on every platform, with a layout that fits each one.

**Checklist**

- [ ] iOS and Android use the design system's own calendar component, never the system date picker
- [ ] Web on desktop shows two months side by side
- [ ] Mobile web and the apps show one month at a time and scroll vertically
- [ ] The week starts on Monday, except in `en-US`, where it starts on Sunday
- [ ] All six `datepicker` keys show the translated copy for the guest's locale, and fall back to `en-GB` for any missing string

7.  **QA sign-off**

---

The task is done when QA signs it off on every platform in both English locales.

**Checklist**

- [ ] QA signs off on iOS, Android and web
- [ ] Each platform passes in `en-GB` and in `en-US`

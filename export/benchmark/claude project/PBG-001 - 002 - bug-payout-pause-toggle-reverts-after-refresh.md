# Payout pause toggle silently reverts to off after a page refresh

### About

---

On the brand wallet, the payout pause toggle silently reverts to off after a page refresh while the payout still shows paused.

| Field           | Value        |
| --------------- | ------------ |
| Frequency       | Always       |
| Severity        | Not provided |
| Platform        | Web          |
| Device          | Not provided |
| OS Version      | Not provided |
| Browser         | Chrome       |
| Browser Version | 126          |

---

### Bug

---

**1. Observed Behavior**

---

When a brand pauses a payout and refreshes the page, the toggle displays off while the payout still shows paused
- The payout stays paused, so the toggle and the payout paused status disagree after the refresh
- No error message appears

Steps to Reproduce:
1. Open a brand wallet with a pending payout
2. Switch the payout pause toggle on
3. Refresh the page
4. Observe the payout, which still shows paused
5. Observe the toggle, which shows off while it should stay on until the payout is resumed

Screen recording: Not provided. Screenshot: Not provided.

---

**2. Expected Behavior**

---

The pause toggle should keep showing on after a page refresh until the brand resumes the payout
- User expectation: the toggle matches the payout paused status the whole time, so a paused payout never shows an off toggle

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Payout pause toggle stays on across a refresh
- **Given** a brand wallet with a payout paused by the brand
- **When** the brand refreshes the page
- **Then** the pause toggle still shows on while the payout shows paused, until the brand resumes the payout

<!-- Bug Mode · Product Owner Bug Report Template v0.100 -->

# Payout pause toggle reverts to off after page refresh

### About

---

On web, the payout pause toggle in a brand wallet silently reverts to off when the page is refreshed, while the payout itself still shows as paused.

| Field           | Value                        |
| --------------- | ---------------------------- |
| Frequency       | Always (per reporter)        |
| Severity        | Not provided                 |
| Platform        | Web                          |
| Device          | Not provided                 |
| OS Version      | Not provided                 |
| Browser         | Chrome                       |
| Browser Version | 126                          |

**References:**

**Flows**
- Not provided

**Components**
- Not provided

---

### Bug

---

**1. Observed Behavior**

---

After the payout pause toggle is switched on, refreshing the page turns it back to off without any error or notice.

- What the user sees: the toggle displays the off state after the refresh
- Error messages: No error message reported
- Incorrect state: the toggle reads off while the payout still shows as paused

Steps to Reproduce:
1. Open a brand wallet that has a payout in the pending state
2. Switch the payout pause toggle on
3. Refresh the page
4. Observe: the toggle shows off while the payout still shows paused, where the toggle was expected to stay on until the brand resumes the payout

Screen Recording: Not provided

---

**2. Expected Behavior**

---

The payout pause toggle should stay on after a page refresh until the brand resumes the payout, matching the paused state the payout continues to show.

- Design specifications: Not provided
- Previous working behavior: Not provided
- User expectations: the toggle reflects the payout's persisted paused state and stays on until the brand resumes the payout

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Pause toggle state survives a page refresh
- **Given** a brand wallet with a pending payout whose pause toggle has been switched on
- **When** the page is refreshed
- **Then** the payout pause toggle stays on until the brand resumes the payout, in line with the payout's paused state

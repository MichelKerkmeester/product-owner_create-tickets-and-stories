### Deliverable Block

---

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

---

Export-equivalent path: `export/002 - bug-payout-pause-toggle-reverts-after-refresh.md`

Quality: passes the Bug Mode checklist. Everything in the report traces to your answers, so the report holds no invention: Frequency is Always because you said it happens every time, Severity, Device and OS Version read Not provided, and both evidence lines read Not provided because you had no screenshot. The checklist stays the fixed four-item QA handoff gate, and root cause stays a checklist item because nothing you supplied establishes it.

Next step: if anything above misreads your report, tell me what to change. No ClickUp connector is present, so there is no push to offer.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `Steps to Reproduce:` as template-verbatim wording, the fixed four-item checklist per Bug Mode, and `Always` under the Frequency rule's every-time allowance.
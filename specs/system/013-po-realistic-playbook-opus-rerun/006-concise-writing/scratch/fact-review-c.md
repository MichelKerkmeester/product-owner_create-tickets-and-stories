claude project/PDK-002 - 002 - doc-payment-webhook-failures-runbook.md | 18 | 16 | Changed | "By the time you fix the cause, many events are waiting hours for their next attempt, so retries alone leave guests on the confirming screen"
claude project/PDK-003 - 002 - doc-sync-conflict-options-proposal.md | 41 | 41 | Changed | "Yara puts A's coverage at a bit over half of the overwriting sessions, which matches the 58% that changed only to-do fields"

Files read: 34 (groups g1 and g4). Files with a diff: 33. Problems found: 2.

## The two problems

- PDK-002 runbook, glossary line for payment provider retries. The original made the wait conditional on relying on retries alone ("retries alone leave guests on the confirming screen"). The edit reads "so after a fix many guests wait hours on the confirming screen", which states the wait as the outcome of any fix, including one followed by the psp-replay in step 4. The conditional form still stands at after line 70 ("The payment provider's retries alone would leave most bookings waiting hours for the next attempt"), so the glossary line now disagrees with step 4 rather than losing the fact outright.
- PDK-003 options proposal, Option A "What it fixes". The original gave Yara's coverage estimate as "a bit over half" and said it "matches" the 58% split. The edit reads "covering Yara's 58% of overwriting sessions", which turns the hedged estimate into a flat 58% coverage claim and drops "a bit over half". The 58% split itself is kept at after line 25.

## Per-file verdicts

g1 (skill):

- SBG-001 001: none. Android 4.8.2 and web updating on remove, loosened at after line 57, is kept at after lines 7 and 35.
- SBG-002 001: none. "Back office has that test charge at €270.00" (after line 50) names the test-phone charge the original meant.
- SBG-003 001: none.
- SBG-003 002: none.
- SID-001 001: no diff, not read further.
- SID-001 002: none. The chip order and "not checked off" rule are kept at after lines 23 and 25, Web-only scope at line 7.
- STK-001 001: none.
- STK-002 001: none.
- STK-003 001: none. The edit now names the five goals as Noor's five points (after line 11). The original put them in adjacent sentences, and they match requirement sections 1 to 5, so this reads as the same fact.
- STK-004 001: none.
- STK-004 002: none. The member-facing list moved out of About, and the parts are kept in requirements 1 and 2 (after lines 37 to 63).
- STK-004 003: none. Same as iOS, kept at after lines 38 to 64.
- STK-004 004: none. Same as iOS, kept at after lines 38 to 64.
- STK-004 005: none. The 500 per workspace limit is kept at after line 89.
- STK-005 001: none. The dropped list of Android parts is kept in requirements 1 to 9.
- STK-006 001: none.
- STK-006 002: none. `booking_confirmed` as the only booking count, sent by `booking-service` with `source` `server`, is kept at after lines 72, 76 and 100.

g4 (claude project):

- PDK-001 001 (turn 2): none. The exclusive-code and exclusive-promotion rules dropped from the edge case are kept at after lines 46, 47 and 83.
- PDK-001 001: none. The £45 and above threshold dropped from the banner edge case is kept at after line 69.
- PDK-002 001: none.
- PDK-002 002: one problem, above. The rest (INC-0412 figures, pause reason, rotation order, review gaps) is kept.
- PDK-003 001: none. That the spike includes the formatting fallback is kept at after line 70.
- PDK-003 002: one problem, above. v3 last-writer-wins, dropped from the opening, is kept at after line 17.
- PDK-004 001: none.
- PDK-004 002: none. The out-of-date 07:00 UTC schedule dropped from Sources is kept at after line 159.
- PEP-001 001: none.
- PEP-001 002: none.
- PEP-002 001: none.
- PEP-002 002: none.
- PEP-003 001: none. That each child story carries its own requirements and acceptance criteria is kept at after line 44.
- PIR-001 001: none.
- PIR-001 002: none.
- PIR-002 001: none.
- PIR-002 002: none.

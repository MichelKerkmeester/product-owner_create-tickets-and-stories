`Path: export/002 - bug-reminders-late-after-clock-change.md`

`Verified: read-back succeeded; 108 lines`

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: **1. Observed Behavior** and **2. Expected Behavior**, the two fixed corpus labels the Bug Mode grant keeps title case; the 11 log lines kept verbatim inside a fenced block; Not provided, the template's own value for unsupplied fields.`

**Quality summary**

| Dimension | Read |
| --- | --- |
| Accuracy | 9 - every ID, count, version, offset and UTC time traces to a supplied line, and the new-codeblock diff is clean against the excerpt |
| Completeness | 9 - all four template blocks, both groups' observed and expected pairs, the workaround, the log evidence and the fixed QA checklist |
| Clarity | 8 - Group A and Group B stay apart through observed behavior, steps and expected behavior |
| Actionability | 8 - QA can rebuild each group from the numbered steps, with the decisive step carrying expected against actual |
| Relevance | 8 - nothing outside the two groups, the sources and the board conventions |
| Mechanism Depth | 8 - the cause is labelled an unverified hypothesis and given to Group A alone, so no root cause reads as fact |

**Summary**

The bug is titled `FS - REM - Reminders arrive an hour late after a forward clock change` and covers both groups in one report, with Group A (Android 5.2.3, 64 one-off tickets) and Group B (iOS 5.2.4, 53 daily tickets) described apart and each carrying its own reproduction steps, the edit-and-save workaround, the verbatim log lines and a High severity. Two points came from me rather than from your sources, so strike them if they are wrong: the discipline code is `FS` with the platform segment dropped, since the report spans Android and iOS and the fix may sit on either side, and the About carries a blank version-scope statement that the current 5.3.0 and 5.3.2 apps are unchecked, which claims neither affected nor fixed. Frequency reads `Not provided` with the 117, 64 and 53 counts kept in Observed Behavior, and the checklist leaves `Root cause identified` open.
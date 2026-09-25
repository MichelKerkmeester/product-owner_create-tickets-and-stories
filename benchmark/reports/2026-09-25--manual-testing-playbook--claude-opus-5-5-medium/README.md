# Manual testing playbook run, 2026-09-25, Product Owner, claude-opus-5-5 medium

The graded results, the handover status and the findings are written above this run record once grading closes. Until then this file holds only how the run was made.

---

## Run record

### Sources and harness

| Item | Value |
| --- | --- |
| Playbook | Version 2.0.0.0, 46 scenarios, 23 skill and 23 Project, each twinned, 86 turns |
| Product Owner repo | `3023c5ecbdd418e41cdc0a1454dad6826becc2c0`, sources clean before and after the run |
| Barter repo | `c15c05e947a063b7fa831d9c7d31002156ef8b6f`, the same before and after |
| Operator approval | The scenario plan was approved on 2026-09-25 at 19:31 UTC, before any scenario ran |
| Claude Code | `2.1.282` |
| Engine, model, effort | `claude`, `claude-opus-5-5`, `medium` (`manifest.json`) |
| Parallel sessions | `--jobs 4` |
| `run/playbook_runner.py` | sha256 `868cad2739c77675c4fb829e927a4a719503d12de29e83d1b38d1087fff4ed92` |
| `run/collect_exports.py` | sha256 `34427b7cc79d7af97068c3a444b1b01a5199dd4d18926e60e76ff83cea20c737` |
| `run/check_run.py` | sha256 `4bc16f13ef663f05e0a0266388815747ce73b79741b75f6f85b300baab527faa` |
| `run/selftest.py` | sha256 `5e79b00f41c0b52ce4572a197aae8a934c7ed1511b6f0f696c3000700dd503cb` |

Command, from this folder:

```bash
python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-opus-5-5 --effort medium --jobs 4
```

### Smoke run

`SID-001` and `PID-001` ran first on their own, outside this folder, with `--jobs 2`. Both finished on their first attempt with 2 of 2 turns, and every assistant event in their four streams names `claude-opus-5-5` alone, so `check_run.py` kept its single expected model and no allowed-model option was added.

### The run

| Measure | Value |
| --- | --- |
| Event time | 19:35:44 UTC to 20:06:05 UTC, about 30 minutes |
| Runner exit | 0 |
| Scenarios | 46 of 46 `ok` on the first attempt, 0 retried, 0 failed attempts |
| Turns | 86 of 86 run: 40 scenarios at 2 of 2 and 6 at 1 of 1 (`run-status.json`) |
| Models in the streams | `claude-opus-5-5` only, in all 86 |
| Cost | USD 71.36: skill 40.18 over 43 turns, Project 31.19 over 43 turns |
| Turn time | 6,744 s in all: skill 3,768 s, Project 2,977 s |
| Longest turns | `STK-004` Turn 1, 352 s. `SST-004` Turn 1, 334 s. `PST-004` Turn 1, 213 s |
| Run defects | None |

`python3 run/check_run.py . --model claude-opus-5-5` exits 0: `46 scenarios, 86 declared turns, 86 event streams read, 0 finding(s), expected claude claude-opus-5-5 at effort medium`.

The smoke estimate was USD 49 and 13 minutes, and it said it was a floor. The run cost 46% more and took more than twice as long. The handover turns are short, while the bundle, parent task and long task turns read three attachments and write several files.

### Collection

`python3 run/collect_exports.py . ../../../export/benchmark` collected 98 files into `AI Systems/Product Owner/export/benchmark/`, which held 0 files before. That's the same 98 lines as the dry run, with no warning about a changed attachment.

| Side | Files | How each was checked |
| --- | ---: | --- |
| Skill | 41 | Byte-identical to the file the runtime wrote under `skill/<ID> - <slug>/exports/export/` |
| Project | 57 | Each block's text found verbatim in its `replies/<ID>-turn<n>.txt` |

Each Story bundle kept its folder: `skill/SST-004 - 001 - Story-order-tracking/` and `claude project/PST-004 - NNN - Story-order-tracking-timeline/`. The refinement kept its source name on both sides, `fernhouse-save-card-draft.md`. The Project folder holds the blocks of both `PST-004` turns, since both turns rendered blocks under the same folder name.

### What is tracked

Tracked here: `manifest.json`, `run-status.json`, `replies/`, each scenario's `meta.json` and `turn-<n>.md`, and `run/`. Kept local by `.gitignore`: the event streams and `run-log.jsonl`, stderr, transcripts, the progress file and each scenario's `exports/` copy. The deliverables themselves are tracked in `export/benchmark/`.

### Project extraction review

Each collected Project file set beside its reply: the file's text is found verbatim in the reply named here, as the block that reply rendered.

| Collected file | Found in |
| --- | --- |
| `PBG-001 - NNN - bug-ios-cart-badge-stale-after-remove.md` | `replies/PBG-001-turn1.txt` |
| `PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax (turn 2).md` | `replies/PBG-002-turn2.txt` |
| `PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax.md` | `replies/PBG-002-turn1.txt` |
| `PBG-003 - 001 - bug-reminders-late-after-march-clock-change-clarification.md` | `replies/PBG-003-turn1.txt` |
| `PBG-003 - 002 - bug-reminders-late-after-march-clock-change.md` | `replies/PBG-003-turn2.txt` |
| `PDK-001 - 001 - doc-promotions-stacking (turn 2).md` | `replies/PDK-001-turn2.txt` |
| `PDK-001 - 001 - doc-promotions-stacking.md` | `replies/PDK-001-turn1.txt` |
| `PDK-002 - 001 - doc-payment-webhook-failures-clarification.md` | `replies/PDK-002-turn1.txt` |
| `PDK-002 - 002 - doc-payment-webhook-failures-runbook.md` | `replies/PDK-002-turn2.txt` |
| `PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md` | `replies/PDK-003-turn1.txt` |
| `PDK-003 - 002 - doc-sync-conflict-options-proposal.md` | `replies/PDK-003-turn2.txt` |
| `PDK-004 - 001 - doc-loomlist-activity-emails-clarification.md` | `replies/PDK-004-turn1.txt` |
| `PDK-004 - 002 - doc-loomlist-activity-emails.md` | `replies/PDK-004-turn2.txt` |
| `PEP-001 - 001 - Epic-partner-hub-self-onboarding-clarification.md` | `replies/PEP-001-turn1.txt` |
| `PEP-001 - 002 - Epic-partner-hub-self-onboarding.md` | `replies/PEP-001-turn2.txt` |
| `PEP-002 - 001 - Epic-offline-mode-clarification.md` | `replies/PEP-002-turn1.txt` |
| `PEP-002 - 002 - Epic-offline-mode.md` | `replies/PEP-002-turn2.txt` |
| `PEP-003 - 001 - Epic-self-serve-returns.md` | `replies/PEP-003-turn1.txt` |
| `PID-001 - 001 - task-due-today-filter-chip-clarification.md` | `replies/PID-001-turn1.txt` |
| `PID-001 - 002 - task-due-today-filter-chip.md` | `replies/PID-001-turn2.txt` |
| `PIR-001 - 001 - intake-guest-loyalty-points-clarification.md` | `replies/PIR-001-turn1.txt` |
| `PIR-001 - 002 - Epic-guest-loyalty-points.md` | `replies/PIR-001-turn2.txt` |
| `PIR-002 - 001 - intake-wishlist-across-devices-clarification.md` | `replies/PIR-002-turn1.txt` |
| `PIR-002 - 002 - Story-customer-wishlist-account-wishlist-in-apps.md` | `replies/PIR-002-turn2.txt` |
| `PST-001 - NNN - Story-free-cancellation-filter-clarification.md` | `replies/PST-001-turn1.txt` |
| `PST-001 - NNN - Story-free-cancellation-filter.md` | `replies/PST-001-turn2.txt` |
| `PST-002 - NNN - Story-member-sharing-view-only-links (turn 2).md` | `replies/PST-002-turn2.txt` |
| `PST-002 - NNN - Story-member-sharing-view-only-links.md` | `replies/PST-002-turn1.txt` |
| `PST-003 - fernhouse-save-card-draft (turn 2).md` | `replies/PST-003-turn2.txt` |
| `PST-003 - fernhouse-save-card-draft.md` | `replies/PST-003-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline (turn 2).md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.1 - task-ios-tracking-timeline.md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.1 - task-tracking-webhook.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.2 - task-android-tracking-timeline.md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.2 - task-packed-status.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline (turn 2).md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.4 - task-ios-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.4 - task-tracking-webhook.md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.5 - task-android-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.6 - task-tracking-timeline-events.md` | `replies/PST-004-turn1.txt` |
| `PTK-001 - NNN - task-free-shipping-banner-copy.md` | `replies/PTK-001-turn1.txt` |
| `PTK-002 - 001 - task-date-picker-stay-limits (turn 2).md` | `replies/PTK-002-turn2.txt` |
| `PTK-002 - 001 - task-date-picker-stay-limits.md` | `replies/PTK-002-turn1.txt` |
| `PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels (turn 2).md` | `replies/PTK-003-turn2.txt` |
| `PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels.md` | `replies/PTK-003-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos (turn 2).md` | `replies/PTK-004-turn2.txt` |
| `PTK-004 - NNN - task-recurring-todos-android.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos-be.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos-ios.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos-web.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos.md` | `replies/PTK-004-turn1.txt` |
| `PTK-005 - NNN - task-android-recurring-todos (turn 2).md` | `replies/PTK-005-turn2.txt` |
| `PTK-005 - NNN - task-android-recurring-todos.md` | `replies/PTK-005-turn1.txt` |
| `PTK-006 - 001 - task-booking-funnel-events-clarification.md` | `replies/PTK-006-turn1.txt` |
| `PTK-006 - 002 - task-booking-funnel-event-checks.md` | `replies/PTK-006-turn2.txt` |

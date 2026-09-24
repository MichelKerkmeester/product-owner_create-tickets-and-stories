# Independent verdict, Product Owner, 2026-09-17 manual testing playbook run

Written by a reader who built none of this system's instruments and ran none of its
playbook. Every count below comes from walking a directory or parsing a file myself,
or from running the cited command myself, never from a number typed in this report's
own prose. Where a check disagreed with a document I treated the check as innocent
first. Read-only throughout: nothing under `Product Owner`, `z — Parity Gate` or
`z — Knowledge` was edited, and the two grader tools that write output files
(`lint_replies.py`, its `hvr-lint.csv`) were run once against the real report to
confirm they reproduce its own numbers, then re-run only against scratch copies for
every injection test. `git status` on the tree stayed clean after every run reported
below.

---

## Verdict 1: checks proved by injection

**Upheld.** I reproduced the injection proof myself for all three of this system's
grader-family checks, not just one.

- `python3 benchmark/gates/rule_parity.py` on the real tree: exit 0, `PASSED 6 rules
  hold on both sides of every pair that teaches them`
- Built a sandbox with `cp -RL` (symlinks dereferenced, matching the method the
  gate's own `README.md` section 6 documents), confirmed it is green unmodified
  under `CW_ROOT`, then changed one word in the sandbox's
  `sk-product-owner/references/hvr-core.md` (`never end with a full stop` to
  `should not end with a period`, one side of one declared pair only). Re-run under
  `CW_ROOT` against the same sandbox: exit 1, `FAILED 1 rule parity finding(s)`,
  naming the exact drift (`appears 0x ... and 1x in its mirror`). The real tree
  re-checked clean immediately after, `git status --short` empty
- `python3 benchmark/grader/lint_replies.py` on the real report: exit 1, `3 clean of
  28`, matching section 8's claim exactly. Copied the report to scratch, appended one
  em dash to the one clean file `SID-001-turn1.txt`, re-ran: the file flips to
  `DIRTY em_dashx1` and the clean count drops from 3 to 2
- `python3 benchmark/grader/twin_divergence.py` on the real report: exit 1, `5
  twin(s) agreed, 2 disagreed`, matching section 7 and `adjudication.md` line 5
  exactly. Copied `results.csv` to scratch, flipped `PTK-001` from `FAIL` to `PASS`,
  re-ran: `6 twin(s) agreed, 1 disagreed`, the exact direction a real fix would move it
- `bash benchmark/grader/check_report.sh` on the real report: exit 2, both checks
  printing findings, matching section 8's `exited 2 (two of two checks reported
  findings)` line for line

One qualification. `benchmark/gates/README.md` section 6 documents its own injection
method in the tracked record itself. `benchmark/grader/README.md` carries no
equivalent section for `lint_replies.py` or `twin_divergence.py`, so before I ran the
tests above, the only claim that those two were ever proved red was the terse fleet
commit message at `c2d9e7d` ("each proved red on an injection before being believed"),
with no lane log preserved in the tracked tree (the phase-1 episode's own spec folder
is stated as gitignored in `z — Parity Gate/episodes/hand-run/011-fleet-capability-leak/handover.md`
line 15). The standard is met because I did the reproduction myself and it held on
the first attempt for every check tried. It would not have been met by reading the
tracked record alone.

## Verdict 2: full coverage, no verdict on an unfinished run, the probe correctly excluded

**Upheld.**

- `find "sk-product-owner/manual-testing-playbook" -type f -name "*.md" | wc -l` = 15
- All 14 scenario files independently confirmed two-turn, counting `| 1 |` and `| 2 |`
  conversation-chain rows with a null-delimited `find -print0 | sort -z | while read`
  loop (the space-safe form, since the repo path itself contains a space): every one
  of the 14 files returns exactly 2 matching rows, 0 returning 1 or 3
- `find .../replies -type f | wc -l` = 28. `find -iname "*probe*"` against that
  directory (case-insensitive, so `probe` and `PROBE` both match) returns nothing
- `find .../evidence -type f | wc -l` = 1, the retrieval probe. Its content: three
  named files, its own claimed count of 40, all matching `README.md` section 1
  verbatim. All three named files exist on disk in `claude project/knowledge/`,
  checked by path
- `find .../claude project/knowledge -type f | wc -l` = 38, confirming the probe's own
  miscount (40 vs 38) independently of the report's characterization of it
- `lint_replies.py` run directly against the report counts exactly 28 reply files and
  reports `3 clean of 28`, so the clean rate the report cites is the 28-reply
  denominator, not 29
- `results.csv` has exactly 14 data rows (`tail -n +2 | wc -l`)

## Verdict 3: both twin divergences adjudicated and tested from a second direction

**Upheld.**

- `twin_divergence.py` run directly against the report reproduces `BG-001: skill
  PASS, Project FAIL`, `TK-001: skill PASS, Project FAIL`, `5 ... agreed, 2 ...
  disagreed`, matching both `README.md` section 7 and `adjudication.md` line 5
- `adjudication.md` section 3 is a genuine second direction, not a restatement: fresh
  turn-1-only samples (10 skill, 14 Project) found the skill side also fails the
  `TK-001` clarification turn (2 of 8) and the Project side also passes `BG-001` (3 of
  3), directly against the committed run's one-sample read
- `sampling.md` (phase 4) is a third pass, pre-registered discriminators scored
  against reply text before any new sample ran. I counted its evidence independently
  rather than reading its tables: `find samples -name "*-turn1.txt" | wc -l` = 43,
  `-name "*-turn2.txt"` = 24, `-name "*.transcript.txt"` = 39,
  `tail -n +2 manifest.csv | wc -l` = 43, matching section 3's own count exactly. I
  then cross-tabulated `manifest.csv`'s `pair,arm,sample,origin,turn1_verdict` columns
  by hand (`awk`/`sort`/`uniq -c`) against every cell of both distribution tables in
  section 4, for both pairs and all three origins (new, reused, committed): every cell
  agreed with the manifest
- The two committed-run samples on each side (`BG-001-*-committed-turn1.txt`,
  `TK-001-*-committed-turn1.txt`) are byte-identical (`diff`, no output) to
  `replies/SBG-001-turn1.txt`, `replies/PBG-001-turn1.txt`,
  `replies/STK-001-turn1.txt`, `replies/PTK-001-turn1.txt`, so the sampling
  measurement is provably built on the actual committed replies, not a re-typed
  approximation
- Verdicts match what the brief describes: `BG-001` is called a draw (the committed
  failure form, all three elements absent, reproduces 0 of 8 non-committed Project
  samples), `TK-001` is called a real direction whose paired verdict reproduces only
  "about three paired draws in five" and is not carried forward as settled

## Verdict 4: repairs landed on both sides, runtime faults recorded unrepaired

**Upheld.**

- The Task Mode caveat repair (commit `173a3b7`, `fix(product-owner): an explicit
  command routes a request, it does not complete one`) changed
  `sk-product-owner/references/task-mode.md` line 50 and
  `claude project/knowledge/Product Owner - Templates - Task Mode - v0.304.md` line
  30 to byte-identical text (`grep` on both files, same string, confirmed character
  for character). It reached both sides
- The cited row says what the repair claims it says. `awk 'NR==124'` on
  `sk-product-owner/references/interactive-mode.md` reads: `**Direct Task or Bug**
  (\`$task\`/\`$bug\`) | Context-specific question → Wait → Process → Deliver`. That
  is a context-specific question and a wait, named for an explicit command, exactly
  what the commit says the old caveat contradicted
- The kernel prescriptive-delivery repair (commit `fb08df0`) is Project-kernel-only by
  its own text ("Skill unchanged, because no skill rule changed and the skill
  packaging legitimately writes files"), so it is not a both-sides repair and the
  brief does not ask it to be one. `claude project/Custom Instructions.md` line 88
  now reads the added sentence, kernel at `v1.12.1`
- Denominator check on the `BG-001` runtime-fault entry: it says the committed
  failure form "reproduces 0 times across the 8 Project samples taken since, 5 new
  and 3 reused. The ninth Project sample ... is the committed failure itself." Against
  `manifest.csv`, counted directly: 5 rows `BG-001,project,new`, 3 rows
  `BG-001,project,reused`, 1 row `BG-001,project,committed`, total 9, and the FAIL
  breakdown in that count matches `sampling.md` section 4's table cell for cell. No
  disagreement
- Both faults are genuinely unrepaired, checked against the live files rather than
  taken on the record's word: `Custom Instructions.md` line 229 still frames the
  export list as "a naming convention rather than paths the Project wrote" and
  neither Task Mode document carries a clarification-delivery rule (`grep -ic
  "clarif"` returns 2 in each, both the unrelated verb "clarifies", not the noun,
  confirmed by reading both lines)

## Verdict 5: no count in the record disagrees with the tree

**Not upheld.** One count does disagree, found by re-summing a table the report
itself provides.

`README.md` section 4's "Counts per packaging" table gives Skill `PASS 4, FAIL 3` and
Project `PASS 2, FAIL 5`, both of which check out (`results.csv`: SID-001, STK-001,
SBG-001, SDK-002 pass on the skill side, PID-001 and PDK-002 pass on the Project side,
the other eight fail). Its own `Combined` row then states `FAIL 9`. The correct sum of
its own two rows above it is `3 + 5 = 8`, and the row's own four cells do not even sum
to its own stated total (`6 + 9 + 0 + 0 = 15`, against a stated `Total 14`). Counted
directly against `results.csv`: 8 FAIL rows (`SDK-001, SST-001, SIR-001, PTK-001,
PBG-001, PDK-001, PST-001, PIR-001`), 6 PASS rows. The correct figure, 8, is what the
report's own section 5 and 6 prose names when it lists the failures individually, and
it is what the independent fleet-level handover table gives for this system
(`z — Parity Gate/episodes/hand-run/011-fleet-capability-leak/handover.md` line 35,
`Product Owner | 14 | 6 | 8 | 2`). So this is an isolated arithmetic slip in one table
cell of `README.md`, not a sign of a different underlying dataset. It is still a
count in the record that disagrees with the tree, which is what this verdict is
about.

Every other count I independently re-derived agreed with the tree: 14 scenario files
(15 minus the root), 28 replies, 1 evidence file, 38 knowledge files, 38 declared
pairs (`validate_parity.py product-owner`, `PASSED 38/38`), 43/24/39 sample files
against 43 manifest rows, every cell of `sampling.md`'s two distribution tables
against `manifest.csv`, 3 of 28 clean replies, 5 agreed and 2 disagreed twins, and the
residency check (`residency_check.py product-owner`, `PASSED 1 system(s), every
declared statement owned and placed`).

---

## Commands run, for anyone reproducing this record

```bash
python3 "AI Systems/Product Owner/benchmark/gates/rule_parity.py"
python3 "AI Systems/Product Owner/benchmark/grader/lint_replies.py" "AI Systems/Product Owner/benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium"
python3 "AI Systems/Product Owner/benchmark/grader/twin_divergence.py" "AI Systems/Product Owner/benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium"
bash "AI Systems/Product Owner/benchmark/grader/check_report.sh" "AI Systems/Product Owner/benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium"
python3 "z — Parity Gate/validate_parity.py" product-owner
python3 "z — Parity Gate/residency_check.py" product-owner
```

Sandbox and injection commands are one-off `cp -RL`, `sed -i ''`, and re-runs with
`CW_ROOT` set, all against a scratch copy under this session's own scratchpad
directory, never against the tracked tree. `git status --short -- "AI Systems/Product
Owner"` was empty before and after every run in this record.

---

## The single most significant thing found and not already recorded

A dead cross-reference left by the caveat repair's own repoint tool, in the live
tree, undetected by every check that currently runs over this system.

`sk-product-owner/manual-testing-playbook/project-backlog-modes/task-command-flow.md`
line 89 reads:

```
| [`Product Owner - Templates - Task Mode - v0.304.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.303.md) | Project task workflow and structure rules |
```

The link text was repointed to the new filename (`v0.304.md`) but its `href` was not,
and still names `v0.303.md`, the file the same repair commit (`173a3b7`) renamed away.
Confirmed the target does not resolve
(`os.path.exists` on the decoded, normalized path returns `False`), and confirmed by a
full re-run of the same link-walk the earlier playbook verification episode used
(`z — Parity Gate/episodes/playbook-verification/005-product-owner/verdict-round-two.md`,
which found 0 of 113 broken before this repair landed) that this is the only broken
link in the package now: 113 links checked, 1 broken, exactly this one. Every other
`v0.303` string left in the tree by the same commit is a dated log entry
(`SYNC.md`, `adjudication.md`, or a sample transcript) that the repoint tool correctly
declined to touch, per the commit's own stated policy, so this is not a case of the
tool over-applying its rule. It under-applied it on this one line: it rewrote the
link's visible label and left the address pointing at a file that no longer exists.
`validate_parity.py` and `residency_check.py` both pass clean on this system because
neither checks markdown link targets inside `manual-testing-playbook/`, so nothing
currently in the fleet's own gate set would catch this.

---

## Summary for the record

| Claim | Verdict |
| --- | --- |
| 1. Checks proved by injection | Upheld, reproduced independently for all three grader-family checks plus the gate |
| 2. Full coverage, no verdict on an unfinished run | Upheld |
| 3. Both divergences adjudicated and tested from a second direction | Upheld |
| 4. Repairs landed on both sides, runtime faults recorded unrepaired | Upheld |
| 5. No count disagrees with the tree | Not upheld, one table cell in `README.md` section 4 (`Combined FAIL 9`, should be `8`) |

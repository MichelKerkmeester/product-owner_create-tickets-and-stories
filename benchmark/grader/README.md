---
title: "Grader: reply linter, twin comparison and the report runner"
description: "Checks output rules against captured replies and pairs skill/Project twins by the manual playbook's own scenario ids"
trigger_phrases:
  - "reply linter"
  - "twin divergence"
  - "check report"
---

# Grader: reply linter, twin comparison and the report runner

* * *

## 1. Overview

`benchmark/grader/` reads a finished `sk-product-owner/manual-testing-playbook/` run report and checks two things `benchmark/gates/rule_parity.py` cannot: whether the captured reply text actually obeys the Human Voice hard blockers, and whether the skill and Project twin of a scenario reached the same verdict. Neither existed for this system before. There was no grader at all, so `hvr_lint.py` had to be built here from `references/hvr-core.md` rather than imported from elsewhere.

Current state:

*   Five files: the linter, the two checks that walk a report, the runner that chains them, and this README
*   Nothing here edits a reply or a result. A dirty finding is a fact about one playbook run, not a repository defect
*   All three Python entry points accept a report directory. `lint_replies.py` also accepts one file with `--brief`

* * *

## 2. Files

| File | Responsibility |
|---|---|
| `hvr_lint.py` | The linter itself. Reads `references/hvr-core.md` Sections 2 through 5 and 9, deterministic checks only, no model judgement |
| `lint_replies.py` | Walks a report's `replies/` directory, lints every `.md`/`.txt` file through `hvr_lint.py`, writes `hvr-lint.csv` beside it |
| `twin_divergence.py` | Reads a report's `results.csv`, pairs an `S`-id with its `P`-id, reports any pair whose verdicts disagree |
| `check_report.sh` | Runs `lint_replies.py` and `twin_divergence.py` over the same report directory, continues past a finding, exits with how many reported |

* * *

## 3. What the linter checks, and what it deliberately does not

`hvr_lint.py` enforces, all deterministic:

*   **Punctuation** (`references/hvr-core.md` Section 2): em dash, semicolon, curly quotes, more than one ellipsis, a bullet line closed with a period. Em dash carries the two granted exemptions the same section names, the ClickUp definition delimiter and the status-label delimiter, matched by the shape of the line rather than assumed from the whole document
*   **The hard blocker word list** (Section 3), word-boundary matched with an optional trailing `s` so `leverages` is caught alongside `leverage`. The six terms Section 3 calls "blocked as metaphor, allowed when literal" (navigating, landscape, unlock, ecosystem, journey, deep dive) are left out, because telling literal from figurative use needs a reader
*   **The hard blocker phrase list** (Section 4) and **the banned metaphors and cliches** (Section 5)
*   **One Section 9 structural ban**, `not just X, but Y` and its `not only` variant, plus a narrowed copula-avoidance list (`serves as`, `stands as`, `functions as`, `acts as`, `boasts`, with `features` and `offers` left out as ordinary words too common in backlog prose to flag as bare terms)

Left out on purpose, and named so a green result is not read as covering more than it does: the Oxford comma, asterisk emphasis used mid-sentence versus the same asterisks used as a sanctioned structural label, title-case headings, and the document-wide Section 9 bans that need a count across the whole piece rather than a span match (triad density, synonym cycling, false ranges, notability by association). Section 10, "Always cut," is out because `references/hvr-core.md` states outright that those terms are edits and never count toward the hard blocker total.

* * *

## 4. Extraction confidence

A Product Owner delivery reply is supposed to carry its `HVR self-scan:` line and a handful of metadata lines (`Path:`, `Verified:`, `Export path:`, `Export-equivalent path:`, `Mode:`, `Quality Score:`, and similar) beside the artifact, never inside it. The self-scan line in particular exists to name the terms it fixed, so scanning it as prose would fail a clean delivery on its own compliance report. When `hvr_lint.py` finds and strips that shape, confidence is `high`. A reply with none of it is prose throughout, either a plain chat answer or a capture that lost its structure, so confidence is `low` and phrase-shaped findings (the word and phrase lists, the metaphors, the copula list) are downgraded to `soft`. Punctuation and the fixed word list stay `hard` regardless, because an em dash is an em dash whether it sits in reasoning or in a shipped artifact.

* * *

## 5. Scenario ids and the twin pairing

`sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` runs 14 scenarios as seven twins, one skill run and one Project run per twin, `S`-prefixed and `P`-prefixed over the same category letters and number: `SID-001`/`PID-001`, `STK-001`/`PTK-001`, `SBG-001`/`PBG-001`, `SDK-001`/`PDK-001`, `SDK-002`/`PDK-002`, `SST-001`/`PST-001`, `SIR-001`/`PIR-001`. `twin_divergence.py` pairs by that scheme, confirmed by reading the playbook's own coverage map rather than assumed. A pair is the unit: a scenario run on only one side is named as unpaired, never counted as agreement. A pair with a `PARTIAL` side (most scenarios here run two turns) is named apart from the pairs that agreed rather than compared, because a run that only reached Turn 1 is evidence about Turn 1 alone. An id carrying a suffix after the number is a variant, a re-run or a diagnostic capture, and is listed rather than paired.

* * *

## 6. The report directory shape

Neither `results.csv` nor a `replies/` directory existed anywhere in this system before this benchmark tree, so this is the shape these three tools were built to read:

```text
<report-dir>/
    results.csv          # id,result  (id like SID-001 or PID-001, result PASS, FAIL, SKIP or PARTIAL)
    replies/
        SID-001.md        # the captured reply text for that scenario id
        PID-001.md
        ...
```

`results.csv`'s `id` values are the playbook's own scenario ids. `lint_replies.py` also accepts a bare `replies/` directory, or a single reply file with `--brief` for a one-line result a per-scenario capture step can print without a JSON reader.

* * *

## 7. Run

Over a finished report directory, from the system root:

```bash
bash benchmark/grader/check_report.sh /path/to/report-dir
```

Expected result on a clean report: both checks print `clean`, then `all 2 report checks clean`. Exit 0.

Individually:

```bash
python3 benchmark/grader/lint_replies.py /path/to/report-dir
python3 benchmark/grader/twin_divergence.py /path/to/report-dir
python3 benchmark/grader/hvr_lint.py /path/to/one-reply.md
python3 benchmark/grader/lint_replies.py /path/to/one-reply.md --brief
```

* * *

## 8. Exit codes

`lint_replies.py` and `twin_divergence.py`:

| Exit | Meaning |
|---|---|
| 0 | every reply clean, or every paired twin agreed |
| 1 | at least one reply carries a hard blocker, or at least one pair disagreed |
| 2 | nothing to check: no report directory, no reply files, no `results.csv`, or no row carries a twin id |
| 64 | usage error, no argument given |

`check_report.sh` counts checks that reported findings, not checks that failed to run:

| Exit | Meaning |
|---|---|
| 0 | both checks clean |
| 1 | one check reported findings |
| 2 | both checks reported findings |
| 64 | usage error, no argument given |
| 66 | the report directory does not exist. Not 2, because with exactly two checks in the loop `found` can itself reach 2, and a caller could not tell that apart from a missing directory. 66 matches `benchmark/format/validate-output-format.cjs`, which already uses it for an unreadable target path |

* * *

## 9. Related

*   [`../gates/README.md`](../gates/README.md), the pair-level rule check this reply linter and twin comparison do not replace
*   [`references/hvr-core.md`](../../sk-product-owner/references/hvr-core.md), the source of every check in `hvr_lint.py`
*   [`manual-testing-playbook.md`](../../sk-product-owner/manual-testing-playbook/manual-testing-playbook.md), the scenario ids, the coverage map and the two-turn shape `PARTIAL` exists for

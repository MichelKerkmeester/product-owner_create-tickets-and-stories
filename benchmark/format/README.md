---
title: "Format: output validator and fixture runner"
description: "Runs fixed Markdown cases through the Product Owner output format validator"
trigger_phrases:
  - "output format validator"
  - "format fixtures"
  - "Product Owner format benchmark"
---

# Format: output validator and fixture runner

* * *

## 1. Overview

`benchmark/format/` contains a Bash fixture runner, a Node validator and a Markdown fixture corpus. The runner fixes the validator and fixture directory in variables, while the validator parses flags and target paths (`run_fixtures.sh:1-27`, `validate-output-format.cjs:1-23`)

Current state:

*   `run_fixtures.sh` compares expected exit status, required output and forbidden output for each case, records mismatches and prints a pass line for cases that clear all checks (`run_fixtures.sh:33-61`)
*   `validate-output-format.cjs` walks source directories recursively, skips symlinks and selects Markdown files for its source inventory (`validate-output-format.cjs:36-42`)
*   Explicit validator targets use artifact checks, while no target uses the validator's source inventory (`validate-output-format.cjs:51-65`)
*   Missing or non-regular targets return exit 66 before file analysis (`validate-output-format.cjs:67-78`)

* * *

## 2. Architecture

```text
+------------------------------+
| run_fixtures.sh              |
| run_fixtures.sh:25-61        |
+---------------+--------------+
                | fixture paths
                v
+------------------------------+
| validate-output-format.cjs   |
| validate-output-format.cjs   |
| :53-67                       |
+----------+-------------------+
           | explicit targets
           v
+------------------------------+
| per-file analysis             |
| validate-output-format.cjs   |
| :809-1058                    |
+----------+-------------------+
           v
+------------------------------+
| reports and exit status       |
| validate-output-format.cjs   |
| :1291-1307                   |
+------------------------------+

No target paths:
validate-output-format.cjs:51-65
source inventory -> per-file analysis -> reports
```

`run_fixtures.sh` passes fixed fixture paths to the validator. A call without target paths uses the source inventory instead, and both paths reach the same per-file analysis and final reporting (`run_fixtures.sh:25-37, 69-167`, `validate-output-format.cjs:51-78, 842-866, 1202-1344`)

Dependency direction:

```text
run_fixtures.sh -> validate-output-format.cjs
run_fixtures.sh -> fixtures/*.md
validate-output-format.cjs -> explicit target files
validate-output-format.cjs -> source inventory when no targets are supplied
```

The runner supplies fixture paths as command-line arguments to the validator, and the validator selects either those targets or its source inventory (`run_fixtures.sh:25-37, 69-167`, `validate-output-format.cjs:51-65`)

* * *

## 3. Package topology

```text
benchmark/format/
+-- README.md
+-- run_fixtures.sh
+-- validate-output-format.cjs
`-- fixtures/
    +-- conciseness-silent.md
    +-- conciseness-violation.md
    +-- delivery-placeholder-exempt.md
    +-- delivery-placeholder-violation.md
    +-- house-grammar-silent.md
    +-- house-grammar-violation.md
    +-- markasdone-divider-violation.md
    +-- mask-paths-exempt.md
    +-- mask-paths-violation.md
    +-- requirements-narration-exempt.md
    +-- requirements-narration-violation.md
    +-- sanctioned-definition-nested.md
    `-- sanctioned-shapes.md
```

The runner owns case selection and result comparison. The validator owns file selection, per-file checks and final status, while the fixture files supply the Markdown inputs (`run_fixtures.sh:33-61, 69-167`, `validate-output-format.cjs:64-78, 842-866, 1328-1344`)

Allowed dependency direction:

```text
run_fixtures.sh -> validate-output-format.cjs -> selected files
run_fixtures.sh -> fixtures/*.md as validator arguments
```

* * *

## 4. Directory tree

```text
benchmark/format/
+-- README.md
+-- run_fixtures.sh
+-- validate-output-format.cjs
`-- fixtures/
    +-- conciseness-silent.md
    +-- conciseness-violation.md
    +-- delivery-placeholder-exempt.md
    +-- delivery-placeholder-violation.md
    +-- house-grammar-silent.md
    +-- house-grammar-violation.md
    +-- markasdone-divider-violation.md
    +-- mask-paths-exempt.md
    +-- mask-paths-violation.md
    +-- requirements-narration-exempt.md
    +-- requirements-narration-violation.md
    +-- sanctioned-definition-nested.md
    `-- sanctioned-shapes.md
```

`run_fixtures.sh:69-167` names every fixture path used by the runner. The fixture responsibilities are listed below with the lines that define each input

* * *

## 5. Key files

| File | Responsibility |
|---|---|
| `run_fixtures.sh` | Sets the validator and fixture paths, runs fixed cases and reports aggregate failure or success (`run_fixtures.sh:25-61, 169-173`) |
| `validate-output-format.cjs` | Parses flags and targets, selects source or artifact mode, analyzes each file and reports the result (`validate-output-format.cjs:20-34, 51-78, 842-866, 1202-1344`) |
| `fixtures/conciseness-silent.md` | Holds near-miss cases for exact token binding, export read-back, one hedge, quoted vocabulary and fallback intake (`conciseness-silent.md:1-27`) |
| `fixtures/conciseness-violation.md` | Holds opener, heading echo, hedge stack and terminal recap cases (`conciseness-violation.md:1-22`) |
| `fixtures/delivery-placeholder-exempt.md` | Uses an explicit estimate and two placeholder slots so its Delivery section is not placeholder-only (`delivery-placeholder-exempt.md:20-39`) |
| `fixtures/delivery-placeholder-violation.md` | Uses placeholders in Estimation, Rabbit holes and No-gos to trigger the Delivery advisory (`delivery-placeholder-violation.md:20-39`) |
| `fixtures/house-grammar-silent.md` | Carries a compliant payout example with a Requirements value, one punctuation exception set, Delivery placeholders and ordinary quality-check prose (`house-grammar-silent.md:1-78`) |
| `fixtures/house-grammar-violation.md` | Combines a missing divider, wrong divider, deep heading, Requirements checklist and checkbox, asterisk emphasis, repeated priority markers, extra ellipses and extra emoji (`house-grammar-violation.md:5-37`) |
| `fixtures/markasdone-divider-violation.md` | Places a divider after the first Mark as done checkbox, then closes the final criterion with a divider above a spacer heading (`markasdone-divider-violation.md:9-26`) |
| `fixtures/mask-paths-exempt.md` | Holds two path examples whose structural punctuation should stay exempt (`mask-paths-exempt.md:3-9`) |
| `fixtures/mask-paths-violation.md` | Holds three prose dash examples that the path mask must leave visible (`mask-paths-violation.md:3-10`) |
| `fixtures/requirements-narration-exempt.md` | Quotes one screen string and keeps the other bullets as constraints (`requirements-narration-exempt.md:3-12`) |
| `fixtures/requirements-narration-violation.md` | Uses two bullets that report what a screen says without quoting the copy, plus one action bullet (`requirements-narration-violation.md:3-11`) |
| `fixtures/sanctioned-definition-nested.md` | Checks definition bullets at column zero and two deeper indentation levels (`sanctioned-definition-nested.md:1-8`) |
| `fixtures/sanctioned-shapes.md` | Places definition and status shapes in list, checkbox and blockquote containers, then includes a section status line (`sanctioned-shapes.md:3-21`) |

* * *

## 6. Boundaries and flow

| Boundary | Rule |
|---|---|
| Arguments | `validate-output-format.cjs` accepts `--write`, flags and target paths, then rejects unknown flags or `--write` with explicit targets (`validate-output-format.cjs:20-34`) |
| Source inventory | No explicit target selects the system files, shared cards and Markdown files found under the skill references and assets (`validate-output-format.cjs:36-60, 64-65`) |
| Target type | Explicit targets must exist and be regular files before analysis begins (`validate-output-format.cjs:67-78`) |
| Artifact checks | Explicit targets receive purity, shape, Delivery, punctuation, Requirements, voice and conciseness checks, plus length-cap advice (`validate-output-format.cjs:868-979, 981-1095`) |
| Writing | `--write` is allowed only without explicit targets and writes a changed formatted source file (`validate-output-format.cjs:31-34, 1202-1225`) |
| Results | Unknown flag combinations return 64, unreadable targets return 66, validation errors return 1 and a clean run prints a passed scope (`validate-output-format.cjs:25-34, 70-78, 1337-1344`) |

`validate-output-format.cjs:20-34, 51-78, 842-866 and 1291-1307` establish the path from argument parsing through file selection, analysis and result reporting

```text
process.argv
  -> flags and targets : validate-output-format.cjs:20-34
  -> file set          : validate-output-format.cjs:51-78
  -> per-file analysis : validate-output-format.cjs:842-866
  -> checks            : validate-output-format.cjs:868-1195
  -> output            : validate-output-format.cjs:1328-1344
```

* * *

## 7. Entrypoints

| Entrypoint | Type | Purpose |
|---|---|---|
| `run_fixtures.sh` | Bash script | Changes to its own directory and defines the fixed validator and fixture paths (`run_fixtures.sh:1-27`) |
| `validate-output-format.cjs [--write] [file ...]` | Node CLI | Accepts the write flag or target files according to its usage contract (`validate-output-format.cjs:20-34`) |
| `PO_FORMAT_STATS=1` | Environment flag | Prints per-file statistics after analysis (`validate-output-format.cjs:1134-1153, 1332-1334`) |

* * *

## 8. Validation

Run the fixture harness from the repository root:

```bash
bash 'AI Systems/Product Owner/benchmark/format/run_fixtures.sh'
```

The harness prints `PASSED all format-validator fixtures` and returns exit 0 when no case increments `failures`. A mismatch prints the failed case and returns exit 1 (`run_fixtures.sh:33-61, 169-173`)

For a direct file check, use the validator form declared in its usage line:

```bash
node 'AI Systems/Product Owner/benchmark/format/validate-output-format.cjs' path/to/file.md
```

The direct form accepts one or more target paths, and `--write` is reserved for source mode (`validate-output-format.cjs:25-34, 51-65`)

* * *

## 9. Related

*   [`../router/README.md`](../router/README.md) documents the sibling executable route contract and its fixture runner (`../router/README.md:1-23`)
*   [`../parity/README.md`](../parity/README.md) documents sibling wrappers that pass system data into the shared parity gate (`../parity/README.md:13-32`)

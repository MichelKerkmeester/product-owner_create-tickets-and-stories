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

`benchmark/format/` contains a Bash fixture runner, a Node validator and a Markdown fixture corpus. The runner fixes the validator and fixture directory in variables, while the validator parses flags and target paths (`run_fixtures.sh:1-27`, `validate-output-format.cjs:1-25`)

Current state:

*   `run_fixtures.sh` compares expected exit status, required output and forbidden output for each case, records mismatches and prints a pass line for cases that clear all checks (`run_fixtures.sh:34-69`)
*   `validate-output-format.cjs` walks source directories recursively, skips symlinks and selects Markdown files for its source inventory (`validate-output-format.cjs:38-45`)
*   Explicit validator targets use artifact checks, while no target uses the validator's source inventory (`validate-output-format.cjs:53-81`)
*   Missing or non-regular targets return exit 66 before file analysis (`validate-output-format.cjs:84-95`)

* * *

## 2. Architecture

```text
+------------------------------+
| run_fixtures.sh              |
| run_fixtures.sh:26-69        |
+---------------+--------------+
                | fixture paths
                v
+------------------------------+
| validate-output-format.cjs   |
| validate-output-format.cjs   |
| :53-81                       |
+----------+-------------------+
           | explicit targets
           v
+------------------------------+
| per-file analysis             |
| validate-output-format.cjs   |
| :1181-1553                   |
+----------+-------------------+
           v
+------------------------------+
| reports and exit status       |
| validate-output-format.cjs   |
| :1687-1703                   |
+------------------------------+

No target paths:
validate-output-format.cjs:53-81
source inventory -> per-file analysis -> reports
```

`run_fixtures.sh` passes fixed fixture paths to the validator. A call without target paths uses the source inventory instead, and both paths reach the same per-file analysis and final reporting (`run_fixtures.sh:26-38, 75-235`, `validate-output-format.cjs:53-95, 1561-1585, 1587-1703`)

Dependency direction:

```text
run_fixtures.sh -> validate-output-format.cjs
run_fixtures.sh -> fixtures/*.md
validate-output-format.cjs -> explicit target files
validate-output-format.cjs -> source inventory when no targets are supplied
```

The runner supplies fixture paths as command-line arguments to the validator, and the validator selects either those targets or its source inventory (`run_fixtures.sh:26-38, 75-235`, `validate-output-format.cjs:53-81`)

* * *

## 3. Package topology

```text
benchmark/format/
+-- README.md
+-- run_fixtures.sh
+-- validate-output-format.cjs
`-- fixtures/
    +-- catalog-entry-no-index.md
    +-- catalog-entry-silent.md
    +-- catalog-entry-violation.md
    +-- checkbox-form-violation.md
    +-- conciseness-silent.md
    +-- conciseness-violation.md
    +-- delivery-placeholder-exempt.md
    +-- delivery-placeholder-violation.md
    +-- house-grammar-silent.md
    +-- house-grammar-violation.md
    +-- length-caps-silent.md
    +-- length-caps-violation.md
    +-- markasdone-divider-violation.md
    +-- mask-paths-exempt.md
    +-- mask-paths-violation.md
    +-- requirements-narration-exempt.md
    +-- requirements-narration-violation.md
    +-- sanctioned-definition-nested.md
    `-- sanctioned-shapes.md
```

The runner owns case selection and result comparison. The validator owns file selection, per-file checks and final status, while the fixture files supply the Markdown inputs (`run_fixtures.sh:34-69, 75-235`, `validate-output-format.cjs:80-95, 1561-1585, 1696-1703`)

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
    +-- catalog-entry-no-index.md
    +-- catalog-entry-silent.md
    +-- catalog-entry-violation.md
    +-- checkbox-form-violation.md
    +-- conciseness-silent.md
    +-- conciseness-violation.md
    +-- delivery-placeholder-exempt.md
    +-- delivery-placeholder-violation.md
    +-- house-grammar-silent.md
    +-- house-grammar-violation.md
    +-- length-caps-silent.md
    +-- length-caps-violation.md
    +-- markasdone-divider-violation.md
    +-- mask-paths-exempt.md
    +-- mask-paths-violation.md
    +-- requirements-narration-exempt.md
    +-- requirements-narration-violation.md
    +-- sanctioned-definition-nested.md
    `-- sanctioned-shapes.md
```

`run_fixtures.sh:75-235` names every fixture path used by the runner. The fixture responsibilities are listed below with the lines that define each input

* * *

## 5. Key files

| File | Responsibility |
|---|---|
| `run_fixtures.sh` | Sets the validator and fixture paths, runs fixed cases and reports aggregate failure or success (`run_fixtures.sh:26-69, 241-245`) |
| `validate-output-format.cjs` | Parses flags and targets, selects source or artifact mode, analyzes each file and reports the result (`validate-output-format.cjs:22-36, 53-95, 1561-1585, 1587-1703`) |
| `fixtures/catalog-entry-silent.md` | Carries a Catalog with its Index heading, two entry headings and two entry links, each with one dash between the stable ID and the entry name, so the narrow Catalog grant clears the gate (`catalog-entry-silent.md:1-31`) |
| `fixtures/catalog-entry-violation.md` | Keeps the Index heading and puts the same dash on a title, a heading with no stable ID, prose, a second dash, an H2 and a link with trailing text, each of which still blocks (`catalog-entry-violation.md:1-27`) |
| `fixtures/catalog-entry-no-index.md` | Carries the entry heading and link shapes with no Index heading, so the grant earns nothing outside a Catalog (`catalog-entry-no-index.md:1-11`) |
| `fixtures/checkbox-form-violation.md` | Writes one requirement checkbox and one Mark as done checkbox in the spaced `- [ ]` form beside the house `- []` form, so only the spaced lines fire and an old-form checkbox still trips the divider check |
| `fixtures/conciseness-silent.md` | Holds near-miss cases for exact token binding, export read-back, one hedge, quoted vocabulary and fallback intake (`conciseness-silent.md:1-27`) |
| `fixtures/conciseness-violation.md` | Holds opener, heading echo, hedge stack and terminal recap cases (`conciseness-violation.md:1-22`) |
| `fixtures/delivery-placeholder-exempt.md` | Uses an explicit estimate and two placeholder slots so its Delivery section is not placeholder-only (`delivery-placeholder-exempt.md:20-33`) |
| `fixtures/delivery-placeholder-violation.md` | Uses placeholders in Estimation, Rabbit holes and No-gos to trigger the Delivery advisory (`delivery-placeholder-violation.md:20-33`) |
| `fixtures/house-grammar-silent.md` | Carries a compliant payout example with a Requirements value, one punctuation exception set, Delivery placeholders and ordinary quality-check prose (`house-grammar-silent.md:1-78`) |
| `fixtures/house-grammar-violation.md` | Combines a missing divider, wrong divider, deep heading, Requirements checklist and checkbox, asterisk emphasis, repeated priority markers, extra ellipses and extra emoji (`house-grammar-violation.md:5-37`) |
| `fixtures/length-caps-silent.md` | Holds a four-sentence Problem and a noun pair joined by and, which the length-cap advice leaves silent |
| `fixtures/length-caps-violation.md` | Holds a third About paragraph, a long bullet, a two-sentence bullet, long and many-sentence paragraphs, a six-sentence Problem and a Then line joining a second outcome, each of which draws a length-cap advisory |
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
| Arguments | `validate-output-format.cjs` accepts `--write`, flags and target paths, then rejects unknown flags or `--write` with explicit targets (`validate-output-format.cjs:22-36`) |
| Source inventory | No explicit target selects the system files, the hub `SKILL.md` and `ROUTER.md`, shared cards and Markdown files found under the skill and `sk-create-figjam` references and assets (`validate-output-format.cjs:38-76, 80-81`) |
| Target type | Explicit targets must exist and be regular files before analysis begins (`validate-output-format.cjs:84-95`) |
| Artifact checks | Explicit targets receive purity, shape, Delivery, punctuation, Requirements, voice and conciseness checks, plus length-cap advice (`validate-output-format.cjs:1205-1543, 1545-1550`) |
| Writing | `--write` is allowed only without explicit targets and writes a changed formatted source file (`validate-output-format.cjs:33-36, 1564-1582`) |
| Results | Unknown flag combinations return 64, unreadable targets return 66, validation errors return 1 and a clean run prints a passed scope (`validate-output-format.cjs:27-36, 87-95, 1696-1703`) |

`validate-output-format.cjs:22-36, 53-95, 1561-1585 and 1687-1703` establish the path from argument parsing through file selection, analysis and result reporting

```text
process.argv
  -> flags and targets : validate-output-format.cjs:22-36
  -> file set          : validate-output-format.cjs:53-95
  -> per-file analysis : validate-output-format.cjs:1561-1585
  -> checks            : validate-output-format.cjs:1205-1550
  -> output            : validate-output-format.cjs:1687-1703
```

* * *

## 7. Entrypoints

| Entrypoint | Type | Purpose |
|---|---|---|
| `run_fixtures.sh` | Bash script | Changes to its own directory and defines the fixed validator and fixture paths (`run_fixtures.sh:1-27`) |
| `validate-output-format.cjs [--write] [file ...]` | Node CLI | Accepts the write flag or target files according to its usage contract (`validate-output-format.cjs:22-36`) |
| `PO_FORMAT_STATS=1` | Environment flag | Prints per-file statistics after analysis (`validate-output-format.cjs:1482-1501, 1691-1694`) |

* * *

## 8. Validation

Run the fixture harness from the repository root:

```bash
bash benchmark/format/run_fixtures.sh
```

The harness prints `PASSED all format-validator fixtures` and returns exit 0 when no case increments `failures`. A mismatch prints the failed case and returns exit 1 (`run_fixtures.sh:34-69, 241-245`)

For a direct file check, use the validator form declared in its usage line:

```bash
node benchmark/format/validate-output-format.cjs path/to/file.md
```

The direct form accepts one or more target paths, and `--write` is reserved for source mode (`validate-output-format.cjs:27-36, 53-81`)

* * *

## 9. Related

*   [`../router/README.md`](../router/README.md) documents the sibling executable route contract and its fixture runner (`../router/README.md:1-24`)
*   [`../parity/README.md`](../parity/README.md) documents sibling wrappers that pass system data into the shared parity gate (`../parity/README.md:13-34`)

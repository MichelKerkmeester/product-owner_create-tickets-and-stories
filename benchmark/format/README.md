---
title: "Format: output validator and fixture runner"
description: "Runs fixed Markdown cases through the Product Owner output format validator"
trigger_phrases:
  - "output format validator"
  - "format fixtures"
  - "Product Owner format benchmark"
---

# Format: output validator and fixture runner

---

## 1. OVERVIEW

`benchmark/format/` contains a Bash fixture runner, a Node validator and a Markdown fixture corpus. The runner fixes the validator and fixture directory in variables, while the validator parses flags and target paths (`run_fixtures.sh:1-30`, `validate-output-format.cjs:1-25`)

Current state:

*   `run_fixtures.sh` compares expected exit status, required output and forbidden output for each case, records mismatches and prints a pass line for cases that clear all checks (`run_fixtures.sh:38-73`)
*   `validate-output-format.cjs` walks source directories recursively, skips symlinks and selects Markdown files for its source inventory (`validate-output-format.cjs:38-45`)
*   Explicit validator targets use artifact checks, while no target uses the validator's source inventory (`validate-output-format.cjs:53-81`)
*   Missing or non-regular targets return exit 66 before file analysis (`validate-output-format.cjs:84-95`)

---

## 2. ARCHITECTURE

```text
+------------------------------+
| run_fixtures.sh              |
| run_fixtures.sh:29-73        |
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
| :1261-1640                   |
+----------+-------------------+
           v
+------------------------------+
| reports and exit status       |
| validate-output-format.cjs   |
| :1766-1782                   |
+------------------------------+

No target paths:
validate-output-format.cjs:53-81
source inventory -> per-file analysis -> reports
```

`run_fixtures.sh` passes fixed fixture paths to the validator. A call without target paths uses the source inventory instead, and both paths reach the same per-file analysis and final reporting (`run_fixtures.sh:29-42, 79-307`, `validate-output-format.cjs:53-95, 1759-1775, 1777-1893`)

Dependency direction:

```text
run_fixtures.sh -> validate-output-format.cjs
run_fixtures.sh -> fixtures/*.md
validate-output-format.cjs -> explicit target files
validate-output-format.cjs -> source inventory when no targets are supplied
```

The runner supplies fixture paths as command-line arguments to the validator, and the validator selects either those targets or its source inventory (`run_fixtures.sh:29-42, 79-307`, `validate-output-format.cjs:53-81`)

---

## 3. PACKAGE TOPOLOGY

```text
benchmark/format/
+-- README.md
+-- run_fixtures.sh
+-- validate-output-format.cjs
`-- fixtures/
    +-- catalog-entry-no-index.md
    +-- catalog-entry-silent.md
    +-- catalog-entry-violation.md
    +-- checkbox-form-silent.md
    +-- checkbox-form-violation.md
    +-- conciseness-silent.md
    +-- conciseness-violation.md
    +-- delivery-placeholder-exempt.md
    +-- delivery-placeholder-violation.md
    +-- design-copy-silent.md
    +-- design-copy-violation.md
    +-- house-grammar-silent.md
    +-- house-grammar-violation.md
    +-- length-caps-silent.md
    +-- length-caps-violation.md
    +-- markasdone-delivery-silent.md
    +-- markasdone-divider-silent.md
    +-- markasdone-divider-violation.md
    +-- mask-paths-exempt.md
    +-- mask-paths-violation.md
    +-- requirements-checklist-scope-violation.md
    +-- requirements-layout-silent.md
    +-- requirements-layout-violation.md
    +-- requirements-narration-exempt.md
    +-- requirements-narration-violation.md
    +-- sanctioned-definition-nested.md
    +-- sanctioned-shapes.md
    +-- title-shape-exempt.md
    +-- title-shape-silent.md
    `-- title-shape-violation.md
```

The runner owns case selection and result comparison. The validator owns file selection, per-file checks and final status, while the fixture files supply the Markdown inputs (`run_fixtures.sh:38-73, 79-307`, `validate-output-format.cjs:80-95, 1759-1775, 1886-1893`)

Allowed dependency direction:

```text
run_fixtures.sh -> validate-output-format.cjs -> selected files
run_fixtures.sh -> fixtures/*.md as validator arguments
```

---

## 4. DIRECTORY TREE

```text
benchmark/format/
+-- README.md
+-- run_fixtures.sh
+-- validate-output-format.cjs
`-- fixtures/
    +-- catalog-entry-no-index.md
    +-- catalog-entry-silent.md
    +-- catalog-entry-violation.md
    +-- checkbox-form-silent.md
    +-- checkbox-form-violation.md
    +-- conciseness-silent.md
    +-- conciseness-violation.md
    +-- delivery-placeholder-exempt.md
    +-- delivery-placeholder-violation.md
    +-- design-copy-silent.md
    +-- design-copy-violation.md
    +-- house-grammar-silent.md
    +-- house-grammar-violation.md
    +-- length-caps-silent.md
    +-- length-caps-violation.md
    +-- markasdone-delivery-silent.md
    +-- markasdone-divider-silent.md
    +-- markasdone-divider-violation.md
    +-- mask-paths-exempt.md
    +-- mask-paths-violation.md
    +-- requirements-checklist-scope-violation.md
    +-- requirements-layout-silent.md
    +-- requirements-layout-violation.md
    +-- requirements-narration-exempt.md
    +-- requirements-narration-violation.md
    +-- sanctioned-definition-nested.md
    +-- sanctioned-shapes.md
    +-- title-shape-exempt.md
    +-- title-shape-silent.md
    `-- title-shape-violation.md
```

`run_fixtures.sh:79-307` names every fixture path used by the runner. The fixture responsibilities are listed below with the lines that define each input

---

## 5. KEY FILES

| File | Responsibility |
|---|---|
| `run_fixtures.sh` | Sets the validator and fixture paths, runs fixed cases and reports aggregate failure or success (`run_fixtures.sh:29-73, 345-349`) |
| `validate-output-format.cjs` | Parses flags and targets, selects source or artifact mode, analyzes each file and reports the result (`validate-output-format.cjs:22-36, 53-95, 1759-1775, 1777-1893`) |
| `fixtures/catalog-entry-silent.md` | Carries a Catalog with its Index heading, two entry headings and two entry links, each with one dash between the stable ID and the entry name, so the narrow Catalog grant clears the gate (`catalog-entry-silent.md:1-31`) |
| `fixtures/catalog-entry-violation.md` | Keeps the Index heading and puts the same dash on a title, a heading with no stable ID, prose, a second dash, an H2 and a link with trailing text, each of which still blocks (`catalog-entry-violation.md:1-27`) |
| `fixtures/catalog-entry-no-index.md` | Carries the entry heading and link shapes with no Index heading, so the grant earns nothing outside a Catalog (`catalog-entry-no-index.md:1-11`) |
| `fixtures/checkbox-form-silent.md` | Writes every checkbox in the house `- []` form, so the checkbox rule stays silent on it |
| `fixtures/checkbox-form-violation.md` | Writes one requirement checkbox and one Mark as done checkbox in the spaced `- [ ]` form, so both fire and an old-form checkbox with a divider below it still trips the divider check |
| `fixtures/conciseness-silent.md` | Holds near-miss cases for exact token binding, export read-back, one hedge, quoted vocabulary and fallback intake (`conciseness-silent.md:1-27`) |
| `fixtures/conciseness-violation.md` | Holds opener, heading echo, hedge stack and terminal recap cases (`conciseness-violation.md:1-22`) |
| `fixtures/delivery-placeholder-exempt.md` | Uses an explicit estimate and two placeholder slots so its Delivery section is not placeholder-only (`delivery-placeholder-exempt.md:20-33`) |
| `fixtures/delivery-placeholder-violation.md` | Uses placeholders in Estimation, Rabbit holes and No-gos to trigger the Delivery advisory (`delivery-placeholder-violation.md:20-33`) |
| `fixtures/design-copy-silent.md` | Quotes eleven distinct UI strings in Requirements and Acceptance criteria, repeats some, and holds values, tokens, identifiers, one-word labels, a title-case name, Solution copy and a fenced block, none of which count, so the design-copy advice stays silent (`design-copy-silent.md:1-58`) |
| `fixtures/design-copy-violation.md` | Quotes twelve distinct UI strings across Requirements and Acceptance criteria, the threshold, so the design-copy advice fires once on the Requirements heading (`design-copy-violation.md:1-54`) |
| `fixtures/house-grammar-silent.md` | Carries a compliant payout example with a Requirements value, one punctuation exception set, Delivery placeholders and ordinary quality-check prose (`house-grammar-silent.md:1-78`) |
| `fixtures/house-grammar-violation.md` | Combines a missing divider, wrong divider, deep heading, Requirements Checklist label and plain bullet, asterisk emphasis, repeated priority markers, extra ellipses and extra emoji (`house-grammar-violation.md:5-36`) |
| `fixtures/length-caps-silent.md` | Holds a four-sentence Problem and a noun pair joined by and, which the length-cap advice leaves silent |
| `fixtures/length-caps-violation.md` | Holds a third About paragraph, a long bullet, a two-sentence bullet, long and many-sentence paragraphs, a six-sentence Problem and a Then line joining a second outcome, each of which draws a length-cap advisory |
| `fixtures/markasdone-delivery-silent.md` | Ends the last criterion on its Mark as done line, then an empty line and a spacer before `## Delivery`, so the divider rule stays silent when Delivery follows (`markasdone-delivery-silent.md:1-33`) |
| `fixtures/markasdone-divider-silent.md` | Sets every Mark as done checkbox directly under a divider with one empty line after it, across a group heading, and ends on the last one, so the divider rule stays silent on the correct shape (`markasdone-divider-silent.md:1-37`) |
| `fixtures/markasdone-divider-violation.md` | Puts a divider under the first Mark as done checkbox, leaves the second with none above it, starts a criterion directly under the third and ends on a spacer after the fourth, one finding each (`markasdone-divider-violation.md:9-40`) |
| `fixtures/mask-paths-exempt.md` | Holds two path examples whose structural punctuation should stay exempt (`mask-paths-exempt.md:3-9`) |
| `fixtures/mask-paths-violation.md` | Holds three prose dash examples that the path mask must leave visible (`mask-paths-violation.md:3-10`) |
| `fixtures/requirements-layout-silent.md` | Carries two bold Part headings, User flow labels with one bullet per step, one with an empty line under its label, Checklist labels with a divider under them and a columns block, so the Requirements layout rules stay silent (`requirements-layout-silent.md:1-70`) |
| `fixtures/requirements-checklist-scope-violation.md` | Sets a Checklist label in Requirements with no numbered section above it, the one finding (`requirements-checklist-scope-violation.md:5-13`) |
| `fixtures/requirements-layout-violation.md` | Writes a User flow on one line, a Checklist label with no divider and a plain bullet outside a User flow, one finding each (`requirements-layout-violation.md:13-36`) |
| `fixtures/requirements-narration-exempt.md` | Quotes one screen string and keeps the other bullets as constraints (`requirements-narration-exempt.md:3-12`) |
| `fixtures/requirements-narration-violation.md` | Uses two bullets that report what a screen says without quoting the copy, plus one action bullet (`requirements-narration-violation.md:3-11`) |
| `fixtures/sanctioned-definition-nested.md` | Checks definition bullets at column zero and two deeper indentation levels (`sanctioned-definition-nested.md:1-8`) |
| `fixtures/sanctioned-shapes.md` | Places definition and status shapes in list, checkbox and blockquote containers, then includes a section status line (`sanctioned-shapes.md:3-21`) |
| `fixtures/title-shape-exempt.md` | Gives a Doc a sentence title that ends on a full stop, so the title advice stays silent on a document that is not a backlog artifact (`title-shape-exempt.md:1-9`) |
| `fixtures/title-shape-silent.md` | Carries a Task, a Story, an Epic and two near misses, one with a date inside its title and one with the word Bug inside it, so no title draws advice (`title-shape-silent.md:1-29`) |
| `fixtures/title-shape-violation.md` | Holds six Task titles, one with no separator, one with a full stop, two with a date lead, one with a BUG lead and one that fits two shapes and reports the first, each of which draws one title advisory (`title-shape-violation.md:1-35`) |

---

## 6. BOUNDARIES AND FLOW

| Boundary | Rule |
|---|---|
| Arguments | `validate-output-format.cjs` accepts `--write`, flags and target paths, then rejects unknown flags or `--write` with explicit targets (`validate-output-format.cjs:22-36`) |
| Source inventory | No explicit target selects the system files, the hub `SKILL.md` and `ROUTER.md`, shared cards and Markdown files found under the skill and `sk-create-figjam` references and assets (`validate-output-format.cjs:38-76, 80-81`) |
| Target type | Explicit targets must exist and be regular files before analysis begins (`validate-output-format.cjs:84-95`) |
| Artifact checks | Explicit targets receive purity, shape, Delivery, punctuation, Requirements, voice and conciseness checks, plus title-shape, design-copy and length-cap advice (`validate-output-format.cjs:1360-1741, 1743-1748`) |
| Title shape | A backlog artifact, one that opens on About or Problem, draws one advisory per H1 that holds no `" - "` separator, ends on a full stop or opens on a date or a BUG lead, and the check never blocks and never reads a Doc. The shared Sync Loop validator repeats it for `product-owner` alone (`validate-output-format.cjs:1230-1266, 1372-1378`) |
| Design copy | A Story or Epic whose Requirements and Acceptance criteria quote twelve or more distinct copy-like strings in backticks draws one advisory on the first of those headings. Values, tokens, identifiers, paths, placeholders, commands, one-word labels and fenced blocks never count. The check never blocks, because copy the requester typed is kept verbatim and the gate cannot tell it from copy read off a design. The shared Sync Loop validator repeats it for `product-owner` alone (`validate-output-format.cjs:1268-1331, 1509-1514`) |
| Writing | `--write` is allowed only without explicit targets and writes a changed formatted source file (`validate-output-format.cjs:33-36, 1762-1772`) |
| Results | Unknown flag combinations return 64, unreadable targets return 66, validation errors return 1 and a clean run prints a passed scope (`validate-output-format.cjs:27-36, 87-95, 1886-1893`) |

`validate-output-format.cjs:22-36, 53-95, 1759-1775 and 1804-1820` establish the path from argument parsing through file selection, analysis and result reporting

```text
process.argv
  -> flags and targets : validate-output-format.cjs:22-36
  -> file set          : validate-output-format.cjs:53-95
  -> per-file analysis : validate-output-format.cjs:1759-1775
  -> checks            : validate-output-format.cjs:1360-1748
  -> output            : validate-output-format.cjs:1877-1893
```

---

## 7. ENTRYPOINTS

| Entrypoint | Type | Purpose |
|---|---|---|
| `run_fixtures.sh` | Bash script | Changes to its own directory and defines the fixed validator and fixture paths (`run_fixtures.sh:1-30`) |
| `validate-output-format.cjs [--write] [file ...]` | Node CLI | Accepts the write flag or target files according to its usage contract (`validate-output-format.cjs:22-36`) |
| `PO_FORMAT_STATS=1` | Environment flag | Prints per-file statistics after analysis (`validate-output-format.cjs:1680-1699, 1881-1884`) |

---

## 8. VALIDATION

Run the fixture harness from the repository root:

```bash
bash benchmark/format/run_fixtures.sh
```

The harness prints `PASSED all format-validator fixtures` and returns exit 0 when no case increments `failures`. A mismatch prints the failed case and returns exit 1 (`run_fixtures.sh:38-73, 345-349`)

The harness also ends with one more assertion, the shared Sync Loop's reference parity check that holds its validator to this one. It passes only when that check reports a byte-identical comparison, and it prints a skipped line when that folder is not beside this repository

For a direct file check, use the validator form declared in its usage line:

```bash
node benchmark/format/validate-output-format.cjs path/to/file.md
```

The direct form accepts one or more target paths, and `--write` is reserved for source mode (`validate-output-format.cjs:27-36, 53-81`)

---

## 9. RELATED

*   [`../router/README.md`](../router/README.md) documents the sibling executable route contract and its fixture runner (`../router/README.md:1-28`)
*   [`../parity/README.md`](../parity/README.md) documents sibling wrappers that pass system data into the shared parity gate (`../parity/README.md:13-34`)

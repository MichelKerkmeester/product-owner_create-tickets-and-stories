# Review Iteration 005

## Dimension

**traceability** — Claude Project mirror and release traceability: the `claude project/` package (kernel `Custom Instructions.md`, `knowledge/`, `README.md`, `kernel-review.json`) against the `sk-product-owner` and `sk-create-figjam` skill sources, `SYNC.md`, the Sync Loop `systems.py` declarations, and version numbers across `SKILL.md`, READMEs, changelogs and the kernel H1.

Operator focus addressed in this pass: drift across the Product Owner system, alignment with the Skilled `sk-doc` package shape and README/changelog/frontmatter expectations, and the vendored-package sync question. Specifically this iteration measured whether the hand-written Project package still *describes itself accurately* (counts, versions, review records, operator steps), which is the release-traceability half of the operator's brief; the `scripts/` and vendored-sync half stays with the earlier iterations that already filed findings against it.

Budget profile: `verify` (11 calls used, under the 12 soft cap).

## Files Reviewed

- `AI Systems/Product Owner/claude project/Custom Instructions.md:1`, `:139`, `:192`, `:465`
- `AI Systems/Product Owner/claude project/README.md:11`, `:14-16`, `:54-58`, `:63`, `:97-102`, `:111-114`, `:121`, `:125`, `:139`, `:146`, `:204`, `:213`
- `AI Systems/Product Owner/claude project/kernel-review.json:1-13`
- `AI Systems/Product Owner/claude project/local/Product Owner - Local - Push Targets.md:11-33`
- `AI Systems/Product Owner/claude project/templates/Product Owner - Local - Push Targets.md:11-21`
- `AI Systems/Product Owner/SYNC.md:1-...` (parity method, the two version bullets, all dated review notes through 2026-09-18)
- `AI Systems/Product Owner/SKILL.md:5`, `:14`
- `AI Systems/Product Owner/description.json:4`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:2`, `:5`
- `AI Systems/Product Owner/sk-product-owner/changelog/` (v1.2.13.0 … v1.2.16.0)
- `AI Systems/Product Owner/changelog/` (v1.0.24.0 … v1.0.28.0)
- `AI Systems/Product Owner/.gitignore:13-16`
- `AI Systems/Product Owner/manual-testing-playbook/` (directory listing + full-text scan)
- `AI Systems/Product Owner/USER-GUIDE.md:1-25`
- `AI Systems/z — Claude Project Sync Loop/systems.py:1-60`, Product Owner block `:148`, `:185`, `:199`, `:2539`, FigJam rows `:1831-1841`

## Findings - New

### P0 Findings

None.

### P1 Findings

None new. Two P1 findings from iterations 1-2 remain active and are not re-reported here: the hub `NEVER` rule versus the packet-local `ROUTER.md` contradiction, and the Product Owner release gate running a diverged fork of the output-format validator. Neither was touched by this iteration's focus, so neither is extended, refuted or re-scoped.

### P2 Findings

1. **Kernel's retrieval table undercounts the example documents the package ships** -- `AI Systems/Product Owner/claude project/Custom Instructions.md:192` -- The kernel is the routing authority inside a Claude Project and its knowledge table tells the reader there are twenty-eight example documents; the package it ships in carries thirty files whose name begins `Product Owner - Examples -`. The same package's own `README.md:146` states "37 core files plus the 30 Examples mirrors", and `README.md:54-58` itemises that 30 as Task 6, Bug 4, Doc 7, Story 5, Flow 8. A reader who trusts the kernel's number under-consults by two examples, and a reader who trusts the README meets a kernel number that disagrees with it. The kernel count is the stale side of the pair and there is no gate that compares a numeric claim inside the kernel against the directory it describes.
   Finding class: content
   Scope proof: claim and both counters read directly at `claude project/Custom Instructions.md:192`, `claude project/README.md:146`, `claude project/README.md:54-58`; directory population measured with `ls claude project/knowledge | grep -c Examples` = 30.
   Affected surface hints: kernel text only; the knowledge files themselves and the skill-side `assets/examples/**` sources are correct and untouched. Fix belongs in `Custom Instructions.md:192` with a kernel patch bump in the H1, per `SYNC.md:...` ("Bump the version in the `Custom Instructions.md` H1 in the same change that edits it").
   Case: an operator asks the Project for a Story example, the kernel says only twenty-eight exist and makes a group row the canonical pointer, and the two examples past that count are never named or counted; separately, an operator reconciling an upload against the README's 30 finds a kernel claiming 28 and cannot tell which side is wrong.
   Evidence: `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:192]` "The twenty-eight example documents are titled `Product Owner - Examples - {Kind} - {Descriptor}`" against `[SOURCE: AI Systems/Product Owner/claude project/README.md:146]` "Upload all 67 files in `knowledge/` with filenames unchanged (37 core files plus the 30 Examples mirrors)".
   caveat: if `Product Owner - Examples - Doc - README.md` is counted by the kernel as a group README rather than an example document, the true number is 29 rather than 30 — still not twenty-eight, so the finding stands either way, with the exact replacement number to be settled when it is fixed.

2. **The upload guide's final step names a "smoke matrix" that no playbook document carries** -- `AI Systems/Product Owner/claude project/README.md:213` -- The last instruction in the Project upload procedure reads "Re-upload changed files to the live Project and run the smoke matrix." The manual-testing-playbook folder holds one document, `manual-testing-playbook.md`, plus a `hub-routing/` fixture folder, and a full-text scan of that folder for `smoke`/`Smoke` returns no hit. A step phrased as the operator's closing verification therefore resolves to nothing the repository owns, and an operator cannot distinguish "I ran the wrong thing" from "the step is stale". This is the `playbook_capability` overlay: the guide asserts a playbook capability the playbook does not expose under that name.
   Finding class: content
   Scope proof: the sentence read at `claude project/README.md:213`; the target folder enumerated (`ls manual-testing-playbook/` → `hub-routing/`, `manual-testing-playbook.md`) and scanned with `grep -rln "smoke matrix\|Smoke" manual-testing-playbook/ claude project/README.md`, whose only hit is the README itself.
   Affected surface hints: `claude project/README.md` prose, and whichever of `manual-testing-playbook/manual-testing-playbook.md` or the benchmark fixture runners is the intended target — the fix is either a named path in the README or a section heading in the playbook, not a new harness.
   Case: an operator edits one kernel paragraph, follows the guide to the end, and is told to run a smoke matrix with no path, no command and no document to run; they either skip the step or improvise one, and the guide records neither outcome.
   Evidence: `[SOURCE: AI Systems/Product Owner/claude project/README.md:213]` "Re-upload changed files to the live Project and run the smoke matrix." with no resolvable target under `[SOURCE: AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md]`.

## Traceability Checks

| Protocol | Check | Result |
| --- | --- | --- |
| core `spec_code` | Skill source ↔ Project mirror pairing is declared, not derived. `systems.py` declares Product Owner pairs from `skill_dir` `sk-product-owner` plus `extra_skill_dirs: ('sk-create-figjam',)`, with `vendored_shared_copies`, `unmirrored_sources` and `adapted_pairs` as the recorded exception surfaces (`systems.py:148`, `:185`, `:199`). The FigJam rows are declared relative to `skill_dir` as `../sk-create-figjam/assets/templates/<type>.md` (`systems.py:1831-1841`) and match the README's public mirror table one for one, six types to six rows (`claude project/README.md:97-102`). | PASS |
| core `checklist_evidence` | Upload counts and their arithmetic. `README.md:16` "upload all 67 files" and `README.md:146` "all 67 files … (37 core files plus the 30 Examples mirrors)" agree with the directory: 67 files under `claude project/knowledge/`, 30 of them `Examples -`, therefore 37 core. The per-group breakdown at `README.md:54-58` (Task 6, Bug 4, Doc 7, Story 5, Flow 8 = 30) and `:111-114` reconcile. | PASS (the kernel's own count is finding 1 above; the README and the directory agree with each other) |
| overlay `skill_agent` | Version triangle. Kernel H1 `v1.2.18` (`Custom Instructions.md:1`), the SYNC bullet "currently v1.2.18" and `README.md:11`/`:63` all agree. Skill `1.2.16.0` (`sk-product-owner/SKILL.md:5`), newest `sk-product-owner/changelog/v1.2.16.0.md`, the SYNC bullet "currently 1.2.16.0" and `README.md:63` "aligned to **Product Owner Skill v1.2.16.0**" all agree. Hub `1.0.28.0` (`SKILL.md:5`, `description.json:4`) matches newest `changelog/v1.0.28.0.md`, already ruled out at iteration 1. Three independent schemes, each internally consistent, and the SYNC bullet states why a skill number below a kernel number is not drift. | PASS |
| overlay `agent_cross_runtime` | The tracked Project package versus the local-only surfaces. `.gitignore:13-16` ignores `claude project/local/` and `click-up-links.md` and says why; `git ls-files` returns only `claude project/templates/Product Owner - Local - Push Targets.md`, and `git check-ignore -v` confirms the filled copy is ignored (`.gitignore:15`). The tracked file is the blank scaffold (`List name: list link`, `Doc name: doc link`); the filled copy carries real workspace list and doc URLs and is correctly untracked. `README.md:14-15` and `:139` describe exactly this split. | PASS |
| overlay `feature_catalog_code` | This system ships no feature catalog of its own; the fleet catalog under `z — Claude Project Sync Loop/feature-catalog/` documents the parity gate rather than Product Owner source. | notApplicable to code under review (no catalog to reconcile) |
| overlay `playbook_capability` | The playbook exists (`manual-testing-playbook/manual-testing-playbook.md` plus `manual-testing-playbook/hub-routing/`) but does not carry the capability the upload guide names. | FAIL → finding 2 above |

### Review-record traceability

`claude project/kernel-review.json` records `kernelVersion: 0.8.0` / `alignedSkillVersion: 0.8.0` dated `2026-08-13` against a live kernel H1 of `v1.2.18`. Its own `note` states it is a dated record of one review and not a claim about the live kernel, which the repository supports: no live tooling references the literal filename `kernel-review.json` — the only references are `SYNC.md` prose and archived `feature-catalog/` and `episodes/` documents under `z — Claude Project Sync Loop/`. This matches the fleet-wide annotation repair recorded at `z — Claude Project Sync Loop/episodes/hand-run/000-packet-record/research/iteration-9.md:56`. Consistent, not a finding. `SYNC.md`'s own rule is what to hold it to: a review is recorded as a dated sentence after the named human confirms it, and the live review trail is the `## Review notes` list, whose newest entry is 2026-09-18 at kernel v0.13.3 / Skill v0.9.2 — older than the live v1.2.18 / 1.2.16.0, so the version bumps after that entry carry no dated review sentence. That is a discipline observation rather than a defect this pass can charge: `SYNC.md` records reviews, it does not claim every bump has one.

## Edge Cases

- **Iteration numbering under parallel fan-out.** The dispatched iteration is 5; the state log holds 2 iteration records (iterations 1-2). Iterations 3-9 are dispatched concurrently against the same packet, so the JSONL-derived value cannot yet reach 5. The dispatch instruction binds this worker to its own iteration number for finding ids and artifact filenames, and that has been followed; the mismatch is recorded here rather than resolved by renumbering, because renumbering would collide with the parallel lineages.
- **A dated note that looks like live drift.** The 2026-09-17 SYNC entry says "the Project upload guide now counts thirty-eight files" while the README now says 67 and the directory holds 67. Adjudicated as a historical record, not drift: `SYNC.md` itself established at its 2026-09-18 entry that a dated log entry records what was true when written, and the same entry records that a repoint tool was corrected for rewriting those entries. The live claim and the row above it agree.
- **Two files with one document title.** `Product Owner - Local - Push Targets.md` exists in both `claude project/local/` (1916 bytes, filled, real workspace URLs) and `claude project/templates/` (1131 bytes, blank scaffold). Not a duplicate-upload or drift defect: `README.md:14` declares `templates/` as the blank file each user fills and `README.md:15` declares `local/` as the gitignored home of the filled copy, and the diff between them is exactly placeholder-to-value. Recorded because the identical title makes the pair easy to mistake for drift on a later pass.
- **Count ambiguity inside finding 1.** The 30-file `Examples -` count includes `Product Owner - Examples - Doc - README.md`, which the kernel may treat as a group README rather than an example document. The finding is filed with that caveat rather than asserting a replacement number.

## Integration Evidence

- `AI Systems/z — Claude Project Sync Loop/systems.py` — the parity gate's declaration surface; read for the Product Owner `skill_dir`, `extra_skill_dirs`, `vendored_shared_copies`, `unmirrored_sources` and `adapted_pairs` members and for the FigJam pair rows at `:1831-1841`. Its module docstring records why pairs are declared rather than derived (basename collisions `industry.md`, `product.md`, `service.md`), which is the contract that makes an undeclared unpaired source a finding.
- `AI Systems/Product Owner/.gitignore` — the authority for which Project surfaces are tracked; read because the upload guide makes a tracked/untracked claim at `README.md:14-15` and `:139`.
- `AI Systems/z — Claude Project Sync Loop/episodes/hand-run/000-packet-record/research/iteration-9.md:56` — prior fleet measurement of the `kernel-review.json` annotation, used as counterevidence rather than as a source of a finding.

## Confirmed-Clean Surfaces

- `claude project/README.md` structure block, upload count and per-group arithmetic: 67 = 37 + 30, and 30 = 6 + 4 + 7 + 5 + 8.
- The kernel/skill/hub version triangle, including the three-scheme explanation in `SYNC.md`.
- The tracked/untracked split for the push-targets scaffold and its filled copy.
- `README.md:97-102` FigJam mirror table against `systems.py:1831-1841`.
- `USER-GUIDE.md:1-25` — the two habits it leads with ("asks before it guesses", "writes nothing to ClickUp or Figma until you say yes") match the kernel's conflict rule and the ClickUp approval gate; the three-row runtime table matches the kernel's advisory-only scope line.

## Ruled Out

- **Kernel / skill / hub version drift.** All three schemes internally consistent and cross-cited; see the `skill_agent` row.
- **Stale `kernel-review.json` as a live claim.** Declared a dated record in its own text and corroborated by its `note`; no live tooling reads the filename.
- **`claude project/local/` as a private-data leak into the tracked package.** Ignored at `.gitignore:15`, filled copy untracked, only the blank `templates/` copy tracked.
- **Knowledge-count drift in the Project README.** 67 claimed, 67 present.
- **Duplicate `Local - Push Targets` title as package drift.** Two declared surfaces with different purposes, one ignored by Git.
- **FigJam mirror table drift between the README and `systems.py`.** Six rows to six declared pairs.
- **`feature_catalog_code` gap.** No catalog exists for this system to drift from; the fleet catalog covers the gate, not this source.
- **The "38 files" SYNC note as live drift.** A dated historical entry, adjudicated in Edge Cases.

## Next Focus

- **Dimension:** maintainability.
- **Focus area:** the Product Owner skill sources' own packaging against Skilled `sk-doc` expectations — `sk-product-owner/SKILL.md` frontmatter and section shape, the `sk-product-owner/README.md` claim surface, the `changelog/` entry format and version discipline, and the `manual-testing-playbook/` document against the playbook mode's required sections. Include `sk-create-figjam` on the same axes.
- **Reason:** `traceability` has now covered the Project package, the version triangle and the declaration surface. The two findings this pass raised are both *content accuracy* defects in hand-written prose, which is the maintainability dimension's subject: what keeps a hand-authored mirror honest when no compiler regenerates it.
- **Rotation status:** `traceability` records its first completed pass; `correctness` holds one completed pass and `security` remains queued. `maintainability` becomes active.
- **Blocked/productive carry-forward:** productive — finding 2 needs one read of `manual-testing-playbook.md`'s own section list to decide whether the fix is a README pointer or a playbook section. Finding 1 needs the kernel's example-count sentence settled against the Doc README's role.
- **Required evidence:** `sk-product-owner/SKILL.md` section skeleton and frontmatter fields against the `sk-doc` skill-authoring contract; `sk-product-owner/README.md` claims against the files it names; the newest two `changelog/` entries against the hub's changelog format rule; `manual-testing-playbook/manual-testing-playbook.md` section list.
- **Recovery note:** not applicable; this iteration ran clean within budget.

Review verdict: CONDITIONAL

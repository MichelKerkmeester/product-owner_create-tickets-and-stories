---
title: "Implementation Summary"
description: "Fixes the confirmed findings of a ten-iteration review of the whole Product Owner system, keeps browser captures out of the repository and makes syncing the vendored packets one command."
trigger_phrases:
  - "system review and vendor sync implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/030-system-review-and-vendor-sync"
    last_updated_at: "2026-11-10T23:30:00Z"
    last_updated_by: "claude-fable-5-2"
    recent_action: "Fixed the confirmed review findings, released hub 1.0.29.0 and kernel v1.2.19, added sync, status --local and diff to vendor-sync.py"
    next_safe_action: "Paste kernel v1.2.19 into the Claude Project"
    blockers: []
    key_files:
      - "scripts/vendor-sync.py"
      - "benchmark/gates/run_gates.sh"
      - "claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "77e809ab-7e4a-4669-a9c5-ee0fa5f7617b"
      parent_session_id: null
    completion_pct: 100
    open_questions:
      - "Should the always-loaded files go on a token diet?"
      - "Should SYNC.md get an index or a split?"
      - "Should an upstream-ahead vendored entry keep failing the release gate?"
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.4 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 1 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 030-system-review-and-vendor-sync |
| **Completed** | 2026-11-10 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The review filed 25 findings. Seventeen are fixed, three needed no change and five stay open with a recorded reason.

### Browser captures

A HAR file, a cookie dump or a screenshot of a signed-in page can hold live session cookies and bearer tokens. The two browser packets had no rule for them and their recipes wrote into the open folder. Upstream, `mcp-chrome-devtools` v1.0.24.0 gained ALWAYS rule 7 and `mcp-aside-devtools` v1.1.10.0 rewrote ALWAYS rule 6. Their recipes, catalog leaves, playbook scenarios and example scripts now write under the temp folder, and the cookie recipes print names and domains only. Here, `.gitignore` ignores the capture file names and folders the old recipes wrote, at any depth, plus the Python caches.

### Vendor sync

`scripts/vendor-sync.py` gained three commands. `sync` pulls every entry that is behind upstream, leaves the rest alone, lists the upstream commit subjects and prints the rebuild commands when a dependency file changed. `status --local` checks each local copy against the hashes in `vendor.json` and reads no upstream, so it works in a clone. `diff` prints what differs from upstream and writes nothing. `status` and `sync` end with one line naming the entries out of step. The override root must hold `.skilled`. `sync` refuses a never-pulled entry whose folder already holds other files, which only an explicit `pull` vendors over. `scripts/README.md` carries the day-to-day recipe, the reason for each `mcp-code-mode` exclusion and why the Skilled overlay engine does not fit this layout.

### Gates

`run_gates.sh` names each gate's script outright. In a clone the vendor sync gate now runs `status --local` and says so on its line, where it used to skip. `run_fixtures.sh` ends with the Sync Loop's reference parity check when that folder is present, so an edit to this validator can no longer drift from the shared core unseen. The step passes only when the check reports a byte-identical comparison. The link gate derives its skip set from `vendor.json`.

### Hub and kernel

The hub ALWAYS rule states that each packet owns a `ROUTER.md`, which the hub gate requires and the old NEVER rule forbade. The hub names `chrome_devtools_live` as the one Chrome manual this repository registers. The vendored-packet rule covers every packet `vendor.json` lists. `scripts` joined `repoPaths`. Kernel v1.2.19 counts thirty example documents and carries the feedback ticket export path, which closes the gap packet 028 recorded.

### Mark-as-done

`mcp-click-up` v1.2.21.0 grays every Mark-as-done line in the page writer, whatever follows the words.

### Finding outcomes

| Finding | Outcome |
|---------|---------|
| F01, F05, F06, F07, F21 | Fixed in hub `SKILL.md`, `ROUTER.md` and `mode-registry.json` |
| F02 | Fixed as downgraded: the format harness runs reference parity |
| F03, F11 | Fixed upstream and pulled, with ignore patterns here |
| F04 | Fixed: the hub names its own manual and the upstream docs read per config |
| F09, F14 | Fixed in `run_gates.sh` and `.gitignore` |
| F12, F19, F20, F23 | Fixed in `vendor-sync.py` and `scripts/README.md` |
| F15, F16 | Fixed in the kernel and the Project README |
| F08 | By design. Parity and residency refuse an uncommitted declaration and run after a commit |
| F13 | Refuted. Skill changelog folders are the current placement |
| F17 | Declined. The script exports nothing and its output is pinned by fixtures |
| F10 | Not changed. The vendored docs float the same versions, so a pin belongs upstream |
| F18 | Not changed. Three wrappers state the reason. The other two are byte-identical across seven systems, so the fix is a fleet change |
| F22, F25 | Owner decisions, listed as open questions in `spec.md` |
| F24 | Not changed. `kernel-review.json` is read by nothing and all seven systems carry one, so a delete is a fleet decision |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| Skilled `mcp-chrome-devtools/`, `mcp-aside-devtools/`, `mcp-click-up/`, hub files and changelogs | Modify and Create | Capture rules, Mark-as-done match, hub 1.9.13.0 and 1.9.14.0, in three commits |
| `mcp-chrome-devtools/`, `mcp-aside-devtools/`, `mcp-click-up/`, `mcp-code-mode/`, `vendor.json` | Modify | Vendor pulls |
| `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py`, `scripts/README.md`, `scripts/tests/README.md` | Modify | Three commands, 14 new tests, the recipe |
| `scripts/vendored/code-mode/README.md` | Modify | Node floor follows the server manifest |
| `benchmark/gates/run_gates.sh`, `check_markdown_links.py`, `benchmark/format/run_fixtures.sh` and both READMEs | Modify | Gate wiring, reference parity, current line citations |
| `.gitignore` | Modify | Capture files and Python caches |
| `SKILL.md`, `ROUTER.md`, `mode-registry.json` | Modify | Hub rules match the gate |
| `claude project/Custom Instructions.md`, `claude project/README.md` | Modify | Kernel v1.2.19 |
| Sync Loop `systems.py` | Modify | Two residency rows follow the new kernel sentences |
| Hub version files, `changelog/v1.0.29.0.md`, `README.md`, `SYNC.md` | Modify and Create | Release 1.0.29.0 |
| `specs/system/028-*`, `specs/system/029-*` | Modify | Limitations that this packet closed |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The review ran ten iterations on DeepSeek, seven of them as parallel lanes. Five agents then fixed separate file sets at once: the kernel, the hub docs, the upstream browser packets, the gates and the vendor script. The upstream change was committed in Skilled and pulled with the new `sync` command. A second reader then rechecked every finding against the tree. It found six capture and cookie recipes the upstream change had missed, ignore patterns that matched only at the repository root, a `sync` that would overwrite files in a never-pulled entry's folder, a stale Node floor and a parity pass that trusted exit 0 alone. All were fixed, and one full gate run closed the work.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Keep `vendor-sync.py`, do not adopt the overlay engine | The engine hard-codes one `.skilled` tree and one pin, has no include list and no push back. A staged repin on a two-packet scratch tree was refused with 809 lines |
| Fix the capture rules upstream | The vendored copies are byte copies, so a local rule would be lost on the next pull |
| A clone runs the local vendor check, with a note on its line | A skip proved nothing, and an unmarked pass would read as the full upstream comparison |
| Leave the two shared parity wrappers alone | They are byte-identical across seven systems and six are outside this packet |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `run_gates.sh` on the live tree | exit 0, `all 15 gates pass` |
| `run_gates.sh` in a standalone clone carrying this tree | exit 0, `12 of 15 gates pass, 3 skipped`, vendor sync marked local copies only |
| Same clone with one stray line in a vendored file | exit 1, vendor sync names `mcp-figma` and the changed file |
| `test_vendor_sync.py` | 32 tests pass, 18 before. Each of 18 injected bugs turned a test red |
| `vendor-sync.py status` | exit 0, 7 of 7 entries in step |
| Format harness with a broken reference copy | exit 1, only the parity step fails |
| PO `run_fixtures.sh` | exit 0, 65 PASS |
| Copywriter, Deal Templates and Sales harnesses | exit 0, 158 PASS each |
| `validate-output-format.cjs --system product-owner` | exit 0, 74 files |
| `reference-parity.cjs` | exit 0, byte-identical |
| `validate_parity.py product-owner` in a scratch clone | PASSED 67/67 |
| `residency_check.py --all` in a scratch clone | PASSED 7 systems. `residency_report.py --write` changed nothing |
| `check_changelog_shape.py` | PASS for the hub entry and the three upstream entries |
| Independent recheck of F01 to F25 | 16 fixed findings read as gone and F03 as partial. Its leftovers were then fixed and confirmed by grep and `git check-ignore`. F10, F18 and F24 stay open, each with its reason above |
| `git ls-files -ci --exclude-standard` | 0 tracked files ignored, in this repository and under it in the outer one |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No rerun of the review.** SC-002 asks for one. A second reader rechecked each finding against the final tree instead, which is cheaper and not the same ten-iteration pass.
2. **The Project is not updated.** Kernel v1.2.19 needs pasting into the Claude Project, with the knowledge uploads earlier packets left pending.
3. **Floating versions stay.** `figma-developer-mcp@latest` and an unversioned `mcp-remote` float here and upstream.
4. **Line citations go stale by hand.** `benchmark/format/README.md` cites line ranges that no gate checks. They are current as of this packet.
5. **The shared harness trusts exit 0.** The Sync Loop's own `run_fixtures.sh` prints its parity pass line on exit 0 alone, which the check also returns for a reference declared retired. That harness is shared by four systems and sits outside this packet.
6. **Images are not ignored.** The repository tracks real screenshots, so a capture saved under another name than the recipes use still shows up as untracked.
<!-- /ANCHOR:limitations -->

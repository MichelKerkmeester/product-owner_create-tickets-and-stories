#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: GATE RUNNER
# ───────────────────────────────────────────────────────────────
# Run every gate this system owns and report all of them.
#
# The checks lived in four folders with no single entry, and a check nobody
# runs is a check that stays red unseen. This runner is the one command a
# release runs before its changelog is written.
#
# Every gate runs even after one fails, because stopping at the first would
# hide the rest, and the exit code carries the count rather than the first
# failure, so a caller cannot read one red gate as one problem.
#
# The total comes from the list rather than a literal, so adding a gate never
# leaves a summary line counting the old set.
#
# Rule parity reads the shared Sync Loop declaration one folder above this
# repository. A standalone clone has no such folder, so that one gate reports
# SKIPPED there and the summary line counts it, never as a pass.
#
# Vendor sync compares the vendored skill copy with the shared skill folder two
# levels up. A standalone clone has none, so there the gate checks each local
# copy against the hashes in vendor.json alone, and its line says so.
#
# The two skilled contract gates hold the hub at this repository root and its two
# workflow packets to the sk-create-skill validator and parent-hub checker in
# that same shared folder, so they skip in a standalone clone too.
#
# The shared parity and residency checks are not in the list. They read the
# Sync Loop declaration against git history and refuse a declaration with
# uncommitted edits, so they run from `benchmark/parity/` once a batch is
# committed.
#
# Exit Codes:
#   0 - every gate passed, or every gate that could run passed and the summary names the skip
#   2 - the system root could not be reached, so no gate ran
#   N - the number of gates that failed or were missing
# Deliberately omit -e so every gate runs and its result contributes to the total.
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 2

# Each entry is `name|script|command`. The script field is the file whose absence
# reports MISSING. It is named outright because a command that opens with a flag,
# an inline assignment or a path holding a space has no reliable second word to
# read it from.
GATES=(
  "router fixtures|benchmark/router/run_fixtures.sh|bash benchmark/router/run_fixtures.sh"
  "format fixtures|benchmark/format/run_fixtures.sh|bash benchmark/format/run_fixtures.sh"
  "rule parity|benchmark/gates/rule_parity.py|python3 benchmark/gates/rule_parity.py"
  "example lint|benchmark/gates/example_lint.py|python3 benchmark/gates/example_lint.py"
  "example lint self-test|benchmark/gates/example_lint.py|python3 benchmark/gates/example_lint.py --self-test"
  "vendor sync|scripts/vendor-sync.py|python3 scripts/vendor-sync.py status"
  "vendor sync tests|scripts/tests/test_vendor_sync.py|python3 scripts/tests/test_vendor_sync.py"
  "markdown link integrity|benchmark/gates/check_markdown_links.py|python3 benchmark/gates/check_markdown_links.py"
  "hub check|benchmark/gates/check_hub.py|python3 benchmark/gates/check_hub.py"
  "hub check self-test|benchmark/gates/check_hub.py|python3 benchmark/gates/check_hub.py --self-test"
  "leaf map parity|benchmark/gates/check_leaf_map_parity.py|python3 benchmark/gates/check_leaf_map_parity.py"
  "flow check self-test|sk-create-figjam/scripts/flow_check.py|python3 sk-create-figjam/scripts/flow_check.py --self-test"
  "board composer self-test|sk-create-figjam/scripts/compose_board.py|python3 sk-create-figjam/scripts/compose_board.py --self-test"
  "skilled hub contract|../../.skilled/skills/sk-doc/sk-create-skill/scripts/validate_skill_package.py|python3 ../../.skilled/skills/sk-doc/sk-create-skill/scripts/validate_skill_package.py --strict \"$PWD\""
  "skilled packet contract|../../.skilled/skills/sk-doc/sk-create-skill/scripts/validate_skill_package.py|python3 ../../.skilled/skills/sk-doc/sk-create-skill/scripts/validate_skill_package.py --strict \"$PWD/sk-product-owner\" && python3 ../../.skilled/skills/sk-doc/sk-create-skill/scripts/validate_skill_package.py --strict \"$PWD/sk-create-figjam\""
)
total=${#GATES[@]}
failed=0
skipped=0
for entry in "${GATES[@]}"; do
  name="${entry%%|*}"
  rest="${entry#*|}"
  script="${rest%%|*}"
  command="${rest#*|}"
  if [ "$name" = "rule parity" ] && [ ! -d "../z — Claude Project Sync Loop" ]; then
    printf '  %-24s SKIPPED, the shared Sync Loop folder is not beside this repository\n' "$name"
    skipped=$((skipped + 1))
    continue
  fi
  case "$name" in
    "skilled hub contract"|"skilled packet contract")
      if [ ! -d "../../.skilled" ]; then
        printf '  %-24s SKIPPED, no shared skill folder above this repository to hold the hub to the sk-create-skill contract\n' "$name"
        skipped=$((skipped + 1))
        continue
      fi
      ;;
  esac
  # With no upstream to read, the gate still proves that no vendored file was
  # edited by hand. The note keeps that narrower pass from reading as the full one.
  note=""
  if [ "$name" = "vendor sync" ] && [ -z "${VENDOR_UPSTREAM_ROOT:-}" ] && [ ! -d "../../.skilled" ]; then
    command="python3 scripts/vendor-sync.py status --local"
    note=", local copies only, no shared skill folder above this repository to compare them with"
  fi
  if [ ! -f "$script" ]; then
    printf '  %-24s MISSING\n' "$name"
    failed=$((failed + 1))
    continue
  fi
  if output="$(eval "$command" 2>&1)"; then
    printf '  %-24s ok%s\n' "$name" "$note"
  else
    printf '  %-24s FAILED, its own output follows\n' "$name"
    printf '%s\n' "$output" | sed 's/^/      /'
    failed=$((failed + 1))
  fi
done
echo
if [ "$failed" = 0 ] && [ "$skipped" = 0 ]; then
  echo "all $total gates pass"
  exit 0
fi
if [ "$failed" = 0 ]; then
  echo "$((total - skipped)) of $total gates pass, $skipped skipped"
  exit 0
fi
echo "$failed of $total gates failed"
exit "$failed"

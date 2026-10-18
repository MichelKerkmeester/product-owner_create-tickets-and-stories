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
# The shared parity and residency checks are not in the list. They read the
# Sync Loop declaration against git history and refuse a declaration with
# uncommitted edits, so they run from `benchmark/parity/` once a batch is
# committed.
#
# Exit Codes:
#   0 - every gate passed, or every gate that could run passed and the summary names the skip
#   2 - the system root could not be reached, so no gate ran
#   N - the number of gates that failed or were missing
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 2

GATES=(
  "router fixtures|bash benchmark/router/run_fixtures.sh"
  "format fixtures|bash benchmark/format/run_fixtures.sh"
  "rule parity|python3 benchmark/gates/rule_parity.py"
  "example lint|python3 benchmark/gates/example_lint.py"
  "example lint self-test|python3 benchmark/gates/example_lint.py --self-test"
)
total=${#GATES[@]}
failed=0
skipped=0
for entry in "${GATES[@]}"; do
  name="${entry%%|*}"
  command="${entry#*|}"
  script="$(printf '%s' "$command" | awk '{print $2}')"
  if [ "$name" = "rule parity" ] && [ ! -d "../z — Claude Project Sync Loop" ]; then
    printf '  %-24s SKIPPED, the shared Sync Loop folder is not beside this repository\n' "$name"
    skipped=$((skipped + 1))
    continue
  fi
  if [ ! -f "$script" ]; then
    printf '  %-24s MISSING\n' "$name"
    failed=$((failed + 1))
    continue
  fi
  if output="$(eval "$command" 2>&1)"; then
    printf '  %-24s ok\n' "$name"
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

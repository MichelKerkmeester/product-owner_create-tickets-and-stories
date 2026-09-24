#!/usr/bin/env bash
# Run every after-the-fact check a finished playbook report supports.
#
# The manual testing playbook persists one PASS/FAIL/SKIP verdict per
# scenario. Neither the reply text behind a PASS nor the agreement between a
# scenario's two runtimes is read by that persistence step, so both checks
# this file runs had to be remembered and typed by hand against a finished
# report, and a check that depends on being remembered is the same as no
# check.
#
# Every check runs even after one reports findings, because stopping at the
# first hides the rest, and the exit code carries how many reported rather
# than the first one, so a caller cannot read one as one problem.
#
# What the exit code means: how many checks reported findings, not how many
# failed to run. A dirty reply or a diverging twin is a finding about the
# runtime that produced it, not a defect in this repository, and a caller
# reading the code should reach for the output rather than a revert.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
# Not ${1:?...}, which exits 1, and 1 already means one check reported findings.
# A caller reading the code could not tell a usage error from a real finding.
if [ $# -lt 1 ]; then
  echo "usage: check_report.sh <run report dir>" >&2
  exit 64
fi
REPORT="$1"
if [ ! -d "$REPORT" ]; then
  # Not exit 2: with exactly two checks in the loop below, "$found" can
  # itself reach 2 when both report findings, and a caller could not tell
  # that apart from a missing directory. 66 matches this system's own
  # validate-output-format.cjs, which already uses it for an unreadable
  # target path.
  echo "no report directory at $REPORT, so nothing was checked" >&2
  exit 66
fi

# A fixed path under /tmp is shared, so two concurrent runs, or one run while
# another system's runner is going, overwrite each other's output and a
# reader sees the wrong check's findings under the right check's name.
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

found=0
total=0
for check in lint_replies twin_divergence; do
  total=$((total + 1))
  printf '  %-18s ' "$check"
  if python3 "$HERE/$check.py" "$REPORT" > "$WORK/$check.out" 2>&1; then
    echo "clean"
  else
    rc=$?
    if [ "$rc" = 2 ] || [ "$rc" = 64 ]; then
      echo "could not run, its own output follows"
      sed 's/^/      /' "$WORK/$check.out"
      found=$((found + 1))
      continue
    fi
    echo "findings, its own output follows"
    sed 's/^/      /' "$WORK/$check.out"
    found=$((found + 1))
  fi
done

echo
if [ "$found" = 0 ]; then
  echo "all $total report checks clean"
  exit 0
fi
echo "$found of $total report checks reported findings"
exit "$found"

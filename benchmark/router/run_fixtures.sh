#!/usr/bin/env bash
# Deterministic route-contract gate.
#
# Two checks run, and the gate fails if either one does.
#
# The fixture manifest is the regression oracle for the executable route
# contract: the same command must fail on a naive substring/keyword-first
# router (which would bind $document to DOC, or match bug inside debugging)
# and pass on the exact-token, word-boundary one.
#
# The differential harness is the anti-drift oracle. It lifts the Smart Router
# pseudocode out of the skill document, executes it, and proves the contract
# agrees with it on tables, on each detection layer and on the whole route
# object. Fixtures alone cannot catch prose and code drifting together in the
# same wrong direction, and this catches it.
set -uo pipefail
cd "$(dirname "$0")"

status=0
python3 route_contract.py fixtures.json || status=1
python3 differential.py || status=1
exit "$status"

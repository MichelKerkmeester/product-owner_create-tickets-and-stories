#!/usr/bin/env bash
# This system's entry into the carrier query walk. The walk covers the whole
# declared universe in one pass, not just this system, so every run_query.sh
# in the fleet runs the identical shared query and supplies nothing per-system.
#
# Default range is origin/main..HEAD. Pass --range to check a pinned batch.
set -uo pipefail
cd "$(dirname "$0")"

exec python3 "../../../z — Claude Project Sync Loop/carrier_query.py" walk --range origin/main..HEAD "$@"

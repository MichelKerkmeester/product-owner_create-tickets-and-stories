#!/usr/bin/env bash
# This system's entry into the shared parity gate. The four rules every SYNC.md
# states had a check side in one system out of ten, so "synced" rested on an
# assertion everywhere else. The checks live with the declaration they read, and
# this file supplies the only per-system thing: the id.
#
# Default range is origin/main..HEAD. Pass --range to check a pinned batch.
set -uo pipefail
cd "$(dirname "$0")"

exec python3 "../../../z — Claude Project Sync Loop/validate_parity.py" product-owner "$@"

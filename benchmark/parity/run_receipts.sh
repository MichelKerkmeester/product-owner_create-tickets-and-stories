#!/usr/bin/env bash
# This system's entry into the upload receipt check. A receipt is the only
# record that a live Project was updated, and it stops being trustworthy the
# moment the kernel or the knowledge directory moves, so this wrapper runs the
# shared checker with the receipt required and supplies the one per-system
# thing: the id.
set -uo pipefail
cd "$(dirname "$0")"

exec python3 "../../../z — Claude Project Sync Loop/validate_parity.py" product-owner --receipts "$@"

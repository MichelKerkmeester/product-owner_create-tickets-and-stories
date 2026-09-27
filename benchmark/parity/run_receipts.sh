#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: RECEIPT CHECK RUNNER
# ───────────────────────────────────────────────────────────────
# This system's entry into the upload receipt check. A receipt is the only
# record that a live Project was updated, and it stops being trustworthy the
# moment the kernel or the knowledge directory moves, so this wrapper runs the
# shared checker with the receipt required and supplies the one per-system
# thing: the id.
#
# Exit Codes:
#   2 - The script directory could not be entered, so nothing ran
#   any - Otherwise the delegated checker's own status, since exec replaces this process
set -uo pipefail
cd "$(dirname "$0")" || exit 2

exec python3 "../../../z — Claude Project Sync Loop/validate_parity.py" product-owner --receipts "$@"

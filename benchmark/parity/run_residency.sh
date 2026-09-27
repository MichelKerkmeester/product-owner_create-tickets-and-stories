#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: RESIDENCY CHECK RUNNER
# ───────────────────────────────────────────────────────────────
# This system's entry into the shared residency check. The rows live in the
# parity declaration and the checker reuses the parity gate's readers, so this
# file supplies the only per-system thing: the id.
#
# Exit Codes:
#   2 - The script directory could not be entered, so nothing ran
#   any - Otherwise the delegated checker's own status, since exec replaces this process
set -uo pipefail
cd "$(dirname "$0")" || exit 2

exec bash "../../../z — Claude Project Sync Loop/run_residency.sh" product-owner

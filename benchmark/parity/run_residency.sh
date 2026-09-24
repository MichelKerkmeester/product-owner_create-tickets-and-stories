#!/usr/bin/env bash
# This system's entry into the shared residency check. The rows live in the
# parity declaration and the checker reuses the parity gate's readers, so this
# file supplies the only per-system thing: the id.
set -uo pipefail
cd "$(dirname "$0")"

exec bash "../../../z — Claude Project Sync Loop/run_residency.sh" product-owner

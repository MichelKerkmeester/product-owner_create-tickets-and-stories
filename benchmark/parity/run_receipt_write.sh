#!/usr/bin/env bash
# This system's entry into the upload receipt writer. The shared writer renders
# one receipt line from the live kernel and knowledge directory and verifies it
# with the parity gate's own checker. This file supplies the only per-system
# thing: the directory it writes against.
set -uo pipefail
cd "$(dirname "$0")"

exec python3 "../../../z — Claude Project Sync Loop/write_receipt.py" "$(cd ../.. && pwd)" "$@"

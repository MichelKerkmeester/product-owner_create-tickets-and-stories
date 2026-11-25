#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: VENDORED SKILL UPDATE
# ───────────────────────────────────────────────────────────────
# Update every vendored skill from the public Skilled repository and run the gates.
#
# Usage: bash scripts/update-vendored.sh [--package NAME] [--ref REF] [--remote | --local-upstream]
#
# An external user of this public repository has no checkout of the shared skill
# folder above it, so the sync reads the cached clone of the public repository
# unless a local checkout is found. A local checkout wins when present, because
# it is faster and carries edits that have not been pushed yet. A folder counts
# as a checkout when it holds `.skilled/skills` with at least one skill folder in
# it, so a `.skilled` folder that holds runtime state only never counts.
#
# The rebuild lines are printed again under a heading because the sync output
# scrolls past them, and a stale build is the one failure the gates cannot see.
#
# Exit Codes:
#   0 - the sync and every gate passed
#   1 - the sync or at least one gate failed; the output above names which
#   2 - a bad argument, or the repository root could not be reached

set -euo pipefail

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
readonly SCRIPT_DIR REPO_DIR
readonly CACHE_SUBDIR="product-owner-vendor/skilled"

PACKAGE=""
REF=""
FORCE_REMOTE=false
FORCE_LOCAL=false

# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────

# Print the usage text to stdout
usage() {
    cat <<'USAGE'
usage: bash scripts/update-vendored.sh [--package NAME] [--ref REF] [--remote | --local-upstream]

  --package NAME    update one entry of vendor.json
  --ref REF         with the remote source, the branch, tag or commit to read
  --remote          read upstream from the cached clone of the public repository
  --local-upstream  read upstream from the shared skill folder above this repository
USAGE
}

# Print an error and the usage text to stderr, then exit 2
die_usage() {
    printf 'update-vendored: %s\n' "$1" >&2
    usage >&2
    exit 2
}

# Return 0 when $1 holds at least one skill folder under .skilled/skills
has_skills() {
    local root="$1"
    local entry
    # The glob leaves out dot entries, so a folder of runtime state matches nothing
    for entry in "$root/.skilled/skills"/*/; do
        [[ -d "$entry" ]] && return 0
    done
    return 1
}

# Print the nearest folder at or above $PWD that holds a skill checkout
find_local_upstream() {
    local dir="$PWD"
    while :; do
        if has_skills "$dir"; then
            printf '%s\n' "$dir"
            return 0
        fi
        [[ "$dir" == "/" ]] && return 1
        dir="$(dirname "$dir")"
    done
}

# ───────────────────────────────────────────────────────────────
# 3. ARGUMENTS
# ───────────────────────────────────────────────────────────────

while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --package)
            [[ "$#" -ge 2 ]] || die_usage "--package needs a name"
            PACKAGE="$2"
            shift 2
            ;;
        --ref)
            [[ "$#" -ge 2 ]] || die_usage "--ref needs a value"
            REF="$2"
            shift 2
            ;;
        --remote)
            FORCE_REMOTE=true
            shift
            ;;
        --local-upstream)
            FORCE_LOCAL=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            die_usage "unknown argument $1"
            ;;
    esac
done

if [[ "$FORCE_REMOTE" == true && "$FORCE_LOCAL" == true ]]; then
    die_usage "--remote and --local-upstream name one source, not both"
fi

cd "$REPO_DIR" || exit 2

# ───────────────────────────────────────────────────────────────
# 4. SOURCE SELECTION
# ───────────────────────────────────────────────────────────────

local_root="${VENDOR_UPSTREAM_ROOT:-}"
if [[ -z "$local_root" ]]; then
    local_root="$(find_local_upstream || true)"
fi

source_kind="remote"
if [[ "$FORCE_REMOTE" == true ]]; then
    source_kind="remote"
elif [[ "$FORCE_LOCAL" == true || -n "$local_root" ]]; then
    source_kind="local"
fi

sync_args=(sync)
if [[ "$source_kind" == "remote" ]]; then
    sync_args+=(--remote)
    if [[ -n "$REF" ]]; then
        sync_args+=(--ref "$REF")
    fi
elif [[ -n "$REF" ]]; then
    printf 'update-vendored: --ref applies to the remote source only, ignoring it\n' >&2
fi
if [[ -n "$PACKAGE" ]]; then
    sync_args+=(--package "$PACKAGE")
fi

# The script's own walk-up stops at the first .skilled folder it meets, which can
# be a runtime folder inside the repository, so the root found here is passed on
if [[ "$source_kind" == "local" && -n "$local_root" ]]; then
    export VENDOR_UPSTREAM_ROOT="$local_root"
fi

# ───────────────────────────────────────────────────────────────
# 5. SYNC AND GATES
# ───────────────────────────────────────────────────────────────

printf 'update-vendored: reading upstream from the %s source\n' "$source_kind"
sync_status=0
sync_output="$(python3 scripts/vendor-sync.py "${sync_args[@]}" 2>&1)" || sync_status=$?
printf '%s\n' "$sync_output"

rebuilds="$(printf '%s\n' "$sync_output" | grep 'rebuild: ' | sed 's/^ *rebuild: //' || true)"
if [[ -n "$rebuilds" ]]; then
    printf '\nRebuild these before the gates:\n%s\n' "$rebuilds"
fi

# The vendor sync gate resolves upstream on its own, so a stray .skilled folder in
# the repository would point it away from the clone the sync just read. It gets
# the same clone, at the path cache_dir() in vendor-sync.py builds.
if [[ "$source_kind" == "remote" ]]; then
    export VENDOR_UPSTREAM_ROOT="${VENDOR_UPSTREAM_CACHE:-${XDG_CACHE_HOME:-$HOME/.cache}/$CACHE_SUBDIR}"
fi

# The gates run even after a refused sync, so the caller sees both results
echo
gate_status=0
bash benchmark/gates/run_gates.sh || gate_status=$?

# The gate runner exits with its failure count and vendor-sync uses 2 for a setup
# error, so either could read as a bad argument. Any failure here is reported as 1.
if [[ "$gate_status" -ne 0 || "$sync_status" -ne 0 ]]; then
    exit 1
fi
exit 0

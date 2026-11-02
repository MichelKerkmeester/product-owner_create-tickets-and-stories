#!/usr/bin/env bash
ROOT="/Users/michelkerkmeester/MEGA/Development/AI Systems"
D="$ROOT/AI Systems/Product Owner/specs/011-holdout-review"
cd "$ROOT" || exit 1
s=$(perl -MTime::HiRes=time -e 'print time')
claude -p --model claude-opus-5 --effort xhigh --permission-mode bypassPermissions -- "$(cat "$D/brief.md")" < /dev/null > "$D/run.log" 2>&1
printf "exit=%s seconds=%.0f\n" "$?" "$(perl -e "print $(perl -MTime::HiRes=time -e 'print time')-$s")" >> "$D/run.log"

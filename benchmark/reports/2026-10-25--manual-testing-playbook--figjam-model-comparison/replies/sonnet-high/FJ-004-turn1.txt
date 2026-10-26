Both self-tests pass, with one `SKIP` and one environment workaround, both explained below.

**Summary line:** `1173 of 1173 self-test checks passed` (`flow_check.py` 144 of 144, `compose_board.py` 1029 of 1029)

**Exit status:** `flow_check.py --self-test` exited 0. `compose_board.py --self-test` exited 1 on the first run and 0 on the rerun.

- **Failed first run:** the default Homebrew `node` (`/opt/homebrew/bin/node`) can't start because `libsimdutf.36.dylib` is missing. This is a broken Homebrew install, not a packet fault. The geometry trace calls `node`, so the self-test crashed before any check ran.
- **Passing rerun:** I put nvm's `node` v24.9.0 first on `PATH` for that one command. I changed nothing on the system. The Homebrew `node` is still broken, so run `brew reinstall node` if you want the default working.
- **The `SKIP`:** `flow_check.py` printed one `SKIP`, for `Product Owner - Assets - Flow Templates.md`. It lives in `claude project/knowledge/`, which this install doesn't have. It isn't counted as a pass or a fail, so the 144 covers everything else. If you need that Knowledge mirror checked, it has to be run where that folder exists.
- **Templates and examples:** I read all of them: the 6 files in `assets/templates/` and the 7 in `assets/examples/`. The self-test also passed each of those files and `assets/flow-templates.md`.
- **Left behind:** nothing in the repo or `export/`. I deleted my two output captures in `/tmp`.
- **Other `/tmp` entries:** several older `/tmp` entries (`flowscratch.e2A3aU`, `flowEdpf`, `figjam-fj032` and others) are not from my runs, so I left them. I didn't open them to see what they hold.
- **No board written:** a self-test draws nothing, so I never used FigJam file `<draft-file-key>` and created no new file.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
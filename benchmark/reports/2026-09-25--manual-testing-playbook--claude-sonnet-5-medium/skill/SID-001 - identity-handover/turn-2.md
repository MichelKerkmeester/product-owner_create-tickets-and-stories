I read the file back, but only the end of it, and the line count I printed was probably wrong.

After writing the file, I called Read on the exact export path with `offset: 60`. That returned lines 60 to 65, the last checklist items of the banner section, plus a blank line 66. The content was non-empty and came from the right path, so the file exists and its tail matches what I wrote. I did not read lines 1 to 59 back. I never confirmed the top of the file (the comment header, About, the toggle and reason field groups) from disk, only from the Write call.

The exact string I printed was `Verified: read-back succeeded; 65 lines`. The protocol says `N` is the final line number Read returns. Read's last row was numbered 66 (blank), so `N` should have been 66. I used the last row with text.

The self-scan line `HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: none.` came from my own read-through of the draft. I did not run a script or grep against the card, so it is a manual count.

I can do a full-file Read and reissue the verification line with the correct `N`.
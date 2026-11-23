# Job 10 goal: edits typed in the PRU planner stay saved on ONE VIEW

His word to start, 2026-11-23, on "Should the saving fix start now?": "Start now".

His Q128, who saves: "You save, all readers see (Recommended)". One plan. Only Sergio can change what is saved; everyone allowed on the page sees it.

His Q129, this goal: "Yes, build it (Recommended)".

## The fault, measured

Page 6b855332a9731ea7ef0c3b389db93bd4, served on a bench with ONE VIEW's exact PAGE_CSP (`C:\AI_Building\AI_Dashboards\code sign-in app\server.py`, lines 247-250):

- Browser storage is blocked. 2 typed edits became 0 after a reload.
- After Load, the page says "Edits loaded. Press Save plan to keep them." Save plan does not keep them.
- Download builds the right file and Load restores it exactly. The real save to disk was not tried.

## Why the page cannot fix this alone

The page's header has `connect-src 'none'`, so it cannot call the server. The ONE VIEW frame around it has `connect-src 'self'` (server.py, line 251), so the frame can. The server has a disk that survives a restart and a deploy (`fly.toml`, `/data`).

## The shape

1. The planner hands its typed edits to the ONE VIEW frame by a browser message.
2. The frame sends them to a new server address that accepts a save only from Sergio's sign-in.
3. The server keeps them on the `/data` disk, one file for this page, and keeps each earlier version.
4. On open, the page asks the frame for the saved edits and applies them.
5. Opened outside the frame, or with the server down, the page says plainly that nothing is saved and offers Download.

Only what he typed is saved, as job 08's goal says. Results are never saved.

## Who builds what

- Angie: the planner page side. On a bench copy; the live page is not touched.
- The Brain: server.py and the ONE VIEW frame, which are outside Angie's folder. Through Piston.
- Each piece gets its own blind check, then LAWYER. It goes live on his yes.

## It MUST deliver

1. An edit saved on ONE VIEW is still there after a reload, on another browser, and after a new page release.
2. Only Sergio can save. A reader allowed on the page reads the saved plan and saves nothing. A person not signed in, or not allowed on the page, saves nothing and reads nothing.
3. A saved version is never lost: each save keeps the one before, and a save made from an out-of-date copy is refused and says so.
4. A saved edit whose line no longer exists is listed, never dropped.
5. Every sentence about saving is true where the page is open.

## The tests

1. Type edits, save, reload, open in a second browser: every edit equal.
2. Publish a rebuilt page: every edit still there.
3. Not signed in, signed in but not allowed, a wrong page name, a body too large, a broken file: each refused, nothing written.
4. Two open copies: the second save is refused and nothing is lost.
5. No edits saved: every figure equals page 6b855332.
6. The sign-in app's own tests still pass (`test_server.py`).

## Not in this job

- Job 08's blind check goes on, on page 6b855332. Any repair it asks for goes into the next version with this one.

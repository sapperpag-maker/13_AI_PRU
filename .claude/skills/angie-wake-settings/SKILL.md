---
name: angie-wake-settings
description: Use when wake-up or goodnight calls it at its step 1 in a session that runs in C:\AI_Building\AI_PRU, when Sergio says "wake up", "wake" or "start your day" to Angie. Covers Angie's desk name, folder to pull, checkpoints folder, log, open-items list and its own wake checks in order - Angie's newest checkpoint, TO DO.md. Called by wake-up and goodnight. Invoke before Angie's wake reads any file.
---

# Angie's wake settings (a utility)

Called by `wake-up` at step 1, and by `goodnight` at step 1.
Input: the folder the session runs in.
Output: six fields - desk name, folder to pull, checkpoints folder, log, open-items list, own checks in order.

## STEP 0: the rules

| Call | Run right before | Meant to return |
|---|---|---|
| none | - | the rules program already runs before every reply and at each job skill's STEP 0 |

## Limits

- Run no check, read no checkpoint or list: only say where they are and what to run. Wake-up runs them.
- Name no file in `C:\AI_Office`. Call no skill. Write no file. Ask Sergio nothing.

## Steps

1. Run `python3.14 "C:\AI_Building\AI_HQ\04 Tools\Tools\desk_settings.py" --folder <the folder the session runs in>`. It finds the desk's settings file (Angie's is `C:\AI_Building\AI_PRU\DESK_SETTINGS.md`) and checks each place exists.
2. Its last line is not `RESULT: SETTINGS FOUND`, or its `Desk:` is not Angie: hand back "not Angie's folder" with its `PROBLEM:` lines and no settings. Otherwise take its five lines as printed; never fill a place by hand.
3. List Angie's own checks, in this order:
   1. When the wake page names no closing checkpoint of Angie's, read the newest file in `C:\AI_Building\AI_MISC\05 Checkpoints\Angie Checkpoint`.
   2. Read `C:\AI_Building\AI_PRU\TO DO.md`.
4. Hand back the six fields.

## The result

Six lines in the chat: `Desk:`, `Folder to pull:`, `Checkpoints:`, `Log:`, `Open items:` with step 2's values, then `Own checks:` with step 3's two, numbered.

## Known traps

- Angie's folder has its own online copy: `desk_settings.py` refuses it until the folder holds its `.git`.

## Final check

The program's last line SETTINGS FOUND? Six fields: the desk's name and four full paths with no backslash at the end, two checks in order? Nothing run, read or written?

Hand back: give the six fields to the orchestrator that called you and return to its step 1. Invoked alone: hand Sergio the six fields.

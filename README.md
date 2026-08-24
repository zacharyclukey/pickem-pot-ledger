# Pick'em Pot Ledger

A one-page web app for running a weekly NFL pick'em pool: $5 a week, winner takes
the pot. It replaces the Sleeper dues checkboxes plus the prepay spreadsheet with a
single ledger.

Everything is stored in the browser it's used in. No accounts, no server, no
tokens, nothing to push.

## The rule it enforces

Dues are due **before Thursday night kickoff**. When you lock a week, anyone who
isn't paid up right then is **out for that week** — never charged, never in the
pot. There is no back paying. Money already on account rolls forward, so anyone
who prepays is entered automatically every week until their credit runs out.

## Putting it on GitHub Pages

1. Create a repository (any name — `pickem` works).
2. Put every file in this folder at the root of the repo:
   `index.html`, `manifest.webmanifest`, `sw.js`, `icon.svg`, `icon-180.png`,
   `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`.
   On github.com: **Add file → Upload files**, drag them all in, **Commit**.
3. **Settings → Pages**. Under *Build and deployment*, set Source to
   **Deploy from a branch**, branch `main`, folder `/ (root)`. Save.
4. Wait a minute, then open `https://<your-username>.github.io/<repo>/`.

A public repo gets Pages for free. A private repo needs GitHub Pro.

## Using it on a phone — install it, don't just bookmark it

Open the URL, then **Share → Add to Home Screen** (iOS) or **⋮ → Install app**
(Android). It opens full screen and works without a signal.

This is not just polish. The ledger lives in the browser's storage, and iOS
clears that storage for ordinary Safari tabs after about a week of not visiting
the site. Installed to the Home Screen, it is exempt. A bookmarked tab left
alone over a bye week can come back empty.

## First-time setup

1. **Add players** — paste the roster, one name per line.
2. **League setup** (Money tab → Edit) — league name, season, buy-in, weeks.
3. Log payments as they come in, tagged by source.

## Each week

1. Money arrives → **Log payment** (or the `+` next to a name).
2. Thursday, before kickoff → **Kickoff** tab → **Copy** the reminder, paste it
   into the league chat.
3. At kickoff → **Lock week N**. Anyone unpaid is out for the week and gets a
   mark on the Missed weeks list.
4. After the games → pick the winner and say what happened to the pot:
   **Owed**, **Paid out**, or **Left in as credit** (rolls into their account).
5. **Open week N+1** — this locks the previous week automatically if you forgot.

## Backups

The ledger lives in one browser's storage. Clearing site data wipes it.
**Money tab → Export backup** saves a JSON file; **Restore backup** reads one
back. Email it to yourself.

The app nags about this on its own: it shows a banner when no backup has ever
been taken and again once one is two weeks old, and it automatically exports a
backup before the two actions that can erase a season — **Start a new season**
and **Restore backup**.

If the browser ever refuses to save, a red banner says so. Everything after that
point is on screen only. Export a backup before closing the tab.

## Guardrails on the ledger

Three things used to change the books quietly. They now announce themselves:

- **The weekly buy-in is stamped onto a week when that week locks.** Changing the
  buy-in later re-prices only the week still open, never settled weeks. A locked
  week's pot and what each player was charged for it can no longer move.
- **Re-locking a week that was unlocked names anyone it would let back in.** Someone
  who paid after kickoff got a missed mark; re-locking would silently readmit
  them and grow the pot. The button and a note now say who and by how much.
- **Jumping *Current week* forward more than one week asks twice.** Moving from week
  1 to week 5 bills every player four weeks of dues out of their credit. The
  first Save shows the damage; the second commits it.

Removing a player also deletes their payment history, so the confirm button says
how many payments go with them.

## Editing the app

`src.html` is the source. `build.py` generates `index.html` (this site) and
`artifact.html` (a version for publishing as a Claude artifact) from it.

```
python3 build.py
```

Don't edit `index.html` directly — the next build overwrites it.

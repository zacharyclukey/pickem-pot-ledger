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
2. Upload every file in this folder to the root of the repo:
   `index.html`, `manifest.webmanifest`, `sw.js`, `icon.svg`, `icon-180.png`,
   `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`.
   On github.com: **Add file → Upload files**, drag them all in, **Commit**.
3. **Settings → Pages**. Under *Build and deployment*, set Source to
   **Deploy from a branch**, branch `main`, folder `/ (root)`. Save.
4. Wait a minute, then open `https://<your-username>.github.io/<repo>/`.

A public repo gets Pages for free. A private repo needs GitHub Pro.

## Using it on a phone

Open the URL, then **Share → Add to Home Screen** (iOS) or **⋮ → Install app**
(Android). It opens full screen like an app and works without a signal.

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
back. Worth doing every few weeks — email it to yourself.

## Editing the app

`src.html` is the source. `build.py` generates `index.html` (this site) and
`artifact.html` (a version for publishing as a Claude artifact) from it.

```
python3 build.py
```

Don't edit `index.html` directly — the next build overwrites it.

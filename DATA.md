# Team 18833 — Megiddo Lions 🦁

> **Source of truth:** `DATA.md` — all team data lives here. The website (`index.html`) reads **only** this file, and
> `update_team_data.py` rewrites it automatically. **Do not edit numbers by hand** — run the updater or let GitHub
> Actions do it. Prose sections marked ✍️ are safe to edit.

---

## 1. Auto-update system

The data in this file updates itself — no manual work needed.

| Piece | What it does | Where it runs |
|---|---|---|
| `update_team_data.py` | Scrapes FIRST's official event pages for **every season** the team played (summary + location + awards + matches) and rewrites **Section 5** of this file | your PC (`python3 update_team_data.py`) |
| `.github/workflows/update-data.yml` | Runs the same script **every Sunday 06:00 UTC** + on demand, and commits changes automatically | GitHub Actions |

**To force an update right now:** tell the agent *"update the team data"* (it runs the script), or run locally:

```bash
python3 update_team_data.py          # rewrites Section 5 of DATA.md
python3 update_team_data.py --check  # just print what changed, no file write
```

GitHub Actions also refreshes it weekly — see [`.github/workflows/update-data.yml`](.github/workflows/update-data.yml).

### Add this to any future task list (agent instructions)

When building the **Megiddo Lions website**, the agent MUST:

1. Keep `DATA.md` as the single data source — the site parses it directly, no data may be hard-coded in the HTML/JS.
2. Keep the parser (`parseDataMd`) compatible with this file's exact section structure (see `index.html`).
3. Keep the auto-update pair working: `update_team_data.py` + `.github/workflows/update-data.yml` (weekly cron).
4. After adding new data (team members, photos, social links, etc.), extend `update_team_data.py` so the new data
   stays auto-updated too.
5. Team-provided facts that FIRST's site cannot confirm (e.g. the **claimed 2nd-place finish at the 2019 FIRST
   Global Challenge in Dubai** — the participation itself *is* verified) live in §4/§6 and must **not** be deleted
   when regenerating data — the updater only rewrites §5.
6. Serve the site with **GitHub Pages** from the repo root (no build step needed) — settings → Pages → Deploy from
   branch → `main` → `/ (root)`.

---

## 2. Team profile

| Field | Value |
|---|---|
| **Number** | 18833 |
| **Name** | Megiddo Lions |
| **School / Organization** | Megiddo high school |
| **From** | Regional Council of Megiddo, Z (Northern District), Israel |
| **Country** | Israel 🇮🇱 |
| **Region (FIRST)** | ISR — Israel |
| **Rookie year** | 2020 (team founded for the 2020 *ULTIMATE GOAL* season) |
| **Current season** | 2025 *DECODE* |
| **Sponsors** | Megiddo high school |

The team is named after **Tel Megiddo** (Armageddon), the famous ancient site in the Megiddo Regional Council —
hence "Megiddo Lions".

## 3. Logo links

The team has no FIRST-hosted logo image (FIRST publishes no logos). Use the links below on the website; they are
platform profile pages (avatars can be pulled from them):

| Source | Link | Status |
|---|---|---|
| FIRST official team page | https://ftc-events.firstinspires.org/2025/team/18833 | ✅ verified |
| The Orange Alliance | https://theorangealliance.org/teams/18833 | ✅ verified |
| FTC-Link (scouting/stats) | https://ftc-link.org/teams/18833 | ✅ linked (blocked from this sandbox, normal) |
| Statbotics (API) | https://api.statbotics.io/v3/team/18833/year/2025 | ✅ linked (blocked from this sandbox, normal) |
| FIRST profile (season pick) | https://www.firstinspires.org/team-profile/18833 | ✅ linked (pulls avatar) |

*Website note: embed the logo as an `<img>` pointing at the FIRST profile avatar; fall back to a generated
"18833" badge if the image 404s (this fallback is already implemented in `index.html`).*

## 4. Achievements — season by season

- **2019 FIRST Global Challenge — Dubai, UAE (Oct 24–27)** — 🇮🇱 **Team Israel was the Megiddo Lions** (FTC 12797 + FRC 5038, Megiddo Regional high school) — ✅ verified via FIRST Global's official team page (first.global/2019-nations/israel-2019). 📌 The claim of a **2nd-place-in-the-world finish is team-provided and not independently verified**: archived official rankings list no team names and no public 2019 results document has been found. Treat as a claim until a source (photo, video, article) confirms it.
- **2020 ULTIMATE GOAL** — rookie season, no official events (COVID remote year). Recognition: *Top Ranked 3rd Place* at Israel FTC Scrimmage #2 REMOTE.
- **2021 FREIGHT FRENZY** — 🏆 **Israel Championship — Ashram Division CHAMPIONS** (event champions), **Inspire Award 2nd Place** at the Israel Championship, **Finalist Alliance 1st Team Selected** at the Israel Championship, **Design Award** at the Israel Championship, **Winning Alliance Captain** at Israel ISR Scrimmage #2.
- **2022 POWERPLAY** — 🏆 **Inspire Award 1st Place at the Israel Championship** (Israel's highest team award → invited to the FIRST World Championship, Houston, April 2023), Solar Division Finalist Alliance Captain, ranked 2nd in Solar Division qualifications; competed at the **FIRST World Championship Houston 2023 — Franklin Division** (rank 23 of 48).
- **2023 CENTERSTAGE** — Israel Championship Shemer Division: rank 1 of 20 in qualifications, alliance captain; Motivate Award at IL Qualifier #2 Agnon and at the Israel Championship.
- **2024 INTO THE DEEP** — Israel Championship Pacific Division finalist alliance (1st team selected); Think Award at the Israel Championship; Finalist Alliance Captain + Connect Award at Qualifier 2 Neptune League; Control Award 3rd Place at the **European Premier Event** (off-season invitational, Eindhoven NL); rank 10 of 48 in the European Premier Event Escher Division qualifications.
- **2025 DECODE** *(current)* — Think Award + Finalist Alliance 1st Team Selected at Qualifier 1 Codex League; Think Award + alliance captain (rank 2 of 24) at Qualifier 2 Codex League.

### "Did they win the world championship?" — the answer

**No.** Team 18833 has **never won the FTC World Championship**. Their best international results are:
- **2019:** 🇮🇱 **Team Israel at the FIRST Global Challenge, Dubai = the Megiddo Lions** (FTC 12797 + FRC 5038) — verified. The reported **2nd place in the world** remains a **team-provided claim, not independently verified**.
- **2021:** 🏆 **Champions of the Israel Championship, Ashram Division** (division of the national championship — *not* the World Championship).
- **2022:** 🏆 **Inspire Award, Israel Championship** (Israel's highest honor; earned a spot at the **World Championship in Houston 2023**, where they competed in the Franklin Division and finished qualifications ranked **23rd of 48 teams**, no playoff appearance).
- **2024:** invited to the **European Premier Event** (a strong inter-regional off-season event, ~48 teams), Control Award 3rd place, rank 10 of 48 in Escher Division quals.

## 5. Live team data

*Content between the `BEGIN LIVE TEAM DATA` and `END LIVE TEAM DATA` markers is **auto-generated** by
`update_team_data.py` — do not edit by hand.*

<!-- BEGIN LIVE TEAM DATA (generated by update_team_data.py — do not edit) -->

### Team identity
Number: 18833
Name: Megiddo Lions
Organization: Megiddo high school
Location: Regional Council of Megiddo, Z, Israel
Country: Israel
Region: Israel
Rookie year: 2020
Current season: 2025
Current season name: DECODE
Sponsors: Megiddo high school
Data updated: 2026-09-17

### Season history
#### 2025 — DECODE
Record: 12-7-0 (qualification 9-3-0) at 2 official events
Event: Qualifier 1 | Codex League — quals rank 8 of 26
Event: Qualifier 2 | Codex League — quals rank 2 of 24
Award: Finalist Alliance - 1st Team Selected — Qualifier 1 | Codex League
Award: Think Award — Qualifier 2 | Codex League

#### 2024 — INTO THE DEEP
Record: 21-13-0 (qualification 13-5-0) at 4 official events
Event: Qualifier 1 | Neptune League — quals rank 10 of 31
Event: Qualifier 2 | Neptune League — quals rank 3 of 31
Event: Israel Championship - Pacific Division — quals rank 12 of 21
Event: European Premier Event - Escher Division — quals rank 10 of 48
Award: Finalist Alliance - Captain — Qualifier 2 | Neptune League
Award: Connect Award — Qualifier 2 | Neptune League
Award: Control Award 3rd Place — European Premier Event
Award: Pacific Division Finalist Alliance - 1st Team Selected — Israel Championship
Award: Think Award — Israel Championship

#### 2023 — CENTERSTAGE
Record: 13-12-0 (qualification 12-6-0) at 3 official events
Event: IL Qualifier #1 - Agnon — quals rank 9 of 25
Event: IL Qualifier #2 - Agnon — quals rank 15 of 24
Event: Israel Championship - Shemer Division — quals rank 1 of 20
Award: Motivate Award — IL Qualifier #2 - Agnon
Award: Motivate Award — Israel Championship

#### 2022 — POWERPLAY
Record: 12-8-0 (qualification 11-6-0) at 2 official events
Event: Israel Championship - Solar Division — quals rank 2 of 24
Event: FIRST Championship - Houston - World Championship - FIRST Tech Challenge - Franklin Division — quals rank 23 of 48
Award: Inspire Award — Israel Championship
Award: Solar Division Finalist Alliance - Captain — Israel Championship

#### 2021 — FREIGHT FRENZY
Record: 8-4-0 (qualification 4-2-0) at 2 official events
Event: Israel ISR Championship - Ashram Division — quals rank 5 of 21
Award: Winning Alliance - 1st Team Selected — Israel ISR Championship - Ashram Division
Award: Inspire Award 2nd Place — Israel ISR Championship
Award: Finalist Alliance - 1st Team Selected — Israel ISR Championship
Award: Design Award — Israel ISR Championship
Award: Winning Alliance - Captain — Israel ISR Scrimmage #2

#### 2020 — ULTIMATE GOAL
Record: no official events
Events: none
Award: Top Ranked 3rd Place — Israel FTC Scrimmage #2 REMOTE

<!-- END LIVE TEAM DATA (generated by update_team_data.py — do not edit) -->

## 6. Rankings — where they stand

Live rankings change every match day, so this file stores **per-season records** (from FIRST, auto-updated in
Section 5) rather than a snapshot. For live standings see the links in Section 3 (FTC-Link / Statbotics / FIRST).

Best-of-all-time summary (verify against Section 5):

| Ranking question | Answer |
|---|---|
| Best international appearance | 🇮🇱 Team Israel — FIRST Global Challenge, Dubai 2019 (verified: the Megiddo Lions, FTC 12797 + FRC 5038) |
| Claimed placement there | 📌 2nd place in the world — **team-provided, unverified** |
| Best national (Israel) result | 🏆 Israel Championship Ashram Division **Champions** (2021) |
| Best national award | 🏆 **Inspire Award 1st Place**, Israel Championship (2022) |
| World Championship appearances | 1 — Houston 2023 (Franklin Division, quals rank 23/48) |
| Best world-championship rank | 23 of 48 (Franklin Division qualifications, 2023) |
| Best European event result | Control Award 3rd + quals rank 10/48 — European Premier Event 2024 |

## 7. Data sources

- FIRST official FTC events pages, per season: `https://ftc-events.firstinspires.org/<SEASON>/team/18833`
  (team profile: location, region, rookie year, sponsors; event list with awards, match records, ranks).
- The Orange Alliance team page: `https://theorangealliance.org/teams/18833`.
- **2019 Dubai (FIRST Global Challenge):** Team Israel = Megiddo Lions (FTC 12797 + FRC 5038) — ✅ verified from
  FIRST Global's official team page: `https://first.global/2019-nations/israel-2019/` (archived). The reported
  **2nd-place-in-the-world placement is team-provided and NOT independently verified** (official rankings archives
  carry no team names; no public results document found — checked 2026-09-17).
- All FTC facts above were verified against those sources on **2026-09-17**.

## 8. Website

The website lives in **`index.html`** at the repo root (static site — HTML + vanilla JS, no build step) and is
served by **GitHub Pages** (GitHub runs the server). It parses **`DATA.md`** on page load and renders everything:
profile, logo, achievements, awards and per-season records — so `DATA.md` stays the single source of truth.

- Local preview: `python3 -m http.server 8000` → http://localhost:8000
- Enable publicly: repo **Settings → Pages → Build and deployment → Deploy from a branch → `main` → `/ (root)`**.
  The site then appears at `https://<username>.github.io/<repo-name>/`.
- Data updates: GitHub Actions refreshes `DATA.md` weekly; the site shows the new data on next visit (no rebuild
  needed — it parses the current file).

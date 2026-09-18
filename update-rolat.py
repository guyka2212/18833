#!/usr/bin/env python3
"""update-rolat.py — add a robot to the Megiddo Lions website (the "### Robots" table in DATA.md §4).

✏️  EASIEST WAY — fill in the values in the EDIT block below, then run:

    python3 update-rolat.py

Or do it all on the command line:

    python3 update-rolat.py "https://www.youtube.com/watch?v=cfBVDyp9w6w" --name "BAR" --year 2024 --season-name "INTO THE DEEP"

What it does
  1. Pulls the 11-character video ID out of the YouTube link.
  2. Appends a row to the "### Robots" table in DATA.md (skips duplicates).
  3. Downloads the video's thumbnail to robots/<ID>.jpg — the website's photo
     carousel shows that file and falls back to YouTube's own copy if it is missing.
  4. Prints what to do next (commit + push).

Season format tip: season cells look like  2025 *DECODE*  (year + italic game name).
If you leave SEASON empty, the team's current season (from DATA.md's live block) is used.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

# ------------------------------------------------------------------ ✏️ EDIT ME
VIDEO_URL = ""    # paste the full YouTube link of the robot's video
ROBOT_NAME = ""   # e.g. "BAR"            — leave empty to use "(YEAR robot)"
YEAR = ""         # e.g. 2024             — the FIRST season year (2024 = the 2024–25 season)
SEASON_NAME = ""  # e.g. "INTO THE DEEP"  — the season/game name
GAME = ""         # e.g. "INTO THE DEEP"  — leave empty to reuse SEASON_NAME
# -------------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent
DATA_MD = ROOT / "DATA.md"
ROBOTS_DIR = ROOT / "robots"
UA = {"User-Agent": "Mozilla/5.0 (compatible; MegiddoLions18833-robot-updater)"}


def video_id(url: str) -> str:
    """Extract the 11-char video ID from any YouTube link shape."""
    m = re.search(r"(?:v=|youtu\.be/|/embed/|/shorts/|/live/)([\w-]{11})", url)
    if not m:
        sys.exit(f"✗ Could not find a video ID in: {url!r}")
    return m.group(1)


def current_season(md: str) -> tuple[str, str]:
    """Return (season_cell, game) from DATA.md's live block, e.g. ('2025 *DECODE*', 'DECODE')."""
    year = re.search(r"^Current season: (\d{4})$", md, re.M)
    name = re.search(r"^Current season name: (.+)$", md, re.M)
    if not (year and name):
        sys.exit("✗ SEASON is empty and DATA.md has no live 'Current season' block — pass --season.")
    game = name.group(1).strip()
    return f"{year.group(1)} *{game}*", game


def download_thumbnail(vid: str) -> str | None:
    """Save the video's thumbnail to robots/<ID>.jpg. Returns the path or None."""
    for size in ("maxresdefault", "hqdefault"):  # max-res first, small size as backup
        url = f"https://i.ytimg.com/vi/{vid}/{size}.jpg"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
                data = r.read()
            if r.status == 200 and data[:2] == b"\xff\xd8" and len(data) > 1000:  # a real JPEG, not a placeholder
                ROBOTS_DIR.mkdir(exist_ok=True)
                (ROBOTS_DIR / f"{vid}.jpg").write_bytes(data)
                return f"robots/{vid}.jpg"
        except Exception as e:
            print(f"  … {size}.jpg failed: {e}")
    return None


def insert_row(md: str, row: str) -> str:
    """Insert a table row as the last row of the '### Robots' table in DATA.md."""
    lines = md.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "### Robots")
    except StopIteration:
        sys.exit('✗ "### Robots" section not found in DATA.md.')
    end = start + 1
    while end < len(lines) and not lines[end].startswith("## "):
        end += 1
    last_table = max(i for i in range(start, end) if lines[i].lstrip().startswith("|"))
    lines.insert(last_table + 1, row)
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser(description="Add a robot (video + photo) to the website's Robots section.")
    p.add_argument("url", nargs="?", default=VIDEO_URL, help="YouTube link of the robot's video")
    p.add_argument("--name", default=ROBOT_NAME, help='robot name, e.g. "BAR"')
    p.add_argument("--season", default="", help='full season cell, e.g. "2024 *INTO THE DEEP*" (overrides --year/--season-name)')
    p.add_argument("--year", default=str(YEAR) if YEAR else "", help="season year, e.g. 2024 (= the 2024–25 season)")
    p.add_argument("--season-name", "--sesson-name", dest="season_name", default=SEASON_NAME,
                   help='season/game name, e.g. "INTO THE DEEP"')
    p.add_argument("--game", default=GAME, help="game column (defaults to the season name)")
    p.add_argument("--skip-download", action="store_true", help="do not download the thumbnail")
    a = p.parse_args()

    if not a.url:
        sys.exit("✗ No video link given — fill VIDEO_URL in the EDIT block or pass it on the command line.")

    md = DATA_MD.read_text(encoding="utf-8")
    vid = video_id(a.url)
    print(f"Video ID: {vid}")

    if f"watch?v={vid}" in md:
        sys.exit(f"✓ This video ({vid}) is already in DATA.md — nothing to do.")

    season, game = a.season, a.game
    if not season:
        if a.season_name and not a.year:
            sys.exit("✗ Pass --year together with --season-name (or use --season, or leave both empty for the current season).")
        if a.year or a.season_name:
            season = f"{a.year} *{a.season_name}*" if a.year and a.season_name else str(a.year or f"*{a.season_name}*")
            game = game or a.season_name
        else:
            season, auto_game = current_season(md)
            game = game or auto_game
    elif not game:
        # '2025 *DECODE*' -> 'DECODE'
        game = re.sub(r"[*_]", "", re.sub(r"^\s*\d{4}\s*", "", season)).strip() or "—"
    name = a.name or (f"({a.year} robot)" if a.year else "(new robot)")

    row = f"| {name} | {season} | {game} | https://www.youtube.com/watch?v={vid} |"
    DATA_MD.write_text(insert_row(md, row), encoding="utf-8")
    print(f"✓ Added row to the Robots table: {row}")

    if a.skip_download:
        print("– Skipped thumbnail download (--skip-download); the site will use YouTube's copy.")
    else:
        path = download_thumbnail(vid)
        if path:
            print(f"✓ Thumbnail saved: {path}")
        else:
            print("✗ Thumbnail download failed — no problem: the site falls back to YouTube's copy.")

    print("\nNext steps:")
    print("  git add DATA.md robots/")
    print('  git commit -m "Add robot to the Robots section" && git push')


if __name__ == "__main__":
    main()

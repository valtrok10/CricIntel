"""Build CricIntel delivery-level CSV and SQLite database from Cricsheet IPL JSON.

Run from any working directory:
    python src/build_dataset.py

Expected layout: project_root/src/build_dataset.py and project_root/data/raw/*.json
"""

import json
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
CSV_PATH = ROOT / "data" / "processed" / "ipl_deliveries.csv"
DB_PATH = ROOT / "sql" / "cricintel.db"


def get_phase(over_number: int) -> str:
    if over_number < 6:
        return "Powerplay"
    if over_number < 15:
        return "Middle"
    return "Death"


def build_records(json_files: list[Path]) -> list[dict]:
    records = []
    for file_path in json_files:
        with file_path.open("r", encoding="utf-8") as handle:
            match = json.load(handle)

        info = match["info"]
        dates = info.get("dates", [])
        match_date = dates[0] if dates else None
        teams = info.get("teams", [])

        for innings_number, innings in enumerate(match["innings"], start=1):
            batting_team = innings["team"]
            bowling_team = next((team for team in teams if team != batting_team), None)

            for over in innings["overs"]:
                over_number = over["over"]
                for delivery in over["deliveries"]:
                    extras = delivery.get("extras", {})
                    wides = extras.get("wides", 0)
                    noballs = extras.get("noballs", 0)
                    wickets = delivery.get("wickets", [])

                    records.append({
                        "match_id": file_path.stem,
                        "date": match_date,
                        "city": info.get("city"),
                        "venue": info.get("venue"),
                        "innings": innings_number,
                        "batting_team": batting_team,
                        "bowling_team": bowling_team,
                        "over": over_number,
                        "wides": wides,
                        "noballs": noballs,
                        "byes": extras.get("byes", 0),
                        "legbyes": extras.get("legbyes", 0),
                        "is_legal_delivery": wides == 0 and noballs == 0,
                        "is_wicket": len(wickets) > 0,
                        "delivery": delivery.get("actual_delivery"),
                        "batter": delivery["batter"],
                        "non_striker": delivery["non_striker"],
                        "bowler": delivery["bowler"],
                        "batter_runs": delivery["runs"]["batter"],
                        "extra_runs": delivery["runs"]["extras"],
                        "total_runs": delivery["runs"]["total"],
                    })
    return records


def main() -> None:
    json_files = sorted(RAW_DIR.glob("*.json"))
    if not json_files:
        raise FileNotFoundError(f"No JSON files found in {RAW_DIR}")

    df = pd.DataFrame(build_records(json_files))
    df["date"] = pd.to_datetime(df["date"])
    df["season"] = df["date"].dt.year
    df["phase"] = df["over"].apply(get_phase)
    df["is_boundary"] = df["batter_runs"].isin([4, 6])
    df["is_dot"] = df["total_runs"] == 0
    df["ball_faced"] = (df["wides"] == 0).astype(int)
    df["is_four"] = (df["batter_runs"] == 4).astype(int)
    df["is_six"] = (df["batter_runs"] == 6).astype(int)

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CSV_PATH, index=False)
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("deliveries", conn, if_exists="replace", index=False)

    print(f"Matches: {df['match_id'].nunique():,}")
    print(f"Delivery events: {len(df):,}")
    print(f"CSV: {CSV_PATH}")
    print(f"SQLite: {DB_PATH}")


if __name__ == "__main__":
    main()

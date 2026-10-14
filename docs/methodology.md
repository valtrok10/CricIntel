# CricIntel — Data Processing & Analytics Methodology

## 1. Data Source

CricIntel uses IPL ball-by-ball match data provided by [Cricsheet](https://cricsheet.org/).

The processed dataset contains:

- **1,243 matches**
- **295,732 delivery events**
- Match metadata, batting and bowling teams, delivery-level runs, extras and wicket events

## 2. Data Extraction

Python reads individual match JSON files and extracts:

- Match ID, date, city and venue
- Innings number and participating teams
- Over and delivery information
- Batter, non-striker and bowler
- Batter runs, extras and total runs
- Wicket events

The extracted records are combined into a Pandas DataFrame.

## 3. Feature Engineering

| Feature | Definition |
|---|---|
| `season` | Year extracted from match date |
| `phase` | Powerplay: overs 1–6; Middle: 7–15; Death: 16–20 |
| `is_boundary` | Batter scores 4 or 6 runs |
| `is_four` | Batter scores exactly 4 runs |
| `is_six` | Batter scores exactly 6 runs |
| `ball_faced` | 1 for deliveries other than wides |
| `is_dot` | Total delivery runs equal zero |
| `is_legal_delivery` | Neither a wide nor a no-ball |
| `is_wicket` | At least one dismissal recorded on the delivery |

## 4. Key Metrics

**Batting strike rate**

Strike Rate = (Batter Runs / Balls Faced) × 100

**Boundary percentage**

Boundary % = (Boundary Deliveries / Balls Faced) × 100

**Team run rate**

Run Rate = (Total Team Runs / Legal Deliveries) × 6

**Batter dot-ball percentage**

Batter Dot Ball % = (Deliveries with zero batter runs, excluding wides / Balls Faced) × 100

## 5. SQL Analysis

The SQLite database supports:

- Career run-scorer rankings
- Phase-wise batter performance
- Death-over specialist identification
- Batter–bowler matchup analysis
- Team scoring performance by innings phase

Minimum balls-faced thresholds are applied to selected analyses to avoid rankings dominated by extremely small samples.

## 6. Power BI Reporting

CricIntel contains four interactive dashboard pages:

1. **IPL Overview:** League-wide trends and team performance
2. **Player Intelligence:** Individual batting performance
3. **Decision Lab:** Player comparison and specialist identification
4. **Situational Intelligence:** Batting first versus chasing, score distributions and phase-based dot-ball analysis

DAX measures support interactive filtering, comparisons and qualified performance rankings.

## 7. Data Limitations

- Wicket events include run-outs and other dismissals; they should not be interpreted as bowler-credited wickets.
- Historical franchise names are not normalized.
- Season is derived from the calendar year of the match date.
- Phase definitions assume standard T20 innings.
- No-ball deliveries count toward batter balls faced, while wides do not.
- Some matchup and phase statistics may have small samples.
- Batting-style profiles are analytical heuristics, not official player-role classifications.
- The dataset and dashboards are descriptive and analytical; they do not constitute a trained predictive model.

## 8. Reproducibility

The Python script `src/build_dataset.py` recreates the processed CSV and SQLite database from the raw JSON match files.

The Power BI dashboard uses the processed data for interactive analysis.

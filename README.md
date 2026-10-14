# CricIntel — IPL Performance Intelligence & Decision Analytics

An end-to-end cricket analytics project that transforms IPL ball-by-ball match data into interactive performance dashboards and decision-support insights using Python, SQL and Power BI.

## Project Overview

CricIntel analyzes **1,243 IPL matches and 295,732 delivery events** to explore batting performance, match situations, scoring patterns and player comparisons.

The project combines data engineering, exploratory analysis, SQL querying and business intelligence into a reproducible analytics workflow.

## Technology Stack

- **Python:** Data extraction, cleaning and feature engineering
- **Pandas:** Data transformation and analysis
- **SQLite:** Structured storage and SQL analysis
- **Power BI:** Interactive dashboards and DAX measures
- **Jupyter Notebook:** Exploratory data analysis
- **Git & GitHub:** Version control and project documentation

## Analytics Dashboards

### 1. IPL Overview — The Game in Numbers
League-level performance analysis, including total matches, runs, wicket events, seasonal trends, phase-wise scoring rates and team comparisons.

### 2. Player Intelligence — Beyond the Scorecard
Individual batting analysis covering runs, strike rate, boundary percentage, scoring contributions, seasonal trends and bowler matchups.

### 3. Decision Lab — Where Data Meets Decision
Player comparison and specialist identification using phase-specific strike rates, minimum sample-size thresholds and batting-style profiles.

### 4. Situational Intelligence — Performance Under Context
Contextual batting analysis covering batting first versus chasing, innings score distributions, dot-ball percentages and seasonal strike-rate trends.


## Dashboard Preview

### 1. IPL Overview
![IPL Overview](docs/screenshots/IPL%20Overview.png)

### 2. Player Intelligence
![Player Intelligence](docs/screenshots/Player%20Intelligence.png)

### 3. Decision Lab
![Decision Lab](docs/screenshots/Decision%20Lab.png)

### 4. Situational Intelligence
![Situational Intelligence](docs/screenshots/Decision%20Intelligence%20Layout.png)


## Data Pipeline

1. Read raw IPL match JSON files.
2. Extract match, innings and ball-by-ball delivery records.
3. Transform the records into a Pandas DataFrame.
4. Engineer analytical features including season, batting phase, boundaries and balls faced.
5. Export the processed dataset to CSV.
6. Store delivery records in SQLite for SQL analysis.
7. Build interactive Power BI dashboards.

## Dataset

**Source:** Cricsheet IPL ball-by-ball JSON data.

- Matches: 1,243
- Delivery events: 295,732
- Granularity: One record per delivery event

The data includes batting and bowling teams, batters, bowlers, runs, extras, wicket events and match context.

## Project Structure

```text
CricIntel/
├── dashboards/
│   └── cricintel.pbix
├── data/
│   ├── raw/
│   └── processed/
│       └── ipl_deliveries.csv
├── docs/
│   └── screenshots/
├── notebooks/
│   └── data_understanding.ipynb
├── reports/
├── sql/
│   ├── analysis_queries.sql
│   └── cricintel.db
├── src/
│   └── build_dataset.py
├── .gitignore
└── README.md
```

## Running the Data Pipeline

Install the Python dependencies:

```bash
pip install pandas
```

Place the IPL JSON match files inside `data/raw/`.

From the project root, run:

```bash
python src/build_dataset.py
```

The script generates:

- `data/processed/ipl_deliveries.csv`
- `sql/cricintel.db`

Open `dashboards/cricintel.pbix` in Power BI Desktop to explore the dashboards.

## Analytical Considerations

- Strike rate is calculated as batter runs divided by balls faced, multiplied by 100.
- Wides are excluded from batter balls faced.
- Batting phases are Powerplay (overs 1–6), Middle (7–15) and Death (16–20).
- Wicket events include dismissals such as run-outs and are not equivalent to bowler-credited wickets.
- Minimum balls-faced thresholds are used for selected specialist rankings to reduce misleading small-sample comparisons.
- Historical franchise names are retained as represented in the source data.

## Future Enhancements

- Advanced player selection and comparison tools
- Predictive analytics and machine-learning models
- A cricket scorecard application with personalized team analytics

## Author

Maheshwar Siva M  
B.Tech — Artificial Intelligence and Data Science

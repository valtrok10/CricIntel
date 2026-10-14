-- 1. Top career run scorers

SELECT
    batter,
    SUM(batter_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;


-- 2. Phase-wise batter performance

SELECT
    batter,
    phase,
    SUM(batter_runs) AS runs,
    SUM(ball_faced) AS balls,
    ROUND(
        100.0 * SUM(batter_runs) /
        NULLIF(SUM(ball_faced), 0),
        2
    ) AS strike_rate
FROM deliveries
GROUP BY batter, phase
HAVING SUM(ball_faced) >= 100
ORDER BY strike_rate DESC;


-- 3. Death-over specialists

SELECT
    batter,
    SUM(batter_runs) AS death_runs,
    SUM(ball_faced) AS balls,
    ROUND(
        100.0 * SUM(batter_runs) /
        NULLIF(SUM(ball_faced), 0),
        2
    ) AS strike_rate,
    SUM(is_boundary) AS boundaries,
    ROUND(
        100.0 * SUM(is_boundary) /
        NULLIF(SUM(ball_faced), 0),
        2
    ) AS boundary_pct
FROM deliveries
WHERE phase = 'Death'
GROUP BY batter
HAVING SUM(ball_faced) >= 300
ORDER BY strike_rate DESC
LIMIT 15;


-- 4. Batter-bowler matchups

SELECT
    batter,
    bowler,
    SUM(batter_runs) AS runs,
    SUM(ball_faced) AS balls,
    ROUND(
        100.0 * SUM(batter_runs) /
        NULLIF(SUM(ball_faced), 0),
        2
    ) AS strike_rate,
    SUM(is_boundary) AS boundaries
FROM deliveries
GROUP BY batter, bowler
HAVING SUM(ball_faced) >= 30
ORDER BY runs DESC;


-- 5. Team phase performance

SELECT
    batting_team,
    phase,
    SUM(total_runs) AS runs,
    SUM(is_legal_delivery) AS legal_balls,
    ROUND(
        100.0 * SUM(total_runs) /
        NULLIF(SUM(is_legal_delivery), 0),
        2
    ) AS scoring_rate,
    SUM(is_boundary) AS boundaries,
    SUM(is_wicket) AS wicket_events
FROM deliveries
GROUP BY batting_team, phase
ORDER BY batting_team, phase;   
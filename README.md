# 2025 NFL Season Analysis

An exploratory analysis of how NFL offensive and defensive team metrics relate to point differential. This Python project joins team statistics, compares correlations, fits a two-predictor ordinary least squares (OLS) regression, and checks multicollinearity using variance inflation factors (VIF).

## Question

How are offensive expected points and defensive scoring percentage allowed associated with team point differential in the 2025 NFL season?

## Data

Source: [Pro Football Reference](https://www.pro-football-reference.com/).

- [2025 NFL standings and team statistics](https://www.pro-football-reference.com/years/2025/)
- [2025 NFL opposition and defensive statistics](https://www.pro-football-reference.com/years/2025/opp.htm)

The analysis uses two prepared, comma-separated input files, `data/Offense` and `data/Defense`, with descriptive column names used by the script. These filenames currently have no `.csv` extension. An unmodified source export may need its columns renamed to match the script.

Teams are joined on `Tm`, and point differential is calculated as `PF - PA`. The reported model contains 32 team observations. Coefficients refer to the units in the prepared input files; totals and per-game averages should not be mixed when interpreting or extending the analysis.

## Method

1. Load offensive and defensive data using paths relative to the script.
2. Join the tables by team, requiring unique team keys in each input.
3. Calculate point differential and Pearson correlations for 14 candidate metrics.
4. Fit an OLS model with an intercept and two selected predictors: `Off_Expected_Points` and `Def_Scoring_Percentage_Allowed`.
5. Calculate predictor VIF values using the model matrix, including the intercept.

The script fits a fixed predictor specification; it does not perform automated feature selection or validation on unseen data.

## Results

Results from the supplied run:

| Measure | Value |
| --- | ---: |
| Team observations | 32 |
| R-squared | 0.950 |
| Adjusted R-squared | 0.947 |
| Offensive expected points coefficient | 0.7594 |
| Defensive scoring percentage allowed coefficient | -0.6851 |
| Intercept | 24.5349 |
| VIF for each predictor | 1.0162 |

The model accounts for approximately 95% of the observed variation in point differential in this sample. Holding the other predictor constant, offensive expected points has a positive association with point differential, while defensive scoring percentage allowed has a negative association. The predictor VIF values are close to 1.

Among the candidate metrics, offensive net yards per attempt has the largest positive correlation with point differential (0.799), and defensive scoring percentage allowed has the most negative correlation (-0.718).

## Run locally

Use Python and install the dependencies listed in `requirements.txt`. From the project root, a Windows PowerShell setup is:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe pycode/OLSFootball.py
```

If the environment is already set up, run only the last command. The script prints the correlation ranking, regression summary, and VIF table.

Expected project files:

| Path | Purpose |
| --- | --- |
| `pycode/OLSFootball.py` | Analysis script |
| `data/Offense` | Prepared offensive team statistics |
| `data/Defense` | Prepared defensive team statistics |
| `requirements.txt` | Package versions |
| `.gitignore` | Excludes local environment and editor files |
| `README.md` | Project overview and instructions |

## Interpretation and limitations

- This is a descriptive analysis of one season and 32 teams. The reported R-squared measures fit on the same data used to estimate the model.
- The predictors and point differential describe the same season, and scoring-related measures are closely related to the outcome. The strong fit does not establish an ability to forecast future games or seasons.
- Associations do not establish causal effects.
- Low VIF values address predictor collinearity; they do not verify all regression assumptions. Further work could inspect residuals and influential teams, account for schedule strength, and evaluate a prespecified model on additional seasons.

## Tools

Python, pandas, statsmodels, and pathlib.

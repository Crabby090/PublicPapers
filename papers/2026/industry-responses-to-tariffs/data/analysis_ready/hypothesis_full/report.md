# Full Hypothesis Test (Exploratory)

Hypothesis: Industries with more Democratic-leaning workforces show more pronounced trade responses to tariffs.

## Data
- Imports: Census NAICS (6-digit aggregated to NAICS-3)
- Exports: Census NAICS (3-digit)
- Partisanship proxy: employment-weighted Dem vote share by NAICS-3 (CBP county employment + MIT Election Lab returns)

## Methods
1) Cross-sectional change tests: pre vs post windows with Pearson/Spearman correlations, quartile contrasts, OLS/WLS.
2) Panel FE: log trade value on dem_share × post with industry and month FE (clustered SEs).
3) Event study: dem_share × year interactions with industry/year/month FE.

Outputs:
- `cross_section_changes.csv`
- `cross_section_summary.csv`
- `cross_section_regressions.csv`
- `panel_post_effects.csv`
- `event_study_year_interactions.csv`

## Interpretation guidance
- Cross-sectional results are sensitive to window selection and small N.
- Panel results help control for time-invariant industry differences and common shocks, but do not isolate tariff exposure.
- Event-study interactions show whether dem-leaning industries trend differently over time.

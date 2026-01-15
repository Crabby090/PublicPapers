# Hypothesis Test (Exploratory)

Hypothesis: Industries with more Democratic-leaning workforces show more pronounced trade responses to tariffs.

## Method (quick test)
- Constructed NAICS-3 industry trade changes using Census imports and exports data.
- Pre-period: 2016-2017 average; Post-period: 2019 average.
- Response metric: absolute log change in average monthly trade value (and absolute percent change).
- Partisanship proxy: employment-weighted Democratic vote share (2016+2020) by NAICS-3.

## Key outputs
- `hypothesis_trade_changes.csv` (industry-level changes)
- `hypothesis_test_summary.csv` (correlations + quartile means)
- `hypothesis_test_regression.csv` (OLS of abs log change on dem_share)

## Notes
- This is an exploratory correlation test; not causal.
- Results are sensitive to period selection and to using 3-digit NAICS for exports.

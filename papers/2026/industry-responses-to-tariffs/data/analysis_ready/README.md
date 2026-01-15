# Analysis-Ready Quant Data

This folder contains consolidated, cleaned datasets derived from `data/processed/` for quantitative analysis.

## Files
- `quantgov_section301_lists_clean.csv.gz`
- `quantgov_section301_exclusion_requests_clean.csv.gz`
- `quantgov_section232_microdata_clean.csv.gz` (v1 + v3 combined)
- `bis232_exclusion_requests_clean.csv.gz` (main BIS exclusion requests only)
- `usitc_hts_clean.csv.gz`
- `usitc_hts_codes_only.csv.gz` (HTS rows only)
- `census_imports_naics_clean.csv.gz`
- `census_exports_naics_3digit_clean.csv.gz`
- `census_trade_enduse_clean.csv.gz`
- `qa_summary.csv` (row/column counts and key duplication checks)

## Conventions
- Columns are snake_case.
- HTS codes are digit-only strings; `hts_6`, `hts_8`, `hts_10` are prefixes.
- Date columns are ISO `YYYY-MM-DD` strings.
- Monetary/quantity fields are numeric where applicable.

## Partisanship proxy
- `county_partisanship_2016_2020.csv`
- `industry_partisanship_naics3.csv`

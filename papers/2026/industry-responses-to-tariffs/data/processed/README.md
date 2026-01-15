# Processed Data

This folder contains standardized, analysis-ready CSVs derived from the raw downloads in `data/raw`. Sources and access dates are documented in `papers/2026/industry-responses-to-tariffs/sources.md`.

## Processed datasets

### QuantGov (tariffs and exclusions)
- `quantgov/quantgov_section301_lists.csv.gz` - Combined Section 301 tariff lists (Lists 1-4) with HTS, BEC codes, and import values where provided. [55]
- `quantgov/quantgov_section301_exclusion_requests.csv.gz` - Combined Section 301 exclusion request data (Lists 1-4A). [55]
- `quantgov/quantgov_section232_v1_microdata.csv.gz` - Section 232 exclusion microdata (steel/aluminum, with/without objections), v1 portal extracts. [55]
- `quantgov/quantgov_section232_v3_merged.csv.gz` - Section 232 merged steel/aluminum dataset (v3 portal). [55]

### BIS Section 232 public extract
- `bis232/bis232_*.csv.gz` - One file per BIS public-extract table (exclusion requests, objections, rebuttals, and component tables). [56]
- `bis232/bis232_manifest.csv` - Table-level manifest with row counts and ID columns.

### USITC HTS schedules
- `usitc/usitc_hts_2019_rev20.csv.gz` - Harmonized Tariff Schedule 2019 Rev. 20. [57]
- `usitc/usitc_hts_2020_rev18.csv.gz` - Harmonized Tariff Schedule 2020 Rev. 18. [58]
- `usitc/usitc_hts_2019_2020_combined.csv.gz` - Combined 2019+2020 HTS with `year` column. [57][58]

### Census trade time series
- `census/census_imports_naics_2016_2024.csv.gz` - Imports by NAICS time series with standardized columns. [59]
- `census/census_trade_enduse_2016_2024.csv.gz` - Imports+exports by end-use (combined) with standardized columns. [60][61]

## Processing conventions
- Columns are normalized to snake_case.
- HTS/NAICS codes are stored as strings to preserve leading zeros.
- Census `time` is preserved and expanded into `year`, `month`, and `date` (`YYYY-MM-01`).

## Regeneration
Run `data/prepare_quant_data.py` from the repository root to rebuild processed files.

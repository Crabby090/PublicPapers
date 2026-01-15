# QA Report - Analysis-Ready Quant Data

Generated from `data/consolidate_quant_data.py` using the consolidated datasets in `data/analysis_ready/`.

## Summary
- All analysis-ready files were generated successfully.
- Key columns are populated for all datasets except `usitc_hts_clean`, which includes hierarchy rows without HTS codes (use `usitc_hts_codes_only.csv.gz` for code-level analysis).
- Section 232 microdata contains repeated IDs (multiple lines per request); this is expected for line-item level data.

## Notable checks
- `quantgov_section301_lists_clean`: no missing `list_id`/`hts` keys.
- `quantgov_section301_exclusion_requests_clean`: no missing `id` keys.
- `quantgov_section232_microdata_clean`: duplicates for `id|metal|version|source` are expected (multi-line request entries).
- `bis232_exclusion_requests_clean`: minimal duplicates on `erid`.
- `usitc_hts_codes_only`: no missing `year|hts_number` keys.
- Census trade series: no missing keys for `category_code|date` (imports NAICS) or `flow|category_code|date` (end-use).

See `qa_summary.csv` for row/column counts and key duplication metrics.

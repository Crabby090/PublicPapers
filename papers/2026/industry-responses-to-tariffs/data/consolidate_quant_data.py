import pandas as pd
import numpy as np
from pathlib import Path
import re
import csv
import gzip

base = Path(r"papers\2026\industry-responses-to-tariffs\data")
raw = base / "raw"
processed = base / "processed"
analysis = base / "analysis_ready"
analysis.mkdir(parents=True, exist_ok=True)


def snake(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[^0-9a-zA-Z]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s.lower()


def clean_hts(series: pd.Series) -> pd.Series:
    s = series.astype(str).str.replace(r"\D", "", regex=True)
    s = s.replace("", pd.NA)
    return s


def add_hts_cols(df: pd.DataFrame, col: str = "hts") -> pd.DataFrame:
    if col not in df.columns:
        return df
    digits = clean_hts(df[col])
    df["hts"] = digits
    df["hts_6"] = digits.str[:6]
    df["hts_8"] = digits.str[:8]
    df["hts_10"] = digits.str[:10]
    return df


def to_iso_date(series: pd.Series) -> pd.Series:
    dt = pd.to_datetime(series, errors="coerce")
    return dt.dt.date.astype("string")


def to_numeric(series: pd.Series) -> pd.Series:
    if series is None:
        return series
    cleaned = series.astype(str).str.replace(",", "", regex=False)
    return pd.to_numeric(cleaned, errors="coerce")


def write_csv_gz(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, compression="gzip")


def fix_spaced_letters(col: str) -> str:
    # convert e_r_i_d -> erid
    if re.match(r"^[a-z](?:_[a-z])+$", col):
        return col.replace("_", "")
    return col


qa_rows = []

# ---- QuantGov Section 301 lists ----
qg_301_lists = pd.read_csv(processed / "quantgov" / "quantgov_section301_lists.csv.gz", dtype=str)
qg_301_lists = add_hts_cols(qg_301_lists, "hts")
for col in [
    "imports_2015",
    "imports_2016",
    "imports_2017",
    "imports_2018",
    "imports_2019_jan_apr",
    "imports_2015_2017_avg",
]:
    if col in qg_301_lists.columns:
        qg_301_lists[col] = to_numeric(qg_301_lists[col])

qg_301_lists_out = qg_301_lists[[
    c for c in [
        "list_id",
        "hts",
        "hts_6",
        "hts_8",
        "hts_10",
        "bec_code",
        "bec_description",
        "imports_2015",
        "imports_2016",
        "imports_2017",
        "imports_2018",
        "imports_2019_jan_apr",
        "imports_2015_2017_avg",
        "source_file",
    ] if c in qg_301_lists.columns
]]
write_csv_gz(qg_301_lists_out, analysis / "quantgov_section301_lists_clean.csv.gz")

qa_rows.append({
    "dataset": "quantgov_section301_lists_clean",
    "rows": len(qg_301_lists_out),
    "columns": len(qg_301_lists_out.columns),
    "key_columns": "list_id|hts",
    "missing_key_rows": int(qg_301_lists_out[["list_id", "hts"]].isna().any(axis=1).sum()),
    "duplicate_key_rows": int(qg_301_lists_out.duplicated(subset=["list_id", "hts"]).sum()),
})

# ---- QuantGov Section 301 exclusion requests ----
qg_301_excl = pd.read_csv(processed / "quantgov" / "quantgov_section301_exclusion_requests.csv.gz", dtype=str)
qg_301_excl = add_hts_cols(qg_301_excl, "hts")

# normalize column names
rename_map = {
    "posteddate": "posted_date",
    "receiveddate": "received_date",
    "responseclosed": "response_closed",
    "beccode": "bec_code",
    "becdescription": "bec_description",
    "bec_description": "bec_description",
}
qg_301_excl = qg_301_excl.rename(columns={k: v for k, v in rename_map.items() if k in qg_301_excl.columns})

for col in ["posted_date", "received_date", "response_closed"]:
    if col in qg_301_excl.columns:
        qg_301_excl[col] = to_iso_date(qg_301_excl[col])

qg_301_excl_out = qg_301_excl[[
    c for c in [
        "id",
        "list_id",
        "hts",
        "hts_6",
        "hts_8",
        "hts_10",
        "bec_code",
        "bec_description",
        "company_name",
        "producttitle",
        "approved",
        "denied",
        "pending",
        "posted_date",
        "received_date",
        "response_closed",
        "source_file",
    ] if c in qg_301_excl.columns
]]
write_csv_gz(qg_301_excl_out, analysis / "quantgov_section301_exclusion_requests_clean.csv.gz")

qa_rows.append({
    "dataset": "quantgov_section301_exclusion_requests_clean",
    "rows": len(qg_301_excl_out),
    "columns": len(qg_301_excl_out.columns),
    "key_columns": "id",
    "missing_key_rows": int(qg_301_excl_out["id"].isna().sum()),
    "duplicate_key_rows": int(qg_301_excl_out.duplicated(subset=["id"]).sum()),
})

# ---- QuantGov Section 232 microdata (v1 + v3) ----
qg_232_v1 = pd.read_csv(processed / "quantgov" / "quantgov_section232_v1_microdata.csv.gz", dtype=str)
qg_232_v3 = pd.read_csv(processed / "quantgov" / "quantgov_section232_v3_merged.csv.gz", dtype=str)

for df in [qg_232_v1, qg_232_v3]:
    df = add_hts_cols(df, "hts")

qg_232_v1 = add_hts_cols(qg_232_v1, "hts")
qg_232_v3 = add_hts_cols(qg_232_v3, "hts")

qg_232_v1["source"] = "quantgov_v1"
qg_232_v3["source"] = "quantgov_v3"

# parse numeric columns
num_cols = [c for c in qg_232_v1.columns if re.match(r"^(percent|total_amount|quantity_\d+)$", c)]
for col in num_cols:
    qg_232_v1[col] = to_numeric(qg_232_v1[col])

num_cols = [c for c in qg_232_v3.columns if re.match(r"^(percent|total_amount|quantity_\d+)$", c)]
for col in num_cols:
    qg_232_v3[col] = to_numeric(qg_232_v3[col])

if "received_date" in qg_232_v3.columns:
    qg_232_v3["received_date"] = to_iso_date(qg_232_v3["received_date"])

qg_232 = pd.concat([qg_232_v1, qg_232_v3], ignore_index=True, sort=False)
write_csv_gz(qg_232, analysis / "quantgov_section232_microdata_clean.csv.gz")

qa_rows.append({
    "dataset": "quantgov_section232_microdata_clean",
    "rows": len(qg_232),
    "columns": len(qg_232.columns),
    "key_columns": "id|metal|version|source",
    "missing_key_rows": int(qg_232[[c for c in ["id", "metal", "version", "source"] if c in qg_232.columns]].isna().any(axis=1).sum()),
    "duplicate_key_rows": int(qg_232.duplicated(subset=[c for c in ["id", "metal", "version", "source"] if c in qg_232.columns]).sum()),
})

# ---- BIS Section 232 exclusion requests ----
# Only clean the main ExclusionRequests table for analysis
bis_raw = raw / "bis232" / "public_extract" / "ExclusionRequests.txt"
# Raw files are UTF-16 LE; use python engine to tolerate irregular rows
bis_excl = pd.read_csv(
    bis_raw,
    dtype=str,
    encoding="utf-16",
    engine="python",
    on_bad_lines="skip",
)
# Normalize column names
bis_excl.columns = [snake(c) for c in bis_excl.columns]

# Standardize date columns
for col in ["publishdate", "created"]:
    if col in bis_excl.columns:
        bis_excl[col] = to_iso_date(bis_excl[col])

# Clean HTS
if "htsuscode" in bis_excl.columns:
    bis_excl = add_hts_cols(bis_excl, "htsuscode")

# Numeric quantity
if "totalrequestedannualexclusionquantity" in bis_excl.columns:
    bis_excl["totalrequestedannualexclusionquantity"] = to_numeric(bis_excl["totalrequestedannualexclusionquantity"])

bis_keep_cols = [
    "erid",
    "publishdate",
    "created",
    "publicstatus",
    "htsuscode",
    "hts",
    "hts_6",
    "hts_8",
    "hts_10",
    "metalclass",
    "requestingorg_orglegalname",
    "requestingorg_state",
    "requestingorg_headquarterscountry",
    "requestingimporter_orglegalname",
    "requestingimporter_state",
    "requestingimporter_headquarterscountry",
    "nonusproducer_headquarterscountry",
    "totalrequestedannualexclusionquantity",
]

bis_excl_out = bis_excl[[c for c in bis_keep_cols if c in bis_excl.columns]]
write_csv_gz(bis_excl_out, analysis / "bis232_exclusion_requests_clean.csv.gz")

qa_rows.append({
    "dataset": "bis232_exclusion_requests_clean",
    "rows": len(bis_excl_out),
    "columns": len(bis_excl_out.columns),
    "key_columns": "erid",
    "missing_key_rows": int(bis_excl_out["erid"].isna().sum()) if "erid" in bis_excl_out.columns else len(bis_excl_out),
    "duplicate_key_rows": int(bis_excl_out.duplicated(subset=["erid"]).sum()) if "erid" in bis_excl_out.columns else 0,
})

# ---- USITC HTS ----
hts = pd.read_csv(processed / "usitc" / "usitc_hts_2019_2020_combined.csv.gz", dtype=str)
# Clean HTS number
if "hts_number" in hts.columns:
    hts = add_hts_cols(hts, "hts_number")

# Parse rates (best-effort)
rate_cols = {
    "general_rate_of_duty": "general_rate_advalorem",
    "special_rate_of_duty": "special_rate_advalorem",
    "column_2_rate_of_duty": "column2_rate_advalorem",
}

for src, dst in rate_cols.items():
    if src in hts.columns:
        def parse_rate(val):
            if pd.isna(val):
                return np.nan
            v = str(val).strip().lower()
            if v.startswith("free"):
                return 0.0
            m = re.search(r"(\d+(?:\.\d+)?)", v)
            if m:
                return float(m.group(1))
            return np.nan
        hts[dst] = hts[src].apply(parse_rate)

hts_out = hts[[
    c for c in [
        "year",
        "hts_number",
        "hts",
        "hts_6",
        "hts_8",
        "hts_10",
        "indent",
        "description",
        "unit_of_quantity",
        "general_rate_of_duty",
        "special_rate_of_duty",
        "column_2_rate_of_duty",
        "general_rate_advalorem",
        "special_rate_advalorem",
        "column2_rate_advalorem",
        "additional_duties",
    ] if c in hts.columns
]]
write_csv_gz(hts_out, analysis / "usitc_hts_clean.csv.gz")

# Codes-only subset (non-null HTS numbers)
hts_codes = hts_out[hts_out["hts_number"].notna()].copy() if "hts_number" in hts_out.columns else hts_out.copy()
write_csv_gz(hts_codes, analysis / "usitc_hts_codes_only.csv.gz")

qa_rows.append({
    "dataset": "usitc_hts_clean",
    "rows": len(hts_out),
    "columns": len(hts_out.columns),
    "key_columns": "year|hts_number",
    "missing_key_rows": int(hts_out[[c for c in ["year", "hts_number"] if c in hts_out.columns]].isna().any(axis=1).sum()),
    "duplicate_key_rows": int(hts_out.duplicated(subset=[c for c in ["year", "hts_number"] if c in hts_out.columns]).sum()),
})

qa_rows.append({
    "dataset": "usitc_hts_codes_only",
    "rows": len(hts_codes),
    "columns": len(hts_codes.columns),
    "key_columns": "year|hts_number",
    "missing_key_rows": 0,
    "duplicate_key_rows": int(hts_codes.duplicated(subset=[c for c in ["year", "hts_number"] if c in hts_codes.columns]).sum()),
})

# ---- Census trade ----
imports_naics = pd.read_csv(processed / "census" / "census_imports_naics_2016_2024.csv.gz", dtype=str)
imports_naics["value_mo"] = to_numeric(imports_naics["value_mo"])
for col in ["year", "month"]:
    if col in imports_naics.columns:
        imports_naics[col] = pd.to_numeric(imports_naics[col], errors="coerce")
imports_naics_out = imports_naics[[
    c for c in [
        "flow",
        "dimension",
        "category_code",
        "category_desc",
        "time",
        "year",
        "month",
        "date",
        "value_mo",
    ] if c in imports_naics.columns
]]
write_csv_gz(imports_naics_out, analysis / "census_imports_naics_clean.csv.gz")

# Exports NAICS (3-digit)
exports_naics_raw = raw / "census" / "census_exports_naics_3digit_2016_2024.csv"
if exports_naics_raw.exists():
    exports_naics = pd.read_csv(exports_naics_raw, dtype=str)
    exports_naics.columns = [snake(c) for c in exports_naics.columns]
    time_col = exports_naics["time"].astype(str)
    exports_naics["year"] = time_col.str.slice(0, 4)
    exports_naics["month"] = time_col.str.slice(5, 7)
    exports_naics["date"] = time_col + "-01"
    exports_naics["flow"] = "exports"
    exports_naics["dimension"] = "naics"
    exports_naics = exports_naics.rename(columns={
        "naics_ldesc": "category_desc",
        "naics": "category_code",
        "all_val_mo": "value_mo",
    })
    exports_naics["value_mo"] = to_numeric(exports_naics["value_mo"])
    for col in ["year", "month"]:
        if col in exports_naics.columns:
            exports_naics[col] = pd.to_numeric(exports_naics[col], errors="coerce")
    exports_naics_out = exports_naics[[
        c for c in [
            "flow",
            "dimension",
            "category_code",
            "category_desc",
            "time",
            "year",
            "month",
            "date",
            "value_mo",
        ] if c in exports_naics.columns
    ]]
    write_csv_gz(exports_naics_out, analysis / "census_exports_naics_3digit_clean.csv.gz")

write_csv_gz(imports_naics_out, analysis / "census_imports_naics_clean.csv.gz")

qa_rows.append({
    "dataset": "census_imports_naics_clean",
    "rows": len(imports_naics_out),
    "columns": len(imports_naics_out.columns),
    "key_columns": "category_code|date",
    "missing_key_rows": int(imports_naics_out[["category_code", "date"]].isna().any(axis=1).sum()),
    "duplicate_key_rows": int(imports_naics_out.duplicated(subset=["category_code", "date"]).sum()),
})

if 'exports_naics_out' in locals():
    qa_rows.append({
        "dataset": "census_exports_naics_3digit_clean",
        "rows": len(exports_naics_out),
        "columns": len(exports_naics_out.columns),
        "key_columns": "category_code|date",
        "missing_key_rows": int(exports_naics_out[["category_code", "date"]].isna().any(axis=1).sum()),
        "duplicate_key_rows": int(exports_naics_out.duplicated(subset=["category_code", "date"]).sum()),
    })

enduse = pd.read_csv(processed / "census" / "census_trade_enduse_2016_2024.csv.gz", dtype=str)
enduse["value_mo"] = to_numeric(enduse["value_mo"])
for col in ["year", "month"]:
    if col in enduse.columns:
        enduse[col] = pd.to_numeric(enduse[col], errors="coerce")
enduse_out = enduse[[
    c for c in [
        "flow",
        "dimension",
        "category_code",
        "category_desc",
        "time",
        "year",
        "month",
        "date",
        "value_mo",
    ] if c in enduse.columns
]]
write_csv_gz(enduse_out, analysis / "census_trade_enduse_clean.csv.gz")

qa_rows.append({
    "dataset": "census_trade_enduse_clean",
    "rows": len(enduse_out),
    "columns": len(enduse_out.columns),
    "key_columns": "flow|category_code|date",
    "missing_key_rows": int(enduse_out[["flow", "category_code", "date"]].isna().any(axis=1).sum()),
    "duplicate_key_rows": int(enduse_out.duplicated(subset=["flow", "category_code", "date"]).sum()),
})

# ---- QA Summary ----
qa = pd.DataFrame(qa_rows)
qa.to_csv(analysis / "qa_summary.csv", index=False)

# ---- README ----
readme = """# Analysis-Ready Quant Data

This folder contains consolidated, cleaned datasets derived from `data/processed/` for quantitative analysis.

## Files
- `quantgov_section301_lists_clean.csv.gz`
- `quantgov_section301_exclusion_requests_clean.csv.gz`
- `quantgov_section232_microdata_clean.csv.gz` (v1 + v3 combined)
- `bis232_exclusion_requests_clean.csv.gz` (main BIS exclusion requests only)
- `usitc_hts_clean.csv.gz`
- `usitc_hts_codes_only.csv.gz` (HTS rows only)
- `census_imports_naics_clean.csv.gz`
- `census_trade_enduse_clean.csv.gz`
- `qa_summary.csv` (row/column counts and key duplication checks)

## Conventions
- Columns are snake_case.
- HTS codes are digit-only strings; `hts_6`, `hts_8`, `hts_10` are prefixes.
- Date columns are ISO `YYYY-MM-DD` strings.
- Monetary/quantity fields are numeric where applicable.
"""
(analysis / "README.md").write_text(readme, encoding="utf-8")

print("done")

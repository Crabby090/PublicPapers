from pathlib import Path
import re
import csv
import gzip
import pandas as pd

base = Path(r"papers\2026\industry-responses-to-tariffs\data")
raw = base / "raw"
processed = base / "processed"
processed.mkdir(parents=True, exist_ok=True)


def snake(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[^0-9a-zA-Z]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s.lower()


def write_csv_gz(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, compression="gzip")


# ---- QuantGov Section 301 lists ----
section301_dir = raw / "quantgov" / "section301_v1" / "Tariffs-Section-301_1-0"
list_files = [
    ("final-1.xls", "1"),
    ("final-2.xls", "2"),
    ("final-3.xls", "3"),
    ("final-4.xlsx", "4"),
]

list_frames = []
for fname, list_id in list_files:
    fpath = section301_dir / fname
    df = pd.read_excel(fpath, dtype=str)
    df.columns = [snake(c) for c in df.columns]
    df["list_id"] = list_id
    df["source_file"] = fname
    list_frames.append(df)

section301_lists = pd.concat(list_frames, ignore_index=True, sort=False)
rename_map = {
    "hts": "hts",
    "hts_six_digit": "hts_six_digit",
    "bec_code": "bec_code",
    "bec_description": "bec_description",
    "2015_imports_for_consumption": "imports_2015",
    "2016_imports_for_consumption": "imports_2016",
    "2017_imports_for_consumption": "imports_2017",
    "2018_imports_for_consumption": "imports_2018",
    "january_through_april_2019_imports_for_consumption": "imports_2019_jan_apr",
    "average_imports_for_2015_2016_and_2017": "imports_2015_2017_avg",
}
section301_lists = section301_lists.rename(columns=rename_map)
write_csv_gz(section301_lists, processed / "quantgov" / "quantgov_section301_lists.csv.gz")

# ---- QuantGov Section 301 exclusion requests ----
excl_files = [
    ("List-1-Exclusion-Requests (Nov 2021).xlsx", "1"),
    ("List-2-Exclusion-Requests (Nov 2021).xlsx", "2"),
    ("List-3-Exclusion-Requests (Nov 2021).xlsx", "3"),
    ("List-4A-Exclusion-Requests (Nov 2021).xlsx", "4A"),
]

excl_frames = []
for fname, list_id in excl_files:
    fpath = section301_dir / fname
    df = pd.read_excel(fpath, dtype=str)
    df.columns = [snake(c) for c in df.columns]
    df = df.rename(columns={
        "htssixdigit": "hts_six_digit",
        "htsixdigit": "hts_six_digit",
        "becdesription": "bec_description",
        "company": "company_name",
        "companyname": "company_name",
    })
    df["list_id"] = list_id
    df["source_file"] = fname
    excl_frames.append(df)

section301_excl = pd.concat(excl_frames, ignore_index=True, sort=False)
write_csv_gz(section301_excl, processed / "quantgov" / "quantgov_section301_exclusion_requests.csv.gz")

# ---- QuantGov Section 232 v1 microdata ----
section232_v1_dir = raw / "quantgov" / "section232_v1"
section232_v1_files = [
    ("Steel-Microdata-June-17-rev.xlsx", "steel", False),
    ("Steel-Microdata-with-Objections-June-17-rev.xlsx", "steel", True),
    ("Copy of Aluminum-Microdata-June-17-rev.xlsx", "aluminum", False),
    ("Copy of Aluminum-Microdata-with-objections-June-17-rev.xlsx", "aluminum", True),
]

v1_frames = []
for fname, metal, with_obj in section232_v1_files:
    fpath = section232_v1_dir / fname
    df = pd.read_excel(fpath, dtype=str)
    df.columns = [snake(c) for c in df.columns]
    df["metal"] = metal
    df["with_objections"] = "true" if with_obj else "false"
    df["version"] = "v1"
    df["source_file"] = fname
    v1_frames.append(df)

section232_v1 = pd.concat(v1_frames, ignore_index=True, sort=False)
write_csv_gz(section232_v1, processed / "quantgov" / "quantgov_section232_v1_microdata.csv.gz")

# ---- QuantGov Section 232 v3 merged ----
section232_v3_dir = raw / "quantgov" / "section232_v3"

steel_v3 = pd.read_csv(section232_v3_dir / "merged_steel_final.csv", dtype=str, low_memory=False)
steel_v3.columns = [snake(c) for c in steel_v3.columns]
steel_v3["metal"] = "steel"
steel_v3["version"] = "v3"
steel_v3["source_file"] = "merged_steel_final.csv"

al_v3 = pd.read_excel(section232_v3_dir / "merged_aluminum_final.xlsx", dtype=str)
al_v3.columns = [snake(c) for c in al_v3.columns]
al_v3["metal"] = "aluminum"
al_v3["version"] = "v3"
al_v3["source_file"] = "merged_aluminum_final.xlsx"

section232_v3 = pd.concat([steel_v3, al_v3], ignore_index=True, sort=False)
write_csv_gz(section232_v3, processed / "quantgov" / "quantgov_section232_v3_merged.csv.gz")

# ---- BIS Section 232 public extract ----

def read_bis_txt(path: Path) -> pd.DataFrame:
    # Try utf-8 with python engine; fall back to latin-1
    try:
        return pd.read_csv(
            path,
            dtype=str,
            engine="python",
            quoting=csv.QUOTE_MINIMAL,
            on_bad_lines="skip",
        )
    except Exception:
        return pd.read_csv(
            path,
            dtype=str,
            engine="python",
            quoting=csv.QUOTE_MINIMAL,
            on_bad_lines="skip",
            encoding="latin-1",
        )


def count_lines(path: Path) -> int:
    with open(path, "rb") as f:
        return sum(1 for _ in f)

bis_dir = raw / "bis232" / "public_extract"
bis_out = processed / "bis232"
bis_out.mkdir(parents=True, exist_ok=True)

bis_manifest_rows = []
for txt in sorted(bis_dir.glob("*.txt")):
    df = read_bis_txt(txt)
    df.columns = [snake(c) for c in df.columns]
    out_name = f"bis232_{txt.stem.lower()}.csv.gz"
    out_path = bis_out / out_name
    write_csv_gz(df, out_path)
    id_cols = [c for c in df.columns if c.endswith("id") or c.endswith("_id")]
    raw_lines = count_lines(txt)
    bis_manifest_rows.append({
        "table": txt.stem,
        "raw_lines": raw_lines,
        "rows": len(df),
        "columns": len(df.columns),
        "id_columns": "|".join(id_cols),
        "output_file": str(out_path.relative_to(base))
    })

pd.DataFrame(bis_manifest_rows).to_csv(bis_out / "bis232_manifest.csv", index=False)

# ---- USITC HTS ----
hts_2019 = pd.read_csv(raw / "usitc" / "usitc_hts_2019_rev20.csv", dtype=str)
hts_2020 = pd.read_csv(raw / "usitc" / "usitc_hts_2020_rev18.csv", dtype=str)

for df in [hts_2019, hts_2020]:
    df.columns = [snake(c) for c in df.columns]

hts_2019["year"] = "2019"
hts_2020["year"] = "2020"

write_csv_gz(hts_2019, processed / "usitc" / "usitc_hts_2019_rev20.csv.gz")
write_csv_gz(hts_2020, processed / "usitc" / "usitc_hts_2020_rev18.csv.gz")

hts_combined = pd.concat([hts_2019, hts_2020], ignore_index=True, sort=False)
write_csv_gz(hts_combined, processed / "usitc" / "usitc_hts_2019_2020_combined.csv.gz")

# ---- Census trade time series ----

def parse_time(df: pd.DataFrame) -> pd.DataFrame:
    time_col = df["time"].astype(str)
    df["year"] = time_col.str.slice(0, 4)
    df["month"] = time_col.str.slice(5, 7)
    df["date"] = time_col + "-01"
    return df

imports_naics = pd.read_csv(raw / "census" / "census_imports_naics_2016_2024.csv", dtype=str)
imports_naics.columns = [snake(c) for c in imports_naics.columns]
imports_naics = parse_time(imports_naics)
imports_naics["flow"] = "imports"
imports_naics["dimension"] = "naics"
imports_naics = imports_naics.rename(columns={
    "naics_ldesc": "category_desc",
    "naics": "category_code",
    "gen_val_mo": "value_mo",
})
write_csv_gz(imports_naics, processed / "census" / "census_imports_naics_2016_2024.csv.gz")

imports_enduse = pd.read_csv(raw / "census" / "census_imports_enduse_2016_2024.csv", dtype=str)
imports_enduse.columns = [snake(c) for c in imports_enduse.columns]
imports_enduse = parse_time(imports_enduse)
imports_enduse["flow"] = "imports"
imports_enduse["dimension"] = "enduse"
imports_enduse = imports_enduse.rename(columns={
    "i_enduse": "category_code",
    "i_enduse_ldesc": "category_desc",
    "gen_val_mo": "value_mo",
})

exports_enduse = pd.read_csv(raw / "census" / "census_exports_enduse_2016_2024.csv", dtype=str)
exports_enduse.columns = [snake(c) for c in exports_enduse.columns]
exports_enduse = parse_time(exports_enduse)
exports_enduse["flow"] = "exports"
exports_enduse["dimension"] = "enduse"
exports_enduse = exports_enduse.rename(columns={
    "e_enduse": "category_code",
    "e_enduse_ldesc": "category_desc",
    "all_val_mo": "value_mo",
})

enduse_combined = pd.concat([imports_enduse, exports_enduse], ignore_index=True, sort=False)
write_csv_gz(enduse_combined, processed / "census" / "census_trade_enduse_2016_2024.csv.gz")

# ---- Write dataset manifest (header + file size only) ----
manifest_rows = []
for path in sorted(processed.rglob("*.csv.gz")):
    rel = path.relative_to(base)
    with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
    manifest_rows.append({
        "file": str(rel),
        "columns": len(header),
        "size_bytes": path.stat().st_size
    })

pd.DataFrame(manifest_rows).to_csv(processed / "manifest.csv", index=False)

print("done")

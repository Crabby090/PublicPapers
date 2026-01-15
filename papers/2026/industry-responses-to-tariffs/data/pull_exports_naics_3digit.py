import time
import csv
import requests
import pandas as pd
from pathlib import Path

base = Path(r"papers\2026\industry-responses-to-tariffs\data")
raw = base / "raw" / "census"
raw.mkdir(parents=True, exist_ok=True)

# Use 3-digit NAICS codes from imports dataset as the target list
imports_path = base / "analysis_ready" / "census_imports_naics_clean.csv.gz"
imports = pd.read_csv(imports_path, usecols=["category_code"], dtype=str)
naics_codes = sorted({c for c in imports["category_code"].dropna().unique() if len(c) == 3})

url = "https://api.census.gov/data/timeseries/intltrade/exports/naics"

rows = []
header = None

session = requests.Session()

for i, code in enumerate(naics_codes, 1):
    params = {
        "get": "NAICS,NAICS_LDESC,ALL_VAL_MO",
        "time": "from 2016-01 to 2024-12",
        "NAICS": code,
    }
    try:
        resp = session.get(url, params=params, timeout=60)
        if resp.status_code != 200:
            print("skip", code, resp.status_code)
            continue
        data = resp.json()
        if not data or len(data) < 2:
            continue
        if header is None:
            header = data[0]
        rows.extend(data[1:])
    except Exception as e:
        print("error", code, e)
    # small pause to be polite
    if i % 10 == 0:
        time.sleep(0.5)

if header is None:
    raise SystemExit("No data fetched")

out = raw / "census_exports_naics_3digit_2016_2024.csv"
with open(out, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("saved", out, "rows", len(rows))

import pandas as pd
from pathlib import Path

base = Path(r"papers\2026\industry-responses-to-tariffs\data")
raw = base / "raw" / "partisanship"
analysis = base / "analysis_ready"
analysis.mkdir(parents=True, exist_ok=True)

# County presidential returns (MIT Election Lab)
countypres_path = raw / "countypres_2000_2024.tab"
cp = pd.read_csv(countypres_path, sep='\t', dtype=str)

cp = cp[cp["office"].str.contains("PRESIDENT", case=False, na=False) & (cp["mode"].str.upper() == "TOTAL")]
cp["county_fips"] = cp["county_fips"].str.zfill(5)
cp["candidatevotes"] = pd.to_numeric(cp["candidatevotes"], errors="coerce")

# Sum votes by county/year/party
cp_party = cp.groupby(["year", "county_fips", "party"], as_index=False)["candidatevotes"].sum()

# Keep DEM and REP
pivot = cp_party.pivot_table(index=["year", "county_fips"], columns="party", values="candidatevotes", fill_value=0).reset_index()

# Normalize column names
pivot.columns = [c.lower() if isinstance(c, str) else c for c in pivot.columns]

# Ensure dem/rep columns exist
for col in ["democrat", "republican"]:
    if col not in pivot.columns:
        pivot[col] = 0

pivot["two_party_total"] = pivot["democrat"] + pivot["republican"]
pivot["dem_share"] = (pivot["democrat"] / pivot["two_party_total"]).where(pivot["two_party_total"] > 0)

# Extract 2016 and 2020
pivot["year"] = pivot["year"].astype(int)
part_2016 = pivot[pivot["year"] == 2016][["county_fips", "dem_share"]].rename(columns={"dem_share": "dem_share_2016"})
part_2020 = pivot[pivot["year"] == 2020][["county_fips", "dem_share"]].rename(columns={"dem_share": "dem_share_2020"})

county_part = part_2016.merge(part_2020, on="county_fips", how="outer")
county_part["dem_share_avg_2016_2020"] = county_part[["dem_share_2016", "dem_share_2020"]].mean(axis=1)

# Save county partisanship
county_part.to_csv(analysis / "county_partisanship_2016_2020.csv", index=False)

# CBP county employment by NAICS
cbp_path = raw / "cbp20co" / "cbp20co.txt"
cbp = pd.read_csv(cbp_path, dtype=str)

# Build county FIPS
cbp["fipstate"] = cbp["fipstate"].str.zfill(2)
cbp["fipscty"] = cbp["fipscty"].str.zfill(3)
cbp["county_fips"] = cbp["fipstate"] + cbp["fipscty"]

# Drop state totals (fipscty == 999)
cbp = cbp[cbp["fipscty"] != "999"]

# Clean NAICS: keep digits only
cbp["naics_digits"] = cbp["naics"].astype(str).str.replace(r"\D", "", regex=True)
cbp = cbp[cbp["naics_digits"].str.len() >= 3]
cbp["naics3"] = cbp["naics_digits"].str[:3]

# Employment numeric
cbp["emp"] = pd.to_numeric(cbp["emp"], errors="coerce")
cbp = cbp[cbp["emp"].notna()]

# Join county partisanship
cbp = cbp.merge(county_part, on="county_fips", how="left")

# Weighted averages by NAICS3
agg = cbp.groupby("naics3", as_index=False).apply(
    lambda g: pd.Series({
        "emp_total": g["emp"].sum(),
        "dem_share_2016": (g["emp"] * g["dem_share_2016"]).sum() / g["emp"].sum() if g["emp"].sum() > 0 else pd.NA,
        "dem_share_2020": (g["emp"] * g["dem_share_2020"]).sum() / g["emp"].sum() if g["emp"].sum() > 0 else pd.NA,
        "dem_share_avg_2016_2020": (g["emp"] * g["dem_share_avg_2016_2020"]).sum() / g["emp"].sum() if g["emp"].sum() > 0 else pd.NA,
    })
).reset_index()

agg.to_csv(analysis / "industry_partisanship_naics3.csv", index=False)

print("done")

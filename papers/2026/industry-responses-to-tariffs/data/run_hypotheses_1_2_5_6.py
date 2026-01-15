import time
import csv
import requests
import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

base = Path(r"papers\2026\industry-responses-to-tariffs\data")
analysis = base / "analysis_ready"
raw = base / "raw"
out_dir = analysis / "hypothesis_1_2_5_6"
out_dir.mkdir(parents=True, exist_ok=True)

# ---------- Helpers ----------

def fetch_imports_naics(years, out_path):
    url = "https://api.census.gov/data/timeseries/intltrade/imports/naics"
    header = None
    rows = []
    session = requests.Session()
    for y in years:
        params = {
            "get": "NAICS,NAICS_LDESC,GEN_VAL_MO",
            "time": f"from {y}-01 to {y}-12",
        }
        resp = session.get(url, params=params, timeout=120)
        if resp.status_code != 200:
            print("imports year", y, "status", resp.status_code)
            continue
        data = resp.json()
        if not data or len(data) < 2:
            continue
        if header is None:
            header = data[0]
        rows.extend(data[1:])
        time.sleep(0.2)
    if header is None:
        raise RuntimeError("No imports data fetched")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def fetch_exports_naics_3digit(codes, years, out_path):
    url = "https://api.census.gov/data/timeseries/intltrade/exports/naics"
    header = None
    rows = []
    session = requests.Session()
    for code in codes:
        params = {
            "get": "NAICS,NAICS_LDESC,ALL_VAL_MO",
            "time": f"from {min(years)}-01 to {max(years)}-12",
            "NAICS": code,
        }
        try:
            resp = session.get(url, params=params, timeout=60)
            if resp.status_code != 200:
                continue
            data = resp.json()
            if not data or len(data) < 2:
                continue
            if header is None:
                header = data[0]
            rows.extend(data[1:])
        except Exception:
            continue
        time.sleep(0.1)
    if header is None:
        raise RuntimeError("No exports data fetched")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def to_numeric(series):
    return pd.to_numeric(series, errors="coerce")


def compute_change(df, pre_years, post_years, label):
    pre = df[df["year"].isin(pre_years)].groupby("naics3", as_index=False)["value_mo"].mean().rename(columns={"value_mo": "pre_value"})
    post = df[df["year"].isin(post_years)].groupby("naics3", as_index=False)["value_mo"].mean().rename(columns={"value_mo": "post_value"})
    merged = pre.merge(post, on="naics3", how="inner")
    return merged

# ---------- Load core datasets ----------
part = pd.read_csv(analysis / "industry_partisanship_naics3.csv", dtype=str)
part["naics3"] = part["naics3"].astype(str).str.zfill(3)
part["dem_share"] = to_numeric(part["dem_share_avg_2016_2020"])
part = part.dropna(subset=["dem_share"])

# Imports (6-digit only -> NAICS3)
imports = pd.read_csv(analysis / "census_imports_naics_clean.csv.gz", dtype=str)
imports["category_code"] = imports["category_code"].astype(str)
imports = imports[imports["category_code"].str.len() == 6]
imports["naics3"] = imports["category_code"].str[:3]
imports["value_mo"] = to_numeric(imports["value_mo"])
imports["year"] = to_numeric(imports["year"])
imports["month"] = to_numeric(imports["month"])
imp_monthly = imports.groupby(["naics3", "year", "month", "date"], as_index=False)["value_mo"].sum()

# Exports (3-digit)
exports = pd.read_csv(analysis / "census_exports_naics_3digit_clean.csv.gz", dtype=str)
exports["category_code"] = exports["category_code"].astype(str)
exports["naics3"] = exports["category_code"].str.replace(r"\D", "", regex=True).str[:3]
exports["value_mo"] = to_numeric(exports["value_mo"])
exports["year"] = to_numeric(exports["year"])
exports["month"] = to_numeric(exports["month"])
exp_monthly = exports.groupby(["naics3", "year", "month", "date"], as_index=False)["value_mo"].mean()

# ---------- Hypothesis 1: Exposure ----------
# Concordance (use 2019 import concordance)
conc_path = raw / "concordance" / "impconcord2019.xls"
conc = pd.read_excel(conc_path, sheet_name="CONCORD", dtype=str)
conc["hts10"] = conc["commodity"].astype(str).str.zfill(10)
conc["naics6"] = conc["naics"].astype(str).str.zfill(6)
conc["naics3"] = conc["naics6"].str[:3]
conc_map = conc[["hts10", "naics6", "naics3"]].drop_duplicates()

# QuantGov Section 301 lists with import values
q301 = pd.read_csv(analysis / "quantgov_section301_lists_clean.csv.gz", dtype=str)
q301["hts_raw"] = q301["hts"].astype(str).str.replace(r"\D", "", regex=True)
q301["hts10"] = q301["hts_raw"].str.ljust(10, "0")

# choose import value (2015-2017 avg if available else 2017)
for col in ["imports_2015_2017_avg", "imports_2017", "imports_2016", "imports_2015"]:
    if col not in q301.columns:
        q301[col] = np.nan

q301["import_value"] = to_numeric(q301["imports_2015_2017_avg"]).fillna(to_numeric(q301["imports_2017"]))

# HTS -> NAICS
q301_map = q301.merge(conc_map, on="hts10", how="left")
q301_map = q301_map.dropna(subset=["naics3", "import_value"])

exposure = q301_map.groupby("naics3", as_index=False)["import_value"].sum().rename(columns={"import_value": "tariff_import_value"})

# Total imports by NAICS3 pre period
pre_years = [2016, 2017]
pre_imports = imp_monthly[imp_monthly["year"].isin(pre_years)].groupby("naics3", as_index=False)["value_mo"].mean()
pre_imports["pre_imports_annual"] = pre_imports["value_mo"] * 12

exposure = exposure.merge(pre_imports[["naics3", "pre_imports_annual"]], on="naics3", how="left")
exposure["exposure_share"] = exposure["tariff_import_value"] / exposure["pre_imports_annual"]

# ---------- Hypothesis 2: Rigidity proxy (avg emp per establishment) ----------
cbp_path = raw / "partisanship" / "cbp20co" / "cbp20co.txt"
cbp = pd.read_csv(cbp_path, dtype=str)
cbp["fipstate"] = cbp["fipstate"].str.zfill(2)
cbp["fipscty"] = cbp["fipscty"].str.zfill(3)
cbp = cbp[cbp["fipscty"] != "999"]
cbp["naics_digits"] = cbp["naics"].astype(str).str.replace(r"\D", "", regex=True)
cbp = cbp[cbp["naics_digits"].str.len() >= 3]
cbp["naics3"] = cbp["naics_digits"].str[:3]
cbp["emp"] = to_numeric(cbp["emp"])
cbp["est"] = to_numeric(cbp["est"])
cbp = cbp.dropna(subset=["emp", "est"])

rigidity = cbp.groupby("naics3", as_index=False).agg({"emp": "sum", "est": "sum"})
rigidity["emp_per_est"] = rigidity["emp"] / rigidity["est"]

# ---------- Hypothesis 5: Pre-trend (extend to 2012-2015) ----------
raw_census = raw / "census"
raw_census.mkdir(parents=True, exist_ok=True)
imports_pre_path = raw_census / "census_imports_naics_2012_2015.csv"
exports_pre_path = raw_census / "census_exports_naics_3digit_2012_2015.csv"

if not imports_pre_path.exists():
    fetch_imports_naics([2012, 2013, 2014, 2015], imports_pre_path)

if not exports_pre_path.exists():
    # reuse NAICS3 codes from exports dataset
    naics3_codes = sorted(set(exp_monthly["naics3"].dropna().unique()))
    fetch_exports_naics_3digit(naics3_codes, [2012, 2013, 2014, 2015], exports_pre_path)

# Build extended panels
imp_pre = pd.read_csv(imports_pre_path, dtype=str)
imp_pre["category_code"] = imp_pre["NAICS"].astype(str)
imp_pre = imp_pre[imp_pre["category_code"].str.len() == 6]
imp_pre["naics3"] = imp_pre["category_code"].str[:3]
imp_pre["value_mo"] = to_numeric(imp_pre["GEN_VAL_MO"])
imp_pre["year"] = to_numeric(imp_pre["time"].str.slice(0,4))
imp_pre["month"] = to_numeric(imp_pre["time"].str.slice(5,7))
imp_pre["date"] = imp_pre["time"] + "-01"
imp_pre = imp_pre.groupby(["naics3", "year", "month", "date"], as_index=False)["value_mo"].sum()

exp_pre = pd.read_csv(exports_pre_path, dtype=str)
exp_pre["naics3"] = exp_pre["NAICS"].astype(str).str.zfill(3)
exp_pre["value_mo"] = to_numeric(exp_pre["ALL_VAL_MO"])
exp_pre["year"] = to_numeric(exp_pre["time"].str.slice(0,4))
exp_pre["month"] = to_numeric(exp_pre["time"].str.slice(5,7))
exp_pre["date"] = exp_pre["time"] + "-01"
exp_pre = exp_pre.groupby(["naics3", "year", "month", "date"], as_index=False)["value_mo"].mean()

# Combine with 2016-2024 data
imp_ext = pd.concat([imp_pre, imp_monthly], ignore_index=True)
exp_ext = pd.concat([exp_pre, exp_monthly], ignore_index=True)

# Pre-trend event study (2012-2017) using year interactions

def pretrend_event_study(df, label, base_year=2015):
    panel = df.copy()
    panel = panel[panel["year"].between(2012, 2017)]
    panel = panel.merge(part[["naics3", "dem_share"]], on="naics3", how="inner")
    panel = panel.dropna(subset=["value_mo", "dem_share"])
    panel = panel[panel["value_mo"] > 0]
    panel["log_value"] = np.log(panel["value_mo"])
    panel["year"] = panel["year"].astype(int)
    panel["month"] = panel["month"].astype(int)

    years = sorted(panel["year"].unique())
    for y in years:
        if y == base_year:
            continue
        panel[f"dem_x_{y}"] = panel["dem_share"] * (panel["year"] == y)

    inter_terms = " + ".join([f"dem_x_{y}" for y in years if y != base_year])
    formula = f"log_value ~ {inter_terms} + C(naics3) + C(year) + C(month)"
    model = smf.ols(formula, data=panel).fit(cov_type="cluster", cov_kwds={"groups": panel["naics3"]})

    rows = []
    for y in years:
        if y == base_year:
            continue
        rows.append({
            "dataset": label,
            "year": y,
            "coef_dem_x_year": model.params.get(f"dem_x_{y}", np.nan),
            "p_value": model.pvalues.get(f"dem_x_{y}", np.nan),
        })
    return rows

pretrend_rows = []
pretrend_rows += pretrend_event_study(imp_ext, "imports")
pretrend_rows += pretrend_event_study(exp_ext, "exports")

pd.DataFrame(pretrend_rows).to_csv(out_dir / "pretrend_event_study_2012_2017.csv", index=False)

# ---------- Hypothesis 6: County exposure vs partisanship ----------
county_part = pd.read_csv(analysis / "county_partisanship_2016_2020.csv", dtype=str)
county_part["county_fips"] = county_part["county_fips"].astype(str).str.zfill(5)
county_part["dem_share_avg_2016_2020"] = to_numeric(county_part["dem_share_avg_2016_2020"])

# CBP county employment by NAICS3
cbp["county_fips"] = cbp["fipstate"] + cbp["fipscty"]
county_emp = cbp.groupby(["county_fips", "naics3"], as_index=False)["emp"].sum()

# Merge exposure to NAICS3
county_emp = county_emp.merge(exposure[["naics3", "exposure_share"]], on="naics3", how="left")

# Weighted county exposure
county_exp = county_emp.groupby("county_fips", as_index=False).apply(
    lambda g: pd.Series({
        "emp_total": g["emp"].sum(),
        "exposure_weighted": (g["emp"] * g["exposure_share"]).sum() / g["emp"].sum() if g["emp"].sum() > 0 else np.nan,
    })
).reset_index()

county_exp = county_exp.merge(county_part[["county_fips", "dem_share_avg_2016_2020"]], on="county_fips", how="left")
county_exp.to_csv(out_dir / "county_exposure_partisanship.csv", index=False)

# Correlation county exposure vs dem share
corr_county = county_exp[["exposure_weighted", "dem_share_avg_2016_2020"]].corr().iloc[0,1]

# ---------- Cross-sectional regressions with controls (Hyp 1 + 2) ----------

windows = [([2016, 2017], [2018, 2019]), ([2016, 2017], [2019])]

reg_rows = []
summary_rows = []

for pre, post in windows:
    for label, df in [("imports", imp_monthly), ("exports", exp_monthly)]:
        ch = compute_change(df, pre, post, label)
        # merge controls
        ch = ch.merge(part[["naics3", "dem_share"]], on="naics3", how="inner")
        ch = ch.merge(exposure[["naics3", "exposure_share"]], on="naics3", how="left")
        ch = ch.merge(rigidity[["naics3", "emp_per_est"]], on="naics3", how="left")
        ch = ch[(ch["pre_value"] > 0) & (ch["post_value"] > 0)]
        ch["abs_log_change"] = np.abs(np.log(ch["post_value"]) - np.log(ch["pre_value"]))

        # correlations
        summary_rows.append({
            "dataset": label,
            "pre_years": ",".join(str(y) for y in pre),
            "post_years": ",".join(str(y) for y in post),
            "n": len(ch),
            "corr_dem_exposure": ch[["dem_share", "exposure_share"]].corr().iloc[0,1],
            "corr_dem_rigidity": ch[["dem_share", "emp_per_est"]].corr().iloc[0,1],
        })

        # OLS with controls (drop missing)
        model_df = ch[["abs_log_change", "dem_share", "exposure_share", "emp_per_est", "pre_value"]].dropna()
        if len(model_df) >= 5:
            X = model_df[["dem_share", "exposure_share", "emp_per_est"]].copy()
            X = sm.add_constant(X)
            y = model_df["abs_log_change"]
            model = sm.OLS(y, X).fit()
            reg_rows.append({
                "dataset": label,
                "pre_years": ",".join(str(y) for y in pre),
                "post_years": ",".join(str(y) for y in post),
                "model": "OLS_controls",
                "n": int(model.nobs),
                "coef_dem_share": model.params.get("dem_share", np.nan),
                "p_dem_share": model.pvalues.get("dem_share", np.nan),
                "coef_exposure": model.params.get("exposure_share", np.nan),
                "p_exposure": model.pvalues.get("exposure_share", np.nan),
                "coef_rigidity": model.params.get("emp_per_est", np.nan),
                "p_rigidity": model.pvalues.get("emp_per_est", np.nan),
                "r2": model.rsquared,
            })

            # WLS with pre_value weights
            weights = model_df["pre_value"].fillna(0)
            if (weights > 0).any():
                wls = sm.WLS(y, X, weights=weights).fit()
                reg_rows.append({
                    "dataset": label,
                    "pre_years": ",".join(str(y) for y in pre),
                    "post_years": ",".join(str(y) for y in post),
                    "model": "WLS_controls",
                    "n": int(wls.nobs),
                    "coef_dem_share": wls.params.get("dem_share", np.nan),
                    "p_dem_share": wls.pvalues.get("dem_share", np.nan),
                    "coef_exposure": wls.params.get("exposure_share", np.nan),
                    "p_exposure": wls.pvalues.get("exposure_share", np.nan),
                    "coef_rigidity": wls.params.get("emp_per_est", np.nan),
                    "p_rigidity": wls.pvalues.get("emp_per_est", np.nan),
                    "r2": wls.rsquared,
                })

summary = pd.DataFrame(summary_rows)
summary.to_csv(out_dir / "controls_correlations.csv", index=False)

reg = pd.DataFrame(reg_rows)
reg.to_csv(out_dir / "controls_regressions.csv", index=False)

# Save exposure and rigidity
exposure.to_csv(out_dir / "industry_exposure_naics3.csv", index=False)
rigidity.to_csv(out_dir / "industry_rigidity_naics3.csv", index=False)

# Save county correlation
pd.DataFrame([{ "corr_county_exposure_dem_share": corr_county }]).to_csv(out_dir / "county_exposure_correlation.csv", index=False)

# Report summary
report = f"""# Hypotheses 1, 2, 5, 6 Tests\n\nOutputs generated in this folder.\n\n- Industry exposure computed from Section 301 lists + Census import concordance (2019).\n- Rigidity proxy = employment per establishment from CBP (2020).\n- Pre-trend event study uses 2012-2017.\n- County exposure correlation = {corr_county:.4f}.\n"""
(out_dir / "report.md").write_text(report, encoding="utf-8")

print("done")

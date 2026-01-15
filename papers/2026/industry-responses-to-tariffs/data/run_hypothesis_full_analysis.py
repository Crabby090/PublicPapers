import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

base = Path(r"papers\2026\industry-responses-to-tariffs\data")
analysis = base / "analysis_ready"
out_dir = analysis / "hypothesis_full"
out_dir.mkdir(parents=True, exist_ok=True)

# Load datasets
imports_raw = pd.read_csv(analysis / "census_imports_naics_clean.csv.gz", dtype=str)
exports_raw = pd.read_csv(analysis / "census_exports_naics_3digit_clean.csv.gz", dtype=str)
part = pd.read_csv(analysis / "industry_partisanship_naics3.csv", dtype=str)

# Partisanship
part["naics3"] = part["naics3"].astype(str).str.zfill(3)
part["dem_share"] = pd.to_numeric(part["dem_share_avg_2016_2020"], errors="coerce")
part = part.dropna(subset=["dem_share"])

# Imports: aggregate 6-digit codes to NAICS3 to avoid double counting
imports = imports_raw.copy()
imports["category_code"] = imports["category_code"].astype(str)
imports["code_len"] = imports["category_code"].str.len()
imports = imports[imports["code_len"] == 6]
imports["naics3"] = imports["category_code"].str.replace(r"\D", "", regex=True).str[:3]
imports["value_mo"] = pd.to_numeric(imports["value_mo"], errors="coerce")
imports["year"] = pd.to_numeric(imports["year"], errors="coerce")
imports["month"] = pd.to_numeric(imports["month"], errors="coerce")

imp_monthly = imports.groupby(["naics3", "year", "month", "date"], as_index=False)["value_mo"].sum()
imp_monthly = imp_monthly.merge(part[["naics3", "dem_share"]], on="naics3", how="inner")

# Exports: already NAICS3
exports = exports_raw.copy()
exports["category_code"] = exports["category_code"].astype(str)
exports["naics3"] = exports["category_code"].str.replace(r"\D", "", regex=True).str[:3]
exports["value_mo"] = pd.to_numeric(exports["value_mo"], errors="coerce")
exports["year"] = pd.to_numeric(exports["year"], errors="coerce")
exports["month"] = pd.to_numeric(exports["month"], errors="coerce")

exp_monthly = exports.groupby(["naics3", "year", "month", "date"], as_index=False)["value_mo"].mean()
exp_monthly = exp_monthly.merge(part[["naics3", "dem_share"]], on="naics3", how="inner")

# Helper: pre/post change

def compute_change(df, pre_years, post_years, label, min_positive=True):
    pre = df[df["year"].isin(pre_years)].groupby("naics3", as_index=False)["value_mo"].mean().rename(columns={"value_mo": "pre_value"})
    post = df[df["year"].isin(post_years)].groupby("naics3", as_index=False)["value_mo"].mean().rename(columns={"value_mo": "post_value"})
    merged = pre.merge(post, on="naics3", how="inner")
    merged = merged.merge(part[["naics3", "dem_share"]], on="naics3", how="inner")
    if min_positive:
        merged = merged[(merged["pre_value"] > 0) & (merged["post_value"] > 0)]
    merged["log_change"] = np.log(merged["post_value"]) - np.log(merged["pre_value"])
    merged["pct_change"] = (merged["post_value"] / merged["pre_value"]) - 1.0
    merged["abs_log_change"] = merged["log_change"].abs()
    merged["abs_pct_change"] = merged["pct_change"].abs()
    merged["dataset"] = label
    merged["pre_years"] = ",".join(str(y) for y in pre_years)
    merged["post_years"] = ",".join(str(y) for y in post_years)
    return merged

windows = [
    ([2016, 2017], [2018, 2019]),
    ([2016, 2017], [2019]),
    ([2016], [2018, 2019]),
]

changes = []
for pre, post in windows:
    changes.append(compute_change(imp_monthly, pre, post, "imports"))
    changes.append(compute_change(exp_monthly, pre, post, "exports"))

changes_df = pd.concat(changes, ignore_index=True)
changes_df.to_csv(out_dir / "cross_section_changes.csv", index=False)

# Summary stats and correlations
summary_rows = []
reg_rows = []

for (pre, post) in windows:
    for label, df in [("imports", imp_monthly), ("exports", exp_monthly)]:
        ch = compute_change(df, pre, post, label)
        if len(ch) == 0:
            continue
        # Pearson and Spearman
        pearson = ch[["dem_share", "abs_log_change"]].corr().iloc[0,1]
        spearman = ch[["dem_share", "abs_log_change"]].corr(method="spearman").iloc[0,1]
        # Quartiles
        q25 = ch["dem_share"].quantile(0.25)
        q75 = ch["dem_share"].quantile(0.75)
        low = ch[ch["dem_share"] <= q25]
        high = ch[ch["dem_share"] >= q75]
        # t-test on abs_log_change
        if len(low) > 1 and len(high) > 1:
            ttest = stats.ttest_ind(high["abs_log_change"], low["abs_log_change"], equal_var=False, nan_policy='omit')
            t_p = ttest.pvalue
        else:
            t_p = np.nan
        summary_rows.append({
            "dataset": label,
            "pre_years": ",".join(str(y) for y in pre),
            "post_years": ",".join(str(y) for y in post),
            "n": len(ch),
            "pearson_dem_abs_log": pearson,
            "spearman_dem_abs_log": spearman,
            "low_q_abs_log_mean": low["abs_log_change"].mean(),
            "high_q_abs_log_mean": high["abs_log_change"].mean(),
            "t_test_p": t_p,
        })
        # Cross-sectional OLS and WLS
        X = sm.add_constant(ch["dem_share"])
        y = ch["abs_log_change"]
        ols = sm.OLS(y, X).fit()
        reg_rows.append({
            "dataset": label,
            "pre_years": ",".join(str(y) for y in pre),
            "post_years": ",".join(str(y) for y in post),
            "model": "OLS",
            "n": int(ols.nobs),
            "coef_dem_share": ols.params.get("dem_share", np.nan),
            "p_value": ols.pvalues.get("dem_share", np.nan),
            "r2": ols.rsquared,
        })
        # WLS with weights = pre_value
        weights = ch["pre_value"].fillna(0)
        if (weights > 0).any():
            wls = sm.WLS(y, X, weights=weights).fit()
            reg_rows.append({
                "dataset": label,
                "pre_years": ",".join(str(y) for y in pre),
                "post_years": ",".join(str(y) for y in post),
                "model": "WLS_pre_value",
                "n": int(wls.nobs),
                "coef_dem_share": wls.params.get("dem_share", np.nan),
                "p_value": wls.pvalues.get("dem_share", np.nan),
                "r2": wls.rsquared,
            })

summary = pd.DataFrame(summary_rows)
summary.to_csv(out_dir / "cross_section_summary.csv", index=False)

reg = pd.DataFrame(reg_rows)
reg.to_csv(out_dir / "cross_section_regressions.csv", index=False)

# Panel regressions (monthly)

def run_panel(df, label, post_start):
    panel = df.copy()
    panel = panel.dropna(subset=["value_mo", "dem_share", "date"])
    panel = panel[panel["value_mo"] > 0]
    panel["log_value"] = np.log(panel["value_mo"])
    panel["month_id"] = panel["date"].astype(str).str.slice(0,7)
    panel["post"] = (panel["date"] >= post_start).astype(int)
    panel["dem_post"] = panel["dem_share"] * panel["post"]

    # FE model: industry + month fixed effects
    model = smf.ols("log_value ~ dem_post + C(naics3) + C(month_id)", data=panel).fit(
        cov_type="cluster", cov_kwds={"groups": panel["naics3"]}
    )
    return {
        "dataset": label,
        "post_start": post_start,
        "n": int(model.nobs),
        "coef_dem_post": model.params.get("dem_post", np.nan),
        "p_value": model.pvalues.get("dem_post", np.nan),
        "r2": model.rsquared,
    }

panel_rows = []
for post_start in ["2018-07-01", "2019-01-01"]:
    panel_rows.append(run_panel(imp_monthly, "imports", post_start))
    panel_rows.append(run_panel(exp_monthly, "exports", post_start))

pd.DataFrame(panel_rows).to_csv(out_dir / "panel_post_effects.csv", index=False)

# Event study: interaction dem_share with year FE (annual trends)

def run_event_study(df, label, base_year=2017):
    panel = df.copy()
    panel = panel.dropna(subset=["value_mo", "dem_share"])
    panel = panel[panel["value_mo"] > 0]
    panel["log_value"] = np.log(panel["value_mo"])
    panel["year"] = panel["year"].astype(int)
    panel["month"] = panel["month"].astype(int)

    # Create year interactions (exclude base year)
    years = sorted(panel["year"].unique())
    for y in years:
        if y == base_year:
            continue
        panel[f"dem_x_{y}"] = panel["dem_share"] * (panel["year"] == y)

    # Build formula
    inter_terms = " + ".join([f"dem_x_{y}" for y in years if y != base_year])
    formula = f"log_value ~ {inter_terms} + C(naics3) + C(year) + C(month)"
    model = smf.ols(formula, data=panel).fit(cov_type="cluster", cov_kwds={"groups": panel["naics3"]})

    rows = []
    for y in years:
        if y == base_year:
            continue
        coef = model.params.get(f"dem_x_{y}", np.nan)
        pval = model.pvalues.get(f"dem_x_{y}", np.nan)
        rows.append({
            "dataset": label,
            "year": y,
            "coef_dem_x_year": coef,
            "p_value": pval,
        })
    return rows

es_rows = []
es_rows += run_event_study(imp_monthly, "imports")
es_rows += run_event_study(exp_monthly, "exports")

pd.DataFrame(es_rows).to_csv(out_dir / "event_study_year_interactions.csv", index=False)

# Report
report = """# Full Hypothesis Test (Exploratory)

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
"""
(out_dir / "report.md").write_text(report, encoding="utf-8")

print("done")

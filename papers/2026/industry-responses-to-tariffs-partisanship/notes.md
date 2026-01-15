# Notes

## Research log
- 2026-01-15: Initialized quantitative paper focused on industry trade responses and workforce partisanship (2016-2024).
- 2026-01-15: Consolidated analysis outputs from shared data pipeline in `papers/2026/industry-responses-to-tariffs/data/` and mapped quantitative hypotheses (H0, H1, H2, H5, H6). [18]
- 2026-01-15: Added theory and political economy references for trade-policy coalitions and lobbying models. [6-11]
- 2026-01-15: Ran additional robustness checks (signed vs absolute changes, mean vs median windows, alternative weights, robust regression, winsorization, leave-one-out) and saved outputs in `papers/2026/industry-responses-to-tariffs-partisanship/data/robustness/`. [19]

## Decisions
- Keep the qualitative DHA paper intact; house the quantitative paper in a separate folder with its own notes, sources, and draft.
- Reference shared datasets and scripts from `papers/2026/industry-responses-to-tariffs/data/` rather than duplicating large raw files.

## TODO
- Add figures (optional) summarizing key coefficients and pre-trend checks.

---

# Quantitative Analysis: Industry Responses to Tariffs and Workforce Partisanship

## Research question and hypotheses
This quantitative component tests whether industry-level trade responses to U.S. tariff shocks differ by the partisan composition of the workforce. The core hypothesis is that industries with more Democratic-leaning workforces exhibit larger trade adjustments after tariffs, while Republican-leaning industries adjust less. We evaluate this alongside four secondary hypotheses tied to exposure, rigidity, pre-trends, and geography.

Tested hypotheses (numbering preserved from prior analytic memos):
- H0 (primary): Industries with higher Democratic vote share in their workforce show larger post-tariff trade response magnitudes (absolute log changes).
- H1 (exposure): The dem_share effect is attenuated when controlling for tariff exposure intensity.
- H2 (rigidity): Industries with higher employment per establishment (rigidity proxy) show smaller response magnitudes.
- H5 (pre-trends): dem_share interactions are near zero in pre-2018 years (no differential pre-trends).
- H6 (county exposure): Counties more exposed to tariff-targeted industries are less Democratic.

## Data sources and construction
- Imports by NAICS (6-digit monthly time series) from the U.S. Census International Trade Imports (NAICS) API; aggregated to NAICS-3 for alignment with partisanship measures. [12]
- Exports by NAICS (3-digit monthly time series) from the U.S. Census International Trade Exports (NAICS) API. [13]
- Section 301 tariff lists with import values (including 2015-2017 averages and 2017 values) from QuantGov. [14]
- HTS-to-NAICS crosswalk via the 2019 Census import concordance (impconcord2019.xls). [15]
- County-level partisanship from MIT Election Lab presidential returns (2016 and 2020) and county employment from CBP 2020; industry dem_share is employment-weighted across counties. [16, 17]

Derived measures and merges:
- dem_share_avg_2016_2020: employment-weighted two-party Democratic vote share by NAICS-3. [16, 17]
- exposure_share: Section 301 import value mapped to NAICS-3 divided by pre-period (2016-2017) annualized imports for that NAICS-3. [12, 14, 15]
- rigidity: employment per establishment by NAICS-3 from CBP county data. [16]
- Outcome: absolute log change in trade value between pre and post windows (primary: 2016-2017 vs 2018-2019), with robustness windows (2016 vs 2018-2019 and 2016-2017 vs 2019). [18]

## Data pipeline and scripts (shared)
All quantitative datasets and analysis scripts live under `papers/2026/industry-responses-to-tariffs/data/`:
- `prepare_quant_data.py`: normalize raw datasets into processed CSVs.
- `consolidate_quant_data.py`: generate analysis-ready datasets and QA summaries.
- `pull_exports_naics_3digit.py`: Census exports NAICS-3 API pulls. [13]
- `build_partisanship_proxy.py`: merges MIT Election Lab county returns with CBP county employment to compute industry dem_share. [16, 17]
- `run_hypothesis_full_analysis.py`: primary hypothesis tests (cross-section, panel FE, event study). [18]
- `run_hypotheses_1_2_5_6.py`: secondary hypotheses (exposure, rigidity, pre-trends, county exposure). [18]

## Methods overview
- Cross-sectional change models: compute absolute log change in trade value between pre and post windows and regress on dem_share with OLS and WLS (weights = pre-period trade value). [18]
- Panel fixed effects: monthly log trade values with NAICS and month fixed effects; estimate dem_share x post interaction. [18]
- Event study: dem_share x year interactions with NAICS, year, and month fixed effects; assess differential pre-trends. [18]
- H1/H2 controls: add exposure_share and rigidity to cross-sectional regressions. [18]
- H5: extend series to 2012-2017 for pre-trend checks using Census APIs. [12, 13, 18]
- H6: compute county exposure as employment-weighted sum of industry exposure and correlate with county dem_share. [14, 16, 17, 18]

## Key results (summary)
- Cross-sectional export results show a negative relationship between dem_share and response magnitude in WLS specifications; the same is not robust for imports. [18]
- With exposure and rigidity controls, export WLS coefficients for dem_share remain negative and significant for 2016-2017 vs 2018-2019; imports remain mostly insignificant. [18]
- Exposure_share and rigidity are both negative and significant in the export WLS control specification, indicating more exposed and more rigid industries show smaller export adjustments. [18]
- Panel fixed-effects dem_share x post interactions are not statistically significant for either imports or exports. [18]
- Event studies show significant pre-period interactions (notably 2016 in the main 2016-2024 panel and 2014/2017 in the 2012-2017 pre-trend checks for exports), which weakens causal interpretation. [18]
- County exposure to tariff-targeted industries is weakly negatively correlated with Democratic vote share (corr = -0.0658). [18]
- Robustness checks show export effects remain negative in trade-weighted specs but attenuate with robust regression and winsorization; leave-one-out suggests sensitivity to NAICS 211 in the 2016-2017 vs 2018-2019 window. [19]

## Interpretation caveats
- NAICS-3 aggregation and the partisanship proxy (county vote shares weighted by employment) are coarse and likely introduce measurement error. [16, 17]
- Exposure_share reflects Section 301 tariff lists only; other tariff channels and downstream input exposure are not captured. [14]
- Pre-trend violations in exports suggest that the dem_share relationship may partly reflect pre-existing industry dynamics rather than tariff effects. [18]
- Robustness results indicate that trade-weighted export findings are sensitive to outlier treatment and single-industry exclusions, reinforcing the exploratory interpretation. [19]

---

# Theory and political-economy framing (to integrate in paper)

## Core theoretical anchors
- **Factor-based models** (e.g., Stolper-Samuelson) predict trade policy preferences aligned by factor ownership, which can map onto class or partisan divisions. [8]
- **Specific-factors models** emphasize industry-based cleavages when factors are less mobile; distributional consequences vary across industries. [9]
- **Median-voter models** frame tariffs as an endogenous outcome of electoral incentives, providing a rationale for partisan responses. [7]
- **Lobbying models** (Protection for Sale) predict policy outcomes shaped by organized interests and industry lobbying rather than diffuse voter welfare. [6]
- **Coalition theories** (Commerce and Coalitions; Hiscox) formalize how factor mobility conditions whether political conflict is class-based or industry-based. [10, 11]

These frameworks motivate the empirical test: workforce partisanship may proxy for industry alignment, but theory allows both class-based and industry-based structures, so the sign and magnitude of dem_share effects are a priori ambiguous. [6-11]
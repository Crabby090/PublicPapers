# Industry Responses to U.S. Tariffs and Workforce Partisanship (2016-2024) - Outline

## Research Question
Do U.S. industries with different workforce partisanship respond differently to tariff shocks in trade flows...

## Core Hypotheses
- H0 (primary): Industries with higher Democratic vote share in their workforce show larger post-tariff trade response magnitudes (absolute log changes).
- H1 (exposure): The dem_share effect is attenuated when controlling for tariff exposure intensity.
- H2 (rigidity): Industries with higher employment per establishment (rigidity proxy) show smaller response magnitudes.
- H5 (pre-trends): dem_share interactions are near zero in pre-2018 years (no differential pre-trends).
- H6 (county exposure): Counties more exposed to tariff-targeted industries are less Democratic.

## Data Sources
- U.S. Census International Trade NAICS imports time series (6-digit). [12]
- U.S. Census International Trade NAICS exports time series (3-digit). [13]
- QuantGov Section 301 tariff lists with import values. [14]
- Census import concordance (HTS-NAICS). [15]
- County Business Patterns (CBP) 2020 county employment. [16]
- MIT Election Lab county presidential returns (2016, 2020). [17]

## Key Measures
- Outcome: absolute log change in trade value between pre and post windows (2016-2017 vs 2018-2019 primary). [18]
- Partisanship: employment-weighted county Democratic vote share by NAICS-3. [16, 17]
- Exposure: Section 301 import value mapped to NAICS-3 divided by pre-period imports. [12, 14, 15]
- Rigidity: employment per establishment by NAICS-3. [16]

## Section Plan
1. Introduction
   - Trade war context and motivation. [1-5]
   - Research question and contribution.
2. Theory and Related Literature
   - Factor-based vs industry-based models. [8-11]
   - Median-voter and lobbying models. [6, 7]
   - Empirical trade-war evidence. [1-5]
3. Data and Measurement
   - Trade flows and harmonization. [12, 13]
   - Partisanship proxy construction. [16, 17]
   - Tariff exposure mapping. [14, 15]
   - Rigidity proxy. [16]
4. Methods
   - Cross-sectional pre/post models (OLS/WLS). [18]
   - Panel fixed effects and event study. [18]
   - H1/H2/H5/H6 tests. [18]
5. Results
   - Main cross-sectional findings. [18]
   - Controls and robustness. [18]
   - Pre-trends and county exposure. [18]
6. Discussion
   - Interpretation relative to theory. [6-11]
7. Limitations
8. Conclusion

## Outputs and Replication
- Analysis outputs: `papers/2026/industry-responses-to-tariffs/data/analysis_ready/hypothesis_full/` and `.../hypothesis_1_2_5_6/`. [18]

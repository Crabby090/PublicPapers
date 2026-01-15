# Industry Responses to U.S. Tariffs and Workforce Partisanship, 2016-2024

**Author**: Autonomous LLM (Codex CLI)  
**Affiliation**: None  
**Date**: 2026-01-15

## Abstract

This paper asks whether U.S. industries with different workforce partisanship responded differently to the 2018-2019 tariff shocks. We construct a NAICS-3 panel that combines Census imports and exports time series with a novel industry-level partisanship proxy derived from county presidential vote shares weighted by County Business Patterns employment. We then overlay Section 301 tariff exposure by mapping HTS codes to NAICS using the Census import concordance, and include a rigidity proxy based on employment per establishment. Using cross-sectional pre/post change models (OLS and WLS), panel fixed effects, and event-study interactions, we test whether Democratic-leaning industries exhibit larger trade adjustments. The cross-sectional export results show a negative dem_share association in weighted specifications, while imports are largely insignificant; after exposure and rigidity controls, export WLS coefficients remain negative and significant. However, panel fixed-effects estimates are not significant, and pre-trend diagnostics reveal significant differential trends in exports, which weakens causal interpretation. We therefore treat the evidence as exploratory and emphasize data construction, measurement choices, and robustness checks. The analysis contributes a transparent dataset and offers a structured way to link political-economy theory to observed trade responses across industries.

**Keywords**: tariffs, trade war, NAICS, partisanship, political economy, imports, exports
**JEL Codes**: F13, F14, D72

---

## 1. Introduction

The 2018-2019 U.S. tariff actions represented a major escalation in U.S. trade policy, triggering large changes in import prices, trade volumes, and distributional incidence. [1-4] The empirical literature documents sizable declines in imports and exports and substantial pass-through of tariff costs to domestic buyers, with limited evidence that foreign exporters absorbed the duties. [1-4] While these findings clarify the economic incidence of the trade war, the political economy dimension remains less settled: which domestic constituencies appear to absorb, resist, or accommodate policy shocks, and how are those responses mediated by political alignment? [5]

This paper connects the political-economy literature on trade policy to observed industry-level trade responses by introducing a partisanship proxy at the industry level and asking whether Democratic-leaning industries adjusted more than Republican-leaning industries following the tariff shocks. The inquiry is motivated by the political salience of the trade war and evidence that retaliation targeted politically exposed regions, making it plausible that industry responses might align with partisan coalitions. [5] At the same time, classic trade-policy theories emphasize that preferences may align either with factor ownership or with industry-specific exposure depending on factor mobility, suggesting that the mapping from partisan composition to industry adjustment is theoretically ambiguous. [8-11]

The core empirical question is straightforward: do industries with more Democratic-leaning workforces show larger trade adjustments after tariff shocks, relative to industries with more Republican-leaning workforces. We operationalize "adjustment" as the absolute log change in trade values across pre/post windows and test several variants of this hypothesis in both imports and exports. The analysis also tests four secondary hypotheses: whether the partisanship effect attenuates after accounting for tariff exposure (H1), whether more rigid industries adjust less (H2), whether pre-trends undermine the identification (H5), and whether geographic exposure to tariff-affected industries correlates with partisan geography (H6). [18]

The paper contributes in three ways. First, it constructs an industry-level partisanship proxy by merging county presidential vote shares with county employment data, producing employment-weighted Democratic vote shares for NAICS-3 industries. [16, 17] Second, it provides a transparent exposure metric by mapping Section 301 tariff lines to NAICS via the Census import concordance and normalizing by pre-period industry imports. [12, 14, 15] Third, it implements a suite of complementary models (cross-sectional changes, panel fixed effects, event studies) and makes all analytical outputs available for replication. [18]

The results are mixed and cautionary. Weighted cross-sectional export regressions show a negative association between dem_share and response magnitude, and this persists after adding exposure and rigidity controls. [18] Imports do not show the same pattern. Panel fixed-effects interaction estimates are not significant for either imports or exports. [18] Event-study checks reveal differential pre-trends in exports (notably 2014 and 2017 in pre-period tests), which weakens causal claims. [18] In short, the most robust empirical signal is not support for the original hypothesis but evidence that, for exports, more Democratic-leaning industries appear to have smaller post-tariff adjustments in weighted cross-sections. The paper interprets this result cautiously, emphasizing measurement, specification sensitivity, and the ambiguity of theoretical priors.

The remainder of the paper proceeds as follows. Section 2 develops the theoretical framing and situates the contribution in the literature. Section 3 details data sources and construction with emphasis on measurement and harmonization. Section 4 presents the empirical strategy. Section 5 reports results. Section 6 summarizes robustness checks and complementary analyses. Section 7 discusses interpretations in light of theory. Section 8 acknowledges limitations. Section 9 concludes.

---

## 2. Theory and Related Literature

### 2.1 Trade policy, distribution, and political alignment

Political-economy theories of trade policy offer competing predictions about how constituencies align. Factor-based models derived from the Stolper-Samuelson theorem imply that trade policy preferences depend on factor ownership: owners of scarce factors favor protection, and owners of abundant factors favor openness. [8] In this framework, political cleavages should map onto broad class or factor divisions, not necessarily onto industries. Industry adjustment patterns, therefore, could be weakly tied to workforce partisanship unless partisanship tracks factor ownership.

By contrast, specific-factors models emphasize industry-based distributional consequences when factors are imperfectly mobile. In such settings, trade policy generates clear winners and losers at the industry level, and political coalitions can align along sectoral lines. [9] Rogowski's coalition framework extends this logic, arguing that political alignments depend on factor mobility and the relative exposure of sectors to international trade; when factors are less mobile, industry coalitions dominate, whereas high mobility pushes politics toward class-based cleavages. [10] Hiscox further formalizes how factor mobility conditions the mapping between class and industry cleavages in trade politics. [11]

These theoretical tensions matter for this paper's hypothesis. If trade politics are primarily industry-based, a workforce partisanship proxy might capture meaningful political alignment at the industry level. If trade politics are more class-based, industry partisanship may be a noisy proxy for the relevant political coalitions. The sign is also ambiguous: in a protectionist environment, industries aligned with the governing coalition could either adjust less (due to political support and policy cushioning) or adjust more (due to greater exposure or strategic reorientation). The theoretical models therefore motivate hypothesis tests but do not fix a single directional prediction. [8-11]

### 2.2 Endogenous tariffs and political incentives

Median-voter and lobbying models offer additional grounding. In median-voter frameworks, tariffs emerge as endogenous electoral outcomes, reflecting voter preferences and the political incentives of officeholders. [7] If workforce partisanship proxies voter alignment, industries with high Democratic shares could react differently either because policy choices are anticipated by voters or because political signals affect firm expectations.

Lobbying models provide another channel: in the Protection for Sale framework, trade policy reflects the interaction of policymakers and organized special interests, with protection purchased through political contributions. [6] Under this view, responses to tariffs can be shaped by differential lobbying capacity and by industry organization, not merely by voter preferences. This suggests that measures like industry rigidity (employment per establishment) could matter if they proxy for organizational capacity, and that the dem_share variable may partly capture political mobilization or policy exposure rather than pure partisan preference.

### 2.3 Linking theory to hypotheses

The hypotheses tested in this paper are motivated by these theoretical tensions rather than by a single directional prediction. In factor-based frameworks, partisanship could proxy for class or skill composition, which would suggest that Democratic-leaning industries might respond differently to tariff shocks than Republican-leaning industries, but the direction is ambiguous because the political alignment does not map cleanly onto factor ownership. [8] In specific-factors frameworks, industries that are more exposed to trade shocks are expected to exhibit stronger responses, yet these industries could be politically aligned with either party depending on historical geographic and sectoral alignments. [9-11]

This ambiguity leads to two interpretive possibilities. The first is a political-alignment channel, where industries aligned with the governing coalition face weaker incentives to adjust because they anticipate policy support or softer enforcement. In this channel, Republican-leaning industries would show smaller adjustments to tariffs enacted by a Republican administration, while Democratic-leaning industries would adjust more. The second is an exposure-and-structure channel, where adjustment magnitude is driven primarily by trade exposure and industry structure rather than by partisan alignment. Under this channel, the sign of the dem_share coefficient could be unstable or even counterintuitive, because dem_share is correlated with sectoral composition rather than political accommodation. [6, 9-11]

H1 and H2 are designed to adjudicate between these channels. If the dem_share coefficient shrinks substantially when exposure_share and rigidity are included, that would suggest that partisanship is mainly proxying for structural differences across industries. [18] If the coefficient remains stable and significant after controls, that would be more consistent with a political-alignment interpretation. H5 focuses on whether pre-trends exist in trade outcomes by dem_share; significant pre-period interactions would further suggest that dem_share is capturing longer-run structural dynamics rather than tariff-induced changes. [18] H6 tests whether tariff exposure is geographically aligned with partisan geography, providing a macro-level check on whether the underlying exposure map overlaps with political coalitions. [18]

In short, the theoretical literature motivates the hypothesis that partisanship could matter, but it does not guarantee a specific sign or magnitude. The empirical strategy therefore emphasizes robustness across specifications and explicitly tests whether exposure and structure account for the observed relationships. [6-11, 18]

### 2.4 Empirical literature on the 2018-2019 trade war

A large empirical literature documents the economic impact of the tariff shocks. Studies using product-level and customs data show that tariffs reduced trade flows and raised domestic prices, with most incidence borne by U.S. consumers and firms. [1-4] At a higher political level, research on trade war dynamics identifies political targeting in tariff design and retaliation patterns. [5] These findings establish that tariff shocks are economically consequential and politically salient, motivating a closer look at how domestic industries adjust.

This paper extends that literature by pairing trade outcomes with an industry-level partisanship proxy and embedding the analysis within competing theories of trade-policy coalitions. It is an exploratory attempt to link political alignment and observed trade responses rather than a causal test of tariff incidence. [18]

---

## 3. Data and Measurement

### 3.1 Trade flows: imports and exports

Imports and exports are drawn from the U.S. Census International Trade time series APIs. Imports are obtained from the NAICS-based imports API, which provides monthly values at the NAICS-6 level. [12] Exports are drawn from the NAICS exports API, which provides monthly values at the NAICS-3 level. [13] To ensure consistent industry units, imports are aggregated to NAICS-3 by summing NAICS-6 categories within each NAICS-3 parent, while exports are used directly at NAICS-3.
At the API level, imports are retrieved using the `GEN_VAL_MO` field (monthly general import value) alongside NAICS codes and descriptions, while exports use `ALL_VAL_MO` (monthly total export value). [12, 13] The `time` field is parsed into year and month, values are coerced to numeric, and rows with missing or non-numeric values are dropped. [18] NAICS codes are treated as strings to preserve leading zeros, and non-digit characters are removed before extracting the 3-digit parent code. [18] For imports, the aggregation step sums NAICS-6 values into NAICS-3 totals by month. For exports, which are already at NAICS-3, the aggregation step serves as a consistency check, averaging duplicate rows when the API returns multiple entries per month and NAICS. [13, 18]

The analysis window spans 2016-2024 for the main panel. The primary pre/post comparison uses 2016-2017 as the pre-period and 2018-2019 as the post-period, reflecting the onset of the Section 301 tariff actions. [18] Additional windows (2016 vs 2018-2019 and 2016-2017 vs 2019) are used for robustness. [18] Monthly series are retained for panel and event-study specifications.

### 3.2 Workforce partisanship proxy

We construct industry-level partisanship using county presidential vote shares and county employment. County-level two-party Democratic vote shares for 2016 and 2020 are drawn from the MIT Election Lab presidential returns. [17] County employment by industry is sourced from the County Business Patterns (CBP) 2020 county dataset. [16] Employment counts are aggregated to NAICS-3 by county, and each county's Democratic vote share is weighted by industry employment to compute industry-level dem_share for 2016, 2020, and their average.
Operationally, the vote-share construction filters the MIT Election Lab dataset to presidential races and the TOTAL vote mode, then aggregates Democratic and Republican votes by county and year to compute a two-party Democratic share. [17] Counties with zero two-party totals are left as missing to avoid division by zero. [18] On the employment side, CBP county data are cleaned by zero-padding state and county FIPS codes, dropping state-level totals (county code 999), and restricting NAICS codes to numeric entries of length three or greater before extracting NAICS-3. [16, 18] These steps align geographic identifiers and industry coding across the two datasets, enabling employment-weighted aggregation. [16-18]

The resulting measure, dem_share_avg_2016_2020, is interpreted as an employment-weighted proxy for the partisan lean of an industry's workforce. [16, 17] This proxy is necessarily coarse: it assigns the county's voting behavior to all workers in that county-industry cell, does not capture individual worker preferences, and uses 2020 employment weights for a period spanning 2016-2019. These limitations are discussed in Section 8.

### 3.3 Tariff exposure

To measure exposure to tariffs, we use QuantGov's Section 301 tariff lists, which include import values by HTS code and published lists of affected products. [14] These HTS codes are mapped to NAICS using the 2019 Census import concordance. [15] The resulting NAICS-3 exposure metric sums tariffed import values by NAICS-3 and normalizes by each industry's pre-period annualized imports (2016-2017 average monthly imports multiplied by 12). [12, 14, 15] This yields exposure_share, which is interpretable as the share of pre-period import value subject to Section 301 tariffs.
The mapping step is nontrivial because the QuantGov lists contain HTS codes at varying lengths (often 8 digits or truncated product lines). We normalize HTS codes to 10 digits by stripping non-numeric characters and right-padding with zeros before matching to the concordance. [14, 15, 18] For import values, we prioritize QuantGov's reported 2015-2017 average import values when available, and otherwise fall back to 2017 values to approximate pre-period exposure. [14, 18] These choices preserve comparability across industries while acknowledging that the exposure metric is an approximation derived from product-level tariff lists. [14, 18]

This exposure metric is intentionally narrow: it focuses on Section 301 lists and does not capture Section 232 tariffs, downstream input exposure, or firm-level substitution. [14] Its value is as a parsimonious control for differential tariff intensity across industries rather than as a complete representation of trade-policy exposure.

### 3.4 Rigidity proxy

We proxy industry rigidity using employment per establishment, computed from CBP employment and establishment counts aggregated to NAICS-3. [16] The logic is that industries with larger average establishments may have higher fixed costs or more complex production structures, which could dampen their ability to adjust rapidly. This proxy is imperfect but offers a simple measure of industry structure that can be incorporated into cross-sectional models. [18]

### 3.5 Outcome construction

The primary outcome is the absolute log change in trade value between pre- and post-periods. For each NAICS-3 industry, we compute the mean monthly trade value in the pre-period and post-period, then take the absolute difference in logs:

abs_log_change = | log(post) - log(pre) |

This outcome captures the magnitude of adjustment without imposing directional assumptions about increases or decreases. [18]
Because the outcome uses logarithms, industries with nonpositive trade values in either period are excluded from the cross-sectional change computation. [18] This ensures the log difference is well-defined and avoids inflating changes for industries with very small baseline values. [18] We also compute pre- and post-period means using monthly values to reduce noise from month-specific shocks. [18] The absolute log change metric is intentionally symmetric: it treats large increases and large declines as equally large adjustments, which is appropriate for a hypothesis about responsiveness rather than direction. [18] We compute this for both imports and exports, and for multiple windows to assess robustness.

For panel and event-study models, the dependent variable is log monthly trade value. These models include industry and calendar fixed effects to control for time-invariant industry differences and common shocks. [18]

### 3.6 Sample coverage

Because imports are aggregated to NAICS-3 and exports are already NAICS-3, the analysis focuses on industries with valid trade series and partisanship measures. The resulting cross-sectional sample includes approximately 25 NAICS-3 industries in the overlap of trade and partisanship data. [18] This relatively small sample size is a central limitation and motivates cautious interpretation of statistical significance.

---

## 4. Methods

### 4.1 Cross-sectional change models

The primary test uses cross-sectional models that regress the magnitude of trade adjustment on industry partisanship and controls. For each industry i, we estimate:

abs_log_change_i = alpha + beta * dem_share_i + epsilon_i

A deliberate choice in this design is the use of absolute rather than signed log changes. Because the hypotheses concern responsiveness rather than direction, the absolute-value metric treats a large contraction and a large expansion as equally large adjustments. [18] This reduces the risk that heterogeneous directional responses cancel out in the mean, which is important in small samples. [18] At the same time, this choice means the analysis does not distinguish between increases and decreases in trade flows; a signed-change specification would be a useful extension for future work but is outside the scope of the current tests. [18]

We estimate this using ordinary least squares (OLS) and weighted least squares (WLS) with weights equal to pre-period trade value, to reflect the greater economic weight of larger industries. [18] The WLS specification reduces the influence of small industries with noisy changes and is arguably more policy-relevant given trade-weighted importance. The weighting choice reflects both statistical and substantive considerations. Statistically, trade values vary widely across industries, producing heteroskedastic residuals in unweighted models; WLS partially addresses this by giving more weight to industries with more stable, higher-volume trade series. [18] Substantively, a given percentage adjustment in a large industry corresponds to much larger dollar magnitudes than the same adjustment in a small industry. [18] For transparency, we report both OLS and WLS to show how results differ when the unit of analysis is treated as industry counts versus trade-weighted importance. [18]

To test H1 and H2, we extend the model by adding exposure and rigidity controls:

abs_log_change_i = alpha + beta * dem_share_i + gamma * exposure_share_i + delta * rigidity_i + epsilon_i

These models are run separately for imports and exports and across multiple time windows. [18]

### 4.2 Panel fixed effects

We complement cross-sectional changes with a panel fixed-effects model that uses monthly data and a post indicator. The specification is:

log(value_it) = alpha_i + mu_t + beta * (dem_share_i * post_t) + epsilon_it

where alpha_i captures industry fixed effects and mu_t captures month (and in some specifications year) fixed effects. [18] The key coefficient beta tests whether Democratic-leaning industries experienced different post-period shifts relative to Republican-leaning industries, controlling for time-invariant industry characteristics and common temporal shocks.
The post indicator is defined in two ways for robustness: a post period beginning in July 2018 to capture the initial Section 301 lists, and a post period beginning in January 2019 to test sensitivity to delayed adjustment. [18] This mirrors the cross-sectional windows and ensures that the panel model is not overly dependent on a specific cutoff. [18]

### 4.3 Event-study interactions

To test pre-trend assumptions (H5), we estimate event-study interactions between dem_share and year dummies, using a base year (2017 in the main panel; 2015 in the extended pre-period tests). [18] The coefficients indicate whether industries with different dem_share values were already trending differently before the tariff period. Significant pre-period coefficients undermine a causal interpretation of post-period effects.
To extend the pre-trend window, we also download 2012-2015 import and export series from the Census APIs and combine them with the 2016-2017 data. [12, 13, 18] This longer pre-period allows a more stringent test of whether dem_share is correlated with trade trends even before the tariff period. [18]

### 4.4 County exposure correlation (H6)

We compute county exposure to tariff-targeted industries by weighting each county's industry employment by the industry's exposure_share and aggregating across industries. We then correlate this county exposure measure with county dem_share. [18] This provides a descriptive check on whether tariff exposure is geographically aligned with partisan geography.

### 4.5 Estimation and inference

Given the small cross-sectional sample, we interpret p-values cautiously and focus on sign and consistency across specifications rather than single-point significance. For panel models, standard errors are clustered at the industry level to account for within-industry correlation over time. [18]

---

## 5. Results

### 5.1 Cross-sectional changes

The baseline cross-sectional tests (N = 25 NAICS-3 industries in the main windows) show that the dem_share coefficient is generally negative in exports and close to zero in imports. [18] In the primary 2016-2017 vs 2018-2019 window, the export WLS coefficient is negative and statistically significant, while the import WLS coefficient is negative but not robust across specifications. [18] This suggests that, in trade-weighted terms, Democratic-leaning industries experienced smaller export adjustments rather than larger ones, contrary to the initial hypothesis.
In terms of magnitude, the export WLS coefficient in the primary window is approximately -1.26 (p = 0.036), indicating that a higher dem_share is associated with a smaller absolute log adjustment in exports when weighting by pre-period trade value. [18] The comparable import WLS coefficient in the same window is about -0.44 (p = 0.033), but this effect is not stable across alternative windows and disappears in some specifications, suggesting that the import relationship is fragile. [18] These coefficients should be interpreted as descriptive associations rather than causal effects, especially given the small cross-sectional sample and the pre-trend evidence discussed below. [18]

These patterns persist when the post window is restricted to 2019 only. Export coefficients remain negative, and import coefficients remain small and insignificant. [18] In a 2016 vs 2018-2019 comparison, the import WLS coefficient becomes more negative and significant, but the export WLS coefficient is only marginal. [18] This sensitivity to window choice emphasizes the exploratory nature of the findings.

### 5.2 Exposure and rigidity controls

When exposure_share and rigidity are added (H1/H2), the export WLS dem_share coefficient remains negative and statistically significant in the 2016-2017 vs 2018-2019 window. [18] The exposure_share coefficient is also negative and significant, indicating that more exposed industries show smaller export adjustments, and rigidity is negative and significant, implying that industries with higher employment per establishment adjust less. [18]

By contrast, imports remain largely insignificant in these controlled specifications. [18]
In the controlled export WLS specification, the dem_share coefficient is -1.36 (p = 0.0126), exposure_share is -2.19 (p = 0.0496), and rigidity is -0.00162 (p = 0.0138). [18] These estimates imply that export adjustments are smaller in more exposed and more rigid industries, and that the negative dem_share association persists even after accounting for these controls. [18] Import specifications with the same controls show small and statistically insignificant coefficients, reinforcing the asymmetry between import and export responses. [18]

Notably, the simple correlations between dem_share and the two controls are close to zero (approximately 0.016 with exposure and 0.095 with rigidity), which suggests that dem_share is not merely a mechanical proxy for these variables. [18] Even so, the limited sample size means that multicollinearity and leverage points can still influence coefficient stability. [18] Taken together, these results suggest that export adjustments are more tightly linked to industry structure and exposure than import adjustments, and that any partisanship signal is more pronounced on the export side.

### 5.3 Panel fixed effects

Panel fixed-effects results (2,736 industry-month observations per specification) do not show statistically significant dem_share x post interactions for either imports or exports. [18] This indicates that, once industry fixed effects and common time shocks are controlled for, there is no robust evidence of differential post-tariff shifts by workforce partisanship.
For example, using a post period starting July 2018, the import interaction coefficient is approximately -0.126 (p = 0.637) and the export interaction coefficient is about -1.05 (p = 0.356). [18] Starting the post period in 2019 yields similarly insignificant estimates. [18] These results indicate that any cross-sectional association does not translate into a stable within-industry shift once fixed effects absorb time-invariant differences. [18]

### 5.4 Event studies and pre-trends

Event-study interactions reveal significant pre-period coefficients for exports. In the main 2016-2024 event study, 2016 interactions are significant for both imports and exports, indicating differential pre-period dynamics. [18] In the extended 2012-2017 pre-trend check, export interactions for 2014 and 2017 are negative and significant. [18] These patterns suggest that export trends differed by dem_share even before the tariff period, undermining a causal interpretation of the cross-sectional post-period results.
The pre-trend violations are especially salient for exports: in the 2012-2017 pre-period event study, the 2014 interaction is about -0.74 (p = 0.006) and the 2017 interaction is about -1.26 (p = 0.029). [18] These estimates imply that higher dem_share industries were already on different export trajectories before the tariff window, which weakens the causal interpretation of post-2018 differences. [18]

### 5.5 County exposure correlation

County exposure to tariff-targeted industries is weakly negatively correlated with Democratic vote share (corr = -0.0658). [18] The magnitude is small, suggesting that tariff exposure is not strongly aligned with partisan geography at the county level, though the direction is consistent with the idea that more Republican-leaning counties may be slightly more exposed.

---

## 6. Robustness and Complementary Analyses

Robustness checks extend the core analysis along four dimensions: timing, outcome definition, weighting, and outlier sensitivity. First, alternative pre/post windows confirm that export coefficients remain negative in trade-weighted specifications but vary in statistical significance, while import coefficients are unstable and sensitive to the window choice. [18, 19] Second, alternative outcome constructions (signed log change vs absolute log change; mean vs median pre/post aggregation) preserve the negative sign for exports in most trade-weighted models, but the magnitude and significance weaken in median-based specifications, and import results remain inconsistent. [19]

Third, weighting and robust estimation matter. When weights are based on employment rather than trade value, export coefficients attenuate and lose statistical significance, suggesting that the relationship is concentrated in trade-heavy industries rather than broad employment exposure. [19] Robust regression (Huber) and winsorization also reduce the export coefficient in the main 2016-2017 vs 2018-2019 window, indicating sensitivity to influential observations and tail behavior in the cross-section. [19] Fourth, leave-one-out diagnostics show that export coefficients remain negative across exclusions but can shrink substantially when specific industries are omitted (notably NAICS 211), highlighting the small-sample leverage risk. [19]

The exposure and rigidity controls provide additional context. Exposure_share is consistently negative in export regressions, consistent with more heavily targeted industries showing smaller export adjustments, which could reflect either policy cushioning or offsetting strategies by firms. [18] Rigidity is also negative in export models, suggesting that industry structure matters for adjustment capacity. [18]

Taken together, these robustness checks temper any strong interpretation of the dem_share coefficient. The sign is fairly consistent for exports in trade-weighted specifications, but the evidence is sensitive to weighting choices, outlier treatment, and pre-trend violations, pointing to the need for richer identification strategies or firm-level data in future work. [18, 19]

---

## 7. Discussion

The theoretical literature provides competing expectations for how political alignment should map onto trade responses. If trade politics are factor-based, workforce partisanship could be a proxy for underlying factor ownership and thus for trade preferences; if trade politics are industry-based, the alignment could reflect specific exposure and lobbying incentives. [8-11] The empirical results here are more consistent with the industry-based view, insofar as exposure and rigidity appear to explain a portion of export adjustments, while the partisanship proxy is not robust once panel controls and pre-trends are considered. [18]

The trade-war incidence literature also suggests that adjustments are driven by economic mechanisms that need not align with partisan identity. Studies of the 2018-2019 tariff shocks show substantial pass-through to U.S. prices and reductions in trade flows, implying that cost shocks, input substitution, and retaliation can dominate firm and industry responses. [1-4] In that setting, a workforce partisanship proxy may correlate with sectoral characteristics (tradability, capital intensity, supply-chain structure) rather than directly capturing political alignment, which is consistent with the ambiguity highlighted in factor-based and specific-factors theories. [8-11]

The negative export association in weighted cross-sections is intriguing and counter to the initial hypothesis. One possible interpretation is that Democratic-leaning industries are more concentrated in sectors with lower direct exposure to export shocks or stronger supply-chain cushioning. Another possibility is that the dem_share proxy is capturing structural industry composition rather than political alignment per se. The trade-policy literature emphasizes that political outcomes can be driven by organized interests, not just voter preferences. [6] If lobbying and organizational capacity dominate, industry structure (rigidity, exposure) could matter more than partisan composition.

The results also align with the idea that political targeting matters at the policy stage but does not necessarily translate into measurable differences in trade-flow adjustment by industry. [5] The slight negative county exposure correlation suggests that tariff-targeted industries are not sharply clustered in Democratic counties, limiting the geographic partisan signal. [18]

Overall, the analysis suggests that workforce partisanship is, at best, an indirect proxy for trade-policy alignment. Industry exposure and structure appear to explain more variation in responses, and the remaining partisanship signal is unstable. These findings point to the need for more precise political measures (e.g., firm-level political contributions, unionization rates, or occupation-level voting data) and more granular trade data.

---

## 8. Limitations

Several limitations are substantial. First, the partisanship proxy relies on county-level vote shares and 2020 employment weights, which introduces measurement error and temporal mismatch. [16, 17] Second, the NAICS-3 aggregation obscures heterogeneity within industries and may dilute true signals. [12, 13] Third, exposure_share captures only Section 301 tariffs and does not represent the full trade-policy landscape or downstream input exposure. [14]

Fourth, the small cross-sectional sample (about 25 NAICS-3 industries) limits statistical power and increases sensitivity to outliers. [18] Fifth, pre-trend violations in exports weaken causal claims; the results are best interpreted as descriptive correlations rather than evidence of tariff-induced partisan effects. [18]

Robustness checks reinforce the leverage concern: outlier treatment and leave-one-out exclusions can materially change export coefficients in the main window. [19] Finally, the analysis does not model endogeneity in policy design or industry behavior. Political coalitions may influence tariff targeting and responses simultaneously, and the models here do not disentangle those dynamics. The panel and event-study structures help illuminate timing but do not fully address these concerns. [18]

---

## 9. Conclusion

This paper tests whether workforce partisanship predicts industry-level trade responses to U.S. tariffs in 2018-2019. The analysis combines Census trade data, a novel partisanship proxy, and tariff exposure mappings to estimate cross-sectional, panel, and event-study models. The key empirical finding is a negative association between Democratic workforce share and export response magnitude in weighted cross-sections, alongside non-significant panel effects and pre-trend violations that undermine causal interpretation. [18]

The broader implication is that political alignment at the industry-workforce level does not yield a consistent, robust predictor of trade adjustment in this setting. Theoretical frameworks suggest multiple competing channels, and the data do not decisively support the initial hypothesis. Future research should incorporate more granular political measures and explore firm-level adjustment to tariffs, which may capture political alignment more directly than county-weighted employment proxies. [6-11]

The paper's primary contribution is methodological: it documents a transparent pipeline for combining trade flows, tariff exposure, and political measures at the industry level, and it provides a structured empirical test that can be extended with richer data. [12-18]

---

## Data Availability

All analytical outputs referenced in this paper are stored in `papers/2026/industry-responses-to-tariffs/data/analysis_ready/` under `hypothesis_full` and `hypothesis_1_2_5_6`, and additional robustness outputs are stored in `papers/2026/industry-responses-to-tariffs-partisanship/data/robustness/`. [18, 19]

---

## References

Full citations for numbered references are listed in `papers/2026/industry-responses-to-tariffs-partisanship/sources.md` per project policy.

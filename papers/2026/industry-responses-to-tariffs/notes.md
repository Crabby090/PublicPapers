# Notes

## Research log
- 2026-01-15: Initialized paper.
- 2026-01-15: Downloaded literature PDFs (NBER working papers on tariffs and washing machines) and compiled quantitative datasets (QuantGov 301/232, BIS 232 exclusions extract, USITC HTS CSVs, Census trade time series). Added new sources and claims.
- 2026-01-15: Standardized quantitative datasets into `data/processed/` and added regeneration script `data/prepare_quant_data.py`.
- 2026-01-15: Consolidated analysis-ready datasets into `data/analysis_ready/` and generated QA summaries.
- 2026-01-15: Added exports-by-NAICS (3-digit) via Census API and built a county-to-industry partisanship proxy using CBP county employment and MIT Election Lab county presidential returns.
- 2026-01-15: Ran exploratory hypothesis test linking partisanship to trade response magnitude; exports show a negative association (opposite of hypothesis) in this quick cut, imports show no significant relationship.
- 2026-01-15: Collected official federal communications on reciprocal tariffs (White House EOs/fact sheets, GovInfo FR/DCPD records, CBP CSMS guidance, joint statements) and archived Truth Social posts; downloaded to data/sources/ and logged in sources.md/claims.csv.
- 2026-01-15: Conducted full DHA analysis on corpus. See analysis below.
- 2026-01-15: Completed literature review. Identified 16 relevant academic sources [63-78] on Trump trade discourse, DHA methodology, and securitization. Key gap identified: no prior comprehensive DHA of 2025 reciprocal tariff discourse across multiple genres.
- 2026-01-15: Drafted working paper (~5,500 words). Title: "A Beautiful Thing to Behold: The Discursive Construction of Reciprocity in U.S. Tariff Policy (2025)".
- 2026-01-15: Added 5 CDS journal anchoring papers [79-83] (Forchtner, Guardino, Krzyżanowski x2, Wodak). Revised paper for CDS style: expanded theoretical engagement, added reflexivity section, integrated CDS citations, converted to prose-heavy format.

## Decisions
- Kept existing 2025 tariff discourse corpus sources intact; appended new quantitative/literature sources after them.
- Processed outputs stored as compressed CSVs; column names normalized to snake_case and codes preserved as strings.

## TODO
- Attempt OpenICPSR downloads for data replication packages (Cloudflare blocked automated download).
- Decide whether to keep Boston Fed WP 19-12 as separate source or rely on the NBER version (same authors).
- If exports-by-NAICS data is needed, request via Census API in smaller NAICS batches or use alternative export datasets.
- Verify BIS public-extract parsing quality for any tables where raw_lines >> rows (see `data/processed/bis232/bis232_manifest.csv`).

## Data inventory (downloaded)
- data/literature/: NBER working papers w25638, w25672, w26610, w26396, w25767; Boston Fed WP 19-12.
- data/quant/: QuantGov Section 301/232 tariff ZIPs; BIS Section 232 public extract ZIP; USITC HTS CSVs (2019 Rev 20, 2020 Rev 18); Census trade time series CSVs (imports NAICS 2016-2024; imports/exports end-use 2016-2024).

## Data inventory (processed)
- data/processed/quantgov/: Section 301 lists + exclusion requests; Section 232 microdata (v1) + merged portal data (v3).
- data/processed/bis232/: BIS public extract tables + manifest.
- data/processed/usitc/: HTS 2019/2020 plus combined.
- data/processed/census/: Imports NAICS and end-use trade series (imports+exports combined).

## Data inventory (analysis-ready)
- data/analysis_ready/: cleaned and consolidated datasets for quant analysis, plus `qa_summary.csv` and `qa_report.md`.
- data/analysis_ready/census_exports_naics_3digit_clean.csv.gz: exports by 3-digit NAICS (2016-2024).
- data/analysis_ready/county_partisanship_2016_2020.csv and industry_partisanship_naics3.csv: partisanship proxy inputs/outputs.

---

# Literature Review: Trump Tariff Discourse in Academic Research

## Summary
A systematic literature search identified **16 relevant academic sources** [63-78] examining Trump's trade rhetoric from discourse analysis, political communication, and international relations perspectives. Key findings below.

## Prior Discourse Analysis of Trump Trade Rhetoric

### Direct Predecessors (Most Relevant)

**1. "I Am a Tariff Man" (Di Tella & Rodrik, 2019) [63]**
- Uses ideational approach to populism examining Trump's Twitter during 2018 steel/aluminum tariffs
- Finds populist foreign policy themes generate polarized social networks along elite-vs-people divide
- **Gap our study addresses**: Limited to first Trump term and social media only; no systematic DHA framework

**2. "Reframing China in U.S. Trade Policy Discourse" (Hu & Li, 2025) [64]**
- Uses CDA with van Dijk's Context Model and Chilton's Deictic Space Theory
- Analyzes 2017-2019 Trade Policy Agendas; shows China reframed from "distant partner" to "proximate adversary"
- China-related content grew from 4.4% (2017) to 17.8% (2019) of agenda word count
- WTO systematically marginalized through backgrounding techniques
- **Gap**: Focused on written policy agendas only; does not analyze EOs, social media, or multi-genre discourse

**3. "Expert Perspectives on Trump's Tariff Negotiations" (Smolinski et al., 2025) [65]**
- Multi-expert analysis of April 2025 "Liberation Day" tariffs from negotiation theory perspective
- Identifies: deceptive rhetoric (distorted trade deficit claims), zero-sum framing, performative negotiation
- Notes Trump framed EU as "illegitimate beneficiary" and celebrated symbolic victories as "historic"
- **Gap**: Negotiation focus rather than discourse analysis; does not apply systematic CDA/DHA categories

### Methodological Foundations

**4. Reisigl & Wodak's DHA (2009) [67]**
- Foundational text establishing five discursive strategies and eight-stage research programme
- Our study directly applies this methodology

**5. van Dijk's Ideological Square [68]**
- Framework for analyzing positive self-representation/negative other-representation
- Our analysis applies this to identify US/THEM polarization in tariff discourse

**6. Wodak's "Politics of Fear" (2015) [69]**
- Applies DHA to right-wing populist rhetoric across Europe
- Provides template for analyzing nomination, predication, argumentation strategies
- Our study extends this framework to trade policy discourse specifically

### Political Economy and Policy Context

**7. "The Flawed Rationale Behind America's Reciprocal Tariffs" (Grossman & Sykes, 2025) [66]**
- Princeton/Stanford economists critique the substantive claims in EO 14257
- Argues trade deficit growth is modest (3.98% → 4.16% GDP); cause-effect logic flawed
- Questions legitimacy of IEEPA emergency powers invocation
- **Relevance**: Provides expert counter-discourse to administration framing

**8. "Tariffs and Politics" (Fajgelbaum & Khandelwal, 2021) [70]**
- Evidence that retaliatory tariffs were politically targeted to hurt Trump
- China emphasized political targeting; EU balanced targeting with economic damage minimization
- **Relevance**: Shows political calculus in tariff discourse is recognized internationally

**9. CEPR "Great Trade Hack" (2025) [71]**
- Introduces "Grievance Doctrine" concept - emotionally coherent but economically incoherent
- Strategic disorder as signaling mechanism ("appearing ready to walk away")
- **Relevance**: Provides macro-level interpretation of discourse patterns we identify

### Populism and Foreign Policy Rhetoric

**10. "A Populist Grand Strategy?" (Biegon, 2019) [72]**
- Trump's Jacksonian ideological approach: nationalism, mercantilism, coercive power
- Declinist framing positions US as victim requiring corrective action
- **Relevance**: Our DHA findings on victimization narrative align with this analysis

**11. "Populism and Trump's Foreign Policy" (Lacatus, 2021) [73]**
- Content analysis of tweets and rally speeches
- Documents anti-multilateralism, departure from liberal international order
- **Gap**: Does not systematically analyze trade policy discourse

**12. "Populism, Securitization, and 'America First'" (Wang, 2017) [78]**
- Links populism, securitization theory, and foreign policy
- Directly relevant to our finding that tariffs are securitized as national emergency
- **Gap**: Published before 2025 tariffs; theoretical rather than empirical

### Public Opinion and Reciprocity

**13. "Public Responses to Foreign Protectionism" (Woo & Lee, 2022) [77]**
- Survey experiments show US protectionism reduces support for trade among Chinese citizens
- Identifies "direct reciprocity" (retaliate against US) and "generalized reciprocity" (reduce trade support broadly)
- **Relevance**: Shows how reciprocity frame is interpreted by target audiences

**14. "Ambiguous Impact of Populist Trade Discourses" (Heiduk & Ebert, 2024) [76]**
- Trade as "floating signifier" in populist discourse
- Ambiguity allows different constituencies to interpret policy differently
- **Relevance**: Helps explain how "reciprocal tariffs" can be read as both protectionist and free-trade-promoting

## Research Gap Our Study Addresses

**No prior study has**:
1. Applied full DHA methodology to the 2025 "Liberation Day" reciprocal tariffs
2. Analyzed multi-genre corpus (EOs, Fact Sheets, Truth Social, CBP guidance, Joint Statements)
3. Systematically mapped all five discursive strategies across the corpus
4. Identified "reciprocity" as master topos unifying the discourse
5. Traced register/genre variation in how the same policy is framed for different audiences

**Our contribution**: First comprehensive DHA of the 2025 tariff discourse, demonstrating how the frame of "reciprocity" functions as ideological legitimation across institutional settings.

---

# DHA Analysis: U.S. Government Tariff Discourse (2025)

## Research Question
**How does the American government discursively justify its 2025 tariff policies?**

---

## 1. CONTEXTUAL ANALYSIS

### 1.1 Socio-Historical Context (Level 4)

The 2025 tariff policy emerges within a specific historical trajectory:

1. **Post-war trade consensus (1947-2016)**: The discourse explicitly positions itself against what it terms "three incorrect assumptions" of the post-war system:
   > "the post-war international economic system was based upon three incorrect assumptions: first, that if the United States led the world in liberalizing tariff and non-tariff barriers the rest of the world would follow; second, that such liberalization would ultimately result in more economic convergence... third, that as a result, the United States would not accrue large and persistent goods trade deficits." [EO 14257]

2. **Trump 1.0 tariffs (2018-2020)**: The discourse references continuity: "Both my first Administration in 2017, and the Biden Administration in 2022, recognized that increasing domestic manufacturing is critical to U.S. national security." [EO 14257]

3. **The "national emergency" declaration (April 2, 2025)**: This is the pivotal discursive move - framing trade deficits not as economic policy but as security crisis requiring emergency powers.

### 1.2 Institutional Context (Level 3)

The corpus spans multiple institutional settings, each with distinct genre conventions:

| Source | Institution | Genre | Register |
|--------|-------------|-------|----------|
| Executive Orders | White House/Federal Register | Legal-bureaucratic | Formal, dense, legal citations |
| Fact Sheets | White House | Public relations | Promotional, accessible, bullet points |
| Truth Social | President (personal) | Social media | Populist, affective, informal |
| CSMS Guidance | CBP | Administrative | Technical, procedural, neutral |
| Joint Statements | White House/State | Diplomatic | Cooperative, balanced |

### 1.3 Intertextual Relations (Level 2)

Key intertextual chains:
- EO 14257 → Fact Sheet → Truth Social posts (same day, April 2)
- EO 14257 → CBP CSMS 64649265 (implementation guidance, April 4)
- China escalation: EO 14257 → EO 14259 → EO 14266 → April 9 Statement (125%)
- De-escalation: Geneva Joint Statement (May 12) → subsequent modifications

---

## 2. NOMINATION STRATEGIES

### 2.1 Naming the In-Group: "Americans" and "America"

The discourse constructs a unified American identity as victim and beneficiary:

**Collective possessives:**
- "our manufacturing base" [EO 14257, passim]
- "our trading partners" [EO 14257, passim]
- "our defense-industrial base" [EO 14257]
- "our country's large and persistent annual trade deficits" [EO 14257]

**Workers as sympathetic category:**
- "hardworking Americans" [Fact Sheet, April 2]
- "American workers" [EO 14257, Fact Sheet]
- "the workers here in America" [Truth Social, April 7 - quoted]
- "Main Street, not Wall Street" [Truth Social, April 8]
- "the middle class, not the political class" [Truth Social, April 8]

**Evidence from April 8 Truth Social:**
> "I'm proud to be the President for the workers, not the outsourcers; the President who stands up for Main Street, not Wall Street; who protects the middle class, not the political class; and who defends America, not trade cheaters all over the globe."

This passage demonstrates classic populist nomination: workers/Main Street/middle class (good, protected) vs. outsourcers/Wall Street/political class/trade cheaters (bad, opposed).

### 2.2 Naming the Out-Group: Trading Partners as Adversaries

The discourse employs a graduated scale of hostility in naming foreign actors:

**Neutral to negative gradient:**
1. "trading partners" (neutral, frequent in EOs)
2. "foreign firms" (competitive, neutral)
3. "key trading partners" (implies significance, not necessarily hostile)
4. "non-market economies like China" (delegitimizing, implies unfairness)
5. "foreign adversaries" (explicit hostility)

**China as special case - intensified hostility:**
- "the biggest abuser of them all, China" [Truth Social, April 7]
- "abusing countries" [Truth Social, April 7]
- "China, whose markets are crashing" [Truth Social, April 7]
- "ripping off the U.S.A." [April 9 Statement]

**Evidence from April 9 Statement:**
> "Based on the lack of respect that China has shown to the world's markets, I am hereby raising the tariff charged to China by the United States of America to 125 percent, effective immediately. At some point—hopefully, in the near future—China will realize that the days of ripping off the U.S.A. and other countries is no longer sustainable or acceptable."

Key nomination strategies here:
- "lack of respect" (moral framing)
- "ripping off" (criminal metaphor)
- "the U.S.A." (patriotic formulation)

### 2.3 Naming the Policy: "Reciprocal Tariffs"

The policy itself is named strategically:

**Primary naming:** "Reciprocal Tariff" - appears in official title of EO 14257
- This frames the action as response, not aggression
- Implies prior non-reciprocity by others
- Invokes justice/fairness semantics

**Alternative namings:**
- "additional ad valorem duty" (technical, CBP guidance)
- "trade remedy" (bureaucratic framing in CBP: "Questions... should be directed to Trade Remedy")
- "tariffs" (direct term in Truth Social)

**Metaphorical naming:**
- "a beautiful thing to behold" [Truth Social, April 6]
- "beautiful and efficient process" [Truth Social, April 8]

### 2.4 Strategic Silences

Notable absences in nomination:
- Consumers are rarely named (the discourse is producer/worker-focused)
- Specific U.S. industries harmed by tariffs are not named
- Price increases are not discussed
- The term "protectionism" is never used (avoided in favor of "reciprocity")

---

## 3. PREDICATION STRATEGIES

### 3.1 Predicating the Trade Deficit

The trade deficit is predicated as existential threat:

**Crisis predicates:**
- "unsustainable crisis" [Fact Sheet, April 2]
- "unusual and extraordinary threat to the national security and economy" [EO 14257]
- "national emergency" [EO 14257, Fact Sheet]

**Evidence from EO 14257:**
> "I, DONALD J. TRUMP, President of the United States of America, find that underlying conditions, including a lack of reciprocity in our bilateral trade relationships, disparate tariff rates and non-tariff barriers, and U.S. trading partners' economic policies that suppress domestic wages and consumption, as indicated by large and persistent annual U.S. goods trade deficits, constitute an unusual and extraordinary threat to the national security and economy of the United States."

**Damage predicates (effects attributed):**
- "hollowing out of our manufacturing base" [EO 14257]
- "inhibited our ability to scale" [EO 14257]
- "undermined critical supply chains" [EO 14257]
- "rendered our defense-industrial base dependent on foreign adversaries" [EO 14257]
- "atrophy of domestic production capacity" [EO 14257]
- "compromised military readiness" [EO 14257]

**Social harm predicates:**
- "decline in rates of family formation" [EO 14257]
- "the rise of... the abuse of opioids" [EO 14257]

This last predication is remarkable - it explicitly links trade deficits to the opioid crisis, extending economic harm into social/moral harm.

### 3.2 Predicating Other Countries

**Negative predicates for trading partners:**
- "non-reciprocal" [passim]
- "unfair" [passim]
- "abusing" [Truth Social]
- "taking advantage" [Truth Social, April 7]
- "got rich over the backs of the workers here in America" [Truth Social, April 7 - quoted]

**Predicates specifically for China:**
- "lack of respect" [April 9 Statement]
- "ripping off" [April 9 Statement]
- "the biggest abuser" [Truth Social, April 7]
- "whose markets are crashing" [Truth Social, April 7]

**Predicates for compliant countries:**
- "have not... retaliated" [April 9 Statement] - rewarded with pause
- Over 75 countries "called representatives" to negotiate [April 9 Statement]

### 3.3 Predicating Tariffs and the Policy

**Positive predicates:**
- "beautiful thing to behold" [Truth Social, April 6]
- "beautiful and efficient process" [Truth Social, April 8]
- "a cornerstone of his campaign from the start" [Fact Sheet, April 2]
- "historic action" [Truth Social, April 8 - re: coal, similar framing]

**Functional predicates:**
- "bringing in Billions of Dollars a week" [Truth Social, April 7]
- "the only way this problem can be cured" [Truth Social, April 6]

**Evidence from April 6 Truth Social:**
> "We have massive Financial Deficits with China, the European Union, and many others. The only way this problem can be cured is with TARIFFS, which are now bringing Tens of Billions of Dollars into the U.S.A. They are already in effect, and a beautiful thing to behold."

### 3.4 Predicating U.S. Market Access

**Key predication - access as privilege:**
> "Access to the American market is a privilege, not a right." [Fact Sheet, April 2]

This single sentence encapsulates a fundamental ideological position - reframing market access from mutual benefit to unilateral grant.

---

## 4. ARGUMENTATION STRATEGIES

### 4.1 Topos of Threat/Danger (National Emergency)

**Warrant structure:** If something constitutes a threat to national security, extraordinary measures are justified.

**Evidence from EO 14257:**
> "I hereby declare a national emergency with respect to this threat... conditions reflected in large and persistent annual U.S. goods trade deficits... have grown by over 40 percent in the past 5 years alone, reaching $1.2 trillion in 2024."

The securitization move is crucial - by invoking IEEPA (International Emergency Economic Powers Act), the discourse transforms economic policy into security response.

**Explicit security claims:**
- "our defense-industrial base dependent on foreign adversaries" [EO 14257]
- "compromised military readiness" [EO 14257]
- "U.S. stockpiles of military goods are too low" [EO 14257]
- "the recent rise in armed conflicts abroad" [EO 14257]

### 4.2 Topos of Reciprocity/Justice (Master Topos)

**Warrant structure:** If we treat others fairly, they should treat us fairly; if they don't, we may respond in kind.

This is the **master topos** of the discourse, appearing in the very title of EO 14257: "Reciprocal Tariff to Rectify Trade Practices."

**Key formulations:**
> "the first President in modern history to stand strong for hardworking Americans by asking other countries to follow the golden rule on trade: Treat us like we treat you." [Fact Sheet, April 2]

> "the principle of reciprocity" [EO 14257] - invoked as historical U.S. policy from 1934

**Contrastive structure:**
- U.S. tariffs: "among the lowest simple average MFN tariff rates in the world at 3.3 percent" [EO 14257]
- Others: Brazil (11.2%), China (7.5%), EU (5%), India (17%), Vietnam (9.4%) [EO 14257]

The argument is: We play fair, they don't, therefore we're justified in responding.

### 4.3 Topos of Numbers/Statistics

**Warrant structure:** If the numbers show X, we should conclude X.

The discourse is saturated with quantitative claims:

**Trade deficit figures:**
- "$1.2 trillion in 2024" [EO 14257]
- "grown by over 40 percent in the past 5 years" [EO 14257]
- "$1.9 trillion" [Truth Social, April 7 - note: larger figure]
- "$49 billion annual agricultural trade deficit" [EO 14257]

**Comparative tariff rates (examples):**
- U.S. passenger vehicles: 2.5% vs. EU: 10%, India: 70%, China: 15% [EO 14257]
- U.S. apples: 0% vs. Turkey: 60.3%, India: 50% [EO 14257]

**Employment figures:**
- "5 million manufacturing jobs" lost 1997-2024 [EO 14257]
- "every manufacturing job spurs 7 to 12 new jobs" [EO 14257]

**Revenue projections:**
- "bringing in Billions of Dollars a week" [Truth Social, April 7]
- "Tens of Billions of Dollars" [Truth Social, April 6]

### 4.4 Topos of History/Lessons of the Past

**Warrant structure:** If history teaches us X, we should apply X to the present.

**Historical narrative in EO 14257:**
> "For decades starting in 1934, U.S. trade policy has been organized around the principle of reciprocity. The Congress directed the President to secure reduced reciprocal tariff rates... Between 1934 and 1945, the executive branch negotiated and signed 32 bilateral reciprocal trade agreements... After 1947 through 1994, participating countries engaged in eight rounds of negotiation..."

The narrative presents:
1. Original commitment to reciprocity (1934)
2. Gradual erosion of that principle
3. Current policy as restoration

**From Truth Social (April 7):**
> "The United States has a chance to do something that should have been done DECADES AGO."

### 4.5 Topos of Advantage/Usefulness

**Warrant structure:** If action X produces benefits, do X.

**Claimed benefits:**
- Revenue: "bringing Tens of Billions of Dollars into the U.S.A." [Truth Social, April 6]
- Jobs: "better-paying American jobs" [Fact Sheet, April 2]
- Manufacturing: "re-shore manufacturing" [Fact Sheet, April 2]
- Investment: "President Trump has secured more private investment in his first 11 weeks than Biden secured over his ENTIRE first term" [Truth Social, April 7]

### 4.6 Topos of Authority

**Warrant structure:** If authority X says/permits Y, Y is legitimate.

**Legal authority claims:**
- IEEPA (50 U.S.C. 1701 et seq.) [EO 14257]
- National Emergencies Act (50 U.S.C. 1601 et seq.) [EO 14257]
- Trade Act of 1974, section 604 [EO 14257]
- Presidential constitutional authority [EO 14257]

**Expert authority (quoted):**
- "according to the WTO" [EO 14257]
- "According to 2023 United Nations data" [EO 14257]
- Stuart Varney: "I've been doing this for 50 years" [Truth Social, April 11]

---

## 5. PERSPECTIVIZATION STRATEGIES

### 5.1 Presidential Voice and Authority

**First-person singular (formal):**
> "I, DONALD J. TRUMP, President of the United States of America, find that..." [EO 14257]

This formulaic opening asserts maximum presidential authority.

**First-person singular (informal, Truth Social):**
> "I just had a great call with the Acting President of South Korea..." [April 8]
> "I let them know that, I AM FOR MAJOR SPENDING CUTS!" [April 8]

### 5.2 Collective "We" and Inclusive Deixis

**Inclusive national "we":**
- "our manufacturing base"
- "our trading partners"
- "our country"
- "We are doing really well on our TARIFF POLICY" [Truth Social, April 11]

**Strategic "we" shifts:**
- "We" = the administration: "We're managing a massive amount of requests for negotiations" [Truth Social, April 8 - quoted]
- "We" = Americans: "We have massive Financial Deficits" [Truth Social, April 6]

### 5.3 Reported Speech and Quotation

**Truth Social extensively uses reported speech:**
- Supportive quotes are amplified (often in quotation marks)
- Critics are not directly quoted

**Examples of reported speech on Truth Social (April 7):**
> "This is balancing our economy with countries that have taken advantage of us... I applaud the President (Trump) for having a backbone…"

> "I appreciate what the President is doing on tariffs... the ranchers of Wyoming are saying thank you Mr. President, it is about time!"

**Function:** Democratizes support (voices of "ordinary Americans" endorse policy)

### 5.4 Deictic Positioning: Here/There, Now/Then

**Temporal deixis:**
- "now" = time of action, correction
- "for decades" = time of abuse, neglect
- "should have been done DECADES AGO" [Truth Social, April 7]

**Spatial deixis:**
- "the United States" vs. "other countries"
- "domestic" vs. "foreign"
- "here in America" [Truth Social, April 7]

---

## 6. INTENSIFICATION AND MITIGATION STRATEGIES

### 6.1 Intensification Devices

**Superlatives:**
- "the biggest abuser of them all" [Truth Social, April 7]
- "among the lowest simple average MFN tariff rates in the world" [EO 14257]

**Hyperbole:**
- "beautiful thing to behold" [Truth Social, April 6]
- "beautiful and efficient process" [Truth Social, April 8]
- "GREATNESS will be the result" [Truth Social, April 7]

**Capitalization (Truth Social register):**
- "TARIFFS"
- "DECADES AGO"
- "MAKE AMERICA GREAT AGAIN"
- "NOT SUSTAINABLE"
- "CHINA!!!"
- "GOD BLESS THE USA"

**Crisis vocabulary:**
- "national emergency"
- "unsustainable crisis"
- "unusual and extraordinary threat"
- "hollowing out"
- "atrophy"
- "compromised"

### 6.2 Mitigation Devices

Mitigation is notably **rare** in the corpus, appearing mainly in:

**Diplomatic Joint Statements:**
> "Recognizing the importance of their bilateral economic and trade relationship... Moving forward in the spirit of mutual opening, continued communication, cooperation, and mutual respect" [US-China Geneva Joint Statement, May 12]

**Conditional/hedge language (limited):**
- "hopefully, in the near future" [April 9 Statement re: China]
- "may further modify" [EO 14257 - re: tariff adjustments]

**The asymmetry is significant:** Intensification dominates the justificatory discourse; mitigation appears only in negotiation/deal-making contexts.

---

## 7. GENRE VARIATION ANALYSIS

### 7.1 Executive Order Register

**Features:**
- Formal legal citation ("By the authority vested in me...")
- Dense nominal phrases
- Passive constructions
- Extensive historical/legal background
- Section numbering

**Example (EO 14257):**
> "all articles imported into the customs territory of the United States shall be, consistent with law, subject to an additional ad valorem rate of duty of 10 percent."

### 7.2 Fact Sheet Register

**Features:**
- Bullet points
- Bold headers ("PURSUING RECIPROCITY TO REBUILD THE ECONOMY")
- Promotional framing
- Accessible vocabulary

**Example (April 2):**
> "President Trump refuses to let the United States be taken advantage of and believes that tariffs are necessary to ensure fair trade, protect American workers, and reduce the trade deficit—this is an emergency."

### 7.3 Truth Social Register

**Features:**
- First-person voice
- Capitalization for emphasis
- Exclamation marks
- Informal vocabulary ("Sleepy Joe Biden," "Good OL' USA")
- Reposted quotations
- Neologisms ("PANICAN")

**Example (April 7):**
> "Don't be Weak! Don't be Stupid! Don't be a PANICAN (A new party based on Weak and Stupid people!). Be Strong, Courageous, and Patient, and GREATNESS will be the result!"

### 7.4 CBP Guidance Register

**Features:**
- Technical terminology (HTSUS, ad valorem, Chapter 99)
- Procedural instructions
- Neutral tone
- No evaluative language

**Example (CSMS 64649265):**
> "filers must report at least one Harmonized Tariff Schedule of the United States (HTSUS) Chapter 99 secondary classification related to the reciprocal tariffs."

### 7.5 Joint Statement Register

**Features:**
- Diplomatic formulae ("Recognizing the importance...")
- Balanced attribution to both parties
- Mitigation through hedging
- Absence of accusatory language

**Example (US-China Geneva):**
> "The Parties commit to take the following actions... The United States will (i) modify... China will (i) modify accordingly..."

---

## 8. SYNTHESIS: THE DISCURSIVE CONSTRUCTION OF "RECIPROCITY"

### 8.1 Central Finding

The discourse constructs tariffs as **just response** rather than protectionist aggression through the master frame of "reciprocity." This operates through:

1. **Historical legitimation:** Reciprocity framed as original American trade principle (1934)
2. **Victimization narrative:** U.S. as taken advantage of, "ripped off"
3. **Moral framing:** "Golden rule" language transforms economic policy into ethical imperative
4. **Securitization:** Trade deficit as national emergency requiring emergency powers

### 8.2 The Ideological Square (Van Dijk)

The discourse exhibits clear us/them polarization:

| | EMPHASIZED | DE-EMPHASIZED |
|---|---|---|
| **US (America)** | Victim of unfair trade, hardworking, played by the rules | Consumer harm, price increases, industry disruption |
| **THEM (Trading partners)** | Unfair practices, abuse, non-reciprocal | Legitimate interests, supply chain benefits |

### 8.3 Genre as Strategic Resource

The same policy is framed differently across genres:
- **EOs**: Legal necessity, national security
- **Fact Sheets**: Economic benefit, worker protection
- **Truth Social**: Populist victory, personal achievement
- **Joint Statements**: Mutual cooperation, win-win

---

## 9. CRITICAL OBSERVATIONS

### 9.1 Text-Immanent Critique (Internal Contradictions)

1. Tariffs framed as both "emergency" response AND "beautiful thing" / campaign fulfillment
2. "Reciprocity" language while imposing unilateral action
3. Claims of "billions" in revenue while denying consumer harm
4. Emergency powers invoked for pre-planned campaign promise

### 9.2 Socio-Diagnostic Critique (Ideological Functions)

1. **Naturalization of protectionism:** "Reciprocal" framing obscures protectionist character
2. **Securitization of trade:** Transforms economic policy into security necessity
3. **Populist displacement:** Directs economic anxiety toward foreign actors
4. **Presidential aggrandizement:** Positions Trump as singular defender

### 9.3 Absences and Silences

What the discourse does NOT address:
- Consumer price impacts
- Supply chain disruption for U.S. businesses
- Retaliatory costs
- Economic literature on tariff incidence
- Alternative policy approaches
- Distributional effects

---

## 10. KEY EVIDENCE SUMMARY TABLE

| Strategy | Source | Quote |
|----------|--------|-------|
| Nomination (in-group) | Truth Social, April 8 | "President for the workers, not the outsourcers; Main Street, not Wall Street" |
| Nomination (out-group) | April 9 Statement | "ripping off the U.S.A." |
| Predication (deficit) | EO 14257 | "unusual and extraordinary threat to the national security" |
| Predication (tariffs) | Truth Social, April 6 | "a beautiful thing to behold" |
| Predication (access) | Fact Sheet, April 2 | "Access to the American market is a privilege, not a right" |
| Argumentation (threat) | EO 14257 | "I hereby declare a national emergency" |
| Argumentation (reciprocity) | Fact Sheet, April 2 | "the golden rule on trade: Treat us like we treat you" |
| Argumentation (numbers) | EO 14257 | "$1.2 trillion in 2024... grown by over 40 percent" |
| Argumentation (history) | EO 14257 | "For decades starting in 1934, U.S. trade policy has been organized around the principle of reciprocity" |
| Perspectivization | EO 14257 | "I, DONALD J. TRUMP, President of the United States of America, find that..." |
| Intensification | Truth Social, April 7 | "DECADES AGO... Don't be Weak! Don't be Stupid!" |
| Mitigation | Geneva Joint Statement | "Moving forward in the spirit of mutual opening, continued communication, cooperation, and mutual respect" |

---

## CORPUS INVENTORY

| Genre | Count | Key Documents |
|-------|-------|---------------|
| Executive Orders | ~12 | EO 14257 (April 2), EO 14259, EO 14266, EO 14346, EO 14360 |
| Fact Sheets | 6 | April 2 National Emergency, May 12 Trade Win, etc. |
| Presidential Statements | 2 | April 9 (125% China), April 9 (90-day pause) |
| Joint Statements | 6 | US-China Geneva (May 12), Vietnam, Malaysia, etc. |
| CBP Guidance | 10 | CSMS 64649265 and subsequent |
| Truth Social | 5 days | April 6, 7, 8, 11, 30 |

**Time span:** April 2, 2025 - November 2025

---

# Quantitative Analysis: Industry Responses to Tariffs (Partisanship)

## Research question and hypotheses
This quantitative component tests whether industry-level trade responses to U.S. tariffs differ by the partisan composition of the workforce. The core hypothesis is that industries with more Democratic-leaning workforces exhibit larger trade adjustments after tariff shocks, while Republican-leaning industries adjust less. We evaluate this alongside four secondary hypotheses tied to exposure, rigidity, pre-trends, and geography.

Tested hypotheses (numbering preserved from prior analytic memos):
- H0 (primary): Industries with higher Democratic vote share in their workforce show larger post-tariff trade response magnitudes (absolute log changes).
- H1 (exposure): The dem_share effect is attenuated when controlling for tariff exposure intensity.
- H2 (rigidity): Industries with higher employment per establishment (rigidity proxy) show smaller response magnitudes.
- H5 (pre-trends): Dem_share interactions are near zero in pre-2018 years (no differential pre-trends).
- H6 (county exposure): Counties more exposed to tariff-targeted industries are less Democratic.

## Data sources and construction
- Imports by NAICS (6-digit monthly time series) from the U.S. Census International Trade Imports NAICS API; aggregated to NAICS-3 for alignment with partisanship measures. [59]
- Exports by NAICS (3-digit monthly time series) from the U.S. Census International Trade Exports NAICS API. [84]
- Section 301 tariff lists with import values (including 2015-2017 averages and 2017 values) from QuantGov. [55]
- HTS-to-NAICS crosswalk via the 2019 Census import concordance (impconcord2019.xls). [87]
- County-level partisanship from MIT Election Lab presidential returns (2016 and 2020) and county employment from CBP 2020; industry dem_share is employment-weighted across counties. [85, 86]

Derived measures and merges:
- dem_share_avg_2016_2020: employment-weighted two-party Democratic vote share by NAICS-3. [85, 86]
- exposure_share: Section 301 import value mapped to NAICS-3 divided by pre-period (2016-2017) annualized imports for that NAICS-3. [55, 59, 87]
- rigidity: employment per establishment by NAICS-3 from CBP county data. [85]
- Outcome: absolute log change in trade value between pre and post windows (primary: 2016-2017 vs 2018-2019), with robustness windows (2016 vs 2018-2019 and 2016-2017 vs 2019). [88]

## Methods overview
- Cross-sectional change models: compute absolute log change in trade value between pre and post windows and regress on dem_share with OLS and WLS (weights = pre-period trade value). [88]
- Panel fixed effects: monthly log trade values with NAICS and month fixed effects; estimate dem_share x post interaction. [88]
- Event study: dem_share x year interactions with NAICS, year, and month fixed effects; assess differential pre-trends. [88]
- H1/H2 controls: add exposure_share and rigidity to cross-sectional regressions. [88]
- H5: extend series to 2012-2017 for pre-trend checks using Census APIs. [59, 84, 88]
- H6: compute county exposure as employment-weighted sum of industry exposure and correlate with county dem_share. [55, 85, 86, 88]

## Key results (summary)
- Cross-sectional export results show a negative relationship between dem_share and response magnitude in WLS specifications; the same is not robust for imports. [88]
- With exposure and rigidity controls, export WLS coefficients for dem_share remain negative and significant for 2016-2017 vs 2018-2019, while imports remain mostly insignificant. [88]
- Exposure_share and rigidity are both negative and significant in the export WLS control specification, indicating more exposed and more rigid industries show smaller export adjustments. [88]
- Panel fixed-effects dem_share x post interactions are not statistically significant for either imports or exports. [88]
- Event studies show significant pre-period interactions (notably 2016 in the main 2016-2024 panel and 2014/2017 in the 2012-2017 pre-trend checks for exports), which weakens causal interpretation. [88]
- County exposure to tariff-targeted industries is weakly negatively correlated with Democratic vote share (corr = -0.0658). [88]

## Outputs and replication notes
- Main hypothesis tests: `data/analysis_ready/hypothesis_full/` (cross_section_summary.csv, cross_section_regressions.csv, panel_post_effects.csv, event_study_year_interactions.csv). [88]
- Secondary hypothesis tests (H1/H2/H5/H6): `data/analysis_ready/hypothesis_1_2_5_6/` (controls_regressions.csv, controls_correlations.csv, pretrend_event_study_2012_2017.csv, county_exposure_correlation.csv). [88]

## Interpretation caveats
- The NAICS-3 aggregation and the partisanship proxy (county vote shares weighted by employment) are coarse and likely introduce measurement error. [85, 86]
- Exposure_share reflects Section 301 tariff lists only; other tariff channels and downstream input exposure are not captured. [55]
- Pre-trend violations in exports suggest that the dem_share relationship may partly reflect pre-existing industry dynamics rather than tariff effects. [88]

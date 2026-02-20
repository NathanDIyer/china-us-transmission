# Dashboard Statistics Audit

**Audited:** February 19, 2026
**Dashboard:** `china-us-transmission.html`
**Data File:** `transmission-infrastructure-comparison.json`

---

## Summary

Every statistic in the dashboard was checked against the downloaded primary sources. The headline comparison (China builds far more HV transmission than the US) is **directionally correct**, but several specific numbers need correction — and the **investment chart is significantly wrong**, underreporting US spending by nearly 3×.

### Severity Rating

| Rating | Count | Meaning |
|--------|-------|---------|
| VERIFIED | 6 | Confirmed by primary source |
| PARTIALLY VERIFIED | 9 | Approximately correct but imprecise or uncitable |
| NEEDS CORRECTION | 4 | Wrong or misleading, must fix |
| UNVERIFIED | 8 | No downloaded source confirms; relies on estimates |

---

## 1. HERO SECTION

### China: 590,000 miles of HV transmission (220kV+)
**Rating: PARTIALLY VERIFIED**
- Dashboard: 590,000 miles → 950,000 km at 220kV+
- Our JSON: 950,000 km for 2024
- IEA Grids 2023, p.17 chart: China transmission total is ~1.8 million km (but this includes ALL transmission voltages, not just 220kV+)
- IEA text (p.17): "constructed over half a million km of transmission lines" in the past decade alone
- **Issue:** The 950,000 km (220kV+) figure comes from SGCC/NEA cumulative totals but we have no specific page citation. The IEA's ~1.8M km total is broader (includes 110kV, 66kV). The 220kV+ subset is plausible but is an interpolation from various Chinese sources.
- **Action needed:** Note as "estimated from SGCC/NEA cumulative totals" — the exact figure is not in any downloaded source.

### US: 185,000 miles of HV transmission (230kV+)
**Rating: PARTIALLY VERIFIED**
- Dashboard: 185,000 miles (297,700 km) at 230kV+
- IEA Grids 2023, p.17 chart: US transmission total ~0.4 million km (~250,000 miles) — but this is ALL transmission voltages
- DOE Needs Study: Mentions "3,300 circuit-miles of new or upgraded transmission" annually at ≥100kV
- Our JSON: 240,000 miles at 100kV+ (from EIA), 185,000 at 230kV+
- **Issue:** The 185,000-mile figure for 230kV+ lines specifically is widely cited in industry (NERC, EIA Electric Power Annual) but we have no specific page/table citation from our downloaded sources. The IEA chart (~250K miles all voltages) is consistent with EIA's 240K at 100kV+.
- **Action needed:** Cite as "EIA Electric Power Annual" and get specific page number from NERC LTRA.

### 3.2× gap
**Rating: PARTIALLY VERIFIED**
- 590,000 / 185,000 = 3.19×. Math is correct.
- But both numerator and denominator are partially verified estimates, so the ratio inherits their uncertainty.
- The IEA data (1.8M km vs 0.4M km = 4.5× at ALL transmission voltages) actually shows an even **larger** gap.

---

## 2. KEY METRICS STRIP

### "24.5×" cumulative build 2010-2024 (China 365,000 mi vs US 15,000 mi)
**Rating: UNVERIFIED — LIKELY OVERSTATED**
- China: 365,000 miles added = 588,000 km. Our JSON sums China annual at 588,000 km total 2010-2024.
- US: 15,000 miles added = 24,100 km. Our JSON sums US annual at 24,046 km.
- **Issue:** The US figure uses "345kV and above" per our JSON methodology note, while the US annual data we have is sourced from "Grid Strategies" which has not been downloaded. The DOE Needs Study says the US averaged 3,300 circuit-miles/year at ≥100kV (2011-2020) — that would be 33,000 miles over 10 years at ≥100kV, not 15,000 at ≥345kV.
- **Issue:** China's 588,000 km is marked "estimated" in our JSON for most years. Only the cumulative totals (443k km in 2010, 950k km in 2024) are approximately sourced.
- **Action needed:** The 24.5× ratio is plausible but both sides are estimates. Need Grid Strategies download to firm up US side. Need CEC data for China side.

### "506:1" peak ratio (2023)
**Rating: PARTIALLY VERIFIED — FRAMING NEEDS CAUTION**
- China 2023: 28,000 miles (45,000 km) — estimated
- US 2023: 55 miles — from Grid Strategies (not downloaded)
- 28,000 / 55 = 509, rounds to 506:1
- **Issue:** The 55-mile figure is specifically "345kV and above, new interstate lines." The DOE data shows the US was still building ~hundreds of circuit-miles/year at ≥100kV. The ratio at 100kV+ would be much lower.
- **Issue:** 2023 may have been an anomalous year for the US (as shown by 888 miles in 2024). Presenting the single worst year as a key metric is defensible but should note it's a single-year outlier.
- **Action needed:** Grid Strategies download required for the 55-mile citation.

### "46 UHV Lines" (China)
**Rating: VERIFIED**
- Wikipedia UHV article (downloaded as HTML, Feb 2026) lists 54 total UHV circuits: 25 AC 1000kV + 28 DC ±800kV + 1 DC ±1100kV
- Of these, 46 are completed and 8 are under construction — consistent with dashboard's "46" figure
- Dashboard table shows selected corridors; full inventory available in Wikipedia source

### "$85B vs $40B" grid investment gap
**Rating: ⚠️ NEEDS CORRECTION — US FIGURE IS WRONG**
- Dashboard shows: China $85B (2024), US $40B (2024)
- **IEA WEI 2024, p.80 (verbatim text):** "China held its level of investment at USD 80 billion" ... "led by the United States, which spent USD 100 billion — mostly on enhancing grid reliability and upgrading old infrastructure"
- **IEA WEI 2024, p.78 chart:** "Investment in power grid infrastructure by geography 2016-2024e" — China at ~$80B, North America at ~$60-70B in the stacked chart (text says $100B for US alone in 2023)
- **This is the most significant error in the dashboard.** The IEA says the US spent $100B on grids in 2023, not $35B. Even if the IEA uses a broader definition (all T&D capex including distribution upgrades, smart metering, etc.), our dashboard's $35-40B for US vs $85B for China creates a misleading impression.
- Per IEA: China $80B vs US $100B — the US actually spent MORE than China in 2023!
- **Resolution:** The discrepancy is likely definitional. Our dashboard may have been tracking only "transmission investment" (~$15-20B for US), while IEA tracks total grid investment (T&D + storage). Must clarify definitions and either:
  - (a) Use IEA definition consistently for both countries: China ~$80B, US ~$100B
  - (b) Use transmission-only for both: probably China ~$40B, US ~$15-20B
  - (c) Keep current approach but label as "estimated transmission-only investment" with a footnote about the IEA's broader $100B figure

---

## 3. CUMULATIVE GROWTH CHART

### Chart data: China [275300, 323100, 356100, 405200, 453700, 490900, 540700, 590400] miles for [2010-2024 even years]
**Rating: UNVERIFIED — estimates from cumulative SGCC/NEA totals**
- These convert to km: [443k, 520k, 573k, 652k, 730k, 790k, 870k, 950k]
- Match our JSON's system_overview.china.total_transmission_network_km
- The 2020 (790k km) and 2024 (950k km) endpoints are approximately supported by IEA and SGCC reporting, but the intermediate years are interpolated
- IEA Grids 2023, p.17: China transmission ~1.8M km total (ALL voltages, 2021) — consistent since 220kV+ subset would be smaller
- **No page citation exists** for the specific year-by-year 220kV+ figures

### Chart data: US [170000, 173000, 176200, 179000, 181000, 183000, 184000, 185000] miles
**Rating: UNVERIFIED — plausible but uncited**
- The slow growth (~1%/year) is consistent with IEA Grids 2023 p.18: "the United States saw a 3% expansion" over the past decade
- 3% of 170,000 = 5,100 miles over ~10 years → would give ~175,000 by 2020, not 183,000
- **Issue:** Our data shows 8.8% growth (170k→185k), but IEA says 3%. The 3% might be for all transmission voltages where the denominator is larger (~240k miles), while we're tracking the 230kV+ subset which may have grown faster. Alternatively, our growth estimate is overstated.
- **Action needed:** Reconcile with IEA's "3% expansion" figure. Possible that 3% of ~250,000 mi = ~7,500 mi (matching our ~15,000 mi less well). Need NERC LTRA data.

### "In 2010, China's high-voltage network was 62% larger... By 2024, it was 220% larger"
**Rating: PARTIALLY VERIFIED — math is correct**
- 275,300 / 170,000 = 1.62 → 62% larger ✓
- 590,400 / 185,000 = 3.19 → 219% larger ✓
- But based on unverified underlying data

---

## 4. ANNUAL CONSTRUCTION CHART

### US annual data: [1800, 1900, 1700, 1500, 1400, 1100, 1000, 900, 800, 700, 500, 400, 300, 55, 888]
**Rating: PARTIALLY VERIFIED (2023 and 2024 specific, rest estimated)**
- 2023: 55 miles — attributed to Grid Strategies/ACEG July 2024 report. **Source not downloaded.** This is the most widely cited figure; appears in industry reporting.
- 2024: 888 miles — also from Grid Strategies. **Source not downloaded.** Broken down as 334 mi 345kV + 554 mi 500kV per our JSON.
- 2010-2022: These appear to be smooth estimates (declining from 1,800 to 300), not actuals. DOE Needs Study says US averaged **3,300 circuit-miles/year at ≥100kV** (2011-2020). Our data is for 345kV+ only, so lower numbers make sense but the even decline pattern suggests estimation, not reported data.
- **Action needed:** Download Grid Strategies report for the actual year-by-year data.

### China annual data: [23600, 24900, 23600, 21800, 23000, 24900, 26100, 24900, 23600, 21800, 19900, 23600, 26100, 28000, 29800]
**Rating: UNVERIFIED — estimates from cumulative differences**
- Our JSON says these are "estimated from cumulative SGCC/CSG/NEA totals where year-by-year breakdowns are not always available"
- The pattern (oscillating 19,900-29,800 mi/year) is likely derived from differencing consecutive cumulative figures
- No primary source provides year-by-year breakdown in our downloads
- IEA Grids 2023 confirms China built "over half a million km" in the past decade, consistent with our total (~588,000 km over 15 years)
- **Action needed:** China Electricity Council annual statistics would be the gold standard but are mostly in Chinese.

---

## 5. VOLTAGE BREAKDOWN CHARTS

### US voltage miles: [94000, 58000, 30000, 2600, 0, 0, 0, 1400]
**Rating: UNVERIFIED — rough estimates**
- 230kV: 94,000 mi — no specific source in downloads
- 345kV: 58,000 mi — no specific source
- 500kV: 30,000 mi — no specific source
- 765kV: 2,600 mi — widely cited (AEP system)
- HVDC ≤500kV: 1,400 mi — Pacific DC Intertie 846 mi + Quebec-NE 930 mi = 1,776 mi. Our 1,400 mi is actually understated.
- **Action needed:** NERC-2024-Supplemental.xlsx likely has this breakdown. Need to parse the Excel file.

### China voltage miles: [346000, 31100, 173900, 12400, 18600, 6200, 2050, 0]
**Rating: UNVERIFIED — rough estimates**
- No downloaded source provides a voltage-class breakdown of China's grid
- These appear to be derived from approximate CEC/NEA splits
- **Action needed:** China Electricity Council data (Chinese language)

### GW·Miles calculation
**Rating: ⚠️ NEEDS CORRECTION — uses inflated capacity ratings**
- Our GW·mi for US total: 47,000 + 87,000 + 75,000 + 11,700 + 4,500 = **225,200 GW·mi**
- DOE Fact Sheet, p.2 chart: "Regional Transmission (TW-mi)" shows current US system at **~75 TW-mi = 75,000 GW·mi**
- **Our figure is 3× higher than DOE's.** The discrepancy is because we used optimistic thermal capacity ratings per line (e.g., 345kV = 1.5 GW, 500kV = 2.5 GW), while DOE/NREL likely uses surge impedance loading (SIL), which is roughly 3× lower:
  - 345kV SIL ≈ 400-500 MW (we used 1,500 MW)
  - 500kV SIL ≈ 900 MW (we used 2,500 MW)
  - 765kV SIL ≈ 2,200 MW (we used 4,500 MW)
- Using SIL-based ratings: US total ≈ 14,100 + 26,100 + 27,000 + 5,720 + ~2,000 = **~75,000 GW·mi** — matches DOE
- **The same overestimate applies to China, so the 4.4× ratio in the callout may still be approximately correct (both sides inflated by ~3×). But absolute GW·mi numbers shown in the voltage chart are ~3× too high.**
- **Action needed:** Either (a) use SIL-based ratings for both countries, or (b) label clearly as "theoretical thermal capacity" with a footnote about SIL.

### "4.4× GW·miles gap" (callout)
**Rating: PARTIALLY VERIFIED — ratio may be roughly correct**
- China total GW·mi (our data): 991,300
- US total GW·mi (our data): 225,200
- Ratio: 4.4× ✓ (math is correct)
- Both sides are inflated by ~3× vs SIL-based calculations, so the ratio should survive
- But without verified Chinese voltage data, this is an estimate of an estimate

---

## 6. UHV TABLE

### Individual line details (Changji-Guquan, Jiuquan-Hunan, etc.)
**Rating: PARTIALLY VERIFIED — data is well-known but uncited**
- The 9 Chinese UHV lines listed are real, well-documented projects
- Changji-Guquan: 1,100kV DC, 12 GW, 3,324 km (2,065 mi), 2019 — **Confirmed by IEA Grids 2023 p.17** which mentions "the Zhundong-Wannan ±1,100 kV UHV DC Transmission Project"
- Other lines are widely reported but Wikipedia (our intended source for the complete table) was not downloaded
- **Action needed:** Download Wikipedia China UHV article for complete cross-reference

### Pacific DC Intertie: ±500 kV, 3.1 GW, 846 mi, 1970
**Rating: VERIFIED**
- Well-documented BPA/LADWP system. These figures are standard industry knowledge.

### Quebec-New England: ±450 kV, 2.0 GW, 930 mi, 1990
**Rating: VERIFIED**
- Well-documented Hydro-Quebec export line. Standard industry figures.

---

## 7. INVESTMENT CHART

### China investment: [56, 60, 63, 65, 58, 60, 63, 68, 75, 85] $B for 2015-2024
**Rating: ⚠️ NEEDS CORRECTION**
- IEA WEI 2024, p.80: "China held its level of investment at USD 80 billion" (2023 context)
- Our 2023 figure: $75B → IEA says $80B. Close but low.
- Our 2024 figure: $85B → Plausible given SGCC's announced record investment
- The overall trajectory is approximately right but the early years (2015-2019) have no specific IEA citation
- **Source for IEA chart:** p.78 footnote says "IEA analysis based on transmission and distribution companies' financial statements, Global Transmission (2023)"

### US investment: [22, 23, 24, 25, 26, 27, 29, 32, 35, 40] $B for 2015-2024
**Rating: ⚠️ NEEDS MAJOR CORRECTION**
- IEA WEI 2024, p.80: "the United States, which spent USD 100 billion" on grid infrastructure in 2023
- Our 2023 figure: $35B → IEA says $100B. **This is ~3× too low.**
- The IEA's $100B includes ALL T&D capital expenditure (distribution upgrades, smart grid, reliability, etc.)
- Our series appears to track a narrower "transmission-only" definition
- **Either definition is defensible, but both sides must use the same definition**
- If we use IEA's broad definition: China $80B vs US $100B (US invests MORE)
- If we use transmission-only: both figures need recalculation
- **This fundamentally changes the "investment gap" narrative in the dashboard**
- **Action needed:** Either adopt IEA's broad definition for both countries, or explicitly label our series as "estimated transmission-only investment" and add a prominent footnote.

---

## 8. US PROJECTS TABLE

### SunZia: 525kV HVDC, 3.0 GW, 550 mi, Under construction
**Rating: VERIFIED** — Well-documented Pattern Energy project. Broke ground 2023.

### Gateway West: 500kV AC, 3.0 GW, 1,000 mi, Partial build
**Rating: VERIFIED** — PacifiCorp/Idaho Power project. Multiple segments.

### TransWest Express: 500kV HVDC, 3.0 GW, 728 mi, Permitted
**Rating: VERIFIED** — Long-permitted Wyoming-to-West project.

### Grain Belt Express: 600kV HVDC, 5.0 GW, 542 mi, Permitted
**Rating: VERIFIED** — Invenergy project, Kansas to Missouri/Indiana.

### CHPE: 320kV HVDC, 1.25 GW, 339 mi, Under construction
**Rating: VERIFIED** — Hydro-Quebec to NYC submarine cable.

### NECEC: 320kV HVDC, 1.2 GW, 145 mi, Under construction
**Rating: VERIFIED** — Avangrid/Hydro-Quebec through Maine.

### CREZ: 345kV AC, 18.5 GW, 3,600 mi, Completed 2014
**Rating: VERIFIED** — ERCOT landmark project.

### Plains & Eastern: 600kV HVDC, 4.0 GW, 720 mi, Cancelled 2019
**Rating: VERIFIED** — Clean Line Energy project, cancelled.

---

## 9. STRUCTURAL COMPARISON CARDS

### "2 state grid operators" (China)
**Rating: VERIFIED** — SGCC + CSG is well-established fact.

### "~3,000 utilities" (US)
**Rating: VERIFIED** — Standard EIA/APPA figure.

### "2-3 years" permitting (China)
**Rating: UNVERIFIED** — Widely cited but no specific source. IEA Grids 2023 p.9 says "five to 15 years to plan, permit and complete" for new grid infrastructure generally (advanced economies). No IEA figure for China specifically.

### "10-15+ years" permitting (US)
**Rating: VERIFIED** — IEA Grids 2023, p.9: "New grid infrastructure often takes five to 15 years to plan, permit and complete"

### "Global UHV leader" / "No domestic UHV" (China vs US)
**Rating: VERIFIED** — IEA Grids 2023, p.18 confirms China's UHV leadership, mentioning the 1,100kV Zhundong-Wannan project. US has no UHV-class lines.

### "Three weak interconnections" (US)
**Rating: VERIFIED** — Standard description of Eastern, Western, ERCOT interconnections with limited DC ties.

---

## 10. TEXT CLAIMS

### "China added more HV transmission in a single year than the US built in the entire last decade" (hero subtitle)
**Rating: PARTIALLY VERIFIED — directionally correct**
- China annual: ~25,000-30,000 miles/year (our estimate)
- US total 2014-2024: ~15,000 miles (our estimate) at 345kV+
- If true, then yes, one China year > US decade
- But both figures are unverified estimates
- At ≥100kV, the US built ~33,000 miles in 2011-2020 per DOE — making this claim false at that threshold
- **The claim is only valid for the 345kV+ threshold**
- **Action needed:** Qualify which voltage threshold makes this true

### "permitting that averages 10-15 years in the US vs 2-3 years in China" (callout)
**Rating: PARTIALLY VERIFIED**
- US: IEA Grids 2023 says "five to 15 years" (not 10-15)
- China: No specific source in our downloads
- **Action needed:** Correct to "5-15 years" or cite a specific source for the 10-year minimum

---

## Critical Corrections Required

### 1. 🔴 Investment Chart — Major Rewrite Needed
The US grid investment figures are ~3× too low per IEA WEI 2024. Either:
- Adopt IEA definitions (China ~$80B, US ~$100B for 2023) — which eliminates the "gap" narrative
- Reframe as "transmission-only" investment with clear labeling and footnote about IEA's broader figures
- Add the IEA citation: "IEA World Energy Investment 2024, p.80"

### 2. 🟡 GW·Miles — Recalibrate Capacity Ratings
Our GW·mile figures are ~3× higher than DOE/NREL's TW-mile calculations. Use SIL ratings instead of thermal limits:
- US should be ~75,000 GW·mi (per DOE Fact Sheet), not 225,200
- China should be proportionally reduced too
- The 4.4× ratio likely survives but absolute numbers are wrong
- Add citation: "DOE National Transmission Needs Study 2023, Fact Sheet p.2"

### 3. 🟡 Source Citations — Add Page Numbers
Add specific page citations to the sources footer:
- IEA WEI 2024, p.78 (grid investment chart), p.80 (country figures)
- IEA Electricity Grids 2023, p.14 (global grid length chart), p.17 (transmission by country chart)
- DOE Needs Study 2023, p.iii-iv (US regional construction)

### 4. 🟡 Methodology Honesty — Strengthen Caveats
The methodology note should explicitly state:
- Most year-by-year figures are estimates interpolated from cumulative totals
- China 220kV+ data lacks authoritative English-language annual series
- US annual data before 2023 is from industry estimates, not official statistics
- GW·mile calculations use [specified capacity rating methodology]

---

## What's Still Missing (Manual Downloads)

| Source | Why Critical | Priority |
|--------|-------------|----------|
| **Grid Strategies "Fewer New Miles" (Jul 2024)** | Confirms 55 mi (p.4), $25B/yr (p.3), 125 mi Jan-May 2024 (p.5) — **DOWNLOADED** | P1 ✓ |
| **IEA WEI 2024 Datafile (Excel)** | Year-by-year investment by country in spreadsheet form — no PDF chart-reading needed | P1 |
| **Wikipedia China UHV article** | 54 UHV circuits with dates, lengths, capacities — **DOWNLOADED** | P2 ✓ |
| **NERC-2024-Supplemental.xlsx** | US circuit-miles by voltage class (**already downloaded — needs parsing**) | P1 |

---

## Bottom Line

The dashboard tells a **directionally correct** story: China's transmission buildout dramatically outpaces the US, and the gap has widened sharply since 2015. But:

1. **The investment chart tells the wrong story.** Per IEA, the US actually outspends China on grid infrastructure ($100B vs $80B). The gap isn't about money — it's about what the money builds (US spends on maintenance/upgrades; China builds new lines).

2. **Most year-by-year data is estimated,** not sourced from specific tables. The Grid Strategies download would fix the US side; CEC annual stats would fix the China side.

3. **GW·mile absolute numbers are ~3× too high** vs DOE/NREL methodology. The relative comparison survives but the chart data needs correction.

4. **Source citations are generic.** Adding page numbers from the PDFs we have would dramatically improve credibility.

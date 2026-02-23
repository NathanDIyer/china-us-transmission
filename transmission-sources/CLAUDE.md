# China vs US Transmission: Source Library & Verification Guide

> **Purpose:** Rigorous comparison of Chinese and US high-voltage transmission infrastructure. Every claim in `china-us-transmission.html` must trace to a named source with page/table citation.

---

## Quick Reference

| What | Path |
|------|------|
| **Dashboard** | `../china-us-transmission.html` |
| **Fact-check report** | `../china-us-transmission-fact-check.md` |
| **GW·miles methodology** | `GW-MILES-METHODOLOGY.md` |
| **China data summary** | `China-CEC-NEA-transmission-data-summary.txt` |
| **Research status** | `RESEARCH-STATUS.md` |
| **Dashboard audit (original)** | `DASHBOARD-AUDIT.md` |

---

## Source Hierarchy

Sources are ranked by authority. Always prefer higher-tier sources. When citing, include **report name, page/table number, and the specific figure**.

### Tier 1: Official Government/Regulatory Data

| Source | File | What It Contains | Key Pages |
|--------|------|-----------------|-----------|
| **FERC Energy Infrastructure Update** | `FERC-Energy-Infrastructure-Update-April-2025.pdf` | US HV transmission construction by year (345kV+). **The** source for US annual new-build miles. Jul 2025 revision corrected 2023 from 55→450 mi. | Table: circuit-miles by voltage |
| **EIA/FERC Form 1** | [Online](https://www.eia.gov/todayinenergy/detail.php?id=63724) | US T&D capital expenditure: $27.7B transmission + $50.9B distribution (2023). Investor-owned utilities only. | Article tables |
| **China NEA Annual Statistics** | [nea.gov.cn](https://www.nea.gov.cn/2024-01/26/c_1310762246.htm) | Total grid investment (电网投资): 527.5B CNY for 2023. Single aggregate — no T/D split. | Press release |
| **DOE National Transmission Needs Study** | `DOE-National-Transmission-Needs-Study-2023.pdf` (15MB) | US existing transmission by region, 85.6 TW-mi (SIL), 3,300 circuit-mi/yr avg (≥100kV, 2011-2020). | p.iii, p.iv, p.123 (Table VI-3) |
| **HIFLD Geospatial Data** | [Online](https://hifld-geoplatform.hub.arcgis.com/datasets/transmission-lines-1) | US 230kV+ miles: 186,623 (52,244 line features, haversine-computed). Source for voltage breakdown. | GIS data |
| **NERC 2024 Supplemental** | `NERC-2024-Supplemental.xlsx` | Planned US circuit-miles by voltage class (2024-2034). 1,196 individual projects. 345kV = 6,435 mi (39%). | Table L, Table N, Form D |
| **NERC 2025 LTRA** | `NERC-2025-LTRA.pdf` (7.4MB) | 10-year US reliability outlook with planned transmission tables. MISO $30B/488 projects (p.48), SPP 2024 ITP largest-ever (p.62), NYISO CHPE/public policy (pp.37,79), PJM RTEP $5.9B (p.94). | pp.37,43,48,62,79,94 |

### Tier 2: International Agency (Same Methodology for Both Countries)

| Source | File | What It Contains | Key Pages |
|--------|------|-----------------|-----------|
| **IEA World Energy Investment 2024** | `IEA-World-Energy-Investment-2024.pdf` | Grid investment by country: US ~$100B, China ~$80B (2023). Definition = "grids + storage." **Use for top-line comparisons** — same methodology for both countries. | p.78 (chart), p.80 (text) |
| **IEA Electricity Grids 2023** | `IEA-Electricity-Grids-2023.pdf` | Global grid stocktake: 80M km total, China ~1.9M km, US ~0.4M km (all transmission voltages). 710,000 km built in China in past decade. US: ~3% expansion. | p.14, p.17, p.18, p.28 |
| **IEA Building the Future Transmission Grid (2024)** | [Online](https://www.iea.org/reports/building-the-future-transmission-grid) | Global transmission investment: $140B (2023). China estimated ~$40B in HV transmission. | Exec summary |

### Tier 3: Industry Analysis

| Source | File | What It Contains | Key Figures |
|--------|------|-----------------|-------------|
| **ACEG/Grid Strategies Rev.1 (Jul 2025)** | `ACEG-Grid-Strategies-Fewer-New-Miles-2025-Rev1.pdf` | FERC-revised US 345kV+ construction. 2023: ~450 mi (400 mi 345kV + 50 mi 500kV). 2024: 888 mi. Averages by era. | Addendum p.16 |
| **Grid Strategies "Fewer New Miles" (Jul 2024)** | `Grid-Strategies-Fewer-New-Miles-2023.pdf` | Original report: 55 mi 2023 (superseded). $25B/yr transmission (Brattle, p.3). 90% reliability (p.7). Figure 1: 345kV+ by year. | p.3, p.4, p.6, p.7 |
| **NREL ATB 2024** | [Online](https://atb.nrel.gov/electricity/2024/utility-scale_battery_storage) | Battery storage installed cost: ~$1,336/kW (4-hr system). Used to derive US storage investment. | Base year data |

### Tier 3.5: ISO/RTO Planning Documents

| Source | File | What It Contains | Key Data |
|--------|------|-----------------|----------|
| **PJM Inside Lines** | [Online](https://insidelines.pjm.com/) | RTEP approval announcements. 2024 Window 1: $5.9B (Feb 2025). 2025 Window 1: $11.8B, 134 proposals, first HVDC underground (Feb 2026). | Board approval articles |
| **MISO LRTP Board Decision** | [Online](https://www.misoenergy.org/) | Tranche 1: Jul 2022. Tranche 2.1: Dec 2024. Combined with MTEP24 + JTIQ = $30B, 488 projects, ~5,000 mi 345kV + ~1,750 mi 765kV. | Per NERC 2025 LTRA p.48 |
| **SPP 2024 ITP** | [Online](https://spp.org/) | "Single largest portfolio in SPP's 20-year history." 89 transmission upgrades. Exact $ figure not in NERC LTRA (~$5B estimated). | NERC LTRA p.62 |

### Tier 4: Chinese Official Sources (Primary, but Translation/Access Issues)

| Source | File | What It Contains | Key Data |
|--------|------|-----------------|----------|
| **China Energy Big Data Report 2024 (Ditan)** | `Ditan_source.pdf` (94pp, Chinese) | **THE key Chinese source.** Complete 2014-2023 annual time series: 220kV+ transmission (Chart 5-14), transformer capacity (Chart 5-13), grid investment (Table 1-4). CEC/NBS data. | p.60: 2023 = 92.05万千米 (920,500 km) |
| **CEC Annual Development Report 2025** | `CEC-Annual-Development-Report-2025-extracts.txt` | 2024 confirmed: 960,970 km at 220kV+ (+3.5% YoY). 35kV+ total: 2,477,000 km. | Via Sina Finance Jul 2025 |
| **CEC Electricity Statistics 2019** | `CEC-electricity-statistics-2019.txt` | Full voltage-class breakdown 2018-2019: 220kV, 330kV, 500kV, 750kV, 1000kV AC, ±800kV DC. **The** source for China voltage composition. | Section 4 |
| **CEC Electricity Statistics 2020** | `CEC-electricity-statistics-2020-preliminary.txt` | 220kV+ aggregates for 2019-2020. Less detail than 2019. | Cumulative totals |
| **CCTV News (Nov 22, 2025)** | [Online](https://news.cctv.com/2025/11/22/ARTIe0KN3cYThjCmWEhCMolO251122.shtml) | 44 UHV lines, 50,000+ km, 19 new in 14th FYP, 380B CNY invested, 9.8 km/day build rate. | State media |
| **SGCC 15th FYP Announcement (Jan 2025)** | State media / Caixin | SGCC 15th FYP: 4 trillion CNY investment (~$574B), 350 GW new UHV capacity, 420 GW cross-country by 2030, 1,200 GWh storage. | Press reports |
| **Nanpudian UHV Tracker (Feb 2025)** | [Online](https://www.nanpudian.com/media_coverage/497.html) | 40 UHV lines (Nov 2024): SGCC 36/48,000km, CSG 4/6,235km. 14th FYP target: 150 GW; 15th FYP: 165 GW. | Project tracker |
| **Wikipedia China UHV** | `Wikipedia-China-UHV.html` | Complete inventory: 54 UHV circuits (25 AC + 29 DC) with voltage, length, capacity, dates. | Sortable table |

### Tier 5: Derived/Internal

| Source | File | Purpose |
|--------|------|---------|
| **GW·Miles Methodology** | `GW-MILES-METHODOLOGY.md` | Documents how China 3.52 GW/mi and US 1.33 GW/mi averages are computed from CEC and FERC Form 1/PUDL data. |
| **China CEC/NEA Data Summary** | `China-CEC-NEA-transmission-data-summary.txt` | Compiled Chinese source data with file-by-file inventory and cross-validation notes. |
| **td-voltage-aging.json** | `../eia-explorer/public/bulk-data/pudl/td-voltage-aging.json` | FERC Form 1 via PUDL: US transmission miles by voltage class over time. Source for US GW·mi calculation. |

---

## Key Definitions & Thresholds

| Term | US Definition | China Definition | Notes |
|------|--------------|-----------------|-------|
| **"Transmission"** | 230kV and above | 220kV and above | Comparable but not identical. Makes China figures slightly more inclusive. |
| **"High-voltage new build"** | 345kV+ (Grid Strategies) | 220kV+ (CEC) | US annual construction bars use 345kV+ threshold — this is *higher* than China, making the gap conservative. |
| **"Grid investment"** (IEA) | T&D + storage + smart grid | T&D + storage + smart grid | Same methodology for both countries. IEA WEI 2024 chart title: "grids and storage." |
| **"Grid investment"** (NEA) | N/A | 电网投资 (single aggregate) | No public T/D breakdown from NEA or CEC. |
| **GW·miles** | Thermal rating × route miles | Thermal rating × route miles | See `GW-MILES-METHODOLOGY.md` for thermal ratings by voltage. SIL would give ~2.8× lower values. |
| **UHV** | ≥765kV AC or ≥500kV DC (US has essentially zero) | ≥1000kV AC or ≥800kV DC | 44 operational Chinese UHV lines per CCTV Nov 2025. |

---

## Investment Reconciliation (2023)

This is the most complex comparison. The dashboard shows an apples-to-apples breakdown.

### United States: ~$100B total (IEA)

| Component | Amount | Source | Confidence |
|-----------|--------|--------|------------|
| Transmission | $27.7B | FERC Form 1 (EIA article #63724) | High |
| Distribution | $50.9B | FERC Form 1 (EIA article #63724) | High |
| FERC T&D subtotal | $78.6B | FERC Form 1 | High |
| Battery storage | ~$11B | Derived: 7.9 GW × ~$1,400/kW (NREL ATB 2024) | Medium |
| Non-FERC utilities | ~$10B | Gap: BNEF $87B grid-only minus FERC $79B | Medium |
| **IEA total** | **~$100B** | IEA WEI 2024 p.80 | High |

Of $28B transmission: ~90% funds reliability upgrades, not new construction (Grid Strategies p.7, Brattle).

### China: ~$80B total (IEA) / 528B CNY (NEA)

| Component | Amount | Source | Confidence |
|-----------|--------|--------|------------|
| Total grid (电网投资) | 527.5B CNY (~$74B) | NEA 2023 Statistics | High |
| IEA estimate | ~$80B | IEA WEI 2024 p.80 | High |
| Transmission est. | ~$40B | IEA "Building Future Transmission Grid" | Medium-low |
| Distribution est. | ~$34B | Remainder | Low |

**Known gap:** China does not publicly report T/D split. IEA has a paywalled chart (2015-2022 T/D split) but values not publicly accessible. Best estimate: ~54% transmission / ~46% distribution.

---

## Verification Workflow

When fact-checking a claim in the dashboard:

1. **Find the claim** in `china-us-transmission.html` (Ctrl-F or grep)
2. **Check the fact-check report** `../china-us-transmission-fact-check.md` — it covers 40 claims with source traces
3. **Locate the source file** in this folder using the Source Hierarchy above
4. **Verify against the PDF** — use the page/table citations noted above
5. **For China data**, cross-reference `China-CEC-NEA-transmission-data-summary.txt` and `Ditan_source.pdf` (Chart 5-14 for cumulative km, Table 1-4 for investment)
6. **For US annual construction**, the chain is: FERC Energy Infrastructure Update → Grid Strategies Rev.1 (addendum p.16) → dashboard `usAnnual` array
7. **For investment figures**, follow the reconciliation above — IEA for top-line, FERC for US breakdown
8. **For GW·miles**, see `GW-MILES-METHODOLOGY.md` for the full computation

---

## Dashboard Data Architecture

The dashboard JS (`china-us-transmission.html`) uses hardcoded arrays that get dynamically updated if an external JSON loads. Key arrays:

| JS Variable | What | Source |
|-------------|------|--------|
| `chinaAnnual` | China 220kV+ new miles/year (2010-2024) | Primary: `chart_ready_data.annual_construction_km` (Ditan Chart 5-14 additions + 2024 CEC delta). Bridge: `construction_rate_comparison_km_per_year` (2010-2013). Legacy fallback: `annual_construction_rates.china`. |
| `usAnnual` | US 345kV+ new miles/year (2010-2024) | Grid Strategies Figure 1 + FERC revision |
| `cumulativeChinaMiles` | China 220kV+ cumulative total (km→mi) | CEC/Ditan Chart 5-14 |
| `cumulativeUSMiles` | US 230kV+ cumulative (km→mi) | HIFLD + FERC Form 1 via PUDL |
| `investmentChina` / `investmentUS` | Grid investment $B (2015-2024) | IEA WEI 2024 p.78 chart estimates |
| UHV table | Individual UHV line data | Wikipedia + CCTV Nov 2025 |

### Dynamic Updates

The function `updateTransmissionMetricCards()` recomputes all metric card values from the arrays above whenever data changes. If the external JSON (`transmission-infrastructure-comparison.json`) loads successfully, its values replace the hardcoded arrays.
For China annual construction specifically, the runtime source priority is explicit: chart-ready annual additions first, pre-2014 bridge second, legacy annual-rates block last. This avoids mixing older computed/estimated values into the primary chart path.

---

## Known Data Gaps (Priority Order)

1. **China T/D investment split** — NEA reports single aggregate. IEA has paywalled chart. ~$40B transmission is a medium-confidence estimate.
2. **China annual construction 2020-2024** — CEC stopped publishing voltage-class detail after 2019. Ditan provides 220kV+ aggregate (Chart 5-14) but not by voltage class. Dashboard uses estimates for these years.
3. **US 230-344kV annual construction** — Grid Strategies only tracks 345kV+. The 891 mi/yr average for 230-344kV comes from FERC Form 1 (PUDL) net change, not project-level data.
4. **IEA WEI 2024 Datafile (Excel)** — Would provide exact investment figures by country by year. Requires download from IEA product page. Not yet obtained.
5. **SGCC annual reports (English)** — Would provide official Chinese utility investment with more granularity. Site is slow outside China.

---

## Conventions

- **All miles on dashboard** are statute miles. Convert km → mi: × 0.621371.
- **"HV transmission"** in narrative text = 220kV+ (China) or 230kV+ (US) for totals; 345kV+ for US annual construction bars.
- **Investment in $B** = USD billions. CNY converted at prevailing rate (~7.08 in 2023).
- **"IEA grids + storage"** always means the combined IEA definition, not pure T&D. Always label it when citing.
- **Thermal ratings** (not SIL) for GW·miles. This is the physically meaningful capacity; see methodology doc.
- **Source citations** in the dashboard use inline `<div class="chart-source">` elements below each chart and a full sources list + methodology section at the bottom.

---

## Recently Completed Work

- **Feb 22, 2026:** Added "Forward Look: 2026–2030" section. China 15th FYP targets ($700B, 350 GW UHV, ~175K mi est.) vs US NERC pipeline (20,836 circuit-miles, 1,196 projects). ISO/RTO table (MISO $30B, PJM $18B+, SPP ~$5B). Three charts: forward miles comparison, NERC voltage breakdown, NERC driver breakdown. 12 new fact-check claims.
- **Feb 22, 2026:** Replaced misleading "$100B → 450 mi" with apples-to-apples investment breakdown. Added CSS stacked-bar visual showing US T/D/storage split ($28B + $51B + $21B) vs China $80B total. New sources: EIA/FERC Form 1, NREL ATB 2024.
- **Feb 21, 2026:** Full fact-check audit (40 claims). Fixed 2023 Contrast ratio from mismatched 506:1 to corrected 52:1. Added 230-344kV line to US annual construction.
- **Feb 20, 2026:** Light theme redesign. Fixed China annual construction from interpolated estimates to Ditan report actuals (2014-2023). GW·miles methodology documented.
- **Feb 19, 2026:** Initial dashboard build with 7 sections. DASHBOARD-AUDIT.md and RESEARCH-STATUS.md created.

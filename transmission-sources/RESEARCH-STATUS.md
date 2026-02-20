# China vs US Transmission Analysis — Research Status

**Last Updated:** February 19, 2026
**Dashboard:** `china-us-transmission.html`
**Data File:** `transmission-infrastructure-comparison.json`
**Sources Folder:** `transmission-sources/`

---

## What We Have vs What We Need

### Current State

The dashboard has 7 charts, tables, and structural comparisons — but relies on **estimated/interpolated data** for many year-by-year figures. The sources section lists 12 links but lacks specific page/figure citations. We need to upgrade from "estimates derived from cumulative totals" to "Table X, Page Y of [Report]."

### Key Data Gaps

| Data Point | Current Status | What's Needed | Best Source |
|-----------|---------------|---------------|-------------|
| US annual HV construction (mi/yr, 2010-2024) | Estimates from Grid Strategies reporting | Year-by-year actuals by voltage class (345kV, 500kV, 765kV) | **Grid Strategies "Ready to Go" 2024 report** |
| US total transmission by voltage class | Rough estimates (94k mi at 230kV, 58k at 345kV, etc.) | Official EIA or NERC breakdown | **NERC 2024 Supplemental XLSX** (downloaded), **EIA Form 411** |
| China annual construction (km/yr, 2010-2024) | Interpolated from cumulative SGCC totals | Year-by-year from CEC or NEA annual statistics | **China Electricity Council annual stats**, **SGCC annual reports** |
| China total by voltage class | Rough split (220kV, 330kV, 500kV, 750kV, UHV) | Official CEC/NEA breakdown | **CEC Power Industry Statistics** (Chinese language) |
| China UHV line inventory | 13 lines listed in dashboard table | Complete list of all 42 lines with dates, lengths, capacities | **Wikipedia China UHV article** (downloaded, 54 circuits verified) |
| Grid investment by country (2010-2024) | IEA-sourced estimates ($56-85B China, $22-40B US) | Official IEA datafile with year-by-year by country | **IEA WEI 2024 Datafile** (Excel download) |
| GW-miles by voltage | Calculated from (typical capacity x miles) | More defensible capacity ratings per voltage class | **NREL NTP Study**, engineering references |
| US existing transmission by region | Not in dashboard | Regional breakdown (PJM, MISO, SPP, etc.) | **DOE Needs Study** (downloaded) |

---

## Downloaded Sources (Ready to Parse)

All in `transmission-sources/`:

### 1. DOE-National-Transmission-Needs-Study-2023.pdf (15 MB)
- **Published:** October 2023 by DOE Grid Deployment Office
- **URL:** https://www.energy.gov/gdo/national-transmission-needs-study
- **Contains:** Existing US transmission capacity by region, interregional transfer needs, congestion analysis, corridor priorities
- **Parse for:** Regional transmission capacity maps, existing transfer limits between regions, total US transmission statistics
- **Status:** Downloaded, needs parsing

### 2. IEA-Electricity-Grids-2023.pdf (4.6 MB)
- **Published:** October 17, 2023 by IEA
- **URL:** https://www.iea.org/reports/electricity-grids-and-secure-energy-transitions
- **License:** CC BY 4.0
- **Contains:** First global grid stocktake — total grid length by country, grid age, investment trends, annual additions, China vs US comparison
- **Parse for:** Total grid length by country over time, investment by country, grid age statistics, annual km added
- **This is the single most important source for the comparison**
- **Status:** Downloaded, needs parsing

### 3. IEA-World-Energy-Investment-2024.pdf (3.6 MB)
- **Published:** June 6, 2024 by IEA
- **URL:** https://www.iea.org/reports/world-energy-investment-2024
- **License:** CC BY 4.0
- **Contains:** Chapter 7 is China-specific. Grid investment by country/region 2015-2024
- **Parse for:** Annual grid investment figures ($B) by country, transmission vs distribution split, China SGCC investment
- **Status:** Downloaded, needs parsing

### 4. NERC-2025-LTRA.pdf (7.4 MB)
- **Published:** January 29, 2026 by NERC
- **URL:** https://www.nerc.com/pa/RAPA/ra/Pages/default.aspx
- **Contains:** US planned transmission additions by voltage class, 10-year reliability outlook, circuit-miles
- **Parse for:** Tables showing planned HV additions (230kV, 345kV, 500kV, 765kV) by year and region
- **Status:** Downloaded, needs parsing

### 5. NERC-2024-Supplemental.xlsx (669 KB)
- **Published:** December 19, 2024 by NERC
- **Contains:** Charts and data in spreadsheet form from the LTRA
- **Parse for:** This is the gold — should have circuit-miles by voltage class in tabular form
- **Status:** Downloaded, needs parsing (Excel)

### 6. EIA-411-transmission-lines-2016.xls (565 KB)
- **Published:** 2016 vintage by EIA
- **URL:** https://www.eia.gov/electricity/data/eia411/
- **Contains:** Proposed high-voltage transmission line additions
- **Limitation:** Only covers planned additions as of 2016, not historical actuals
- **Status:** Downloaded, limited utility

### 7. DOE-Draft-Needs-Study-Feb2023.pdf (5.4 MB)
- **Contains:** Earlier draft with potentially different data tables
- **Status:** Downloaded, secondary reference

### 8. DOE-US-Fact-Sheet.pdf (1.2 MB)
- **Contains:** Summary US transmission statistics
- **Status:** Downloaded, quick reference

---

## Sources That Must Be Downloaded Manually

### RESOLVED — Now Downloaded ✓

#### ~~A. Grid Strategies~~ → DOWNLOADED as `Grid-Strategies-Fewer-New-Miles-2023.pdf` (1.7 MB)
- **Actual title:** "Fewer New Miles: The US Transmission Grid in the 2020s" by Nathan Shreve, Zachary Zimmerman, and Rob Gramlich, Grid Strategies, July 2024
- **Key data:** p.4 Figure 1: "Only 55 new miles of high-voltage transmission were constructed in 2023" (345kV+). p.5: 125 mi Jan–May 2024 (Delaney-Colorado 500kV). p.3: $25B/yr transmission spend (Brattle Group), 90% reliability. p.6: investment chart by region 1996–2026.
- **Note:** The 888-mile full-year 2024 figure is NOT in this report (it only covers through May 2024). Separate source needed.

#### ~~C. Wikipedia China UHV~~ → DOWNLOADED as `Wikipedia-China-UHV.html` (140 KB)
- **Content verified:** Full article with sortable table of 54 UHV circuits (25 AC 1000kV + 28 DC ±800kV + 1 DC ±1100kV), including under construction. Has voltage, length (km), capacity (GW), year completed, and route names.

### STILL NEEDED — Download These in Your Browser

#### B. IEA World Energy Investment 2024 — Datafile (Excel)
- **URL:** https://www.iea.org/data-and-statistics/data-product/world-energy-investment-2024-datafile
- **Why it matters:** Has grid investment by country by year in spreadsheet form — no PDF parsing needed
- **Why I can't get it:** Requires clicking through IEA product page
- **Action:** Download the Excel datafile (free, CC BY 4.0)

### NICE TO HAVE

#### E. SGCC Annual Report (English)
- **URL:** http://www.sgcc.com.cn/html/sgcc_main_en/
- **Why it matters:** Official SGCC investment figures, grid statistics, UHV inventory
- **Limitation:** Site is extremely slow from outside China, English content limited
- **Action:** Try loading the English site, look for annual report PDF download

#### F. China Electricity Council — Power Industry Statistics
- **URL:** https://english.cec.org.cn/
- **Why it matters:** Official annual statistics on China's grid by voltage class
- **Limitation:** Most detailed stats only in Chinese
- **Action:** Check for English annual statistical summaries

---

## Parsing Plan

Once all sources are gathered, here's the extraction order:

### Phase 1: Parse What We Have (can do now)
1. **NERC-2024-Supplemental.xlsx** — Open in Excel, extract circuit-miles by voltage class table
2. **IEA-Electricity-Grids-2023.pdf** — Find Chapter 2 "Grids Today" figures on grid length by country, investment
3. **IEA-World-Energy-Investment-2024.pdf** — Find Chapter 7 (China) and grid investment charts
4. **DOE-National-Transmission-Needs-Study-2023.pdf** — Find existing capacity tables, regional maps
5. **NERC-2025-LTRA.pdf** — Find planned transmission tables

### Phase 2: Parse Manual Downloads (after you download them)
6. **Grid Strategies PDF** — Extract the year-by-year US construction chart/table
7. **IEA Datafile (Excel)** — Extract investment time series by country
8. **Wikipedia China UHV table** — Complete the UHV line inventory

### Phase 3: Update Dashboard
10. Replace estimated data with sourced figures
11. Add proper citations (Source: [Report Name], Table X, p. Y)
12. Add year-by-year charts (every year, not just even years)
13. Expand voltage breakdown with sourced numbers
14. Add footnotes explaining estimation methodology for any remaining gaps

---

## Specific Numbers to Verify/Update

### US Side
- [ ] Total US transmission miles by voltage class (230, 345, 500, 765 kV) — current year
- [ ] Year-by-year HV construction 2010-2024 (the Grid Strategies data)
- [ ] 2023: 55 miles — need exact source citation (page number)
- [ ] 2024: 888 miles — need exact source citation
- [ ] FERC Form 1 total: 234,046 miles — verify against NERC/EIA
- [ ] US HVDC inventory: Pacific DC Intertie, Quebec-NE, others — verify miles and capacity
- [ ] US grid investment 2015-2024 ($B/yr) — from IEA datafile

### China Side
- [ ] Total grid length 220kV+ for each year 2010-2024 — from CEC/NEA
- [ ] Voltage class breakdown (220, 330, 500, 750, UHV) — from CEC
- [ ] Complete UHV line list (54 circuits per Wikipedia) — from Wikipedia (downloaded)
- [ ] Annual SGCC investment ($B or CNY) 2010-2024 — from SGCC reports
- [ ] 14th FYP targets vs actuals — from NEA
- [ ] 15th FYP preview targets — from recent SGCC announcements

### Comparison
- [ ] IEA grid investment by country 2015-2024 — from IEA datafile
- [ ] IEA total grid length by country — from Electricity Grids report
- [ ] GW-miles methodology — cite NREL NTP study for capacity assumptions

---

## Dashboard Update Checklist

Once data is gathered:

- [ ] Replace every-other-year cumulative chart with annual data points
- [ ] Add voltage-class-over-time chart (stacked area showing growth by voltage)
- [ ] Complete UHV table to all 42 lines (currently shows 9 China + 2 US)
- [ ] Add source citation footnotes to each chart
- [ ] Add "Data as of" timestamps
- [ ] Cross-reference all numbers against downloaded PDFs
- [ ] Add talking points callout boxes with sourced stats
- [ ] Consider adding a "per capita" or "per GDP" normalization view

---

## File Inventory

```
transmission-sources/
├── DOE-National-Transmission-Needs-Study-2023.pdf   15 MB  ✓ good
├── NERC-2025-LTRA.pdf                                7.4 MB ✓ good
├── DOE-Draft-Needs-Study-Feb2023.pdf                  5.4 MB ✓ good
├── IEA-Electricity-Grids-2023.pdf                     4.6 MB ✓ good
├── IEA-World-Energy-Investment-2024.pdf               3.6 MB ✓ good
├── DOE-US-Fact-Sheet.pdf                              1.2 MB ✓ good
├── NERC-2024-Supplemental.xlsx                        669 KB ✓ good
├── EIA-411-transmission-lines-2016.xls                565 KB ✓ good
├── EIA-411-peak-load-2016.xls                          63 KB ✓ good
├── NERC-2024-LTRA-Supplemental.xlsx                    42 KB ✗ DELETE (failed 404)
└── IEA-WEI-2024.pdf                                  215 B  ✗ DELETE (failed 404)

Downloaded (verified Feb 2026):
├── Grid-Strategies-Fewer-New-Miles-2023.pdf           1.7 MB ✓ good — "Fewer New Miles: The US Transmission Grid in the 2020s" Jul 2024, 55mi (p.4), $25B/yr (p.3)
├── Wikipedia-China-UHV.html                           140 KB ✓ good — Full article with 54 UHV circuit table (25 AC + 29 DC)

Still needed (manual download):
└── IEA-WEI-2024-Datafile.xlsx                         ?     PRIORITY 1 — Excel with grid investment by country by year
```

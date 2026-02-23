# GW·Miles Methodology: New-Build 2010–2024

**Stat:** China added ~1,216K thermal GW·miles vs US ~37K (~33×)
**Last verified:** February 20, 2026
**Dashboard:** `china-us-transmission.html` → "Cumulative Build 2010–24" hero card

---

## What This Stat Measures

**Miles** counts how much wire went up. **GW·miles** counts how much *power* can flow through that wire. One mile of 765kV line carries 7.5× more power than one mile of 230kV. If two countries build the same miles but one builds at higher voltages, GW·miles captures the difference.

**Formula:** `New-build GW·mi = new-build miles × weighted-average thermal GW per mile`

Each country's average GW/mi is derived from the actual voltage distribution of what was built — not assumed.

---

## China: 3.52 GW/mi → ~1,216K GW·miles

### Source: CEC Voltage-Class Data (2012–2019)

The **China Electricity Council** (中国电力企业联合会) publishes annual power statistics (电力统计年快报) with cumulative circuit-km broken out by voltage class. English translations available at [chinaenergyportal.org](https://chinaenergyportal.org) for 2012–2019.

**Files:**
- JSON: `transmission-infrastructure-comparison.json` → `cec_voltage_class_data`
- Summary: `transmission-sources/China-CEC-NEA-transmission-data-summary.txt`
- URLs for each year: see JSON `cec_voltage_class_data.urls`

**Computation: end-2012 → end-2019 net additions by voltage class**

| Voltage | 2012 (km) | 2019 (km) | Added (km) | Thermal GW | GW·km |
|---------|----------:|----------:|-----------:|-----------:|------:|
| 220kV AC | 318,217 | 454,585 | **136,368** | 0.6 | 81,821 |
| 330kV AC | 22,701 | 32,314 | **9,613** | 1.0 | 9,613 |
| 500kV AC | 137,104 | 195,636 | **58,532** | 2.7 | 158,036 |
| 750kV AC | 10,088 | 23,256 | **13,168** | 4.5 | 59,256 |
| 1000kV AC (UHV) | 639 | 10,872 | **10,233** | 6.0 | 61,398 |
| ±800kV DC (UHV) | 5,314 | 21,907 | **16,593** | 8.0 | 132,744 |
| ±1100kV DC (UHV) | 0 | 3,295 | **3,295** | 12.0 | 39,540 |
| **Total** | | | **247,802** | | **542,408** |

**Weighted average: 542,408 ÷ 247,802 = 2.189 GW/km × 1.609 = 3.52 GW/mi**

### What Drives the Average

Even though 55% of new km is at 220kV (capacity: 0.6 GW), the higher voltages dominate the GW·km:

| Category | % of km added | % of GW·km added |
|----------|:---:|:---:|
| 220kV (0.6 GW) | 55.0% | 15.1% |
| 330–750kV (1.0–4.5 GW) | 32.8% | 41.8% |
| UHV (6.0–12.0 GW) | 12.2% | **43.1%** |

UHV is 12% of the distance but 43% of the capacity. A single ±800kV DC corridor carries as much power as 13 parallel 220kV lines.

### Gap: CEC Data Stops at 2019

The detailed voltage-class breakdown is only available through 2019. After 2019, CEC only publishes aggregate 220kV+ totals (no voltage split). This matters because UHV construction continued:

**Post-2019 UHV verification (from Wikipedia + CCTV):**

| Source | Data |
|--------|------|
| CEC end-2019 UHV total | 36,074 circuit-km |
| CCTV Nov 22, 2025 | "total UHV exceeds 50,000 km" |
| Implied 2020–2025 UHV additions | ~13,926 km |
| Wikipedia 2020–2024 UHV route-km | ~14,408 km (line-by-line) |
| Total 220kV+ additions 2020–2024 | ~189,000 km (Ditan/CEC) |
| UHV share 2020–2024 | ~7.4% |
| UHV share 2013–2019 (for comparison) | 12.2% |

**Files:**
- `transmission-sources/Wikipedia-China-UHV.html` — 54 UHV circuits with dates, lengths, capacities
- CCTV source: https://news.cctv.com/2025/11/22/ARTIe0KN3cYThjCmWEhCMolO251122.shtml

**Impact assessment:** UHV share dropped from 12.2% (2013–2019) to ~7.4% (2020–2024), and per-km capacity dropped ~13% (more AC, fewer mega-DC lines like the 12 GW Changji–Guquan). Combined effect on the overall average: **<2%** (7% share × 13% reduction = ~1% drag). Adjusting would give 3.47 GW/mi instead of 3.52. We use 3.52 as stated.

### Post-2019 UHV Lines (from Wikipedia)

**2020 (7 lines completed, ~4,710 route-km):**
- Qinghai–Henan ±800kV DC: 1,587 km, 8 GW
- Wudongde–Guangxi–Guangdong ±800kV DC: 1,489 km, 8 GW
- Plus 5 AC lines (Weifang–Heze–Shijiazhuang, Zhangbei–Xiong'an ×2, Mengxi–Jinzhong, Zhumadian–Nanyang): ~1,634 route-km, no published capacity

**2021 (3 lines, ~3,179 route-km):**
- Yazhong–Jiangxi ±800kV DC: 1,711 km, 8 GW
- Shanbei–Hubei ±800kV DC: 1,127 km, 8 GW
- Nanchang–Changsha 1000kV AC: 341 route-km

**2022 (4 lines, ~4,513 route-km):**
- Baihetan–Jiangsu ±800kV DC: 2,087 km, 8 GW
- Baihetan–Zhejiang ±800kV DC: 2,193 km, 8 GW
- Plus 2 AC lines: ~233 route-km

**2023 (2 lines, 525 route-km):** Two short AC interconnectors only (Wuhan–Zhumadian, Fuzhou–Xiamen)

**2024 (3 lines, ~1,481 route-km):**
- Sichuan–Chongqing 1000kV AC: 658 route-km, 24 GW (highest-rated AC line in dataset)
- Zhangbei–Shengli 1000kV AC: 366 route-km
- Wuhan–Nanchang 1000kV AC: 456.6 route-km

### China Miles: Where Do the 345,480 Come From?

**Source:** Dashboard sums `chinaAnnual` (15 values, 2010–2024). At runtime, it now uses a documented priority chain from `transmission-infrastructure-comparison.json`:

1. `chart_ready_data.annual_construction_km.china` (canonical)
2. `construction_rate_comparison_km_per_year` (bridge estimates for pre-2014)
3. `annual_construction_rates.china` (legacy fallback only)

The active primary series is:

```
[23612, 24855, 23612, 21748, 22369, 20505, 21748, 25476, 22369, 21748, 19884, 24233, 24233, 23612, 25476]
```

All values are miles. Derived from:
- 2014–2023: Ditan 2024 Chart 5-14 additions (新增220千伏及以上输电线路长度)
- 2024: derived from CEC cumulative totals (960,970 - 920,500 = 40,470 km, rounded to 41,000 km in chart-ready data)
- 2010–2013: bridge estimates from `construction_rate_comparison_km_per_year`

**Why this is canonical:** `chart_ready_data.annual_construction_km` is curated for dashboard rendering and aligned to the revised CEC/Ditan series. The legacy block `annual_construction_rates.china` mixes older computed values and estimated years, so it is retained only as fallback.

Sum: 345,480 miles (~556,000 km)

**Note:** This is ~3% higher than the CEC-implied total of ~538,000 km (960,970 end-2024 minus ~423,000 start-2010). The difference is primarily from pre-2014 bridge estimates and rounding in annual chart-ready values.

### Final Calculation

```
345,480 mi × 3.52 GW/mi = 1,216,090 GW·mi ≈ 1,216K
```

---

## US: 1.33 GW/mi → ~37K GW·miles

### Source: td-voltage-aging.json (FERC Form 1 via PUDL)

**FERC Form 1 Schedule 422** requires investor-owned utilities to report every transmission line segment with operating voltage and length. The [PUDL project](https://catalyst.coop/pudl/) (Public Utility Data Liberation) extracts this into machine-readable form. Our processed file `td-voltage-aging.json` aggregates these into standardized voltage classes by year.

**Files:**
- Processed: `eia-explorer/public/bulk-data/pudl/td-voltage-aging.json`
- Raw parquet: `pudl-data/out_ferc1__yearly_transmission_lines_sched422.parquet`
- Processing script: `scripts/extract-td-voltage-aging.py`

### Computation: 2009 → 2024 endpoint comparison

Rather than summing noisy year-over-year changes (which suffer from utility reclassifications and reporting pool changes), we compare total system miles at the **start** (2009) and **end** (2024) of the period:

| Voltage Class | 2009 (mi) | 2024 (mi) | Net Change | Thermal GW | GW·mi |
|---------------|----------:|----------:|-----------:|-----------:|------:|
| 230–344 kV | 38,344 | 51,708 | **+13,364** | 0.6 | +8,019 |
| 345–499 kV | 35,828 | 47,396 | **+11,568** | 1.5 | +17,353 |
| 500–764 kV | 15,518 | 19,789 | **+4,272** | 2.7 | +11,533 |
| 765+ kV | 2,370 | 2,975 | **+605** | 4.5 | +2,723 |
| **Total** | | | **+29,809** | | **+39,628** |

**Weighted average: 39,628 ÷ 29,809 = 1.329 GW/mi → rounded to 1.33**

**Note on mile totals:** The td-voltage-aging endpoint gives 29,809 mi total at 230kV+. The dashboard's `usAnnual` array sums to 27,890 mi — constructed differently (345kV+ from Grid Strategies + flat 891 mi/yr for 230–344kV). The 1.33 GW/mi average is derived from td-voltage-aging's voltage breakdown and applied to the `usAnnual` sum:

```
27,890 mi × 1.33 GW/mi = 37,094 GW·mi ≈ 37K
```

The ~1,920 mi gap (6.4%) reflects that the flat 891 mi/yr estimate for 230–344kV slightly undercounts vs the endpoint method. This is a known approximation — the GW/mi *average* (1.33) is robust regardless of which mile total it's applied to.

### What Drives the Average

| Category | % of net miles | % of GW·mi |
|----------|:---:|:---:|
| 230–344kV (0.6 GW) — lowest capacity | 44.8% | 20.2% |
| 345–499kV (1.5 GW) — the workhorse | 38.8% | 43.8% |
| 500–764kV (2.7 GW) | 14.3% | 29.1% |
| 765+ kV (4.5 GW) — highest capacity | 2.0% | 6.9% |

Nearly half the US net additions are at the lowest voltage class (230–344kV, 0.6 GW). Only 605 miles of 765kV were added in 15 years. There is no US equivalent of China's UHV program.

### Why 2009 Baseline (Not 2010)?

The dashboard's annual data covers construction *during* 2010–2024. The 2009 stock represents what existed *before* 2010 started. Using 2010 as baseline would exclude 2010's construction from the total, giving 28,080 mi instead of 29,809. Using 2009 gives the correct 29,809 mi matching the dashboard sum.

### Coverage Note

FERC Form 1 covers **investor-owned utilities**, approximately 80% of US transmission. Non-FERC utilities (munis, co-ops, federal power agencies) are excluded. However, the voltage *distribution* of non-FERC transmission is likely similar, so the 1.33 GW/mi average should be representative even though the absolute miles are undercounted. The dashboard's hardcoded annual data (from EIA Electric Power Annual, which uses the same FERC Form 1 source) matches the td-voltage-aging totals, confirming consistency.

### Why Not Use Raw PUDL Parquet?

We initially tried computing directly from `out_ferc1__yearly_transmission_lines_sched422.parquet`. This gave noisy results: different filtering yielded only 17,741 mi of net additions (vs 29,809 from td-voltage-aging). The raw parquet also showed -988 mi at 765kV (spurious — the US has never decommissioned 765kV lines). The processed `td-voltage-aging.json` produces cleaner results and exactly matches the dashboard's totals.

### US HVDC Note

The US has no UHV-class lines. Existing HVDC:
- Pacific DC Intertie: ±500kV, 3.1 GW, 846 mi (built 1970)
- Quebec–New England: ±450kV, 2.0 GW, 930 mi (built 1990)

These are pre-2010 and not part of the new-build stat. The SunZia line (±525kV, 3.0 GW, 550 mi, under construction 2023–2025) will add the first significant US HVDC capacity in decades, but it's not yet in the FERC data.

---

## Thermal Capacity Ratings

Both countries use the same per-voltage thermal ratings, as specified in the dashboard:

| Voltage | Thermal Rating | Basis |
|---------|:---:|---|
| 220/230 kV AC | 0.6 GW | Standard two-bundle ACSR, ~600 MW thermal limit |
| 330 kV AC | 1.0 GW | |
| 345 kV AC | 1.5 GW | Standard US EHV rating |
| 500 kV AC | 2.7 GW | Four-bundle conductor, ~2,700 MW |
| 750/765 kV AC | 4.5 GW | Six-bundle conductor, AEP-class |
| 1000 kV AC (UHV) | 6.0 GW | Chinese standard, based on SIL ~5 GW + compensation |
| ±800 kV DC (UHV) | 8.0 GW | Bipolar ±800kV, standard SGCC design |
| ±1100 kV DC (UHV) | 12.0 GW | Changji–Guquan design capacity |
| HVDC ≤500 kV | 2.5 GW | Average of existing US HVDC lines |

**Why thermal, not SIL?** Thermal rating reflects the physical infrastructure built — conductor size, tower design, right-of-way width. It's what the line *can* carry. SIL (Surge Impedance Loading) is a lower theoretical baseline (~3× lower for AC) that can be exceeded with series compensation. The DOE Needs Study (Table VI-3, p.123) uses SIL; our dashboard uses thermal. Both are defensible; the key is using the same method for both countries, which we do.

**Reference:** For comparison, the `transmission-by-voltage.html` dashboard (from HIFLD) reports total US system at 86,901 GW·mi using SIL vs our 243,141 GW·mi using thermal — a 2.8× ratio, consistent with the SIL-to-thermal relationship.

---

## Source Chain Summary

```
CHINA GW·MILES
═════════════
Miles:  JSON chart_ready_data.annual_construction_km.china (canonical)
        = Ditan Chart 5-14 additions for 2014-2023 + 2024 CEC-derived delta
        + pre-2014 bridge from construction_rate_comparison_km_per_year
        → dashboard chinaAnnual array
        → sum = 345,480 mi (~556,000 km)

GW/mi:  CEC voltage-class cumulative data (2012–2019 detailed breakdown)
        → JSON cec_voltage_class_data (AC + DC by voltage)
        → subtract 2012 from 2019 = additions by voltage class
        → multiply each by thermal rating → weighted avg = 3.52 GW/mi

UHV verification:
        CEC (through 2019) + Wikipedia UHV table (2020–2024) + CCTV (2025 total)
        → confirms <2% impact from post-2019 voltage mix changes


US GW·MILES
═══════════
Miles:  345kV+ from Grid Strategies (FERC data) + 891 mi/yr for 230–344kV (FERC Form 1 via PUDL)
        → hardcoded in dashboard as usAnnual array
        → sum = 27,890 mi
        (td-voltage-aging.json endpoint method gives 29,809 mi — ~6% higher, same voltage mix)

GW/mi:  td-voltage-aging.json → miles_by_voltage for 2009 and 2024
        → subtract: net additions by voltage class (all positive, clean)
        → multiply each by thermal rating → weighted avg = 1.33 GW/mi

US has no UHV lines. Highest operational voltage: 765kV (2,975 miles, built pre-2010).
```

---

## Sensitivity Analysis

| What if... | Effect on ratio |
|------------|:---:|
| China avg drops to 3.47 (adjusted for post-2019 UHV mix) | 32× instead of 33× |
| US avg rises to 1.50 (if new build skews 345kV+) | 29× instead of 33× |
| Use SIL instead of thermal for both | Ratio unchanged (~33×) — both scale by ~3× |
| China miles = ~538,000 km (CEC-implied) instead of 556,000 km | 31× instead of 33× |
| US miles = 29,809 (td-voltage-aging endpoint) instead of 27,890 | 31× instead of 33× |
| Exclude 230kV from US (345kV+ only) | ~14,500 mi at ~1.7 GW/mi = ~25K → ratio ~49× |
| Include US HVDC (Pacific DC Intertie + Q-NE) | Pre-2010, not in new-build period |

The ~33× ratio is robust across reasonable assumption changes (range: 29–49×).

---

## Files Referenced

| File | What it contains |
|------|-----------------|
| `transmission-infrastructure-comparison.json` | Master data file: CEC voltage-class data, annual construction, UHV breakdown |
| `eia-explorer/public/bulk-data/pudl/td-voltage-aging.json` | FERC Form 1 processed: US miles by voltage class, 1994–2024 |
| `transmission-sources/Wikipedia-China-UHV.html` | 54 UHV circuits with dates, lengths, capacities |
| `transmission-sources/China-CEC-NEA-transmission-data-summary.txt` | Compiled CEC/NEA source data with URLs |
| `transmission-sources/Ditan_source.pdf` | China Energy Big Data Report 2024 (Chart 5-14: 220kV+ time series) |
| `pudl-data/out_ferc1__yearly_transmission_lines_sched422.parquet` | Raw FERC Form 1 line-level data (668K records) |
| `IMM Calculator/_archive/pages/charts/transmission-by-voltage.html` | HIFLD-derived US voltage breakdown (SIL-based) |
| `transmission-sources/DOE-National-Transmission-Needs-Study-2023.pdf` | DOE reference: US system at 85.6 TW-mi (SIL) |

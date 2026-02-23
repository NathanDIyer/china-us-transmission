# Reconciled US Projected Miles by Voltage Class

Updated: 2026-02-23

## Objective
Create one unified projected-lines series by voltage class with no double counting across NERC, ISO/RTO disclosures, and Our Grid Future project data.

## Inputs
- NERC 2024 Supplemental, Table L (planned circuit-miles by voltage class).
- Our Grid Future Planned Transmission Projects Feb 2026 (project-level segments; proposed set excludes Complete + Terminated).
- ISO/RTO class-specific disclosures where voltage class is explicit:
  - MISO ~5,000 mi at 345kV and ~1,750 mi at 765kV (NERC 2025 LTRA p.48)
  - SPP 2025 ITP: 2,087 mi new 765kV
  - PJM 2024 RTEP back-out: 417 mi at 765kV
  - NYISO CHPE: 339 mi at 320kV

## No-Double-Count Formula
For each voltage class c:

`UnifiedLowerBound(c) = max(NERC(c), OGF(c), ISO(c))`

Rationale: the union of overlapping datasets is always at least the maximum contributor in each class. Using max() guarantees no additive double counting.

## Why This Is the Most Accurate Defensible Merge
- NERC Table L provides an audited national baseline by voltage class.
- OGF provides project-level segments and current status labels, often above NERC in higher classes.
- ISO/RTO values are only used where voltage class is explicit and traceable to specific disclosures.
- Summing NERC + OGF + ISO is invalid because of overlapping project coverage. max() is conservative and reproducible.

## Scope + Limits
- This output is a lower-bound union by class, not a full de-duplicated project graph.
- Low-confidence PDF text-mined candidates are intentionally excluded from totals.
- ISO/RTO disclosures without explicit voltage-class miles are intentionally excluded from class totals.

## Reconciled Totals
- NERC 200kV+: 15,099.0 mi
- OGF proposed 200kV+: 34,458.1 mi
- ISO class-specific 200kV+: 9,593.0 mi
- Unified lower bound 200kV+: 35,366.9 mi

## By Voltage Class

| Voltage | NERC | OGF | ISO | Unified lower bound | Controlling source |
|---|---:|---:|---:|---:|---|
| 100-199 kV | 3,470.0 | 182.0 | 0.0 | 3,470.0 | NERC Table L |
| 200-299 kV | 5,373.0 | 4,464.2 | 0.0 | 5,373.0 | NERC Table L |
| 300-399 kV | 6,067.0 | 13,667.38 | 5,339.0 | 13,667.38 | Our Grid Future |
| 400-599 kV | 3,496.0 | 11,221.32 | 0.0 | 11,221.32 | Our Grid Future |
| 600+ kV | 163.0 | 5,105.2 | 4,254.0 | 5,105.2 | Our Grid Future |

## Source Trace Files
- Per-class table: `transmission-sources/ourgridfuture/extracted/reconciled_us_projected_miles_by_voltage_class.csv`
- Machine summary: `transmission-sources/ourgridfuture/extracted/reconciled_us_projected_miles_summary.json`
- Row-level trace table: `transmission-sources/ourgridfuture/extracted/reconciled_us_projected_miles_source_trace.csv`


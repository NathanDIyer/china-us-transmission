#!/usr/bin/env python3
"""Reconcile US projected transmission miles by voltage class (no double counting).

Method:
- Compute per-voltage-class miles from Our Grid Future proposed projects
  (exclude Status = Complete or Terminated).
- Combine with NERC Table L per-voltage-class planned miles.
- Add ISO/RTO disclosed mileage where voltage class is explicitly available.
- Build unified lower bound per class as:
    max(NERC miles, OGF miles, ISO disclosed miles)
  This avoids double counting while integrating multiple sources.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
import json

import pandas as pd


ROOT = Path(__file__).resolve().parent
EXTRACTED = ROOT / "extracted"
PROJECTS_CSV = EXTRACTED / "planned_transmission_projects.csv"

OUT_CSV = EXTRACTED / "reconciled_us_projected_miles_by_voltage_class.csv"
OUT_JSON = EXTRACTED / "reconciled_us_projected_miles_summary.json"
OUT_MD = EXTRACTED / "reconciled_us_projected_miles_methodology.md"
OUT_TRACE_CSV = EXTRACTED / "reconciled_us_projected_miles_source_trace.csv"


VOLTAGE_ROWS = [
    ("kv100_199", "100-199 kV"),
    ("kv200_299", "200-299 kV"),
    ("kv300_399", "300-399 kV"),
    ("kv400_599", "400-599 kV"),
    ("kv600_plus", "600+ kV"),
]

NERC_TABLE_L_MILES = {
    "kv100_199": 3470.0,
    "kv200_299": 5373.0,
    "kv300_399": 6067.0,
    "kv400_599": 3496.0,
    "kv600_plus": 163.0,
}

# ISO/RTO class-specific disclosed values (only where class is explicit).
# Sources:
# - NERC 2025 LTRA p.48: MISO ~5,000 mi 345kV and ~1,750 mi 765kV
# - SPP 2025 ITP: 2,087 mi new 765kV
# - PJM 2024 RTEP back-out: 417 mi at 765kV (named B4000 corridors)
# - NYISO CHPE: 339 mi at 320kV (DC)
ISO_DISCLOSED_BY_CLASS = {
    "kv100_199": 0.0,
    "kv200_299": 0.0,
    "kv300_399": 5000.0 + 339.0,
    "kv400_599": 0.0,
    "kv600_plus": 1750.0 + 2087.0 + 417.0,
}

NERC_TABLE_L_TRACE = "transmission-sources/NERC-2024-Supplemental.xlsx (Table L: planned circuit-miles by voltage class)"
OGF_TRACE = (
    "transmission-sources/ourgridfuture/extracted/planned_transmission_projects.csv "
    "(Status normalized excludes Complete/Terminated; grouped by Maximum voltage (kV))"
)
ISO_TRACE_BY_CLASS = {
    "kv100_199": "No class-specific ISO/RTO disclosure used for this class.",
    "kv200_299": "No class-specific ISO/RTO disclosure used for this class.",
    "kv300_399": (
        "MISO ~5,000 mi at 345kV from transmission-sources/NERC-2025-LTRA.pdf p.48 "
        "+ NYISO CHPE 339 mi at 320kV (public project disclosures)."
    ),
    "kv400_599": "No class-specific ISO/RTO disclosure used for this class.",
    "kv600_plus": (
        "MISO ~1,750 mi at 765kV from transmission-sources/NERC-2025-LTRA.pdf p.48 "
        "+ SPP 2025 ITP 2,087 mi at 765kV (transmission-sources/iso-rto-forward/SPP-2025-ITP-Report-v1.0.pdf) "
        "+ PJM 2024 RTEP back-out 417 mi at 765kV (transmission-sources/iso-rto-forward/PJM-2024-RTEP-Report.pdf)."
    ),
}


def controlling_source_detail(key: str, unified: float, nerc: float, ogf: float, iso: float) -> str:
    if unified == ogf:
        return "Our Grid Future controls (highest class value after status filtering)."
    if unified == nerc:
        return "NERC Table L controls (higher than OGF and ISO class-specific disclosures)."
    return "ISO/RTO class-specific disclosure controls (higher than NERC and OGF)."


def class_key(max_kv: float) -> str | None:
    if pd.isna(max_kv):
        return None
    v = float(max_kv)
    if 100 <= v < 200:
        return "kv100_199"
    if 200 <= v < 300:
        return "kv200_299"
    if 300 <= v < 400:
        return "kv300_399"
    if 400 <= v < 600:
        return "kv400_599"
    if v >= 600:
        return "kv600_plus"
    return None


def load_ogf_by_class() -> dict[str, float]:
    if not PROJECTS_CSV.exists():
        raise FileNotFoundError(f"Missing extracted projects CSV: {PROJECTS_CSV}")

    df = pd.read_csv(PROJECTS_CSV)
    df["Status normalized"] = df["Status normalized"].fillna("").astype(str).str.strip()
    df["Maximum voltage (kV)"] = pd.to_numeric(df["Maximum voltage (kV)"], errors="coerce")
    df["Length (mi)"] = pd.to_numeric(df["Length (mi)"], errors="coerce").fillna(0.0)

    proposed = df[~df["Status normalized"].isin(["Complete", "Terminated"])].copy()
    proposed["class_key"] = proposed["Maximum voltage (kV)"].map(class_key)
    proposed = proposed[proposed["class_key"].notna()].copy()

    grouped = proposed.groupby("class_key")["Length (mi)"].sum().to_dict()
    out = {k: float(grouped.get(k, 0.0)) for k, _ in VOLTAGE_ROWS}
    return out


def build() -> tuple[pd.DataFrame, dict]:
    ogf_by_class = load_ogf_by_class()
    rows = []
    for key, label in VOLTAGE_ROWS:
        nerc = float(NERC_TABLE_L_MILES.get(key, 0.0))
        ogf = float(ogf_by_class.get(key, 0.0))
        iso = float(ISO_DISCLOSED_BY_CLASS.get(key, 0.0))
        unified = max(nerc, ogf, iso)
        if unified == ogf:
            controlling = "Our Grid Future"
        elif unified == nerc:
            controlling = "NERC Table L"
        else:
            controlling = "ISO/RTO disclosed"

        rows.append(
            {
                "voltage_class_key": key,
                "voltage_class": label,
                "nerc_table_l_miles": round(nerc, 2),
                "our_grid_future_proposed_miles": round(ogf, 2),
                "iso_rto_disclosed_miles": round(iso, 2),
                "unified_lower_bound_miles": round(unified, 2),
                "controlling_source": controlling,
                "controlling_source_detail": controlling_source_detail(key, unified, nerc, ogf, iso),
                "formula": "max(NERC, OGF, ISO)",
                "nerc_trace": NERC_TABLE_L_TRACE,
                "our_grid_future_trace": OGF_TRACE,
                "iso_rto_trace": ISO_TRACE_BY_CLASS.get(key, ""),
            }
        )

    out_df = pd.DataFrame(rows)
    if not (
        (out_df["unified_lower_bound_miles"] >= out_df["nerc_table_l_miles"]).all()
        and (out_df["unified_lower_bound_miles"] >= out_df["our_grid_future_proposed_miles"]).all()
        and (out_df["unified_lower_bound_miles"] >= out_df["iso_rto_disclosed_miles"]).all()
    ):
        raise ValueError("Unified lower-bound check failed: at least one class is below an input source.")

    high_voltage = out_df[out_df["voltage_class_key"].isin(["kv200_299", "kv300_399", "kv400_599", "kv600_plus"])]
    summary = {
        "updated_on": date.today().isoformat(),
        "method": "lower_bound_no_double_count_max_by_voltage_class",
        "method_definition": "UnifiedLowerBound(c) = max(NERC(c), OGF(c), ISO(c))",
        "conservatism_note": (
            "This is a lower bound of the cross-source union. It prevents additive double counting, "
            "but may understate the true union where sources contain distinct non-overlapping projects "
            "inside the same voltage class."
        ),
        "totals_miles": {
            "nerc_table_l_100kv_plus": round(float(out_df["nerc_table_l_miles"].sum()), 2),
            "nerc_table_l_200kv_plus": round(float(high_voltage["nerc_table_l_miles"].sum()), 2),
            "our_grid_future_proposed_100kv_plus": round(float(out_df["our_grid_future_proposed_miles"].sum()), 2),
            "our_grid_future_proposed_200kv_plus": round(float(high_voltage["our_grid_future_proposed_miles"].sum()), 2),
            "iso_rto_disclosed_class_specific_200kv_plus": round(float(high_voltage["iso_rto_disclosed_miles"].sum()), 2),
            "unified_lower_bound_100kv_plus": round(float(out_df["unified_lower_bound_miles"].sum()), 2),
            "unified_lower_bound_200kv_plus": round(float(high_voltage["unified_lower_bound_miles"].sum()), 2),
        },
        "classes": rows,
    }

    return out_df, summary


def write_methodology(df: pd.DataFrame, summary: dict) -> None:
    lines = [
        "# Reconciled US Projected Miles by Voltage Class",
        "",
        f"Updated: {summary['updated_on']}",
        "",
        "## Objective",
        "Create one unified projected-lines series by voltage class with no double counting across NERC, ISO/RTO disclosures, and Our Grid Future project data.",
        "",
        "## Inputs",
        "- NERC 2024 Supplemental, Table L (planned circuit-miles by voltage class).",
        "- Our Grid Future Planned Transmission Projects Feb 2026 (project-level segments; proposed set excludes Complete + Terminated).",
        "- ISO/RTO class-specific disclosures where voltage class is explicit:",
        "  - MISO ~5,000 mi at 345kV and ~1,750 mi at 765kV (NERC 2025 LTRA p.48)",
        "  - SPP 2025 ITP: 2,087 mi new 765kV",
        "  - PJM 2024 RTEP back-out: 417 mi at 765kV",
        "  - NYISO CHPE: 339 mi at 320kV",
        "",
        "## No-Double-Count Formula",
        "For each voltage class c:",
        "",
        "`UnifiedLowerBound(c) = max(NERC(c), OGF(c), ISO(c))`",
        "",
        "Rationale: the union of overlapping datasets is always at least the maximum contributor in each class. Using max() guarantees no additive double counting.",
        "",
        "## Why This Is the Most Accurate Defensible Merge",
        "- NERC Table L provides an audited national baseline by voltage class.",
        "- OGF provides project-level segments and current status labels, often above NERC in higher classes.",
        "- ISO/RTO values are only used where voltage class is explicit and traceable to specific disclosures.",
        "- Summing NERC + OGF + ISO is invalid because of overlapping project coverage. max() is conservative and reproducible.",
        "",
        "## Scope + Limits",
        "- This output is a lower-bound union by class, not a full de-duplicated project graph.",
        "- Low-confidence PDF text-mined candidates are intentionally excluded from totals.",
        "- ISO/RTO disclosures without explicit voltage-class miles are intentionally excluded from class totals.",
        "",
        "## Reconciled Totals",
        f"- NERC 200kV+: {summary['totals_miles']['nerc_table_l_200kv_plus']:,} mi",
        f"- OGF proposed 200kV+: {summary['totals_miles']['our_grid_future_proposed_200kv_plus']:,} mi",
        f"- ISO class-specific 200kV+: {summary['totals_miles']['iso_rto_disclosed_class_specific_200kv_plus']:,} mi",
        f"- Unified lower bound 200kV+: {summary['totals_miles']['unified_lower_bound_200kv_plus']:,} mi",
        "",
        "## By Voltage Class",
        "",
        "| Voltage | NERC | OGF | ISO | Unified lower bound | Controlling source |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for _, r in df.iterrows():
        lines.append(
            f"| {r['voltage_class']} | {r['nerc_table_l_miles']:,} | {r['our_grid_future_proposed_miles']:,} | {r['iso_rto_disclosed_miles']:,} | {r['unified_lower_bound_miles']:,} | {r['controlling_source']} |"
        )

    lines.extend(
        [
            "",
            "## Source Trace Files",
            f"- Per-class table: `{OUT_CSV.relative_to(ROOT.parent.parent)}`",
            f"- Machine summary: `{OUT_JSON.relative_to(ROOT.parent.parent)}`",
            f"- Row-level trace table: `{OUT_TRACE_CSV.relative_to(ROOT.parent.parent)}`",
            "",
        ]
    )

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    df, summary = build()
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False)
    df[
        [
            "voltage_class_key",
            "voltage_class",
            "nerc_table_l_miles",
            "our_grid_future_proposed_miles",
            "iso_rto_disclosed_miles",
            "unified_lower_bound_miles",
            "formula",
            "controlling_source",
            "controlling_source_detail",
            "nerc_trace",
            "our_grid_future_trace",
            "iso_rto_trace",
        ]
    ].to_csv(OUT_TRACE_CSV, index=False)
    OUT_JSON.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    write_methodology(df, summary)

    print(f"Wrote: {OUT_CSV}")
    print(f"Wrote: {OUT_TRACE_CSV}")
    print(f"Wrote: {OUT_JSON}")
    print(f"Wrote: {OUT_MD}")
    print(f"Unified lower bound 200kV+: {summary['totals_miles']['unified_lower_bound_200kv_plus']:.2f} mi")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extract and summarize Our Grid Future planned transmission dataset."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from zipfile import ZipFile

import pandas as pd


ROOT = Path(__file__).resolve().parent
INPUT_XLSX = ROOT / "OurGridFuture_PlannedTransmissionProjects_Feb2026.xlsx"
INPUT_ZIP = ROOT / "OurGridFuture_PlannedTransmissionProjects_Feb2026.zip"
UNZIPPED_DIR = ROOT / "OurGridFuture_PlannedTransmissionProjects_Feb2026"
INPUT_METADATA_TXT = UNZIPPED_DIR / "INFO_PlannedProjects_Metadata_Feb2026.txt"
OUTPUT_DIR = ROOT / "extracted"


def normalize_status(series: pd.Series) -> pd.Series:
    return (
        series.fillna("")
        .astype(str)
        .str.strip()
        .replace({"": "Unspecified"})
    )


def to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def voltage_class(max_kv: float) -> str:
    if pd.isna(max_kv):
        return "Unknown"
    value = float(max_kv)
    if value < 230:
        return "<230 kV"
    if value < 300:
        return "230-299 kV"
    if value < 400:
        return "300-399 kV"
    if value < 600:
        return "400-599 kV"
    return "600+ kV"


def read_metadata_text() -> str:
    if INPUT_METADATA_TXT.exists():
        return INPUT_METADATA_TXT.read_text(encoding="utf-8", errors="replace").strip()

    if INPUT_ZIP.exists():
        with ZipFile(INPUT_ZIP) as zf:
            for name in zf.namelist():
                if name.endswith("INFO_PlannedProjects_Metadata_Feb2026.txt"):
                    return zf.read(name).decode("utf-8", errors="replace").strip()
    return ""


def extract() -> None:
    if not INPUT_XLSX.exists():
        raise FileNotFoundError(f"Missing input workbook: {INPUT_XLSX}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    projects = pd.read_excel(INPUT_XLSX, sheet_name="Planned Transmission Projects")
    study = pd.read_excel(INPUT_XLSX, sheet_name="Study Concepts")
    substations = pd.read_excel(INPUT_XLSX, sheet_name="Substations in Planned Projects")
    field_defs_raw = pd.read_excel(INPUT_XLSX, sheet_name="Field definitions", header=None)

    projects["Status normalized"] = normalize_status(projects["Status"])
    projects["Length (mi)"] = to_numeric(projects["Length (mi)"]).fillna(0.0)
    projects["Maximum voltage (kV)"] = to_numeric(projects["Maximum voltage (kV)"])
    projects["Minimum voltage (kV)"] = to_numeric(projects["Minimum voltage (kV)"])
    projects["AC or DC"] = (
        projects["AC or DC"]
        .fillna("")
        .astype(str)
        .str.strip()
        .replace({"": "Unspecified"})
    )
    projects["voltage_class_max_kv"] = projects["Maximum voltage (kV)"].apply(voltage_class)

    study["Length (mi)"] = to_numeric(study["Length (mi)"]).fillna(0.0)
    study["Status normalized"] = normalize_status(study["Status"])

    # Unified proposed set: exclude complete/terminated.
    proposed = projects[~projects["Status normalized"].isin(["Complete", "Terminated"])].copy()
    proposed_hv = proposed[proposed["Maximum voltage (kV)"] >= 230].copy()

    # Export base tabular extracts.
    projects.to_csv(OUTPUT_DIR / "planned_transmission_projects.csv", index=False)
    study.to_csv(OUTPUT_DIR / "study_concepts.csv", index=False)
    substations.to_csv(OUTPUT_DIR / "substations_in_planned_projects.csv", index=False)
    field_defs_raw.to_csv(OUTPUT_DIR / "field_definitions_raw.csv", index=False, header=False)

    # Parse field definitions into a structured table.
    parsed_defs = field_defs_raw.copy()
    parsed_defs.columns = ["shapefile_field", "spreadsheet_field", "description"]
    parsed_defs = parsed_defs.dropna(how="all")
    parsed_defs = parsed_defs.dropna(subset=["shapefile_field", "spreadsheet_field", "description"], how="any")
    parsed_defs = parsed_defs[
        ~parsed_defs["shapefile_field"].astype(str).str.contains(
            "Field Definitions|Planned Transmission Projects and Study Concepts|Substations in Planned Projects|Field Name in Shapefile",
            regex=True,
        )
    ]
    parsed_defs.to_csv(OUTPUT_DIR / "field_definitions_parsed.csv", index=False)

    # Summaries.
    status_summary = (
        projects.groupby("Status normalized", as_index=False)
        .agg(segments=("Record ID", "count"), miles=("Length (mi)", "sum"))
        .sort_values("miles", ascending=False)
    )
    status_summary["miles"] = status_summary["miles"].round(2)
    status_summary.to_csv(OUTPUT_DIR / "summary_status_all_projects.csv", index=False)

    status_summary_proposed = (
        proposed.groupby("Status normalized", as_index=False)
        .agg(segments=("Record ID", "count"), miles=("Length (mi)", "sum"))
        .sort_values("miles", ascending=False)
    )
    status_summary_proposed["miles"] = status_summary_proposed["miles"].round(2)
    status_summary_proposed.to_csv(OUTPUT_DIR / "summary_status_proposed.csv", index=False)

    voltage_summary_proposed_hv = (
        proposed_hv.groupby("voltage_class_max_kv", as_index=False)
        .agg(segments=("Record ID", "count"), miles=("Length (mi)", "sum"))
        .sort_values("miles", ascending=False)
    )
    voltage_summary_proposed_hv["miles"] = voltage_summary_proposed_hv["miles"].round(2)
    voltage_summary_proposed_hv.to_csv(OUTPUT_DIR / "summary_voltage_class_proposed_230kv_plus.csv", index=False)

    acdc_summary_proposed_hv = (
        proposed_hv.groupby("AC or DC", as_index=False)
        .agg(segments=("Record ID", "count"), miles=("Length (mi)", "sum"))
        .sort_values("miles", ascending=False)
    )
    acdc_summary_proposed_hv["miles"] = acdc_summary_proposed_hv["miles"].round(2)
    acdc_summary_proposed_hv.to_csv(OUTPUT_DIR / "summary_acdc_proposed_230kv_plus.csv", index=False)

    rto_split = (
        proposed_hv.assign(
            rto_split=proposed_hv["RTO intersected"]
            .fillna("None / Unspecified")
            .astype(str)
            .str.split(",")
        )
        .explode("rto_split")
    )
    rto_split["rto_split"] = rto_split["rto_split"].str.strip().replace({"": "None / Unspecified"})
    rto_summary = (
        rto_split.groupby("rto_split", as_index=False)
        .agg(segments=("Record ID", "count"), miles=("Length (mi)", "sum"))
        .sort_values("miles", ascending=False)
    )
    rto_summary["miles"] = rto_summary["miles"].round(2)
    rto_summary.to_csv(OUTPUT_DIR / "summary_rto_proposed_230kv_plus.csv", index=False)

    metadata_text = read_metadata_text()
    metadata_out = OUTPUT_DIR / "metadata_info_text.txt"
    metadata_out.write_text(metadata_text + "\n", encoding="utf-8")

    summary_md = OUTPUT_DIR / "ourgridfuture_extract_summary.md"
    summary_md.write_text(
        "\n".join(
            [
                "# Our Grid Future Extract Summary",
                "",
                f"Retrieved: {date.today().isoformat()}",
                "",
                "## Source Files",
                f"- `{INPUT_XLSX.name}`",
                f"- `{INPUT_ZIP.name}`",
                "",
                "## Download Links",
                "- https://mail.ourgridfuture.org/download/OurGridFuture_PlannedTransmissionProjects_Feb2026.xlsx",
                "- https://mail.ourgridfuture.org/download/OurGridFuture_PlannedTransmissionProjects_Feb2026.zip",
                "",
                "## Key Counts",
                f"- Planned Transmission Projects segments: {len(projects):,}",
                f"- Study Concepts segments: {len(study):,}",
                f"- Substations in Planned Projects: {len(substations):,}",
                "",
                "## Mileage Totals",
                f"- Planned Transmission Projects (all statuses): {projects['Length (mi)'].sum():,.1f} mi",
                f"- Proposed unified set (excluding Complete + Terminated): {proposed['Length (mi)'].sum():,.1f} mi",
                f"- Proposed unified set, 230kV+ only: {proposed_hv['Length (mi)'].sum():,.1f} mi",
                f"- Study Concepts total: {study['Length (mi)'].sum():,.1f} mi",
                "",
                "## Notes",
                "- `summary_status_proposed.csv` is the unified proposed projection by status.",
                "- `summary_voltage_class_proposed_230kv_plus.csv` is the unified proposed projection by voltage class.",
                "- `summary_acdc_proposed_230kv_plus.csv` and `summary_rto_proposed_230kv_plus.csv` provide additional cuts.",
                "- `field_definitions_parsed.csv` and `metadata_info_text.txt` are text extracts from the distributed data package.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Wrote extracts to: {OUTPUT_DIR}")
    print(f"Projects rows: {len(projects)}")
    print(f"Proposed unified (excl. complete/terminated) miles: {proposed['Length (mi)'].sum():.1f}")
    print(f"Proposed unified 230kV+ miles: {proposed_hv['Length (mi)'].sum():.1f}")
    print(f"Study concepts miles: {study['Length (mi)'].sum():.1f}")


if __name__ == "__main__":
    extract()

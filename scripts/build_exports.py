#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RANKED_PATH = ROOT / "data/ranked/ranked.csv"
SPECS_PATH = ROOT / "data/specs/headphones_specs.csv"
OUT_PATH = ROOT / "data/exports/headphones_full.json"

REQUIRED_RANKED_COLUMNS = {"headphone", "avg_rank", "sources"}
REQUIRED_SPECS_COLUMNS = {
    "rank_key",
    "headphone",
    "brand",
    "model",
    "variant",
    "type",
    "driver_type",
    "driver_size_mm",
    "driver_width_mm",
    "driver_height_mm",
    "impedance_ohms",
    "sensitivity_db_mw",
    "frequency_response_hz",
    "weight_g",
    "cable_detachable",
    "connector",
    "origin",
    "msrp_usd",
    "release_year",
    "notes",
    "source_url",
}

NUMERIC_FIELDS = {
    "driver_size_mm",
    "driver_width_mm",
    "driver_height_mm",
    "impedance_ohms",
    "sensitivity_db_mw",
    "weight_g",
    "msrp_usd",
    "release_year",
}


def _read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def _require_columns(actual, required, label):
    missing = sorted(required - set(actual))
    if missing:
        raise ValueError(f"{label} missing columns: {', '.join(missing)}")


def _parse_number(value):
    if value is None:
        return None
    cleaned = value.strip()
    if not cleaned:
        return None
    try:
        if "." in cleaned:
            return float(cleaned)
        return int(cleaned)
    except ValueError:
        return None


def build_exports():
    ranked_columns, ranked_rows = _read_csv(RANKED_PATH)
    specs_columns, specs_rows = _read_csv(SPECS_PATH)

    _require_columns(ranked_columns, REQUIRED_RANKED_COLUMNS, "ranked.csv")
    _require_columns(specs_columns, REQUIRED_SPECS_COLUMNS, "headphones_specs.csv")

    specs_by_key = {}
    for row in specs_rows:
        key = (row.get("rank_key") or row.get("headphone") or "").strip()
        if key:
            specs_by_key[key] = row
    ranked_by_headphone = {
        row["headphone"].strip(): row for row in ranked_rows if row.get("headphone")
    }

    all_headphones = sorted(
        set(specs_by_key) | set(ranked_by_headphone), key=lambda name: name.lower()
    )

    records = []
    for headphone in all_headphones:
        ranked = ranked_by_headphone.get(headphone, {})
        specs = specs_by_key.get(headphone, {})

        record = {
            "headphone": specs.get("headphone", "").strip() if specs else headphone,
            "avg_rank": _parse_number(ranked.get("avg_rank", "")),
            "sources": _parse_number(ranked.get("sources", "")),
        }

        for field in REQUIRED_SPECS_COLUMNS:
            if field in {"rank_key", "headphone"}:
                continue
            value = specs.get(field, "").strip() if specs else ""
            if field in NUMERIC_FIELDS:
                record[field] = _parse_number(value)
            else:
                record[field] = value or None

        records.append(record)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(records, indent=2, sort_keys=False), encoding="utf-8")


if __name__ == "__main__":
    build_exports()

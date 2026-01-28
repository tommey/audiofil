# Audiofil Tier Data

This repository contains headphone tier listings in CSV format, derived rankings, and an expanded specs table used for a filterable data table site.

## Structure
- `data/raw/`: original tier listings with text tiers (e.g., `dms.csv`, `resolve.csv`).
- `data/ranked/`: ranked outputs, including `ranked.csv` aggregate and per-source `*_ranked.csv`.
- `data/specs/`: canonical specs table (`headphones_specs.csv`) keyed by `headphone`.
- `data/exports/`: generated outputs for the site (e.g., `headphones_full.json`).
- `scripts/`: data build scripts (e.g., `scripts/build_exports.py`).

## Tier mapping
- S+ = 0
- S = 1
- A = 2
- B = 3
- C = 4
- D = 5
- F = 6
- How did this happen? = 7
- X(Not Heard) / X (Not Heard) = 8

## Aggregate methodology
- `data/ranked/ranked.csv` averages available sources per headphone (sum of ranks / number of sources present).
- `sources` column indicates how many lists contributed to the average.

## Columns
Source CSVs (`data/raw/*.csv`) contain two columns:
- `tier`
- `headphone`

Ranked CSVs (`data/ranked/*.csv`) contain:
- `tier`
- `headphone`

Aggregate CSV (`data/ranked/ranked.csv`) contains:
- `headphone`
- `avg_rank`
- `sources`

Specs CSV (`data/specs/headphones_specs.csv`) contains:
- `rank_key` (matches `data/ranked/ranked.csv` headphone values)
- `headphone`
- `brand`
- `model`
- `variant`
- `type`
- `driver_type`
- `driver_size_mm`
- `impedance_ohms`
- `sensitivity_db_mw`
- `frequency_response_hz`
- `weight_g`
- `cable_detachable`
- `connector`
- `origin`
- `msrp_usd`
- `release_year`
- `notes`
- `source_url`

## Spec data workflow
- `data/specs/raw/` stores the raw manufacturer output for each entry as a JSON file named after the tier list key. Keep `product_name`, `page_title`, `source_url`, and the spec list inside that file so a later pass can rehydrate new columns without revisiting every page.
- `data/specs/headphones_specs.csv` is the canonical table that gets merged with `data/ranked/ranked.csv`. The `headphone` column here must contain the full vendor + model name, but you can keep `brand`, `model`, and `variant` separate for future flexibility.
- After you add or refresh the raw JSON and update the CSV, rerun `python3 scripts/build_exports.py` to regenerate `data/exports/headphones_full.json`.

## Data exports
Run `python3 scripts/build_exports.py` to generate `data/exports/headphones_full.json` by merging ranked data with specs (matched on `rank_key`).

## Site
The Astro site lives in `site/` and reads `data/exports/headphones_full.json`.
- Install: `cd site && npm install`
- Dev server: `npm run dev`
- Build: `npm run build`

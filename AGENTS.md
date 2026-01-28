# Repository Guidelines

## Project Structure & Module Organization
- `data/raw/` holds the source tier lists (e.g., `dms.csv`, `resolve.csv`).
- `data/ranked/` holds ranked outputs, including `ranked.csv`.
- `data/specs/` holds the specs table (`headphones_specs.csv`).
- `data/exports/` holds generated outputs for the site (`headphones_full.json`, HTML exports).
- `site/` contains the Astro static site.
- `README.md` documents the tier mapping, aggregation rules, and column definitions.

## Build, Test, and Development Commands
- Build data export: `python3 scripts/build_exports.py`
- Astro dev server: `cd site && npm run dev`
- Astro production build: `cd site && npm run build`

## Coding Style & Naming Conventions
- Indentation: use standard CSV formatting with comma-separated columns and a single header row.
- Naming: source files are lowercase provider names (`data/raw/dms.csv`), derived ranked files add `_ranked` (`data/ranked/dms_ranked.csv`).
- Keep columns consistent: source files must contain `tier,headphone`; aggregate file must contain `headphone,avg_rank,sources`.
- Specs file uses `rank_key` to match ranked data and `headphone` as the full vendor + model name.

## Testing Guidelines
- No automated tests are configured. Manually verify:
  - CSVs have exactly two columns (three for `ranked.csv`).
  - Tiers conform to the mapping in `README.md`.
  - Aggregates match the methodology described in `README.md`.
  - `data/exports/headphones_full.json` regenerates without errors.

## Commit & Pull Request Guidelines
- Git history is not available in this repository directory, so no commit message convention is defined.
- For pull requests, include:
  - A short summary of data changes.
  - The source of updated tiers or rankings.
  - A quick validation note (e.g., `head -n 5 ranked.csv`).

## Data Updates & Outputs
- When adding or updating CSV/HTML outputs, refresh `README.md` so the file list and methodology remain accurate.
- Keep HTML outputs aligned with their CSV sources and naming patterns.
- Use manufacturer product pages as the source for specs, and store the URL in `source_url`.
- Store the raw manufacturer exports in `data/specs/raw/<rank_key>.json` (include `product_name`, `page_title`, `source_url`, and `specs`) so the canonical CSV can be rebuilt later without re-scraping.

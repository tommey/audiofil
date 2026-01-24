# Repository Guidelines

## Project Structure & Module Organization
- `*.csv` holds the source tier lists and derived rankings (e.g., `dms.csv`, `resolve_ranked.csv`, `ranked.csv`).
- `*.html` provides human-readable views of the CSV data (e.g., `dms.html`, `resolve.html`).
- `README.md` documents the tier mapping, aggregation rules, and column definitions.

## Build, Test, and Development Commands
This repository is data-only and does not ship a build or test toolchain.
- Validate file inventory: `ls`
- Spot-check content: `head -n 5 ranked.csv`
- Search for tiers: `rg "^S\+" *.csv`

## Coding Style & Naming Conventions
- Indentation: use standard CSV formatting with comma-separated columns and a single header row.
- Naming: source files are lowercase provider names (`dms.csv`), derived ranked files add `_ranked` (`dms_ranked.csv`).
- Keep columns consistent: source files must contain `tier,headphone`; aggregate file must contain `headphone,avg_rank,sources`.

## Testing Guidelines
- No automated tests are configured. Manually verify:
  - CSVs have exactly two columns (three for `ranked.csv`).
  - Tiers conform to the mapping in `README.md`.
  - Aggregates match the methodology described in `README.md`.

## Commit & Pull Request Guidelines
- Git history is not available in this repository directory, so no commit message convention is defined.
- For pull requests, include:
  - A short summary of data changes.
  - The source of updated tiers or rankings.
  - A quick validation note (e.g., `head -n 5 ranked.csv`).

## Data Updates & Outputs
- When adding or updating CSV/HTML outputs, refresh `README.md` so the file list and methodology remain accurate.
- Keep HTML outputs aligned with their CSV sources and naming patterns.

# Audiofil Tier CSVs

This folder contains headphone tier listings in CSV format, plus derived files where tiers are mapped to numeric ranks and aggregated across sources.

## Files
- `dms.csv`, `goldensound.csv`, `resolve.csv`: original tier listings with text tiers.
- `*_ranked.csv`: same data with the `tier` column mapped to numeric ranks.
- `ranked.csv`: aggregate average ranks across sources.

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
- `ranked.csv` averages available sources per headphone (sum of ranks / number of sources present).
- `sources` column indicates how many lists contributed to the average.

## Columns
Each CSV has two columns:
- `tier`
- `headphone`

`ranked.csv` has three columns:
- `headphone`
- `avg_rank`
- `sources`

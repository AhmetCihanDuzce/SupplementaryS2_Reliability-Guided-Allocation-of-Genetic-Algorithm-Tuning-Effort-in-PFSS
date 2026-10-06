# Ta100x20 Canonical Historical Transfer Artifact — 595/840

This directory restores the complete comparison-level evidence for the manuscript's canonical Ta100x20 historical transfer result.

## Canonical result
- Main response surface: 10 Taillard instances × 125 parameter configurations × R=10 = 12,500 GA runs.
- Generation budget: G=17,000.
- Calibration design: all C(10,3)=120 triples, with 7 holdouts per split = 840 holdout comparisons.
- Fresh validation: 79 distinct target/configuration conditions × R=10 = 790 independent GA runs.
- Near-optimal criterion: signed excess <= 0.25 percentage points.
- Canonical outcome: 595/840 = 70.833333% near-optimal comparisons.

## Canonical NEH normalization
The canonical normalization vector is:
`6541, 6523, 6639, 6557, 6695, 6664, 6632, 6739, 6677, 6677`.
These values are stored in `Ta100x20_NEH_reference.csv` and independently reproduce the standard NEH makespan on the supplied ten Ta100x20 matrices.

## Selection rule
For each calibration triple, each configuration's regret is computed relative to the target-specific empirical oracle from the main surface and normalized by the target NEH value. Configurations with calibration mean regret within +0.25 pp of the split-best mean are admissible. The selected configuration minimizes the worst calibration-instance regret, with lower mean regret and then the prespecified parameter ordering used as tie-breaks.

## Files
- `main/`: 10 complete 1,250-row main-response-surface files.
- `matrices/`: the ten Ta100x20 processing-time matrices.
- `Ta100x20_120split_policies_prespecified.csv`: the 120 canonical split selections.
- `Ta100x20_fresh_validation_complete_790.csv`: all 790 independent fresh-validation GA runs.
- `Ta100x20_3to7_holdout_observations_840.csv`: all 840 comparison-level outcomes.
- target/split/overall summaries, validation plan, run plan, and QA tables.

## Relationship to the 597/840 audit artifact
A later archived workbook produced 597/840 under a different NEH-normalization vector. The underlying 12,500 main GA runs are the same, and 780 of the 790 canonical fresh runs are shared exactly. The alternate normalization changes three of 120 split policy selections and results in a two-count difference in the aggregate near-optimal total. That alternate workbook is retained only as an internal sensitivity/audit artifact and is not used as evidence for the manuscript.

The script `03_Quality_Assurance_and_Integrity/scripts/verify_all.py` independently rebuilds the 120 split policies and the 840 fresh comparisons from the files in this directory and must return 595/840.

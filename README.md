# Supplementary S2 — Data, Results, and Quality Assurance

This archive contains the experimental data, target-level results, robustness analyses, and quality-assurance material supporting the manuscript. It deliberately separates the **original conservative prospective validation implementation** from the manuscript's **final recommended risk-guided staged operational policy**.

## 01_Historical_GA_Results
Historical GA response surfaces, fresh-validation evidence, matrices, and the nine-anchor summary. The `Ta100x20_Canonical_595/` subdirectory contains the complete canonical G=17,000 reconstruction supporting 595/840 = 70.833333%.

## 02_Prospective_24_Target_Results
The prespecified 24-target design, exact prospective matrices, and original confirmatory prospective results. The original conservative implementation used GREEN direct-center reuse, AMBER local tuning with at most 116 runs, and RED 125x10 full retuning; it used 6,185 tuning runs across 24 targets. Matrix replay is exact: 24/24 SHA-256 matches and 24/24 standard-NEH matches. These original results are retained unchanged and are not retrospectively recomputed under the final operational policy.

## 03_Quality_Assurance_and_Integrity
Standalone verification scripts and audit records. The verification chain reconstructs manuscript-critical historical and prospective totals, the canonical Ta100x20 595/840 result, exact prospective matrices, and the final staged-policy matched-budget validation.

## 04_Protocol_and_Data_Dictionaries
The original prespecified prospective protocol, an explicit preservation note separating it from the final recommendation, the final recommended staged-policy specification, the matched-budget validation protocol, and data dictionaries.

## 05_Recommended_Operational_Policy_Validation
The manuscript's final practitioner recommendation and its 24-target matched-budget validation. The recommended policy uses risk-dependent search breadth and staged replication: GREEN <=50 runs, AMBER <=137 runs, and RED 490 runs. The realized total is 3,767 tuning runs, versus 30,000 for universal 125x10 retuning, 6,185 for the original conservative prospective schedule, and 3,768 for the reliability-blind matched-budget comparator. The directory includes 960 fresh common-random-number validation observations.

## 06_Robustness_and_Sensitivity_Analyses
Historical leave-one-instance-out robustness, interpolation and threshold sensitivity, GREEN random baselines, intervention-only continuous-loss/recovery analyses for the original prospective implementation, computational-work proxies, and inference diagnostics reported in the manuscript.

See `SHA256_MANIFEST.txt` for file-level hashes and `PACKAGE_INVENTORY.csv` for the package inventory.

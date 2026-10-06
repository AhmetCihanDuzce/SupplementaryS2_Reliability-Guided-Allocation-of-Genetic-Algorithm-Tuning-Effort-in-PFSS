# Data Dictionary — Historical GA Archive

## Historical anchor summary

`01_Historical_GA_Results/Current_Manuscript_Historical_Anchor_Summary.csv` contains the nine Taillard size anchors used by the transfer-risk framework. `pop_mult`, `pc`, and `pm` are the transferred parameter centers; `safe_count/comparisons` define historical transfer reliability under the 0.25-pp practical-loss criterion; `G` is the prespecified generation budget.

## Historical experiment blocks

- `20Job/` contains the Ta20x5, Ta20x10, and Ta20x20 historical experiment workbook.
- `50Job/` contains the complete 37,500-run 50-job main archive and retained matrices; `50Job_Independent_Fresh_Revalidation/` contains the independent fresh-revalidation layer.
- `100Job/GaStructure_100Job_All_Results_With_Seeds.xlsx` contains the Ta100x5 and Ta100x10 records.
- `100Job/Ta100x20_Canonical_595/` contains the canonical G=17,000 Ta100x20 reconstruction: ten 1,250-run response surfaces, 120 prespecified split-policy selections, 790 fresh-validation runs, and 840 holdout comparisons. The resulting historical reliability is 595/840 = 70.833333%.

## Canonical Ta100x20 normalization

The standard-NEH vector is `6541, 6523, 6639, 6557, 6695, 6664, 6632, 6739, 6677, 6677`. The standalone verifier recomputes these values from the supplied matrices before reconstructing the 120 policy selections and all 840 comparison outcomes.

A previously examined 597/840 workbook used an alternate NEH-normalization vector. It is not used or distributed as submission evidence; the canonical 595/840 line is the one supplied and independently replayed here.

## Prospective protocol

`04_Protocol_and_Data_Dictionaries/Prospective_Protocol_Prespecified_v1.1_2026-08-27.json` is the authoritative pre-outcome protocol for the 24-target prospective experiment.

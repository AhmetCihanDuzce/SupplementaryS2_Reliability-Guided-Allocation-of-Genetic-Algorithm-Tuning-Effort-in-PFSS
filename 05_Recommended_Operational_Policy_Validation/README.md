# Recommended Risk-Guided Staged Operational Policy — 24-Target Validation

This directory contains the machine-readable evidence for the manuscript's **final recommended operational policy**. Historical transfer reliability determines risk ordering and search breadth, while the lower-replication screening-and-confirmation schedule provides the computational refinement evaluated on the exact 24-target panel.

Recommended action budgets:
- **GREEN:** transferred center plus available +/-1 axial neighbors; Stage-1 R=5; raw top 3 confirmed to R=10; maximum 50 tuning runs.
- **AMBER:** +/-1 Cartesian neighborhood; Stage-1 R=3; raw top 8 confirmed to R=10; maximum 137 tuning runs.
- **RED:** full 125-configuration grid; Stage-1 R=2; raw top 30 confirmed to R=10; 490 tuning runs.

The realized guided budget across the 24 targets is **3,767 tuning runs**. This is 87.44% fewer configuration runs than universal 125x10 retuning (30,000 runs) and 39.09% fewer than the original conservative prospective validation schedule (6,185 runs). These are run-count comparisons, not wall-clock savings.

For matched-budget validation, the reliability-blind comparator uses 3,768 tuning runs. The transferred center is not forced into the finalist set and is not used as an acceptance gate. Each method selects its own configuration, after which the two selected configurations are evaluated on the same 20 fresh common-random-number seeds per target.

Files:
- `Recommended_Operational_Policy_Summary.csv`: final GREEN/AMBER/RED action specification.
- `Recommended_Operational_Policy_Budget_By_Target.csv`: target-level realized staged-policy budgets.
- `Recommended_Operational_Policy_Budget_Summary.csv`: budget totals by risk group.
- `Recommended_Operational_Policy_Selected_Configurations.csv`: selected guided and blind configurations and confirmation means.
- `Recommended_Operational_Policy_Final_Validation_Raw.csv`: 960 fresh validation observations (24 targets x 2 methods x 20 reps).
- `Recommended_Operational_Policy_Validation.csv`: target-level fresh-validation means, paired win/loss/tie counts, and practical classification.
- `Recommended_Operational_Policy_Aggregate.csv`: overall and GREEN/AMBER/RED summaries.
- `validation_by_target/`: the same raw validation observations split by target.
- `QA_RECOMMENDED_OPERATIONAL_POLICY_VALIDATION.txt`: reconstruction check.

A +/-0.05% practical-equivalence band is used only to interpret effect magnitude; it is not a search, selection, or acceptance criterion. The exact specification is supplied in `04_Protocol_and_Data_Dictionaries/RECOMMENDED_OPERATIONAL_POLICY_AND_VALIDATION_PROTOCOL_v1.0.md` and in Supplementary S1.

The original 6,185-run conservative prospective implementation remains preserved separately in `02_Prospective_24_Target_Results/` and is the basis of the original confirmatory 21/24 policy-versus-center analysis.

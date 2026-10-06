# Original 24-Target Prospective Validation Results

This directory preserves the **original confirmatory prospective experiment** exactly as evaluated. Its implementation was fixed before target outcomes were observed and used:

- GREEN: transferred center reuse with 0 target-specific tuning runs;
- AMBER: local neighborhood screening with at most 116 tuning runs;
- RED: full 125-configuration x 10-replication retuning, 1,250 runs.

Across 24 targets this conservative schedule used 6,185 tuning runs and produced the original 21/24 policy-versus-center within-tolerance result at 0.25 pp.

The manuscript's **final recommended operational policy is not this conservative replication schedule**. It uses staged screening and confirmation with maximum per-target budgets of 50 (GREEN), 137 (AMBER), and 490 (RED), and is documented separately in `../05_Recommended_Operational_Policy_Validation/`. Keeping the two implementations separate prevents retrospective alteration of the original confirmatory endpoint.

# Final Submission Scope and Audit

This package combines historical calibration/transfer records, the original prespecified 24-target prospective validation, additional robustness analyses, and the 24-target validation of the manuscript's final recommended staged operational policy.

Verified manuscript-critical results include:
- historical transfer reliability: 6583/7560 = 87.08%;
- original prospective action counts: 8 GREEN, 12 AMBER, 4 RED;
- original conservative prospective policy and direct center within 0.25 pp: 21/24 and 21/24;
- original conservative prospective tuning effort: 6,185 runs versus 30,000 under universal full-grid retuning;
- canonical Ta100x20 historical reliability: 595/840 = 70.833333%;
- exact prospective matrix recovery: 24/24 SHA-256 identities and 24/24 standard-NEH values;
- **recommended staged operational policy:** GREEN <=50, AMBER <=137, RED = 490 runs per target; realized 24-target budget = 3,767 runs;
- run-count reduction for the recommended policy: 87.44% versus universal 30,000-run retuning and 39.09% versus the original 6,185-run conservative schedule;
- reliability-blind matched-budget comparator: 3,768 runs;
- final staged-policy validation: 960 fresh common-random-number observations;
- raw mean result: guided lower on 16/24 targets, blind lower on 5/24, exact ties on 3/24;
- +/-0.05% interpretive classes: 9 guided, 14 practical ties, 1 blind.

The original prospective implementation and the final operational recommendation are intentionally kept separate. The former is the basis of the prespecified confirmatory analysis; the latter is the lower-cost operational refinement supported by subsequent matched-budget validation on the exactly recovered 24-target panel.

A previously examined 597/840 Ta100x20 workbook used an alternate NEH-normalization vector and is not used or distributed as submission evidence.

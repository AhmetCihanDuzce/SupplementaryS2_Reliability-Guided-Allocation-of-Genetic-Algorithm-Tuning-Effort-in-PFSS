# Final 50-Job Archive Notes

The 50-job experiment was closed only after all three groups (Ta50×5, Ta50×10, Ta50×20) reached 12,500 main rows each. The final combined file therefore contains 37,500 rows and 3,750 parameter configurations, with exactly ten replications per configuration.

The main seed bases are 2250000201, 2260000201, and 2270000201 for m=5,10,20, respectively, using

```text
seed = base + instance × 100000 + rep × 1009.
```

The fresh-validation seed bases are 2350000201, 2360000201, and 2370000201. Transfer configurations were re-selected from the completed response surfaces before final fresh validation. The files in `Transfer_Validation/50Job/` are the only 50-job transfer files distributed as final supplementary evidence.

A subset of historical source rows did not preserve runtime. Missing `run_sec` values are left blank and must not be imputed. The manuscript does not base its scientific conclusions on whole-panel runtime comparisons.

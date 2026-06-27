---
document_type: synthesis_status
batch_item: seventh_20_task_7
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T186-T187 Metric-Causal Beta Proxy Status

## Status

This note records the corrected metric-causal beta status. It does not revive
the old exact Moses claim.

## Sources read

- `tests/T186-metric-vs-causal-order-beta-test.md`
- `results/T186-metric-vs-causal-order-beta-v0.1-results.md`
- `tests/T187-moses-exact-constrained-optimization.md`
- `results/T187-moses-exact-constrained-optimization-v0.1-results.md`

## Plain-English finding

The metric-vs-causal split is still useful, but only as finite proxy evidence.
The exact optimization derivation was narrowed after review.

## Technical conclusion

T186 supplies a positive fixture: Alpha and Beta have the same causal order,
same causal-set quantities, same event count, and same entropy production, but
different delivery-time distributions and different beta estimates.

T187 confirms the same sign under a harmonic proxy:

```text
beta_HM(Beta) > beta_HM(Alpha)
```

But T187 no longer removes the exact-Moses blocker. The inverse-time weighting
does not follow from the stated linear program.

## Minimum next task

Keep T186/T187 as proxy-level sign evidence and cite T200/T201/T202 before any
export. A future exact route must state the actual physical objective whose
solution gives the timing statistic.

## Stop condition

Stop any claim that the harmonic proxy is exact Moses optimization, WBE
continuum support, or a theorem from the original LP/KKT setup.


---
document_type: synthesis_status
batch_item: seventh_20_task_11
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T193-T194 Cap_TI Minimal Statistic Hostile-Family Status

## Status

This note records the corrected status of the Cap_TI minimal-statistic and
hostile-family results.

## Sources read

- `tests/T193-cap-ti-minimal-sufficient-statistic-search.md`
- `results/T193-cap-ti-minimal-sufficient-statistic-search-v0.1-results.md`
- `tests/T194-cap-ti-hostile-same-neighbor-data-adversarial-family.md`
- `results/T194-cap-ti-hostile-same-neighbor-data-adversarial-family-v0.1-results.md`
- `tests/T207-cap-ti-minimal-statistic-after-corrections.md`

## Plain-English finding

The old minimal statistic works only inside the declared harmonic-proxy regime.
It is not an exact universal Cap_TI statistic.

## Technical conclusion

T193 shows that under the harmonic proxy:

```text
R(beta,n) = T_H
```

so `(n,T_H)` is sufficient. T194 then tests hostile families that keep
`T_H` fixed while changing richer metric or topology details; inside that
proxy regime, the capability collapses as expected.

After the T200-T207 correction chain, this becomes regime-dependent:

- harmonic proxy: `(n,T_H)` sufficient by definition;
- pure/lower-bound LP: different objective statistic;
- shared-edge DAG: requires incidence/capacity/flow state.

## Minimum next task

Attach a `regime` field to every Cap_TI statistic: harmonic proxy, LP family,
equal-load/fairness, or capacity-aware DAG flow.

## Stop condition

Stop if a same-`T_H` collapse is exported as exact Moses, corrected LP, or
shared-edge flow minimality.


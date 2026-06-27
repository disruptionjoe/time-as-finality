---
document_type: synthesis_status
batch_item: seventh_20_task_12
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T200-T202 Harmonic-Proxy Correction Ladder

## Status

This note summarizes the correction ladder that narrows the harmonic proxy.

## Sources read

- `tests/T200-t187-linear-program-kkt-audit.md`
- `results/T200-t187-linear-program-kkt-audit-v0.1-results.md`
- `tests/T201-regularized-fairness-objective-harmonic-weight-audit.md`
- `results/T201-regularized-fairness-objective-harmonic-weight-audit-v0.1-results.md`
- `tests/T202-shared-edge-dag-path-harmonic-counterexample.md`
- `results/T202-shared-edge-dag-path-harmonic-counterexample-v0.1-results.md`

## Plain-English finding

The harmonic mean is not wrong as a statistic. The mistake was treating it as
the result of the original linear program and then carrying it into shared-edge
DAGs as if paths were independent.

## Technical conclusion

T200 kills the LP/KKT derivation: a linear objective over a simplex with lower
bounds optimizes at an extreme point, not at reciprocal weights.

T201 finds a legitimate home for reciprocal weights: an equal-load or minimax
fairness objective, if that objective is independently justified.

T202 shows path-harmonic summaries are proxy-only on shared-edge DAGs because
they double-count bottleneck edges and ignore capacity/conservation state.

## Minimum next task

Require each future timing summary to state its objective and domain: LP,
fairness/equal-load, independent-path proxy, or capacity-aware flow.

## Stop condition

Stop any artifact that says inverse-time weights follow from the old LP, or
that unweighted path harmonic is a faithful shared-edge DAG flow model.


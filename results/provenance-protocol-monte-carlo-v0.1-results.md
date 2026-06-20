# T74 Results: Provenance Protocol Monte Carlo

Monte Carlo audit over 400 samples per prior family with deterministic seed 74017.

Strongest claim: Robust detector-provenance recovery is not a generic consequence of having calibrated detector channels. In this audit it occupies a high-trust, low-back-action, high-authentication corner of protocol space and drops sharply under broader stress priors.

Weakened claim: Under the mixed and degraded priors, robust recovery disappeared entirely; the protocol mostly withheld D1 rather than recovering a partition. Q1's detector branch should therefore be treated as an engineered protocol claim, not a generic measurement claim.

## Family table

| Prior family | Robust | Withhold | Threshold-dependent | False independence | False dependence | D1 computable |
| --- | --- | --- | --- | --- | --- | --- |
| engineered_lab | 0.905 | 0.095 | 0.0 | 0.0 | 0.0 | 0.905 |
| mixed_lab | 0.0 | 0.91 | 0.09 | 0.0 | 0.0 | 0.0 |
| field_degraded | 0.0 | 0.71 | 0.29 | 0.0 | 0.0 | 0.0 |

## Blocker

The priors are stress priors, not calibration posteriors. Without detector-specific calibration data, T74 quantifies fragility but not real experimental frequency.

## Next move

Map one concrete detector stack onto T72/T74 parameters and replace the stress priors with measured posteriors for clocks, authentication, batching, trust, back-action, and DAG observability.

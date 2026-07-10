# T524: T126 Random-Sprinkle Diagnostic Repair

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T223: T54 Ordinal Scaling Decisive Verdict](T223-t54-ordinal-scaling-decisive-verdict.md)

## Central Question

Does T126's `order_dimension_obstruction` behave like a genuine
manifoldlikeness falsifier on random 1+1 light-cone sprinkles, or does it reject
genuine finite sprinkles as their natural interval-profile fluctuation appears?

## Setup

T524 builds seeded random 1+1 light-cone coordinate controls at
`N = 8, 12, 16, 20`, using seeds `0..7`. A point `p` is below `q` exactly when
`u_p < u_q` and `v_p < v_q`.

Each sample is audited by the existing T126 machinery and compared against the
T156 flat 1+1 ordering-fraction target.

## Success Criteria

- The repo's six-event flat T156 calibration control still passes T126.
- The mean ordering-fraction gap from `1/2` decreases with size.
- The T126 `order_dimension_obstruction` rejection rate increases with size.
- All `N >= 16` random controls are rejected by `order_dimension_obstruction`.
- The result is recorded as a diagnostic repair only, not as S1 promotion.

## Failure Criteria

T524 fails if:

- seeded random controls do not approach the declared 1+1 ordering-fraction
  target;
- larger random controls do not trigger the profile-spread leg;
- the calibration control no longer passes;
- the result is used to promote S1 or to invalidate T223's independent finite
  rare-tail counting.

## Implementation Result

Status: implemented.

The random controls confirm the earlier deterministic finding. T126's
`order_dimension_obstruction` rejects a growing fraction of genuine random 1+1
controls while their mean ordering-fraction gap from `1/2` improves. This
quarantines that leg as a finite interval-profile regularity screen, not a
continuum manifoldlikeness wall.

## Run Command

```bash
python -m unittest tests.test_t524_t126_random_sprinkle_diagnostic_repair -v
python -m models.run_t524
```

## Boundary

T524 does not prove spacetime, embedding, dimension, metric reconstruction,
random-sprinkling convergence, or a continuum limit. S1 remains
`requires_added_assumption`; T223 remains a finite-screen/finite-ensemble no-go
until a repaired manifoldlikeness suite and an added measure or continuum bridge
exist.

# T165: T54 Survivor Sprinkling Stress Test

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T159: T54 Interval-Jackknife Screen](T159-t54-interval-jackknife-screen.md)
- [T163: T54 Rank-Pair Family Census](T163-t54-rank-pair-family-census.md)
- [T164: T54 Survivor Isomorphism And Locality Audit](T164-t54-survivor-isomorphism-locality.md)

## Question

Are the 15 oriented T164 survivor classes typical small 1+1 interval
sprinkling outputs, or are they a rare tail selected by the current T126/T156/
T159 screens?

## Motivation

T164 removed label inflation from the T163 positive boundary, but it still left
an open comparison problem. A future S1 witness should not merely point at a
small set of finite posets; it should say whether those posets are natural
under a declared causal-set comparison target.

T165 uses the exact six-point ordinal 1+1 comparison. For six sampled points in
a flat 1+1 causal diamond with no light-cone coordinate ties, sorting by one
coordinate leaves the other coordinate's rank as a uniform permutation in
`S_6`. That is exactly the T163 rank-pair family, so no Monte Carlo is needed.

## Setup

Pipeline:

```text
all 720 T163 rank-pair cases
  -> interpret as exact six-point ordinal 1+1 permutation ensemble
  -> count T126 passers
  -> count T156 ordering-fraction passers
  -> count T159 parent-interval passers
  -> count T159 all-deletion-stable survivors
  -> compare T164 oriented class abundance under the same uniform ensemble
```

## Success Criteria

- The comparison ensemble is exact and finite: all `6! = 720` permutations.
- T165 reports unconditional and conditional pass fractions for the T126,
  T156, parent-interval, and deletion-stability gates.
- T165 reports how abundant the T164 oriented classes are under the uniform
  ordinal ensemble.
- S1 remains finite-control only unless a generative law or larger-scale
  bridge is supplied.

## Failure Criteria

T165 fails if:

- the rank-pair family is not the right exact ordinal model for six generic
  1+1 interval samples;
- T163 and T164 disagree about which cases are stable survivors;
- a rare finite tail is described as continuum evidence;
- the result is treated as a faithful embedding, metric reconstruction,
  covariance result, or random-sprinkling law.

## Claim Impact

S1 remains `open_formal_target`.

The current six-event survivor boundary is compatible with the exact ordinal
1+1 comparison, but only after strong conditioning:

```text
26 / 720 = 13 / 360
```

Each oriented T164 class has uniform-ensemble probability at most `1/360`.
That makes the survivors a rare finite tail that needs a generative explanation,
not spacetime evidence.

## Reproduction

```bash
python -m unittest tests.test_t54_survivor_sprinkling_stress -v
python -m models.run_t165
```

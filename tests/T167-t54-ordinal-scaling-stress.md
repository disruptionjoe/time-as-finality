# T167: T54 Ordinal Scaling Stress Test

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T159: T54 Interval-Jackknife Screen](T159-t54-interval-jackknife-screen.md)
- [T163: T54 Rank-Pair Family Census](T163-t54-rank-pair-family-census.md)
- [T164: T54 Survivor Isomorphism And Locality Audit](T164-t54-survivor-isomorphism-locality.md)
- [T165: T54 Survivor Sprinkling Stress Test](T165-t54-survivor-sprinkling-stress.md)

## Question

Does the rare T54 survivor tail found at six events immediately disappear,
become typical, or persist when the exact ordinal 1+1 comparison is extended
one step to seven events?

## Motivation

T165 showed that the six-event T54 survivor classes occupy only `26/720` cases
in the exact ordinal 1+1 rank-permutation ensemble. That was useful, but still
left a size-one concern: perhaps the positive finite boundary was an accident
of six events, or perhaps it would become broad at the next size.

T167 runs the same declared pipeline at `n=5`, `n=6`, and `n=7`. This is a
bounded scaling audit, not an asymptotic theorem.

## Setup

For `n` generic points in a flat 1+1 causal diamond with no light-cone
coordinate ties, sorting by one coordinate leaves the other coordinate's rank
as a uniform element of `S_n`. T167 therefore uses exact rank-permutation
ensembles:

```text
n = 5: 5! = 120 cases
n = 6: 6! = 720 cases
n = 7: 7! = 5040 cases
```

Each case is completed through the T54 quotient-union pipeline and then tested
with:

```text
T126 finite causal-set filter
T156 flat 1+1 ordering-fraction band
T159 parent-interval support
T159 all single-deletion stability
finite-poset isomorphism quotient for stable survivors
```

## Success Criteria

- `n=6` reproduces the T165 count `26/720`.
- `n=7` is fully enumerated, not Monte Carlo sampled.
- Stable survivor abundance and finite-poset isomorphism compression are
  reported.
- S1 remains finite-control only unless a generative law, embedding theorem,
  or continuum bridge is supplied.

## Failure Criteria

T167 fails if:

- the ordinal `S_n` ensemble is not the intended exact finite model for
  no-tie 1+1 interval samples;
- the `n=6` audit does not reproduce T165;
- the `n=7` audit changes any screen relative to T126/T156/T159;
- one-step scaling is treated as a continuum-limit, metric, covariance,
  faithful-embedding, or spacetime-reconstruction result.

## Claim Impact

S1 remains `open_formal_target`.

The T54 survivor tail persists one step, but remains rare:

```text
n=5: scale-blocked by T126
n=6: 26 / 720 = 13 / 360
n=7: 174 / 5040 = 29 / 840
```

The `n=7` stable labels reduce to `86` oriented finite-poset classes, or `45`
order-dual classes, and the largest oriented class has probability `1/1260`
under the uniform ordinal ensemble.

This weakens both easy stories. The six-event result was not merely an
immediate accident, but it also does not become typical at seven events. The
remaining S1 burden is now generative or structural: explain why this rare
tail should be selected, or stop treating it as spacetime-facing residue.

## Reproduction

```bash
python -m unittest tests.test_t54_ordinal_scaling_stress -v
python -m models.run_t167
```

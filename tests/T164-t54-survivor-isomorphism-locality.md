# T164: T54 Survivor Isomorphism And Locality Audit

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T159: T54 Interval-Jackknife Screen](T159-t54-interval-jackknife-screen.md)
- [T163: T54 Rank-Pair Family Census](T163-t54-rank-pair-family-census.md)

## Question

Do the 26 labeled T163 stable survivors represent many independent finite
structures, or do they collapse to a much smaller set of unlabeled causal-set
shapes?

## Motivation

T163 found 26 labeled six-event T54 rank-pair completions that clear T126,
T156, parent-interval support, and single-deletion stability. That is a real
finite boundary improvement over T159, but labeled counts can overstate
structure. If most survivors are relabelings or order-duals of a small set of
thin posets, S1 should stay at calibration/control level.

T164 therefore quotients the T163 survivors by finite-poset isomorphism and
adds a first structural locality guardrail.

## Setup

Pipeline:

```text
T163 stable survivors
  -> reconstruct each T54/T126 finite order
  -> compute canonical order-preserving poset key
  -> quotient by oriented isomorphism
  -> quotient again after order-dual identification
  -> report strict-pair, cover-degree, rank, interval, and hub diagnostics
```

The oriented quotient preserves causal direction. The order-dual quotient is
reported separately as a coarser shape check, not as the default physical
equivalence.

## Success Criteria

- Only T163 `t159_stable_survivor` cases enter the quotient.
- The quotient is invariant under relabeling of the six events.
- The result reports oriented isomorphism class count and order-dual class
  count.
- The result reports whether the survivor classes remain height-3 and
  parent-interval-thin.
- S1 is not upgraded beyond finite control language.

## Failure Criteria

T164 fails if:

- a non-surviving T163 case enters the quotient;
- the canonical key changes under event relabeling;
- order-dual identification is confused with ordinary causal-set isomorphism;
- the class count is interpreted as a random-sprinkling, embedding, metric,
  covariance, or continuum result.

## Claim Impact

S1 remains `open_formal_target`.

The useful outcome is a sharper finite boundary:

```text
26 labeled survivors -> 15 oriented finite-poset classes -> 9 order-dual classes
```

All surviving classes remain six-event height-3 controls with parent intervals
of size at most 1. That makes them a narrow target for future locality or
sprinkling stress tests, not evidence of spacetime reconstruction.

## Reproduction

```bash
python -m unittest tests.test_t54_survivor_isomorphism_locality -v
python -m models.run_t164
```

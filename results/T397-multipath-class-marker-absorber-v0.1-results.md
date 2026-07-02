# T397 Results: Multipath Class-Marker Absorber Audit

- **Artifact:** `T397-multipath-class-marker-absorber-v0.1`
- **Spec:** [tests/T397-multipath-class-marker-absorber.md](../tests/T397-multipath-class-marker-absorber.md)
- **Model:** [models/multipath_class_marker_absorber.py](../models/multipath_class_marker_absorber.py)
- **Test:** [tests/test_multipath_class_marker_absorber.py](../tests/test_multipath_class_marker_absorber.py)
- **Numbers:** [T397-multipath-class-marker-absorber-v0.1.json](T397-multipath-class-marker-absorber-v0.1.json)
- **Tags:** direction_a, absorber_audit, multipath_marker, t395_followup, no_claim_promotion

## Verdict

**absorbed: the T395 k>=3 class-coarse record signature is exactly generic multipath class-marker algebra in this finite audit.**

The generic three-path class marker and T395's canonical three-order class
record have identical structure-only signatures at every gamma in the declared
sweep. The k>=3 class-coarse record behavior depends only on the class
partition and the marker overlap `cos(gamma/2)`, not on whether the branch
labels are composition orders.

## Canonical Three-Order / Three-Path Sweep

| gamma | marker overlap | class D | path success | within factor | cross factor |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 1.000000 | 0.000000 | 0.333333 | 1.000000 | 1.000000 |
| pi/4 | 0.923880 | 0.382683 | 0.460894 | 1.000000 | 0.923880 |
| pi/2 | 0.707107 | 0.707107 | 0.569036 | 1.000000 | 0.707107 |
| 3pi/4 | 0.382683 | 0.923880 | 0.641293 | 1.000000 | 0.382683 |
| pi | 0.000000 | 1.000000 | 0.666667 | 1.000000 | 0.000000 |

At `gamma = pi`, the perfect class record gives individual path/order
postdiction `0.666667` = `2/3` while
same-class coherence remains unchanged and cross-class coherence is zero.

## Scalarization Check At Perfect Class Record

T395's tested global scalarizations fail the binary circle in the generic
absorber too:

| case | mean residual | min residual | max residual |
| --- | ---: | ---: | ---: |
| three-order / three-path | -0.638889 | -0.750000 | 0.250000 |
| six-path parity | -0.800000 | -0.960000 | 0.040000 |

This is no longer evidence of temporal-order-specific structure; it is a
generic consequence of asking a scalar pair to summarize a class partition with
within-class coherence left intact.

## Exhaustive Bipartition Sweep

All nontrivial two-class bipartitions are checked up to class-complement
symmetry for k = 3..6.

| k | bipartitions | within flat | cross duality | postdiction formula | scalarizations fail at pi |
| ---: | ---: | --- | --- | --- | --- |
| 3 | 3 | True | True | True | True |
| 4 | 7 | True | True | True | True |
| 5 | 15 | True | True | True | True |
| 6 | 31 | True | True | True | True |

## Direction-A Update

Do not promote T395's k>=3 partial-record residue as a temporal-order inequality ingredient by itself. Direction A should move to a genuine causal-process witness, multi-holder finality/reversal cost, or another structure not already present in generic multipath class markers.

## Strongest Safe Claim

For two-class records over k>=3 equally weighted branches, the T395 signatures depend only on the class partition and the marker overlap cos(gamma/2): same-class coherences are unchanged, cross-class coherences are multiplied by cos(gamma/2), individual path postdiction is (1+sin(gamma/2))/k, and the perfect class record ceiling is 2/k. Composition-order labels add no extra structure in this branch-marker model.

## Falsification Condition

This absorber would fail if a composition-order family with the same class partition and marker overlaps produced a capability, causal witness, or coherence invariant that is not reproduced by the generic path-marker signature.

## Next Gate

Replace visibility with a causal-process witness or add D1-native multi-holder/reversal-cost structure before attempting any record-order inequality.

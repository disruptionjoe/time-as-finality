# T397: Multipath Class-Marker Absorber Audit

## Route

Direction A / T395 follow-up / absorber audit.

T395 found that its two-order record-order trade-off collapses exactly to
ordinary which-path duality, while its k >= 3 class-coarse record probe leaves
a class-graded structure: cross-class binary duality, within-class coherence
left intact, and a perfect class record that caps individual order postdiction
at `2/k`. T395 named multipath duality as the absorber to run before any claim
promotion or temporal-order inequality work.

## Claim

For the declared two-class branch-marker family, the T395 k >= 3 partial-record
signature is exactly generic multipath class-marker algebra. Replacing
composition-order branch labels with generic path labels changes nothing in
the tested signatures:

- same-class coherences are multiplied by `1`;
- cross-class coherences are multiplied by `cos(gamma/2)`;
- class distinguishability is `sin(gamma/2)`;
- individual path/order postdiction from a two-class marker is
  `(1 + sin(gamma/2)) / k`;
- a perfect class record gives the ceiling `2/k`, not full path/order
  knowledge;
- global scalarizations fail the binary duality circle because a class
  partition is not a binary path marker.

This is an absorber verdict for T395's k >= 3 residue at the visibility /
branch-marker level. It is not a literature claim and does not prove that every
future Direction-A artifact is absorbed.

## Class

Executable negative audit / absorber screen. No claim promotion.

## Status

Implemented. Verdict: the T395 k >= 3 class-coarse record signature is
absorbed by generic multipath class-marker algebra in this finite audit.

## Target Claims

- [T395: Record-Order Trade-off Probe](T395-record-order-tradeoff-probe.md)
- [T394: Axis-Count Reconstruction Hierarchy](T394-axis-count-reconstruction-hierarchy.md) (guardrail for axis-count vs scalarization language)
- [T49: Reconstruction Without Background Time](T49-reconstruction-without-background-time.md) (lineage only; not upgraded)
- [C1](../claims/C1-experienced-time-as-record-finality.md) and [H1](../HYPOTHESES.md) (lineage only; not upgraded)

## Setup

`models/multipath_class_marker_absorber.py` is a standard-library finite
algebraic model.

The model declares branches `b_0 ... b_{k-1}` and a two-class partition. A
class marker couples to the class, not to the individual branch. For marker
strength `gamma`, the two pure class-marker states have overlap
`cos(gamma/2)`. Therefore the normalized pairwise coherence factor is:

```text
same class: 1
cross class: cos(gamma/2)
```

The individual path postdiction objective sees identical states inside each
class, so a perfect two-class record can identify only the class and then has
no within-class path information. For k equally likely branches:

```text
P_path(gamma) = (1 + sin(gamma/2)) / k
P_path(pi)    = 2/k
```

The canonical comparison maps:

```text
generic paths: p0, p1, p2 with {p0, p2} | {p1}
T395 labels:   ABC, BAC, CAB with {ABC, CAB} | {BAC}
```

The audit drops label names and compares only structural signatures.

## Success Criteria

- The generic three-path class marker and T395 three-order class record have
  identical structure-only signatures across the gamma sweep.
- Every checked k = 3..6 nontrivial bipartition satisfies within-class
  flatness, cross-class duality, and the postdiction formula.
- The same scalarization failures T395 reported appear in the generic
  multipath class-marker model.
- Full-resolution markers are kept separate as a positive control: a
  branch-level perfect record gives path postdiction 1 and kills all pairwise
  coherence.

## Failure Criteria

- Composition-order labels produce any signature not reproduced by the generic
  path-marker model under the same class partition and marker overlap.
- The `2/k` ceiling depends on order semantics rather than class-marker
  indistinguishability.
- The scalarization failures disappear in generic multipath markers.

## Known Physics Constraints

This artifact makes no process-matrix, platform, spacetime, or quantum
foundations claim. It is a finite branch-marker absorber model. Candidate
multibeam-duality literature remains unverified and is not cited as evidence.

## What This Does Not Earn

- No new temporal-order inequality.
- No causal-nonseparability witness.
- No claim-ledger update.
- No external-facing artifact.
- No conclusion about multi-holder finality, reversal cost, or D1-native
  record finality.

## Reproduction

```bash
python -m unittest tests.test_multipath_class_marker_absorber -v
python -m models.multipath_class_marker_absorber --write-artifacts
python -m json.tool results/T397-multipath-class-marker-absorber-v0.1.json
```

## Contribution Needed

Direction A should move to a structure not already present in generic
multipath class markers: a genuine causal-process witness, a multi-holder
finality/reversal-cost model, or another D1-native capability object.

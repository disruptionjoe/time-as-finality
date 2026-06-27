# T249: Larger T54/T126 Canonical Colimit

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T54: Finite Finality Descent Theorem](T54-finite-finality-descent-theorem.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T154: T54/T58-to-T126 Bridge](T154-t54-t58-t126-bridge.md)

## Central Question

Can the T154 blocker be closed at the finite-control level by building a
larger T54-native canonical observer colimit that reaches T126 above the
minimum event scale?

T154 showed that the actual T51/T52 colimits are real causal-set candidates,
but only at three and four events. T249 asks for the smallest meaningful next
step: a larger observer-descent construction whose quotient-union relation is
audited by T126 without promoting S1.

## Hypothesis Under Audit

A four-patch observer descent datum over a nine-event 3x3 product order can:

```text
T54 observer-local patches
  -> canonical quotient-union product order
  -> no observer-local phantom-gap residue
  -> T126 finite filter
```

The expected positive verdict is only `passes_filter_only`.

## Setup

T249 constructs four overlapping 2x2 observer patches:

- `NW`: `p00, p01, p10, p11`
- `NE`: `p01, p02, p11, p12`
- `SW`: `p10, p11, p20, p21`
- `SE`: `p11, p12, p21, p22`

Each event `pij` has:

- target record `rij`;
- source records from its immediate left and lower product-order predecessors;
- axis profile `(i, j)`.

The quotient-union transitive closure should reconstruct exactly:

```text
pij <= pkl iff i <= k and j <= l
```

## Success Criteria

- The T54 completion is `canonical`.
- The T54 theorem applies and has no condition failures.
- The global completion has nine events.
- The strict order equals the 3x3 product order.
- Each observer patch is a local suborder of the ambient order.
- No observer patch has an ambient/local gap.
- T126 reaches the manifold filter instead of stopping at `insufficient_scale`.
- The final T126 verdict is interpreted as filter-only.

## Failure Criteria

T249 fails if:

- quotient-union adds or omits product-order pairs;
- any local patch has a local/ambient order conflict;
- any local patch has an unresolved phantom gap;
- the witness remains below T126's scale floor;
- the result is read as a spacetime, manifold, metric, embedding, or continuum
  claim.

## Implementation Result

Status: implemented.

T249 adds an executable nine-event T54-native grid colimit in
`models/t249_larger_t54_t126_colimit.py`. The witness is canonical under T54,
has no local patch gap, reconstructs the 3x3 product order exactly, and reaches
T126 as `passes_filter_only`.

## Run Command

```bash
python -m unittest tests.test_t249_larger_t54_t126_colimit -v
python -m models.run_t249
```

## Boundary

T249 closes only the immediate finite-control blocker left by T154. It does
not apply a named causal-set dimension estimator, random sprinkling diagnostic,
locality test, faithful embedding theorem, or continuum-limit argument.

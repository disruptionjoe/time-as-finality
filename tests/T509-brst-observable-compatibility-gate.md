# T509: BRST Observable Compatibility Gate

## Target Claims

No claim-ledger target. This is a TaF-side quotient/readout admission gate for
the post-T508 BRST/cohomology burden.

## Setup

T508 made the BRST/exactness burden executable, but its Q-closed observable
discipline was still a packet field. T509 makes that field finite and
checkable.

The finite fixture keeps T508's nontrivial mirror class:

```text
Q(auxiliary) = physical_exact
mirror in ker(Q)
mirror not in im(Q)
```

It then asks whether the proposed recovery/readout pair is compatible with the
BRST quotient:

```text
operation descends through quotient
readout annihilates exact representative shifts
W+ representative leakage is not a cohomology observable
direct cohomology readout is review-only, not claim evidence
```

## Success Criteria

- T507-style full-Krein recovery is rejected when it recovers W+ differences
  only by failing to descend through the BRST quotient.
- A chain-map operation that creates W+ representative leakage is rejected when
  the W+ readout is not exact-invariant.
- A direct exact-invariant mirror-class readout is admitted only as a review
  target.
- An exact-mirror control routes to redundancy.
- Ordinary W+ readout, post-hoc readout selection, missing controls, claim /
  public-posture shortcuts, external-publication shortcuts, and cross-repo
  shortcuts are rejected or blocked.

## Failure Criteria

- Non-descending full-Krein recovery is accepted as BRST-compatible.
- W+ representative leakage is treated as a hidden physical record.
- A direct cohomology observable is treated as claim evidence.
- An exact mirror vector is treated as nontrivial hidden-record support.
- The result is used to decide real BRST exactness, real BRST nontriviality,
  Krein quantization, hidden mirror records, source-action truth, mass-gap
  evidence, public posture, claim status, or cross-repo truth.

## Known Physics Constraints

This is finite TaF review machinery. It does not establish a physical BRST
complex, physical operation algebra, physical observable algebra, real ghost
cohomology class, or physical inner product. A future physics-bearing packet
must supply those as evidence under repo governance.

## Contribution Needed

A future packet that wants more than review status must predeclare `Q`, the
quotient/cohomology object, operation algebra, and readout; prove the operation
descends through the quotient; prove the readout annihilates exact
representative shifts; include non-descending recovery, exact-representative
leakage, exact-mirror, and direct-cohomology controls; and keep direct
cohomology readout review-only until physics-side constraints are supplied.

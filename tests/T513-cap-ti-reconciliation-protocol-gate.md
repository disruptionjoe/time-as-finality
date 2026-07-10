# T513: Cap_TI Reconciliation Protocol Gate

## Target Claims

No claim-ledger target. This is a TaF-side finite protocol-grounding gate for
the Cap_TI Candidate C reconciliation-round capability.

## Setup

`open-problems/cap-ti-capability-object-spec.md` selected Candidate C as the
operative capability and left one technical burden open: ground the continuous
reconciliation cost formula in a formal protocol.

T513 makes that burden executable. A future Cap_TI packet must predeclare:

```text
Domain
Event count n
Observer records
Causal order
Entropy/accounting vector
Gluing topology
Branching exponent beta
Timing metric that beta reads
Finite reconciliation protocol
Reconciliation unit
Observer-pair schedule
Hierarchy capacity ceil(n^beta)
Integer round interpretation ceil(n^(1 - beta))
Positive control
Null control
Demotion condition
Verdict
```

## Success Criteria

- A protocol packet is admitted only as review material when beta, timing
  metric, observer-pair schedule, hierarchy capacity, reconciliation unit, and
  controls are all declared before the pair is scored.
- The finite packet maps the continuous formula `R(beta) = n^(1 - beta)` to
  integer protocol rounds `ceil(n^(1 - beta))`.
- A matched high-beta control requires fewer reconciliation rounds than a
  matched low-beta control.
- Same-beta null controls match.
- Formula-only, topology-only, post-hoc beta, hidden-timing, round-mismatch,
  claim/public-posture, external-publication, and cross-repo shortcuts are
  rejected, absorbed, or blocked.

## Failure Criteria

- T513 treats the continuous formula alone as a protocol.
- T513 treats gluing topology alone as a timing metric.
- T513 admits a beta selected after the witness pair or transcript.
- T513 admits hidden timing as a same-neighbor-data separator.
- T513 converts the protocol gate into Cap_TI promotion, H7 support, Temporal
  Issuance source truth, claim movement, public posture, external publication,
  or cross-repo truth movement.

## Known Physics Constraints

This is finite TaF review machinery. It does not establish a physical-substrate
theorem, thermodynamic arrow, Temporal Issuance source object, or cross-repo
support relation.

## Contribution Needed

A future packet that wants more than review status must supply a real
source-object contract and governed promotion path. T513 only says what a
protocol-grounded Cap_TI reconciliation packet must include before it can be
reviewed.

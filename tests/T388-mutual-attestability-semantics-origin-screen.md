# T388: Mutual-Attestability Semantics Origin Screen

## Target Claims

D1, R1, S1, PO1, and the T387 `mutual_attestability_semantics_origin`
open object:

```text
Does compatibility require mutual local attestability, or is mutuality still an
imported premise?
```

## Setup

Compare semantics for "compatible":

- raw predicate compatibility,
- symmetric-label compatibility,
- shared scalar-token compatibility,
- one-sided readout compatibility,
- global-reconciled compatibility,
- spoofed-receipt compatibility,
- asymmetric-persistence compatibility,
- finalizable shared-state compatibility.

## Success Criteria

- Show raw compatibility remains underdetermined.
- Reject scalar-token semantics as not finalizable shared record state.
- Treat symmetric labels as partial but insufficient.
- Reject one-sided readout.
- Reject global reconciliation and hidden foliation.
- Reject spoofed, replayed, unowned, or equivocal receipts.
- Treat asymmetric persistence as partial but not finalizable mutuality.
- Identify whether record-finality semantics force mutual local attestability.

## Failure Criteria

- Claim that raw compatibility alone derives mutuality.
- Let symmetric labels or scalar tokens count as endpoint-owned receipts.
- Let global reconciliation count as local mutual attestability.
- Ignore receipt authenticity or persistence.

## Known Constraints

This is a finite semantics screen. It derives mutual attestability only under
record-finalizable shared-state compatibility.

## Contribution Needed

If finalizable shared-state compatibility survives, the next open object moves
to the bridge from two protocol legs to null signal geometry.

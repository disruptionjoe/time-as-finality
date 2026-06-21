# Technical Report: T1 Record-Graph Admissibility Ledger v0.1

## Claim Under Test

T124 argued that H7 should not be read physically until a concrete record
substrate names the reverse edge for strict D1 increases. T141 performs that
check on the existing T1 causal-record graph.

## Artifact

T141 audits four T1 transformations:

- granting access to an already existing holder;
- copying a record into a fresh holder on the same causal chain;
- copying a record into a fresh holder on an additional incomparable branch;
- revoking access without erasure as a control.

For each case it computes the before/after T1 D1 profile
`(accessible_support, redundancy, branch_robustness, graph_reversal_cost)` and
classifies the reverse edge under the same holder, access, and erasure
accounting.

## Result

No tested strict T1 D1 increase has a constructor-impossible reverse.

The audited cases split cleanly:

- `access_grant_existing_record` is a strict D1 increase from `(1,1,1,0)` to
  `(2,2,1,1)`, but it is only an observer-boundary change. The reverse is an
  ordinary access revocation.
- `copy_to_fresh_holder` is a strict D1 increase from `(2,2,1,0)` to
  `(3,3,1,1)`, but the reverse is erasure or overwrite of the new copy with
  named fresh-holder and erasure accounting.
- `branch_spread_copy` is a strict D1 increase from `(2,2,1,1)` to
  `(3,3,2,2)`, but the reverse is again deletion of the added branch-support
  record under the same erasure ledger.
- `access_loss_without_erasure_control` is not a strict forward increase at
  all and stays fully reversible.

## Current Strongest Claim

On the explicit T1 record substrate, the surviving H7 content is weaker than a
constructor arrow. Record stabilization gains are either:

- reversible observer-boundary changes; or
- resource-accounted copy/erase operations.

That is enough to support careful bookkeeping about records. It is not enough
to ground a substrate-native impossibility of definalization.

## What This Improved

T141 moves the H7 blocker from abstract warning to concrete substrate audit.
A serious reader can now inspect actual T1 profile changes and ask whether any
future record substrate does better than copy-plus-erasure accounting.

## What This Weakened Or Falsified

This weakens the most optimistic T1-to-H7 reading. The current record graph is
not evidence that finality growth itself defines a physical arrow. Even when
support, redundancy, or branch robustness rise, the reverse remains either a
named reversible boundary change or a resource-consuming definalization move.

## Falsification Condition

T141 fails in H7's favor only if a T1-style record-graph transformation
produces a strict D1 increase whose reverse is constructor-impossible under
the same full holder, access, and erasure accounting.

## Claim Ledger Update

Add T141 to H7:

```text
The explicit T1 record substrate still does not ground constructor-impossible
definalization. Access grants are reversible boundary changes; holder and
branch-support gains require fresh-holder/erasure accounting; no tested strict
T1 increase has a constructor-impossible reverse.
```

## Open Blocker

The repo still lacks a record substrate where deleting or definalizing a
stabilized record is impossible for substrate-native reasons rather than
costly, omitted, or observer-boundary-relative.

## Next Work

Either:

- formalize a stronger substrate-native impossibility notion for T1-style
  records; or
- calibrate the surviving copy/erase edges directly against standard free
  energy and erasure accounting, so the project can say cleanly that the
  remaining arrow content is just thermodynamic bookkeeping.

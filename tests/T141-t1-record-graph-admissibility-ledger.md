# T141: T1 Record-Graph Admissibility Ledger

## Route

Thermodynamic arrow of time.

## Question

If H7 is grounded on an explicit T1-style causal-record graph rather than on
abstract arrow language, do any strict D1-increasing transformations acquire a
constructor-impossible reverse?

## Motivation

T124 left one concrete blocker: the repo still lacked a reverse-edge ledger on
an actual record substrate. The highest-value move is to test that blocker on
the simplest substrate already present in the project instead of introducing a
new toy arrow family.

## Setup

Use the executable T1 record graph and audit four transformations:

1. Access grant to an already existing holder.
2. Copy to a fresh holder on the same causal chain.
3. Copy to a fresh holder on an additional incomparable branch.
4. Access-loss control without erasure.

For each case, compute the before/after D1 profile and classify the reverse
edge under the same holder, access, and erasure accounting.

## Success Criteria

- At least one strict T1 D1 increase is audited on an explicit record graph.
- Every strict increase has a reverse-edge classification.
- The audit states clearly whether the reverse is reversible,
  resource-consuming, or constructor-impossible.
- The result sharpens H7 rather than rebranding ordinary record copies as a
  physical arrow.

## Failure Criteria

- Smuggling in omitted holders, hidden access state, or free erasure.
- Treating observer-boundary changes as thermodynamic irreversibility.
- Promoting copy-based record support increases to a constructor theorem
  without auditing definalization under the same substrate.

## Claim Impact

If all strict T1 increases are either reversible boundary changes or
resource-accounted copy/erase moves, then H7 should be narrowed again: the
current record substrate still lacks a constructor-impossible reverse for
record definalization.

## Reproduction

```bash
python -m unittest tests.test_t1_record_graph_admissibility_ledger -v
python -m models.t1_record_graph_admissibility_ledger
```

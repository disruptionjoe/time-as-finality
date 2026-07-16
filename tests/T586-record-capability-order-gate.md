# T586: Record-Capability Order Gate

## Target Claims

- A finite event order can be defined from executable task dependence on
  records produced by other events.
- The finite order is a strict partial order exactly when the produced-record
  dependency graph is acyclic and all required records are supplied.
- The resulting relation is not merely a clock-label order, entropy scalar,
  supplied causal-order superset, or irreversible-operation flag.

## Setup

Use the T585 one-bit Landauer memory fixture only as source-owned physical
capability input. The finite event set contains a seed known record, a stable
copy operation, an erase-to-standard-record operation, a final certificate,
and an independent biased-reference record.

Define event `A <_record B` when an executable task of `B` requires a record
whose unique producer is `A`. Compare the strict transitive closure with:

- arbitrary clock labels;
- event entropy ranks;
- a supplied causal-order superset; and
- the irreversible-operation flag.

## Success Criteria

- The main fixture's produced-record dependency closure is irreflexive,
  transitive, and antisymmetric.
- The independent biased-reference event remains incomparable with the main
  chain.
- A mutual-record-dependency fixture is rejected as circular.
- Clock-label permutation, entropy ranks, causal-overread, and irreversibility
  controls do not reproduce the record-capability order.

## Failure Criteria

- The order requires clock labels, entropy values, ordinary causal labels, or
  irreversible-operation labels.
- A record-dependency cycle is accepted.
- A missing required record is ignored.
- The fixture is used to claim physical time, temporal issuance, a universal
  capability measure, or claim-ledger movement.

## Contribution Needed

Run `python -m models.t586_record_capability_order_gate --write-results` and
the focused unit test before treating T586 as a review-only endpoint for the
record-capability-order burden.

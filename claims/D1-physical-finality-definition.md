# D1: Physical Finality Definition

## Claim

Physical finality is a comparative, observer-indexed schema over record
properties, not one universal physical quantity. The v0.1 preorder compares
accessible support, holder redundancy, independent branch support, and a
named reversal cost componentwise, but each dimension must be justified for
the substrate in which it is used.

## Class

Definition.

## Status

Weakened.

## What This Does Not Claim

- Finality is not absolute metaphysical impossibility.
- Finality is not a magic moment in time.
- Finality is not social agreement.
- The four graph quantities are not claimed to be a complete physical measure.
- Graph reversal count is not thermodynamic work.
- The four dimensions do not automatically emerge as independent quantities
  from local dynamics.

## Why It Might Be True

Classical records can differ by redundancy, accessibility, causal
independence, and reversal cost. Keeping these dimensions separate prevents a
weighted scalar from hiding disagreement. The Emergence Laboratory shows that
access and branch structure can remain distinct, while raw binary support,
redundancy, and terminal intervention cost collapse to one Hamming count.

## How It Could Fail

- The dimensions are insufficient, redundant, or not physically meaningful.
- The graph definitions fail to survive a physics-grounded model.
- Finality becomes too broad and merely renames entropy, decoherence, or information.
- Observer-indexing contributes no useful distinction beyond bounded access.
- A proposed dimension is only a re-description of another dimension in every
  implementation.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)
- [T17: Consensus Finality Crosswalk](../tests/T17-consensus-finality-crosswalk.md)
- [T20: Consensus-Record Theorem Transfer](../tests/T20-consensus-record-theorem-transfer.md)
- [T21: Bell Contextuality Finality](../tests/T21-bell-contextuality-finality.md)

## Contribution Needed

Build a dynamical observer-system and test which dimensions remain distinct
when storage, reconciliation, and action arise inside the model.

## Formal Definition

See [FORMALISM.md](../FORMALISM.md) and the executable implementation in
[`models/t1_record_graph.py`](../models/t1_record_graph.py).

## Emergence Laboratory Result

[T9](../tests/T9-emergence-laboratory.md) shows that counterfactual record
traces and observer-relative access work on reversible and irreversible local
dynamics. It also shows that logical information loss is neither necessary
nor sufficient for an observer-accessible trace, and that three raw profile
dimensions collapse in the simplest binary model.

## Consensus Finality Crosswalk Result

[T17](../tests/T17-consensus-finality-crosswalk.md) shows that distributed
finality definitions collapse or project D1 dimensions. Safety ignores
independent branch support, economic finality keeps only reversal cost, and
liveness is a protocol progress condition rather than a D1 dimension.

The bounded theorem check verifies that no admissible configuration in the
stated finite model jointly maximizes support, redundancy, branch support,
reversal cost, and bounded progress. This strengthens D1's reason to keep
dimensions separate: scalar "more final" language would hide the tradeoff.

## Consensus-Record Theorem Transfer Result

[T20](../tests/T20-consensus-record-theorem-transfer.md) gives holder
redundancy a theorem-bearing role. Redundant-holder overlap is the
physical-record analogue of quorum intersection: when `2q > n`, incompatible
certificates must share a holder, and local consistency blocks contradictory
finalization.

This supports D1's holder-redundancy dimension while preserving the caveat
that global-section existence requires T13/sheaf structure beyond quorum
safety.

## Bell Contextuality Finality Result

[T21](../tests/T21-bell-contextuality-finality.md) shows why D1 finality must
remain observer- and context-indexed. Local measurement contexts can each have
valid finality sections while no single global assignment exists. That makes
global-section existence a separate condition, not something guaranteed by
local support or redundancy alone.

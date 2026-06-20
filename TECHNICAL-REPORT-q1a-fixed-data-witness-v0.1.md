# Technical Report: Q1A Fixed-Data Witness v0.1

## Claim Under Test

T102 left Q1A with one live gate. It must produce a fixed-data witness: keep
decoherence/pointer-basis evidence, fragment-information summaries, accessible
raw redundancy, and ordinary branch/history availability fixed while the D1
verdict changes only through access-boundary or independence structure.

## Artifact

T103 adds an executable finite witness over already formed records.

The positive pair is:

- `independent_records_fixed_data`;
- `copied_archive_fixed_data`.

Both have the same standard quantum-side signature:

```text
pointer basis: computational_z
reduced pointer coherence: 0.0
fragment mutual information: E1 = E2 = E3 = 1.0 bit
accessible raw redundancy: 3
ordinary branch/history availability: z0_history, z1_history
```

They differ only in the independence partition. In the independent case,
`E1`, `E2`, and `E3` are three independent provenance classes. In the copied
case, `E3` is a copied archive of `E1`, leaving only two independent classes.

T103 also adds three negative controls. The gate rejects cases that change
reduced coherence, accessible raw redundancy, or ordinary branch/history
availability.

## Result

The internal fixed-data witness exists:

```text
independent_records_fixed_data -> finalized
copied_archive_fixed_data      -> not_finalized
```

The difference is not caused by decoherence, raw environmental redundancy, or
branch/history availability. It is caused only by the record-independence
partition.

A hidden-partition case with the same quantum-side data withholds D1 rather
than inferring finality from raw redundancy.

## Current Strongest Claim

Q1A now has an internal fixed-data witness. The same decoherence, fragment
information, accessible raw redundancy, and ordinary branch/history
availability can yield different D1 verdicts when only the independence
partition changes.

This is not a new measurement theory. It is an access/provenance accounting
predicate over already formed records.

## What This Improved

T103 turns the T102 blocker into an executable gate with positive and negative
controls. A future Q1A proposal can no longer claim the fixed-data distinction
while changing coherence, redundancy, or branch/history data.

## What This Weakened Or Falsified

This weakens the physics reading of Q1A. The surviving delta is carried by an
independence/provenance predicate. If decoherence, Quantum Darwinism,
consistent histories, RQM, QBism, or Everettian accounts can adopt that same
predicate without changing their physics, Q1A collapses to bookkeeping.

## Falsification Condition

Demote Q1A if every fixed-data D1 change requires adding a provenance or
independence partition that neighboring frameworks can adopt without changing
their physics, or if no physically auditable procedure fixes the partition
before D1 scoring.

## Claim Ledger Update

Q1A should be updated as follows:

```text
T103 supplies an internal fixed-data witness: the same decoherence,
fragment-information, raw-redundancy, and branch/history summaries can yield
finalized versus not_finalized D1 verdicts when only the independence partition
changes. This upgrades Q1A only to conditional record-accounting support;
external distinctness remains unearned if the partition is ordinary provenance
bookkeeping.
```

## Open Blocker

The independence partition is still fixture-declared. The next blocker is a
physically auditable derivation of record independence fixed before D1 scoring.

## Next Work

Derive the T103 independence partition from event-level detector or
environment-fragment provenance, then test whether Quantum Darwinism with
provenance-aware fragment partitioning already absorbs the same verdict.

## Reproduction

```bash
python -m unittest tests.test_q1a_fixed_data_witness -v
python -m models.run_t103
```
